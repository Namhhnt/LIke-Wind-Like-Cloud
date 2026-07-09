# Chapter Runtime Systems Guide

## Purpose

This guide explains how authored story chapters should interact with the project's three runtime systems:

- time management and inter-chapter free-time flow
- smartphone content and character-status updates
- character scores, flags, directions, and ending support

It is based on the live implementation in `game/`, not on older design-only specs.

## The short version

For chapter authors, the safest pattern is:

1. Use `story_*` helpers inside scenes to change narrative state.
2. Use phone helpers only when a scene intentionally unlocks or reveals phone content now.
3. End the chapter with `$ story_complete_chapter("chapter_id")`.
4. If that chapter starts an inter-chapter free-time period, immediately call `$ time_start_period_after_chapter("chapter_id")`.
5. `jump route_map` so the player returns to the story hub / interactive map flow.

That is the pattern already used by the current Tâm chapter wrappers.

## Where the systems live

### Narrative state

- `game/story_state.rpy`
- `game/ending_rules.rpy`

### Phone state and logic

- `game/smartphone/phone_state.rpy`
- `game/smartphone/phone_logic.rpy`
- `game/data/phone_contacts.rpy`
- `game/data/phone_threads.rpy`
- `game/data/phone_mail.rpy`
- `game/data/phone_social.rpy`
- `game/screens/phone_screen.rpy`
- `game/screens/phone_subscreens.rpy`

### Time and free-time flow

- `game/time_management_data.rpy`
- `game/time_management_logic.rpy`
- `game/map_logic_with_interactions.rpy`
- `game/map_location_interactions.rpy`
- `game/map_hub_with_interactions.rpy`
- `game/route_map.rpy`

## Runtime flow between chapters

The important control flow is:

1. A chapter label runs its scene labels.
2. The wrapper calls `$ story_complete_chapter(...)`.
3. `story_complete_chapter()` delegates to `complete_chapter()` in `game/progression_logic.rpy` when available.
4. `complete_chapter()` updates progression, unlocks, exclusions, route status, recommendations, map unlocks, and also calls `phone_refresh_all()`.
5. If the finished chapter should open a free-time period, the wrapper must separately call `$ time_start_period_after_chapter(...)`.
6. `jump route_map` returns to `label route_map` in `game/route_map.rpy`.
7. `route_map` resolves the current map context and calls `story_hub`, which leads into `label interactive_map` in `game/map_hub_with_interactions.rpy`.

The key implementation detail is that chapter completion and time-period start are separate. Completing a chapter does **not** automatically start the next free-time period.

## Existing wrapper pattern

Current examples:

- `game/story/tam/tam_c01_interview_day/_chapter.rpy`
- `game/story/tam/tam_c02_company_party/_chapter.rpy`
- `game/story/tam/tam_c03_thienan_family/_chapter.rpy`

Pattern:

```renpy
label tam_c02_company_party:
    call tam_c02_company_party_s00_onboarding
    call tam_c02_company_party_s01_company_rumors_about_quan
    ...

    $ story_complete_chapter("tam_c02_company_party")
    $ time_start_period_after_chapter("tam_c02_company_party")

    jump route_map
```

Use this as the default wrapper shape for chapters that transition into free time.

## 1) Character scores, flags, directions, and ending support

### Primary API for scene authors

Use these helpers from `game/story_state.rpy`:

- `story_add(key, amount=1)`
- `story_sub(key, amount=1)`
- `story_set(key, value)`
- `story_flag(flag)`
- `story_unflag(flag)`
- `story_has_flag(flag)`
- `story_add_direction(character, direction)`
- `story_has_direction(character, direction)`
- `story_add_ending_support(ending_id)`
- `story_has_ending_support(ending_id)`
- `story_set_minyuu_relation(relation)`
- `story_complete_chapter(chapter_id)`

### Why these helpers matter

`story_add()` and `story_set()` clamp defined score keys to the 0-100 range and call `story_notify_state_change()`. That notification is important because `career_handle_story_state_change()` in `game/smartphone/phone_logic.rpy` can react to story-score changes and update character career status or promotions.

So for score changes, use the helper instead of mutating `story_state[...]` directly.

### What is already common in authored scenes

The score helpers are already in normal use across story files. For example, several Yuuka chapter scenes use patterns like:

```renpy
$ story_add("tam_respect_yuuka", 1)
$ story_add("career_tam", 1)
$ story_flag("noticed_minyuu_pause")
```

That is the correct scene-level pattern.

### Special relation helpers

`story_set_minyuu_relation(...)` is not just a simple setter. It also applies romance locks and direction flags depending on the chosen relation:

- `old_close_friends`
- `ex_lovers_long_separated`
- `still_lovers`

If a chapter is deciding the Minh/Yuuka relationship branch, use this helper instead of assigning `story_state["minh_yuuka_relation"]` directly.

### Ending support

Late-game nudges should use `story_add_ending_support(ending_id)` rather than manually appending to `story_state["ending_support"]`.

### Do not do this

Avoid direct mutation like:

```renpy
$ story_state["career_tam"] += 1
$ story_state["tam_hoang_interest"] = 999
$ story_flags.append("some_flag")
```

Those bypass clamping, notifications, and helper-level consistency.

## 2) Smartphone system

### What the phone system actually is

The phone runtime is structurally complete and data-driven.

State lives in `phone_state` and `character_status` in `game/smartphone/phone_state.rpy`.
Main logic lives in `game/smartphone/phone_logic.rpy`.
The UI entry point is `screen phone_home(...)` in `game/screens/phone_screen.rpy`.

On show, the phone screen runs:

- `phone_ensure_state()`
- `phone_refresh_all()`

So the UI is designed to reveal whatever content is now eligible based on current flags, completion state, directions, and scores.

### Unlock-condition model

Phone content is mostly unlocked by declarative `unlock_conditions` in the data files. The condition evaluator supports these forms in `phone_eval_condition(...)`:

- `completed:chapter_id`
- `flag:flag_name`
- `not_flag:flag_name`
- `contact:contact_id`
- `thread_read:thread_id`
- `mail_read:mail_id`
- `post_read:post_id`
- `direction:character_id:direction_id`
- `score_gte:score_key:value`
- `score_lte:score_key:value`

Examples from live data:

- `game/data/phone_threads.rpy` uses `unlock_conditions: ["completed:tam_c01_interview_day"]`
- `game/data/phone_mail.rpy` uses `unlock_conditions: ["flag:tam_interview_invitation_received"]`

This means many phone events should be authored as narrative flags or chapter completions first, then allowed to unlock through `phone_refresh_all()`.

### Phone helpers chapter authors should use

Use these when a scene deliberately creates or reveals phone content now:

- `phone_unlock_contact(contact_id)`
- `phone_unlock_thread(thread_id, mark_unread=True)`
- `phone_unlock_mail(mail_id, mark_unread=True)`
- `phone_unlock_post(post_id)`
- `phone_refresh_all()`
- `phone_update_character_status(character_id, **kwargs)`
- `char_add_item(character_id, item_id)`
- `char_add_known_info(character_id, note)`

### Existing chapter-level phone pattern

`game/story/tam/tam_c01_interview_day/_chapter.rpy` is the clearest live example:

```renpy
$ story_flag("tam_interview_invitation_received")
$ phone_unlock_mail("company_interview_invitation")
$ phone_refresh_all()
...
$ story_complete_chapter("tam_c01_interview_day")
$ story_flag("tam_c01_onboarding_mail_sent")
$ phone_unlock_mail("company_onboarding_process")
$ phone_refresh_all()
```

This is the right pattern when the phone artifact is part of the scene beat and should appear immediately.

### Read effects and reply effects

Phone entries can apply consequences when the player reads or replies:

- thread `effects_on_read` run in `phone_mark_thread_read()`
- mail `effects_on_read` run in `phone_mark_mail_read()`
- post `effects_on_read` run in `phone_mark_post_read()`
- reply effects run in `phone_send_reply()`

`phone_apply_effects(...)` can apply:

- `flags`
- `story_add`
- `directions`
- `character_status`
- `inventory_add`
- `known_info_add`
- `chapter_unlocks`

So if a phone interaction itself should change story state, prefer data-driven `effects_on_read` or reply `effects` rather than hard-coding the same consequences in the story scene.

### Character status and career data

`phone_update_character_status(...)` is the public way to patch phone-facing character info such as:

- `job_title`
- `job_level`
- `salary`
- `income_monthly`
- `inventory`
- `known_info`
- `public_stats`

Live example: `game/story/tam/tam_c02_company_party/s01b_first_salary_and_shopping.rpy` updates Tâm's money/status through `phone_update_character_status(...)` and also keeps activity-state money in sync.

### Important phone gotcha

`story_complete_chapter()` already causes `complete_chapter()` to call `phone_refresh_all()`. That means post-completion phone content gated only on `completed:chapter_id` will usually unlock automatically.

You still need an explicit `phone_refresh_all()` when:

- you unlock phone content before chapter completion
- you set a `flag:`-based unlock and want it visible immediately in the same chapter flow
- you directly call `phone_unlock_mail/thread/post/contact` and want UI/state to reflect newly eligible related content

## 3) Time management and free-time flow

### Where state lives

Free-time state is stored in `progress["activity_state"]`, created by `ensure_activity_state()` in `game/map_location_interactions.rpy` and extended by `time_management_extend_activity_state()` in `game/time_management_logic.rpy`.

This state includes both day/cycle data and player stats like:

- `time_units` / `time_points`
- `current_day`, `weekday_index`, `day_of_month`, `calendar_month`
- `current_period_id`, `next_event_chapter_id`, `period_days_remaining`
- `money`, `energy`, `stress`, `mood`, `health`
- `inventory`
- attendance / salary / bills fields

### Starting a free-time period

The chapter-facing helper is:

- `time_start_period_after_chapter(chapter_id)`

It looks up `PERIOD_BY_COMPLETED_CHAPTER` / `INTER_CHAPTER_PERIODS` and, when present, starts the configured period:

- aligns the calendar to the chapter
- sets `current_period_id`
- resets day state
- sets `period_days_total` / `period_days_remaining`
- stores the forced `next_event_chapter_id`
- sets employment expectations for the period

Current configured examples live in `game/time_management_data.rpy`, including:

- `after_tam_c01`
- `after_tam_c02`
- `after_tam_c03`

If a chapter has no configured period, `time_start_period_after_chapter(...)` safely returns `False`.

### Returning to the map

After the wrapper jumps to `route_map`, the flow becomes:

- `route_map` -> `resolve_story_map_context()`
- `story_hub(context_id=...)`
- `interactive_map(...)`

Inside `interactive_map`, the runtime:

- ensures activity state
- sets up day expectations
- lets the player choose map actions, phone, or time skip
- can force the next event chapter when the current period expires

### Activity helpers

For map/free-time actions, the low-level helpers are:

- `activity_get(key, default=None)`
- `activity_set(key, value)`
- `activity_add(key, delta)`
- `activity_inventory_get(item_id)`
- `activity_inventory_add(item_id, delta)`
- `activity_add_flag(flag_id)`
- `activity_apply_story_effects(story_effects)`
- `activity_apply_effects(effects)`
- `activity_apply_inventory_effects(effects)`
- `activity_start_free_time_session(time_units=5, reset_part_time_counter=True)`

Map actions in `MAP_LOCATION_ACTIONS` can apply:

- `effects` to activity-state values
- `inventory_effects`
- `story_effects`

So time/free-time content is designed to be mostly data-driven at the map-action layer.

### Chapter author guidance for time state

Inside normal story scenes, do not directly rewrite lots of `activity_state` unless the scene is explicitly about time-management setup or payoff.

Good uses:

- toggling employment status during onboarding
- syncing monthly salary after a career/status change
- awarding or spending money tied to a scene outcome
- unlocking map locations after a story beat

Live example: `game/story/tam/tam_c02_company_party/s00_onboarding.rpy` sets `player_is_employed = True` and syncs salary into activity state.

### Map-location integration

Use these when a chapter unlocks physical exploration:

- `unlock_map_location(location_id)`
- `unlock_map_locations(location_ids)`

Live example: `tam_c01_interview_day` unlocks `tam_apartment`, `huyen_apartment`, and `company` after the opening setup.

### Context-routing helper

`queue_story_map_context(context_id=None, chapter_id=None, scene_id=None)` exists in `game/map_logic_with_interactions.rpy` if you need to explicitly route the next return to a particular map context. The normal path usually does not need this because `resolve_story_map_context()` can derive context from the last completed chapter.

## Recommended authoring patterns

### Pattern A: normal score-only scene

```renpy
label some_scene:
    menu:
        "Support her directly":
            $ story_add("thienan_self_assertion", 2)
            $ story_add("tam_self_clarity", 1)
        "Stay quiet":
            $ story_add("family_pressure_thienan", 1)
            $ story_add("doom_score", 1)
    return
```

### Pattern B: scene that sends immediate phone content

```renpy
label some_scene:
    $ story_flag("tam_sent_followup_message")
    $ phone_unlock_thread("tam_hoang_followup_01")
    $ phone_refresh_all()
    return
```

### Pattern C: chapter wrapper that opens free time

```renpy
label chapter_id:
    call chapter_scene_01
    call chapter_scene_02

    $ story_complete_chapter("chapter_id")
    $ time_start_period_after_chapter("chapter_id")
    jump route_map
```

### Pattern D: chapter wrapper with immediate post-chapter mail

```renpy
label chapter_id:
    call chapter_scene_01

    $ story_complete_chapter("chapter_id")
    $ story_flag("chapter_id_mail_sent")
    $ phone_unlock_mail("chapter_followup_mail")
    $ phone_refresh_all()
    $ time_start_period_after_chapter("chapter_id")
    jump route_map
```

## What not to do

### Avoid direct mutation when a helper exists

Avoid direct writes to:

- `story_state`
- `story_flags`
- `phone_state`
- `character_status`
- `progress["activity_state"]`

unless you are doing something that has no helper and you understand the side effects being skipped.

### Do not assume chapter completion starts free time

It does not. You must call `time_start_period_after_chapter(...)` yourself.

### Do not duplicate phone consequences in both story code and phone data

If a thread/mail/post already defines `effects_on_read` or reply `effects`, let the phone system apply those consequences.

### Do not bypass score notifications for career-linked values

Career progression hooks depend on `story_notify_state_change()` via the `story_*` helpers.

### Do not assume the phone system is widely used in authored content yet

The system is ready, but current narrative integration is still relatively light. Existing Tâm chapters provide the clearest canonical pattern.

## Practical checklist for a new chapter

1. Write scene logic with `story_add`, `story_flag`, and other `story_*` helpers.
2. If the chapter should unlock mail/thread/post/contact immediately, call the matching `phone_unlock_*` helper and `phone_refresh_all()`.
3. If the chapter changes career/public info, use `phone_update_character_status(...)`.
4. If the chapter unlocks exploration, call `unlock_map_location(...)` or `unlock_map_locations(...)`.
5. End the wrapper with `story_complete_chapter(...)`.
6. If the chapter opens free time, call `time_start_period_after_chapter(...)`.
7. Return with `jump route_map`.

## Current reality of system adoption

As of the current codebase:

- score/flag helpers are actively used in many story scene files
- wrapper-level chapter completion is standard
- explicit free-time startup is currently present in the Tâm chapter wrappers that lead into the map system
- phone integration exists and works, but only a smaller set of story files currently uses it directly

That means new chapter work should treat the score/helper pattern as mature and the phone/time chapter pattern as established but still expanding.
