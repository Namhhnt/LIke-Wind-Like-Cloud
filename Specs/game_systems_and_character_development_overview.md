# Game Systems and Character Development Overview

This document is a developer-facing map of the major gameplay systems, character-development systems, and extension points in **Like Wind, Like Cloud**.

Use it as the starting point for continuing or expanding the game.

---

## 1. High-level runtime flow

Primary entry flow:

1. `game/script.rpy` → `label start`
2. `initialize_progression()` builds or normalizes runtime progression state
3. The game enters story content, then returns to navigation
4. Navigation currently routes through:
   - `label route_map` in `game/route_map.rpy`
   - `label story_hub` / `label interactive_map` in `game/map_hub_with_interactions.rpy`
5. Supporting systems refresh on load in `label after_load`:
   - progression validation
   - phone state
   - character career/status state
   - phone content refresh

In practice, the project is built around a **data-driven progression core** with several attached subsystems:

- route/chapter progression
- character score and flag development
- ending resolution
- interactive map + free-time/time systems
- smartphone simulation
- library and side-story systems
- minigame runtime and replay systems

---

## 2. Core architecture at a glance

### Main runtime files

| Area | Main files |
|---|---|
| Bootstrap | `game/script.rpy` |
| Progression data | `game/progression_data.rpy` |
| Progression logic | `game/progression_logic.rpy` |
| Story state / scores | `game/story_state.rpy` |
| Ending rules | `game/ending_rules.rpy` |
| Ending dispatch | `game/story/endings/ending_resolver.rpy` |
| Route/timeline entry | `game/route_map.rpy` |
| Interactive map | `game/map_data.rpy`, `game/map_logic_with_interactions.rpy`, `game/map_hub_with_interactions.rpy`, `game/map_location_interactions.rpy`, `game/map_screen_with_interactions.rpy` |
| Time management | `game/time_management_data.rpy`, `game/time_management_logic.rpy`, `game/time_skip_screen.rpy`, `game/daily_hud_screen.rpy` |
| Smartphone | `game/smartphone/phone_state.rpy`, `game/smartphone/phone_logic.rpy`, `game/data/phone_*.rpy`, `game/screens/phone_*.rpy` |
| Library | `game/data/library_data.rpy`, `game/screens/library_*.rpy` |
| Story library reader | `game/story_library.rpy`, `game/story_parser.rpy`, `game/story_player.rpy`, `game/stories/**` |
| Character status/careers | `game/data/character_status_data.rpy` |
| Music room | `game/data/library_music_data.rpy` |
| Minigames | `game/minigames/**`, `game/minigames/minigame_runtime.rpy`, `game/data/library_minigame_data.rpy` |
| Debugging | `game/debug_progression.rpy` |

---

## 3. Character development systems

Character development is not handled in one place. It is spread across several connected systems.

### 3.1 Story score system

**Main file:** `game/story_state.rpy`

**Meaning**

This is the hidden emotional-development layer of the game. Scores represent how a character is changing over time, not just whether a scene happened.

This is the core hidden character-development layer. It stores numeric and relationship state used by route logic, endings, and side systems.

Key structures:

- `default story_state = { ... }`
- `default story_flags = []`
- `default story_completed_chapters = []`

Important score families:

- **Tâm:** `tam_hoang_interest`, `tam_minh_drawn`, `tam_self_clarity`, `tam_insecurity`, `tam_observation`, `career_tam`
- **Hoàng:** `hoang_tam_trust`, `hoang_huyen_interest`, `hoang_insecurity`, `hoang_self_acceptance`, `career_hoang`
- **Huyền:** `huyen_quan_trust`, `huyen_quan_interest`, `huyen_hoang_interest`, `career_huyen`
- **Thiên An:** `thienan_quang_trust`, `thienan_minh_residue`, `family_pressure_thienan`, `thienan_self_assertion`, `career_thienan`
- **Minh/Yuuka shared arc:** `minh_yuuka_trust`, `minh_yuuka_intimacy`, `minh_yuuka_unresolved`, `old_friend_score`, `ex_lover_score`, `still_lover_score`, `romantic_score`, `boundary_score`, `career_minh`, `career_yuuka`
- **Global pressure:** `doom_score`

Also stored here:

- `minh_yuuka_relation`
- `minh_romance_lock`
- `yuuka_romance_lock`
- `ending_support`

**How it is implemented**

- The file defines the source-of-truth state shape and score ranges.
- Story-facing helpers include `story_add()`, `story_flag()`, `story_add_direction()`, and `story_add_ending_support()`.
- Helper functions normalize/clamp and expose score access.
- Story scenes mutate this state as chapters and choices play out.
- Ending logic and phone/career systems read from it later.

**How to extend**

When adding a new character arc or pressure meter:

1. Add the new score or state field to `story_state`
2. Add helper support if needed in `story_state.rpy`
3. Update ending rules or progression checks that should read it
4. Apply changes from story scenes or side systems through existing helpers

**When to use**

- gradual emotional change
- trust, attraction, insecurity, clarity, pressure, ambition
- any arc that should rise or fall over multiple scenes

**When not to use**

- one-time facts
- simple yes/no unlock conditions
- public-facing profile information that players should directly read

### 3.2 Story flags system

**Main files:** `game/story_state.rpy`, `game/progression_logic.rpy`, story scenes under `game/story/**`

**Meaning**

Flags are binary narrative facts. They record that something happened, became known, or was committed to.

`story_flags` is the loose, event-based layer used for narrative state that does not fit a numeric score.

Examples:

- chapter-sensitive reveals
- one-time outcomes
- direction commitments
- phone unlock triggers
- mail/social/thread read state consequences

Relationship directions also use flag-like state through helpers and `direction_<character>_<direction>` patterns.

**How to extend**

- Use flags for binary narrative state, not for long-running emotional intensity
- Prefer a score for gradients and a flag for irreversible or categorical outcomes

**When to use**

- revelations
- read states
- route commitments
- one-time events
- irreversible narrative state

**When not to use**

- relationship intensity
- emotional progression over time
- anything that should be rebalanced numerically later

### 3.3 Character flag and relationship-direction system

**Main files:** `game/progression_data.rpy`, `game/progression_logic.rpy`

**Meaning**

This is the trajectory layer. Scores tell you how strong a feeling is; directions tell you where an arc is leaning.

Each chapter can push route-specific state into progression.

Per-chapter metadata includes:

- `character_flags_set`
- `relationship_directions_set`
- `choice_unlocks`
- `emotional_effects`

Runtime storage inside `progress` includes:

- `character_flags`
- `relationship_directions`
- `emotional_state`
- `unlocked_choices`

This means chapter completion can do more than unlock another chapter: it can also shift relationship posture, expose future choices, and alter cross-route narrative direction.

**When to use**

- route lean
- romance vs independence
- reconciliation vs distance
- unlocking future choice sets based on narrative direction

**When not to use**

- raw progression unlocks only
- public codex/profile text
- broad emotional tracking better represented as scores

### 3.4 Character status and career progression

**Main files:**

- `game/smartphone/phone_state.rpy`
- `game/smartphone/phone_logic.rpy`
- `game/data/character_status_data.rpy`

**Meaning**

This is the public-facing life-development layer. It translates hidden story change into visible status, work growth, possessions, and known facts.

This is the most explicit public-facing character development layer.

Runtime structures:

- `default character_status = { ... }`
- per-character fields like:
  - `job_title`
  - `job_level`
  - `salary`
  - `income_monthly`
  - `inventory`
  - `known_info`
  - `public_stats`

Static configuration:

- `CHARACTER_STATUS_BASE`
- `STORY_ITEMS`
- `CHARACTER_CAREER_TRACKS`

Career tracks are data-driven. Each uses `career_level(...)` entries with:

- level number
- title
- salary
- required flags
- required minimum scores
- required maximum scores
- required completed chapters

`phone_logic.rpy` contains the runtime layer:

- `career_get_track()`
- `career_requirements_met()`
- `career_get_pending_level()`
- `career_apply_promotion()`
- `career_refresh_all_statuses()`
- `career_check_all_promotions()`

**How it works**

- Character public status is shown through the phone UI
- Story state and progression can unlock new public information
- Career score changes can produce promotions and salary changes
- Mail/social/inventory effects can also update known info and items

**How to extend**

To add a new public character-development branch:

1. Add or update the character in `CHARACTER_STATUS_BASE`
2. Add a new career track or levels in `CHARACTER_CAREER_TRACKS`
3. Connect required scores/flags/chapters
4. Trigger status, item, or known-info changes from story, phone, or map actions

**When to use**

- job title changes
- promotions and salary progression
- public notes about a character
- visible inventory and known facts

**When not to use**

- hidden emotional state
- ending-only logic
- route-availability gating by itself

---

## 4. Main game mechanism systems

### 4.1 Route and chapter progression system

**Main files:** `game/progression_data.rpy`, `game/progression_logic.rpy`

**Meaning**

This is the structural skeleton of the game. It answers what content is available now because of everything the player has already done.

This is the central game mechanism.

#### Data model

`progression_data.rpy` defines:

- `DEFAULT_ROUTE_ID`
- `ROUTE_ORDER`
- `RELATIONSHIP_TRACK_ORDER`
- `ROUTES`
- `CHAPTER_ORDER`
- `CHAPTERS`

Each chapter in `CHAPTERS` is a metadata object with fields such as:

- `id`
- `title`
- `route`
- `type`
- `prerequisites`
- `optional_conditions`
- `unlocks`
- `excludes`
- `flags_set`
- `character_flags_set`
- `relationship_directions_set`
- `emotional_effects`
- `choice_unlocks`

#### Runtime state

`make_progress_state()` creates the live progression object with:

- `completed`
- `available`
- `excluded`
- `hidden`
- `temporarily_hidden`
- `unlocked_map_locations`
- `play_order`
- `recommended_next`
- `route_status`
- `route_focus`
- `player_flags`
- `character_flags`
- `relationship_directions`
- `emotional_state`
- `unlocked_choices`
- `ending_eligibility`
- validation fields

#### Important progression functions

In `progression_logic.rpy`:

- `initialize_progression()`
- `prerequisites_met()`
- `recalculate_chapter_availability()`
- `recalculate_route_status()`
- `update_recommended_next()`
- `complete_chapter()`
- `apply_direct_unlocks()`
- `apply_flags()`
- `apply_relationship_directions()`
- `apply_choice_unlocks()`
- `apply_emotional_effects()`
- `apply_exclusions()`

**How it works**

- Chapters are authored as data, not hardcoded progression branches
- `complete_chapter()` is the main integration point for unlock propagation, flags, relationship directions, exclusions, recommendations, map unlocks, phone refresh, and ending recalculation
- Completing a chapter mutates progression state and may affect scores, flags, choices, route focus, and endings
- Availability is recalculated centrally instead of inside every scene

**How to extend**

To add a new chapter or route segment:

1. Add chapter metadata in `CHAPTERS`
2. Place the chapter in `CHAPTER_ORDER`
3. Add or update route entry in `ROUTES` if needed
4. Create the actual label(s) under `game/story/**`
5. Ensure the chapter ends by calling the proper completion helper
6. Update translation mirrors if source strings change

**When to use**

- chapter unlock chains
- cross-route prerequisites
- exclusions and hidden states
- recommendation flow and route availability

**When not to use**

- emotional meaning of a relationship
- public character presentation
- optional side-content currency logic

### 4.2 Route map / timeline system

**Main files:**

- `game/route_map.rpy`
- `game/screens/timeline/timeline_map_data.rpy`
- `game/screens/timeline/timeline_map_screen.rpy`
- `game/screens/timeline/timeline_map_styles.rpy`

**Meaning**

This is the chapter-selection view of progression. It presents the interwoven route structure as a navigable story map.

This is the chapter-node navigation system.

`route_map.rpy` provides:

- `label route_map`
- `label route_map_timeline`

The timeline screen returns tuples that drive actions like:

- play chapter
- preview chapter
- bookmark chapter
- change route

Supporting progression functions include:

- `timeline_route_has_selectable_node()`
- `timeline_get_first_available_route_id()`
- `timeline_resolve_route_selection()`

**Purpose**

- expose interwoven route structure to the player
- show chapter status safely
- provide bookmarks and previews
- coexist with the interactive map

**When to use**

- chapter-node browsing
- route overview
- status previews and bookmarks

**When not to use**

- place-based free-time interaction
- daily-life simulation
- phone-driven subtext delivery

### 4.3 Ending eligibility and ending resolver system

**Main files:** `game/ending_rules.rpy`, `game/story/endings/ending_resolver.rpy`

**Meaning**

This is the interpretation layer. It converts all accumulated hidden state into the ending that is narratively true for the playthrough.

This system transforms hidden character development and route state into final outcomes.

`ending_rules.rpy` defines:

- numeric thresholds
- helper evaluators
- route-pair and single-ending condition logic
- doom/canon gates

Examples of important helper logic:

- `minyuu_shared_arc_ok()`
- `thienan_family_pressure_overrides_self()`
- `hoang_growth_ok()`
- score threshold helpers via `score()`

`ending_resolver.rpy` then jumps to the selected ending label through `label ending_resolver`.

**Implementation pattern**

- chapters seed ending support through `story_state["ending_support"]`
- ending rules combine that with score thresholds and locks
- resolver selects one ending label from the full set of endings

**How to extend**

To add or refine an ending:

1. Add or adjust thresholds and helper conditions in `ending_rules.rpy`
2. Seed support from relevant scenes if needed
3. Add or update the ending label in `game/story/endings/**`
4. Ensure `ending_resolver.rpy` can dispatch to it

**When to use**

- final route outcome selection
- threshold-based ending logic
- combining scores, flags, locks, and support seeds

**When not to use**

- mid-story chapter availability
- public character status
- routine side-effect handling

### 4.4 Interactive map system

**Main files:**

- `game/map_data.rpy`
- `game/map_logic_with_interactions.rpy`
- `game/map_hub_with_interactions.rpy`
- `game/map_screen_with_interactions.rpy`
- `game/map_location_interactions.rpy`

**Meaning**

This is the lived-space layer of the game. It makes the world feel inhabitable by tying actions and narrative opportunities to places.

This is the location-based navigation and free-action layer.

Core data:

- `FIXED_MAP_LOCATIONS`
- `TEMPORARY_MAP_LOCATIONS`
- `MAP_CONTEXTS`
- `MAP_CONTEXT_BY_SCENE`
- `MAP_LOCATION_ACTIONS`

Core logic in `map_logic_with_interactions.rpy`:

- condition parsing: `completed:`, `flag:`, `direction:` and related negations
- location unlock evaluation
- story hub entry resolution
- map target label resolution

Core action/state logic in `map_location_interactions.rpy`:

- `ensure_activity_state()`
- `activity_get()` / `activity_set()` / `activity_add()`
- `activity_inventory_add()`
- `activity_apply_story_effects()`
- `location_action_is_visible()`
- `location_action_resolve_state()`
- scene label resolution helpers

Activity state includes gameplay stats such as:

- money
- energy
- stress
- mood
- health
- confidence
- style
- knowledge
- work skill
- cooking skill
- life skill
- work focus
- inventory
- flags

**How it works**

- chapters and flags unlock map locations
- locations expose actions
- actions consume time/resources and can change story state or inventory
- map flow can branch into story labels, phone, or time-skip flow

**How to extend**

To add a new map-driven interaction:

1. Add a location or reuse an existing one in `map_data.rpy`
2. Add actions in `MAP_LOCATION_ACTIONS`
3. Define conditions, costs, and effects
4. Add scene labels if the action dispatches to authored narrative
5. If the action should influence story, use story-effect hooks instead of duplicating logic

**When to use**

- place-based interactions
- free-time activities
- routine world navigation
- environmental pacing between story beats

**When not to use**

- chapter graph logic
- optional story-library unlock flow
- ending resolution

### 4.5 Time management and inter-chapter period system

**Main files:** `game/time_management_data.rpy`, `game/time_management_logic.rpy`

**Meaning**

This is the everyday-life bridge between major chapters. It gives weight to passing time, deadlines, work cycles, and missed opportunities.

This extends the interactive map into a daily-loop system.

Key data:

- `WEEKDAY_NAMES`
- `CHAPTER_TIME_METADATA`
- `INTER_CHAPTER_PERIODS`
- `PERIOD_BY_COMPLETED_CHAPTER`

Key runtime fields added onto activity state:

- `current_day`
- `calendar_month`
- `day_of_month`
- `weekday_index`
- `time_points`
- `daily_time_points`
- `period_day`
- `period_days_total`
- `period_days_remaining`
- `monthly_salary`
- `pending_bills`
- `salary_history`
- `missed_important_interactions`
- `time_skip_plan`

Important functions:

- `time_start_period_after_chapter()`
- `time_reset_day()`
- `time_end_day()`
- `time_should_force_next_event()`
- `time_resolve_next_event_label()`
- `time_prepare_monthly_bills()`
- `time_pay_pending_bills()`
- `time_process_payroll_if_due()`
- `time_skip_*` helpers

**How it works**

- chapters can begin an inter-chapter period
- a period defines the next forced story event, its duration, and warning timings
- daily actions spend time points
- employment/payroll/bills integrate with activity and career state
- time skip automates routine days while preserving system effects

**Current status note**

This system is implemented and wired into the map flow, but still looks like an expanding foundation rather than a fully content-complete simulation layer.

**When to use**

- inter-chapter downtime
- deadlines and warning windows
- salary/bill cycles
- routine action pacing

**When not to use**

- core chapter unlock metadata
- hidden relationship meaning by itself
- library bonus-content gating

### 4.6 Smartphone simulation system

**Main files:**

- `game/smartphone/phone_state.rpy`
- `game/smartphone/phone_logic.rpy`
- `game/data/phone_contacts.rpy`
- `game/data/phone_threads.rpy`
- `game/data/phone_mail.rpy`
- `game/data/phone_social.rpy`
- `game/screens/phone_screen.rpy`
- `game/screens/phone_subscreens.rpy`

**Meaning**

This is the subtext delivery system. It reveals what characters say privately, publicly, or indirectly outside major scenes.

This system acts as a story-facing communication and public-status layer.

#### Runtime phone state

`phone_state` stores:

- unlocked contacts
- unlocked threads
- read/unread thread state
- read messages
- sent replies
- unlocked/read mail
- unlocked/read posts
- liked posts
- notification log

#### Data-driven content types

- `PHONE_CONTACTS`
- `PHONE_THREADS`
- `PHONE_MAILS`
- `PHONE_SOCIAL_POSTS`

Entries use condition- and effect-based configuration such as:

- `unlock_conditions`
- `effects_on_read`
- `effects_on_like`
- reply effects
- known-info updates
- inventory rewards
- chapter unlocks

Important runtime functions:

- `phone_refresh_contacts()`
- `phone_refresh_threads()`
- `phone_refresh_mails()`
- `phone_refresh_posts()`
- `phone_refresh_all()`
- `phone_unlock_*()` helpers
- `phone_mark_*_read()` helpers
- `phone_send_reply()`
- `phone_apply_effects()`

**How it works**

- story progression or flags unlock phone content
- reading content can set flags, unlock chapters, add items, or reveal character info
- the phone also surfaces the character status/career layer

**How to extend**

To add new phone content:

1. Add the data entry in the proper `game/data/phone_*.rpy` file
2. Set `unlock_conditions`
3. Define side effects carefully
4. If it should expose public character development, use `known_info_add`, inventory effects, or status updates rather than raw score dumps

**When to use**

- follow-up emotional beats
- unread or delayed communication
- public/private contrast
- official notices, logistics, and small optional revelations

**When not to use**

- main route progression as the only gate
- deep hidden-state storage
- large branching story structure by itself

### 4.7 Library system

**Main files:** `game/data/library_data.rpy`, `game/screens/library_screen.rpy`, `game/screens/library_subscreens.rpy`

**Meaning**

This is the archive and enrichment shell. It holds optional or revisitable content outside the main story loop.

The library is the bonus-content shell.

Categories are defined in `LIBRARY_CATEGORIES`:

- Character Profiles
- Original Stories
- CG Gallery
- Music Room
- Minigames
- Extras

`library_get_progress_text()` dynamically reports progress by category.

This is the main player-facing hub for non-core-story content.

**When to use**

- codex/profile content
- optional stories
- music and minigame replay
- bonus/extras presentation

**When not to use**

- mandatory chapter progression
- day-loop simulation
- ending rule evaluation

### 4.8 Character profiles system

**Main files:** `game/data/library_data.rpy`, `game/screens/library_subscreens.rpy`, `game/smartphone/phone_logic.rpy`

**Meaning**

This is the codex-style character reference layer. It presents curated character knowledge rather than raw simulation state.

Character profiles are a separate player-facing representation of character development.

They complement, rather than replace:

- hidden story scores
- phone public status
- route progression

The library profile system is best for:

- static or semi-static character information
- unlockable profile sections
- codex-style narrative reference

**When to use**

- profile cards
- stable background/reference info
- unlockable bios and sections

**When not to use**

- dynamic emotional math
- route completion logic
- phone-style conversational subtext

### 4.9 Original stories / side-story reader system

**Main files:**

- `game/story_library.rpy`
- `game/story_parser.rpy`
- `game/story_player.rpy`
- `game/stories/**`
- `game/stories/manifest.json`

**Meaning**

This is the optional prose-content pipeline. It expands the world without needing full route-map chapter complexity.

This is a separate content pipeline for prose-style optional story content.

Key persistent state:

- `persistent.investment_points`
- `persistent.spent_investment_points`
- `persistent.unlocked_library_content`
- `persistent.read_library_content`
- `persistent.claimed_rewards`
- `persistent.unlocked_library_characters`
- `persistent.unlocked_character_sections`

Important functions in `story_library.rpy`:

- manifest and file loading
- library item normalization/registration
- prerequisite evaluation
- investment-point checking and spending
- unlock and read tracking
- chapter reward handling

`story_parser.rpy` parses Markdown/text-like content into events.

Supported story-reader event types include things like:

- `scene`
- `show`
- `hide`
- `music`
- `sfx`
- `pause`
- dialogue/text content

`story_player.rpy` renders the parsed pages in a dedicated reader screen.

**How it works**

- optional stories are loaded from local files and manifest metadata
- story progression can grant investment points
- points unlock side content without gating core story

**How to extend**

To add a side story:

1. Add the Markdown/text file under `game/stories/`
2. Register it through manifest metadata or compatible auto-loading shape
3. Define prerequisites and cost
4. Confirm reader parsing works with your formatting

**When to use**

- side memories
- after-stories
- bonus prose scenes
- worldbuilding that does not need full chapter-graph logic

**When not to use**

- core mandatory route chapters
- phone conversation content
- map activity definitions

### 4.10 Investment points system

**Main files:** `game/story_library.rpy`

**Meaning**

This is optional-content currency. It rewards engagement without blocking the main story.

This system is the currency layer for optional content.

Key functions:

- `award_investment_points()`
- `award_investment_points_for_story_chapter()`
- `has_investment_points()`
- `spend_investment_points()`
- `unlock_library_content()`

Use this for:

- optional side stories
- bonus or expanded narrative content

Do not use this to block core route progression.

**When to use**

- unlocking optional stories and bonus content
- pacing side-content consumption

**When not to use**

- core chapter access
- emotional or relationship modeling
- public status progression

### 4.11 Music room system

**Main file:** `game/data/library_music_data.rpy`

**Meaning**

This is the soundtrack memory archive. It ties music unlocks to narrative milestones.

This system scans `game/audio/music` and builds library entries using filename-to-chapter mappings.

Important parts:

- `MUSIC_CHAPTER_BY_FILENAME`
- music slug/title helpers
- folder scan helpers
- unlock-by-chapter ordering

This keeps the music room data-driven and tied to story progress.

**When to use**

- chapter-based soundtrack unlocks
- replayable audio archive content

**When not to use**

- main story gating
- side-effect-heavy narrative systems

### 4.12 Minigame framework and replay system

**Main files:**

- `game/minigames/minigame_runtime.rpy`
- `game/minigames/problem_diagnosis/**`
- `game/minigames/speech_order/**`
- `game/data/library_minigame_data.rpy`

**Meaning**

This is the performance-and-competence layer. It lets character pressure, skill, or judgment become gameplay instead of pure dialogue.

#### Runtime framework

`minigame_runtime.rpy` provides the generic registry/result system:

- `minigame_register()`
- `minigame_get_config()`
- `minigame_get_variant()`
- `minigame_build_result()`
- `minigame_store_result()`
- effect-application protection

#### Implemented minigame families

- **Speech ordering**: used for Tâm interview/speech-style logic and replay variants
- **Problem diagnosis**: screen-based puzzle with multi-phase evaluation

#### Library replay layer

`game/data/library_minigame_data.rpy` registers replayable minigame variants and exposes them through the Library → Minigames category.

**How to extend**

To add a new minigame variant:

1. Register it in the minigame runtime config
2. Define outcomes/effects
3. Add a replay/library entry if it should be replayable
4. Connect narrative consequences through scores, flags, rewards, or route state

**When to use**

- competence-based moments
- high-pressure interactive scenes
- replayable challenge content

**When not to use**

- passive lore delivery
- route unlock metadata alone
- systems that do not benefit from interaction

### 4.13 Debug and validation systems

**Main files:** `game/debug_progression.rpy`, `game/progression_logic.rpy`

The project includes explicit validation and debugging support.

Important helpers:

- `validate_progression_metadata()`
- `run_acceptance_checks()`
- `refresh_validation_state()`
- `debug_unlock()`
- `debug_complete()`
- `debug_reset_progress()`
- spoiler reveal toggles

Use these when expanding routes, unlock chains, and map integration.

---

## 5. How the systems connect

The key relationships are:

### Story scenes → progression

Scenes complete chapters and mutate score/flag state.

### Progression → map / timeline / endings / phone

Completed chapters and flags unlock:

- new chapters
- new routes
- map locations
- phone content
- music
- side content prerequisites
- ending eligibility

### Story scores → endings / careers / public character status

Hidden emotional development controls:

- romance outcomes
- single/career outcomes
- career promotions
- public notes/status updates

### Map actions / time system → story state and inventory

Free-time and daily actions can alter:

- money
- energy/stress/mood/health
- work/life skills
- story scores
- inventory
- availability of future interactions

### Phone system → public-facing narrative texture

The phone does not replace progression, but enriches it with:

- messages
- mail
- social posts
- reply choices
- public character info

### Library system → optional retention and expansion surface

The library holds optional content loops that can be expanded without breaking core route progression.

---

## 6. Developer decision guide

If you want X, use Y:

| If you want to... | Use this system |
|---|---|
| Track gradual emotional change | story scores in `game/story_state.rpy` |
| Record that a narrative fact happened | `story_flags` |
| Show an arc is leaning toward a specific outcome | relationship directions in progression |
| Unlock or block future chapters | progression metadata in `game/progression_data.rpy` |
| Decide which ending is valid | ending rules + ending support |
| Show visible life growth | character status + career tracks |
| Deliver quiet follow-up characterization | phone threads/mail/social |
| Let players spend time in places | interactive map + location actions |
| Simulate daily routines and deadlines | time management + inter-chapter periods |
| Skip repetitive routine while keeping effects | time skip |
| Add optional codex/bonus content | library system |
| Add optional prose side stories | story library reader |
| Reward optional engagement without gating core story | investment points |
| Tie music unlocks to progress | music room |
| Turn pressure/competence into gameplay | minigame framework |

Quick rule set:

- **Feeling over time** → score
- **Fact that happened** → flag
- **Narrative lean** → direction
- **What unlocks next** → progression
- **What ending this all means** → ending rules
- **What the player can publicly see** → status / career / phone
- **What the player can do between story beats** → map / time systems
- **What deepens the world optionally** → library / side stories / investment points

---

## 7. Best places to extend the game next

### For more main story content

- add new scene files under `game/story/<route>/<chapter>/`
- add chapter metadata in `game/progression_data.rpy`
- connect endings/score effects as needed

### For stronger character development

- add or rebalance story scores in `game/story_state.rpy`
- add public status changes in `phone_logic.rpy` and `character_status_data.rpy`
- add phone threads/social/mail to externalize subtext

### For more systemic gameplay

- expand `MAP_LOCATION_ACTIONS`
- add more inter-chapter periods in `time_management_data.rpy`
- expand bills, work expectations, or event urgency logic

### For optional content growth

- add side stories under `game/stories/`
- add library extras, CG entries, and music unlock mappings
- add minigame variants with replay support

### For ending depth

- refine threshold logic in `ending_rules.rpy`
- seed more ending support from late-route scenes
- write the currently stubbed ending narratives

---

## 8. Safe development rules for this project

- Do not edit generated/runtime files like `game/cache/`, `game/saves/`, `.rpyc`, `.rpymc`, `log.txt`, or `traceback.txt`
- Keep translations mirrored under `game/tl/**` when source strings change
- Treat `game/progression_data.rpy` + `game/progression_logic.rpy` as the source of truth for route/chapter mechanics
- Treat `game/story_state.rpy` as the source of truth for hidden character-development state
- Prefer data-driven additions over hardcoding inside screens
- Prefer using existing effect hooks instead of inventing one-off logic inside scenes when possible

---

## 9. Recommended onboarding order for new developers

Read in this order:

1. `game/script.rpy`
2. `game/progression_data.rpy`
3. `game/progression_logic.rpy`
4. `game/story_state.rpy`
5. `game/ending_rules.rpy`
6. `game/route_map.rpy`
7. `game/map_data.rpy` + `game/map_logic_with_interactions.rpy` + `game/map_location_interactions.rpy`
8. `game/time_management_data.rpy` + `game/time_management_logic.rpy`
9. `game/smartphone/phone_state.rpy` + `game/smartphone/phone_logic.rpy`
10. `game/story_library.rpy` + `game/story_parser.rpy` + `game/story_player.rpy`
11. `game/data/character_status_data.rpy`
12. `game/minigames/minigame_runtime.rpy`

Then review:

- `Specs/game_mechanics.md`
- `Specs/character_scores_and_flags_reference.md`
- `Specs/interactive_map_updated_20260706.md`
- `Specs/phone-simulator.md`
- `Specs/stories_reader.md`

---

## 10. Current high-value expansion opportunities

The biggest continuation opportunities appear to be:

1. finish authored content for scaffolded routes/chapters
2. replace ending stubs with full narrative endings
3. integrate the smartphone system into more in-story moments
4. deepen interactive map and time-management content loops
5. expand library optional content, especially stories/CG/extras
6. tighten translation sync for routes beyond the currently clean-synced sections

If you are continuing the game from scratch, start by deciding which of these six fronts you are extending, then work from the source-of-truth system listed above.
