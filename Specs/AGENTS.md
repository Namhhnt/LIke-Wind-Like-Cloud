# SPECS DOMAIN

## OVERVIEW
`Specs/` is reference material: gameplay design plus visual mockups. It informs implementation but is not loaded by Ren'Py at runtime.

## STRUCTURE
```text
Specs/
├── game_mechanics.md   # Route/chapter unlock model.
├── Design/             # Main menu mockups.
└── Base_assets/        # Reference backgrounds/buttons/title art.
```

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Route/chapter progression logic | `game_mechanics.md` | Most detailed product intent in the repo. |
| Main menu desktop/mobile targets | `Design/` | PNG mockups only. |
| Visual reference pieces | `Base_assets/` | Source/reference art, not runtime script. |

## CONVENTIONS
- Treat `game_mechanics.md` as the highest-signal design document.
- Treat images in `Design/` and `Base_assets/` as references for implementation decisions.
- When runtime behavior changes materially, update the spec if it changes route logic or menu intent.

## ANTI-PATTERNS
- Do not confuse reference art with live assets under `game/gui/`.
- Do not implement large progression systems directly from memory when `game_mechanics.md` already defines data shapes and unlock concepts.
- Do not let menu mockups drift from the actual Ren'Py UI without noting the mismatch.

## NOTES
- `game_mechanics.md` describes a much richer interwoven-route system than the current `game/script.rpy` implements.
- This folder is documentation-first; keep it concise and synchronized with real engine behavior.
