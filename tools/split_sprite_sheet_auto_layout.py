from __future__ import annotations

import argparse
import re
from collections import deque
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


DEFAULT_EXPRESSIONS = [
    "neutral",      # bình thường
    "smile",        # cười mỉm
    "happy",        # vui
    "laughing",     # cười to

    "shy",          # e thẹn
    "embarrassed",  # bối rối / ngượng
    "teasing",      # trêu chọc
    "surprised",    # ngạc nhiên

    "sad",          # buồn
    "teary",        # rưng rưng
    "hurt",         # tổn thương
    "lonely",       # cô đơn

    "angry",        # tức giận
    "irritated",    # khó chịu
    "confused",     # khó hiểu / lúng túng
    "tired",        # mệt mỏi
]

DEFAULT_EXPRESSIONS_5X5 = [
    "neutral",      # bình thường
    "smile",        # cười mỉm
    "happy",        # vui
    "grinning",     # cười rạng rỡ
    "laughing",     # cười to

    "shy",          # e thẹn
    "embarrassed",  # bối rối / ngượng
    "flustered",    # luống cuống
    "bashful",      # thẹn thùng
    "teasing",      # trêu chọc

    "sad",          # buồn
    "melancholic",  # u buồn
    "teary",        # rưng rưng
    "crying",       # khóc
    "hurt",         # tổn thương

    "angry",        # tức giận
    "irritated",    # khó chịu
    "frustrated",   # bực bội
    "disgusted",    # ghét bỏ / ghê tởm
    "contemptuous", # khinh thường

    "surprised",    # ngạc nhiên
    "shocked",      # sửng sốt
    "confused",     # khó hiểu / lúng túng
    "bored",        # chán
    "tired",        # mệt mỏi
]


SHEET_FILENAME_RE = re.compile(
    r"^(?P<char>.+?)_expression_sheet(?P<suffix>[^.]*)?\.(?P<ext>png|webp|jpg|jpeg)$",
    re.IGNORECASE,
)

GRID_TOKEN_5X5_RE = re.compile(r"(?<!\d)5x5(?!\d)", re.IGNORECASE)
GRID_TOKEN_4X4_RE = re.compile(r"(?<!\d)4x4(?!\d)", re.IGNORECASE)


@dataclass(frozen=True)
class SheetJob:
    char_name: str
    sheet_path: Path
    output_dir: Path
    version_digits: str


@dataclass(frozen=True)
class SheetLayout:
    name: str
    cols: int
    rows: int
    expressions: list[str]


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
    """
    Parse sprite sheet filename.

    Supported examples:
    - tam_expression_sheet.png
    - tam_expression_sheet_01.png
    - tam_expression_sheet_4x4.png
    - tam_expression_sheet_5x5.png
    - tam_expression_sheet_5x5_01.png
    - tam_expression_sheet_01_5x5.png

    Returns:
    - char name
    - version digits, if any
    """
    match = SHEET_FILENAME_RE.match(input_path.name)
    if not match:
        return None, ""

    suffix = match.group("suffix") or ""
    suffix_tokens = [token for token in suffix.split("_") if token]
    version_digits = next(
        (token for token in reversed(suffix_tokens) if token.isdigit()),
        "",
    )

    return match.group("char"), version_digits


def infer_char_name_from_input(input_path: Path) -> str | None:
    char_name, _ = parse_sheet_filename(input_path)
    return char_name


def infer_sheet_layout(
    sheet_path: Path,
    cols_override: int | None = None,
    rows_override: int | None = None,
) -> SheetLayout:
    """
    Infer sprite sheet layout from filename.

    Naming rule:
    - filenames containing `5x5` use the 25-expression sheet.
    - filenames containing `4x4`, or no grid token, use the default 16-expression sheet.

    `--cols` and `--rows` remain available as manual overrides.
    When either override is used, the final grid must still match one of the
    supported expression sets.
    """
    filename = sheet_path.name
    is_5x5 = GRID_TOKEN_5X5_RE.search(filename) is not None

    default_cols = 5 if is_5x5 else 4
    default_rows = 5 if is_5x5 else 4

    cols = cols_override if cols_override is not None else default_cols
    rows = rows_override if rows_override is not None else default_rows
    cell_count = cols * rows

    if cell_count == len(DEFAULT_EXPRESSIONS_5X5):
        return SheetLayout(
            name="5x5",
            cols=cols,
            rows=rows,
            expressions=DEFAULT_EXPRESSIONS_5X5,
        )

    if cell_count == len(DEFAULT_EXPRESSIONS):
        return SheetLayout(
            name="4x4",
            cols=cols,
            rows=rows,
            expressions=DEFAULT_EXPRESSIONS,
        )

    raise ValueError(
        f"Unsupported sprite sheet grid for {sheet_path.name}: {cols}x{rows} "
        f"= {cell_count} cells. Supported layouts are 4x4 "
        f"({len(DEFAULT_EXPRESSIONS)} expressions) and 5x5 "
        f"({len(DEFAULT_EXPRESSIONS_5X5)} expressions)."
    )


def build_expression_order(primary_expressions: list[str] | None = None) -> list[str]:
    ordered: list[str] = []
    seen: set[str] = set()

    for expression_list in (
        primary_expressions or [],
        DEFAULT_EXPRESSIONS,
        DEFAULT_EXPRESSIONS_5X5,
    ):
        for expression in expression_list:
            if expression not in seen:
                ordered.append(expression)
                seen.add(expression)

    return ordered


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
    queue = []

    def is_blackish(x: int, y: int) -> bool:
        r, g, b, a = pixels[x, y]
        return a > 0 and r <= threshold and g <= threshold and b <= threshold

    def push_if_background(x: int, y: int) -> None:
        if (
            0 <= x < width
            and 0 <= y < height
            and not visited[y][x]
            and is_blackish(x, y)
        ):
            visited[y][x] = True
            queue.append((x, y))

    corner_span = max(1, min(3, width // 4, height // 4))
    corner_x_ranges = (
        range(corner_span),
        range(max(0, width - corner_span), width),
    )
    corner_y_ranges = (
        range(corner_span),
        range(max(0, height - corner_span), height),
    )

    for xs in corner_x_ranges:
        for ys in corner_y_ranges:
            for x in xs:
                for y in ys:
                    push_if_background(x, y)

    while queue:
        x, y = queue.pop(0)

        r, g, b, a = pixels[x, y]
        pixels[x, y] = (r, g, b, 0)

        push_if_background(x + 1, y)
        push_if_background(x - 1, y)
        push_if_background(x, y + 1)
        push_if_background(x, y - 1)

    return img


def normalize_sheet_size(
    sheet: Image.Image,
    cols: int,
    rows: int,
    target_size: int,
    enabled: bool = True,
) -> tuple[Image.Image, tuple[int, int], tuple[int, int], bool]:
    """
    Resize the full sprite sheet to canonical grid size before splitting.

    Default target:
    - 4x4 with 256px cells => 1024x1024
    - 5x5 with 256px cells => 1280x1280

    If --size changes, canonical size becomes:
    - width  = cols * target_size
    - height = rows * target_size
    """
    original_size = sheet.size
    canonical_size = (cols * target_size, rows * target_size)

    if not enabled:
        return sheet, original_size, canonical_size, False

    if original_size == canonical_size:
        return sheet, original_size, canonical_size, False

    resized = sheet.resize(canonical_size, Image.LANCZOS)
    return resized, original_size, canonical_size, True


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
    normalize_sheet: bool,
    crop_padding: int = 0,
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

    sheet, original_size, canonical_size, did_resize = normalize_sheet_size(
        sheet=sheet,
        cols=cols,
        rows=rows,
        target_size=target_size,
        enabled=normalize_sheet,
    )

    expected_sheet_size = (cols * target_size, rows * target_size)
    if normalize_sheet and sheet.size != expected_sheet_size:
        raise RuntimeError(
            f"Normalized sheet size mismatch. Expected {expected_sheet_size}, got {sheet.size}."
        )

    sheet_width, sheet_height = sheet.size

    print(f"Input:   {sheet_path}")
    print(f"Output:  {output_dir}")
    print(f"Grid:    {cols}x{rows}")
    print(f"Cells:   {expected_cells}")
    print(f"Sheet:   {original_size[0]}x{original_size[1]}")
    print(f"Canon:   {canonical_size[0]}x{canonical_size[1]}")
    print(f"Actual:  {sheet_width}x{sheet_height}")
    print(f"Resize:  {'yes' if did_resize else 'no'}")
    final_size = target_size - crop_padding * 2 if crop_padding > 0 else target_size
    print(f"Cell:    exact {target_size}x{target_size}")
    print(f"Target:  {target_size}x{target_size}")
    print(f"Crop:    {crop_padding}px" if crop_padding > 0 else "Crop:    none")
    print(f"Result:  {final_size}x{final_size}")
    print(f"Version: {version_digits or '(base)'}")
    print(f"Transparent BG: {transparent_bg}")
    print()

    for index, expression in enumerate(expressions):
        row = index // cols
        col = index % cols

        left = col * target_size
        upper = row * target_size
        right = left + target_size
        lower = upper + target_size

        cell = sheet.crop((left, upper, right, lower))

        if cell.size != (target_size, target_size):
            raise RuntimeError(
                f"Unexpected cell size at row={row}, col={col}. "
                f"Expected {(target_size, target_size)}, got {cell.size}."
            )

        if transparent_bg:
            # Keep fixed canvas size, do not trim/further fit.
            cell = remove_connected_black_background(cell, threshold=threshold)

        if crop_padding > 0:
            cell = cell.crop((
                crop_padding,
                crop_padding,
                cell.width - crop_padding,
                cell.height - crop_padding,
            ))

        expression_name = build_expression_name(expression, version_digits)
        output_path = output_dir / f"{char_name}_{expression_name}.png"
        cell.save(output_path)

        print(f"Saved:   {output_path}")


def split_expression_variant(
    expression_name: str,
    known_expressions: list[str] | None = None,
) -> tuple[str, str]:
    expressions = build_expression_order(known_expressions)

    for expression in sorted(expressions, key=len, reverse=True):
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


def write_sprite_script(
    project_root: Path,
    char_name: str,
    output_dir: Path,
    expression_order: list[str] | None = None,
) -> Path:
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

        base_expression, version_digits = split_expression_variant(
            expression_name,
            known_expressions=expression_order,
        )

        sprite_entries.append((base_expression, version_digits, expression_name))

    ordered_expressions = build_expression_order(expression_order)
    order_map = {name: index for index, name in enumerate(ordered_expressions)}

    sprite_entries.sort(
        key=lambda item: (
            order_map.get(item[0], len(ordered_expressions)),
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
        lines.append(f'image side {char_name} {expression_name} = "{renpy_path}"')

    lines.append("")

    scripts_dir = project_root / "game" / "scripts"
    scripts_dir.mkdir(parents=True, exist_ok=True)

    script_path = scripts_dir / f"{char_name}_sprites.rpy"
    script_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"Sprites:  {script_path}")
    return script_path


def get_preview_output_path(
    sheet_path: Path,
    output_dir: Path,
    char_name: str,
    layout_name: str,
    version_digits: str,
    preview_output: str | None = None,
) -> Path:
    if preview_output:
        return Path(preview_output).expanduser().resolve()

    suffix = f"_{version_digits}" if version_digits else ""
    filename = f"{char_name}_expression_sheet_{layout_name}{suffix}_preview.png"

    # Put preview inside output_dir parent or output_dir itself
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir / filename


def load_preview_font(font_size: int = 16) -> ImageFont.ImageFont:
    candidates = [
        "arial.ttf",
        "Arial.ttf",
        "DejaVuSans.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/Library/Fonts/Arial.ttf",
        "C:/Windows/Fonts/arial.ttf",
    ]

    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, font_size)
        except Exception:
            continue

    return ImageFont.load_default()


def draw_text_label(
    draw: ImageDraw.ImageDraw,
    text: str,
    box: tuple[int, int, int, int],
    font: ImageFont.ImageFont,
) -> None:
    left, top, right, bottom = box

    try:
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
    except Exception:
        text_width, text_height = draw.textsize(text, font=font)

    padding_x = 8
    padding_y = 4
    label_height = text_height + padding_y * 2
    label_width = min((right - left) - 8, text_width + padding_x * 2)

    bg_left = left + 4
    bg_top = top + 4
    bg_right = bg_left + label_width
    bg_bottom = bg_top + label_height

    draw.rectangle(
        (bg_left, bg_top, bg_right, bg_bottom),
        fill=(0, 0, 0, 180),
        outline=(255, 255, 255, 180),
        width=1,
    )

    text_x = bg_left + padding_x
    text_y = bg_top + padding_y - 1

    draw.text(
        (text_x, text_y),
        text,
        font=font,
        fill=(255, 255, 255, 255),
    )


def render_dry_run_preview(
    sheet_path: Path,
    output_path: Path,
    char_name: str,
    expressions: list[str],
    cols: int,
    rows: int,
    target_size: int,
    version_digits: str,
    normalize_sheet: bool,
) -> Path:
    sheet = Image.open(sheet_path).convert("RGBA")

    sheet, original_size, canonical_size, did_resize = normalize_sheet_size(
        sheet=sheet,
        cols=cols,
        rows=rows,
        target_size=target_size,
        enabled=normalize_sheet,
    )

    expected_size = (cols * target_size, rows * target_size)
    if normalize_sheet and sheet.size != expected_size:
        raise RuntimeError(
            f"Normalized preview sheet size mismatch. Expected {expected_size}, got {sheet.size}."
        )

    preview = sheet.convert("RGBA").copy()
    draw = ImageDraw.Draw(preview, "RGBA")
    font = load_preview_font(font_size=max(14, target_size // 14))

    # Grid lines
    grid_color = (0, 255, 255, 220)
    border_color = (255, 80, 80, 235)

    # Outer border
    draw.rectangle(
        (0, 0, preview.width - 1, preview.height - 1),
        outline=border_color,
        width=3,
    )

    # Internal grid
    for col in range(1, cols):
        x = col * target_size
        draw.line((x, 0, x, preview.height), fill=grid_color, width=2)

    for row in range(1, rows):
        y = row * target_size
        draw.line((0, y, preview.width, y), fill=grid_color, width=2)

    # Per-cell border + label
    for index, expression in enumerate(expressions):
        row = index // cols
        col = index % cols

        left = col * target_size
        upper = row * target_size
        right = left + target_size
        lower = upper + target_size

        draw.rectangle(
            (left, upper, right - 1, lower - 1),
            outline=(255, 255, 255, 180),
            width=1,
        )

        expression_name = build_expression_name(expression, version_digits)
        draw_text_label(
            draw=draw,
            text=f"{index + 1:02d}. {expression_name}",
            box=(left, upper, right, lower),
            font=font,
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    preview.save(output_path)

    print(f"Dry-run preview saved: {output_path}")
    print(f"Sheet:   {original_size[0]}x{original_size[1]}")
    print(f"Canon:   {canonical_size[0]}x{canonical_size[1]}")
    print(f"Actual:  {preview.width}x{preview.height}")
    print(f"Resize:  {'yes' if did_resize else 'no'}")
    print(f"Grid:    {cols}x{rows}")
    print(f"Cell:    exact {target_size}x{target_size}")
    print()

    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Split character expression sprite sheets into transparent PNGs "
            "and update Ren'Py sprite declarations."
        )
    )

    parser.add_argument(
        "char_name",
        nargs="?",
        default=None,
        help=(
            "Character name. If omitted, it is inferred from --input. "
            "If both are omitted, all matching sheets under "
            "game/images/characters/ are processed."
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
        help=(
            "Output directory for a single split run. Defaults to "
            "game/images/characters/[char_name]/expressions"
        ),
    )

    parser.add_argument(
        "--project-root",
        default=None,
        help="Project root containing the game/ folder. If omitted, auto-detected.",
    )

    parser.add_argument(
        "--cols",
        type=int,
        default=None,
        help=(
            "Override number of columns in sprite sheet. "
            "If omitted, inferred from filename: 5x5 => 5, otherwise 4."
        ),
    )

    parser.add_argument(
        "--rows",
        type=int,
        default=None,
        help=(
            "Override number of rows in sprite sheet. "
            "If omitted, inferred from filename: 5x5 => 5, otherwise 4."
        ),
    )

    parser.add_argument(
        "--size",
        type=int,
        default=256,
        help=(
            "Output sprite cell size. Default: 256. "
            "Canonical sheet size is cols * size by rows * size."
        ),
    )

    parser.add_argument(
        "--threshold",
        type=int,
        default=28,
        help="Black background removal threshold. Default: 28",
    )

    parser.add_argument(
        "--crop-padding",
        type=int,
        default=4,
        help=(
            "Crop N pixels from each edge of every cell after splitting. "
            "Removes residues from neighboring cells. Default: 4. "
            "Set to 0 to disable."
        ),
    )

    parser.add_argument(
        "--transparent-bg",
        action="store_true",
        default=False,
        help=(
            "Remove black background connected to the image corners. "
            "Disabled by default."
        ),
    )

    parser.add_argument(
        "--no-normalize-sheet",
        action="store_true",
        default=False,
        help=(
            "Disable full-sheet resize before splitting. "
            "By default, 4x4 sheets are normalized to 1024x1024 and "
            "5x5 sheets are normalized to 1280x1280 when --size is 256."
        ),
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help=(
            "Do not split sprites. Instead, generate a preview image with grid "
            "and expression labels for review."
        ),
    )

    parser.add_argument(
        "--preview-output",
        default=None,
        help=(
            "Output file path for --dry-run preview image. "
            "If omitted, a default preview PNG is created in the output folder."
        ),
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
        layout = infer_sheet_layout(
            job.sheet_path,
            cols_override=args.cols,
            rows_override=args.rows,
        )

        print(f"Layout:  {layout.name}")

        if args.dry_run:
            preview_path = get_preview_output_path(
                sheet_path=job.sheet_path,
                output_dir=job.output_dir,
                char_name=job.char_name,
                layout_name=layout.name,
                version_digits=job.version_digits,
                preview_output=args.preview_output,
            )

            render_dry_run_preview(
                sheet_path=job.sheet_path,
                output_path=preview_path,
                char_name=job.char_name,
                expressions=layout.expressions,
                cols=layout.cols,
                rows=layout.rows,
                target_size=args.size,
                version_digits=job.version_digits,
                normalize_sheet=not args.no_normalize_sheet,
            )
            continue

        split_sheet(
            sheet_path=job.sheet_path,
            output_dir=job.output_dir,
            char_name=job.char_name,
            expressions=layout.expressions,
            cols=layout.cols,
            rows=layout.rows,
            target_size=args.size,
            threshold=args.threshold,
            transparent_bg=args.transparent_bg,
            version_digits=job.version_digits,
            normalize_sheet=not args.no_normalize_sheet,
            crop_padding=args.crop_padding,
        )

        write_sprite_script(
            project_root=project_root,
            char_name=job.char_name,
            output_dir=job.output_dir,
            expression_order=layout.expressions,
        )

        print()


if __name__ == "__main__":
    main()