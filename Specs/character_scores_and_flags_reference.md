# Character Scores and Flags Reference

This document summarizes the current story-state fields used by the live Ren'Py source as of 2026-07-02.

Primary sources:
- `game/story_state.rpy`
- `game/ending_rules.rpy`
- `game/story/final/final_c24_last_choices/*.rpy`
- story scene files under `game/story/**`

## How the state is stored

- `story_state`: main dictionary for numeric scores, relation state, romance locks, and ending nudges.
- `story_flags`: free-form list of string flags set by scenes through `story_flag(...)`.
- `story_completed_chapters`: chapter completion fallback list.
- Relationship direction flags are also stored inside `story_flags` via the helper format `direction_<character>_<direction>`.

## Structured state fields

### Relation and lock fields

| Field | Type | Meaning |
|---|---|---|
| `minh_yuuka_relation` | string | Current canonized Minh/Yuuka relationship state. Current values used in source: `old_close_friends`, `ex_lovers_long_separated`, `still_lovers`. |
| `minh_romance_lock` | bool | When `True`, Minh is locked away from non-Yuuka romance outcomes. Used directly by Tâm-Minh and Thiên An-Minh ending checks. |
| `yuuka_romance_lock` | bool | When `True`, Yuuka is locked away from non-Minh romance outcomes. |
| `ending_support` | list[string] | Collected ending nudges such as `e02_tam_hoang` or `e10_minyuu_reunion`. Ending resolution checks this list alongside scores. |

### Helper-derived relation meanings

| Relation value | Meaning |
|---|---|
| `old_close_friends` | Minh and Yuuka are close former friends, with both romance locks cleared. |
| `ex_lovers_long_separated` | Minh and Yuuka are former lovers separated for a long time; Minh is romance-locked except toward Yuuka. |
| `still_lovers` | Minh and Yuuka are still romantically committed; both sides are romance-locked toward each other. |

## Numeric scores in `story_state`

### Global

| Score | Meaning |
|---|---|
| `doom_score` | Global tragedy / avoidance / unresolved-pressure meter. Low values help the canon true ending; high values push toward doom resolution. |

### Tâm

| Score | Meaning |
|---|---|
| `tam_hoang_interest` | Tâm's attraction or openness toward Hoàng. |
| `tam_minh_drawn` | Tâm's pull toward Minh, especially romantic or emotionally fated interest. |
| `tam_self_clarity` | Tâm's ability to understand and choose her own feelings clearly. |
| `tam_respect_yuuka` | Tâm's respect for Yuuka's competence, boundaries, or judgment. |
| `tam_insecurity` | Tâm's self-doubt or emotional instability. |
| `tam_observation` | Tâm's attentiveness to subtle social or emotional details. |
| `career_tam` | Tâm's work/career momentum and professional focus. |

### Hoàng

| Score | Meaning |
|---|---|
| `hoang_tam_trust` | Mutual trust / emotional confidence between Hoàng and Tâm. |
| `hoang_huyen_interest` | Hoàng's romantic or emotional interest in Huyền. |
| `hoang_insecurity` | Hoàng's emotional uncertainty; lower values are better for Hoàng/Tâm resolution. |
| `hoang_self_acceptance` | Hoàng's personal growth and comfort with himself. |
| `hoang_professional_credit` | Hoàng's competence / recognition in work-related threads. |

### Huyền

| Score | Meaning |
|---|---|
| `huyen_quan_trust` | Trust and compatibility between Huyền and Quân. |
| `huyen_hoang_interest` | Huyền's interest in Hoàng. |
| `career_huyen` | Huyền's work/career growth and independent trajectory. |

### Thiên An

| Score | Meaning |
|---|---|
| `thienan_quang_trust` | Trust and relationship strength between Thiên An and Quang. |
| `thienan_minh_residue` | Remaining emotional attachment or unresolved feeling toward Minh. |
| `family_pressure_thienan` | Pressure on Thiên An from family and arranged expectations. |
| `thienan_self_assertion` | Thiên An's ability to assert her own wants and choices. |

### Minh / Yuuka shared arc

| Score | Meaning |
|---|---|
| `minh_yuuka_trust` | Trust and emotional reliability between Minh and Yuuka. |
| `minh_yuuka_intimacy` | Emotional or relational closeness between Minh and Yuuka. |
| `minh_yuuka_unresolved` | Lingering unresolved pain, confusion, or unfinished tension in the Minh/Yuuka arc. |
| `old_friend_score` | Weight toward the old-friends branch in the flashback arc. |
| `ex_lover_score` | Weight toward the ex-lovers branch in the flashback arc. |
| `still_lover_score` | Weight toward the still-lovers branch in the flashback arc. |
| `romantic_score` | General romantic intensity in the Minh/Yuuka backstory. |
| `boundary_score` | Boundary-setting / distance / emotional separation pressure in the Minh/Yuuka arc. |

## Explicit `story_flag(...)` flags

These are literal flags currently set by scenes or helper functions.

### Romance lock / route block flags

| Flag | Meaning |
|---|---|
| `lock_minh_romance_except_yuuka` | Marks that Minh is locked into the Yuuka relationship path. Set by the romance-lock helper. |
| `lock_yuuka_romance_except_minh` | Marks that Yuuka is locked into the Minh relationship path. Set by the romance-lock helper. |
| `blocked_tam_minh_commit` | Records that Tâm-Minh should be blocked once Minh is locked to Yuuka. |
| `blocked_thienan_minh_commit` | Records that Thiên An-Minh should be blocked once Minh is locked to Yuuka. |
| `blocked_yuuka_single_true` | Records that Yuuka single/true-style outcomes are blocked once Yuuka is locked to Minh. |
| `minh_romance_open_after_yuuka` | Marks the old-friends branch where Minh is free to pursue someone else later. |
| `minh_route_unlocked` | Marks that Minh's route has been unlocked. |

### Prologue / dream memory flags

| Flag | Meaning |
|---|---|
| `dream_remembered_face` | Tâm most strongly remembers the man's face from the dream. |
| `dream_remembered_rain` | Tâm most strongly remembers the rain / atmosphere from the dream. |
| `dream_ignored` | Tâm chooses to dismiss or downplay the dream. |
| `huyen_knows_dream` | Huyền has been told about Tâm's dream. |
| `huyen_teases_dream` | Huyền responds to the dream in a teasing way. |
| `tam_keeps_dream_private` | Tâm does not tell Huyền about the dream. |

### Early Tâm / Huyền / interview flags

| Flag | Meaning |
|---|---|
| `tam_supports_huyen` | Tâm actively supports Huyền during the interview-day opening. |
| `tam_huyen_taxi_bonding` | Tâm and Huyền share a stronger bonding beat during the ride / morning setup. |
| `tam_honest_about_interview_pressure` | Tâm is open about the pressure she feels around the interview. |
| `tam_honest_with_interview_insight` | Tâm gives a more candid or self-aware interview-related answer. |
| `tam_keeps_interview_vague` | Tâm avoids being direct about her interview pressure. |
| `tam_interview_passed` | Tâm passed the interview. |
| `huyen_interview_passed` | Huyền passed the interview. |
| `tam_huyen_first_job_offer` | Tâm and Huyền receive their first job offer milestone together. |
| `tam_huyen_strong_bond` | Their post-interview celebration creates a stronger bond. |
| `tam_notices_hoang_first` | Tâm is the first one to notice Hoàng at the dinner scene. |
| `huyen_notices_hoang_first` | Huyền is the first one to notice Hoàng at the dinner scene. |

### Tâm route / Thiên An / party flags

| Flag | Meaning |
|---|---|
| `tam_stays_with_huyen` | At the company party, Tâm chooses to stay near Huyền. |
| `tam_supports_thienan` | Tâm offers support to Thiên An in the family thread. |
| `tam_asked_thienan_happiness` | Tâm directly asks whether Thiên An is happy. |
| `tam_heard_minh_hint` | Tâm asks about Minh and picks up a hint about that history. |

### Yuuka / Minh-Yuuka observation flags

| Flag | Meaning |
|---|---|
| `ask_hoang_about_yuuka_later` | The player intends to ask Hoàng later about Yuuka. |
| `noticed_minyuu_pause` | Tâm notices the small pause between Minh and Yuuka, implying subtext. |

### Minh / Yuuka separation flags

| Flag | Meaning |
|---|---|
| `minyuu_clean_break` | Minh and Yuuka separate through a clear breakup. |
| `minyuu_silent_distance` | Minh and Yuuka drift apart through silence rather than explicit breakup. |
| `yuuka_left_first` | Yuuka leaves before Minh fully explains himself. |

### Final-route control flag

| Flag | Meaning |
|---|---|
| `final_scores_decide` | In the final choice hub, the player chooses not to force a target ending and lets current scores decide. |

## Relationship direction flags

These are not hand-written literal flag names in scenes. They are created through:

- `story_add_direction(character, direction)`
- stored as `direction_<character>_<direction>` inside `story_flags`

### Current direction values found in source

| Stored flag form | Meaning |
|---|---|
| `direction_hoang_hoang_tam_open` | Hoàng opens emotionally toward Tâm. |
| `direction_hoang_hoang_tam_pursue` | Hoàng directly pursues Tâm romantically. |
| `direction_hoang_hoang_friend_group` | Hoàng keeps his feelings in the safer friendship/group lane. |
| `direction_hoang_hoang_huyen_open` | Hoàng opens toward Huyền instead of focusing only on Tâm. |
| `direction_huyen_huyen_hoang_open` | Huyền becomes open to a Hoàng possibility. |
| `direction_huyen_huyen_hoang_commit` | Huyền commits to the Hoàng path. |
| `direction_tam_tam_hoang_open` | Tâm is open to Hoàng. |
| `direction_tam_tam_hoang_commit` | Tâm commits to Hoàng. |
| `direction_tam_tam_minh_open` | Tâm is open to Minh. |
| `direction_tam_tam_minh_commit` | Tâm commits to Minh. |
| `direction_tam_tam_career_focus` | Tâm prioritizes career over romance in that choice point. |
| `direction_thienan_thienan_minh_commit` | Thiên An commits to the Minh path. |
| `direction_minyuu_old_friend_seed` | Flashback branch seed for old-close-friends history. |
| `direction_minyuu_ex_lover_seed` | Flashback branch seed for ex-lovers history. |
| `direction_minyuu_still_lover_seed` | Flashback branch seed for still-lovers history. |
| `direction_minyuu_ex_lovers_need_separation` | The ex-lovers branch now requires an explicit separation step before finalization. |
| `direction_minh_minh_yuuka_old_friends` | Minh-side marker that the old-friends relation was finalized. |
| `direction_minh_minh_yuuka_ex_lovers` | Minh-side marker that the ex-lovers relation was finalized. |
| `direction_minh_minh_yuuka_still_lovers` | Minh-side marker that the still-lovers relation was finalized. |
| `direction_yuuka_yuuka_minh_old_friends` | Yuuka-side marker that the old-friends relation was finalized. |
| `direction_yuuka_yuuka_minh_ex_lovers` | Yuuka-side marker that the ex-lovers relation was finalized. |
| `direction_yuuka_yuuka_minh_still_lovers` | Yuuka-side marker that the still-lovers relation was finalized. |

## Practical reading notes

- If you need the full numeric/state definition, start with `game/story_state.rpy`.
- If you need to know which scores matter for endings, read `game/ending_rules.rpy` next.
- If you need to know where a score or flag is actually earned, search for `story_add('<name>'`, `story_flag('<name>'`, or `story_add_direction(...)` in `game/story/`.


-----------------
Giải thích thêm một chút các chỉ số:

## Numeric scores in `story_state`

### Maximum scores: from 0  - 100 points
Notes:
- Điểm có thể kiếm được từ nhiều route khác nhau, không bắt buộc phải chơi route cố định của nhân vật đó mới tăng được điểm. VD: điểm Tâm - Hoàng có thể tăng hoặc giảm ở cả 2 route Tâm và Hoàng.

### Tâm
Tâm có 2 nhánh romance là Hoàng hoặc Minh. 
- Nhánh mặc định là Hoàng, tuy nhiên nếu score không đủ cao thì đến chapter cuối, họ vẫn không ở bên nhau. Hoàng cực tôn trọng anh trai, nên nếu Tâm không đạt điểm công nhận từ Minh đủ cao thì se rất khó bước được vào gia đinh anh. Tương tự cho Yuuka. Điểm số dự kiến:
| Score | Min value |
|---|---|
| `tam_hoang_interest` | 75+ |
| `tam_minh_drawn` | 50+ |
| `tam_self_clarity` | 50+ |
| `tam_respect_yuuka` | 25+ |
| `tam_insecurity` | 25- |
| `tam_observation` | 25+ |
| `career_tam` | 50+ |

- Với nhánh Minh, điểm số cần khó hơn một chút, vì Minh là "ultra-final boss" rồi. Vẫn cần một sự thân thiết đủ với Hoàng để có thể đến đc với Minh. Điểm twist ở đây là Yuuka, cần điểm quan hệ với Yuuka cao để: hiểu Minh hơn từ tương tác với Yuuka; và để Yuuka công nhận và chấp nhận rút lui. Điểm nghề nghiệp cao để đủ tự tin và vị trí có thể tương xứng với anh.  Điểm số dự kiến:
| Score | Min value |
|---|---|
| `tam_hoang_interest` | 50- |
| `tam_minh_drawn` | 90+ |
| `tam_self_clarity` | 75+ |
| `tam_respect_yuuka` | 50+ |
| `tam_insecurity` | 25- |
| `tam_observation` | 50+ |
| `career_tam` | 75+ |


### Hoàng
Có 2 route  romances:  với Tâm và với Huyền. Với cả 2 route này thì các điểm số chung cần đạt được dự kiến là:
| Score | Meaning |
|---|---|
| `hoang_tam_trust` | 75+ cho route với Tâm |
| `hoang_huyen_interest` | 75+ cho route với Huyền |
| `hoang_insecurity` | 15- |
| `hoang_self_acceptance` | 80+ |
| `hoang_professional_credit` | 90+ |


### Huyền
Cần đạt số điểm tối thiểu để có ending tốt:
| Score | Meaning |
|---|---|
| `huyen_quan_trust` | 75+ cho  nhánh QUân |
| `huyen_hoang_interest` | 75+ cho nhánh Hoàng. |
| `career_huyen` | 50+ |

### Thiên An

| Score | Meaning |
|---|---|
| `thienan_quang_trust` | tối thiểu 90+ choh nhánh Quang. |
| `thienan_minh_residue` | điểm này sẽ giảm dần trong game, cần còn tối thiểu 50+ cho nhánh Minh |
| `family_pressure_thienan` | điểm này sẽ giảm dần trong game, nếu còn 60+ điểm ở final và lớn hơn điểm `thienan_self_assertion` thì Thiên An sẽ kết hôn theo gia đình sắp xếp |
| `thienan_self_assertion` | 50+ |

### Minh / Yuuka shared arc
Hai nhân vật này chủ yếu phát triển quan hệ trong phase quá khứ. Nếu người chơi không đạt được điểm tối thiểu thì sẽ "game over" luôn. 

| Score | Meaning |
|---|---|
| `minh_yuuka_trust` | 80+ |
| `minh_yuuka_intimacy` | 75+ |
| `minh_yuuka_unresolved` | điểm này sẽ giảm dần trong game, 28- |
| `old_friend_score` | 80+ |
| `ex_lover_score` | 80+ |
| `still_lover_score` | 80+ |
| `romantic_score` | 43+ |
| `boundary_score` | 34- |

Ba nhánh `old_friend_score`, `ex_lover_score`, `still_lover_score` là exclusive và dựa theo nhánh đã chốt ở arc flashback. 