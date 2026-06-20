# Interwoven Route & Chapter Unlock System — Technical Spec

## 1. Purpose

The system manages a non-linear Visual Novel progression model where multiple character routes are unlocked gradually and interwoven with each other.

The player does not complete one full route before moving to the next. Instead, completing specific chapters unlocks chapters from other routes, alternate POV chapters, extra/bonus chapters, and new emotional or relationship directions.

The system must support:

```text
- Multiple character routes
- Chapter unlock conditions
- POV unlock chains
- Route order influence
- Extra/bonus chapter exclusion
- Hidden emotional flags
- Unlockable dialogue choices
- Unlockable relationship directions
- Route map / chapter selection UI
```

This system is designed for Ren’Py but should be implemented in a data-driven way so that chapter logic remains maintainable.

---

## 2. Core Concept

### 2.1 Route

A **route** is a group of chapters associated with a specific character or narrative perspective.

Example route identifiers:

```text
tam
hoang
yuuka
minh
```

Each route contains multiple chapter nodes.

A route may be:

```text
locked
available
partially_unlocked
completed
```

Routes are not necessarily linear. A later chapter from one route may depend on completing chapters from several other routes.

---

### 2.2 Chapter Node

A **chapter node** is the smallest selectable story unit in the route map.

Each chapter should be treated as a data object.

Example:

```python
{
    "id": "tam_c03",
    "route": "tam",
    "type": "core",
    "timeline_position": 30,
    "title": "Chapter Title",
    "status": "locked",
    "prerequisites": ["tam_c02"],
    "optional_conditions": [],
    "unlocks": ["hoang_h01"],
    "excludes": [],
    "flags_set": [],
    "emotional_effects": {},
    "choice_unlocks": []
}
```

The system should not hardcode route progression directly inside story scripts unless necessary. Progression should be handled through chapter metadata and centralized unlock logic.

---

## 3. Chapter Types

The system should support the following chapter types.

### 3.1 Core Chapter

A mandatory or major chapter required for main progression.

```text
type = "core"
```

Core chapters usually advance the main timeline and unlock important route nodes.

---

### 3.2 POV Chapter

A chapter that revisits or complements an event from another perspective.

```text
type = "pov"
```

A POV chapter may unlock new understanding, alternate dialogue options, or new emotional flags.

---

### 3.3 Memory Chapter

A flashback, memory, or context chapter.

```text
type = "memory"
```

Memory chapters usually unlock hidden insight flags, alternate narration, or emotional choices in later chapters.

---

### 3.4 Extra / Bonus Chapter

An optional chapter that may change character direction, emotional tendency, or future unlocks.

```text
type = "extra"
type = "bonus"
```

Extra and bonus chapters may use exclusion rules.

Important:

> Some extra/bonus chapters are mutually exclusive.
> Playing chapter X may hide or disable chapter Y.

This allows the player’s chosen side content to influence emotional development without creating too many full branches.

---

### 3.5 Convergence Chapter

A chapter where multiple route paths reconnect.

```text
type = "convergence"
```

These are useful to keep the overall structure controlled while still allowing route order variation.

---

## 4. Chapter Status Model

Each chapter must have one of the following statuses:

```text
locked
available
completed
hidden
excluded
disabled
```

### 4.1 locked

The chapter exists but prerequisites are not met.

The player cannot select it.

---

### 4.2 available

The chapter is unlocked and selectable.

---

### 4.3 completed

The chapter has been played to completion.

---

### 4.4 hidden

The chapter should not be shown on the route map yet.

This is useful for spoiler protection.

---

### 4.5 excluded

The chapter has been permanently excluded in the current playthrough because the player completed another mutually exclusive chapter.

Example:

```text
Complete bonus_a → bonus_b becomes excluded
```

Excluded chapters should usually be hidden or marked as unavailable depending on UI design.

---

### 4.6 disabled

The chapter is visible but temporarily unavailable.

This can be used when the chapter is known to the player but cannot currently be selected.

---

## 5. Route Unlock Flow

### 5.1 Default Route

The game starts with only one route available.

Example:

```python
initial_available_routes = ["tam"]
```

All other routes are locked or hidden.

---

### 5.2 Progressive Route Unlock

Routes are unlocked by completing specific chapter nodes.

Example:

```python
"tam_c03" unlocks "hoang_h01"
"hoang_h02" unlocks "yuuka_y01"
"yuuka_y02" unlocks "minh_m01"
```

The system should not require strict full-route completion before unlocking another route.

---

### 5.3 Route Interweaving

After several routes are unlocked, the player may choose which available chapter to play next.

The chosen order should influence:

```text
- Available choices
- Emotional flags
- Relationship direction
- Extra/bonus unlocks
- Chapter variations
- Ending eligibility
```

However, route order should not automatically break the master timeline unless explicitly designed.

---

## 6. Master Timeline vs Player Order

The system must distinguish between:

### 6.1 Master Timeline

The internal chronological order of events.

```python
timeline_position = 10
timeline_position = 20
timeline_position = 30
```

This is used for consistency checking, recap generation, and route map sorting.

---

### 6.2 Player Order

The actual order in which the player completes chapters.

Example:

```python
play_order = [
    "tam_c01",
    "tam_c02",
    "hoang_h01",
    "tam_c03",
    "yuuka_y01"
]
```

The player order may affect unlocks and flags.

---

### 6.3 Knowledge Separation

The system should distinguish:

```text
player_knowledge
character_knowledge
```

The player may know something because they played another route, but the current POV character may not know it.

This is important for unlocking “insight choices” without creating illogical character behavior.

Example:

```python
player_flags.add("knows_hidden_context_a")
character_flags["tam"].does_not_include("knows_hidden_context_a")
```

This can unlock a subtle narration variant, but should not force the character to act on knowledge they do not possess.

---

## 7. Unlock Conditions

Each chapter may define conditions.

### 7.1 Required Prerequisites

All required prerequisites must be completed.

```python
"prerequisites": [
    "tam_c03",
    "hoang_h01"
]
```

---

### 7.2 Optional Conditions

Optional conditions may unlock variants or bonus choices.

```python
"optional_conditions": [
    "completed_yuuka_y01",
    "flag_player_knows_context_a"
]
```

---

### 7.3 Route Weight Conditions

The system may track how much attention the player gives to each route.

Example:

```python
route_focus = {
    "tam": 5,
    "hoang": 3,
    "yuuka": 2,
    "minh": 1
}
```

Route focus can influence:

```text
- Bonus chapter availability
- Emotional direction
- Ending eligibility
- Recommended next chapters
```

---

## 8. Extra / Bonus Chapter Exclusion System

### 8.1 Purpose

Extra and bonus chapters allow optional character development.

Some optional chapters should be mutually exclusive to make player choice meaningful.

The player should not be able to see every emotional direction in one playthrough.

---

### 8.2 Exclusion Group

Chapters can belong to an exclusion group.

Only one chapter in the same group can be completed in a single playthrough.

Example:

```python
"exclusion_group": "hoang_emotional_direction_01"
```

Example group:

```python
[
    "hoang_bonus_restraint",
    "hoang_bonus_confession",
    "hoang_bonus_distance"
]
```

If the player completes one, the others become excluded.

---

### 8.3 Hard Exclusion

Hard exclusion permanently disables other chapters in the same group for the current playthrough.

Example:

```python
{
    "id": "hoang_bonus_restraint",
    "type": "bonus",
    "exclusion_group": "hoang_emotional_direction_01",
    "exclusion_mode": "hard"
}
```

When completed:

```text
hoang_bonus_confession → excluded
hoang_bonus_distance → excluded
```

---

### 8.4 Soft Exclusion

Soft exclusion hides competing chapters temporarily, but they may return if later conditions are met.

Example:

```python
"exclusion_mode": "soft"
```

Use soft exclusion when a temporary emotional state blocks another chapter but does not permanently remove it.

---

### 8.5 Exclusion Result

When an extra/bonus chapter is completed, it may:

```text
- Hide competing bonus chapters
- Unlock new choices
- Unlock a new emotional direction
- Modify character route weight
- Set relationship flags
- Alter future dialogue
- Open or close specific ending conditions
```

Example:

```python
{
    "id": "tam_bonus_trust",
    "type": "bonus",
    "exclusion_group": "tam_relationship_direction_01",
    "exclusion_mode": "hard",
    "on_complete": {
        "exclude": ["tam_bonus_doubt"],
        "set_flags": ["tam_direction_trust"],
        "unlock_choices": ["tam_c05_soft_question"],
        "emotional_effects": {
            "tam_trust_hoang": "+",
            "misunderstanding": "-"
        }
    }
}
```

---

## 9. Relationship Direction System

The system should support multiple emotional or romantic directions per character.

These are not necessarily separate romance routes. They are emotional tendencies that influence available choices and chapter variants.

Example directions:

```text
trust
distance
restraint
confrontation
avoidance
reconciliation
attachment
independence
```

A bonus chapter can unlock one or more directions.

Example:

```python
relationship_directions["tam"].add("trust")
relationship_directions["hoang"].add("restraint")
```

Unlocked relationship directions may affect:

```text
- Available dialogue choices
- Future bonus chapters
- Character-specific emotional responses
- Route map recommendations
- Ending eligibility
```

---

## 10. Choice Unlock System

Certain choices should only appear if the player has completed specific chapters or unlocked specific flags.

### 10.1 Basic Choice Condition

Example:

```python
{
    "choice_id": "ask_gently",
    "label": "Ask gently",
    "conditions": [
        "completed_hoang_h01",
        "flag_tam_direction_trust"
    ]
}
```

---

### 10.2 Insight Choice

An insight choice appears when the player has knowledge from another route.

Example:

```python
{
    "choice_id": "notice_subtle_reaction",
    "type": "insight",
    "conditions": [
        "player_knows_yuuka_context"
    ]
}
```

This choice should be written so that it reflects player insight without violating the POV character’s knowledge.

---

### 10.3 Emotional Direction Choice

A choice unlocked by playing a specific extra/bonus chapter.

Example:

```python
{
    "choice_id": "choose_direct_affection",
    "conditions": [
        "direction_tam_trust"
    ]
}
```

---

## 11. Emotional State System

The game should support hidden emotional variables.

These variables should not be displayed as raw numbers.

Example:

```python
emotional_state = {
    "tam_trust_hoang": 0,
    "tam_doubt": 0,
    "hoang_restraint": 0,
    "yuuka_guard": 0,
    "minh_regret": 0,
    "misunderstanding": 0
}
```

UI may display vague indicators only.

Example:

```text
[Trust ↑]
[Distance ↓]
[Misunderstanding ?]
```

Avoid:

```text
Trust +5
Affection -3
```

---

## 12. Unlock Algorithm

The system should evaluate chapter availability after every completed chapter.

### 12.1 Completion Flow

When a chapter ends:

```text
1. Mark current chapter as completed.
2. Add chapter to play_order.
3. Apply emotional effects.
4. Set flags.
5. Apply relationship direction changes.
6. Apply exclusions.
7. Unlock directly listed chapters.
8. Recalculate all conditional unlocks.
9. Update route availability.
10. Refresh route map UI.
```

---

### 12.2 Pseudocode

```python
def complete_chapter(chapter_id):
    chapter = CHAPTERS[chapter_id]

    state.completed.add(chapter_id)
    state.play_order.append(chapter_id)

    apply_emotional_effects(chapter)
    apply_flags(chapter)
    apply_relationship_directions(chapter)
    apply_exclusions(chapter)
    apply_direct_unlocks(chapter)

    recalculate_chapter_availability()
    recalculate_route_availability()
    update_recommended_next()
```

---

### 12.3 Exclusion Logic

```python
def apply_exclusions(chapter):
    group = chapter.get("exclusion_group")

    if not group:
        return

    mode = chapter.get("exclusion_mode", "hard")

    for other_id in EXCLUSION_GROUPS[group]:
        if other_id == chapter.id:
            continue

        if mode == "hard":
            state.excluded.add(other_id)
            state.available.discard(other_id)

        elif mode == "soft":
            state.temporarily_hidden.add(other_id)
            state.available.discard(other_id)
```

---

### 12.4 Availability Logic

```python
def can_unlock(chapter):
    if chapter.id in state.completed:
        return False

    if chapter.id in state.excluded:
        return False

    if not all(req in state.completed for req in chapter.prerequisites):
        return False

    if not evaluate_conditions(chapter.conditions):
        return False

    return True
```

---

## 13. Data Schema

Recommended chapter data structure:

```python
CHAPTERS = {
    "tam_c01": {
        "id": "tam_c01",
        "route": "tam",
        "type": "core",
        "title": "Chapter Title",
        "timeline_position": 10,
        "default_status": "available",

        "prerequisites": [],
        "conditions": [],

        "unlocks": [
            "tam_c02"
        ],

        "exclusion_group": None,
        "exclusion_mode": None,

        "on_complete": {
            "set_flags": [],
            "unlock_choices": [],
            "unlock_directions": [],
            "emotional_effects": {},
            "route_focus_effects": {
                "tam": 1
            }
        }
    }
}
```

---

## 14. Exclusion Group Schema

```python
EXCLUSION_GROUPS = {
    "tam_relationship_direction_01": [
        "tam_bonus_trust",
        "tam_bonus_doubt"
    ],

    "hoang_emotional_direction_01": [
        "hoang_bonus_restraint",
        "hoang_bonus_directness",
        "hoang_bonus_distance"
    ]
}
```

Each chapter in the same exclusion group should define the same `exclusion_group`.

---

## 15. Player State Schema

```python
class PlayerProgress:
    completed = set()
    available = set()
    excluded = set()
    hidden = set()
    temporarily_hidden = set()

    play_order = []

    route_status = {
        "tam": "available",
        "hoang": "locked",
        "yuuka": "locked",
        "minh": "locked"
    }

    route_focus = {
        "tam": 0,
        "hoang": 0,
        "yuuka": 0,
        "minh": 0
    }

    player_flags = set()

    character_flags = {
        "tam": set(),
        "hoang": set(),
        "yuuka": set(),
        "minh": set()
    }

    relationship_directions = {
        "tam": set(),
        "hoang": set(),
        "yuuka": set(),
        "minh": set()
    }

    emotional_state = {
        "trust": 0,
        "distance": 0,
        "guard": 0,
        "misunderstanding": 0
    }

    unlocked_choices = set()
```

In Ren’Py, this can be represented using `default` variables for playthrough state and `persistent` variables only for meta-progression if needed.

---

## 16. Ren’Py Implementation Notes

### 16.1 Use Labels for Chapters

Each chapter should have a Ren’Py label.

```renpy
label tam_c01:
    # chapter content
    call complete_chapter_screen("tam_c01")
    return
```

Or:

```renpy
label tam_c01:
    # chapter content
    $ complete_chapter("tam_c01")
    jump route_map
```

---

### 16.2 Centralize Completion Logic

Do not scatter unlock logic throughout story files.

Recommended:

```text
progression.rpy
routes_data.rpy
chapter_map_screen.rpy
chapter_scripts/
```

Example file structure:

```text
game/
  scripts/
    routes/
      tam.rpy
      hoang.rpy
      yuuka.rpy
      minh.rpy

    systems/
      progression.rpy
      chapter_data.rpy
      route_map.rpy
      emotional_state.rpy
      choice_conditions.rpy
```

---

### 16.3 Use Python Functions

Example:

```renpy
init python:
    def complete_chapter(chapter_id):
        chapter = CHAPTERS[chapter_id]

        progress.completed.add(chapter_id)
        progress.play_order.append(chapter_id)

        apply_on_complete(chapter)
        apply_exclusions(chapter)
        recalculate_unlocks()
```

---

## 17. Route Map UI Requirements

The route map should show available chapter nodes grouped by route.

Minimum requirements:

```text
- Show unlocked routes
- Show available chapters
- Hide spoiler chapters
- Mark completed chapters
- Indicate locked chapters when appropriate
- Hide or visually disable excluded chapters
- Show recommended next chapters
```

---

### 17.1 Chapter Node Display States

```text
Available: glowing node / selectable
Completed: dimmed but readable / replayable
Locked: hidden or dark
Excluded: hidden or crossed out depending on design
New Variant: subtle pulse indicator
Recommended: small marker
```

---

### 17.2 Recommended Next

After each chapter, the system should generate recommended next chapters.

Example logic:

```python
def update_recommended_next():
    recommendations = []

    for chapter_id in progress.available:
        chapter = CHAPTERS[chapter_id]

        score = 0

        if chapter["type"] == "core":
            score += 3

        if chapter["route"] == get_underplayed_route():
            score += 2

        if unlocks_important_context(chapter):
            score += 2

        recommendations.append((chapter_id, score))

    return sorted(recommendations, key=lambda x: x[1], reverse=True)
```

The recommendation system should guide but not force the player.

---

## 18. Ending Eligibility

Ending eligibility should be calculated from:

```text
- Completed chapter groups
- Route focus balance
- Relationship directions
- Emotional state thresholds
- Excluded bonus chapter paths
- Key flags
```

Example:

```python
ENDING_REQUIREMENTS = {
    "true_ending": {
        "required_completed": [
            "tam_c_final",
            "hoang_h_final",
            "yuuka_y_final",
            "minh_m_final"
        ],
        "required_flags": [
            "cross_route_understanding"
        ],
        "route_focus_mode": "balanced"
    },

    "present_route_ending": {
        "required_routes": ["tam", "hoang"],
        "route_focus_priority": ["tam", "hoang"]
    },

    "past_route_ending": {
        "required_routes": ["yuuka", "minh"],
        "route_focus_priority": ["yuuka", "minh"]
    }
}
```

Extra/bonus chapter exclusions may influence ending paths.

Example:

```text
If bonus_trust completed → trust-oriented ending choices unlocked.
If bonus_doubt completed → doubt-oriented ending choices unlocked.
```

---

## 19. Save / Load Requirements

The system must support save/load correctly.

The following must be saved:

```text
- Completed chapters
- Available chapters
- Excluded chapters
- Hidden chapters
- Play order
- Route statuses
- Player flags
- Character flags
- Emotional state
- Relationship directions
- Unlocked choices
- Ending eligibility flags
```

In Ren’Py, normal `default` variables are save-dependent. Use `persistent` only for unlocks that should survive across playthroughs.

Example use of `persistent`:

```python
persistent.gallery_unlocks
persistent.route_clear_history
persistent.true_ending_seen
```

Do not store current playthrough state in `persistent` unless it is intended to carry across new games.

---

## 20. Debug Requirements

For development, provide a debug screen or console commands.

Debug tools should allow:

```text
- Unlock chapter
- Complete chapter
- Reset chapter
- Show current flags
- Show excluded chapters
- Show route focus
- Show emotional state
- Force ending eligibility
- Reset playthrough state
```

Example debug command:

```python
debug_unlock("yuuka_y01")
debug_complete("hoang_h02")
debug_show_progress()
```

---

## 21. Acceptance Criteria

The feature is considered complete when:

```text
1. The game starts with only the default route available.
2. Completing configured chapters unlocks chapters from other routes.
3. The player can choose between multiple available route chapters.
4. Completing one extra/bonus chapter can exclude another chapter in the same exclusion group.
5. Excluded chapters cannot be selected.
6. Bonus chapter completion can unlock new dialogue choices.
7. Bonus chapter completion can unlock new relationship directions.
8. Route order is recorded.
9. Route order can influence available choices or chapter variants.
10. Player knowledge and character knowledge can be tracked separately.
11. Route map UI updates after every completed chapter.
12. Save/load preserves progression correctly.
13. Debug tools allow testing unlock and exclusion logic.
```

---

## 22. Recommended Implementation Priority

### Phase 1 — Core Progression

```text
- Chapter data schema
- Route data schema
- Completed / available / locked states
- Basic unlock logic
- Route map UI
```

### Phase 2 — Interwoven Route Logic

```text
- Cross-route prerequisites
- Player order tracking
- Route focus tracking
- Recommended next chapters
```

### Phase 3 — Extra / Bonus Exclusion

```text
- Exclusion groups
- Hard exclusion
- Soft exclusion
- Bonus-driven choice unlocks
- Bonus-driven relationship directions
```

### Phase 4 — Emotional / Choice System

```text
- Hidden emotional variables
- Conditional choices
- Insight choices
- Relationship direction choices
- Chapter variants
```

### Phase 5 — Ending Logic

```text
- Ending eligibility rules
- Route focus endings
- Exclusion-dependent endings
- True route conditions
```

---

## 23. Design Principle

The system should create the feeling that:

```text
The player is not simply choosing a route.
The player is choosing which emotional truth to discover first.
```

Mechanically, this means:

```text
- Chapters unlock other chapters.
- Some bonus chapters exclude others.
- Route order changes available choices.
- Different chapter paths unlock different emotional directions.
- The main timeline remains controlled.
- The player’s understanding deepens through interwoven POV progression.
```

The system should be flexible enough to support complex narrative structure, but strict enough to prevent route logic from becoming unmaintainable.
