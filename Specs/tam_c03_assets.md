# Chapter 3 scene illustrations

Eight new CGs cover all eight narrative scenes. Generated with built-in ImageGen,
using the existing character portraits and location backgrounds as references.
Full prompts, ordered references and generation IDs are recorded in
`tam_c03_asset_prompts.json`. Runtime assets live under `game/images/assets/cg/`,
opaque 1920x1080 WebP, quality 94 with Lanczos fit.

## Identity and continuity

Tam, Thien An and Quang use their own portraits from
`game/images/characters/<name>/expressions/`. Thien An's defined face and low bun
remain distinct from Tam's longer half-up hair. Quang uses his youthful, gentle
portrait, never Quan's older stern face. The approved chapter-one collar CG is a
rendering reference only. Parents are viewed from behind or outside focus.

Tam wears a dusty-rose knit cardigan, ivory top and beige skirt. Thien An wears
an ivory blouse and charcoal trousers, hair tied low. Quang wears a pale-blue
open-collar shirt with charcoal tailoring. Keep these consistent within connected
scenes. Preserve the existing locations, including the daytime villa backgrounds
already used for the packing and gate scenes.

## Integration cues

Names below use the `cg_tam_c03_` prefix.

| Image | Show / cleanup |
| --- | --- |
| `thienan_sofa` | Thien An exhausted on sofa, open laptop on table; restore living room before choice of blanket, laptop or distance. |
| `quang_visit` | Quang outside the open doorway with gray document bag, Tam welcoming him; restore entry before he changes slippers and enters. Thien An must not appear early. |
| `trip_checklist` | Thien An and Quang check luggage with Tam observing from stairs; restore daytime living room before interpretation menu. |
| `family_dinner` | Tense pause at dinner, focus on the sisters and soup/rice bowls; restore dining room before Tam's response menu. |
| `sisters_balcony` | Both hold warm water and look toward street; restore balcony before the repeatable private-talk menu. |
| `quang_jacket` | Quang covers sleeping Thien An with jacket, closed laptop on table, Tam in background; restore living room before he turns toward Tam. |
| `quang_gifts` | Quang still holds paper bag of supplements, coffee and mints at gate; restore exterior before support choice and gift transfer. |
| `career_notebook` | Tam alone reads small navy notebook; pages face away so no generated lettering needs reading. Restore bedroom before Thien An's footsteps and entrance. |

## Validation

```powershell
& D:/RenPy/renpy-8.3.2-sdk/lib/py3-windows-x86_64/python.exe `
  D:/RenPy/renpy-8.3.2-sdk/renpy.py . `
  --savedir D:/Projects/RenPy_Games/LikeWindLikeCloud/tests/chapter_assets_saves `
  test chapter_three_assets --report-detailed --overwrite-screenshots
```

Four playthroughs vary family choices, all four Quang-support outcomes, all
career-notebook responses, and both full sister-topic depth and early silence.
They assert scene cleanup, branch flags and chapter completion and capture all
eight CGs at 1080p and 720p. Local captures are ignored under
`tests/screenshots/chapter_three_assets/`.

Verified on Windows with Ren'Py 8.5.4.26101301+nightly: all four playthroughs
passed, 56/56 assertions, 32 CG captures. All eight generated images and all eight
scene compositions in representative in-game captures were visually inspected,
including 1080p and 720p views. Final lint adds no warnings; existing Tam C07 and
Yuuka C08 warnings remain.

A normalized comparison against commit `78fc2fc` across all 17 chapter-two/three
story files confirmed unchanged narrative, menus, labels and scoring after
excluding scene/transition statements and the new image-only outfit selector.
All 19 new image declarations plus the retained premium CG decode as opaque
1920x1080 images (5.78 MiB total including the existing CG).

Narrative strings, translations, scoring and existing choice logic are unchanged.
