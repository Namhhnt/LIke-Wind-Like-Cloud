# Chapter Progression and State Flow

This document explains what happens between chapters in the live Ren'Py project, which mechanisms fire automatically when a chapter ends, and which character scores or state fields are only changed by authored scene code.

Primary sources:
- `game/script.rpy`
- `game/route_map.rpy`
- `game/progression_data.rpy`
- `game/progression_logic.rpy`
- `game/story_state.rpy`
- `game/ending_rules.rpy`
- chapter wrappers under `game/story/**/_chapter.rpy`
- scene files under `game/story/**`

---

## 1. High-level runtime loop

The chapter-to-chapter runtime is split into two layers:

1. **Scene-authored state changes** happen while the player is inside a chapter's scene files.
2. **Engine-authored progression updates** happen after the chapter wrapper calls `story_complete_chapter(...)`.

In practice, the loop looks like this:

1. `label start` in `game/script.rpy` calls `initialize_progression()`.
2. The game jumps into story content, beginning with `prologue_rain_dream`.
3. A chapter wrapper in `game/story/**/_chapter.rpy` calls its scene labels in order.
4. Those scene labels may modify `story_state`, `story_flags`, relationship directions, or ending support.
5. The wrapper calls `story_complete_chapter('chapter_id')`.
6. `story_complete_chapter(...)` delegates to `complete_chapter(...)` in `game/progression_logic.rpy`.
7. `complete_chapter(...)` records progression completion and recalculates availability, route status, ending eligibility, validation state, and recommendations.
8. The wrapper then usually jumps back to `route_map`, though a few chapters chain somewhere else.

The important consequence is this:

> Completing a chapter automatically advances progression metadata, but it does **not** automatically change romance or character scores unless the wrapper or one of its scenes explicitly calls a story-state helper.

---

## 2. What chapter wrappers actually do

The wrapper files under `game/story/**/_chapter.rpy` are transition shells.

Typical responsibilities:
- call each scene label for that chapter
- call `story_complete_chapter('chapter_id')`
- optionally call extra subsystem hooks such as `time_start_period_after_chapter(...)`
- jump to the next destination (`route_map`, a direct next chapter, or `ending_resolver`)

Examples:

- `game/story/prologue/prologue_rain_dream/_chapter.rpy`
  - completes `prologue_rain_dream`
  - jumps directly to `tam_c01_interview_day` if available
  - otherwise falls back to `route_map`

- `game/story/tam/tam_c03_thienan_family/_chapter.rpy`
  - completes `tam_c03_thienan_family`
  - calls `time_start_period_after_chapter('tam_c03_thienan_family')`
  - returns to `route_map`

- `game/story/final/final_c24_last_choices/_chapter.rpy`
  - completes `final_c24_last_choices`
  - hands off to `ending_resolver`

Current wrapper inventory findings:
- all current chapter wrappers call `story_complete_chapter(...)`
- only `tam_c01_interview_day`, `tam_c02_company_party`, and `tam_c03_thienan_family` currently start an inter-chapter time period in the wrapper
- almost every wrapper exits to `route_map`
- special exits:
  - `prologue_rain_dream` can jump directly to `tam_c01_interview_day`
  - `final_c24_last_choices` jumps to `ending_resolver`

---

## 3. What fires automatically when a chapter completes

`story_complete_chapter(...)` in `game/story_state.rpy` is an adapter. If `complete_chapter(...)` exists, it delegates into the real progression engine.

The automatic post-chapter flow in `game/progression_logic.rpy` is:

1. normalize/init progression state
2. reject unknown or already-completed chapter IDs
3. append the chapter to `progress["completed"]`
4. remove it from `progress["available"]`
5. append it to `progress["play_order"]`
6. add it to `persistent.unlocked_chapters`
7. award story-library investment points through `award_investment_points_for_story_chapter(...)`
8. increment route focus for the chapter's route
9. apply chapter metadata through:
   - `apply_flags(...)`
   - `apply_emotional_effects(...)`
   - `apply_relationship_directions(...)`
   - `apply_choice_unlocks(...)`
   - `apply_exclusions(...)`
   - `apply_direct_unlocks(...)`
10. refresh unlocked map locations
11. recalculate chapter availability
12. recalculate route status
13. recalculate ending eligibility
14. refresh validation state
15. update recommended next chapters
16. refresh phone state

This means chapter completion **does** always affect progression structure, but mostly through progression data and chapter metadata, not through direct relationship-score mutation.

### Automatic metadata effects from chapter data

The `apply_*` functions change `progress`, not `story_state` numeric scores:

- `apply_flags(...)`
  - writes to `progress["player_flags"]`
  - writes to `progress["character_flags"]`

- `apply_relationship_directions(...)`
  - writes to `progress["relationship_directions"]`

- `apply_choice_unlocks(...)`
  - writes to `progress["unlocked_choices"]`

- `apply_emotional_effects(...)`
  - writes to `progress["emotional_state"]`
  - this is progression-layer emotional metadata, separate from `story_state` numeric romance and character scores

- `apply_exclusions(...)`
  - writes to `progress["completed_exclusion_groups"]`
  - writes to `progress["excluded"]`

- `apply_direct_unlocks(...)`
  - may push new chapter IDs into `progress["available"]`

---

## 4. What changes inside scenes instead of automatically

Most character development happens in scene files under `game/story/**`, using helpers from `game/story_state.rpy`.

Core scene-side helpers:
- `story_add(key, amount)`
- `story_sub(key, amount)`
- `story_set(key, value)`
- `story_flag(flag)`
- `story_add_direction(character, direction)`
- `story_add_ending_support(ending_id)`
- `story_set_minyuu_relation(relation)`

### Numeric character scores

The main numeric relationship / emotion / career values live in `story_state` in `game/story_state.rpy`, including:

- `doom_score`
- Tâm scores such as `tam_hoang_interest`, `tam_minh_drawn`, `tam_self_clarity`, `tam_insecurity`, `tam_observation`, `career_tam`
- Hoàng scores such as `hoang_tam_trust`, `hoang_huyen_interest`, `hoang_insecurity`, `hoang_self_acceptance`, `career_hoang`
- Huyền scores such as `huyen_quan_trust`, `huyen_quan_interest`, `huyen_hoang_interest`, `career_huyen`
- Thiên An scores such as `thienan_quang_trust`, `thienan_minh_residue`, `family_pressure_thienan`, `thienan_self_assertion`, `career_thienan`
- Minh / Yuuka shared scores such as `minh_yuuka_trust`, `minh_yuuka_intimacy`, `minh_yuuka_unresolved`, `old_friend_score`, `ex_lover_score`, `still_lover_score`, `romantic_score`, `boundary_score`, `career_minh`, `career_yuuka`

These values are generally changed by explicit scene code, not by chapter completion itself.

### Example scene mutations

- `game/story/tam/tam_c02_company_party/s04_first_branch.rpy`
  - can change `tam_hoang_interest`, `hoang_tam_trust`, `tam_self_clarity`
  - also sets directions and flags

- `game/story/flashback_minyuu/fb_minyuu_03_door_left_open/s02_help_choice.rpy`
  - changes branch-building scores like `old_friend_score`, `boundary_score`, `romantic_score`, `ex_lover_score`, `still_lover_score`

- `game/story/thienan/thienan_c21a_minh_possible/s03_thienan_choice.rpy`
  - changes `thienan_minh_residue`, `thienan_quang_trust`, `family_pressure_thienan`, or `thienan_self_assertion`
  - also seeds multiple possible endings

- `game/story/final/final_c24_last_choices/s01_tam_final_choice.rpy`
  - nudges late-game values like `hoang_tam_trust`, `tam_minh_drawn`, `tam_self_clarity`, and `doom_score`

---

## 5. Special mechanism: Minh/Yuuka relation locking

The flashback Minh/Yuuka arc has a deeper mechanism than ordinary score changes.

`story_set_minyuu_relation(...)` in `game/story_state.rpy`:
- sets `story_state["minh_yuuka_relation"]`
- may lock or unlock romance possibilities through:
  - `lock_minh_romance_except_yuuka()`
  - `unlock_minh_romance_after_yuuka()`
  - `lock_yuuka_romance_except_minh()`
  - `unlock_yuuka_romance_after_minh()`
- adds relationship direction flags for Minh and Yuuka

This means those flashback chapters do not just add score points; they can reconfigure later route and ending eligibility.

Representative files:
- `game/story/flashback_minyuu/fb_minyuu_04a_old_friends/s03_finalize_old_friends.rpy`
- `game/story/flashback_minyuu/fb_minyuu_05b_separation/s04_finalize_ex_lovers.rpy`
- `game/story/flashback_minyuu/fb_minyuu_04c_no_breakup/s04_finalize_still_lovers.rpy`

---

## 6. What does **not** happen automatically

These are easy mistakes to make when reading the chapter tree:

- Completing a chapter does **not** automatically raise or lower romance scores.
- Returning to `route_map` does **not** itself mutate character state.
- Recalculation of chapter availability and ending eligibility does **not** imply new points were awarded; it often only reevaluates already-stored flags, directions, relation state, and scores.
- Many late-game or scaffold chapters add **ending support** or **directions** without changing many numeric values.
- Some chapters are structurally important even when they have little score movement, because they decide relation state, locks, route direction, or ending nudges.

---

## 7. Chapter wrapper exit behavior

| Chapter | Exit behavior |
|---|---|
| `prologue_rain_dream` | Complete chapter, then try to jump directly to `tam_c01_interview_day`; otherwise fall back to `route_map`. |
| `final_c24_last_choices` | Complete chapter, then jump to `ending_resolver`. |
| All other current chapter wrappers | Complete chapter, then jump to `route_map`. |

Additional wrapper-time subsystem hook:

| Chapter | Extra wrapper hook |
|---|---|
| `tam_c01_interview_day` | `time_start_period_after_chapter('tam_c01_interview_day')` |
| `tam_c02_company_party` | `time_start_period_after_chapter('tam_c02_company_party')` |
| `tam_c03_thienan_family` | `time_start_period_after_chapter('tam_c03_thienan_family')` |

---

## 8. Chapter-by-chapter mutation inventory

The table below summarizes what each current chapter's scene files call.

Column meanings:
- **Scenes**: number of non-wrapper `.rpy` files in the chapter directory
- **Time period**: whether the wrapper calls `time_start_period_after_chapter(...)`
- **`story_add`**: number of `story_add(...)` calls across the chapter's scene files
- **`story_set`**: number of `story_set(...)` calls across the chapter's scene files
- **`story_flag`**: number of `story_flag(...)` calls across the chapter's scene files
- **Directions**: number of `story_add_direction(...)` calls across the chapter's scene files
- **Ending support**: number of `story_add_ending_support(...)` calls across the chapter's scene files
- **Relation set**: number of `story_set_minyuu_relation(...)` calls across the chapter's scene files

These counts indicate **authored mutation activity**, not unique score keys.

### Prologue and early Tâm chapters

| Chapter | Scenes | Time period | `story_add` | `story_set` | `story_flag` | Directions | Ending support | Relation set | Notes |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| `prologue_rain_dream` | 3 | No | 10 | 0 | 6 | 0 | 0 | 0 | Early authored state setup; wrapper chains directly into `tam_c01_interview_day`. |
| `tam_c01_interview_day` | 4 | Yes | 20 | 0 | 12 | 0 | 0 | 0 | Score- and flag-heavy authored chapter; also starts inter-chapter time state. |
| `tam_c02_company_party` | 7 | Yes | 53 | 0 | 36 | 11 | 0 | 0 | One of the densest early authored chapters for score, flag, and direction mutation. |
| `tam_c03_thienan_family` | 8 | Yes | 62 | 0 | 45 | 0 | 0 | 0 | Another dense authored chapter; strong direct score mutation without ending-support seeding. |
| `tam_c05_sunday_date` | 4 | No | 13 | 0 | 0 | 3 | 1 | 0 | Mid-route Tâm/Hoàng/Minh steering with some ending nudges. |
| `tam_c06_minh_returns` | 4 | No | 14 | 0 | 1 | 0 | 0 | 0 | Mostly direct score shifts with little routing metadata. |
| `tam_c07_minh_at_company` | 4 | No | 16 | 0 | 0 | 3 | 0 | 0 | Direct score mutation plus relationship-direction shaping. |
| `tam_c20a_tam_minh_possible` | 4 | No | 10 | 0 | 0 | 4 | 6 | 0 | Late-game commitment chapter; mixes direct scores with ending support. |
| `tam_c20b_admiration_vs_love` | 3 | No | 10 | 0 | 0 | 0 | 3 | 0 | Smaller chapter; more resolution-oriented than exploratory. |

### Hoàng / Huyền / group-work chapters

| Chapter | Scenes | Time period | `story_add` | `story_set` | `story_flag` | Directions | Ending support | Relation set | Notes |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| `hoang_h01_brother_house` | 4 | No | 14 | 0 | 0 | 5 | 0 | 0 | Strong direction-setting chapter with direct score movement. |
| `hoang_h05_shadow_of_minh` | 4 | No | 16 | 0 | 0 | 2 | 3 | 0 | Mixes direct score changes with late-game ending support. |
| `huyen_c22_quan_or_hoang` | 4 | No | 15 | 0 | 0 | 1 | 5 | 0 | Primarily a chooser chapter: still changes scores, but also heavily seeds endings. |
| `group_c11_social_dinner` | 4 | No | 14 | 0 | 0 | 0 | 0 | 0 | Direct score-state chapter with no ending-support or relation finalization. |
| `work_c10_project_festival_overlap` | 4 | No | 14 | 0 | 0 | 0 | 0 | 0 | Work/group progression chapter with direct score changes only. |
| `work_c16_project_crisis` | 4 | No | 18 | 0 | 0 | 0 | 0 | 0 | Still score-active, but without relation locks or ending-support logic. |

### Yuuka route and career/long-distance interludes

| Chapter | Scenes | Time period | `story_add` | `story_set` | `story_flag` | Directions | Ending support | Relation set | Notes |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| `yuuka_c08_festival_arrival` | 4 | No | 13 | 0 | 2 | 0 | 0 | 0 | Direct score and a small amount of flag setup. |
| `yuuka_c09_yuukas_work` | 4 | No | 15 | 0 | 0 | 0 | 0 | 0 | Direct score movement without ending-support seeding. |
| `yuuka_c18a_career_interlude` | 3 | No | 2 | 0 | 0 | 0 | 9 | 0 | Low direct score movement; mostly an ending-support chapter. |
| `yuuka_c18b_habit_of_you` | 4 | No | 7 | 0 | 0 | 0 | 9 | 0 | More ending nudges than raw score mutation. |
| `yuuka_c18c_long_distance_interlude` | 3 | No | 1 | 0 | 0 | 0 | 10 | 0 | Almost entirely ending-support seeding. |

### Minh/Yuuka flashback arc and post-flashback branches

| Chapter | Scenes | Time period | `story_add` | `story_set` | `story_flag` | Directions | Ending support | Relation set | Notes |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| `fb_minyuu_01_first_frame` | 3 | No | 16 | 0 | 0 | 0 | 0 | 0 | Flashback opening with direct shared-state buildup. |
| `fb_minyuu_02_working_rhythm` | 4 | No | 20 | 0 | 0 | 0 | 0 | 0 | Shared-score development chapter. |
| `fb_minyuu_03_door_left_open` | 4 | No | 12 | 0 | 0 | 4 | 0 | 0 | Branch-seeding chapter; direction markers matter later. |
| `fb_minyuu_04a_old_friends` | 3 | No | 7 | 0 | 1 | 0 | 2 | 1 | Finalizes `old_close_friends`; unlock/lock consequences matter more than raw score totals. |
| `fb_minyuu_04b_living_together` | 4 | No | 19 | 0 | 0 | 1 | 0 | 0 | Score-heavy flashback chapter before final relation lock-in. |
| `fb_minyuu_04c_no_breakup` | 4 | No | 7 | 0 | 0 | 0 | 8 | 1 | Finalizes `still_lovers`; heavily seeds lover-path endings. |
| `fb_minyuu_05b_separation` | 4 | No | 15 | 0 | 3 | 0 | 3 | 1 | Finalizes `ex_lovers_long_separated`; relationship lock logic becomes important. |
| `c19a_city_after_festival_old_friends` | 3 | No | 4 | 0 | 0 | 0 | 8 | 0 | Post-flashback chapter; mostly ending-support routing. |
| `c19b_city_after_festival_ex_lovers` | 3 | No | 9 | 0 | 0 | 0 | 6 | 0 | Mixed score/ending-support follow-up. |
| `c19c_city_after_festival_still_lovers` | 3 | No | 0 | 0 | 0 | 0 | 10 | 0 | Pure ending-support chapter in current implementation. |
| `minyuu_c23a_old_friends_resolution` | 3 | No | 2 | 0 | 0 | 0 | 11 | 0 | Resolution chapter with minimal score changes and strong ending nudges. |
| `minyuu_c23b_ex_lovers_resolution` | 3 | No | 6 | 0 | 0 | 0 | 8 | 0 | Mixed resolution chapter. |
| `minyuu_c23c_still_lovers_resolution` | 3 | No | 0 | 0 | 0 | 0 | 12 | 0 | Pure ending-support resolution chapter in current implementation. |

### Thiên An and final route chapters

| Chapter | Scenes | Time period | `story_add` | `story_set` | `story_flag` | Directions | Ending support | Relation set | Notes |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| `thienan_c21a_minh_possible` | 4 | No | 10 | 0 | 0 | 2 | 8 | 0 | Major chooser chapter balancing direct score changes with ending seeds. |
| `thienan_c21b_choose_own_path` | 3 | No | 9 | 0 | 0 | 0 | 3 | 0 | Smaller follow-up chapter with explicit route steering. |
| `final_c24_last_choices` | 5 | No | 16 | 0 | 1 | 2 | 31 | 0 | Final aggregation chapter; heavy ending-support seeding, light direct nudges, exits to `ending_resolver`. |

---

## 9. Practical reading guide

When analyzing a future chapter, read it in this order:

1. the chapter wrapper under `game/story/**/_chapter.rpy`
   - tells you when the chapter is considered complete
   - shows whether time-management or another subsystem is triggered
   - shows where control goes next

2. the scene files inside that chapter folder
   - these usually contain the real score, flag, direction, and ending-support changes

3. `game/progression_logic.rpy`
   - explains the automatic progression recalculation chain that fires after completion

4. `game/story_state.rpy` and `game/ending_rules.rpy`
   - explain how those stored values are later interpreted for locks, route eligibility, and ending resolution

---

## 10. Bottom line

The live project uses a hybrid chapter system:

- **story scenes** handle emotional truth, relationship movement, branch seeding, and ending nudges
- **chapter completion** handles structural progression updates and availability recalculation

So when asking "what happens between chapters?", the real answer is:

1. scenes mutate state while the chapter is being played
2. the wrapper marks the chapter complete
3. the progression engine recomputes what the player is now allowed or encouraged to do next

That distinction is the key to understanding why some chapters feel emotionally heavy but barely affect unlock structure, while other chapters make only small numeric changes yet have huge downstream consequences through relation locks, ending support, or route-direction metadata.
