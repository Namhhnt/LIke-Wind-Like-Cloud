# SPECS DOMAIN

## OVERVIEW
`Specs/` is product and implementation reference material: progression design, delivery planning, authoring guidance, sample story writing, UI mockups, and library design docs. It informs implementation but is not loaded by Ren'Py at runtime.

## STRUCTURE
```text
Specs/
├── game_mechanics.md                  # Route/chapter unlock model and product target.
├── progression_implementation_plan.md # Delivery roadmap — all phases now complete.
├── chapter_authoring_guide.md         # How runtime metadata/labels should be authored.
├── library-screen.md                  # Library system design reference.
├── library_story_authoring_guide.md   # How to write Markdown side stories for the library reader.
├── stories_reader.md                  # Custom stories reader spec.
├── Visual_Novel_timeline.md           # Timeline/chapter-map visual design reference.
├── timeline-chapter-map.md            # Timeline UI spec.
├── main_game-menu.md                  # Main menu design spec.
├── chapter-map_diagram_draft.md       # Route/chapter relationship diagram.
├── Mini-games/                        # Tam's speech + Problem Diagnosis design docs.
├── stories/                           # Story drafting/reference chapter content (Chapter 01-02 Tam).
├── Design/                            # Main menu mockups.
└── Base_assets/                       # Reference backgrounds/buttons/title art.
```

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Route/chapter progression logic | `game_mechanics.md` | Most detailed product intent in the repo; still valid reference. |
| Runtime delivery status | `progression_implementation_plan.md` | All phases checked complete; live runtime has surpassed the roadmap. |
| Add new chapters using current runtime shape | `chapter_authoring_guide.md` | Documents the metadata keys and label patterns the prototype uses. |
| Library system design | `library-screen.md` | Library UI/UX reference still valid. |
| Write side stories for the library reader | `library_story_authoring_guide.md` | Markdown format, frontmatter, CG reference patterns. |
| Custom stories reader technical spec | `stories_reader.md` | Story player parser/reader architecture. |
| Timeline/chapter map visual design | `Visual_Novel_timeline.md`, `timeline-chapter-map.md` | UI reference for the route map screen. |
| Main menu desktop/mobile targets | `Design/`, `main_game-menu.md` | PNG mockups and UI spec. |
| Read drafted story content | `stories/` | Narrative references separate from executable `.rpy` scenes. |
| Visual reference pieces | `Base_assets/` | Source/reference art, not runtime script. |

## CONVENTIONS
- Treat `game_mechanics.md` as the highest-signal design document.
- Treat `chapter_authoring_guide.md` as the fastest path to matching the live runtime authoring pattern.
- Treat `library_story_authoring_guide.md` as reference for writing Markdown-based side stories.
- Treat images in `Design/` and `Base_assets/` as references for implementation decisions.
- When runtime behavior changes materially, update the spec if it changes route logic or menu intent.
- Keep roadmap/history docs honest: if implementation catches up, remove stale "not implemented" claims.

## ANTI-PATTERNS
- Do not confuse reference art with live assets under `game/gui/`.
- Do not implement large progression systems directly from memory when `game_mechanics.md` already defines data shapes and unlock concepts.
- Do not assume planning documents describe the current runtime perfectly; cross-check against `game/progression_*.rpy`, `game/route_map.rpy`, and `game/screens/*.rpy`.
- Do not let menu mockups drift from the actual Ren'Py UI without noting the mismatch.
- Do not write side stories without checking the manifest pattern in `game/stories/manifest.json`.

## NOTES
- `game_mechanics.md` still reaches beyond the currently authored amount of story content, but the runtime now implements a meaningful slice of the progression model.
- `progression_implementation_plan.md` has become partly historical: its phases are all checked complete but the live codebase has evolved beyond the original plan structure.
- The library system (Character Profiles, Original Stories, CG Gallery, Music Room, Minigames, Extras) is implemented with a full screen shell, 21 character profiles, and a Markdown-based custom story reader with investment points.
- Two minigames are documented in Specs and implemented in `game/minigames/`: Problem Diagnosis and Speech Ordering.
- This folder is documentation-first; keep it concise and synchronized with real engine behavior.
