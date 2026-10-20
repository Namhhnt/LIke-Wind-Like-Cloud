# Chapter 4 assets — option 1

## Inventory and backup

`tam_c04_cg_backup.md` preserves the pre-generation shot list with weeks, cast,
locations and descriptions, followed by all 139 source scene labels. The working
inventory is `tam_c04_asset_manifest.json`; exact prompts and ordered references
are in `tam_c04_asset_prompts.json`. Runtime insertion anchors and restore
backgrounds are recorded in `tam_c04_asset_integration.json`.

Budget: 38 CGs (22 reusable tableaux, 16 highlights), six backgrounds and one
recurring-character reference sheet for Anh Nhi. Sources are generated with the
built-in ImageGen tool. Runtime images are opaque 1920x1080 WebP, quality 94.
The identity sheet lives in `Specs/Design/`, outside the shipped runtime.

## Art direction

Use each existing character's own portrait. Huyen additionally follows the
approved chapter-one collar CG: compact face, short chin, natural eyes,
shoulder-length layered half-up hair. Tam has a longer oval face and long hair.
Quan and Quang retain separate identities. Anh Nhi is an approximately eight-year-old
Vietnamese girl with two low pigtails, wispy bangs, yellow cardigan and navy skirt;
all her CGs use the same new reference sheet.

The work capsule is Tam's white blouse/beige skirt and Huyen's powder-blue
blouse/charcoal trousers. Home scenes use Tam's dusty-rose cardigan and Huyen's
lavender knit. Thien An wears ivory and charcoal; Quang pale blue and charcoal;
Hoang navy and a light shirt; Quan charcoal and a dark shirt. Reusing this capsule
over six months is an intentional economy, not a claim that all scenes occur on
one day. Neutral common tableaux do not imply relationship commitments.

Important faces, hands and action sit above the bottom quarter reserved for the
textbox. Gaze follows partners/actions. Documents and phone screens never require
generated text to be read. The new apartment backgrounds have matching day/night
layouts and are reused as location references.

## Integration behavior

CGs illustrate bounded beats in the existing dialogue and restore an appropriate
BG immediately afterward. This deliberately prevents static common props or
gestures from persisting into later actions, menu outcomes or another scene.
The existing script conditions own every romantic branch; no image selector
changes story flags, scoring, menu conditions or translations.

Week 18's hand contact and confession appear only after the corresponding route
choice. Week 24's Tam finale selects the existing Hoang, Quang or independent
branch. Quang/Thien An scenes retain their existing exclusion when Tam chooses
Quang. Quan is only on the video-call screen in the week-23 dinner image.

Some scenes use existing/new BGs rather than forcing a common tableau that would
show the wrong action or cast. In week 14 Huyen folds a child's jacket alone while
Anh Nhi sleeps offscreen; the historical ID `huyen_nhi_quan_home` names that family
thread, not two visible characters. State-only monthly snapshots need no CG.

Chapter-agnostic career bonus scenes and optional free-time location content are
outside this chapter's 139-scene inventory and retain their existing assets.

## Verification

Verified on Windows with Ren'Py 8.5.4.26101301+nightly:

- `tools/validate_chapter_four_assets.py`: 45 opaque RGB images at 1920x1080,
  44 runtime declarations, all 38 CGs used, 13.71 MiB including the identity sheet.
  All 141 chapter source files preserve narrative, menus, scoring and control flow
  against `60c06cb` after removing only scene/transition statements and comments.
- `chapter_four_assets`: two cases passed, 4/4 assertions; all 38 CGs rendered
  under the real textbox at both native 1920x1080 and 1280x720 (76 screenshots).
  All source images and all compositions were visually reviewed; hand contact,
  final evaluation folders and spare key were reframed for textbox clearance.
- `chapter_four_asset_branches`: three cases passed, 28/28 assertions, six actual
  story screenshots. Tests play the week-18 decision and its three outcomes,
  week-19 first meeting, week-24 Tam finale, Quang/Thien An exclusion and blanket
  finale; CGs are absent at the checked menus/scene boundaries.
- `chapter_four_family_assets`: three cases passed, 24/24 assertions, three actual
  dinner screenshots. Covers every option at school pickup, spare key, school
  bridge and sleepover, plus the independent group dinner and Huyen/Hoang corridor.
- Final lint: no chapter-four or asset-load warnings. The 29 existing warnings
  remain in Tam C07 (Linh/Truong/Mai sprites), Yuuka C08 (Van sprites and `Yuuka`
  speaker). This work does not change those chapters.

Total: eight cases, 56/56 assertions, 85 screenshots. These are isolated scene and
visual acceptance tests, not a full 24-week route-map playthrough. The unchanged
weekly progression wrappers were not modified. Common CGs cover 133 bounded beats
across 124 scene labels; eight other narrative scenes and the closing scene use
backgrounds. Six state-only monthly snapshots retain their existing behavior.

Use the installed SDK with isolated `tests/chapter_assets_saves`; screenshots and
review sheets remain local under ignored `tests/screenshots/`. Example:

```powershell
& D:/RenPy/renpy-8.3.2-sdk/lib/py3-windows-x86_64/python.exe `
  D:/RenPy/renpy-8.3.2-sdk/renpy.py . `
  --savedir D:/Projects/RenPy_Games/LikeWindLikeCloud/tests/chapter_assets_saves `
  test chapter_four_assets --report-detailed --overwrite-screenshots
```

Run the other two suite names with the same command. For inventory validation:

```powershell
uv run --with pillow --no-project python tools/validate_chapter_four_assets.py
```
