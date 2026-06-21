# Chapter Authoring Guide

## Purpose

Use this guide when adding or editing route chapters in the current progression system. It documents the real metadata keys and label flow already implemented in `game/progression_data.rpy`, `game/progression_logic.rpy`, and the demo route scripts.

## Where To Edit

- Chapter metadata: `game/progression_data.rpy`
- Progression rules: `game/progression_logic.rpy`
- Route map / debug UI: `game/route_map.rpy`, `game/debug_progression.rpy`
- Demo chapter labels: `game/demo_route_tam.rpy`, `game/demo_route_hoang.rpy`

## Minimal Chapter Pattern

Every playable chapter needs two pieces:

1. A chapter object in `CHAPTERS`
2. A Ren'Py label whose name matches the chapter `label`

Example:

```python
"tam_c01": {
    "id": "tam_c01",
    "route": "tam",
    "type": "core",
    "timeline_position": 10,
    "title": "First Morning",
    "label": "tam_c01",
    "prerequisites": [],
    "unlocks": ["tam_c02"],
}
```

```renpy
label tam_c01:
    "Chapter content here."
    $ complete_chapter("tam_c01")
    jump route_map
```

## Chapter Types

Use `type` to describe narrative role:

- `core` - main event chapter
- `pov` - alternate point-of-view chapter
- `bonus` - optional chapter with meaningful consequences
- `extra` - optional content that is not required for core flow

The current demo uses:

- `tam_c01`, `tam_c02`, `tam_c03` as `core`
- `hoang_h01` as `pov`
- `hoang_bonus_restraint`, `hoang_bonus_confession` as `bonus`

## How To Unlock Another Chapter Or Route

Add target chapter ids to `unlocks`, and add any hard requirements to the target chapter's `prerequisites`.

Example: Tam unlocks Hoang.

```python
"tam_c02": {
    "unlocks": ["hoang_h01"],
}

"hoang_h01": {
    "prerequisites": ["tam_c02"],
}
```

This is the pattern for cross-route unlocks too. A route becomes visible because one of its chapters becomes available.

## How To Make Two Chapters Mutually Exclusive

Put both chapters in the same `exclusion_group`, and make each one list the other in `excludes`.

```python
"hoang_bonus_restraint": {
    "type": "bonus",
    "exclusion_group": "hoang_direction_01",
    "excludes": ["hoang_bonus_confession"],
}

"hoang_bonus_confession": {
    "type": "bonus",
    "exclusion_group": "hoang_direction_01",
    "excludes": ["hoang_bonus_restraint"],
}
```

When one completes, the other is pushed into `excluded` and can no longer be selected.

## How To Soft-Hide A Chapter

Use `soft_hide_until_any_completed` when a chapter should stay hidden until one of several other chapters is completed.

```python
"hoang_h02": {
    "soft_hide_until_any_completed": [
        "hoang_bonus_restraint",
        "hoang_bonus_confession",
    ],
}
```

This is a temporary hide, not a hard exclusion.

## How To Make A Bonus Or Extra Chapter Matter

Bonus chapters can do all of these at once:

- unlock later chapters via `unlocks`
- exclude other chapters via `excludes`
- set player flags via `flags_set`
- set character-only knowledge via `character_flags_set`
- set relationship direction via `relationship_directions_set`
- modify hidden emotional values via `emotional_effects`
- unlock menu options via `choice_unlocks`

Example:

```python
"hoang_bonus_restraint": {
    "type": "bonus",
    "unlocks": ["tam_c03", "hoang_h02"],
    "relationship_directions_set": {"hoang": ["restraint"]},
    "emotional_effects": {"distance": -1, "trust": 1},
    "choice_unlocks": ["ask_gently"],
}
```

## How To Require A Direction Before A Chapter Unlocks

Use `required_directions` on the blocked chapter.

```python
"tam_c03": {
    "prerequisites": ["tam_c02"],
    "required_directions": {
        "hoang": ["restraint", "confession"],
    },
}
```

That means Tam's chapter opens only after Hoang's route has committed to one of those directions.

## How To Add Conditional Choices Inside A Chapter

Define the choice in `CHOICE_DEFINITIONS`, then check it in the label with `choice_is_available()`.

```python
"ask_gently": {
    "label": "Ask gently",
    "type": "conditional",
    "conditions": ["direction_hoang_restraint"],
}
```

```renpy
menu:
    "How should Tam respond?"

    "Ask gently" if choice_is_available("ask_gently"):
        $ add_unique(progress["player_flags"], "tam_choice_gentle")
        "Tam softens her words and lets the moment breathe."
```

Implemented choice types:

- normal conditional
- insight (`flag_player_knows_*` style conditions)
- emotional-direction (`direction_*` style conditions)

## How To Mark A Chapter As A Main Event

Use `type = "core"` and place it on the main route timeline with the right `timeline_position`.

```python
"tam_c03": {
    "type": "core",
    "timeline_position": 30,
}
```

Core chapters should usually end with `complete_chapter()` and jump back to the route map.

## How Endings Work

Endings are defined in `ENDING_RULES`. The current runtime supports:

- `requires_completed`
- `requires_directions_any`
- `emotional_min`
- `emotional_max`
- `route_focus_greater`
- `persistent_endings_all`

That lets you build:

- route-focus endings
- exclusion-sensitive endings
- convergence / true endings that require prior clears across playthroughs

## Authoring Checklist

- Add chapter metadata to `CHAPTERS`
- Put chapter id into `CHAPTER_ORDER`
- Create matching `label`
- End label with `$ complete_chapter("chapter_id")`
- Return to `jump route_map`
- If player-facing route-map strings changed, update `game/tl/vietnamese/route_map.rpy`
- Run Ren'Py lint after edits

## Demo References

- Cross-route unlock: `tam_c02` -> `hoang_h01`
- Mutually exclusive bonus chapters: `hoang_bonus_restraint`, `hoang_bonus_confession`
- Direction-gated core chapter: `tam_c03`
- Ending resolution: `resolve_seed_ending`
- Debug testing: `screen debug_progression()`
