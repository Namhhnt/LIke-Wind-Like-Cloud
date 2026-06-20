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

- [x] Define chapter schema: id, route, type, title, timeline position, prerequisites, unlocks, flags, effects.
- [x] Define route schema and route status model.
- [x] Define `default` player progress state.
- [x] Implement `complete_chapter(chapter_id)` as the single completion entry point.
- [x] Implement prerequisite-based availability recalculation.
- [x] Create first route map screen with available, completed, locked, and hidden states.
- [x] Replace `label start` with entry into the progression flow.
- [x] Seed one playable default route.

Exit criteria:

- [x] Game starts with one default route available.
- [x] Completing a chapter unlocks the next configured chapter.
- [x] Route map refreshes after completion.

## Phase 2 - Interwoven Route Logic

Goal: support cross-route progression and order-sensitive unlock behavior.

- [x] Add cross-route prerequisites.
- [x] Track `play_order`.
- [x] Track `route_focus`.
- [x] Recalculate route availability independently from chapter availability.
- [x] Sort chapters by `timeline_position` while preserving actual play order in state.
- [x] Add recommended-next logic.
- [x] Separate `player_flags` from `character_flags`.

Exit criteria:

- [x] Completing route A can unlock route B chapters.
- [x] Player order affects recommendations or availability.
- [x] Insight-style knowledge can exist without forcing POV-character knowledge.

## Phase 3 - Optional Content and Exclusion

Goal: make bonus content meaningful and mutually exclusive.

- [x] Implement exclusion group schema.
- [x] Implement hard exclusion.
- [x] Implement soft exclusion or temporary hiding if needed by content.
- [x] Support `extra` and `bonus` chapter types in runtime data.
- [x] Apply exclusions during chapter completion.
- [x] Represent excluded chapters in the route map.

Exit criteria:

- [x] Completing one bonus chapter excludes other chapters in its group.
- [x] Excluded chapters cannot be selected.

## Phase 4 - Emotional State and Conditional Choice System

Goal: make optional content affect later narration and decisions.

- [x] Implement hidden emotional variables.
- [x] Implement relationship direction tracking.
- [x] Implement conditional choice evaluation.
- [x] Support normal conditional, insight, and emotional-direction choices.
- [x] Allow chapter completion to set emotional effects and unlock directions.
- [x] Add subtle UI indicators instead of raw numeric stat display.
- [x] Add chapter variants gated by flags or directions.

Exit criteria:

- [x] Bonus chapters can unlock choices and directions.
- [x] Hidden variables influence later content.
- [x] Insight choices depend on player knowledge only when appropriate.

## Phase 5 - Ending Logic

Goal: make route order and optional choices affect final outcomes.

- [x] Define ending eligibility rules.
- [x] Implement route-focus-based endings.
- [x] Implement exclusion-sensitive endings.
- [x] Implement true-route or convergence conditions.
- [x] Store only meta-progression in `persistent` when intended.

Exit criteria:

- [x] Ending access depends on playthrough state, not just last chapter seen.
- [x] True ending conditions are explicit and testable.

## Phase 6 - Debugging and QA Support

Goal: make the progression system practical to author and verify.

- [x] Add debug commands for unlock, complete, reset, flag dump, route focus, and emotional state.
- [x] Add a debug progression screen.
- [x] Add metadata validation for missing chapter ids, bad prerequisites, and exclusion conflicts.
- [x] Build a small vertical-slice dataset across at least two routes.
- [x] Test all acceptance criteria from the spec.

Exit criteria:

- [x] Progression can be tested without replaying manually.
- [x] Broken metadata is visible early.

## Cross-Cutting Feature Checklist

### Data Model

- [x] Chapter data schema
- [x] Route data schema
- [x] Exclusion group schema
- [x] Player progress schema
- [x] Ending rule schema

### Progression Engine

- [x] Completion flow
- [x] Direct unlocks
- [x] Conditional unlock recalculation
- [x] Route status recalculation
- [x] Play order tracking
- [x] Route focus tracking

### Narrative State

- [x] Player flags
- [x] Character flags
- [x] Knowledge separation
- [x] Emotional state
- [x] Relationship directions
- [x] Unlocked choices

### UI and Tooling

- [x] Route map screen
- [x] Recommended-next presentation
- [x] Excluded-state presentation
- [x] Debug screen
- [x] Debug commands
- [x] Save/load verification

## First Vertical Slice

Build this before full content production:

- [x] 2 routes
- [x] 3-4 chapters per route
- [x] 1 cross-route unlock
- [x] 1 exclusion group with 2 bonus chapters
- [x] 1 insight choice
- [x] 1 emotional variable
- [x] 1 route map screen
- [x] 1 debug panel

## Source References

- Mechanics source: `Specs/game_mechanics.md`
- Current story entry: `game/script.rpy`
- Current UI surface: `game/screens.rpy`
- Current theme constants: `game/gui.rpy`
- Current runtime metadata: `game/options.rpy`
