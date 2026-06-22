<!-- Context: project-intelligence/navigation | Priority: high | Version: 1.1 | Updated: 2026-06-22 -->

# Project Intelligence

> Quick routes for project-specific context used by agents and contributors.

## Quick Routes

| File | Description | Priority |
|------|-------------|----------|
| `technical-domain.md` | Stack, runtime layout, progression architecture, naming, safety rules | critical |

## Deep Dives

| Topic | Source |
|------|--------|
| Story/bootstrap entry | `/home/hhnam/Documents/Projects/LikeWindLikeCloud/game/script.rpy` |
| Progression metadata | `/home/hhnam/Documents/Projects/LikeWindLikeCloud/game/progression_data.rpy` |
| Progression logic | `/home/hhnam/Documents/Projects/LikeWindLikeCloud/game/progression_logic.rpy` |
| Route map / progression UI | `/home/hhnam/Documents/Projects/LikeWindLikeCloud/game/route_map.rpy` |
| Debug progression UI | `/home/hhnam/Documents/Projects/LikeWindLikeCloud/game/debug_progression.rpy` |
| Core menu/UI behavior | `/home/hhnam/Documents/Projects/LikeWindLikeCloud/game/screens.rpy` |
| Theme system | `/home/hhnam/Documents/Projects/LikeWindLikeCloud/game/gui.rpy` |
| Progression design target | `/home/hhnam/Documents/Projects/LikeWindLikeCloud/Specs/game_mechanics.md` |
| Implementation roadmap | `/home/hhnam/Documents/Projects/LikeWindLikeCloud/Specs/progression_implementation_plan.md` |
| Chapter authoring pattern | `/home/hhnam/Documents/Projects/LikeWindLikeCloud/Specs/chapter_authoring_guide.md` |

## 📂 Codebase References

- Root project guide: `/home/hhnam/Documents/Projects/LikeWindLikeCloud/AGENTS.md`
- Runtime domain guide: `/home/hhnam/Documents/Projects/LikeWindLikeCloud/game/AGENTS.md`
- Specs domain guide: `/home/hhnam/Documents/Projects/LikeWindLikeCloud/Specs/AGENTS.md`

## Notes

- The current repo is no longer scaffold-only: startup initializes progression state and jumps directly into a route-map flow.
- Tam is the default unlocked route; Hoang prototype POV/bonus content unlocks through chapter completion.
- Prefer the AGENTS files above for maintained high-level context, then drill into the listed `.rpy` and spec files.
