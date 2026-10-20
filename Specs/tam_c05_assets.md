# Chapter 5 anniversary illustrations

32 new runtime images: 24 CGs and eight backgrounds. Created with built-in
ImageGen, then converted to opaque RGB 1920x1080 WebP, quality 94, Lanczos fit.
All assets live in `game/images/assets/{cg,bg}/`; declarations are in
`game/scripts/cgs_tam_c05.rpy`.

Inventory: `tam_c05_asset_manifest.json`. Exact generation/edit prompts and source
images: `tam_c05_asset_prompts.json`. The 27 bounded CG insertion cues, original
dialogue anchors and restore backgrounds: `tam_c05_asset_integration.json`.

## Character and wardrobe continuity

Tam's date branch uses **the same pale peach-pink chiffon dress she wore at the
C01 celebration dinner with Huyen**. `cg_tam_c01_celebration_toast.webp` is the
mandatory dress reference: gathered bodice and sheer puff sleeves, with the same
color and cut throughout pickup, breakfast, conservatory, park, gifts and the
nighttime collar adjustment. The morning CG shows her holding that dress before
changing. The existing morning choices retain their original text and scoring;
the images follow the requested dress continuity across those choices.

Huyen has a compact rounded face, short soft chin, natural small eyes, wispy bangs
and shoulder-length layered half-up hair. Her casual capsule is a mint open
overshirt over an ivory tee with charcoal trousers, compatible with the prepared
shirt and safer tee/overshirt choices. Her morning CG uses lavender sleepwear.
Group-branch Tam wears an ivory blouse and beige trousers. Hoang wears a pale
blue collared shirt and thin navy casual jacket. Each character uses their own
portrait reference; Huyen and Tam must not share faces or hair length.

## Coverage and integration

| Segment | CGs | Coverage |
| --- | ---: | --- |
| Morning | 3 | Tam choosing the dress, Huyen waking, group in the car. |
| Tam outing | 4 | Pickup, breakfast, closed conservatory, stone park bench. |
| Huyen outing | 4 | Two drinks at pickup, breakfast, candid photo, rain shelter. |
| Group outing | 2 | Shared meal and timer photograph. |
| Tam gifts | 4 | Small topaz earrings, fastening, excessive topaz, folded breakfast receipt. |
| Huyen gifts | 3 | Printer unboxing, personal album photograph, new print. |
| Group gift | 1 | Equal photo envelopes. |
| Evening | 3 | Tam adjusts collar, Huyen's car conversation, Tam reads group chat at home. |

The eight new backgrounds cover breakfast, conservatory gate, stone park bench,
market cafe, dry market, rain shelter, parked car at night and apartment entrance
at night. Existing bedrooms, daytime car and Tam's nighttime living room are
reused. The two extra backgrounds beyond the initial six-image estimate prevent
the nighttime exterior and outdoor market passages from retaining the wrong
indoor setting.

Every CG illustrates one existing narration beat and immediately restores its
location before later gestures, menus or outcomes. Gift variants remain inside
their original story conditions. Earring fastening appears only after choosing
to wear the earrings or ask for help, including the hesitant fastening branch.
The generic printer shot hides the album so it also fits the printer-only branch;
the personal album shot is restricted to the personal-photo branch. The nighttime
collar shot hides Tam's ears so it does not force an earring outcome.

No dialogue, menu text, flags, scores, chapter dispatch or translation strings
were changed. The validator compares all five C05 source files against commit
`0f2ab80`, ignoring only scene/transition statements, comments and blank lines.

## Verification

Runtime: Windows, Ren'Py 8.5.4.26101301+nightly, Python 3.12.7, game 4.11.0.

Final results on 2026-10-20:

- Inventory/narrative validator: PASS; all 32 images declared and used,
  12.44 MiB, all five source files preserve narrative and logic.
- `chapter_five_assets`: two cases PASS, 6/6 assertions, 64 catalog captures.
- `chapter_five_branches`: 15 cases PASS, 145/145 assertions, 45 captures of
  actual story mornings/outings and chapter completion.
- All 32 final illustrations and all 64 catalog compositions were visually
  inspected, including identity, dress continuity and textbox clearance.
- Lint exited 0: no C05 warnings or asset-load failures. The existing 28 missing
  sprite warnings and one undefined `Yuuka` speaker warning in C07/C08 remain.

Total: 17 cases PASS, 151/151 assertions, 109 runtime screenshots. These checks
cover C05 itself; they do not claim a full C01-to-ending progression playthrough.

`chapter_five_branches` covers 15 full C05 playthroughs: Tam's three gift paths,
all three earring choices, confident/hesitant help, all excessive-gift responses,
Huyen's four album/printer configurations, three group outcomes and varied
self-acceptance/morning choices. It checks completion, exact outcome flags and
CG cleanup at each reached menu, with isolated test saves.

Run the visual catalog and chapter integration suites:

```powershell
$sdk = 'D:/RenPy/renpy-8.3.2-sdk'
$testSaves = Join-Path (Get-Location) 'tests/chapter_five_assets_saves'
foreach ($suite in @('chapter_five_assets', 'chapter_five_branches')) {
    & "$sdk/lib/py3-windows-x86_64/python.exe" "$sdk/renpy.py" . --savedir $testSaves test $suite --report-detailed --overwrite-screenshots
    if ($LASTEXITCODE -ne 0) { throw "Failed: $suite" }
}
```

The catalog renders all 32 images under the real textbox at 1920x1080 and
1280x720. Captures are in ignored `tests/screenshots/chapter_five_assets/` and
`tests/screenshots/chapter_five_branches/`. Test scripts and saves are excluded
from distribution builds by the existing `game/tests/**` and `tests/**` rules.

Inventory/narrative validation uses a separate Python environment, leaving the
Ren'Py SDK unchanged:

```powershell
$env:UV_PYTHON_INSTALL_DIR = Join-Path (Get-Location) 'tests/python_runtime'
uv run --python 3.12 --with pillow --no-project python tools/validate_chapter_five_assets.py
```

Run the SDK outside the restricted execution sandbox if it reports Illegal
System DLL Relocation. This session's SDK runs normally outside that sandbox.
