# Progression Implementation Plan

## Purpose

This plan turns `Specs/game_mechanics.md` into an implementation roadmap for the Ren'Py runtime. It is meant to track delivery of the interwoven route system from scaffold to production-ready progression.

## Current Gap

- `game/script.rpy` is still starter-template content.
- `game/screens.rpy` and `game/gui.rpy` provide generic menu and styling infrastructure, not progression logic.
- No current runtime files implement route metadata, chapter availability, exclusion groups, emotional state, or ending logic.

## Recommended Runtime Layout

```text
game/
  scripts/
    routes/
      tam.rpy
      hoang.rpy
      yuuka.rpy
      minh.rpy
  systems/
    chapter_data.rpy
    progression_state.rpy
    progression_logic.rpy
    choice_conditions.rpy
    emotional_state.rpy
    endings.rpy
    debug_tools.rpy
  screens/
    route_map.rpy
    debug_progression.rpy
```

## Phase 1 - Core Progression Foundation

Goal: replace hardcoded starter flow with data-driven chapter progression.

- [ ] Define chapter schema: id, route, type, title, timeline position, prerequisites, unlocks, flags, effects.
- [ ] Define route schema and route status model.
- [ ] Define `default` player progress state.
- [ ] Implement `complete_chapter(chapter_id)` as the single completion entry point.
- [ ] Implement prerequisite-based availability recalculation.
- [ ] Create first route map screen with available, completed, locked, and hidden states.
- [ ] Replace `label start` with entry into the progression flow.
- [ ] Seed one playable default route.

Exit criteria:

- [ ] Game starts with one default route available.
- [ ] Completing a chapter unlocks the next configured chapter.
- [ ] Route map refreshes after completion.

## Phase 2 - Interwoven Route Logic

Goal: support cross-route progression and order-sensitive unlock behavior.

- [ ] Add cross-route prerequisites.
- [ ] Track `play_order`.
- [ ] Track `route_focus`.
- [ ] Recalculate route availability independently from chapter availability.
- [ ] Sort chapters by `timeline_position` while preserving actual play order in state.
- [ ] Add recommended-next logic.
- [ ] Separate `player_flags` from `character_flags`.

Exit criteria:

- [ ] Completing route A can unlock route B chapters.
- [ ] Player order affects recommendations or availability.
- [ ] Insight-style knowledge can exist without forcing POV-character knowledge.

## Phase 3 - Optional Content and Exclusion

Goal: make bonus content meaningful and mutually exclusive.

- [ ] Implement exclusion group schema.
- [ ] Implement hard exclusion.
- [ ] Implement soft exclusion or temporary hiding if needed by content.
- [ ] Support `extra` and `bonus` chapter types in runtime data.
- [ ] Apply exclusions during chapter completion.
- [ ] Represent excluded chapters in the route map.

Exit criteria:

- [ ] Completing one bonus chapter excludes other chapters in its group.
- [ ] Excluded chapters cannot be selected.

## Phase 4 - Emotional State and Conditional Choice System

Goal: make optional content affect later narration and decisions.

- [ ] Implement hidden emotional variables.
- [ ] Implement relationship direction tracking.
- [ ] Implement conditional choice evaluation.
- [ ] Support normal conditional, insight, and emotional-direction choices.
- [ ] Allow chapter completion to set emotional effects and unlock directions.
- [ ] Add subtle UI indicators instead of raw numeric stat display.
- [ ] Add chapter variants gated by flags or directions.

Exit criteria:

- [ ] Bonus chapters can unlock choices and directions.
- [ ] Hidden variables influence later content.
- [ ] Insight choices depend on player knowledge only when appropriate.

## Phase 5 - Ending Logic

Goal: make route order and optional choices affect final outcomes.

- [ ] Define ending eligibility rules.
- [ ] Implement route-focus-based endings.
- [ ] Implement exclusion-sensitive endings.
- [ ] Implement true-route or convergence conditions.
- [ ] Store only meta-progression in `persistent` when intended.

Exit criteria:

- [ ] Ending access depends on playthrough state, not just last chapter seen.
- [ ] True ending conditions are explicit and testable.

## Phase 6 - Debugging and QA Support

Goal: make the progression system practical to author and verify.

- [ ] Add debug commands for unlock, complete, reset, flag dump, route focus, and emotional state.
- [ ] Add a debug progression screen.
- [ ] Add metadata validation for missing chapter ids, bad prerequisites, and exclusion conflicts.
- [ ] Build a small vertical-slice dataset across at least two routes.
- [ ] Test all acceptance criteria from the spec.

Exit criteria:

- [ ] Progression can be tested without replaying manually.
- [ ] Broken metadata is visible early.

## Cross-Cutting Feature Checklist

### Data Model

- [ ] Chapter data schema
- [ ] Route data schema
- [ ] Exclusion group schema
- [ ] Player progress schema
- [ ] Ending rule schema

### Progression Engine

- [ ] Completion flow
- [ ] Direct unlocks
- [ ] Conditional unlock recalculation
- [ ] Route status recalculation
- [ ] Play order tracking
- [ ] Route focus tracking

### Narrative State

- [ ] Player flags
- [ ] Character flags
- [ ] Knowledge separation
- [ ] Emotional state
- [ ] Relationship directions
- [ ] Unlocked choices

### UI and Tooling

- [ ] Route map screen
- [ ] Recommended-next presentation
- [ ] Excluded-state presentation
- [ ] Debug screen
- [ ] Debug commands
- [ ] Save/load verification

## First Vertical Slice

Build this before full content production:

- [ ] 2 routes
- [ ] 3-4 chapters per route
- [ ] 1 cross-route unlock
- [ ] 1 exclusion group with 2 bonus chapters
- [ ] 1 insight choice
- [ ] 1 emotional variable
- [ ] 1 route map screen
- [ ] 1 debug panel

## Source References

- Mechanics source: `Specs/game_mechanics.md`
- Current story entry: `game/script.rpy`
- Current UI surface: `game/screens.rpy`
- Current theme constants: `game/gui.rpy`
- Current runtime metadata: `game/options.rpy`
