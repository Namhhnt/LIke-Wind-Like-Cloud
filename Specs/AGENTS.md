# SPECS DOMAIN

## OVERVIEW
`Specs/` is product and implementation reference material: progression design, delivery planning, authoring guidance, sample story writing, and menu/background mockups. It informs implementation but is not loaded by Ren'Py at runtime.

## STRUCTURE
```text
Specs/
├── game_mechanics.md                  # Route/chapter unlock model and product target.
├── progression_implementation_plan.md # Delivery roadmap and historical implementation gaps.
├── chapter_authoring_guide.md         # How current runtime metadata/labels should be authored.
├── stories/                           # Story drafting/reference chapter content.
├── Design/                            # Main menu mockups.
└── Base_assets/                       # Reference backgrounds/buttons/title art.
```

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Route/chapter progression logic | `game_mechanics.md` | Most detailed product intent in the repo. |
| Runtime delivery status | `progression_implementation_plan.md` | Useful roadmap, but some "current gap" notes are now outdated by the live prototype. |
| Add new chapters using current runtime shape | `chapter_authoring_guide.md` | Documents the metadata keys and label patterns the prototype already uses. |
| Read drafted story content | `stories/` | Narrative references separate from executable `.rpy` scenes. |
| Main menu desktop/mobile targets | `Design/` | PNG mockups only. |
| Visual reference pieces | `Base_assets/` | Source/reference art, not runtime script. |

## CONVENTIONS
- Treat `game_mechanics.md` as the highest-signal design document.
- Treat `chapter_authoring_guide.md` as the fastest path to matching the live runtime authoring pattern.
- Treat images in `Design/` and `Base_assets/` as references for implementation decisions.
- When runtime behavior changes materially, update the spec if it changes route logic or menu intent.
- Keep roadmap/history docs honest: if implementation catches up, remove stale "not implemented" claims.

## ANTI-PATTERNS
- Do not confuse reference art with live assets under `game/gui/`.
- Do not implement large progression systems directly from memory when `game_mechanics.md` already defines data shapes and unlock concepts.
- Do not assume planning documents describe the current runtime perfectly; cross-check against `game/progression_*.rpy` and `game/route_map.rpy`.
- Do not let menu mockups drift from the actual Ren'Py UI without noting the mismatch.

## NOTES
- `game_mechanics.md` still reaches beyond the currently authored amount of story content, but the runtime now implements a meaningful slice of the progression model.
- `progression_implementation_plan.md` has become partly historical: it still helps explain intent, yet some Phase 1-4 items are already delivered.
- This folder is documentation-first; keep it concise and synchronized with real engine behavior.
