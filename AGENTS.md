# PROJECT KNOWLEDGE BASE

**Generated:** 2026-06-22
**Commit:** working tree
**Branch:** develop

## OVERVIEW
Ren'Py visual novel project with a custom warm-themed UI and a data-driven progression runtime that now spans a full multi-route chapter map. The repo includes route/chapter state, route-map and debug tooling, a broad authored `game/story/` chapter tree across Tam/Hoàng/Yuuka/Minh-plus-final branches, and supporting authoring/design docs.

## STRUCTURE
```text
LikeWindLikeCloud/
├── game/              # Executable Ren'Py scripts, progression runtime, story content, assets.
├── Specs/             # Mechanics spec, implementation docs, authored chapter references, design art.
├── .vscode/           # Local editor exclusions for Ren'Py generated files.
├── log.txt            # Recent Ren'Py session log.
└── traceback.txt      # Latest runtime failure details.
```

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Story/bootstrap entry | `game/script.rpy` | Initializes progression state and jumps to `route_map`. |
| Route/chapter metadata | `game/progression_data.rpy` | Central route list, chapter schema, unlock graph, endings seeds. |
| Progression state/logic | `game/progression_logic.rpy` | Initialization, unlock recalculation, validation, recommendations, endings. |
| Route map and progression UI | `game/route_map.rpy` | Main progression surface and route selection screen. |
| Debug progression UI | `game/debug_progression.rpy` | Validation, reset, completion shortcuts, acceptance summaries. |
| Story content and chapter labels | `game/story/` | Authored chapter wrappers and scene files for the current route map live here. |
| Legacy/demo Hoang route and endings | `game/demo_route_hoang.rpy` | Older POV/bonus demo labels and seed-ending flow still present alongside the newer chapter tree. |
| Menus, save/load, preferences, help | `game/screens.rpy` | Core Ren'Py UI surface; includes desktop and touch variants. |
| Project metadata, version, build name | `game/options.rpy` | Window title, version, build-facing config. |
| Theme colors, sizes, menu backgrounds | `game/gui.rpy` | Warm palette and layout constants live here. |
| Character/background declarations | `game/scripts/` | Sprite declarations and shared scene/background definitions. |
| Translation work | `game/tl/` | Mirrors source filenames by locale. |
| Progression design | `Specs/game_mechanics.md` | Data model for routes, chapters, unlocks. |
| Implementation roadmap | `Specs/progression_implementation_plan.md` | Tracks delivered vs planned progression milestones. |
| Chapter-writing guidance | `Specs/chapter_authoring_guide.md` | Documents the live metadata/label authoring pattern. |
| UI/design reference | `Specs/Design/`, `Specs/Base_assets/` | Mockups and visual reference for menu/background assets. |

## CODE MAP
No `.rpy` LSP is configured in this workspace. Use these file-level anchors instead:

| Symbol Area | Location | Role |
|-------------|----------|------|
| `label start` / `label after_load` | `game/script.rpy` | Progression bootstrap and load-time refresh hooks. |
| `ROUTES`, `CHAPTERS`, `CHAPTER_ORDER` | `game/progression_data.rpy` | Canonical progression metadata for the playable prototype. |
| `initialize_progression()`, `complete_chapter()`, `refresh_validation_state()` | `game/progression_logic.rpy` | Core runtime progression engine. |
| `screen route_map`, `label route_map` | `game/route_map.rpy` | Main progression navigation surface. |
| `screen debug_progression` | `game/debug_progression.rpy` | Prototype-only diagnostics and reset tools. |
| `label prologue_rain_dream`, `tam_c01_interview_day`, `tam_c02_company_party` | `game/story/**/_chapter.rpy` | Current chapter entry labels live in per-chapter wrapper files across the story tree. |
| `label hoang_h01`, `hoang_bonus_*`, `hoang_h02` | `game/demo_route_hoang.rpy` | Hoang POV/bonus prototype and ending gateway. |
| `screen say`, `choice`, `navigation`, `main_menu`, `preferences` | `game/screens.rpy` | Core Ren'Py screen set. |
| Touch `screen quick_menu()` variant | `game/screens.rpy` near mobile section | Mobile override of the desktop quick menu. |
| `define gui.*` | `game/gui.rpy` | Visual system: colors, fonts, spacing, backgrounds. |
| `define config.*`, `build.name` | `game/options.rpy` | Game metadata and engine config. |
| Generated symbol index | `game/saves/navigation.json` | Runtime-produced location map; inspect, do not hand-maintain. |

## TOOLING
- Local Ren'Py runtime is available at `/home/hhnam/Applications/renpy`.
- Preferred launcher for validation is `/home/hhnam/Applications/renpy/renpy.sh` rather than assuming `renpy` is on `PATH`.
- When reproducing issues from `log.txt`, `traceback.txt`, or `errors.txt`, use that local launcher unless the user points to a different install.
- `.rpy` LSP is not configured in this workspace, so file-level anchors and text search remain the primary navigation tools.

## CONVENTIONS
- Hand-edited Ren'Py source lives in `game/*.rpy` and `game/tl/**`.
- Progression metadata currently lives directly in `game/progression_data.rpy` and `game/progression_logic.rpy`, not yet under a `systems/` subtree proposed by older planning docs.
- Story content now lives in route/chapter folders under `game/story/`, while sprite/background declarations live under `game/scripts/`.
- GUI image assets live under `game/gui/`; behavior stays in `game/gui.rpy` and `game/screens.rpy`.
- Translation files mirror source filenames and subfolders: `script.rpy` -> `tl/vietnamese/script.rpy`, `stories/tam/chapter_02_scene_01.rpy` -> `tl/vietnamese/stories/tam/chapter_02_scene_01.rpy`.
- `.vscode/settings.json` hides `cache/`, `.rpyc`, and `.rpymc`; follow that lead when reviewing diffs.
- `game/libs/libs.txt` changes Ren'Py load order for files placed under `game/libs/`.

## ANTI-PATTERNS (THIS PROJECT)
- Do not edit generated/runtime files: `game/cache/`, `game/saves/`, `*.rpyc`, `*.rpymc`, `log.txt`, `traceback.txt`.
- Do not treat `game/saves/navigation.json` as source of truth; it is generated runtime output.
- Do not assume `game/screens.rpy` is untouched boilerplate; custom menu styling and a touch-only quick menu live there.
- Do not assume `Specs/progression_implementation_plan.md` is current source of truth for missing features; several Phase 1-4 items are already implemented in runtime files.
- Do not change source strings without checking the mirrored locale files under `game/tl/`.

## UNIQUE STYLES
- UI palette is warm beige/brown, not Ren'Py default blue.
- Both main menu and game menu backgrounds point at `gui/theme/background_full.png`.
- The project already contains PC/mobile visual references under `Specs/Design/` and `Specs/Base_assets/`.
- The current playable build still starts on Tam by default, but the progression graph and chapter labels now cover a much broader route map through Hoàng, Yuuka, work/group, Minh-Yuuka resolution branches, and the final route.
- Progression runtime already tracks recommendations, route focus, emotional state, relationship directions, validation issues, and seeded ending eligibility.

## COMMANDS
```bash
# No project-local build/test scripts were found.
# Useful repo inspection commands used during analysis:
find game -maxdepth 3 -type f | sort
grep -RInE '^(label|screen|translate [^ ]+ strings|define )' game
```

## NOTES
- `Specs/game_mechanics.md` still represents the broad product target, but the runtime has moved well beyond scaffold status into a large authored chapter tree backed by the live progression system.
- `Specs/progression_implementation_plan.md` now contains historical gap statements that no longer match the live runtime exactly.
- `traceback.txt` records a real translation failure: duplicate `old "Rolls forward to later dialogue."` entries in `game/tl/vietnamese/screens.rpy`.
