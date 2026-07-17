#!/usr/bin/env python3
"""
Batch-optimize Ren'Py PNG assets to WebP.

Designed for visual novels with:
- Opaque photographic / illustrated backgrounds.
- Character sprites with transparency.
- Lossless UI elements, masks, icons, and text-like artwork.

Safety:
- Dry-run by default.
- --apply is required to modify files.
- Originals and modified source files are backed up.
- Output is validated before replacement.
- A file is kept as PNG when WebP does not save enough space.
- Explicit .png references in project text files can be rewritten to .webp.

Requires:
    python -m pip install --upgrade Pillow

Examples:
    # Analyze and estimate savings without changing anything.
    python tools/optimize_renpy_images.py --project-root .

    # Recommended balanced conversion.
    python tools/optimize_renpy_images.py --project-root . --apply

    # Also shrink backgrounds so they fit within 1920x1080.
    python tools/optimize_renpy_images.py --project-root . --apply \
        --max-bg-size 1920x1080

    # Maximum visual safety for transparent sprites.
    python tools/optimize_renpy_images.py --project-root . --apply \
        --profile safe

    # More aggressive package-size reduction.
    python tools/optimize_renpy_images.py --project-root . --apply \
        --profile aggressive

Restore:
    Copy files from the printed backup directory back into the project.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import fnmatch
import json
import os
import shutil
import sys
import tempfile
import time
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, Optional

try:
    from PIL import Image, ImageChops, features
except ImportError:
    print(
        "ERROR: Pillow is not installed.\n"
        "Install it with:\n"
        "  python -m pip install --upgrade Pillow",
        file=sys.stderr,
    )
    raise SystemExit(2)


PNG_SUFFIX = ".png"
TEXT_SUFFIXES = {
    ".rpy", ".py", ".json", ".yaml", ".yml", ".toml", ".txt", ".md",
    ".csv", ".ini", ".cfg",
}

# Ren'Py/platform files that may be required by a fixed filename or are safer
# to leave alone unless the developer handles them explicitly.
DEFAULT_EXCLUDE_GLOBS = (
    "**/presplash.png",
    "**/presplash_background.png",
    "**/presplash_foreground.png",
    "**/web-icon.png",
    "**/icon.png",
    "**/android-icon_*.png",
    "**/ios-icon_*.png",
    "**/*.9.png",  # Android nine-patch.
)

UI_HINTS = {
    "gui", "ui", "icon", "icons", "button", "buttons", "bar", "bars",
    "frame", "frames", "textbox", "text_box", "overlay", "overlays",
    "mask", "masks", "cursor", "cursors", "badge", "badges", "logo",
    "logos", "window", "windows", "choice", "choices", "slider", "sliders",
}

BG_HINTS = {
    "bg", "bgs", "background", "backgrounds", "backdrop", "backdrops",
    "scene", "scenes", "environment", "environments", "location", "locations",
}

SPRITE_HINTS = {
    "sprite", "sprites", "character", "characters", "char", "chars",
    "side", "sides", "portrait", "portraits", "standing", "expression",
    "expressions",
}


@dataclass(frozen=True)
class CompressionProfile:
    name: str
    background_quality: int
    transparent_quality: int
    transparent_lossless: bool
    ui_lossless: bool = True
    method: int = 6
    alpha_quality: int = 100
    exact_alpha_rgb: bool = True


PROFILES = {
    "safe": CompressionProfile(
        name="safe",
        background_quality=90,
        transparent_quality=100,
        transparent_lossless=True,
    ),
    "balanced": CompressionProfile(
        name="balanced",
        background_quality=85,
        transparent_quality=92,
        transparent_lossless=False,
    ),
    "aggressive": CompressionProfile(
        name="aggressive",
        background_quality=78,
        transparent_quality=86,
        transparent_lossless=False,
    ),
    "lossless": CompressionProfile(
        name="lossless",
        background_quality=100,
        transparent_quality=100,
        transparent_lossless=True,
    ),
}


@dataclass
class JobResult:
    source: str
    destination: str
    status: str
    kind: str = ""
    width_before: int = 0
    height_before: int = 0
    width_after: int = 0
    height_after: int = 0
    bytes_before: int = 0
    bytes_after: int = 0
    savings_bytes: int = 0
    savings_percent: float = 0.0
    resized: bool = False
    has_alpha: bool = False
    encoding: str = ""
    temp_path: Optional[str] = None
    message: str = ""


def parse_size(value: str) -> tuple[int, int]:
    try:
        width_text, height_text = value.lower().split("x", 1)
        width = int(width_text)
        height = int(height_text)
    except (ValueError, AttributeError) as exc:
        raise argparse.ArgumentTypeError(
            "Size must use WIDTHxHEIGHT, for example 1920x1080."
        ) from exc

    if width <= 0 or height <= 0:
        raise argparse.ArgumentTypeError("Width and height must be positive.")
    return width, height


def normalized_parts(path: Path) -> set[str]:
    parts: set[str] = set()
    for raw in path.parts:
        lowered = raw.lower()
        parts.add(lowered)
        stem = Path(lowered).stem
        parts.add(stem)
        for token in stem.replace("-", "_").split("_"):
            if token:
                parts.add(token)
    return parts


def path_has_hint(path: Path, hints: set[str]) -> bool:
    return bool(normalized_parts(path) & hints)


def has_real_alpha(image: Image.Image) -> bool:
    if "A" in image.getbands():
        alpha = image.getchannel("A")
        minimum, maximum = alpha.getextrema()
        return minimum < 255
    if image.mode == "P" and "transparency" in image.info:
        return True
    return "transparency" in image.info


def classify_asset(relative_path: Path, image: Image.Image) -> tuple[str, bool]:
    alpha = has_real_alpha(image)

    if path_has_hint(relative_path, UI_HINTS):
        return "ui", alpha

    if path_has_hint(relative_path, BG_HINTS):
        return "background", alpha

    if alpha or path_has_hint(relative_path, SPRITE_HINTS):
        return "sprite", alpha

    # Opaque PNG artwork is usually closer to a background/CG than a sprite.
    return "opaque-art", alpha


def should_exclude(relative_path: Path, globs: Iterable[str]) -> Optional[str]:
    posix_path = relative_path.as_posix()
    for pattern in globs:
        if fnmatch.fnmatch(posix_path, pattern):
            return pattern
    return None


def fit_background(
    image: Image.Image,
    max_size: Optional[tuple[int, int]],
) -> tuple[Image.Image, bool]:
    if not max_size:
        return image, False

    if image.width <= max_size[0] and image.height <= max_size[1]:
        return image, False

    resized = image.copy()
    resized.thumbnail(max_size, Image.Resampling.LANCZOS)
    return resized, True


def validate_webp(
    source_image: Image.Image,
    output_path: Path,
    expected_size: tuple[int, int],
    require_exact_alpha: bool,
) -> None:
    with Image.open(output_path) as decoded:
        decoded.load()
        if decoded.size != expected_size:
            raise ValueError(
                f"Dimension mismatch: expected {expected_size}, got {decoded.size}"
            )

        if require_exact_alpha and "A" in source_image.getbands():
            source_alpha = source_image.getchannel("A")
            if source_alpha.size != decoded.size:
                source_alpha = source_alpha.resize(
                    decoded.size, Image.Resampling.LANCZOS
                )

            decoded_rgba = decoded.convert("RGBA")
            decoded_alpha = decoded_rgba.getchannel("A")
            difference = ImageChops.difference(source_alpha, decoded_alpha)
            if difference.getbbox() is not None:
                raise ValueError("Alpha channel changed during conversion.")


def encode_one(
    source: Path,
    assets_root: Path,
    profile: CompressionProfile,
    max_bg_size: Optional[tuple[int, int]],
    min_savings_percent: float,
    force_convert: bool,
    overwrite: bool,
    preserve_icc: bool,
) -> JobResult:
    destination = source.with_suffix(".webp")
    relative_path = source.relative_to(assets_root)
    before_size = source.stat().st_size

    if destination.exists() and not overwrite:
        return JobResult(
            source=str(source),
            destination=str(destination),
            status="skipped",
            bytes_before=before_size,
            message="Destination already exists. Use --overwrite to replace it.",
        )

    temp_file = tempfile.NamedTemporaryFile(
        prefix=f".{source.stem}.",
        suffix=".webp.tmp",
        dir=source.parent,
        delete=False,
    )
    temp_path = Path(temp_file.name)
    temp_file.close()

    try:
        with Image.open(source) as opened:
            if getattr(opened, "n_frames", 1) > 1:
                return JobResult(
                    source=str(source),
                    destination=str(destination),
                    status="skipped",
                    bytes_before=before_size,
                    message="Animated/multi-frame PNG is not converted.",
                )

            opened.load()
            original_size = opened.size
            kind, alpha = classify_asset(relative_path, opened)

            working = opened
            resized = False
            if kind == "background":
                working, resized = fit_background(working, max_bg_size)

            # Normalize uncommon PNG modes to formats that WebP handles reliably.
            if alpha:
                working = working.convert("RGBA")
            else:
                working = working.convert("RGB")

            save_options: dict[str, object] = {
                "format": "WEBP",
                "method": profile.method,
            }

            if preserve_icc and opened.info.get("icc_profile"):
                save_options["icc_profile"] = opened.info["icc_profile"]

            if kind == "ui":
                save_options.update(
                    lossless=True,
                    quality=100,  # Effort in Pillow's lossless mode.
                    exact=alpha,
                )
                encoding = "webp-lossless-ui"
                exact_alpha = alpha
            elif alpha:
                if profile.transparent_lossless:
                    save_options.update(
                        lossless=True,
                        quality=100,
                        exact=profile.exact_alpha_rgb,
                    )
                    encoding = "webp-lossless-alpha"
                else:
                    save_options.update(
                        lossless=False,
                        quality=profile.transparent_quality,
                        alpha_quality=profile.alpha_quality,
                        exact=profile.exact_alpha_rgb,
                    )
                    encoding = (
                        f"webp-lossy-rgb-q{profile.transparent_quality}"
                        f"+lossless-alpha"
                    )
                exact_alpha = profile.alpha_quality == 100
            elif profile.name == "lossless":
                save_options.update(lossless=True, quality=100)
                encoding = "webp-lossless"
                exact_alpha = False
            else:
                save_options.update(
                    lossless=False,
                    quality=profile.background_quality,
                )
                encoding = f"webp-lossy-q{profile.background_quality}"
                exact_alpha = False

            working.save(temp_path, **save_options)
            validate_webp(
                working,
                temp_path,
                expected_size=working.size,
                require_exact_alpha=exact_alpha and alpha,
            )

            after_size = temp_path.stat().st_size
            savings_bytes = before_size - after_size
            savings_percent = (
                (savings_bytes / before_size) * 100.0 if before_size else 0.0
            )

            if not force_convert and savings_percent < min_savings_percent:
                temp_path.unlink(missing_ok=True)
                return JobResult(
                    source=str(source),
                    destination=str(destination),
                    status="kept-png",
                    kind=kind,
                    width_before=original_size[0],
                    height_before=original_size[1],
                    width_after=working.width,
                    height_after=working.height,
                    bytes_before=before_size,
                    bytes_after=after_size,
                    savings_bytes=savings_bytes,
                    savings_percent=round(savings_percent, 2),
                    resized=resized,
                    has_alpha=alpha,
                    encoding=encoding,
                    message=(
                        f"WebP saved less than {min_savings_percent:.1f}%; "
                        "original PNG kept."
                    ),
                )

            return JobResult(
                source=str(source),
                destination=str(destination),
                status="ready",
                kind=kind,
                width_before=original_size[0],
                height_before=original_size[1],
                width_after=working.width,
                height_after=working.height,
                bytes_before=before_size,
                bytes_after=after_size,
                savings_bytes=savings_bytes,
                savings_percent=round(savings_percent, 2),
                resized=resized,
                has_alpha=alpha,
                encoding=encoding,
                temp_path=str(temp_path),
            )
    except Exception as exc:
        temp_path.unlink(missing_ok=True)
        return JobResult(
            source=str(source),
            destination=str(destination),
            status="error",
            bytes_before=before_size,
            message=f"{type(exc).__name__}: {exc}",
        )


def human_bytes(value: int) -> str:
    sign = "-" if value < 0 else ""
    size = abs(float(value))
    units = ("B", "KiB", "MiB", "GiB", "TiB")
    for unit in units:
        if size < 1024.0 or unit == units[-1]:
            return f"{sign}{size:.2f} {unit}"
        size /= 1024.0
    return f"{sign}{size:.2f} TiB"


def discover_text_files(project_root: Path, backup_root: Path) -> list[Path]:
    ignored_dirs = {
        ".git", ".hg", ".svn", "__pycache__", ".renpy", "cache",
        "saves", "tmp", "temp",
    }
    files: list[Path] = []
    for path in project_root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            path.relative_to(backup_root)
            continue
        except ValueError:
            pass
        try:
            relative_parts = path.relative_to(project_root).parts
        except ValueError:
            relative_parts = path.parts
        if any(part.lower() in ignored_dirs for part in relative_parts[:-1]):
            continue
        files.append(path)
    return files


def replacement_pairs(
    project_root: Path,
    assets_root: Path,
    conversions: list[JobResult],
    rewrite_basenames: bool,
) -> list[tuple[str, str]]:
    pairs: set[tuple[str, str]] = set()
    game_root = project_root / "game"

    for result in conversions:
        source = Path(result.source)
        destination = Path(result.destination)

        # Project-relative path: game/images/...
        try:
            old = source.relative_to(project_root).as_posix()
            new = destination.relative_to(project_root).as_posix()
            pairs.add((old, new))
            pairs.add((old.replace("/", "\\"), new.replace("/", "\\")))
        except ValueError:
            pass

        # Ren'Py game-relative path: images/...
        try:
            old = source.relative_to(game_root).as_posix()
            new = destination.relative_to(game_root).as_posix()
            pairs.add((old, new))
            pairs.add((old.replace("/", "\\"), new.replace("/", "\\")))
        except ValueError:
            pass

        # Assets-root-relative path. Useful for custom loaders.
        try:
            old = source.relative_to(assets_root).as_posix()
            new = destination.relative_to(assets_root).as_posix()
            if "/" in old:  # Avoid risky global basename replacement by default.
                pairs.add((old, new))
                pairs.add((old.replace("/", "\\"), new.replace("/", "\\")))
        except ValueError:
            pass

        if rewrite_basenames:
            pairs.add((source.name, destination.name))

    # Longest paths first to avoid partial replacement surprises.
    return sorted(pairs, key=lambda item: len(item[0]), reverse=True)


def backup_file(path: Path, project_root: Path, backup_root: Path) -> None:
    try:
        relative = path.relative_to(project_root)
    except ValueError:
        # External assets are placed under a clearly named fallback.
        relative = Path("_external") / path.anchor.replace(":", "") / Path(
            *path.parts[1:]
        )

    target = backup_root / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, target)


def patch_references(
    project_root: Path,
    assets_root: Path,
    backup_root: Path,
    conversions: list[JobResult],
    rewrite_basenames: bool,
) -> tuple[int, int]:
    pairs = replacement_pairs(
        project_root,
        assets_root,
        conversions,
        rewrite_basenames,
    )
    if not pairs:
        return 0, 0

    files_changed = 0
    replacements_made = 0

    for path in discover_text_files(project_root, backup_root):
        try:
            original = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        updated = original
        local_replacements = 0
        for old, new in pairs:
            count = updated.count(old)
            if count:
                updated = updated.replace(old, new)
                local_replacements += count

        if updated == original:
            continue

        backup_file(path, project_root, backup_root)
        path.write_text(updated, encoding="utf-8", newline="")
        files_changed += 1
        replacements_made += local_replacements

    return files_changed, replacements_made


def commit_conversions(
    project_root: Path,
    assets_root: Path,
    backup_root: Path,
    conversions: list[JobResult],
    rewrite_refs: bool,
    rewrite_basenames: bool,
    overwrite: bool,
) -> tuple[int, int]:
    # Back up image files before touching the source tree.
    for result in conversions:
        source = Path(result.source)
        destination = Path(result.destination)
        backup_file(source, project_root, backup_root)
        if destination.exists() and overwrite:
            backup_file(destination, project_root, backup_root)

    for result in conversions:
        source = Path(result.source)
        destination = Path(result.destination)
        temp_path = Path(result.temp_path or "")

        destination.parent.mkdir(parents=True, exist_ok=True)
        os.replace(temp_path, destination)
        source.unlink()
        result.status = "converted"
        result.temp_path = None

    if rewrite_refs:
        return patch_references(
            project_root=project_root,
            assets_root=assets_root,
            backup_root=backup_root,
            conversions=conversions,
            rewrite_basenames=rewrite_basenames,
        )
    return 0, 0


def cleanup_temps(results: Iterable[JobResult]) -> None:
    for result in results:
        if result.temp_path:
            Path(result.temp_path).unlink(missing_ok=True)
            result.temp_path = None


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Safely batch-convert Ren'Py PNG assets to WebP.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--project-root",
        type=Path,
        default=Path("."),
        help="Ren'Py project root containing the game directory.",
    )
    parser.add_argument(
        "--assets-root",
        type=Path,
        default=None,
        help="Asset directory. Defaults to <project-root>/game/images.",
    )
    parser.add_argument(
        "--profile",
        choices=sorted(PROFILES),
        default="balanced",
        help="Compression profile.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Modify files. Without this flag the script performs a dry-run.",
    )
    parser.add_argument(
        "--max-bg-size",
        type=parse_size,
        default=None,
        metavar="WIDTHxHEIGHT",
        help=(
            "Shrink detected backgrounds to fit this bounding box. "
            "Sprites and UI are never resized."
        ),
    )
    parser.add_argument(
        "--min-savings-percent",
        type=float,
        default=3.0,
        help="Keep PNG when WebP saves less than this percentage.",
    )
    parser.add_argument(
        "--force-convert",
        action="store_true",
        help="Convert even when WebP is not smaller enough.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace an existing .webp file after backing it up.",
    )
    parser.add_argument(
        "--no-rewrite",
        action="store_true",
        help="Do not rewrite explicit .png references in project text files.",
    )
    parser.add_argument(
        "--rewrite-basenames",
        action="store_true",
        help=(
            "Also replace bare names like foo.png. More complete, but riskier "
            "when duplicate basenames exist."
        ),
    )
    parser.add_argument(
        "--strip-icc",
        action="store_true",
        help="Remove embedded ICC color profiles for slightly smaller files.",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        metavar="GLOB",
        help="Additional project-relative glob to exclude. Repeatable.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=max(1, min(8, os.cpu_count() or 1)),
        help="Parallel encoder worker count.",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=None,
        help="JSON report path. Defaults to <project-root>/image_optimization_report.json.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()

    if not features.check("webp"):
        print(
            "ERROR: This Pillow build has no WebP encoder support.\n"
            "Install a current official Pillow wheel:\n"
            "  python -m pip install --upgrade --force-reinstall Pillow",
            file=sys.stderr,
        )
        return 2

    project_root = args.project_root.expanduser().resolve()
    assets_root = (
        args.assets_root.expanduser().resolve()
        if args.assets_root
        else project_root / "game" / "images"
    )
    report_path = (
        args.report.expanduser().resolve()
        if args.report
        else project_root / "image_optimization_report.json"
    )

    if not project_root.is_dir():
        print(f"ERROR: Project root does not exist: {project_root}", file=sys.stderr)
        return 2
    if not assets_root.is_dir():
        print(f"ERROR: Assets root does not exist: {assets_root}", file=sys.stderr)
        return 2
    if args.min_savings_percent < 0:
        print("ERROR: --min-savings-percent cannot be negative.", file=sys.stderr)
        return 2
    if args.workers < 1:
        print("ERROR: --workers must be at least 1.", file=sys.stderr)
        return 2

    profile = PROFILES[args.profile]
    all_excludes = tuple(DEFAULT_EXCLUDE_GLOBS) + tuple(args.exclude)

    sources: list[Path] = []
    excluded_results: list[JobResult] = []

    for source in sorted(assets_root.rglob("*")):
        if not source.is_file() or source.suffix.lower() != PNG_SUFFIX:
            continue
        relative = source.relative_to(assets_root)
        matched = should_exclude(relative, all_excludes)
        if matched:
            excluded_results.append(
                JobResult(
                    source=str(source),
                    destination=str(source.with_suffix(".webp")),
                    status="excluded",
                    bytes_before=source.stat().st_size,
                    message=f"Matched exclusion: {matched}",
                )
            )
        else:
            sources.append(source)

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"[{mode}] Project: {project_root}")
    print(f"[{mode}] Assets : {assets_root}")
    print(f"[{mode}] Profile: {profile.name}")
    if args.max_bg_size:
        print(
            f"[{mode}] Background limit: "
            f"{args.max_bg_size[0]}x{args.max_bg_size[1]}"
        )
    print(f"[{mode}] PNG candidates: {len(sources)}")
    print(f"[{mode}] Excluded: {len(excluded_results)}")
    print()

    started = time.perf_counter()
    results: list[JobResult] = []

    with concurrent.futures.ThreadPoolExecutor(
        max_workers=args.workers
    ) as executor:
        future_map = {
            executor.submit(
                encode_one,
                source,
                assets_root,
                profile,
                args.max_bg_size,
                args.min_savings_percent,
                args.force_convert,
                args.overwrite,
                not args.strip_icc,
            ): source
            for source in sources
        }

        completed = 0
        total = len(future_map)
        for future in concurrent.futures.as_completed(future_map):
            result = future.result()
            results.append(result)
            completed += 1

            marker = {
                "ready": "OK",
                "kept-png": "KEEP",
                "skipped": "SKIP",
                "error": "ERROR",
            }.get(result.status, result.status.upper())

            relative_display = Path(result.source).relative_to(assets_root)
            if result.status in {"ready", "kept-png"}:
                print(
                    f"[{completed:>4}/{total}] {marker:<5} "
                    f"{relative_display} | {result.kind} | "
                    f"{human_bytes(result.bytes_before)} -> "
                    f"{human_bytes(result.bytes_after)} | "
                    f"{result.savings_percent:+.2f}%"
                )
            else:
                print(
                    f"[{completed:>4}/{total}] {marker:<5} "
                    f"{relative_display} | {result.message}"
                )

    results.extend(excluded_results)
    results.sort(key=lambda item: item.source)

    ready = [result for result in results if result.status == "ready"]
    files_changed = 0
    references_changed = 0
    backup_root: Optional[Path] = None

    try:
        if args.apply and ready:
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            backup_root = project_root / ".image-backup" / timestamp
            backup_root.mkdir(parents=True, exist_ok=False)

            files_changed, references_changed = commit_conversions(
                project_root=project_root,
                assets_root=assets_root,
                backup_root=backup_root,
                conversions=ready,
                rewrite_refs=not args.no_rewrite,
                rewrite_basenames=args.rewrite_basenames,
                overwrite=args.overwrite,
            )
        else:
            cleanup_temps(ready)
    except Exception:
        cleanup_temps(ready)
        raise

    elapsed = time.perf_counter() - started

    converted_or_ready = [
        result
        for result in results
        if result.status in {"ready", "converted"}
    ]
    total_before = sum(result.bytes_before for result in converted_or_ready)
    total_after = sum(result.bytes_after for result in converted_or_ready)
    total_saved = total_before - total_after
    total_percent = (total_saved / total_before * 100.0) if total_before else 0.0

    report = {
        "mode": mode,
        "project_root": str(project_root),
        "assets_root": str(assets_root),
        "profile": asdict(profile),
        "max_bg_size": args.max_bg_size,
        "min_savings_percent": args.min_savings_percent,
        "backup_root": str(backup_root) if backup_root else None,
        "reference_files_changed": files_changed,
        "reference_occurrences_changed": references_changed,
        "summary": {
            "png_candidates": len(sources),
            "converted_or_ready": len(converted_or_ready),
            "kept_png": sum(r.status == "kept-png" for r in results),
            "skipped": sum(r.status == "skipped" for r in results),
            "excluded": sum(r.status == "excluded" for r in results),
            "errors": sum(r.status == "error" for r in results),
            "bytes_before": total_before,
            "bytes_after": total_after,
            "bytes_saved": total_saved,
            "savings_percent": round(total_percent, 2),
            "elapsed_seconds": round(elapsed, 2),
        },
        "files": [asdict(result) for result in results],
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print()
    print("=" * 72)
    print(f"Mode                  : {mode}")
    print(f"Converted / ready     : {len(converted_or_ready)}")
    print(f"Kept as PNG           : {report['summary']['kept_png']}")
    print(f"Skipped               : {report['summary']['skipped']}")
    print(f"Excluded              : {report['summary']['excluded']}")
    print(f"Errors                : {report['summary']['errors']}")
    print(f"Selected bytes before : {human_bytes(total_before)}")
    print(f"Selected bytes after  : {human_bytes(total_after)}")
    print(
        f"Estimated / saved     : {human_bytes(total_saved)} "
        f"({total_percent:.2f}%)"
    )
    print(f"Reference files edited: {files_changed}")
    print(f"Reference replacements: {references_changed}")
    print(f"Elapsed               : {elapsed:.2f}s")
    print(f"Report                : {report_path}")
    if backup_root:
        print(f"Backup                : {backup_root}")
    if not args.apply:
        print()
        print("No project files were modified. Add --apply after reviewing the report.")
    print("=" * 72)

    return 1 if report["summary"]["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
