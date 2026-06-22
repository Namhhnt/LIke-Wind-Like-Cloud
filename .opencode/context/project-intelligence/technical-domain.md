<!-- Context: project-intelligence/technical | Priority: critical | Version: 1.1 | Updated: 2026-06-22 -->

# Technical Domain

> Tech stack, runtime structure, progression architecture, naming, and contributor-safe coding patterns for this project.

## Quick Reference

- **Primary stack**: Ren'Py 8.x runtime, Ren'Py screen language, Python `init`/script blocks, PNG GUI assets
- **Update when**: stack, file layout, progression architecture, naming, or translation workflow changes
- **Key runtime files**: `game/script.rpy`, `game/progression_data.rpy`, `game/progression_logic.rpy`, `game/route_map.rpy`, `game/debug_progression.rpy`, `game/screens.rpy`, `game/gui.rpy`, `game/options.rpy`

## Core Concept

This project is a Ren'Py visual novel with a live data-driven progression prototype rather than a pure starter scaffold. Runtime flow initializes progression state, enters a route map, tracks chapter unlocks across routes, supports exclusions and recommendations, and resolves prototype ending eligibility through centralized metadata and logic.

## Key Points

- Keep progression metadata in `game/progression_data.rpy` and progression rules/state transitions in `game/progression_logic.rpy`.
- Treat `game/route_map.rpy` and `game/debug_progression.rpy` as the progression-facing UI layer; keep core menu UI in `game/screens.rpy`.
- Story content is now split across root route/demo files and authored content folders like `game/stories/tam/`.
- Keep locale files mirrored by source filename under `game/tl/`.
- Avoid hand-editing generated/runtime artifacts such as `game/cache/`, `game/saves/`, `.rpyc`, and `.rpymc`.
- Preserve the warm beige/brown UI palette and existing menu background usage unless intentionally redesigning.

## Primary Stack

| Layer | Technology | Notes |
|------|------------|-------|
| Engine | Ren'Py 8.x | Visual novel runtime and screen system |
| Scripting | Ren'Py script + Python blocks | Labels, `define`, `init python`, screen actions |
| Progression | Data-driven route/chapter metadata | Centralized in `progression_data.rpy` + `progression_logic.rpy` |
| UI | Ren'Py screens/styles | Core menus in `screens.rpy`, progression UI in `route_map.rpy` |
| Assets | PNG-based GUI theme | `game/gui/` images plus theme backgrounds |
| Localization | Ren'Py translation files | Mirrored locale files under `game/tl/vietnamese/` |

## Runtime Structure

| Area | Files | Role |
|------|-------|------|
| Bootstrap | `game/script.rpy` | Initializes progression and handles load-time refresh |
| Metadata | `game/progression_data.rpy` | Route order, chapter list, unlock graph, flags, endings |
| Logic | `game/progression_logic.rpy` | Availability, exclusions, validation, recommendations, endings |
| Progression UI | `game/route_map.rpy`, `game/debug_progression.rpy` | Route selection and prototype diagnostics |
| Story content | `game/stories/tam/`, `game/demo_route_hoang.rpy` | Authored route scenes, bonus branches, prototype endings |
| Core UI/theme | `game/screens.rpy`, `game/gui.rpy`, `game/options.rpy` | Menus, styling, metadata, engine config |
| Supporting declarations | `game/scripts/` | Character sprites and shared backgrounds |

## Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Files | lowercase role-based `.rpy` names | `progression_logic.rpy`, `route_map.rpy` |
| Screens/styles | snake_case identifiers | `route_map`, `debug_progression` |
| Labels | lowercase route/chapter-style names | `start`, `tam_c01`, `hoang_h02` |
| Metadata constants | uppercase identifiers | `ROUTES`, `CHAPTERS`, `ROUTE_ORDER` |
| Config/theme values | `define config.*` / `define gui.*` | `define gui.accent_color` |
| Locale files | mirror source filename | `tl/vietnamese/route_map.rpy` |

## Contributor Standards

- Put unlock rules, recommendation logic, validation, and ending eligibility in the centralized progression files rather than scattering them across labels.
- When adding a chapter, update both the metadata object and the matching Ren'Py label.
- Check mirrored translation files before changing user-facing strings.
- Cross-check implementation docs with live runtime files; some roadmap text is now historical and not exact source of truth.
- Use the local Ren'Py SDK at `/mnt/d/RenPy/renpy-8.3.2-sdk` for future runtime validation instead of assuming `renpy` is on `PATH`.

## Safety Rules

- Do not edit generated files or runtime logs as source.
- Do not treat `game/saves/navigation.json` as authoritative source code.
- Do not assume `screens.rpy` is untouched boilerplate; it contains custom styling and both desktop/touch quick menu variants.
- Do not keep describing the project as scaffold-only; the current repo already implements a meaningful slice of the route progression model.
