# Library-aligned menus — 2026-10-20

- Core PC menu shell (Settings, Save/Load, History, About, Help) now uses the
  Library's rainy café backdrop, translucent brown panels, gold hairline rims,
  smooth rounded corners, serif headings, and cached gold navigation icons.
- Selected navigation, radio/check controls, sliders, save cards, help tabs,
  pagination and confirmation dialogs use the same palette and state styling.
  Existing preference/save actions are retained. Developer shortcuts remain
  available after enabling Debugging Mode. Vietnamese “Preferences” is now
  consistently labelled “Cài đặt”. No story source text changed.
- Library overview has six equal 386×316 cards, 40px horizontal / 36px vertical
  gaps, centered in the right panel with balanced 42px horizontal insets.
- Side-story reader uses a centered 1280×720 (16:9) scene with a close-fitting
  24px outer mat rather than the old full-width, partially empty panel. Artwork,
  dialogue, portraits, page counter and inset previous/next buttons share this
  scene coordinate system. The scene clips its children; page buttons stay below
  the dialogue, and Back to Stories remains outside the frame.
- Existing cached panel/icon rendering is reused; no newly generated bitmap,
  continuous animation or per-frame progression refresh was added.

## Validation

`game/tests/ui_menu_refresh.rpy` exercises English and Vietnamese at 1920×1080
and 1280×720. It captures Settings, Load, Save, About, Help, History, Library,
the Sunday Market reader, and the confirmation modal; checks page navigation
and Escape behavior. Save is displayed without invoking a save operation.
Screenshots are written to ignored `tests/screenshots/ui_menu_refresh/`.

Run with the installed Windows SDK and isolated saves:

```powershell
& D:/RenPy/renpy-8.3.2-sdk/lib/py3-windows-x86_64/python.exe D:/RenPy/renpy-8.3.2-sdk/renpy.py D:/Projects/RenPy_Games/LikeWindLikeCloud --savedir D:/Projects/RenPy_Games/LikeWindLikeCloud/tests/ui_refresh_saves test ui_menu_refresh --overwrite-screenshots --report-detailed
```

Also run `test ui_refresh` for existing Map/Library/Phone coverage and
`test ui_performance` for cached factory and activity-state invariants.

Final Windows validation: menu suite 60/60 assertions, existing UI suite 48/48,
performance/state suite 5/5; all passed sequentially with isolated saves.
The menu suite also verifies the text-speed slider and Settings scrolling.
Visual captures were inspected at both resolutions. Lint exits successfully,
with the existing 28 missing story-sprite warnings and one undefined `Yuuka`
speaker warning outside this UI change. Mobile layout and full narrative
playthroughs are not covered by this validation.
