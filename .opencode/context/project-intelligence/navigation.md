<!-- Context: project-intelligence/navigation | Priority: high | Version: 1.3 | Updated: 2026-07-05 -->

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
| Library minigame data | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/data/library_minigame_data.rpy` |
| Library music data | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/data/library_music_data.rpy` |
| Character status data | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/data/character_status_data.rpy` |
| Library story reader | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/story_library.rpy` |
| Story parser | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/story_parser.rpy` |
| Story player screen | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/story_player.rpy` |
| Phone state / logic | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/smartphone/phone_state.rpy`, `phone_logic.rpy` |
| Phone UI screens | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/screens/phone_screen.rpy`, `phone_subscreens.rpy` |
| Phone data | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/data/phone_contacts.rpy`, `phone_mail.rpy`, `phone_social.rpy`, `phone_threads.rpy` |
| Interactive Map screens | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/map_screen_with_interactions.rpy`, `map_hub_with_interactions.rpy` |
| Map logic / interactions | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/map_logic_with_interactions.rpy`, `map_location_interactions.rpy` |
| Map data | `/mnt/d/Projects/RenPy_Games/LikeWindLikeCloud/game/map_data.rpy` |
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
- The smartphone simulation (contacts, mail, social feed, messaging threads) is implemented across 8 files (~1,673 lines) but awaits in-story integration.
- The interactive map provides location-based chapter selection with free-time actions and time management (~2,819 lines across 5 files).
- 202 authored scene files across 8 routes / 36 chapters / 24 endings in `game/story/` (~9,300 lines).
- Prefer the AGENTS files above for maintained high-level context, then drill into the listed `.rpy` and spec files.
