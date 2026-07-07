# Visual Novel Timeline — Tựa Gió, Tựa Mây

**Version:** 2026-07-05 score/flag alignment update  
**Purpose:** Route-map timeline for Ren'Py progression metadata, ending rules, and future choice definitions.  
**Score scale:** all numeric scores use **0–100**.

---

# 0. Update Notes

This version updates the timeline to match the newer route spine:

- Score thresholds now use **0–100**, not the old `0–6` / `+1` style.
- Choice effects should use a consistent delta rhythm:
  - **±5** = small beat / subtle acknowledgement
  - **±10** = meaningful scene choice
  - **±15** = major route-defining choice
  - **±20** = crisis-level event or branch lock
- Adds **Thiên An — Arranged Marriage** as a valid ending path.
- Clarifies that **Minh/Yuuka flashback resolution is mandatory**. If the player fails the core Minyuu requirement, final resolution should fall to `e24_doom`.
- Aligns score and flag names with `story_state.rpy` / `ending_rules.rpy` where possible.
- Adds missing timeline flags for route readability. Some are narrative/planning flags and may need to be added in scenes later.

---

# 1. Chapter ID Mapping

```text
Spec Chapter           | Code ID                                | Route     | Status
-----------------------|----------------------------------------|-----------|-----------------------
Prologue               | prologue_rain_dream                    | tam       | DONE
C01 — Ngày phỏng vấn   | tam_c01_interview_day                  | tam       | DONE
C02 — Buổi tiệc công ty| tam_c02_company_party                  | tam       | DONE
C03 — Chị gái Thiên An | tam_c03_thienan_family                 | tam       | DONE
C04 — Căn nhà của anh  | hoang_h01_brother_house                | hoang     | SKELETON
C05 — Buổi hẹn CN      | tam_c05_sunday_date                    | tam       | SKELETON
C06 — Minh về nước     | tam_c06_minh_returns                   | tam       | SKELETON
C07 — Minh ở công ty   | tam_c07_minh_at_company                | tam       | SKELETON
C08 — Yuuka xuất hiện  | yuuka_c08_festival_arrival             | yuuka     | SKELETON
C09 — Buổi chiếu phim  | yuuka_c09_yuukas_work                  | yuuka     | SKELETON
C10 — Dự án lệch nhịp  | work_c10_project_festival_overlap      | work      | SKELETON
C11 — Bữa tối người cũ | group_c11_social_dinner                | group     | SKELETON
C12 — Minyuu flashback | fb_minyuu_01-03                        | minh      | SKELETON
C13 — Tâm chọn vị trí  | tam_c20a_tam_minh_possible             | tam       | SKELETON
C14 — Điểm gãy Minyuu  | fb_minyuu_04a/b/c + fb_05b             | minh      | SKELETON
C15 — Yuuka interlude  | yuuka_c18a/b/c                         | yuuka     | SKELETON
C16 — Khủng hoảng dự án| work_c16_project_crisis                | work      | SKELETON
C17 — Bóng Minh        | hoang_h05_shadow_of_minh               | hoang     | SKELETON
C18 — Habit of You     | yuuka_c18a/b/c                         | yuuka     | SKELETON
C19 — City After Fest  | c19a/b/c                               | minh      | SKELETON
C20 — Tam late choices | tam_c20a + tam_c20b                    | tam       | SKELETON
C21 — Thiên An path    | thienan_c21a + thienan_c21b            | thienan   | SKELETON
C22 — Huyền route      | huyen_c22_quan_or_hoang                | huyen     | SKELETON
C23 — Minyuu resolution| minyuu_c23a/b/c                        | minh      | SKELETON
C24 — Last choices     | final_c24_last_choices                 | final     | SKELETON
```

---

# 2. Core Design

Game không phải dating-sim kiểu “tặng đủ quà thì cưới”. Cái đó tiện, nhưng hơi rẻ. Truyện này sống bằng nhịp quan hệ, vết cũ, lựa chọn đúng lúc, và những người không nói hết điều mình biết.

Cấu trúc route hợp nhất:

> **Một canon cảm xúc có thật, nhưng người chơi có thể làm lệch nhịp, mở hoặc khóa những khả năng khác bằng lựa chọn đủ sớm.**

Game có 5 lớp logic:

1. **Main timeline:** các sự kiện lớn vẫn xảy ra.
2. **Relationship direction:** nhân vật nghiêng về ai, có dám bước tới không.
3. **Score consequence:** điểm không chỉ tăng ở “route chính”. Một scene của Hoàng vẫn có thể tăng/giảm điểm Tâm-Hoàng hoặc Huyền-Hoàng.
4. **Flashback influence:** lựa chọn trong quá khứ của Minh/Yuuka quyết định khóa/mở romance của Minh ở hiện tại.
5. **Exclusion route:** một số hướng tình cảm loại trừ nhau, vì nhân vật đã đi vào một lựa chọn tâm lý khác.

---

# 3. Score System

## 3.1 Delta Rhythm

```text
+5 / -5      small emotional beat, minor observation, polite support
+10 / -10    meaningful choice, route-relevant scene
+15 / -15    major route choice, confession, refusal, crisis intervention
+20 / -20    branch lock, family crisis, separation/reunion decision
```

For negative-nature scores, lower is better:

```text
tam_insecurity
hoang_insecurity
minh_yuuka_unresolved
boundary_score
family_pressure_thienan
doom_score
```

So for these:

```text
-10 tam_insecurity    # good: Tâm becomes steadier
+10 tam_insecurity    # bad: Tâm compares herself / destabilizes
-10 family_pressure   # good: Thiên An resists family pressure
+15 family_pressure   # bad: family crisis / arranged marriage pressure rises
```

---

## 3.2 Initial Character Scores

These are baseline emotional positions, **not final eligibility**.

```text
# Core relation state
minh_yuuka_relation        = "unknown"
minh_romance_lock          = False
yuuka_romance_lock         = False
doom_score                 = 0

# Tâm
tam_hoang_interest         = 35
tam_quang_interest         = 0
tam_quan_interest          = 0
tam_minh_drawn             = 5
tam_self_clarity           = 20
tam_respect_yuuka          = 0
tam_insecurity             = 35
tam_observation            = 20
career_tam                 = 15

# Hoàng
hoang_tam_trust            = 35
hoang_huyen_interest       = 5
hoang_insecurity           = 30
hoang_self_acceptance      = 35
hoang_professional_credit  = 30

# Huyền
huyen_quan_trust           = 10
huyen_quan_interest        = 5
huyen_hoang_interest       = 10
career_huyen               = 15

# Thiên An
thienan_quang_trust        = 35
thienan_minh_residue       = 65
family_pressure_thienan    = 70
thienan_self_assertion     = 35
quang_persistence          = 60

# Minh / Yuuka
minh_yuuka_trust           = 0
minh_yuuka_intimacy        = 0
minh_yuuka_unresolved      = 55
old_friend_score           = 0
ex_lover_score             = 0
still_lover_score          = 0
romantic_score             = 0
boundary_score             = 50

ending_support             = []
```

---

## 3.3 Ending Thresholds

### Tâm

#### Tâm — Hoàng ending

```text
tam_hoang_interest         >= 75
tam_minh_drawn             >= 50
tam_self_clarity           >= 50
tam_respect_yuuka          >= 25
tam_insecurity             <= 25
tam_observation            >= 25
career_tam                 >= 50
hoang_tam_trust            >= 75
hoang_insecurity           <= 15
hoang_self_acceptance      >= 80
hoang_professional_credit  >= 90
NOT direction_tam_tam_minh_commit
ending_support includes e02_tam_hoang
```

Note: `tam_minh_drawn >= 50` here is not “Tâm yêu Minh”. It means Tâm has faced the impression Minh left on her clearly enough. If this score is too low, her later choice of Hoàng feels untested and a bit… dễ dãi. Không ổn.

#### Tâm — Minh ending

```text
minh_yuuka_relation        == old_close_friends
minh_romance_lock          == False
minyuu_shared_arc_ok       == True
tam_hoang_interest         <= 50
hoang_tam_trust            >= 50
tam_minh_drawn             >= 90
tam_self_clarity           >= 75
tam_respect_yuuka          >= 50
tam_insecurity             <= 25
tam_observation            >= 50
career_tam                 >= 75
direction_tam_tam_minh_commit
ending_support includes e03_tam_minh
```

This is the rare route. Minh is the ultra-final boss, and yes, unfortunately he knows it.

---

### Hoàng

```text
# Hoàng — Tâm
hoang_tam_trust            >= 75

# Hoàng — Huyền
hoang_huyen_interest       >= 75
huyen_hoang_interest       >= 75

# Shared Hoàng growth gate
hoang_insecurity           <= 15
hoang_self_acceptance      >= 80
hoang_professional_credit  >= 90
```

---

### Huyền

```text
# Huyền — Quân
huyen_quan_trust           >= 75
career_huyen               >= 50
NOT direction_huyen_huyen_hoang_commit

# Huyền — Hoàng
huyen_hoang_interest       >= 75
hoang_huyen_interest       >= 75
career_huyen               >= 50
NOT direction_tam_tam_hoang_commit
```

---

### Thiên An

```text
# Thiên An — Quang
thienan_quang_trust        >= 90
thienan_self_assertion     >= 50
family_pressure_thienan    < 60 OR family_pressure_thienan <= thienan_self_assertion
ending_support includes e06_thienan_quang

# Thiên An — Minh
minh_yuuka_relation        == old_close_friends
minh_romance_lock          == False
minyuu_shared_arc_ok       == True
thienan_minh_residue       >= 50
thienan_self_assertion     >= 50
family_pressure_thienan    < 60 OR family_pressure_thienan <= thienan_self_assertion
direction_thienan_thienan_minh_commit
ending_support includes e07_thienan_minh

# Thiên An — Single
thienan_self_assertion     >= 50
family_pressure_thienan    < 60 OR family_pressure_thienan <= thienan_self_assertion
ending_support includes e08_thienan_single

# Thiên An — Arranged Marriage
family_pressure_thienan    >= 60
family_pressure_thienan    > thienan_self_assertion
ending_support includes e09_thienan_arranged
```

Arranged Marriage is not “bad end màu mè”. It is a sacrifice ending: Thiên An chooses family survival over self-choice.

---

### Minh / Yuuka shared arc

This phase is mandatory. If it fails, the story resolves to `e24_doom`.

```text
minh_yuuka_relation in:
  - old_close_friends
  - ex_lovers_long_separated
  - still_lovers

minh_yuuka_trust           >= 80
minh_yuuka_intimacy        >= 75
minh_yuuka_unresolved      <= 28

# Exclusive branch score based on relation:
old_friend_score           >= 80  if relation == old_close_friends
ex_lover_score             >= 80  if relation == ex_lovers_long_separated
still_lover_score          >= 80  if relation == still_lovers

romantic_score             >= 43
boundary_score             <= 34
```

The three branch scores are exclusive. Do not let a playthrough accumulate all three above threshold unless you enjoy debugging ghosts. Which, respectfully, no.

---

# 4. Score / Flag Registry

## 4.1 Runtime Score Keys

These are the score keys currently expected by the updated route logic.

```text
doom_score

tam_hoang_interest
tam_quang_interest
tam_quan_interest
tam_minh_drawn
tam_self_clarity
tam_respect_yuuka
tam_insecurity
tam_observation
career_tam

hoang_tam_trust
hoang_huyen_interest
hoang_insecurity
hoang_self_acceptance
hoang_professional_credit

huyen_quan_trust
huyen_quan_interest
huyen_hoang_interest
career_huyen

thienan_quang_trust
thienan_minh_residue
family_pressure_thienan
thienan_self_assertion
quang_persistance
quang_persistence

minh_yuuka_trust
minh_yuuka_intimacy
minh_yuuka_unresolved
old_friend_score
ex_lover_score
still_lover_score
romantic_score
boundary_score
```

## 4.2 Optional Future Score Keys

These are not strictly required by current ending rules, but the timeline references them conceptually. Add only if scenes need finer branching.

```text
career_yuuka               # Only needed if Yuuka career should be scored separately.
group_trust                # Friend-group stability; can remain flags-only for MVP.
family_business_damage     # Useful if crisis outcome needs more granularity than doom_score.
```

For now, avoid adding too many “cute little scores”. They multiply like rabbits and then someone has to feed them.

---

## 4.3 Relationship Direction Flags

Directions use the helper:

```renpy
story_add_direction("<character>", "<direction>")
```

The resulting flag is:

```text
direction_<character>_<direction>
```

### Tâm

```text
direction_tam_tam_hoang_open
direction_tam_tam_hoang_commit
direction_tam_tam_minh_open
direction_tam_tam_minh_commit
direction_tam_tam_career_focus
direction_tam_tam_support_huyen
direction_tam_tam_quang_open              # optional rare route
```

### Hoàng

```text
direction_hoang_hoang_tam_open
direction_hoang_hoang_tam_pursue
direction_hoang_hoang_huyen_open
direction_hoang_hoang_friend_group
```

### Huyền

```text
direction_huyen_huyen_hoang_open
direction_huyen_huyen_hoang_commit
direction_huyen_huyen_quan_open
direction_huyen_huyen_quan_commit
```

### Minh / Yuuka

```text
direction_minh_minh_yuuka_old_friends
direction_minh_minh_yuuka_ex_lovers
direction_minh_minh_yuuka_still_lovers

direction_yuuka_yuuka_minh_old_friends
direction_yuuka_yuuka_minh_ex_lovers
direction_yuuka_yuuka_minh_still_lovers

direction_minyuu_old_friend_seed
direction_minyuu_ex_lover_seed
direction_minyuu_still_lover_seed
direction_minyuu_ex_lovers_need_separation
```

### Thiên An / Quang

```text
direction_thienan_thienan_quang_open
direction_thienan_thienan_minh_commit
direction_thienan_thienan_single
direction_thienan_thienan_family_arranged

direction_quang_quang_thienan_commit
direction_quang_quang_tam_open             # optional rare route
```

---

## 4.4 Important Story Flags

### Romance lock / route block

```text
lock_minh_romance_except_yuuka
lock_yuuka_romance_except_minh
blocked_tam_minh_commit
blocked_thienan_minh_commit
blocked_yuuka_single_true
minh_romance_open_after_yuuka
minh_route_unlocked
```

### Prologue / dream

```text
dream_remembered_face
dream_remembered_rain
dream_ignored
huyen_knows_dream
huyen_teases_dream
tam_keeps_dream_private
tam_remember_rain
```

### Tâm / Hoàng / Huyền route state

```text
tam_hoang_level_up
tam_hoang_stable_path
tam_hoang_break
tam_hoang_never_started
tam_explain_later
tam_minh_possible
tam_minh_private_scene
tam_minh_late_night_work
tam_step_back_choice

hoang_jealousy_resolved
hoang_huyen_possible
hoang_huyen_late_path
hoang_independent_ending_support

huyen_hoang_possible
huyen_quan_side_01
huyen_quan_after_work
```

### Minh / Yuuka

```text
old_friend_seed
ex_lover_seed
still_lover_seed
ex_lovers_need_separation
minyuu_clean_break
minyuu_silent_distance
yuuka_left_first
yuuka_return_standing
yuuka_respect_boundary
yuuka_fear_repeating_past
yuuka_confess_without_running
yuuka_single_possible
minh_yuuka_reopen
minh_yuuka_guarded
minh_yuuka_closed
minh_can_ask_directly
```

### Thiên An / family crisis

```text
thienan_old_story_hint
thienan_private_talk
thienan_quang_open
thienan_minh_flashback
thienan_family_arranged
arranged_marriage_path
arranged_marriage_offer_seen
thienan_arranged_accepts
thienan_arranged_refuses
quang_identity_revealed

family_business_crisis_started
family_business_scandal_triggered
family_father_hospitalized
crisis_minh_adviser
crisis_quang_financial_support
crisis_hoang_legal_support
crisis_bad_default
crisis_best_outcome
crisis_good_outcome
crisis_partial_legal_clear
crisis_partial_business_saved
```

### Ending support

```text
e01_canon_true
e02_tam_hoang
e03_tam_minh
e04_hoang_huyen
e05_huyen_quan
e06_thienan_quang
e07_thienan_minh
e08_thienan_single
e09_thienan_arranged
e10_minyuu_reunion
e11_minyuu_late_reunion
e12_minyuu_private_lovers
e13_minyuu_public_lovers
e14_minyuu_non_marriage
e15_minyuu_long_distance
e16_minh_single
e17_yuuka_single
e18_minyuu_mutual_single
e19_yuuka_career
e20_minyuu_friendship
e21_tam_independent
e22_huyen_independent
e23_hoang_single_growth
e24_doom
```

---

# 5. Route Unlock Logic

```text
# Default-unlocked:
Tâm route starts at prologue_rain_dream.

# Main chain:
prologue_rain_dream
  -> tam_c01_interview_day
  -> tam_c02_company_party
  -> tam_c03_thienan_family
  -> hoang_h01_brother_house
  -> tam_c05_sunday_date
  -> tam_c06_minh_returns
  -> tam_c07_minh_at_company
  -> yuuka_c08_festival_arrival

# Flashback Minyuu:
yuuka_c08_festival_arrival
  -> fb_minyuu_01_first_frame
  -> fb_minyuu_02_working_rhythm
  -> fb_minyuu_03_door_left_open
  -> one of:
       fb_minyuu_04a_old_friends
       fb_minyuu_04b_living_together
       fb_minyuu_04c_no_breakup
  -> if 04b:
       fb_minyuu_05b_separation
  -> yuuka_c09_yuukas_work

# Midgame:
yuuka_c09_yuukas_work
  -> work_c10_project_festival_overlap
  -> group_c11_social_dinner
  -> work_c16_project_crisis
  -> hoang_h05_shadow_of_minh

# Branch-based present Yuuka:
hoang_h05_shadow_of_minh
  -> yuuka_c18a_career_interlude
  -> yuuka_c18b_habit_of_you
  -> yuuka_c18c_long_distance_interlude

# City After Festival:
yuuka_c18a -> c19a_city_after_festival_old_friends
yuuka_c18b -> c19b_city_after_festival_ex_lovers
yuuka_c18c -> c19c_city_after_festival_still_lovers

# Late game:
c19a/b/c
  -> tam_c20a_tam_minh_possible
  -> tam_c20b_admiration_vs_love
  -> thienan_c21a_minh_possible
  -> thienan_c21b_choose_own_path
  -> huyen_c22_quan_or_hoang
  -> minyuu_c23a/b/c
  -> final_c24_last_choices
```

---

# 6. Main Timeline with Score / Flag Effects

## PROLOGUE — `prologue_rain_dream`

### Function

Foreshadow Minh through Tâm's dream. The dream should not “explain fate”. It should feel like a small safety memory misplaced in the wrong life.

### Choices

```text
A. Cố nhớ mặt người trong mơ
+10 tam_minh_drawn
+5 tam_observation
flag: dream_remembered_face

B. Nhớ cơn mưa hơn là người
+5 tam_minh_drawn
+10 tam_observation
flag: dream_remembered_rain

C. Gạt đi vì chỉ là mơ
+5 tam_self_clarity
+5 career_tam
flag: dream_ignored

D. Kể cho Huyền
+5 career_huyen
flag: huyen_knows_dream
flag: huyen_teases_dream
```

---

## C01 — `tam_c01_interview_day`

### Function

Introduce Tâm and Huyền through pressure, not exposition. First visual seed of Hoàng.

### Choices

```text
A. Tâm chuẩn bị kỹ, trả lời có cấu trúc
+10 career_tam
+5 tam_self_clarity

B. Tâm hỗ trợ Huyền trước phỏng vấn
+5 career_huyen
+5 tam_observation
flag: tam_supports_huyen

C. Tâm nhìn Hoàng lâu hơn một chút ở nhà hàng
+10 tam_hoang_interest
+5 hoang_tam_trust

D. Huyền bình luận Hoàng hợp gu mình
+10 huyen_hoang_interest
+5 hoang_huyen_interest
flag: huyen_tease_hoang
```

---

## C02 — `tam_c02_company_party`

### Function

First active Tâm/Hoàng/Huyền branching. Quân is seeded by reputation and work standards.

### Branch A — Tâm approaches Hoàng

```text
Condition:
tam_hoang_interest >= 40 OR direct player choice

Effects:
+15 tam_hoang_interest
+15 hoang_tam_trust
-5 tam_insecurity
direction: tam / tam_hoang_open
direction: hoang / hoang_tam_open
flag: hoang_notices_tam
```

### Branch B — Hoàng approaches Tâm

```text
Condition:
hoang_notices_tam OR Tâm does not approach

Effects:
+10 tam_hoang_interest
+10 hoang_tam_trust
+5 hoang_self_acceptance
direction: hoang / hoang_tam_open
```

### Branch C — Huyền interacts with Hoàng more

```text
Condition:
huyen_hoang_interest >= 20 OR Tâm pushes Huyền forward

Effects:
+15 huyen_hoang_interest
+10 hoang_huyen_interest
direction: huyen / huyen_hoang_open
direction: hoang / hoang_huyen_open
direction: tam / tam_support_huyen
```

### Branch D — Tâm avoids social route

```text
Effects:
+10 career_tam
+5 tam_self_clarity
-5 tam_hoang_interest
direction: tam / tam_career_focus
```

---

## C03 — `tam_c03_thienan_family`

### Function

Introduce Thiên An as family pressure plus quiet competence. Seed Quang, Minh residue, and the later family crisis.

### Choices

```text
A. Tâm bênh Thiên An trước mẹ
+10 tam_self_clarity
+10 tam_observation
-10 family_pressure_thienan
flag: thienan_private_talk

B. Tâm hỏi Thiên An về quản lý / công việc
+15 career_tam
+5 tam_observation
flag: tam_project_management_skill

C. Tâm hỏi chị từng yêu ai chưa
+10 thienan_minh_residue
+5 tam_observation
flag: thienan_old_story_hint

D. Tâm im lặng để bữa cơm trôi qua
+10 family_pressure_thienan
+5 tam_insecurity
```

### Quang Seed

```text
If Quang appears as assistant/deputy:
+5 thienan_quang_trust
+5 quang_persistence
flag: quang_present_in_family_arc
```

---

## C04 — `hoang_h01_brother_house`

### Function

Hoàng POV. He lives in Minh's house, calls Minh for advice, and reveals his own insecurity under Minh's shadow.

### Gift Branches

#### Gift for Tâm

```text
Condition:
direction_tam_tam_hoang_open
hoang_tam_trust >= 45

Effects:
+10 tam_hoang_interest
+10 hoang_tam_trust
+5 hoang_self_acceptance
direction: hoang / hoang_tam_pursue
```

#### Gift for Huyền

```text
Condition:
direction_huyen_huyen_hoang_open
huyen_hoang_interest >= 25

Effects:
+10 huyen_hoang_interest
+10 hoang_huyen_interest
direction: hoang / hoang_huyen_open
```

#### Friend group gift

```text
Condition:
No clear romance direction

Effects:
+5 hoang_self_acceptance
+5 career_huyen
+5 career_tam
direction: hoang / hoang_friend_group
```

#### Bad / confused gift

```text
Effects:
+10 hoang_insecurity
-5 hoang_self_acceptance
flag: hoang_repair_attempt
```

---

## C05 — `tam_c05_sunday_date`

### Function

Soft upgrade chapter. No need for fireworks. Let the cup, car door, jacket, seat choice, and unasked question do the work.

### Branch A — Tâm / Hoàng canon date

```text
Condition:
direction_tam_tam_hoang_open OR direction_hoang_hoang_tam_open

Effects:
+15 tam_hoang_interest
+15 hoang_tam_trust
-10 tam_insecurity
+10 hoang_self_acceptance
direction: tam / tam_hoang_open
direction: hoang / hoang_tam_pursue
flag: tam_hoang_level_up
```

### Branch B — Hoàng / Huyền date

```text
Condition:
direction_huyen_huyen_hoang_open
huyen_hoang_interest >= 30

Effects:
+15 huyen_hoang_interest
+15 hoang_huyen_interest
+5 hoang_self_acceptance
direction: huyen / huyen_hoang_open
direction: hoang / hoang_huyen_open
```

### Branch C — Three-person outing

```text
Effects:
+5 tam_hoang_interest
+5 huyen_hoang_interest
+5 hoang_huyen_interest
+5 hoang_tam_trust

If Tâm lightly opens:
  +10 tam_hoang_interest
  flag: tam_hoang_late_open

If Tâm pushes Huyền:
  +10 huyen_hoang_interest
  direction: tam / tam_support_huyen
```

---

## C06 — `tam_c06_minh_returns`

### Function

Minh returns. Tâm's dream/intuition collides with real life. Hoàng witnesses enough to become unsettled.

### Canon Branch

```text
Condition:
Tâm and Hoàng have meaningful connection.

Effects:
+15 tam_minh_drawn
+10 hoang_insecurity
+5 tam_observation
flag: minh_route_unlocked
flag: minh_notices_tam
```

### Tâm stays despite shock

```text
+10 tam_self_clarity
+10 hoang_tam_trust
-5 hoang_insecurity
```

### Tâm leaves abruptly

```text
+15 tam_minh_drawn
+15 hoang_insecurity
+10 tam_insecurity
flag: tam_explain_later
```

### Tâm tells Hoàng partial truth

```text
+15 hoang_tam_trust
+10 tam_self_clarity
-10 hoang_insecurity
```

---

## C07 — `tam_c07_minh_at_company`

### Function

Minh appears as project adviser. Tâm/Huyền interact with him through competence, not melodrama.

### Tâm keeps distance because of Hoàng

```text
+10 hoang_tam_trust
+10 tam_self_clarity
-10 tam_minh_drawn
direction: tam / tam_hoang_open
```

### Tâm asks Minh about work

```text
+15 career_tam
+10 tam_observation
+5 tam_minh_drawn
flag: tam_minh_professional_bond
```

### Tâm follows the pull toward Minh

```text
+15 tam_minh_drawn
+10 tam_insecurity
+10 hoang_insecurity
direction: tam / tam_minh_open
```

### Minh helps with a small work error

```text
+10 career_tam
+10 tam_observation
+5 tam_minh_drawn
```

---

## C08 — `yuuka_c08_festival_arrival`

### Function

Yuuka enters. Her presence tests whether Tâm understands the difference between attraction, history, and actual claim.

### Canon: Tâm is with Hoàng

```text
+15 tam_respect_yuuka
+10 tam_observation
+10 tam_insecurity
+10 minh_yuuka_unresolved
flag: group_notices_past
```

### Tâm-Minh lean

```text
Condition:
tam_minh_drawn >= 50

Effects:
+15 tam_respect_yuuka
+15 tam_insecurity
+10 tam_observation
flag: tam_step_back_choice
flag: yuuka_rival_not_rival_scene
```

### Hoàng-Huyền route

```text
+10 huyen_hoang_interest
+10 hoang_huyen_interest
+5 career_huyen
flag: huyen_question_minh
```

### Yuuka arrival core

```text
+10 minh_yuuka_trust
+10 minh_yuuka_intimacy
+10 minh_yuuka_unresolved
flag: yuuka_route_unlocked
```

---

## C09 — `yuuka_c09_yuukas_work`

### Function

Yuuka is seen as a professional. This matters. She cannot be reduced to Minh's old wound.

### Yuuka keeps professional mask

```text
+10 minh_yuuka_trust
+5 boundary_score
-5 minh_yuuka_unresolved
```

### Yuuka jokes like old days

```text
+10 minh_yuuka_intimacy
+10 romantic_score
+5 minh_yuuka_unresolved
```

### Minh comments on a precise detail in her film

```text
+15 minh_yuuka_trust
+10 minh_yuuka_intimacy
-10 minh_yuuka_unresolved
```

### Minh only says “Congratulations”

```text
+10 boundary_score
+10 minh_yuuka_unresolved
```

### Tâm witnesses and steps back

```text
+10 tam_self_clarity
+10 tam_respect_yuuka
-10 tam_insecurity
-10 tam_minh_drawn
```

---

## C10 — `work_c10_project_festival_overlap`

### Function

Work pressure begins. This prevents romance from floating in empty air like cheap perfume.

### Tâm career win

```text
Condition:
flag tam_project_management_skill

Effects:
+15 career_tam
+10 tam_observation
+5 hoang_professional_credit
```

### Huyền / Quân seed

```text
Condition:
Huyền confronts Quân directly but not stupidly.

Effects:
+15 huyen_quan_trust
+10 career_huyen
direction: huyen / huyen_quan_open
flag: huyen_quan_side_01
```

### Huyền / Hoàng comfort beat

```text
Condition:
direction_hoang_hoang_huyen_open

Effects:
+10 huyen_hoang_interest
+10 hoang_huyen_interest
-5 huyen_quan_trust
```

### Tâm / Minh risk

```text
Condition:
tam_minh_drawn >= 50

Effects:
+10 tam_minh_drawn
+10 career_tam
+10 hoang_insecurity
flag: tam_minh_private_scene
```

---

## C11 — `group_c11_social_dinner`

### Function

The dinner shows history without explaining it. Yuuka knows Minh's kitchen. Tâm and Hoàng both notice.

### Tâm helps Hoàng in the kitchen

```text
+15 hoang_tam_trust
+10 tam_hoang_interest
-10 tam_minh_drawn
-5 hoang_insecurity
```

### Tâm asks Yuuka about film

```text
+15 tam_respect_yuuka
+10 tam_observation
-5 tam_insecurity
flag: tam_yuuka_private_talk
```

### Huyền lightens the room

```text
+10 career_huyen
+5 huyen_quan_trust
+5 huyen_hoang_interest
```

### Minh cooks a Yuuka dish by memory

```text
+15 minh_yuuka_intimacy
+10 romantic_score
-10 minh_yuuka_unresolved
+10 tam_observation
flag: group_notices_past
```

---

## C12 — `fb_minyuu_01_03`

### Function

Flashback: living together begins. It defines whether affection became friendship, love, or an unbroken bond.

### Yuuka accepts help with clear rules

```text
+15 minh_yuuka_trust
-10 boundary_score
-5 minh_yuuka_unresolved
flag: yuuka_respect_boundary
```

### Yuuka depends on Minh heavily

```text
+15 minh_yuuka_intimacy
+10 romantic_score
+10 boundary_score
+10 minh_yuuka_unresolved
flag: yuuka_fear_repeating_past
```

### Yuuka teases Minh to break the room open

```text
+10 minh_yuuka_intimacy
+10 romantic_score
-5 boundary_score
```

### Minh keeps too much distance

```text
+15 boundary_score
+10 minh_yuuka_unresolved
```

---

## C13 — `tam_c20a_tam_minh_possible`

### Function

Tâm must choose where to stand. This protects her from becoming “the girl who got swept away by a cooler man”. No, thank you.

### Tâm tells Hoàng the partial truth

```text
+15 hoang_tam_trust
+15 tam_self_clarity
-10 hoang_insecurity
-10 tam_insecurity
direction: tam / tam_hoang_open
flag: blocked_tam_minh_commit unless later breakup branch
```

### Tâm steps back from Hoàng

```text
+15 tam_self_clarity
+10 tam_insecurity
+10 hoang_insecurity
flag: tam_hoang_break
flag: tam_minh_possible
flag: hoang_huyen_possible
```

### Tâm follows her pull toward Minh

```text
+15 tam_minh_drawn
+10 career_tam
+15 hoang_insecurity
direction: tam / tam_minh_open
flag: tam_minh_route_01
```

### Tâm pushes Huyền toward Hoàng

```text
Condition:
Tâm has not committed to Hoàng OR tam_hoang_break

Effects:
+15 huyen_hoang_interest
+10 hoang_huyen_interest
direction: tam / tam_support_huyen
direction: hoang / hoang_huyen_open
```

---

## C14 — `fb_minyuu_04a/b/c + fb_minyuu_05b`

### Function

The flashback branch lock. This is where Minh/Yuuka relation is canonized for the playthrough.

### 04A — Old Close Friends

```text
Set:
minh_yuuka_relation = "old_close_friends"

Effects:
+80 old_friend_score
+80 minh_yuuka_trust
+75 minh_yuuka_intimacy
+45 romantic_score
-20 minh_yuuka_unresolved
-20 boundary_score

Flags:
old_friend_seed
minh_romance_open_after_yuuka
```

Result:

- Minh/Yuuka had affection, maybe even mutual awareness, but never officially became lovers.
- Minh can later open to Tâm or Thiên An if current route earns it.
- Yuuka can end as friend, late confession, career, or single depending later support.

### 04B — Ex-Lovers / Living Together / Separation

```text
Set after fb_minyuu_05b:
minh_yuuka_relation = "ex_lovers_long_separated"

Effects:
+80 ex_lover_score
+85 minh_yuuka_trust
+80 minh_yuuka_intimacy
+70 romantic_score
-30 boundary_score
# unresolved must be repaired later:
minh_yuuka_unresolved should end <= 28

Flags:
ex_lover_seed
ex_lovers_need_separation
yuuka_left_first OR minyuu_silent_distance
lock_minh_romance_except_yuuka
lock_yuuka_romance_except_minh
```

Result:

- Canon separation/reunion path.
- Minh is locked away from Tâm/Thiên An romance.
- Yuuka has strongest career growth in this branch.

### 04C — Still Lovers / No Breakup

```text
Set:
minh_yuuka_relation = "still_lovers"

Effects:
+80 still_lover_score
+90 minh_yuuka_trust
+85 minh_yuuka_intimacy
+75 romantic_score
-30 minh_yuuka_unresolved
-25 boundary_score

Flags:
still_lover_seed
lock_minh_romance_except_yuuka
lock_yuuka_romance_except_minh
```

Result:

- Minh/Yuuka never fully separate.
- Yuuka becomes known, but less brilliant than canon because the long solitude did not refine her as brutally.
- No Tâm-Minh or Thiên An-Minh route.

---

## C15 / C18 — `yuuka_c18a/b/c`

### Function

Playable montage of Yuuka's years away / emotional development.

### Tokyo / Akiko section

```text
Yuuka avoids naming her grief:
+10 minh_yuuka_unresolved
+5 boundary_score

Yuuka admits she misses Minh:
+10 minh_yuuka_trust
-10 minh_yuuka_unresolved
```

### First job section

```text
Yuuka treats Minh's influence as her own growth:
+10 minh_yuuka_trust
-5 minh_yuuka_unresolved

Yuuka recognizes “the habit of him”:
+15 minh_yuuka_intimacy
+10 romantic_score
-10 minh_yuuka_unresolved
```

### Ayumi section

```text
Yuuka gets defensive:
+10 minh_yuuka_unresolved
+5 doom_score

Yuuka learns from Ayumi:
+10 minh_yuuka_trust
-10 minh_yuuka_unresolved
flag: yuuka_return_standing
```

### Low point

```text
Yuuka cuts Minh out:
+20 boundary_score
+15 minh_yuuka_unresolved
flag: yuuka_single_possible

Yuuka turns longing into discipline:
-15 minh_yuuka_unresolved
-10 boundary_score
flag: yuuka_return_standing
```

---

## C16 — `work_c16_project_crisis`

### Function

Test competence under pressure.

### Tâm career success

```text
Condition:
career_tam >= 50
flag tam_project_management_skill

Effects:
+15 career_tam
+10 tam_self_clarity
+5 hoang_professional_credit
flag: tam_promotion_ending_support
```

### Huyền / Quân bond

```text
Condition:
direction_huyen_huyen_quan_open

Effects:
+15 huyen_quan_trust
+10 career_huyen
direction: huyen / huyen_quan_open
flag: huyen_quan_after_work
```

### Minh / Tâm late-night work

```text
Condition:
tam_minh_drawn >= 70
NOT direction_tam_tam_hoang_commit

Effects:
+10 tam_minh_drawn
+10 career_tam
+5 tam_observation
flag: tam_minh_late_night_work
```

### Failure

```text
+10 doom_score
-10 career_tam
-10 career_huyen
+10 tam_insecurity
```

---

## C17 — `hoang_h05_shadow_of_minh`

### Function

Hoàng faces Minh's shadow. The scene must avoid making him petty. He can be hurt and still kind.

### Hoàng / Tâm repair

```text
Condition:
direction_tam_tam_hoang_open
hoang_tam_trust >= 60

Effects:
+15 hoang_tam_trust
+15 tam_hoang_interest
-15 hoang_insecurity
+15 hoang_self_acceptance
direction: tam / tam_hoang_commit
direction: hoang / hoang_tam_pursue
flag: hoang_jealousy_resolved
flag: tam_hoang_stable_path
```

### Break path

```text
Condition:
tam_minh_drawn high OR hoang_insecurity high

Effects:
+15 tam_self_clarity
+15 hoang_insecurity
flag: tam_hoang_break
flag: tam_minh_possible
flag: hoang_huyen_late_path
```

### Hoàng / Huyền path

```text
Condition:
direction_hoang_hoang_huyen_open

Effects:
+15 hoang_huyen_interest
+15 huyen_hoang_interest
-10 hoang_insecurity
+10 hoang_self_acceptance
```

### Hoàng independent growth

```text
+15 hoang_self_acceptance
+15 hoang_professional_credit
flag: hoang_independent_ending_support
```

---

## C19 — `c19a/b/c_city_after_festival`

### Function

Present-day Minyuu test. Same city, older people, less room for lying.

### Reopen

```text
Condition:
yuuka_return_standing
minh_yuuka_unresolved <= 35
boundary_score <= 40

Effects:
+15 minh_yuuka_trust
+15 minh_yuuka_intimacy
-15 minh_yuuka_unresolved
-10 boundary_score
flag: minh_yuuka_reopen
```

### Guarded

```text
Condition:
boundary_score high OR unresolved high

Effects:
+10 boundary_score
+10 minh_yuuka_unresolved
flag: minh_yuuka_guarded
```

### Break again

```text
Condition:
wrong choices + high unresolved

Effects:
+20 doom_score
+20 minh_yuuka_unresolved
flag: yuuka_single_possible
flag: minh_yuuka_closed
```

---

## C20 — `tam_c20b_admiration_vs_love`

### Function

Tâm and Minh test whether this is love, rescue instinct, admiration, or old dream residue.

### Tâm asks if Minh sees her as herself

```text
+15 tam_self_clarity
+10 tam_observation

If minh_yuuka_closed and old_close_friends:
  +15 tam_minh_drawn
  direction: tam / tam_minh_open

Else:
  -10 tam_minh_drawn
  +10 tam_respect_yuuka
```

### Tâm realizes it was impression, not love

```text
+20 tam_self_clarity
+15 tam_respect_yuuka
-20 tam_minh_drawn
-15 tam_insecurity
flag: tam_independent_or_hoang_repair
```

### Minh steps toward Tâm

```text
Condition:
minh_yuuka_relation == old_close_friends
minh_romance_lock == False
tam_minh_drawn >= 90
tam_self_clarity >= 75
career_tam >= 75
tam_hoang_interest <= 50

Effects:
direction: tam / tam_minh_commit
ending_support: e03_tam_minh
```

---

## C21 — `thienan_c21a/b`

### Function

Thiên An has four possible resolutions: Quang, Minh, Single, Arranged Marriage.

### Quang route

```text
Condition:
quang_persistence >= 60

Effects:
+15 thienan_quang_trust
+10 thienan_self_assertion
-10 family_pressure_thienan
direction: thienan / thienan_quang_open
```

### Minh residue

```text
Condition:
flag thienan_old_story_hint

Effects:
+10 thienan_minh_residue
+5 thienan_self_assertion
flag: thienan_minh_flashback
```

### Family arranged pressure

```text
Effects:
+15 family_pressure_thienan
-10 thienan_self_assertion
direction: thienan / thienan_family_arranged
flag: arranged_marriage_offer_seen
flag: arranged_marriage_path
```

### Thiên An refuses both family and romance

```text
+20 thienan_self_assertion
-15 family_pressure_thienan
direction: thienan / thienan_single
ending_support: e08_thienan_single
```

---

# 7. Family Business Crisis Arc

This arc may be implemented inside `thienan_c21b_choose_own_path` and `final_c24_last_choices`, or split into a future optional chapter if the project needs more breathing room.

## 7.1 Crisis Start

### Event

Family business begins to fail:

```text
- southern branch revenue drops
- contracts delay/cancel
- internal reports are beautified
- factions blame each other
- cashflow pressure rises
```

### Effects

```text
+15 family_pressure_thienan
+10 doom_score
flag: family_business_crisis_started
```

Thiên An steps in and temporarily stabilizes things.

```text
+10 thienan_self_assertion
+10 thienan_quang_trust   # if Quang supports professionally
-5 family_pressure_thienan
```

## 7.2 Scandal Trap

Opponent/internal planted person creates:

```text
- bad subcontracts
- hidden/scrubbed data
- shell-company transactions
- suspicious paper trail pointing to Thiên An
- media scandal timing
```

### Effects

```text
+20 family_pressure_thienan
+15 doom_score
flag: family_business_scandal_triggered
flag: family_father_hospitalized
```

## 7.3 Intervention Branch A — Minh as Strategic Adviser

### Conditions

```text
tam_observation >= 50 OR thienan_minh_residue >= 50
AND enough trust to ask Minh
AND Minh is not narratively blocked from helping
```

### Effects

```text
+10 tam_observation
+10 thienan_self_assertion
-15 family_pressure_thienan
-10 doom_score
flag: crisis_minh_adviser
```

### Result tiers

```text
Early:
  scandal prevented or reversed
  -20 family_pressure_thienan
  -15 doom_score

Mid:
  legal/economic damage reduced
  -10 family_pressure_thienan
  -10 doom_score

Late:
  partial vindication only
  -5 doom_score
  flag: crisis_partial_legal_clear
```

## 7.4 Intervention Branch B — Quang Reveals Identity

### Conditions

```text
thienan_quang_trust >= 70 OR tam_quang_interest >= 50
quang_persistence >= 60
```

### Effects

```text
+15 thienan_quang_trust
+15 thienan_self_assertion
-20 family_pressure_thienan
-10 doom_score
flag: quang_identity_revealed
flag: crisis_quang_financial_support
```

### Cost

```text
Quang must return closer to family power/inheritance conflict.
```

If Quang route is weak, this may feel like debt rather than love:

```text
if thienan_quang_trust < 70:
  +10 family_pressure_thienan
  flag: crisis_partial_business_saved
```

## 7.5 Intervention Branch C — Hoàng Asks Mother for Legal Fairness

### Conditions

```text
direction_tam_tam_hoang_commit OR hoang_tam_trust >= 75
Tâm tells Hoàng the family crisis truth
```

### Effects

```text
+10 hoang_self_acceptance
+15 hoang_professional_credit
-15 family_pressure_thienan
-10 doom_score
flag: crisis_hoang_legal_support
```

This is not “bẻ luật”. It is ensuring evidence is read fairly.

## 7.6 Arranged Marriage Offer

### Event

A powerful family offers to save the business through marriage alliance.

### Trigger

```text
family_pressure_thienan >= 60
family_business_scandal_triggered
NOT crisis_best_outcome
```

### Effects

```text
flag: arranged_marriage_offer_seen
flag: arranged_marriage_path
```

### Accept

```text
+20 family_pressure_thienan
-15 thienan_self_assertion
direction: thienan / thienan_family_arranged
flag: thienan_arranged_accepts
ending_support: e09_thienan_arranged
```

### Refuse

```text
+20 thienan_self_assertion
-10 family_pressure_thienan
flag: thienan_arranged_refuses

If Quang trust high:
  ending_support: e06_thienan_quang

If Minh path open:
  ending_support: e07_thienan_minh

If romance closed:
  ending_support: e08_thienan_single
```

## 7.7 Crisis Outcomes

### Best Outcome

```text
Conditions:
crisis_minh_adviser early
AND at least one of:
  crisis_quang_financial_support
  crisis_hoang_legal_support

Effects:
-30 family_pressure_thienan
-20 doom_score
+15 thienan_self_assertion
flag: crisis_best_outcome
```

### Good Outcome

```text
Conditions:
Any two intervention branches
OR one very strong early branch

Effects:
-20 family_pressure_thienan
-15 doom_score
flag: crisis_good_outcome
```

### Partial Legal Clear

```text
Conditions:
Minh/Hoàng late
No Quang support

Effects:
-10 doom_score
flag: crisis_partial_legal_clear
```

### Partial Business Saved

```text
Conditions:
Quang only
No Minh/Hoàng

Effects:
-10 family_pressure_thienan
flag: crisis_partial_business_saved
```

### Bad Default

```text
Conditions:
No strong intervention
Thiên An self-gathers until too late

Effects:
+20 doom_score
+20 family_pressure_thienan
flag: crisis_bad_default
```

### Doom

```text
Condition:
doom_score >= 80
OR Minyuu mandatory arc failed
OR final has no valid ending

Ending:
e24_doom
```

---

# 8. C22 — `huyen_c22_quan_or_hoang`

## Function

Resolve Huyền without making her a spare wheel. Huyền deserves an actual arc, not “Tâm didn’t pick Hoàng, so here, recycle.”

### Huyền — Quân

```text
Condition:
huyen_quan_trust >= 75
career_huyen >= 50
NOT direction_huyen_huyen_hoang_commit

Effects:
direction: huyen / huyen_quan_commit
ending_support: e05_huyen_quan
```

### Huyền — Hoàng

```text
Condition:
huyen_hoang_interest >= 75
hoang_huyen_interest >= 75
career_huyen >= 50
NOT direction_tam_tam_hoang_commit

Effects:
direction: huyen / huyen_hoang_commit
direction: hoang / hoang_huyen_open
ending_support: e04_hoang_huyen
```

### Huyền independent

```text
Condition:
career_huyen >= 50
No romance direction

Effects:
ending_support: e22_huyen_independent
```

---

# 9. C23 — `minyuu_c23a/b/c`

## Function

Resolve Minh/Yuuka based on branch.

### Old Close Friends

```text
Condition:
minh_yuuka_relation == old_close_friends
minyuu_shared_arc_ok

Possible supports:
e20_minyuu_friendship
e11_minyuu_late_reunion    # if neither Tâm/Thiên An route claims Minh
e17_yuuka_single
e19_yuuka_career
```

### Ex-Lovers

```text
Condition:
minh_yuuka_relation == ex_lovers_long_separated
minyuu_shared_arc_ok

Possible supports:
e10_minyuu_reunion
e11_minyuu_late_reunion
e18_minyuu_mutual_single
e16_minh_single
e17_yuuka_single
```

### Still Lovers

```text
Condition:
minh_yuuka_relation == still_lovers
minyuu_shared_arc_ok

Possible supports:
e13_minyuu_public_lovers
e14_minyuu_non_marriage
e15_minyuu_long_distance
e12_minyuu_private_lovers
```

### Incomplete Ending Variant — Yuuka Single Mother

This is a special sub-branch of the ex-lovers/canon branch.

```text
Conditions:
minh_yuuka_relation == ex_lovers_long_separated
first-night/separation flag exists
Yuuka does not return after four years
Minh/Yuuka reunion support is absent or delayed
Yuuka single support is active

Suggested flags:
minyuu_first_night
yuuka_pregnant_after_separation
yuuka_single_mother
minh_finds_child_late
```

Ending handling options:

- Fold into `e17_yuuka_single` if MVP needs fewer endings.
- Or create future `e25_yuuka_single_mother_late_reunion` if expanding beyond 24 endings.

Do not add this as a casual shock twist. If used, it needs a quiet pain structure, not soap-opera thunder.

---

# 10. C24 — `final_c24_last_choices`

Final chapter should not ask “who do you like?” like a menu at a food court. It should present choices that are emotionally earned.

## Tâm

```text
Choose Hoàng:
  requires tam_hoang_interest >= 75
  requires hoang_tam_trust >= 75
  ending_support: e02_tam_hoang

Choose Minh:
  requires old_close_friends
  requires tam_minh_drawn >= 90
  requires Yuuka respect gate
  direction: tam / tam_minh_commit
  ending_support: e03_tam_minh

Choose self/career:
  requires tam_self_clarity >= 50
  requires career_tam >= 50
  ending_support: e21_tam_independent
```

## Hoàng

```text
Choose Tâm:
  ending_support: e02_tam_hoang

Choose Huyền:
  ending_support: e04_hoang_huyen

Choose growth:
  requires hoang_self_acceptance >= 80
  requires hoang_professional_credit >= 90
  ending_support: e23_hoang_single_growth
```

## Huyền

```text
Choose Quân:
  ending_support: e05_huyen_quan

Choose Hoàng:
  ending_support: e04_hoang_huyen

Choose independent:
  ending_support: e22_huyen_independent
```

## Thiên An

```text
Choose Quang:
  requires thienan_quang_trust >= 90
  ending_support: e06_thienan_quang

Choose Minh:
  requires old_close_friends
  requires thienan_minh_residue >= 50
  direction: thienan / thienan_minh_commit
  ending_support: e07_thienan_minh

Choose self:
  requires thienan_self_assertion >= 50
  ending_support: e08_thienan_single

Accept arranged marriage:
  requires family_pressure_thienan >= 60
  requires family_pressure_thienan > thienan_self_assertion
  direction: thienan / thienan_family_arranged
  ending_support: e09_thienan_arranged
```

## Minh / Yuuka

```text
Still lovers:
  support e13/e14/e15/e12 based on exact final choice.

Ex-lovers:
  support e10/e11/e18 based on reunion level.

Old close friends:
  support e20 or open Minh to Tâm/Thiên An route if those are earned.
```

---

# 11. Ending Resolver Priority

Current priority should be treated as:

```text
1. e24_doom
2. mandatory Minyuu relation validation
3. e01_canon_true
4. still_lovers Minyuu resolver:
   - e13_minyuu_public_lovers
   - e14_minyuu_non_marriage
   - e15_minyuu_long_distance
   - e12_minyuu_private_lovers
5. ex_lovers Minyuu resolver:
   - e10_minyuu_reunion
   - e11_minyuu_late_reunion
   - e18_minyuu_mutual_single
   - e16_minh_single / e17_yuuka_single fallbacks
6. old_close_friends major alternatives:
   - e03_tam_minh
   - e07_thienan_minh
   - e20_minyuu_friendship
7. e09_thienan_arranged
8. e02_tam_hoang
9. e04_hoang_huyen
10. e05_huyen_quan
11. e06_thienan_quang
12. e19_yuuka_career
13. e21_tam_independent
14. e22_huyen_independent
15. e23_hoang_single_growth
16. e08_thienan_single
17. e16_minh_single
18. e17_yuuka_single
19. e24_doom fallback
```

Important: `e09_thienan_arranged` must be checked **before** softer side-route endings. Otherwise the family pressure route can be swallowed by “single” or “Quang” support even when the story says Thiên An has already sacrificed herself.

---

# 12. Clean Canon Route Summary

```text
prologue_rain_dream:
  Tâm dreams of a stranger in rain.

tam_c01_interview_day:
  Tâm and Huyền interview. Hoàng is first noticed.

tam_c02_company_party:
  Tâm talks to Hoàng. Huyền observes and teases.

tam_c03_thienan_family:
  Family dinner introduces Thiên An pressure and Quang seed.

hoang_h01_brother_house:
  Hoàng lives in Minh's house and calls Minh for advice.

tam_c05_sunday_date:
  Hoàng and Tâm's relationship upgrades.

tam_c06_minh_returns:
  Minh returns. Tâm is shaken. Hoàng notices.

tam_c07_minh_at_company:
  Minh acts as adviser. Tâm sees his competence.

yuuka_c08_festival_arrival:
  Yuuka appears. Old Minyuu history enters the room.

fb_minyuu_01-03:
  Living together flashback. Care becomes dangerous.

fb_minyuu_04a/b/c + fb_05b:
  Past branch locks: old friends / ex-lovers / still lovers.

yuuka_c09_yuukas_work:
  Yuuka is seen as a serious professional.

work_c10 + group_c11 + work_c16:
  Work crisis tests Tâm/Huyền/Quân/Minh.

hoang_h05_shadow_of_minh:
  Hoàng faces Minh's shadow.

yuuka_c18a/b/c:
  Yuuka processes the years away.

c19a/b/c:
  City after festival. Minyuu doors reopen or close.

tam_c20a/b:
  Tâm distinguishes admiration, dream residue, love, and choice.

thienan_c21a/b:
  Thiên An faces Quang, Minh residue, family crisis, and arranged marriage pressure.

huyen_c22:
  Huyền resolves toward Quân, Hoàng, or independence.

minyuu_c23:
  Minyuu resolves according to flashback branch.

final_c24_last_choices:
  Final supports are chosen.

ending_resolver:
  Final ending is determined by score, direction, relation, lock, and support.
```

---

# 13. Implementation Notes

## 13.1 Scene choice score deltas

Old scene effects such as:

```text
+1 trust_tam_hoang
+2 intimacy_minh_yuuka
```

should be converted to:

```text
+5 / +10 / +15 existing score keys
```

Example replacement:

```text
trust_tam_hoang       -> hoang_tam_trust
intimacy_tam_hoang    -> tam_hoang_interest + hoang_tam_trust
trust_tam_minh        -> tam_minh_drawn + tam_observation + career_tam
trust_hoang_huyen     -> hoang_huyen_interest + huyen_hoang_interest
trust_thienan_quang   -> thienan_quang_trust
distance_minh_yuuka   -> boundary_score
pain_minh_yuuka       -> minh_yuuka_unresolved
```

## 13.2 Avoid score inflation

Do not add `+15` too often. A 0–100 scale gives room, but if every scene is dramatic then no scene is dramatic. Tragic, in a spreadsheet way.

Suggested pacing:

```text
Early chapters:
  +5 to +10 mostly

Midgame:
  +10 standard, +15 for route-relevant choices

Late game:
  +15 for commitments
  +20 only for branch locks / crisis
```

## 13.3 Ending support is not score replacement

A route should need both:

```text
score threshold
AND direction/flag
AND ending_support
```

Score says the emotional groundwork exists.  
Direction says the character actually chose that path.  
Ending support says the final chapter allowed that ending.

All three are needed. Otherwise a route can appear because of math alone, and math is not romance. It is accounting.

---

# 14. Pending Expansion

Possible future additions:

```text
1. Add explicit family crisis chapter:
   thienan_c21c_family_business_crisis

2. Add optional Quang/Tâm route chapter:
   tam_c20c_quang_unexpected_route

3. Add optional Yuuka single-mother special ending:
   e25_yuuka_single_mother_late_reunion

4. Add career_yuuka score only if Yuuka career ending needs more than ending_support.
```

For MVP, the current 24-ending structure is enough. Do not let the route tree become a banyan tree with emotional licensing problems.
