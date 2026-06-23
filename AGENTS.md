# PROJECT KNOWLEDGE BASE

**Generated:** 2026-06-22
**Commit:** working tree
**Branch:** develop

## OVERVIEW
Ren'Py visual novel project with a custom warm-themed UI and an in-progress but already functional progression prototype. The repo now includes data-driven route/chapter state, a route map screen, debug progression tooling, seeded Tam/Hoang route content, and supporting authoring/design docs.

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
| Route map and progression UI | `game/route_map.rpy` | Main prototype progression surface and route selection screen. |
| Debug progression UI | `game/debug_progression.rpy` | Validation, reset, completion shortcuts, acceptance summaries. |
| Story content and chapter labels | `game/stories/` | Authored Tam route scenes and minigame labels live here. |
| Demo Hoang route and endings | `game/demo_route_hoang.rpy` | POV/bonus chapter flow plus prototype ending resolution. |
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
| `label tam_c01`, `tam_c02`, `tam_c03` | `game/stories/tam/**` | Current authored Tam route chapter entry points. |
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
- Story content is starting to move into domain folders like `game/stories/tam/`, while sprite/background declarations live under `game/scripts/`.
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
- The current playable prototype centers on Tam as the default unlocked route, then unlocks Hoang POV/bonus content through chapter completion.
- Progression runtime already tracks recommendations, route focus, emotional state, relationship directions, validation issues, and seeded ending eligibility.

## COMMANDS
```bash
# No project-local build/test scripts were found.
# Useful repo inspection commands used during analysis:
find game -maxdepth 3 -type f | sort
grep -RInE '^(label|screen|translate [^ ]+ strings|define )' game
```

## NOTES
- `Specs/game_mechanics.md` still represents the broad product target, but runtime has partially caught up through a data-driven prototype rather than remaining pure scaffold.
- `Specs/progression_implementation_plan.md` now contains historical gap statements that no longer match the live runtime exactly.
- `traceback.txt` records a real translation failure: duplicate `old "Rolls forward to later dialogue."` entries in `game/tl/vietnamese/screens.rpy`.
