# PROJECT KNOWLEDGE BASE

**Generated:** 2026-06-20
**Commit:** 8d7937c
**Branch:** develop

## OVERVIEW
Small Ren'Py visual novel project. Runtime code is still mostly scaffold-level, while the real progression design lives in specs and the UI theme has already been customized.

## STRUCTURE
```text
LikeWindLikeCloud/
├── game/              # Executable Ren'Py scripts, translations, runtime artifacts.
├── Specs/             # Mechanics spec plus menu/background reference art.
├── .vscode/           # Local editor exclusions for Ren'Py generated files.
├── log.txt            # Recent Ren'Py session log.
└── traceback.txt      # Latest runtime failure details.
```

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Story entry | `game/script.rpy` | Currently default starter script. |
| Menus, save/load, preferences, help | `game/screens.rpy` | Main UI surface; includes desktop and touch variants. |
| Project metadata, version, build name | `game/options.rpy` | Window title, version, build-facing config. |
| Theme colors, sizes, menu backgrounds | `game/gui.rpy` | Warm palette and layout constants live here. |
| Translation work | `game/tl/` | Mirrors source filenames by locale. |
| Progression design | `Specs/game_mechanics.md` | Data model for routes, chapters, unlocks. |
| UI/design reference | `Specs/Design/`, `Specs/Base_assets/` | Mockups and visual reference only. |

## CODE MAP
No `.rpy` LSP is configured in this workspace. Use these file-level anchors instead:

| Symbol Area | Location | Role |
|-------------|----------|------|
| `label start` | `game/script.rpy` | Current story entry label. |
| `screen say`, `choice`, `navigation`, `main_menu`, `preferences` | `game/screens.rpy` | Core Ren'Py screen set. |
| Touch `screen quick_menu()` variant | `game/screens.rpy` near mobile section | Mobile override of the desktop quick menu. |
| `define gui.*` | `game/gui.rpy` | Visual system: colors, fonts, spacing, backgrounds. |
| `define config.*`, `build.name` | `game/options.rpy` | Game metadata and engine config. |
| Generated symbol index | `game/saves/navigation.json` | Runtime-produced location map; inspect, do not hand-maintain. |

## TOOLING
- Local Ren'Py SDK/runtime is available at `/mnt/d/RenPy/renpy-8.3.2-sdk`.
- For future runtime validation, launch the project with that SDK instead of assuming Ren'Py is on `PATH`.
- Prefer using the SDK when reproducing issues from `log.txt`, `traceback.txt`, or `errors.txt`.

## CONVENTIONS
- Hand-edited Ren'Py source lives in `game/*.rpy` and `game/tl/**`.
- GUI image assets live under `game/gui/`; behavior stays in `game/gui.rpy` and `game/screens.rpy`.
- Translation files mirror source filenames: `script.rpy` -> `tl/vietnamese/script.rpy`, etc.
- `.vscode/settings.json` hides `cache/`, `.rpyc`, and `.rpymc`; follow that lead when reviewing diffs.
- `game/libs/libs.txt` changes Ren'Py load order for files placed under `game/libs/`.

## ANTI-PATTERNS (THIS PROJECT)
- Do not edit generated/runtime files: `game/cache/`, `game/saves/`, `*.rpyc`, `*.rpymc`, `log.txt`, `traceback.txt`.
- Do not treat `game/saves/navigation.json` as source of truth; it is generated runtime output.
- Do not assume `game/screens.rpy` is untouched boilerplate; custom menu styling and a touch-only quick menu live there.
- Do not change source strings without checking the mirrored locale files under `game/tl/`.

## UNIQUE STYLES
- UI palette is warm beige/brown, not Ren'Py default blue.
- Both main menu and game menu backgrounds point at `gui/theme/background_full.png`.
- The project already contains PC/mobile visual references under `Specs/Design/` and `Specs/Base_assets/`.

## COMMANDS
```bash
# No project-local build/test scripts were found.
# Useful repo inspection commands used during analysis:
find game -maxdepth 3 -type f | sort
grep -RInE '^(label|screen|translate [^ ]+ strings|define )' game
```

## NOTES
- `Specs/game_mechanics.md` is more advanced than the current story scripts; implementation work should reconcile that gap explicitly.
- `traceback.txt` records a real translation failure: duplicate `old "Rolls forward to later dialogue."` entries in `game/tl/vietnamese/screens.rpy`.
