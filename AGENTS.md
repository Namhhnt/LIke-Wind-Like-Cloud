# PROJECT KNOWLEDGE BASE

**Generated:** 2026-06-26
**Commit:** working tree
**Branch:** library-screen (based on develop)

## OVERVIEW
Ren'Py visual novel with a warm custom-themed UI, a full data-driven progression system across 8 routes / 36 chapters / 24 endings, a recent Library screen with character profiles and custom side stories, and a large authored chapter tree under `game/story/`. The project has moved beyond prototype scaffold into a playable multi-route narrative with branching endings.

## STRUCTURE
```text
LikeWindLikeCloud/
├── game/              # Executable Ren'Py scripts, progression runtime, story content, assets, translations.
├── Specs/             # Mechanics spec, implementation docs, authored chapter references, design art.
├── .opencode/         # Agent/project intelligence context files.
├── .vscode/           # Local editor exclusions for Ren'Py generated files.
├── log.txt            # Recent Ren'Py session log.
└── traceback.txt      # Latest runtime failure details.
```

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Story/bootstrap entry | `game/script.rpy` | Initializes progression state and jumps to `route_map`. |
| Route/chapter metadata | `game/progression_data.rpy` | 8 routes (tam, hoang, yuuka, minh, thienan, huyen, work, final), 36 chapters, unlock graph, endings seeds. |
| Progression state/logic | `game/progression_logic.rpy` | State init, unlock recalculation, recommendations, route focus, validation, ending helpers. |
| Story state/scoring | `game/story_state.rpy` | Character-specific score variables for all 8 character tracks. |
| Ending conditions | `game/ending_rules.rpy` | Condition helpers (can_get_*) for all 24 endings. |
| Ending resolver | `game/story/endings/ending_resolver.rpy` | Route to the correct ending label. |
| Route map and progression UI | `game/route_map.rpy` | Timeline-based chapter selection surface with bookmarks. |
| Debug progression UI | `game/debug_progression.rpy` | State inspection, reset, completion shortcuts, acceptance summaries. |
| Library system | `game/data/library_data.rpy`, `game/screens/library_screen.rpy`, `game/screens/library_subscreens.rpy` | 6 categories, 21 character profiles, custom styles. |
| Library story reader | `game/story_library.rpy`, `game/story_parser.rpy`, `game/story_player.rpy` | Markdown side story parser + reader screen with investment point system. |
| Library minigame data | `game/data/library_minigame_data.rpy` | Minigame replay data for the library. |
| Main story content (authored) | `game/story/` | ~194 scene files across prologue, tam, hoang, yuuka, flashback_minyuu, thienan, huyen, work, group, minyuu, final branches. |
| Legacy/demo Hoang route | `game/demo_route_hoang.rpy` | Older POV/bonus demo labels and seed-ending flow. |
| Custom side stories | `game/stories/` | Markdown files for library custom stories reader. |
| Menus, save/load, preferences, help | `game/screens.rpy` | Core Ren'Py UI surface; includes desktop and touch variants. |
| Custom main menu | `game/screens/screens_main_menu_custom.rpy` | Main menu with custom nav buttons and asset debug. |
| Project metadata, version, build name | `game/options.rpy` | Window title, version (1.0), build-facing config. |
| Theme colors, sizes, menu backgrounds | `game/gui.rpy` | Warm palette and layout constants. |
| Styles | `game/styles/library_styles.rpy` | Library-specific style definitions. |
| Character/background declarations | `game/scripts/` | Sprites (tam, hoang, yuuka, minh, thienan, huyen, quan, thienan) + backgrounds + CGs. |
| Translation work | `game/tl/` | Mirrors source filenames by locale (Vietnamese). |
| Minigames | `game/minigames/` | Problem Diagnosis + Speech Ordering, with global minigame runtime. |
| Progression design | `Specs/game_mechanics.md` | Data model for routes, chapters, unlocks (still valid reference). |
| Implementation roadmap | `Specs/progression_implementation_plan.md` | All implementation phases checked complete. |
| Chapter-writing guidance | `Specs/chapter_authoring_guide.md` | Documents the live metadata/label authoring pattern. |
| UI/design reference | `Specs/Design/`, `Specs/Base_assets/` | Mockups and visual reference for menu/background assets. |

## CODE MAP
No `.rpy` LSP is configured in this workspace. Use these file-level anchors instead:

| Symbol Area | Location | Role |
|-------------|----------|------|
| `label start` / `label after_load` | `game/script.rpy` | Progression bootstrap and load-time refresh hooks. |
| `ROUTES`, `CHAPTERS`, `CHAPTER_ORDER` | `game/progression_data.rpy` | Canonical progression metadata. |
| `initialize_progression()`, `complete_chapter()`, `refresh_validation_state()` | `game/progression_logic.rpy` | Core runtime progression engine. |
| `screen route_map`, `label route_map` | `game/route_map.rpy` | Main progression navigation surface. |
| `screen debug_progression` | `game/debug_progression.rpy` | Prototype-only diagnostics and reset tools. |
| `screen library_menu_shell` | `game/screens/library_screen.rpy` | Shared library shell screen. |
| `screen library_characters`, `library_character_card` | `game/screens/library_subscreens.rpy` | Character profile listing and card UI. |
| `CHARACTER_PROFILES`, `LIBRARY_CATEGORIES` | `game/data/library_data.rpy` | Library metadata and data definitions. |
| `story_state` (default dict) | `game/story_state.rpy` | All character score variables. |
| `ending_resolver` label | `game/story/endings/ending_resolver.rpy` | Ending dispatch. |
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
- Progression metadata lives in `game/progression_data.rpy` and `game/progression_logic.rpy`.
- Story content lives in route/chapter folders under `game/story/`. Each chapter has a `_chapter.rpy` wrapper plus `sNN_*.rpy` scene files.
- Sprite/background/CG declarations live under `game/scripts/`.
- GUI image assets live under `game/gui/`; behavior stays in `game/gui.rpy` and `game/screens.rpy`.
- Library data lives in `game/data/` (library_data.rpy, library_minigame_data.rpy).
- Custom side stories for the library are Markdown files in `game/stories/`.
- Translation files mirror source filenames and subfolders under `game/tl/`.
- `game/libs/libs.txt` changes Ren'Py load order for files placed under `game/libs/`.
- `.vscode/settings.json` hides `cache/`, `.rpyc`, and `.rpymc`.

## ANTI-PATTERNS (THIS PROJECT)
- Do not edit generated/runtime files: `game/cache/`, `game/saves/`, `*.rpyc`, `*.rpymc`, `log.txt`, `traceback.txt`.
- Do not treat `game/saves/navigation.json` as source of truth; it is generated runtime output.
- Do not assume `game/screens.rpy` is untouched boilerplate; custom menu styling and a touch-only quick menu live there.
- Do not assume `Specs/progression_implementation_plan.md` is current source of truth for missing features; all phases are checked complete.
- Do not change source strings without checking the mirrored locale files under `game/tl/`.

## UNIQUE STYLES
- UI palette is warm beige/brown, not Ren'Py default blue.
- Both main menu and game menu backgrounds point at `gui/theme/background_full.png`.
- The project contains PC/mobile visual references under `Specs/Design/` and `Specs/Base_assets/`.
- Progression runtime tracks recommendations, route focus, emotional state, relationship directions, validation issues, and seeded ending eligibility across 8 routes and 24 endings.
- Library system supports 6 content categories, 21 character profiles, and Markdown-based custom story reading with investment point unlocks.
- The current playable build starts on Tâm by default; all 8 routes have authored content in the story tree.

## COMMANDS
```bash
# No project-local build/test scripts were found.
# Useful repo inspection commands used during analysis:
find game -maxdepth 3 -type f | sort
grep -RInE '^(label|screen|translate [^ ]+ strings|define )' game
```

## NOTES
- `traceback.txt` currently records a translation issue: duplicate `old` entries in `game/tl/vietnamese/screens.rpy`.
- The most recent work added custom side stories (Yuuka/Minh "Sunday Market") with CG assets and fixed a bracket interpolation bug in the character profiles screen.
