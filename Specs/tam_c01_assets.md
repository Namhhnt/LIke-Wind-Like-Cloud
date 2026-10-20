# Chapter 1 asset direction

Generated with built-in ImageGen on 2026-10-20, following `prologue_assets.md`.
Final images are opaque 1920×1080 WebP, quality 94, Lanczos fit. Existing images
are retained. No dialogue, translation strings, choices or scoring were changed.

## Identity and continuity

Use `game/images/characters/{tam,huyen,hoang}/expressions/*_neutral.webp` as
the respective identity references, never interchangeable faces. Tam has long
half-up dark hair; Huyen has shoulder-length dark hair with a loose half-up
ponytail and wispy bangs. Tam wears a white office blouse and beige skirt;
Huyen wears a powder-blue collared shirt and charcoal trousers throughout the
interview day and dinner. Hoang wears a dark navy blazer over charcoal shirt.

Style reference: `game/images/assets/cg/cg_tam_company_anniversary_party_01.webp`.
Keep its semi-realistic natural rendering, not the party dress. Full-bleed 16:9,
natural skin and hands, restrained depth of field, no text/logos/watermarks.
Keep faces and key gestures above the bottom 26% dialogue region. Anonymous
interviewers and background extras have occluded or out-of-focus faces.

## Images, prompts and story cues

| Name (`cg_tam_c01_` prefix) | Prompt / framing | Integration |
| --- | --- | --- |
| `collar_coffee` | Candid medium two-shot at Tam's front door. Tam left gently straightens Huyen's crooked collar; Huyen right holds two plain coffee cups in a cardboard carrier. Warm morning rim light, beige/wood/green apartment decor. | Collar adjustment through their teasing exchange; return to living room before coffee is placed on table. |
| `interview_portfolio` | From the panel side of the long wood table, Tam clearly presents an open portfolio. Exactly three anonymous interviewers frame her in soft foreground: two women and one man. Glass of water to her right, pen parallel to paper. Soft city-window daylight, controlled nervousness. Quân is absent. | Perfect and pass presentation labels after the ordering minigame. Skip retains the interview-room background. Restore room after the minigame returns. |
| `offer_hug` | Huyen leans across to hug Tam on lobby seating, both laughing in relief. Distinct recognizable faces, phone face-down on Tam's lap, portfolio beside seat. Candid diagonal medium two-shot, warm midday window light and marble lobby. | Common hug before all result-response choices; restore lobby before menu. |
| `celebration_toast` | Tam left and Huyen right gently touch stemless water glasses at chest height. Small white-tablecloth table, foreground candle bokeh, golden restaurant light against blue city windows. Same office clothes, friendship celebration. | First clink of glasses, before Hoang introduction. |
| `hoang_window` | Hoang alone beside the restaurant window, quiet reserved expression, gazing toward the city. 85mm three-quarter view, subject on right with negative space left, amber sidelight and blue rim. Hand beside wine glass, almost untouched dinner. | Establishing shot before he looks toward the women; return to restaurant background before his head turn and all notice-choice branches. |

Setting references under `game/images/assets/bg/`: `bg_tam_living_room_morning`,
`bg_interview_room`, `bg_company_lobby_noon`, `bg_luxury_restaurant_evening`.
The taxi passage now uses the existing `bg_taxi_interior_day` instead of carrying
the apartment lobby into the moving car.

Generation IDs: collar `62499726-d286-4c66-89b4-e547613dc697`, portfolio
`8f3c0dd9-6a43-40e7-a330-be581fd6aa4e`, hug
`e4e554e4-a8bb-471f-86d7-5e4990facfa5`, toast
`069bd70f-893e-4f5e-82ee-b693fc040375`. Hoang's initial image
`cebde1a6-c5c4-490c-95d4-2e5f75cab32c` received a targeted meal/wine correction;
the face, pose, framing and lighting were preserved. Final generation ID:
`967225af-19ee-4d16-a44d-7cd861af0d82`.

## Validation

Run the opening story suite with a separate save directory:

```powershell
& D:/RenPy/renpy-8.3.2-sdk/lib/py3-windows-x86_64/python.exe `
  D:/RenPy/renpy-8.3.2-sdk/renpy.py . `
  --savedir D:/Projects/RenPy_Games/LikeWindLikeCloud/tests/opening_assets_saves `
  test opening_assets --report-detailed --overwrite-screenshots
```

The suite plays through all seven scenes three times, varies story choices,
exercises perfect/pass/three failures then skip, checks image cleanup and chapter
completion, and captures the new backgrounds/CGs at 1080p and 720p. Screenshots
are local under ignored `tests/screenshots/opening_assets/`; saves are local only
and must not be committed. Lint has existing unrelated missing-sprite/character
warnings in Tam C07 and Yuuka C08.

Verified on Windows with Ren'Py 8.5.4.26101301+nightly (the installed SDK's
actual version): all 3 opening playthroughs passed, 41/41 assertions, 23 story
frames captured with representative frames inspected at 1080p/720p. The pre-existing UI suite also passed
48/48 assertions before asset work. All eight new images have valid declarations,
decode at 1920×1080 and total 2.61 MiB. A source comparison excluding only scene
and transition statements confirmed unchanged narrative, menus, labels and
scoring across all modified story/minigame files. Lint reports no warnings in
Prologue, C01, the changed speech minigame or the new test suite.
