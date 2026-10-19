# UI refresh delivery — 2026-10-19

Branch: `codex/ui-refresh-approved` (from `chapter-08`).

## Implemented

- Main menu: clearer Continue/Start hierarchy, simplified title area, aligned navigation and shared warm panel styling.
- Map: existing city artwork and location coordinates retained; inspect/select pins before travel; locked travel disabled; bottom action inset from frame ornament; consolidated daily HUD.
- Timeline: centered selected chapter, clearer nodes and connectors, removed debug-facing noise, fixed cache signatures for native and rollback containers.
- Library: six-category overview with honest empty states; character list/detail layout using existing spoiler/unlock gates.
- Phone: common shell/header/footer across apps, consistent message rows and incoming/outgoing bubbles, separate reply area, in-game clock and predictable back navigation.
- Shared gold/brown scrollbars and Vietnamese translations for added UI labels.

The concept is implemented with live Ren'Py text, borders and pins, not flattened concept screenshots. Decorative borders are restrained procedural equivalents, not pixel-identical concept ornaments. Existing profile prose, location names and time-system data still contain untranslated English; this change does not rewrite narrative content.

## Verification

Windows SDK at `D:/RenPy/renpy-8.3.2-sdk` reports **Ren'Py 8.5.3.26051504**. Main menu, Library and Profiles were also inspected in the native game window.

Automated suite: English/Vietnamese × 1920×1080/1280×720; 4 test cases, 36 assertions. Covers screen opening, phone app/back navigation, chapter graph after progression and disabled travel for locked locations. Screenshots cover nine views per configuration under `tests/screenshots/ui_refresh/` (ignored by Git). Test saves are isolated under `tests/ui_refresh_saves/`; test scripts are excluded from distribution builds.

```powershell
& D:/RenPy/renpy-8.3.2-sdk/lib/py3-windows-x86_64/python.exe D:/RenPy/renpy-8.3.2-sdk/renpy.py D:/Projects/RenPy_Games/LikeWindLikeCloud --savedir D:/Projects/RenPy_Games/LikeWindLikeCloud/tests/ui_refresh_saves test ui_refresh --overwrite-screenshots --report-detailed
```

Lint exits 0 with the same 29 existing story warnings: 28 missing sprite attributes in chapters 7/8 and one undefined `Yuuka` speaker reference. No UI parse errors or duplicate translation warnings in the final run. `git diff --check` is clean.

This is desktop UI verification, not a full-route narrative regression or mobile-specific adaptation. Gameplay chapter dispatch and unlock rules were retained. Unrelated optimizer edits, project metadata and archives were not included.
