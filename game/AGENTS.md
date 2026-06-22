# GAME DOMAIN

## OVERVIEW
`game/` is the executable Ren'Py runtime surface: progression metadata and logic, route-map/debug UI, authored story labels, theme assets, translations, and engine-generated artifacts.

## STRUCTURE
```text
game/
├── script.rpy             # Bootstrap entry and after-load hooks.
├── progression_data.rpy   # Routes, chapters, unlock graph, ending seeds.
├── progression_logic.rpy  # State init, unlock recalculation, validation, endings.
├── route_map.rpy          # Main progression selection UI.
├── debug_progression.rpy  # Prototype/debug UI for state inspection and resets.
├── demo_route_hoang.rpy   # Hoang POV/bonus demo flow and prototype endings.
├── stories/               # Authored route scenes and minigame labels.
├── scripts/               # Sprite declarations and shared backgrounds.
├── screens/               # Extra screen fragments used by story/minigame flows.
├── screens.rpy            # Menus, overlays, history, save/load, help.
├── options.rpy            # Game metadata and engine config.
├── gui.rpy                # Theme constants and layout values.
├── tl/                    # Per-locale translation mirrors.
├── gui/                   # Image assets only.
├── libs/                  # Optional preload area controlled by libs.txt.
├── cache/                 # Generated.
└── saves/                 # Runtime output, includes navigation.json.
```

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Change game bootstrap flow | `script.rpy` | Initializes progression state, then jumps to route map. |
| Edit route/chapter metadata | `progression_data.rpy` | Route order, chapter graph, flags, exclusions, endings. |
| Edit progression rules | `progression_logic.rpy` | Unlock logic, route status, recommendations, validation. |
| Change progression navigation UI | `route_map.rpy` | Main chapter selection and recommendation surface. |
| Change prototype debug tools | `debug_progression.rpy` | State inspection, reset, and forced completion actions. |
| Add Hoang prototype beats/endings | `demo_route_hoang.rpy` | POV/bonus branch and ending-resolution labels. |
| Add or expand Tam chapter content | `stories/tam/` | Current authored route content and minigame flow. |
| Add sprites/background declarations | `scripts/` | Character images and shared background setup. |
| Change menu flow or buttons | `screens.rpy` | Desktop and touch variants both live here. |
| Change title/version/build metadata | `options.rpy` | `config.name`, `config.version`, `build.name`. |
| Change colors, fonts, spacing, menu backgrounds | `gui.rpy` | `define gui.*` values only. |
| Check symbol locations quickly | `saves/navigation.json` | Generated index, not editable source. |
| Add preload libraries | `libs/libs.txt` | Alters load order for `game/libs/`. |

## TOOLING
- Local Ren'Py SDK/runtime path: `/mnt/d/RenPy/renpy-8.3.2-sdk`.
- Use that SDK for future runtime launches, translation validation, and traceback reproduction.
- Do not assume `renpy` is installed globally or available on `PATH`.
- There is no `.rpy` language server in this workspace; rely on file reads, text search, and navigation artifacts.

## CONVENTIONS
- Runtime behavior now spans both root `.rpy` files and content folders like `stories/`, `scripts/`, and `screens/`; check existing placement before creating new files.
- `progression_data.rpy` + `progression_logic.rpy` are the source of truth for unlock state, validation, recommendations, and prototype ending eligibility.
- `screens.rpy` mixes stock Ren'Py scaffolding with custom styling; inspect before replacing sections wholesale.
- There are two `quick_menu()` definitions: desktop plus `variant "touch"` mobile override.
- `gui.rpy` is the central source for palette, sizing, and menu backgrounds.
- `config.check_conflicting_properties = True` is enabled; treat screen/style conflicts as real issues.

## ANTI-PATTERNS
- Do not hand-edit `cache/`, `saves/`, `.rpyc`, or `.rpymc` files.
- Do not add new runtime source under `game/gui/`; that directory is image-heavy and already crowded.
- Do not duplicate translated `old` strings when editing UI text; the current repo already has one collision in Vietnamese screens.
- Do not keep calling the runtime scaffold-only; route map, validation, recommendations, and prototype endings already exist.
- Do not change screen text casually without checking matching locale files under `game/tl/`.

## NOTES
- `route_map.rpy` and `debug_progression.rpy` are now the main entry points for progression-facing UI work; avoid re-implementing that logic inside `screens.rpy` unless it truly belongs in core menus.
- The playable prototype currently centers on Tam route chapters (`tam_c01`, `tam_c02`, `tam_c03`) and a Hoang branch (`hoang_h01`, `hoang_bonus_*`, `hoang_h02`).
- `game/libs/libs.txt` means future vendor/shared code in `game/libs/` loads before later source files; account for load order when introducing shared utilities.
