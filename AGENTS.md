# PROJECT KNOWLEDGE BASE

**Generated:** 2026-07-05
**Commit:** working tree
**Branch:** chapter_03 (based on develop)

## OVERVIEW
Ren'Py visual novel with a warm custom-themed UI, a full data-driven progression system across 8 routes / 36 chapters / 24 endings, a Library screen with character profiles and custom side stories, a newly introduced smartphone simulation system, an interactive location-based map, a music room with 18 tracks, and a large authored chapter tree under `game/story/` (202 files, ~9,300 lines). The project has moved beyond prototype scaffold into a playable multi-route narrative with branching endings and growing secondary systems.

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
| Library music data | `game/data/library_music_data.rpy` | 18 music tracks scanned from `game/audio/music/` with chapter unlock gates. |
| Character status data | `game/data/character_status_data.rpy` | Per-character runtime status (job, inventory, known info). |
| Phone/smartphone system | `game/smartphone/phone_state.rpy`, `game/smartphone/phone_logic.rpy` | Phone state, logic, contacts, mail, social, threads. Newly implemented. |
| Phone UI screens | `game/screens/phone_screen.rpy`, `game/screens/phone_subscreens.rpy` | Phone main screen, messaging, contacts, social feed, notifications. |
| Phone data | `game/data/phone_contacts.rpy`, `game/data/phone_mail.rpy`, `game/data/phone_social.rpy`, `game/data/phone_threads.rpy` | Contacts, mail, social posts, and messaging threads data. |
| Interactive Map | `game/map_data.rpy`, `game/map_screen_with_interactions.rpy`, `game/map_logic_with_interactions.rpy`, `game/map_location_interactions.rpy`, `game/map_hub_with_interactions.rpy` | Location-based chapter selection, free-time actions, time management. |
| Main story content (authored) | `game/story/` | 202 scene files across prologue, tam, hoang, yuuka, flashback_minyuu, thienan, huyen, work, group, minyuu, final branches. |
| Legacy/demo Hoang route | `game/demo_route_hoang.rpy` | Older POV/bonus demo labels and seed-ending flow. |
| Custom side stories | `game/stories/` | Markdown files for library custom stories reader. |
| Menus, save/load, preferences, help | `game/screens.rpy` | Core Ren'Py UI surface; includes desktop and touch variants. |
| Custom main menu | `game/screens/screens_main_menu_custom.rpy` | Main menu with custom nav buttons and asset debug. |
| Project metadata, version, build name | `game/options.rpy` | Window title, version (1.0), build-facing config. |
| Theme colors, sizes, menu backgrounds | `game/gui.rpy` | Warm palette and layout constants. |
| Styles | `game/styles/library_styles.rpy` | Library-specific style definitions. |
| Character/background declarations | `game/scripts/` | Sprites (tam, hoang, yuuka, minh, thienan, huyen, quan, thienan) + backgrounds + CGs. |
| Translation work | `game/tl/` | Mirrors source filenames by locale (`game/tl/english/`, `game/tl/vietnamese/`). |
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
- Local Ren'Py runtime is available at `/home/hhnam/Applications/renpy` or `/mnt/d/RenPy/renpy-8.3.2-sdk`.
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
- Do not change source strings without checking the mirrored locale files under `game/tl/`. English TL files (`game/tl/english/story/`) mirror the `game/story/` folder structure with `translate english strings:` blocks containing `old`/`new` entry pairs. Every Vietnamese source string, `"..."` silence, and English menu choice requires a matching `old` entry — missing entries fall back to source text, duplicate or stale entries produce Ren'Py warnings.

## UNIQUE STYLES
- UI palette is warm beige/brown, not Ren'Py default blue.
- Both main menu and game menu backgrounds point at `gui/theme/background_full.png`.
- The project contains PC/mobile visual references under `Specs/Design/` and `Specs/Base_assets/`.
- UI palette is warm beige/brown, not Ren'Py default blue.
- Both main menu and game menu backgrounds point at `gui/theme/background_full.png`.
- The project contains PC/mobile visual references under `Specs/Design/` and `Specs/Base_assets/`.
- Progression runtime tracks recommendations, route focus, emotional state, relationship directions, validation issues, and seeded ending eligibility across 8 routes and 24 endings.
- Library system supports 6 content categories, 21 character profiles, and Markdown-based custom story reading with investment point unlocks.
- The current playable build starts on Tâm by default; all 8 routes have authored content in the story tree.

## FEATURE STATUS
### — Complete / Production —
| Feature | Status | Notes |
|---------|--------|-------|
| Custom Main Menu | **DONE** | Custom warm-themed UI with fallback assets; PC-first 1920x1080. |
| Progression Engine | **DONE** | 8 routes, 36 chapters, full unlock graph, prerequisites, exclusions, recommendations, route focus, relationship directions, emotional state, debug screen/commands. All phases in impl plan checked. |
| Route Map / Timeline | **DONE** | Timeline chapter selection with bookmarks, available/locked/hidden/excluded states. |
| Library Shell | **DONE** | 6 categories (Characters, Stories, CG, Music, Minigames, Extras), card-based navigation, warm palette matching main menu. |
| Character Profiles | **DONE** | 21 profiles with unlocked/locked states per playthrough. |
| Minigame Runtime | **DONE** | Two minigames: Problem Diagnosis, Speech Ordering. Global runtime. |
| Interactive Map | **DONE** | Location-based chapter selection with fixed + temp locations, unlock logic, label dispatch, free-time actions, time management. |
| Character Sprites (side) | **DONE** | 7 characters with 30+ expressions each. Expanded Hoàng, Quân, Quang sprite sets in working tree. |
| Background / CG Definitions | **DONE** | Background and CG image declarations. |
| Story Parser | **DONE** | Markdown/txt parser for custom Library stories. |
| Investment Points Engine | **DONE** | Point earning/spending for story unlocks, tied to manifest.json. |

### — Has Content, Needs Authoring Iteration —
| Feature | Status | Notes |
|---------|--------|-------|
| Prologue (Rain Dream) | **DONE** | 3 scene files, ~420 lines, full dialogue. |
| Tam Route C01 (Interview Day) | **DONE** | 4 files, ~1,300 lines, full dialogue. Eng TL synced. |
| Tam Route C02 (Company Party) | **DONE** | 7 files, ~1,900 lines, authored content. Eng TL synced. |
| Tam Route C03 (Thiên An Family) | **DONE** | 8 files, ~1,580 lines, full dialogue. Branching choices with Thiên An/Quang. Eng TL synced. |
| Tam Route (remaining chapters) | **SKELETON** | C05, C06, C07, C20a, C20b — scaffold-level scene structure with branching choices, minimal dialogue (~67-89 lines each). |
| Flashback Minyuu | **AUTHORED** | ~570 lines across 33 files, authored backstory content. |

### — Skeleton / Scaffold (Minimal Content) —
| Feature | Status | Notes |
|---------|--------|-------|
| Hoang Route | **SKELETON** | ~176 lines across 10 files. Scene structure exists, needs dialogue. |
| Yuuka Route | **SKELETON** | ~385 lines across 23 files. Some authored segments, mostly scaffold. |
| Thiên An Route | **SKELETON** | ~159 lines across 9 files. Choice branches defined, no dialogue. |
| Huyền Route | **SKELETON** | ~90 lines across 5 files. Basic scene structure. |
| Work / Group Route | **SKELETON** | ~258 lines across 15 files. Scene headers and choice points. |
| Minyuu Route (c19a-c19c, c23a-c23c) | **SKELETON** | Scene structure with branch choices, minimal prose. |
| Final Route (c24) | **SKELETON** | ~168 lines across 6 files. Doom/canon check logic exists. |

### — Needs Content / Placeholder —
| Feature | Status | Notes |
|---------|--------|-------|
| Ending Narratives (e01-e24) | **STUB** | All 24 ending labels exist with condition helpers (`can_get_*`), but each is an ~11-line stub with no narrative content. Only `ending_resolver.rpy` has real routing logic. |
| CG Gallery | **STUB** | Category exists in library; no CG entries populated. |
| Music Room | **IMPL** | 18 tracks scanned from `game/audio/music/`, play/pause/stop UI, chapter-unlock gating. Fully functional. |
| Extras | **STUB** | Category exists; screen with SECRET_DEFINITIONS framework; content minimal. |

### — Partially Implemented / Needs Polish —
| Feature | Status | Notes |
|---------|--------|-------|
| English Translations | **PARTIAL** | 137 TL files (7,499 lines). Prologue + Tam C01 + Tam C02 clean-synced. Other routes have TL coverage but may be out of sync with source changes. |
| Vietnamese TL | **KNOWN ISSUE** | `traceback.txt` reports duplicate `old` entries in `game/tl/vietnamese/screens.rpy`. |
| Library Stories | **3 STORIES** | Tam (2) + Yuuka/Minh (1). Reader, parser, investment unlock work. Needs more content. |
| Interactive Map | **BASIC** | Implemented but likely needs content tuning. Some features from spec (temporary location locking, animation) may not be fully wired. |
| Phone/Smartphone System | **NEW/BETA** | UI, state management, contacts/mail/social/threads data all implemented. Awaiting gameplay integration — no in-story phone usage calls yet. |
| Mobile Adaptation | **NOT STARTED** | PC-first. Touch quick menu exists; no tablet/phone layout adaptation. |
| Full-size Character Sprites | **NOT STARTED** | Only side sprites defined. No full-body character art. |
| Main Menu BG Assets | **FALLBACK** | Uses `gui/theme/background_full.png`. Design mockups exist but may not match final art. |

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
- Prologue and Tam C01 English translation files were synced to reflect updated story lines (7 TL files under `game/tl/english/story/prologue/prologue_rain_dream/` and `game/tl/english/story/tam/tam_c01_interview_day/`). Every Vietnamese source string and `"..."` silence has a matching `translate english strings:` entry; no orphan entries remain. The sync was automated via a Python extraction/parsing pipeline.
- Tam Route C03 (Thiên An Family) was recently completed with 8 scene files (~1,580 lines), introducing branching choices involving Thiên An and Quang and expanding the authored story content significantly.
- The smartphone simulation system (phone_state, phone_logic, phone screens, plus contacts/mail/social/threads data) was implemented across 8 files (~1,673 lines total). It is structurally complete and integrated into the game bootstrap, but has no in-story phone usage calls yet — awaiting narrative integration.
- The interactive map was redesigned with location interactions, free-time actions, time management, and hub navigation (~2,819 lines across 5 files).
- Hoàng and Quân/Quang sprite sets were significantly expanded in the working tree with new expression variants and updated file naming conventions.
- Ending condition helpers (`can_get_*`) were refined with additional validation through `story_has_ending_support()` pattern.
