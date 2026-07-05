<!-- Context: project-intelligence/technical | Priority: critical | Version: 1.3 | Updated: 2026-07-05 -->

# Technical Domain

> Tech stack, runtime structure, progression architecture, naming, and contributor-safe coding patterns for this project.

## Quick Reference

- **Primary stack**: Ren'Py 8.x runtime, Ren'Py screen language, Python `init`/script blocks, PNG GUI assets
- **Update when**: stack, file layout, progression architecture, naming, or translation workflow changes
- **Key runtime files**: `game/script.rpy`, `game/progression_data.rpy`, `game/progression_logic.rpy`, `game/story_state.rpy`, `game/ending_rules.rpy`, `game/route_map.rpy`, `game/debug_progression.rpy`, `game/screens.rpy`, `game/gui.rpy`, `game/options.rpy`, `game/data/library_data.rpy`, `game/screens/library_screen.rpy`, `game/story_library.rpy`, `game/story_parser.rpy`, `game/story_player.rpy`, `game/smartphone/phone_state.rpy`, `game/smartphone/phone_logic.rpy`, `game/map_data.rpy`, `game/map_*_with_interactions.rpy`, `game/data/character_status_data.rpy`, `game/data/library_music_data.rpy`

## Core Concept

This project is a Ren'Py visual novel with a live data-driven progression system running across 8 routes, 36 chapters, and 24 endings. Runtime flow initializes progression state, enters a timeline-based route map (or location-based interactive map), tracks chapter unlocks with cross-route prerequisites and exclusions, and resolves ending eligibility through centralized metadata and condition helpers. A library system provides character profiles, Markdown-based custom story reading with investment points, and category-organized bonus content including a music room with 18 tracks. A smartphone simulation system (contacts, mail, social feed, messaging) and an interactive location map with free-time actions extend the gameplay surface beyond linear reading.

## Key Points

- Progression metadata in `game/progression_data.rpy`; progression rules/state in `game/progression_logic.rpy`; story scoring in `game/story_state.rpy`; ending conditions in `game/ending_rules.rpy`.
- Authored story content lives in `game/story/` organized by route/chapter folders; each chapter has a `_chapter.rpy` wrapper and `sNN_*.rpy` scene files.
- Library data lives in `game/data/`; screens in `game/screens/library_*.rpy`; story reader in `game/story_*.rpy`.
- Custom side stories for the library reader are Markdown files under `game/stories/`, registered via `game/stories/manifest.json`.
- Phone system lives in `game/smartphone/` (state + logic), `game/screens/phone_*.rpy` (UI), `game/data/phone_*.rpy` (contacts, mail, social, threads data).
- Interactive map is implemented across `game/map_data.rpy` + `game/map_*_with_interactions.rpy` (5 files) — location selection, free-time actions, time management.
- Keep locale files mirrored by source filename under `game/tl/vietnamese/`.
- Avoid hand-editing generated/runtime artifacts: `game/cache/`, `game/saves/`, `.rpyc`, `.rpymc`.
- Preserve the warm beige/brown UI palette and existing menu background usage unless intentionally redesigning.
- Ren'Py settings in `game/gui.rpy` and `game/options.rpy`.

## Primary Stack

| Layer | Technology | Notes |
|------|------------|-------|
| Engine | Ren'Py 8.x | Visual novel runtime and screen system |
| Scripting | Ren'Py script + Python blocks | Labels, `define`, `init python`, screen actions |
| Progression | Data-driven route/chapter metadata | Centralized in `progression_data.rpy` + `progression_logic.rpy` |
| Story state | Python dict with scoring | `story_state` default dict, character-specific variables |
| Library | Ren'Py screens + Markdown parser | 6 categories, custom story reader, investment points |
| Smartphone Simulation | Ren'Py screens + Python data | Contacts, mail, social feed, messaging threads; 8 files (~1,673 lines) |
| Interactive Map | Ren'Py screens + location data | Location selection, free-time actions, time management; 5 files (~2,819 lines) |
| UI | Ren'Py screens/styles | Core menus in `screens.rpy`, library UI in `screens/library_*.rpy` |
| Assets | PNG-based GUI theme | `game/gui/` images plus theme backgrounds |
| Localization | Ren'Py translation files | Mirrored locale files under `game/tl/vietnamese/` |

## Runtime Structure

| Area | Files | Role |
|------|-------|------|
| Bootstrap | `game/script.rpy` | Initializes progression, handles load-time refresh |
| Progression metadata | `game/progression_data.rpy` | 8 routes, 36 chapters, unlock graph, emotional effects, ending seeds |
| Progression logic | `game/progression_logic.rpy` | State init, availability, exclusions, validation, recommendations, route focus |
| Story state | `game/story_state.rpy` | Character scores (tam, hoang, yuuka, minh, thienan, huyen, work, minyuu) |
| Ending conditions | `game/ending_rules.rpy` | `can_get_*` helpers for all 24 endings |
| Ending resolver | `game/story/endings/ending_resolver.rpy` | Routes to correct ending label |
| Progression UI | `game/route_map.rpy`, `game/debug_progression.rpy` | Timeline chapter selection, diagnostics, resets |
| Authored story content | `game/story/` (202 files across 12 branches) | Prologue, tam, hoang, yuuka, flashback_minyuu, thienan, huyen, work, group, minyuu, final |
| Minigames | `game/minigames/` | Problem Diagnosis and Speech Ordering with global runtime |
| Library screens | `game/screens/library_screen.rpy`, `game/screens/library_subscreens.rpy` | Menu shell, character profiles, category listing |
| Library data | `game/data/library_data.rpy`, `game/data/library_music_data.rpy`, `game/data/character_status_data.rpy` | 21 character profiles, 6 categories, 18 music tracks, secret definitions |
| Story reader | `game/story_library.rpy`, `game/story_parser.rpy`, `game/story_player.rpy` | Markdown parsing, investment point system, reader screen |
| Custom side stories | `game/stories/` | Markdown files registered via `manifest.json` |
| Phone system | `game/smartphone/phone_state.rpy`, `game/smartphone/phone_logic.rpy`, `game/screens/phone_screen.rpy`, `game/screens/phone_subscreens.rpy`, `game/data/phone_contacts.rpy`, `game/data/phone_mail.rpy`, `game/data/phone_social.rpy`, `game/data/phone_threads.rpy` | Smartphone simulation with contacts, mail, social feed, messaging threads. 8 files (~1,673 lines total). |
| Interactive Map | `game/map_data.rpy`, `game/map_screen_with_interactions.rpy`, `game/map_logic_with_interactions.rpy`, `game/map_location_interactions.rpy`, `game/map_hub_with_interactions.rpy` | Location-based chapter selection, free-time actions, time management. 5 files (~2,819 lines). |
| Core UI/theme | `game/screens.rpy`, `game/gui.rpy`, `game/options.rpy` | Menus, styling, metadata, engine config |
| Custom main menu | `game/screens/screens_main_menu_custom.rpy` | Custom nav buttons, asset debug |
| Library styles | `game/styles/library_styles.rpy` | Library-specific style definitions |
| Supporting declarations | `game/scripts/` | Character sprites, backgrounds, CGs |
| Legacy demo | `game/demo_route_hoang.rpy` | Older Hoang POV/bonus flow with seed endings |
| Translation | `game/tl/vietnamese/` | Mirrors source filenames per locale |

## Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Files | lowercase role-based `.rpy` names | `progression_logic.rpy`, `route_map.rpy` |
| Screens/styles | snake_case identifiers | `route_map`, `debug_progression`, `library_menu_shell` |
| Labels | lowercase route/chapter-style names | `start`, `tam_c01_interview_day`, `ending_resolver` |
| Metadata constants | uppercase identifiers | `ROUTES`, `CHAPTERS`, `ROUTE_ORDER`, `CHARACTER_PROFILES` |
| Story chapters | `route_id_cNN_descriptive_name` | `tam_c01_interview_day`, `yuuka_c08_festival_arrival` |
| Chapter scene files | `sNN_descriptive_name.rpy` | `s01_first_context.rpy`, `s03_tam_choice.rpy` |
| Endings | `eNN_descriptive_name.rpy` | `e01_canon_true.rpy`, `e24_doom.rpy` |
| Config/theme values | `define config.*` / `define gui.*` | `define gui.accent_color` |
| Locale files | mirror source filename | `tl/vietnamese/route_map.rpy` |

## Contributor Standards

- Put unlock rules, recommendation logic, validation, and ending eligibility in the centralized progression files rather than scattering them across labels.
- When adding a chapter, add metadata to `CHAPTERS` in `progression_data.rpy`, add the chapter id to `CHAPTER_ORDER`, and create the corresponding label + `_chapter.rpy`/`sNN_*.rpy` files under `game/story/`.
- When adding a custom side story, add the Markdown file under `game/stories/` and register it in `manifest.json`.
- Check mirrored translation files under `game/tl/vietnamese/` before changing user-facing strings.
- Cross-check implementation docs with live runtime files; some roadmap text is now historical and not exact source of truth.
- Use the local Ren'Py launcher at `/home/hhnam/Applications/renpy/renpy.sh` for runtime validation.

## Safety Rules

- Do not edit generated files or runtime logs as source (`game/cache/`, `game/saves/`, `*.rpyc`, `*.rpymc`, `log.txt`, `traceback.txt`).
- Do not treat `game/saves/navigation.json` as authoritative source code.
- Do not assume `screens.rpy` is untouched boilerplate; it contains custom styling and both desktop/touch quick menu variants.
- Do not keep describing the project as scaffold-only; the project has a full progression system, ~194 authored story scenes, 8 routes, 24 endings, and a working library system.
- Do not edit source strings without checking mirrored translations in `game/tl/vietnamese/`.
- Do not use `text "[...]"` with bracket-wrapped strings without adding `substitute False` — Ren'Py interprets `[...]` as variable interpolation.
