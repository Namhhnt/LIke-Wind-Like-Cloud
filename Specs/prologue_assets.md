# Prologue asset direction

Generated with the built-in ImageGen tool on 2026-10-20. Final files are opaque
1920×1080 WebP, quality 94, Lanczos fit from the generated 1672×941 originals.
Existing backgrounds and character portraits remain unchanged.

## Shared direction

Semi-realistic, elegant natural rendering matching the existing Tam party CG;
soft natural skin, believable materials, restrained depth of field, no cartoon
outlines. Full-bleed 16:9, no typography/logos/watermarks/letterboxing. Keep faces
and significant gestures above the bottom 26% occupied by the dialogue box.
Use portrait references for identity, setting references for spatial continuity,
and the party CG for rendering only, never its dress in other story contexts.

## Assets and generation prompts

| Image name | Scene / insertion | Prompt |
| --- | --- | --- |
| `bg_prologue_rain_street_night` | Rain meeting, after chapter title | Empty contemporary Vietnamese street at night in fine drizzle, seen beneath a closed shop awning. Rolled shutter left, wet sidewalk, long blurred amber lamp reflections across blue-gray asphalt. Human eye-height 35mm environmental view, dreamlike loneliness; no people or umbrella. |
| `cg_prologue_umbrella_touch` | Immediately before the man adjusts the umbrella; return to street when he fades | Tam holds a gray umbrella beneath the same awning. A tall slim man in a dark coat straightens its rib, fingers near hers. Over his blurred shoulder, Tam's recognizable face left-center, hands and mechanism in upper frame. His face remains unreadable in shadow and rain; never reveal his identity. Pale blouse and dark skirt, not party dress. |
| `cg_prologue_tam_wakes` | Tam sits up; return to bedroom before the slippers description | Adult Tam sits upright in her pink bed after an unsettling dream, hand over upper chest on modest opaque cream pajamas, weary eyes toward the left window. Cream curtains, wood headboard and beige wardrobe match bedroom. Intimate three-quarter view, soft dawn light; no readable phone screen. |

References: `game/images/characters/tam/expressions/tam_neutral.webp` (identity),
`game/images/assets/cg/cg_tam_company_anniversary_party_01.webp` (style),
`game/images/assets/bg/bg_tam_room_morning.webp` (bedroom).
The generated rain background was also supplied as the umbrella CG's setting.

Original generation IDs: background `49456fbc-d085-4ede-8da8-812e562ab7e8`,
umbrella `1235de2f-ab7e-4996-8b2a-a2c05e613a00`,
waking `755c8be9-604c-4341-8bd5-a1a910345161`.

## Integration

Declarations follow the existing `bg_*` / `cg_*` convention. No dialogue,
translation strings, choices, scoring, or chapter wrappers are changed.
The dream fades to black before its recollection menu. The waking CG appears
only after Tam sits up and ends before she leaves the bed.
