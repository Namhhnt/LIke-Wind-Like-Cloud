<!-- Context: project-intelligence/navigation | Priority: high | Version: 1.2 | Updated: 2026-06-26 -->

# Project Intelligence

> Quick routes for project-specific context used by agents and contributors.

## Quick Routes

| File | Description | Priority |
|------|-------------|----------|
| `technical-domain.md` | Stack, runtime layout, progression architecture, naming, safety rules | critical |

## Deep Dives

| Topic | Source |
|------|--------|
| Story/bootstrap entry | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/script.rpy` |
| Progression metadata | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/progression_data.rpy` |
| Progression logic | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/progression_logic.rpy` |
| Story state / scoring | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/story_state.rpy` |
| Ending conditions | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/ending_rules.rpy` |
| Ending resolver | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/story/endings/ending_resolver.rpy` |
| Route map / progression UI | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/route_map.rpy` |
| Debug progression UI | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/debug_progression.rpy` |
| Library screens | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/screens/library_screen.rpy` |
| Library subscreens | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/screens/library_subscreens.rpy` |
| Library data | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/data/library_data.rpy` |
| Library story reader | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/story_library.rpy` |
| Story parser | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/story_parser.rpy` |
| Story player screen | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/story_player.rpy` |
| Core menu/UI behavior | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/screens.rpy` |
| Custom main menu | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/screens/screens_main_menu_custom.rpy` |
| Theme system | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/gui.rpy` |
| Progression design target | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/Specs/game_mechanics.md` |
| Implementation roadmap | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/Specs/progression_implementation_plan.md` |
| Chapter authoring pattern | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/Specs/chapter_authoring_guide.md` |
| Library design ref | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/Specs/library-screen.md` |
| Library story authoring | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/Specs/library_story_authoring_guide.md` |
| Minigame designs | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/Specs/Mini-games/` |
| Authored story content | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/story/` |
| Custom side stories (Markdown) | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/stories/` |
| Translation locale | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/tl/vietnamese/` |

## Codebase References

- Root project guide: `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/AGENTS.md`
- Runtime domain guide: `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/AGENTS.md`
- Specs domain guide: `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/Specs/AGENTS.md`

## Notes

- Startup initializes progression state and jumps directly into the route-map flow.
- Tam is the default unlocked route; 7 other routes unlock through chapter completion.
- The library system (Character Profiles, Original Stories, CG Gallery, Music Room, Minigames, Extras) is live with a Markdown-based story reader and investment point unlocks.
- ~194 authored scene files across 8 routes / 36 chapters / 24 endings in `game/story/`.
- Prefer the AGENTS files above for maintained high-level context, then drill into the listed `.rpy` and spec files.
