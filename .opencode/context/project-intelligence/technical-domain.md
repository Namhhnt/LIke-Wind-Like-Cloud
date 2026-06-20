<!-- Context: project-intelligence/technical | Priority: critical | Version: 1.0 | Updated: 2026-06-20 -->

# Technical Domain

> Tech stack, runtime structure, naming, and contributor-safe coding patterns for this project.

## Quick Reference

- **Primary stack**: Ren'Py 8.5.x, Ren'Py screen language, Python init/script blocks, PNG GUI assets
- **Update when**: stack, file layout, naming, or translation workflow changes
- **Key runtime files**: `game/script.rpy`, `game/screens.rpy`, `game/gui.rpy`, `game/options.rpy`

## Core Concept

This project is a Ren'Py visual novel with most executable logic concentrated in a few top-level `.rpy` files. Story flow is still scaffold-level, while UI theming and translation structure are already established and should be preserved.

## Key Points

- Keep runtime logic in `game/*.rpy`; do not hide new behavior inside asset folders.
- Treat `game/screens.rpy` as the main UI behavior file and `game/gui.rpy` as the visual constants file.
- Keep locale files mirrored by source filename under `game/tl/`.
- Avoid hand-editing generated/runtime artifacts such as `game/cache/`, `game/saves/`, `.rpyc`, and `.rpymc`.
- Preserve the warm beige/brown UI palette and existing menu background usage unless intentionally redesigning.

## Primary Stack

| Layer | Technology | Notes |
|------|------------|-------|
| Engine | Ren'Py 8.5.x | Visual novel runtime and screen system |
| Scripting | Ren'Py script + Python blocks | Labels, `define`, `init python`, screen actions |
| UI | Ren'Py screens/styles | Menus, history, preferences, touch variant |
| Assets | PNG-based GUI theme | `game/gui/` images plus theme backgrounds |
| Localization | Ren'Py translation files | Mirrored locale files under `game/tl/vietnamese/` |

## Code Patterns

### Runtime Structure

- `script.rpy` for story labels and dialogue entry points
- `screens.rpy` for screens, menus, overlays, and quick-menu variants
- `gui.rpy` for colors, fonts, spacing, and menu backgrounds
- `options.rpy` for game metadata and engine configuration

### Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Files | lowercase role-based `.rpy` names | `script.rpy`, `screens.rpy` |
| Screens/styles | snake_case identifiers | `quick_menu`, `main_menu` |
| Labels | lowercase label names | `label start` |
| Config/theme values | `define config.*` / `define gui.*` | `define gui.accent_color` |
| Locale files | mirror source filename | `tl/vietnamese/screens.rpy` |

## Contributor Standards

- Put story progression code in explicit labels rather than scattered screen-side logic.
- Update mirrored locale files when changing player-facing strings.
- Reuse existing screen/style patterns before adding new UI structures.
- Treat `Specs/game_mechanics.md` as product intent when implementing progression systems.

## Security / Safety Requirements

- Prefer built-in Ren'Py actions and static assets over ad hoc dynamic behavior.
- Do not treat generated files as source of truth.
- Keep translation `old` strings unique per locale file to avoid startup failures.
- Avoid silent drift between runtime files and referenced specs/translations.

## Minimal Example

```renpy
define e = Character("Eileen")

label start:
    scene bg room
    show eileen happy
    e "You've created a new Ren'Py game."
    return
```

## 📂 Codebase References

- **Story entry**: `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/script.rpy`
- **UI behavior**: `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/screens.rpy`
- **Theme constants**: `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/gui.rpy`
- **Engine metadata**: `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/options.rpy`
- **Translations**: `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/tl/vietnamese/screens.rpy`
- **Product spec**: `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/Specs/game_mechanics.md`

## Reference

- Project intelligence standard: `/home/m3noa/.opencode/context/core/standards/project-intelligence.md`
