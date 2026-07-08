#!/usr/bin/env python3
"""
batch_remove_black_bg.py

Batch remove black / near-black background connected to image borders.

Features:
- Scan images from input folder.
- Output cleaned PNG files to output folder.
- Remove only dark pixels connected to image borders.
- Support near-black threshold via --range.
- Feather alpha edge via --smooth-padding.
- Clear border artifacts via per-edge --safe-padding.

Dependencies:
    pip install pillow numpy

Examples:
    python batch_remove_black_bg.py --input ./input --output ./output

    python batch_remove_black_bg.py --input ./input --output ./output --range 28

    python batch_remove_black_bg.py --input ./input --output ./output --range 28 --smooth-padding 6

    python batch_remove_black_bg.py --input ./input --output ./output --safe-padding 4

    python batch_remove_black_bg.py --input ./input --output ./output --safe-padding 4 2 4 0

    python batch_remove_black_bg.py --input ./input --output ./output --opacity

    python batch_remove_black_bg.py --input ./input --output ./output --opacity 0.65

    python batch_remove_black_bg.py --input ./input --output ./output --recursive
"""

from __future__ import annotations

import argparse
from collections import deque
from pathlib import Path
from typing import Iterable, NamedTuple

import numpy as np
from PIL import Image


SUPPORTED_EXTENSIONS = {
    ".png",
    ".webp",
    ".jpg",
    ".jpeg",
    ".bmp",
    ".tif",
    ".tiff",
}


class SafePadding(NamedTuple):
    """
    Border clear padding order:
        left, top, right, bottom
    """

    left: int
    top: int
    right: int
    bottom: int


def parse_safe_padding(values: list[int]) -> SafePadding:
    """
    Parse --safe-padding.

    Supported:
        --safe-padding 4
            => left=4, top=4, right=4, bottom=4

        --safe-padding 4 2 4 0
            => left=4, top=2, right=4, bottom=0
    """
    if not values:
        values = [4]

    if len(values) == 1:
        value = values[0]

        if value < 0:
            raise ValueError("--safe-padding must be >= 0")

        return SafePadding(
            left=value,
            top=value,
            right=value,
            bottom=value,
        )

    if len(values) == 4:
        left, top, right, bottom = values

        if min(left, top, right, bottom) < 0:
            raise ValueError("--safe-padding values must be >= 0")

        return SafePadding(
            left=left,
            top=top,
            right=right,
            bottom=bottom,
        )

    raise ValueError(
        "--safe-padding accepts either 1 value or 4 values: "
        "--safe-padding 4 OR --safe-padding LEFT TOP RIGHT BOTTOM"
    )


def is_inside_path(path: Path, parent: Path) -> bool:
    """
    Return True if path is inside parent.
    Compatible with older Python versions that may not have Path.is_relative_to.
    """
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def find_border_connected_dark(
    rgb: np.ndarray,
    black_range: int,
    safe_padding: SafePadding,
) -> np.ndarray:
    """
    Detect dark pixels connected to image borders.

    A pixel is considered background candidate if:
        R <= black_range and G <= black_range and B <= black_range

    The safe-padding area is also used as an expanded seed zone.
    This helps remove near-edge artifacts that may not touch the exact image edge.
    """
    h, w, _ = rgb.shape

    dark = np.all(rgb <= black_range, axis=2)

    visited = np.zeros((h, w), dtype=bool)
    q: deque[tuple[int, int]] = deque()

    left = min(safe_padding.left, w)
    top = min(safe_padding.top, h)
    right = min(safe_padding.right, w)
    bottom = min(safe_padding.bottom, h)

    def push(y: int, x: int) -> None:
        if dark[y, x] and not visited[y, x]:
            visited[y, x] = True
            q.append((y, x))

    # Always seed the true outer border.
    for x in range(w):
        push(0, x)
        push(h - 1, x)

    for y in range(h):
        push(y, 0)
        push(y, w - 1)

    # Expanded top seed band.
    for y in range(top):
        for x in range(w):
            push(y, x)

    # Expanded bottom seed band.
    if bottom > 0:
        for y in range(h - bottom, h):
            for x in range(w):
                push(y, x)

    # Expanded left seed band.
    for y in range(h):
        for x in range(left):
            push(y, x)

    # Expanded right seed band.
    if right > 0:
        for y in range(h):
            for x in range(w - right, w):
                push(y, x)

    # 8-connected flood fill.
    neighbors = (
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    )

    while q:
        y, x = q.popleft()

        for dy, dx in neighbors:
            ny = y + dy
            nx = x + dx

            if 0 <= ny < h and 0 <= nx < w:
                if dark[ny, nx] and not visited[ny, nx]:
                    visited[ny, nx] = True
                    q.append((ny, nx))

    return visited


def dilate_8(mask: np.ndarray) -> np.ndarray:
    """
    8-neighbor binary dilation using numpy slicing.
    """
    out = mask.copy()

    out[1:, :] |= mask[:-1, :]
    out[:-1, :] |= mask[1:, :]
    out[:, 1:] |= mask[:, :-1]
    out[:, :-1] |= mask[:, 1:]

    out[1:, 1:] |= mask[:-1, :-1]
    out[1:, :-1] |= mask[:-1, 1:]
    out[:-1, 1:] |= mask[1:, :-1]
    out[:-1, :-1] |= mask[1:, 1:]

    return out


def apply_edge_feather(
    alpha: np.ndarray,
    bg_mask: np.ndarray,
    smooth_padding: int,
) -> np.ndarray:
    """
    Remove background alpha and feather nearby edge pixels.

    Background pixels become alpha 0.
    Pixels near the cut edge gradually recover toward their original alpha.
    """
    original_alpha = alpha.copy()
    alpha[bg_mask] = 0

    if smooth_padding <= 0:
        return alpha

    expanded = bg_mask.copy()

    for i in range(1, smooth_padding + 1):
        dilated = dilate_8(expanded)
        ring = dilated & ~expanded

        # Nearer to the removed background = more transparent.
        # Farther from the removed background = closer to original alpha.
        factor = i / float(smooth_padding + 1)

        alpha[ring] = np.minimum(
            alpha[ring],
            original_alpha[ring] * factor,
        )

        expanded = dilated

    return alpha


def clear_safe_padding(
    alpha: np.ndarray,
    safe_padding: SafePadding,
) -> np.ndarray:
    """
    Force-clear selected border areas.

    Order:
        left, top, right, bottom

    Example:
        --safe-padding 4 2 4 0

    Means:
        clear left 4px
        clear top 2px
        clear right 4px
        clear bottom 0px

    Warning:
        If the subject touches a cleared border, that part will be trimmed.
    """
    h, w = alpha.shape

    left = min(safe_padding.left, w)
    top = min(safe_padding.top, h)
    right = min(safe_padding.right, w)
    bottom = min(safe_padding.bottom, h)

    if top > 0:
        alpha[:top, :] = 0

    if bottom > 0:
        alpha[h - bottom:, :] = 0

    if left > 0:
        alpha[:, :left] = 0

    if right > 0:
        alpha[:, w - right:] = 0

    return alpha


def remove_background_from_image(
    input_path: Path,
    output_path: Path,
    smooth_padding: int,
    opacity: float | None,
    black_range: int,
    safe_padding: SafePadding,
) -> None:
    image = Image.open(input_path).convert("RGBA")
    arr = np.array(image)

    rgb = arr[:, :, :3]
    alpha = arr[:, :, 3].astype(np.float32)

    bg_mask = find_border_connected_dark(
        rgb=rgb,
        black_range=black_range,
        safe_padding=safe_padding,
    )

    alpha = apply_edge_feather(
        alpha=alpha,
        bg_mask=bg_mask,
        smooth_padding=smooth_padding,
    )

    alpha = clear_safe_padding(
        alpha=alpha,
        safe_padding=safe_padding,
    )

    if opacity is not None:
        alpha *= opacity

    arr[:, :, 3] = np.clip(alpha, 0, 255).astype(np.uint8)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(arr, mode="RGBA").save(output_path)


def iter_image_files(
    input_dir: Path,
    output_dir: Path,
    recursive: bool,
) -> list[Path]:
    """
    Collect image files.

    If output_dir is inside input_dir, skip output_dir to avoid re-processing
    already cleaned files on recursive runs.
    """
    pattern = "**/*" if recursive else "*"

    files: list[Path] = []

    for path in input_dir.glob(pattern):
        if not path.is_file():
            continue

        if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        if is_inside_path(path, output_dir):
            continue

        files.append(path)

    return sorted(files)


def build_output_path(
    input_file: Path,
    input_dir: Path,
    output_dir: Path,
) -> Path:
    """
    Always output PNG to preserve alpha.

    Keeps relative folder structure when --recursive is used.
    """
    relative_path = input_file.relative_to(input_dir)
    return output_dir / relative_path.with_suffix(".png")


def process_folder(
    input_dir: Path,
    output_dir: Path,
    smooth_padding: int,
    opacity: float | None,
    recursive: bool,
    black_range: int,
    safe_padding: SafePadding,
) -> None:
    if not input_dir.exists():
        raise FileNotFoundError(f"Input folder does not exist: {input_dir}")

    if not input_dir.is_dir():
        raise NotADirectoryError(f"--input must be a folder: {input_dir}")

    if smooth_padding < 0:
        raise ValueError("--smooth-padding must be >= 0")

    if opacity is not None and not (0.0 <= opacity <= 1.0):
        raise ValueError("--opacity must be between 0.0 and 1.0")

    if not (0 <= black_range <= 255):
        raise ValueError("--range must be between 0 and 255")

    image_files = iter_image_files(
        input_dir=input_dir,
        output_dir=output_dir,
        recursive=recursive,
    )

    if not image_files:
        print(f"No supported image files found in: {input_dir}")
        return

    total = len(image_files)
    success = 0
    failed = 0

    print(f"Input folder      : {input_dir}")
    print(f"Output folder     : {output_dir}")
    print(f"Recursive         : {recursive}")
    print(f"Range             : {black_range}")
    print(f"Smooth padding    : {smooth_padding}")
    print(
        "Safe padding      : "
        f"left={safe_padding.left}, "
        f"top={safe_padding.top}, "
        f"right={safe_padding.right}, "
        f"bottom={safe_padding.bottom}"
    )
    print(f"Global opacity    : {opacity if opacity is not None else 'unchanged'}")
    print()

    for index, input_file in enumerate(image_files, start=1):
        output_file = build_output_path(
            input_file=input_file,
            input_dir=input_dir,
            output_dir=output_dir,
        )

        try:
            remove_background_from_image(
                input_path=input_file,
                output_path=output_file,
                smooth_padding=smooth_padding,
                opacity=opacity,
                black_range=black_range,
                safe_padding=safe_padding,
            )

            success += 1
            print(f"[{index}/{total}] OK   {input_file} -> {output_file}")

        except Exception as exc:
            failed += 1
            print(f"[{index}/{total}] FAIL {input_file}: {exc}")

    print()
    print(f"Done. Success: {success}, Failed: {failed}, Total: {total}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Batch remove black / near-black border-connected background."
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Input folder containing images.",
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Output folder for processed PNG images.",
    )

    parser.add_argument(
        "--smooth-padding",
        type=int,
        default=4,
        help="Feather distance in pixels. Default: 4.",
    )

    parser.add_argument(
        "--safe-padding",
        nargs="*",
        type=int,
        default=[4],
        help=(
            "Force-clear border pixels. "
            "Use one value for all sides, e.g. --safe-padding 4. "
            "Use four values as LEFT TOP RIGHT BOTTOM, "
            "e.g. --safe-padding 4 2 4 0. "
            "Default: 4."
        ),
    )

    parser.add_argument(
        "--range",
        dest="black_range",
        type=int,
        default=0,
        help=(
            "Near-black threshold. "
            "0 = exact #000000 only. "
            "28 = remove pixels where R/G/B are all <= 28."
        ),
    )

    parser.add_argument(
        "--opacity",
        nargs="?",
        const=0.8,
        default=None,
        type=float,
        help=(
            "Apply global opacity to the whole image after background removal. "
            "If used without value, defaults to 0.8."
        ),
    )

    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Scan images inside subfolders too.",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    safe_padding = parse_safe_padding(args.safe_padding)

    process_folder(
        input_dir=Path(args.input),
        output_dir=Path(args.output),
        smooth_padding=args.smooth_padding,
        opacity=args.opacity,
        recursive=args.recursive,
        black_range=args.black_range,
        safe_padding=safe_padding,
    )


if __name__ == "__main__":
    main()