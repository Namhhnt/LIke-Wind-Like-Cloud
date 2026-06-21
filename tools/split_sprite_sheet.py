from __future__ import annotations


import argparse
import re
from collections import deque
from dataclasses import dataclass
from pathlib import Path

from PIL import Image


DEFAULT_EXPRESSIONS = [
    "neutral",      # bình thường
    "smile",        # cười mỉm
    "happy",        # vui
    "laugh",        # cười to

    "sad",          # buồn
    "teary",        # khóc nhẹ
    "cry",          # khóc to
    "shy",          # e thẹn

    "embarrassed",  # bối rối
    "confused",     # khó hiểu / lúng túng
    "surprised",    # ngạc nhiên
    "shocked",      # sửng sốt

    "dazed",        # ngái ngủ, choáng
    "thoughtful",   # lo lắng, trầm tư
    "pouty",        # phụng phịu / dỗi
    "serious",      # nghiêm túc
]

SHEET_FILENAME_RE = re.compile(
    r"^(?P<char>.+?)_expression_sheet(?P<version>_\d+)?\.(?P<ext>png|webp|jpg|jpeg)$",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class SheetJob:
    char_name: str
    sheet_path: Path
    output_dir: Path
    version_digits: str


def find_project_root() -> Path:
    """
    Prefer running from project root.
    If not, infer root as parent of /tools.
    """
    cwd = Path.cwd()

    if (cwd / "game").exists():
        return cwd

    script_path = Path(__file__).resolve()
    if script_path.parent.name == "tools":
        return script_path.parent.parent

    return cwd


def parse_sheet_filename(input_path: Path) -> tuple[str | None, str]:
    match = SHEET_FILENAME_RE.match(input_path.name)
    if not match:
        return None, ""

    version_token = match.group("version") or ""
    return match.group("char"), version_token.removeprefix("_")


def infer_char_name_from_input(input_path: Path) -> str | None:
    char_name, _ = parse_sheet_filename(input_path)
    return char_name


def characters_root(project_root: Path) -> Path:
    return project_root / "game" / "images" / "characters"


def default_output_dir(project_root: Path, char_name: str) -> Path:
    return characters_root(project_root) / char_name / "expressions"


def collect_candidate_sheets(root: Path, char_name: str | None = None) -> list[Path]:
    candidates: list[Path] = []

    for path in root.iterdir() if root.exists() else []:
        if path.is_file():
            parsed_char, _ = parse_sheet_filename(path)
            if parsed_char and (char_name is None or parsed_char == char_name):
                candidates.append(path)
        elif path.is_dir():
            for nested in path.iterdir():
                if not nested.is_file():
                    continue

                parsed_char, _ = parse_sheet_filename(nested)
                if parsed_char and (char_name is None or parsed_char == char_name):
                    candidates.append(nested)

    return candidates


def choose_sheet_for_character(project_root: Path, char_name: str) -> tuple[Path, str]:
    root = characters_root(project_root)
    candidates = collect_candidate_sheets(root, char_name=char_name)
    if not candidates:
        raise FileNotFoundError(
            "Sprite sheet not found for character "
            f"'{char_name}'. Checked both game/images/characters/ and "
            f"game/images/characters/{char_name}/"
        )

    nested_dir = root / char_name

    def sort_key(path: Path) -> tuple[int, int, int]:
        _, version_digits = parse_sheet_filename(path)
        version_value = int(version_digits) if version_digits else -1
        is_nested = 0 if path.parent == nested_dir else 1
        has_version = 1 if version_digits else 0
        if has_version:
            version_rank = -version_value
        else:
            version_rank = -1
        return has_version, is_nested, version_rank

    selected = sorted(candidates, key=sort_key)[0]
    _, version_digits = parse_sheet_filename(selected)
    return selected, version_digits


def discover_sheet_jobs(project_root: Path, output_dir: str | None) -> list[SheetJob]:
    if output_dir:
        raise ValueError(
            "--output can only be used when splitting a single sheet. "
            "Provide --input or char_name as well."
        )

    root = characters_root(project_root)
    candidates = collect_candidate_sheets(root)
    if not candidates:
        raise FileNotFoundError(
            f"No sprite sheets matching '*_expression_sheet*.png' were found under {root}"
        )

    jobs_by_key: dict[tuple[str, str], SheetJob] = {}

    for candidate in candidates:
        char_name, version_digits = parse_sheet_filename(candidate)
        if not char_name:
            continue

        job = SheetJob(
            char_name=char_name,
            sheet_path=candidate.resolve(),
            output_dir=default_output_dir(project_root, char_name),
            version_digits=version_digits,
        )
        key = (char_name, version_digits)
        existing = jobs_by_key.get(key)

        if existing is None:
            jobs_by_key[key] = job
            continue

        existing_nested = existing.sheet_path.parent.name == char_name
        candidate_nested = candidate.parent.name == char_name
        if candidate_nested and not existing_nested:
            jobs_by_key[key] = job

    return sorted(jobs_by_key.values(), key=lambda job: (job.char_name, job.version_digits))


def resolve_jobs(
    char_name: str | None,
    input_path: str | None,
    output_dir: str | None,
    project_root: Path,
) -> list[SheetJob]:
    if input_path:
        sheet_path = Path(input_path).expanduser().resolve()
        inferred_char, version_digits = parse_sheet_filename(sheet_path)
        resolved_char_name = char_name or inferred_char or "tam"
        resolved_output_dir = (
            Path(output_dir).expanduser().resolve()
            if output_dir
            else default_output_dir(project_root, resolved_char_name)
        )
        return [
            SheetJob(
                char_name=resolved_char_name,
                sheet_path=sheet_path,
                output_dir=resolved_output_dir,
                version_digits=version_digits,
            )
        ]

    if char_name:
        sheet_path, version_digits = choose_sheet_for_character(project_root, char_name)
        resolved_output_dir = (
            Path(output_dir).expanduser().resolve()
            if output_dir
            else default_output_dir(project_root, char_name)
        )
        return [
            SheetJob(
                char_name=char_name,
                sheet_path=sheet_path.resolve(),
                output_dir=resolved_output_dir,
                version_digits=version_digits,
            )
        ]

    return discover_sheet_jobs(project_root, output_dir)


def remove_connected_black_background(
    image: Image.Image,
    threshold: int = 28,
) -> Image.Image:
    """
    Convert black background connected to image borders into transparency.

    Safer than deleting all black pixels because it preserves dark hair,
    dark eyes, and inner shadows.
    """

    img = image.convert("RGBA")
    width, height = img.size
    pixels = img.load()

    visited = [[False for _ in range(width)] for _ in range(height)]
    queue = deque()

    def is_blackish(x: int, y: int) -> bool:
        r, g, b, a = pixels[x, y]
        return a > 0 and r <= threshold and g <= threshold and b <= threshold

    def push_if_background(x: int, y: int) -> None:
        if 0 <= x < width and 0 <= y < height and not visited[y][x] and is_blackish(x, y):
            visited[y][x] = True
            queue.append((x, y))

    corner_span = max(1, min(3, width // 4, height // 4))
    corner_x_ranges = (range(corner_span), range(max(0, width - corner_span), width))
    corner_y_ranges = (range(corner_span), range(max(0, height - corner_span), height))

    for xs in corner_x_ranges:
        for ys in corner_y_ranges:
            for x in xs:
                for y in ys:
                    push_if_background(x, y)

    while queue:
        x, y = queue.popleft()

        r, g, b, a = pixels[x, y]
        pixels[x, y] = (r, g, b, 0)

        push_if_background(x + 1, y)
        push_if_background(x - 1, y)
        push_if_background(x, y + 1)
        push_if_background(x, y - 1)

    return img


def trim_transparent_area(image: Image.Image) -> Image.Image:
    bbox = image.getbbox()
    if bbox is None:
        return image

    return image.crop(bbox)


def fit_to_canvas(
    image: Image.Image,
    target_size: int = 256,
    bottom_align: bool = True,
) -> Image.Image:
    img = image.convert("RGBA")
    width, height = img.size

    scale = min(target_size / width, target_size / height)

    new_width = max(1, int(width * scale))
    new_height = max(1, int(height * scale))

    img = img.resize((new_width, new_height), Image.LANCZOS)

    canvas = Image.new("RGBA", (target_size, target_size), (0, 0, 0, 0))

    x = (target_size - new_width) // 2
    y = target_size - new_height if bottom_align else (target_size - new_height) // 2

    canvas.paste(img, (x, y), img)
    return canvas


def build_expression_name(expression: str, version_digits: str) -> str:
    return f"{expression}{version_digits}" if version_digits else expression


def split_sheet(
    sheet_path: Path,
    output_dir: Path,
    char_name: str,
    expressions: list[str],
    cols: int,
    rows: int,
    target_size: int,
    threshold: int,
    transparent_bg: bool,
    version_digits: str,
) -> None:
    if not sheet_path.exists():
        raise FileNotFoundError(f"Sprite sheet not found: {sheet_path}")

    expected_cells = cols * rows
    if len(expressions) != expected_cells:
        raise ValueError(
            f"Expression count mismatch. Got {len(expressions)} expressions, "
            f"but grid is {cols}x{rows} = {expected_cells}."
        )

    output_dir.mkdir(parents=True, exist_ok=True)

    sheet = Image.open(sheet_path).convert("RGBA")
    sheet_width, sheet_height = sheet.size

    cell_width = sheet_width / cols
    cell_height = sheet_height / rows

    print(f"Input:   {sheet_path}")
    print(f"Output:  {output_dir}")
    print(f"Grid:    {cols}x{rows}")
    print(f"Cell:    approx {cell_width:.2f}x{cell_height:.2f}")
    print(f"Target:  {target_size}x{target_size}")
    print(f"Version: {version_digits or '(base)'}")
    print(f"Transparent BG: {transparent_bg}")
    print()

    for index, expression in enumerate(expressions):
        row = index // cols
        col = index % cols

        left = round(col * cell_width)
        upper = round(row * cell_height)
        right = round((col + 1) * cell_width)
        lower = round((row + 1) * cell_height)

        cell = sheet.crop((left, upper, right, lower))
        if transparent_bg:
            cell = remove_connected_black_background(cell, threshold=threshold)
            cell = trim_transparent_area(cell)
        cell = fit_to_canvas(cell, target_size=target_size, bottom_align=True)

        expression_name = build_expression_name(expression, version_digits)
        output_path = output_dir / f"{char_name}_{expression_name}.png"
        cell.save(output_path)

        print(f"Saved:   {output_path}")


def split_expression_variant(expression_name: str) -> tuple[str, str]:
    for expression in sorted(DEFAULT_EXPRESSIONS, key=len, reverse=True):
        if expression_name == expression:
            return expression, ""
        if expression_name.startswith(expression):
            suffix = expression_name[len(expression):]
            if suffix.isdigit():
                return expression, suffix

    return expression_name, ""


def to_renpy_image_path(project_root: Path, image_path: Path) -> str:
    images_root = project_root / "game" / "images"
    try:
        return image_path.relative_to(images_root).as_posix()
    except ValueError:
        return image_path.as_posix()


def write_sprite_script(project_root: Path, char_name: str, output_dir: Path) -> Path:
    sprite_files = sorted(output_dir.glob(f"{char_name}_*.png"))
    if not sprite_files:
        raise FileNotFoundError(
            f"No generated sprites found for '{char_name}' in {output_dir}"
        )

    sprite_entries: list[tuple[str, str, str]] = []
    prefix = f"{char_name}_"

    for sprite_file in sprite_files:
        stem = sprite_file.stem
        if not stem.startswith(prefix):
            continue
        expression_name = stem[len(prefix):]
        base_expression, version_digits = split_expression_variant(expression_name)
        sprite_entries.append((base_expression, version_digits, expression_name))

    order_map = {name: index for index, name in enumerate(DEFAULT_EXPRESSIONS)}
    sprite_entries.sort(
        key=lambda item: (
            order_map.get(item[0], len(DEFAULT_EXPRESSIONS)),
            item[0],
            int(item[1]) if item[1] else 0,
            item[2],
        )
    )

    lines = [
        "# Generated by tools/split_sprite_sheet.py",
        "# Keep character definitions elsewhere; this file only declares side images.",
        "",
    ]

    for _, _, expression_name in sprite_entries:
        image_path = output_dir / f"{char_name}_{expression_name}.png"
        renpy_path = to_renpy_image_path(project_root, image_path)
        lines.append(
            f'image side {char_name} {expression_name} = "{renpy_path}"'
        )

    lines.append("")

    scripts_dir = project_root / "game" / "scripts"
    scripts_dir.mkdir(parents=True, exist_ok=True)

    script_path = scripts_dir / f"{char_name}_sprites.rpy"
    script_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Sprites:  {script_path}")
    return script_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Split character expression sprite sheets into transparent PNGs and update Ren'Py sprite declarations."
    )

    parser.add_argument(
        "char_name",
        nargs="?",
        default=None,
        help=(
            "Character name. If omitted, it is inferred from --input. "
            "If both are omitted, all matching sheets under game/images/characters/ are processed."
        ),
    )

    parser.add_argument(
        "-i",
        "--input",
        default=None,
        help=(
            "Full path to an input sprite sheet. Filenames like "
            "[char-name]_expression_sheet[_NN].png are auto-parsed."
        ),
    )

    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="Output directory for a single split run. Defaults to game/images/characters/[char_name]/expressions",
    )

    parser.add_argument(
        "--project-root",
        default=None,
        help="Project root containing the game/ folder. If omitted, auto-detected.",
    )

    parser.add_argument(
        "--cols",
        type=int,
        default=4,
        help="Number of columns in sprite sheet. Default: 4",
    )

    parser.add_argument(
        "--rows",
        type=int,
        default=4,
        help="Number of rows in sprite sheet. Default: 4",
    )

    parser.add_argument(
        "--size",
        type=int,
        default=256,
        help="Output sprite size. Default: 256",
    )

    parser.add_argument(
        "--threshold",
        type=int,
        default=28,
        help="Black background removal threshold. Default: 28",
    )

    parser.add_argument(
        "--transparent-bg",
        action="store_true",
        default=False,
        help="Remove black background connected to the image corners. Disabled by default.",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    project_root = (
        Path(args.project_root).expanduser().resolve()
        if args.project_root
        else find_project_root()
    )

    jobs = resolve_jobs(
        char_name=args.char_name,
        input_path=args.input,
        output_dir=args.output,
        project_root=project_root,
    )

    for job in jobs:
        split_sheet(
            sheet_path=job.sheet_path,
            output_dir=job.output_dir,
            char_name=job.char_name,
            expressions=DEFAULT_EXPRESSIONS,
            cols=args.cols,
            rows=args.rows,
            target_size=args.size,
            threshold=args.threshold,
            transparent_bg=args.transparent_bg,
            version_digits=job.version_digits,
        )
        write_sprite_script(project_root, job.char_name, job.output_dir)
        print()


if __name__ == "__main__":
    main()
