# Ren'Py Image Optimization

## Recommended strategy

- Backgrounds / CGs without transparency: lossy WebP, quality around 85.
- Character sprites with transparency: lossy RGB WebP around quality 92, with
  lossless alpha.
- GUI, icons, masks, line-art, and text-like assets: lossless WebP.
- Keep special platform images such as `presplash.png`, `web-icon.png`, and
  Android `.9.png` files in their required formats.
- Resize backgrounds to the game's actual virtual resolution when no zoom/pan
  needs the extra pixels. File compression does not reduce decoded texture
  memory; pixel dimensions do.

## Installation

```bash
python -m pip install --upgrade Pillow
```

Place `optimize_renpy_images.py` under the project's `tools/` directory.

## 1. Dry-run first

```bash
python tools/optimize_renpy_images.py --project-root .
```

This encodes temporary WebP files, validates them, prints estimated savings,
writes `image_optimization_report.json`, and changes nothing.

## 2. Apply the balanced profile

```bash
python tools/optimize_renpy_images.py --project-root . --apply
```

The script:

1. Recursively scans `game/images`.
2. Detects backgrounds, transparent sprites, and UI-like assets.
3. Converts each category using an appropriate WebP mode.
4. Keeps PNG when WebP saves less than 3%.
5. Backs up originals under `.image-backup/<timestamp>/`.
6. Rewrites explicit `.png` paths in `.rpy` and other project text files.
7. Produces a JSON report.

## 3. Resize oversized backgrounds

For a 1920x1080 game:

```bash
python tools/optimize_renpy_images.py \
  --project-root . \
  --apply \
  --max-bg-size 1920x1080
```

This only downsizes assets classified as backgrounds. Sprites and UI are not
resized. It preserves aspect ratio and never upscales.

Do not use this when a background is intentionally larger for camera pan/zoom,
or when it uses Ren'Py oversampling.

## Profiles

```bash
# Safer sprite quality: transparent assets use lossless WebP.
python tools/optimize_renpy_images.py --project-root . --apply --profile safe

# Recommended default.
python tools/optimize_renpy_images.py --project-root . --apply --profile balanced

# Smaller package, inspect sprites and gradients carefully.
python tools/optimize_renpy_images.py --project-root . --apply --profile aggressive

# Everything lossless.
python tools/optimize_renpy_images.py --project-root . --apply --profile lossless
```

## Useful options

```bash
# Add exclusions.
--exclude "**/cg/special_panorama.png"

# Replace an existing .webp after backing it up.
--overwrite

# Convert even when WebP is not at least 3% smaller.
--force-convert

# Do not update explicit .png paths in source files.
--no-rewrite

# Also rewrite bare names such as "foo.png".
# Use only when duplicate basenames are not present.
--rewrite-basenames

# Strip ICC profiles for slightly smaller output.
--strip-icc
```

## Verification after conversion

1. Run Ren'Py's **Check Script (Lint)**.
2. Launch the game in developer mode.
3. Test:
   - character edges over bright and dark backgrounds;
   - dissolve transitions;
   - zoom/pan scenes;
   - GUI nine-slice frames;
   - Android/Web builds if targeted.
4. Compare `image_optimization_report.json`.
5. Commit the conversion separately so reverting is simple.

## Runtime notes

Smaller files improve package size and often disk I/O, but decoded images still
consume memory according to pixel count. For runtime performance, also review:

```renpy
define config.image_cache_size_mb = 300
define config.predict_statements = 32
define config.optimize_texture_bounds = True
```

Do not raise the cache blindly. Test on the lowest-memory target device.
