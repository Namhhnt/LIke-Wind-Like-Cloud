# UI consistency — review gate

## Status

Four runnable samples are isolated from live navigation pending visual approval:
Settings, Library, Phone conversation, and the Sunday Market reader. Existing
production menus remain in place. Review screens and their translation file are
excluded from distribution builds.

This is phase 1 of the agreed plan, not completion of the full UI migration.
After approval: extract accepted sample patterns into shared production
components, migrate menus/Library, then gameplay screens and responsive layouts.

## Design decisions

- Warm café artwork, restrained gold outlines, Noto Serif, more opaque reading
  surfaces and distinct selected indicators.
- Settings: desktop two columns; compact tabs with large controls and thin slider
  tracks inside larger hit areas.
- Library: equal 3×2 desktop cards; two-column compact scrolling grid.
- Phone: desktop handset and thread list; compact full-width conversation with
  a separate list view. Replies use local preview state only.
- Reader: desktop 16:9 artwork and dialogue overlay. Per user correction,
  compact/mobile uses fullscreen artwork, overlaid dialogue, and icon-only
  back/previous/next/hide/show controls. No side-by-side reading pane on mobile.
- Sample profiles are explicit parameters, not automatic device detection.
  Automatic profile selection and device safe-area integration belong to the
  subsequent production migration.

## Review and reproduction

With the developer console, `renpy.show_screen("ui_review_hub")` opens the sample
selector. Its PC / Mobile landscape switch changes the profile. These are review
screens: Library cards do not open production categories; Phone reply simulation
does not change story state. Settings use actual Ren'Py preference actions, so
use the isolated test save directory when evaluating them.

```powershell
& D:/RenPy/renpy-8.3.2-sdk/lib/py3-windows-x86_64/python.exe `
  D:/RenPy/renpy-8.3.2-sdk/renpy.py `
  D:/Projects/RenPy_Games/LikeWindLikeCloud `
  --savedir D:/Projects/RenPy_Games/LikeWindLikeCloud/tests/ui_review_saves `
  test ui_review_samples --overwrite-screenshots --report-detailed
```

The suite captures English/Vietnamese at 1920×1080, 960×540 and 800×450. It checks
screen entry, compact settings tabs, Library scrolling, phone list navigation,
reader previous/next and hide/show. Captures are under
`tests/screenshots/ui_review_samples/`.

Final verification after the fullscreen-reader correction: 6/6 parameterized
cases, 64/64 assertions passed on the installed Windows Ren'Py runtime
(8.5.4 nightly). Screenshot review included compact Settings tabs, Library,
Phone, and fullscreen Reader. No claim of full production migration is made.

Windows viewport simulations do not establish real-device touch usability,
safe-area behavior, contrast compliance or performance on mobile hardware.
Authored phone/story copy is reused unchanged; existing untranslated or
unaccented narrative content is not rewritten as part of the layout samples.
