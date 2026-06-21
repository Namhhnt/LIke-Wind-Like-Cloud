# GAME DOMAIN

## OVERVIEW
`game/` is the executable Ren'Py runtime surface: story labels, screens, GUI constants, translations, and engine-generated artifacts.

## STRUCTURE
```text
game/
├── script.rpy        # Story labels.
├── screens.rpy       # Menus, overlays, history, save/load, help.
├── options.rpy       # Game metadata and engine config.
├── gui.rpy           # Theme constants and layout values.
├── tl/               # Per-locale translation mirrors.
├── gui/              # Image assets only.
├── libs/             # Optional preload area controlled by libs.txt.
├── cache/            # Generated.
└── saves/            # Runtime output, includes navigation.json.
```

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Add or replace story flow | `script.rpy` | Current script is still starter-template scale. |
| Change menu flow or buttons | `screens.rpy` | Desktop and touch variants both live here. |
| Change title/version/build metadata | `options.rpy` | `config.name`, `config.version`, `build.name`. |
| Change colors, fonts, spacing, menu backgrounds | `gui.rpy` | `define gui.*` values only. |
| Check symbol locations quickly | `saves/navigation.json` | Generated index, not editable source. |
| Add preload libraries | `libs/libs.txt` | Alters load order for `game/libs/`. |

## TOOLING
- Local Ren'Py SDK/runtime path: `/mnt/d/RenPy/renpy-8.3.2-sdk`.
- Use that SDK for future runtime launches, translation validation, and traceback reproduction.
- Do not assume `renpy` is installed globally or available on `PATH`.

## CONVENTIONS
- Keep behavior in `.rpy` files at the `game/` root; `game/gui/` is asset storage, not script logic.
- `screens.rpy` mixes stock Ren'Py scaffolding with custom styling; inspect before replacing sections wholesale.
- There are two `quick_menu()` definitions: desktop plus `variant "touch"` mobile override.
- `gui.rpy` is the central source for palette, sizing, and menu backgrounds.
- `config.check_conflicting_properties = True` is enabled; treat screen/style conflicts as real issues.

## ANTI-PATTERNS
- Do not hand-edit `cache/`, `saves/`, `.rpyc`, or `.rpymc` files.
- Do not add new runtime source under `game/gui/`; that directory is image-heavy and already crowded.
- Do not duplicate translated `old` strings when editing UI text; the current repo already has one collision in Vietnamese screens.
- Do not change screen text casually without checking matching locale files under `game/tl/`.

## NOTES
- `screens.rpy` is the largest source file in the repo by far; search for an existing screen before adding new UI patterns.
- `game/libs/libs.txt` means future vendor/shared code in `game/libs/` loads before the rest of `game/`.
