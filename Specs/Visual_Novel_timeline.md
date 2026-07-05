Được, Sir. Em dựng lại thành bản **Game Timeline hoàn chỉnh dạng route-map**, có thể dùng làm nền để viết metadata `CHAPTERS`, `ENDING_RULES`, `CHOICE_DEFINITIONS`. Cách chia nhánh bên dưới bám theo progression system hiện tại: chapter có thể unlock route khác, mutually exclusive bằng `excludes`, set hướng quan hệ bằng `relationship_directions_set`, cộng/trừ cảm xúc bằng `emotional_effects`, và mở choice có điều kiện bằng `choice_unlocks`. 
Phần Yuuka/Minh flashback sẽ dùng cấu trúc “quá khứ ảnh hưởng hiện tại”, đặc biệt là tuyến chia xa: Yuuka rời đi, nhận ra Minh đã ngấm vào cách cô sống, rồi quay lại trong trạng thái đã trưởng thành hơn. 

---

## 4. Chapter ID Mapping (Spec → Code)

The spec uses numbered chapters (C01-C25) for readability. The code uses unique string IDs. Below is the mapping:

```text
Spec Chapter           | Code ID                          | Route     | Status
------------------------|----------------------------------|-----------|-----------------------
Prologue                | prologue_rain_dream              | tam       | DONE (authored)
C01 — Ngày phỏng vấn    | tam_c01_interview_day             | tam       | DONE (authored)
C02 — Buổi tiệc công ty | tam_c02_company_party             | tam       | DONE (authored)
C03 — Chị gái Thiên An  | tam_c03_thienan_family            | tam       | DONE (authored)
C04 — Căn nhà của anh   | hoang_h01_brother_house           | hoang     | SKELETON
C05 — Buổi hẹn CN       | tam_c05_sunday_date               | tam       | SKELETON
C06 — Minh về nước      | tam_c06_minh_returns              | tam       | SKELETON
C07 — Minh ở công ty    | tam_c07_minh_at_company           | tam       | SKELETON
C08 — Yuuka xuất hiện   | yuuka_c08_festival_arrival        | yuuka     | SKELETON
C09 — Buổi chiếu phim   | yuuka_c09_yuukas_work             | yuuka     | SKELETON
C10 — Dự án lệch nhịp   | work_c10_project_festival_overlap  | work      | SKELETON
C11 — Bữa tối người cũ  | group_c11_social_dinner           | group     | SKELETON
C12 — Flashback sống ch | fb_minyuu_01-03                   | minh      | DONE (authored)
C13 — Tâm chọn vị trí   | tam_c20a (late-game)              | tam       | SKELETON
C14 — Flashback chia xa | fb_minyuu_04a/b/c + fb_05b        | minh      | DONE (authored)
C15 — (not in spec)     | yuuka_c18a/b/c                    | yuuka     | SKELETON
C16 — Khủng hoảng dự án | work_c16_project_crisis            | work      | SKELETON
C17 — Hoàng bóng Minh   | hoang_h05_shadow_of_minh          | hoang     | SKELETON
C18 — Habit of You      | yuuka_c18a/b/c                    | yuuka     | SKELETON
C19 — City After Fest   | c19a/b/c                          | minh      | SKELETON
C20 — Tam late choices  | tam_c20a + tam_c20b               | tam       | SKELETON
C21 — Thiên An path     | thienan_c21a + thienan_c21b       | thienan   | SKELETON
C22 — Huyền route       | huyen_c22_quan_or_hoang           | huyen     | SKELETON
C23 — Minyuu resolution | minyuu_c23a/b/c                   | minh      | SKELETON
C24 — Last choices      | final_c24_last_choices            | final     | SKELETON
```

---

# MASTER GAME TIMELINE — Tựa Gió, Tựa Mây

## I. Core Design

Game này không nên là dating-sim thuần kiểu “tặng quà đủ điểm thì cưới”. Không hợp. Hơi… rẻ, và truyện này không nghèo đến thế.

Cấu trúc hợp hơn là:

> **Một tuyến canon cảm xúc có thật, nhưng người chơi có quyền làm lệch nhịp, mở hoặc khóa các khả năng tình cảm khác.**

Tức là game có:

* **Main timeline:** các sự kiện lớn vẫn xảy ra.
* **Relationship direction:** ai nghiêng về ai, có dám bước tới không.
* **Emotional consequence:** chọn sai không lập tức game over, nhưng làm nhân vật chậm mở lòng, né tránh, hoặc hiểu lầm lâu hơn.
* **Flashback influence:** lựa chọn trong quá khứ của Minh/Yuuka thay đổi lựa chọn khả dụng ở hiện tại.
* **Exclusion route:** một số chương bonus/extra khi đã chơi sẽ khóa chương khác, vì nhân vật đã đi vào một hướng tâm lý khác.

---

# II. Key Variables / Directions

## 1. Relationship Directions

Directions are set at runtime via `story_add_direction(character_id, direction)` and checked via `story_has_direction(character, direction)`. Each direction corresponds to a `story_flag("direction_{character}_{direction}")`.

```text
tam_direction:
- tam_hoang_open       # Tam opens up to Hoàng
- tam_hoang_commit     # Tam commits to Hoàng relationship
- tam_minh_open        # Tam opens up to Minh
- tam_minh_commit      # Tam commits to Minh path
- tam_career_focus     # Tam prioritises career

hoang_direction:
- hoang_tam_open       # Hoàng opens up to Tâm
- hoang_tam_pursue     # Hoàng actively pursues Tâm
- hoang_huyen_open     # Hoàng opens up to Huyền
- hoang_friend_group   # Hoàng stays in friend group

huyen_direction:
- huyen_hoang_open     # Huyền opens up to Hoàng
- huyen_hoang_commit   # Huyền commits to Hoàng

minh_direction:
- minh_yuuka_old_friends     # Minh-Yuuka as old friends
- minh_yuuka_ex_lovers       # Minh-Yuuka as ex-lovers
- minh_yuuka_still_lovers    # Minh-Yuuka still in love

yuuka_direction:
- yuuka_minh_old_friends     # Yuuka-Minh as old friends
- yuuka_minh_ex_lovers       # Yuuka-Minh as ex-lovers
- yuuka_minh_still_lovers    # Yuuka-Minh still in love

minyuu_direction:
- old_friend_seed            # Seed for old friends outcome
- ex_lover_seed              # Seed for ex-lovers outcome
- still_lover_seed           # Seed for still lovers outcome
- ex_lovers_need_separation  # Lock ex-lovers path through separation

thienan_direction:
- thienan_minh_commit  # Thiên An commits to Minh path
```


## 2. Story State Variables

Live runtime state is stored in the global `story_state` dictionary (defined in `game/story_state.rpy`). These variables are modified via `story_add(key, amount)` and `story_set(key, value)`.

```text
# Core relation state
minh_yuuka_relation     # unknown | old_close_friends | ex_lovers_long_separated | still_lovers
minh_romance_lock       # True locks Minh from romantic routes except Yuuka
yuuka_romance_lock      # True locks Yuuka from romantic routes except Minh
doom_score              # Accumulates toward doom ending (thresholds: 5, 8)

# Tâm
tam_hoang_interest      # Interest in Hoàng
tam_quang_interest      # Interest in Quang (static)
tam_quan_interest       # Interest in Quân
tam_minh_drawn          # Drawn toward Minh
tam_self_clarity        # Self-awareness
tam_respect_yuuka       # Respect for Yuuka
tam_insecurity          # Insecurity level
tam_observation         # Observation skill
career_tam              # Career progression

# Hoàng
hoang_tam_trust         # Trust in Tâm
hoang_huyen_interest    # Interest in Huyền
hoang_insecurity        # Insecurity level
hoang_self_acceptance   # Self-acceptance growth
hoang_professional_credit # Professional standing

# Huyền
huyen_quan_trust        # Trust in Quân
huyen_quan_interest     # Interest in Quân
huyen_hoang_interest    # Interest in Hoàng
career_huyen            # Career progression

# Thiên An
thienan_quang_trust     # Trust in Quang
thienan_minh_residue    # Residual feelings for Minh
family_pressure_thienan # Family pressure level
thienan_self_assertion  # Self-assertion growth
quang_persistance        # Quang's persistence (static)

# Minh-Yuuka
minh_yuuka_trust        # Mutual trust
minh_yuuka_intimacy     # Intimacy level
minh_yuuka_unresolved   # Unresolved tension
old_friend_score        # Score toward old friends outcome
ex_lover_score          # Score toward ex-lovers outcome
still_lover_score       # Score toward still lovers outcome
romantic_score          # Romantic intensity
boundary_score          # Boundary/avoidance score

# Ending support flags (set by late-game choices)
ending_support          # List of ending IDs unlocked by narrative choices
```

## 3. Route Unlock Logic (Actual)

Route unlocking is controlled by the progression system in `game/progression_data.rpy` and `game/progression_logic.rpy`. Each chapter has `prerequisites` (all must be completed) and/or `prerequisites_any` (any one must be completed). Below is the actual unlock graph:

```text
# Default-unlocked routes:
- Tâm (default_unlocked=True, entry: prologue_rain_dream)

# Route unlock conditions:
- Hoàng: unlocked after completing tam_c03_thienan_family
- Minh: unlocked after yuuka_c08_festival_arrival (via fb_minyuu_01)
- Yuuka: unlocked after tam_c07_minh_at_company (via yuuka_c08)
- Work/Group: unlocked via work_c10 (prereq: group_c11 prerequisites cascade)
- Huyền: unlocked via huyen_c22 (prereq: tam_c20b or thienan_c21b)
- Thiên An: unlocked via thienan_c21a (prereq: tam_c20b)
- Final: default_unlocked=False, entry via final_c24

# Core chapter prerequisite chain:
prologue_rain_dream
  -> tam_c01_interview_day
  -> tam_c02_company_party
  -> tam_c03_thienan_family
  -> hoang_h01_brother_house  (Hoàng POV)
  -> tam_c05_sunday_date
  -> tam_c06_minh_returns
  -> tam_c07_minh_at_company
  -> yuuka_c08_festival_arrival  (Yuuka enters)

# Flashback Minyuu chain (branching):
yuuka_c08 -> fb_minyuu_01 -> fb_minyuu_02 -> fb_minyuu_03
  -> fb_minyuu_04a OR fb_minyuu_04b OR fb_minyuu_04c  (branch)
  -> fb_minyuu_05b (from 04b only)
All fb_minyuu_04 branches -> yuuka_c09

# Mid-game parallel chapters:
yuuka_c09 -> work_c10 -> group_c11 -> work_c16
work_c16 -> hoang_h05_shadow_of_minh
hoang_h05 -> yuuka_c18a, yuuka_c18b, yuuka_c18c  (parallel, route-dependent)

# Late-game branches (mutually exclusive paths):
yuuka_c18a -> c19a (old friends path)
yuuka_c18b -> c19b (ex-lovers path)
yuuka_c18c -> c19c (still lovers path)
All c19 paths -> tam_c20b (convergence)

# Final routes (route-specific):
tam_c20b -> thienan_c21a (Thiên An-Minh possible)
         -> thienan_c21b (choose own path)
         -> huyen_c22 (Quân or Hoàng)
         -> minyuu_c23a/b/c (resolution, route-dependent)
         -> final_c24_last_choices (final chapter)
```

See `game/progression_data.rpy` for the full prerequisite graph with all 36 chapters.

---

# III. Main Timeline

---

# PROLOGUE (prologue_rain_dream) — Giấc mơ trong mưa

## POV

Tâm.

## Nội dung

Game mở đầu bằng một giấc mơ của Tâm.

Cô thấy mình đứng ở trạm xe bus trong một cơn mưa rất cũ. Mọi thứ mờ đi vì nước mưa và ánh đèn xe. Có một chàng trai đứng cạnh cô, không rõ mặt. Anh đưa cho cô một chiếc khăn giấy, hoặc kéo chiếc ô lệch về phía cô nhiều hơn một chút.

Không có lời tỏ tình. Không có cứu rỗi hào nhoáng. Chỉ là một hành động nhỏ.

Tâm tỉnh dậy, không nhớ rõ mặt người đó. Chỉ nhớ cảm giác: người ấy từng khiến cô thấy an toàn một cách rất lạ.

## Function

* Foreshadow Minh.
* Tạo `flag_dream_rain_man`.
* Nếu người chơi chọn “cố nhớ rõ gương mặt”, tăng `tam_minh_drawn`.
* Nếu chọn “gạt đi vì chỉ là mơ”, tăng `tam_grounded`.
* Nếu chọn “ghi lại giấc mơ”, unlock later choice khi gặp Minh: `tam_remember_rain`.

## Branch Effect

```text
Choice A: Cố nhớ người trong mơ
+1 tam_minh_drawn
+1 sensitivity

Choice B: Cười bản thân rồi dậy đi làm
+1 tam_grounded
+1 career_tam

Choice C: Gửi tin nhắn kể cho Huyền
+1 huyen_tam_bond
unlock: huyen_tease_dream
```

---

# CHAPTER 1 (tam_c01_interview_day) — Ngày phỏng vấn

## POV

Tâm.

## Nội dung chính

Tâm và Huyền cùng đi phỏng vấn xin việc. Hai cô gái còn trẻ, có năng lực, nhưng phản ứng khác nhau trước áp lực.

Tâm chuẩn bị kỹ, hơi căng, muốn mọi thứ “đúng”. Huyền thoải mái hơn, có vẻ lanh và biết xoay tình huống. Trong phần phỏng vấn, game có thể có mini-game speech/interview, lựa chọn thứ tự ý trả lời.

Hai người đều trúng tuyển.

Buổi tối, họ ăn mừng ở một nhà hàng sang trọng. Đây là lần đầu Hoàng nhìn thấy Tâm và Huyền. Lúc này họ chưa quen nhau. Hoàng đến đó cùng một người quen trong ngành/đối tác, không chủ động xen vào quá sâu, chỉ có vài khoảnh khắc ánh mắt chạm nhau.

Tâm có thể để ý Hoàng, Huyền có thể để ý, hoặc cả hai chỉ xem anh là “một anh đẹp trai bàn bên”.

## Canon

Tâm chú ý Hoàng, nhưng chưa làm gì. Huyền trêu.

## Branches

```text
Choice A: Tâm nhìn Hoàng lâu hơn một chút
+1 tam_hoang_interest
+1 hoang_notices_tam

Choice B: Tâm kéo Huyền khỏi việc hóng chuyện
+1 tam_grounded
+1 huyen_tam_bond

Choice C: Huyền bình luận Hoàng hợp gu mình
+1 huyen_hoang_interest
unlock: huyen_tease_hoang

Choice D: Tâm tập trung vào công việc mới
+1 career_tam
+1 tam_confidence
```

## Unlock

* `tam_c02_company_party`
* `tam_c03_thienan_family` seed

---

# CHAPTER 2 (tam_c02_company_party) — Buổi tiệc công ty

## POV

Tâm, có thể có đoạn ngắn Hoàng POV nếu đủ điều kiện.

## Nội dung

Tâm và Huyền bắt đầu đi làm. Quân — trưởng phòng khó tính — được giới thiệu qua những lời đồn trong công ty: năng lực cao, soi kỹ, ít khen, không thích nhân viên làm màu.

Buổi tiệc công ty diễn ra sau giai đoạn onboarding. Hoàng xuất hiện với tư cách nhà thiết kế kiến trúc trẻ, bạn của trưởng phòng/được mời hợp tác trong một dự án của công ty.

Đây là lần Tâm, Huyền và Hoàng chính thức có cơ hội nói chuyện.

## Canon

Tâm chủ động bắt chuyện với Hoàng. Hoàng ban đầu lịch sự, hơi phòng thủ, sau đó bị sự tự nhiên của Tâm làm mềm. Huyền đứng ngoài trêu, nhưng không chen.

## Game Branches

### Route A — Canon Seed: Tâm bắt chuyện

```text
Condition:
tam_hoang_interest >= 1 OR player chooses direct approach

Effects:
+2 trust_tam_hoang
+1 intimacy_tam_hoang
set tam_direction: tam_hoang_open
unlock: hoang_h01_first_impression
```

### Route B — Hoàng chủ động

```text
Condition:
hoang_notices_tam >= 1 AND Tâm không chủ động

Effects:
+1 trust_tam_hoang
+1 hoang_tam_interest
set hoang_direction: hoang_tam_open
unlock: tam_surprised_by_hoang
```

### Route C — Không gặp gỡ đáng kể

```text
Condition:
Tâm chọn né xã giao / tập trung Huyền / rời tiệc sớm

Effects:
+1 career_tam
-1 intimacy_tam_hoang
set hoang_direction: hoang_friend_group_possible
Hoàng và Tâm vẫn biết nhau, nhưng không thân.
```

### Route D — Huyền tương tác với Hoàng nhiều hơn

```text
Condition:
huyen_hoang_interest >= 1 OR Tâm đẩy Huyền lên nói chuyện

Effects:
+2 trust_hoang_huyen
+1 huyen_hoang_interest
set huyen_direction: huyen_hoang_interest
set tam_direction: tam_support_huyen
```

## Unlock

* `tam_c03_thienan_family`
* `hoang_h01_brother_house` (seed) nếu Tâm/Hoàng/Huyền có tương tác đủ.

---

# CHAPTER 3 (tam_c03_thienan_family) — Chị gái Thiên An

## POV

Tâm.

## Nội dung

Chương giới thiệu Thiên An: chị gái Tâm, xinh đẹp, tài giỏi, thành đạt, nhưng tình duyên không trọn vẹn. Mẹ thường xuyên giục xem mắt, giới thiệu người tốt, nhưng Thiên An không thật sự quan tâm.

Tâm về nhà ăn cơm. Không khí gia đình ấm nhưng có áp lực. Mẹ hỏi chuyện Thiên An, rồi tiện hỏi sang Tâm. Thiên An khéo léo chuyển hướng để bảo vệ em, Tâm cũng nhận ra chị mình mệt.

Đây là chương gia đình, nhưng cũng là chương đặt nền cho ước muốn thầm kín của Tâm: **chị mình cũng nên được hạnh phúc**.

Đồng thời, chương có nhánh career: Thiên An có thể gợi ý Tâm học thêm quản lý, triển khai dự án, cách đọc người trong môi trường công sở.

## Canon

Tâm thương chị, chưa can thiệp gì nhiều. Thiên An vẫn giữ khoảng cách với chuyện tình cảm.

## Branches

### Family Support

```text
Choice A: Tâm bênh Thiên An trước mẹ
+2 trust_tam_thienan
+1 tam_family_courage
unlock: thienan_private_talk
```

### Career Growth

```text
Choice B: Tâm hỏi Thiên An về quản lý dự án
+2 career_tam
unlock: tam_project_management_skill
unlock later choice: tam_handle_project_crisis
```

### Romance Curiosity

```text
Choice C: Tâm hỏi chị có từng yêu ai chưa
+1 thienan_minh_residue
+1 tam_insight_romance
unlock: thienan_old_story_hint
```

### Family Pressure

```text
Choice D: Tâm im lặng để bữa cơm trôi qua
+1 family_pressure_thienan
-1 trust_tam_thienan
```

## Unlock

* `hoang_h01_brother_house`
* `tam_c05_sunday_date`
* `thienan_c21a_minh_possible` soft-hidden until later.

---

# CHAPTER 4 (hoang_h01_brother_house) — Hoàng POV: Căn nhà của anh trai

## POV

Hoàng.

## Nội dung

Chương chuyển sang Hoàng. Người chơi thấy Hoàng sống một mình trong căn biệt thự của Minh. Không gian rộng, đẹp, hơi quá yên tĩnh với một người như Hoàng.

Hé lộ gia thế: cha mẹ làm nhà nước, có vị trí quan trọng nhưng không nói rõ. Không exposition lộ liễu. Chỉ qua cách Hoàng nhận điện thoại từ cha, cách anh tránh nói quá nhiều về gia đình, cách người khác nể anh “vừa đủ”.

Hoàng gọi/nhắn cho Minh đang ở xa. Hai anh em nói chuyện ngắn, không sướt mướt. Hoàng hỏi xin tư vấn chọn quà.

Tính chất món quà thay đổi theo route.

## Gift Branches

### Canon — Quà cho Tâm

```text
Condition:
tam_direction has tam_hoang_open
trust_tam_hoang >= 2

Gift:
Một món tinh tế, không quá đắt, liên quan đến thói quen của Tâm.
Ví dụ: sổ tay đẹp, kẹp tóc, khăn, hoặc một món nhỏ dùng được hằng ngày.

Effects:
+1 hoang_tam_commit
+1 intimacy_tam_hoang
```

### Hoàng — Huyền

```text
Condition:
huyen_hoang_interest >= 2
tam_support_huyen active

Gift:
Món có tính vui, hợp tính Huyền hơn: phụ kiện sáng, đồ decor bàn làm việc, vé workshop/trải nghiệm.

Effects:
+2 trust_hoang_huyen
set hoang_direction: hoang_huyen_open
```

### Friend Group

```text
Condition:
No romance lock

Gift:
Hoàng mua quà chung / chuẩn bị đồ ăn / vé sự kiện ba người.

Effects:
+1 trust_friend_group
+1 hoang_friend_group
```

### Bad/Confused Gift

```text
Condition:
hoang_insecurity_active OR player ignores Minh's advice

Effects:
-1 trust_target
+1 awkwardness
unlock: hoang_repair_attempt
```

## Minh Presence

Minh chỉ xuất hiện qua tin nhắn/cuộc gọi nhưng phải đủ “nặng”. Anh không nói nhiều, nhưng tư vấn chuẩn, vì Minh giỏi đọc người. Đồng thời lộ ra một chút: Hoàng rất tin anh trai.

## Unlock

* `tam_c05_sunday_date`
* `hoang_h01_brother_house` (tiếp)
* `hoang_h05_shadow_of_minh` seed

---

# CHAPTER 5 (tam_c05_sunday_date) — Buổi hẹn Chủ Nhật

## POV

Tâm hoặc Hoàng, tùy route.

## Nội dung

Một buổi Chủ Nhật đặc biệt. Đây là chương tăng gắn kết. Không cần drama lớn. Chỉ cần đủ nhiều hành động nhỏ.

## Branch Structure

### Route A — Canon Date: Hoàng & Tâm

Hoàng chủ động hẹn Tâm. Tâm sửa soạn kỹ hơn bình thường. Hoàng đến đón bằng xe hơi. Buổi hẹn có cảm giác vừa lạ vừa ngọt.

Họ ăn sáng, đi dạo, có một hoạt động nhẹ: xem triển lãm, chọn đồ nội thất, đi hiệu sách, hoặc ghé một chỗ Hoàng muốn cho Tâm thấy.

Quan trọng nhất là: Tâm nhận ra Hoàng đang cố bước ra khỏi vùng bị động.

```text
Effects:
+2 trust_tam_hoang
+2 intimacy_tam_hoang
set hoang_direction: hoang_tam_commit
set tam_direction: tam_hoang_open
unlock: tam_hoang_level_up
```

### Route B — Hoàng & Huyền

Nếu Huyền là người nghiêng về Hoàng, buổi hẹn riêng diễn ra với sắc thái khác: vui hơn, sắc hơn, đỡ ngượng hơn. Huyền dễ chọc Hoàng. Hoàng bị kéo ra khỏi nhịp phòng thủ nhanh hơn.

```text
Effects:
+2 trust_hoang_huyen
+2 intimacy_hoang_huyen
set hoang_direction: hoang_huyen_open
set huyen_direction: huyen_hoang_interest
```

### Route C — Hẹn ba người

Nếu không có romance lock, Hoàng rủ cả Tâm và Huyền. Không khí nhẹ, hợp cạ. Hoàng hơi thích Tâm hơn, nhưng Tâm không bật đèn xanh nên anh giữ chừng mực.

Huyền có thể nhận ra Hoàng thích Tâm.

```text
Effects:
+1 trust_friend_group
+1 trust_tam_hoang
+1 trust_hoang_huyen

Choice:
- Tâm bật đèn xanh nhẹ → unlock tam_hoang_late_open
- Tâm đẩy Huyền → unlock huyen_hoang_possible
- Tâm giữ bạn bè → set hoang_tam_restraint
```

## Unlock

* `tam_c06_minh_returns`
* `tam_c07_minh_at_company` seed
* `hoang_h05_shadow_of_minh` seed

---

# CHAPTER 6 (tam_c06_minh_returns) — Minh về nước

## POV

Tâm, Hoàng, optional Minh.

## Nội dung

Minh về nước. Hoàng đưa bạn về giới thiệu.

Đây là chương then chốt để unlock Minh route.

## Canon Branch

Tâm đang hẹn hò với Hoàng. Hoàng đưa Tâm về gặp Minh. Khi nhìn thấy Minh, Tâm bất ngờ bỏ về/khựng lại quá rõ. Không phải vì cô yêu Minh, mà vì giấc mơ/trạm mưa/ký ức mờ bật lên quá mạnh.

Hoàng thấy. Minh cũng thấy.

Sau đó dẫn tới buổi hẹn thứ hai: bàn ăn bốn người gồm Minh, Hoàng, Tâm, và Huyền. Bầu không khí có nhiều lớp: Hoàng cố bình thường, Tâm ngượng, Huyền quan sát, Minh lịch sự nhưng khó đọc.

```text
Effects:
unlock: minh_route
+1 tam_minh_drawn
+1 hoang_insecurity_active
+1 minh_notices_tam
```

## Huyền Route Branch

Nếu Hoàng đang nghiêng về Huyền, lần đầu chỉ có Hoàng đưa Huyền về gặp Minh.

Huyền thấy Minh thú vị. Không nhất thiết là thích kiểu lãng mạn; là kiểu “người này quá khó đọc, hơi đáng ghét, nhưng đáng để nhìn thêm”. Sau đó Huyền lôi Tâm tới bữa tối bốn người.

```text
Effects:
+1 huyen_minh_curiosity
+1 trust_hoang_huyen
unlock: dinner_four_people
```

## Friend Group Branch

Nếu không ai hẹn hò, Hoàng mời cả Tâm và Huyền về ăn tối, giới thiệu hai cô bạn thân trong công việc với Minh.

```text
Effects:
+1 trust_friend_group
unlock: minh_route
unlock: group_dinner_variation
```

## Critical Choices

```text
Tâm:
A. Ở lại dù bối rối
+1 tam_courage
+1 trust_hoang_tam
+1 minh_respect_tam

B. Bỏ về
+1 tam_minh_drawn
+1 hoang_insecurity_active
unlock: tam_explain_later

C. Nói thật một phần với Hoàng
+2 trust_tam_hoang
-1 hoang_insecurity_active
```

## Unlock

* `tam_c07_minh_at_company`
* `yuuka_c08_festival_arrival` seed
* `group_c11_social_dinner` seed

---

# CHAPTER 7 (tam_c07_minh_at_company) — Minh ở công ty

## POV

Mutually exclusive: Tâm POV hoặc Minh POV.

## Nội dung

Minh xuất hiện ở công ty với vai trò giám sát/cố vấn dự án từ tập đoàn đối tác lớn. Quân cũng xuất hiện rõ hơn ở vị trí trưởng phòng khó tính.

Tâm và Huyền tiếp xúc với Minh trong môi trường công việc.

Tâm bắt đầu nhận ra Minh không chỉ là “người trong mơ” hay “anh trai Hoàng”. Anh rất sắc, rất giỏi, và nguy hiểm theo kiểu có thể đọc được điều người khác chưa kịp nói.

Huyền thì thấy Minh “thú vị”, nhưng cũng biết đây không phải kiểu đàn ông dễ đùa quá tay.

## Route Structure

### Tâm POV — Emotional Route

Người chơi thấy Tâm bối rối giữa Hoàng và Minh.

```text
Condition:
tam_minh_drawn >= 1

Choices:
A. Giữ khoảng cách với Minh vì đang nghĩ cho Hoàng
+2 trust_tam_hoang
-1 tam_minh_drawn
set tam_direction: tam_hoang_open

B. Chủ động hỏi Minh về công việc
+1 career_tam
+1 trust_tam_minh
unlock: tam_minh_professional_bond

C. Theo đuổi cảm giác với Minh rõ hơn
+2 tam_minh_drawn
+1 distance_tam_hoang
set tam_direction: tam_minh_drawn
```

### Minh POV — Observation Route

Người chơi thấy Minh đọc Tâm, Hoàng, Huyền, Quân. Minh không dễ rung động, nhưng Tâm gợi cho anh một cảm giác khó gọi tên: vừa quen, vừa không nên chạm vào.

Minh là kiểu yêu bằng quan sát và trách nhiệm; anh thường giữ lại cảm xúc, nghĩ bằng hệ quả và khoảng cách an toàn. 

```text
Choices:
A. Giữ ranh giới công việc
+1 minh_boundary_high
+1 trust_professional

B. Giúp Tâm xử lý một lỗi nhỏ
+1 trust_tam_minh
+1 tam_minh_drawn

C. Cảnh báo Hoàng nhẹ nhàng
+1 trust_minh_hoang
+1 hoang_insecurity_active
```

## Exclusion

`tam_c07_pov` và `minh_m01_pov` nên mutually exclusive trong một playthrough.

## Unlock

* `yuuka_c08_festival_arrival`
* `work_c10_project_festival_overlap` seed
* `fb_minyuu_01_first_frame` soft-hidden

---

# CHAPTER 8 (yuuka_c08_festival_arrival) — Sự xuất hiện của Yuuka

## POV

Tâm hoặc Minh, tùy route focus.

## Nội dung

Yuuka đến Việt Nam tham dự Liên hoan phim Châu Á - Thái Bình Dương. Cô không đến như cô gái năm xưa, mà là một đạo diễn/người làm phim đã có tên tuổi.

Minh biết trước qua Ayumi rằng Yuuka sẽ tham dự festival. Nhưng biết trước không làm anh sẵn sàng hơn.

Buổi sáng trước ngày gặp lại, Minh vô thức mua nguyên liệu để nấu những món Yuuka thích. Anh tự nhận ra rồi hơi khó chịu với chính mình. Rất “vợ chồng già giận nhau lâu ngày”: nghĩ đến thì bực, nhưng tay vẫn tự nhớ đường đến quầy nguyên liệu.

Yuuka xuất hiện ở sân bay/festival/hotel. Tùy route, người đầu tiên thấy cô có thể là Minh, Tâm, Hoàng hoặc Huyền.

## Core Emotional Function

* Unlock Yuuka route.
* Đưa “quá khứ chưa đóng” vào hiện tại.
* Làm Tâm thấy: cảm giác của mình với Minh có thể không phải thứ duy nhất đang tồn tại.
* Làm Hoàng hiểu anh trai mình có một vết cũ rất sâu.
* Làm Huyền nhận ra đây không còn là gossip vui nữa.

## Branches

### Canon

Tâm đang hẹn hò Hoàng. Yuuka xuất hiện. Tâm thấy Yuuka đẹp, trẻ, khí chất quá khác. Sau đó nhận ra giữa Yuuka và Minh có một dòng điện ngầm rất rõ.

```text
Effects:
+2 minh_yuuka_tension
+1 tam_insecurity
+1 hoang_protective_tam
unlock: yuuka_y01
unlock: minh_yuuka_flashback_01
```

### Tâm-Minh Lean

Nếu Tâm đã nghiêng về Minh, Yuuka xuất hiện như một cú đánh thẳng vào ảo tưởng còn non của Tâm.

```text
Effects:
+2 tam_minh_conflict
+2 tam_self_compare
unlock: tam_step_back_choice
unlock: yuuka_rival_not_rival_scene
```

### Hoàng-Huyền Route

Yuuka xuất hiện chủ yếu tác động vào Minh/Hoàng. Huyền quan sát Yuuka và thấy “người này không đơn giản”. Tâm có thể đứng ngoài, trở thành người nhận ra câu chuyện sâu hơn.

```text
Effects:
+1 huyen_insight
+1 tam_observer_role
unlock: huyen_question_minh
```

### Friend Group Route

Yuuka xuất hiện khiến cả nhóm bị kéo vào quá khứ của Minh. Không ai có quyền hỏi, nhưng ai cũng thấy.

```text
Effects:
+1 group_tension
unlock: group_dinner_yuuka
```

## Unlock

* `yuuka_c08_festival_arrival` (chương này)
* `fb_minyuu_01_first_frame`
* `yuuka_c09_yuukas_work`

---

# CHAPTER 9 (yuuka_c09_yuukas_work) — Buổi chiếu phim

## POV

Yuuka.

## Nội dung

Yuuka tham dự buổi chiếu phim của mình. Cô đứng trước đám đông với tư cách đạo diễn, trả lời phỏng vấn, nói về tác phẩm, ánh sáng, ký ức, lựa chọn và cái giá của trưởng thành.

Nhưng khi nhìn thấy Minh dưới hàng ghế khách mời, nhịp của cô lệch đi một chút.

Không ai ngoài Minh nhận ra. Hoặc Tâm nhận ra nếu `tam_insight >= 2`.

Sau buổi chiếu, có reception. Minh và Yuuka buộc phải nói chuyện xã giao.

## Choices

```text
Yuuka:
A. Giữ vẻ chuyên nghiệp
+1 career_yuuka
+1 minh_yuuka_guarded

B. Đùa nhẹ với Minh như ngày cũ
+1 intimacy_minh_yuuka
+1 pain_minh_yuuka

C. Hỏi thẳng anh có xem phim không
+1 yuuka_honest_pursuit
unlock: minh_answer_about_film

Minh:
A. Khen phim bằng nhận xét kỹ thuật
+1 yuuka_respect
+1 distance_minh_yuuka

B. Nhắc một chi tiết nhỏ trong phim
+2 intimacy_minh_yuuka
-1 distance_minh_yuuka

C. Chỉ nói “Chúc mừng”
+1 minh_boundary_high
+1 yuuka_hurt
```

## Route Impact

* Nếu Minh nhận xét đúng một chi tiết nhỏ, Yuuka biết anh vẫn nhìn cô như trước.
* Nếu Minh quá lạnh, Yuuka route chuyển sang `yuuka_avoidance` hoặc `yuuka_late_reunion`.
* Nếu Tâm chứng kiến và chọn lùi, route Tâm-Hoàng được cứu.
* Nếu Tâm chọn cạnh tranh, mở nhánh Tâm-Minh nhưng tăng risk.

## Unlock

* `fb_minyuu_02_working_rhythm`
* `work_c10_project_festival_overlap`
* `tam_c20a_tam_minh_possible` seed

---

# CHAPTER 10 (work_c10_project_festival_overlap) — Dự án bắt đầu lệch nhịp

## POV

Tâm/Huyền.

## Nội dung

Công ty bắt đầu vào giai đoạn căng của dự án. Minh làm cố vấn, Quân quản lý trực tiếp, Hoàng liên quan phần thiết kế/hình ảnh/không gian, Tâm và Huyền nằm trong team triển khai.

Đây là chương công việc để tránh game chỉ xoay quanh yêu đương. Yêu đương mà không có đời sống thì như món ăn chỉ có nước sốt. Ngon hai thìa đầu, sau đó hơi mệt.

Quân thể hiện rõ năng lực và sự khó tính. Huyền ban đầu khó chịu với anh, nhưng dần thấy anh không bắt bẻ vô lý.

## Branches

### Tâm Career

```text
Condition:
tam_project_management_skill unlocked

Choice:
Tâm đứng ra xử lý một điểm nghẽn trong dự án.

Effects:
+2 career_tam
+1 minh_respect_tam
+1 quan_respect_tam
unlock: tam_promotion_path
```

### Huyền — Quân Seed

```text
Condition:
Huyền chọn đối thoại trực tiếp thay vì than phiền

Effects:
+2 trust_huyen_quan
set huyen_direction: huyen_quan_interest
unlock: huyen_quan_side_01
```

### Huyền — Hoàng Seed

```text
Condition:
hoang_huyen_open active

Effects:
Hoàng giúp Huyền giải tỏa sau giờ làm.
+1 intimacy_hoang_huyen
-1 huyen_quan_interest
```

### Tâm — Minh Risk

```text
Condition:
tam_minh_drawn >= 2

Effects:
Minh giúp Tâm một lỗi công việc nhỏ.
+1 trust_tam_minh
+1 distance_tam_hoang
unlock: tam_minh_private_scene
```

## Unlock

* `group_c11_social_dinner`
* `work_c16_project_crisis` seed
* `huyen_c22_quan_or_hoang` seed

---

# CHAPTER 11 (group_c11_social_dinner) — Bữa tối có thêm người cũ

## POV

Hoàng hoặc Tâm.

## Nội dung

Một bữa tối tại nhà Minh/Hoàng. Tùy nhánh, thành phần có thể khác:

* Canon: Minh, Yuuka, Hoàng, Tâm; Huyền có thể đến sau hoặc là người kéo Tâm tới.
* Huyền route: Minh, Yuuka, Hoàng, Huyền, rồi Tâm.
* Friend route: cả nhóm.

Yuuka ở trong không gian của Minh. Cô biết căn bếp, biết vài thói quen của anh. Không cần nói, nhưng người khác nhìn thấy.

Tâm nhận ra mình đang nhìn vào một dạng quan hệ đã có lịch sử quá sâu. Hoàng cũng nhận ra. Anh không biết hết, nhưng đủ hiểu Minh từng có một người quan trọng.

## Key Scene Options

```text
A. Tâm giúp Hoàng trong bếp
+2 trust_tam_hoang
-1 tam_minh_drawn

B. Tâm hỏi Yuuka về phim
+1 trust_tam_yuuka
+1 tam_maturity
unlock: tam_yuuka_private_talk

C. Huyền kéo không khí nhẹ lại
+1 group_trust
+1 huyen_social_skill

D. Minh vô thức nấu món Yuuka thích
+2 minh_yuuka_tension
+1 group_notices_past
```

## Canon Result

Tâm và Hoàng có trục trặc âm, nhưng chưa vỡ. Minh và Yuuka bị kéo lại gần một chút dù cả hai đều cố tỏ ra bình thường.

## Unlock

* `fb_minyuu_03_door_left_open`
* `work_c16_project_crisis`
* `hoang_h05_shadow_of_minh`

---

# CHAPTER 12 (fb_minyuu_01_03) — Flashback: Lần đầu sống chung

## POV

Yuuka.

## Nội dung

Flashback về thời Yuuka và Minh từng sống chung ở nước ngoài/sau biến cố ký túc xá. Yuuka gặp khó khăn tài chính/chỗ ở, Minh đề nghị cô về ở cùng. Ban đầu là giúp đỡ, sau đó là một cấu trúc thân mật rất nguy hiểm.

Yuuka nhận ra Minh chăm sóc bằng hệ thống: phòng đã dọn, đồ cần dùng đã chuẩn bị, auto-save, backup, thuốc, đồ ăn, thói quen nhỏ. Không tỏ tình, nhưng mọi thứ trong nhà dần có dấu tay của nhau.

## Choices Affect Present

```text
Choice A: Yuuka nhận giúp đỡ nhưng đặt quy tắc rõ
+1 yuuka_independence
+1 trust_minh_yuuka
unlock present choice: yuuka_respect_boundary

Choice B: Yuuka dựa vào Minh nhiều hơn
+2 intimacy_minh_yuuka
+1 yuuka_dependency
unlock present risk: yuuka_fear_repeating_past

Choice C: Yuuka trêu Minh để phá băng
+1 intimacy_minh_yuuka
+1 yuuka_playful_pursuit

Choice D: Minh giữ khoảng cách quá kỹ
+1 minh_boundary_high
+1 yuuka_loneliness
```

## Unlock

* `fb_minyuu_05b_separation` (từ nhánh 04b)
* `yuuka_c09_yuukas_work`
* `work_c10_project_festival_overlap`

---

# CHAPTER 13 (tam_c20a_tam_minh_possible) — Tâm chọn đứng ở đâu (late-game)

## POV

Tâm.

## Nội dung

Sau khi chứng kiến Minh và Yuuka, Tâm phải định vị cảm xúc của mình. Đây là chương quan trọng để tránh biến Tâm thành “nữ phụ bị cuốn theo trai đẹp”. Không được. Tâm phải có lòng tự trọng và độ thật riêng.

## Choices

### A. Nói chuyện thẳng với Hoàng

Tâm nói rằng cô đã từng có một cảm giác kỳ lạ với Minh, nhưng không muốn dùng im lặng làm tổn thương Hoàng.

```text
Effects:
+3 trust_tam_hoang
-1 hoang_insecurity_active
set tam_direction: tam_hoang_open
lock out: tam_minh_romance unless later breakup branch
```

### B. Lùi khỏi Hoàng để suy nghĩ

Tâm không muốn tiếp tục khi lòng chưa yên.

```text
Effects:
+1 tam_maturity
+2 distance_tam_hoang
set tam_direction: tam_uncertain
unlock: tam_minh_possible
unlock: hoang_huyen_possible
```

### C. Theo cảm giác với Minh

Tâm chủ động tiếp cận Minh nhiều hơn qua công việc.

```text
Effects:
+2 tam_minh_drawn
+2 distance_tam_hoang
+1 hoang_hurt
set tam_direction: tam_minh_drawn
unlock: tam_minh_route_01
```

### D. Đẩy Huyền về phía Hoàng

Chỉ nên khả dụng nếu Tâm chưa hẹn hò Hoàng hoặc đã lùi rõ ràng.

```text
Effects:
+2 huyen_hoang_interest
+1 tam_support_huyen
set hoang_direction: hoang_huyen_open
```

## Unlock

* `tam_c20b_admiration_vs_love`
* `thienan_c21a_minh_possible` seed

---

# CHAPTER 14 (thienan_c21a_b) — Thiên An, Minh, và Quang (late-game)

## POV

Thiên An.

## Nội dung

Thiên An route mở. Quang xuất hiện rõ hơn: trợ lý của Thiên An, thiếu gia tập đoàn lớn nhưng từ chối thừa kế sản nghiệp, kiên trì theo đuổi Thiên An suốt 6 năm.

Quang không nên viết như “nam phụ simp”. Không. Anh phải có phẩm chất riêng: bền, biết giữ khoảng cách, làm tốt công việc, không dùng gia thế ép cô. Cái đẹp của Quang là anh ở lại đủ lâu nhưng không biến việc ở lại thành cái còng.

Thiên An bị gia đình giục kết hôn/sắp xếp đối tượng. Cô mệt nhưng không vỡ.

## Branches

### Quang Route

```text
Choice A: Thiên An cho phép Quang bước gần hơn nửa bước
+2 trust_thienan_quang
+1 intimacy_thienan_quang
set thienan_direction: thienan_quang_open
```

### Minh Residue

```text
Condition:
player unlocked thienan_old_story_hint

Choice B: Thiên An nhớ lại Minh
+2 thienan_minh_residue
unlock: thienan_minh_flashback
```

### Family Arrangement

```text
Choice C: Thiên An chấp nhận đi xem mắt để yên chuyện
+2 family_pressure_thienan
set thienan_direction: thienan_family_arranged
unlock: arranged_marriage_path
```

### Single Path

```text
Choice D: Thiên An từ chối cả gia đình lẫn Quang
+1 thienan_single
+1 career_thienan
```

## Unlock

* `thienan_c21a_minh_possible`
* `thienan_c21b_choose_own_path`

---

# CHAPTER 15 (fb_minyuu_04_05) — Flashback: Điểm gãy của Minh và Yuuka

## POV

Minh hoặc Yuuka, mutually exclusive.

## Nội dung

Flashback về biến cố chia xa. Đây không nên chỉ là “Yuuka bỏ chạy”. Phải cho người chơi thấy cả hai đều có lý do, nhưng cách họ chọn làm tổn thương nhau.

Minh sợ sự dịu dàng của mình làm Yuuka yếu đi. Yuuka sợ nếu trả lời, cô sẽ mất cả tình yêu lẫn bản thân. Một người lùi vì trách nhiệm. Một người chạy vì sợ. Tuyệt vời. Rất trưởng thành theo kiểu làm khổ nhau có học thức.

## Choices

### Minh POV

```text
A. Nói thẳng rằng cả hai cần dừng lại
+2 minh_boundary_high
+2 yuuka_hurt
set past_break: minh_cut_clean

B. Hỏi Yuuka muốn gì thật sự
+1 minh_vulnerability
unlock present: minh_can_ask_directly

C. Im lặng gánh quyết định
+2 avoidance_minh
+1 unresolved_past
```

### Yuuka POV

```text
A. Ở lại đối thoại
+2 yuuka_courage
unlock present: yuuka_confess_without_running

B. Bỏ chạy
+2 yuuka_avoidance
+2 unresolved_past
canon compatible

C. Nói rằng cô cần thời gian
+1 yuuka_independence
+1 minh_waiting_pain
unlock: late_reunion_path
```

## Present Impact

* Nếu quá khứ chọn “đối thoại”, hiện tại mở lựa chọn tái hợp sớm.
* Nếu quá khứ chọn “bỏ chạy”, hiện tại cần nhiều chương repair hơn.
* Nếu quá khứ chọn “cần thời gian”, mở ending “Minh và Yuuka đến với nhau rất lâu sau đó, không kết hôn”.

## Unlock

* `yuuka_c18a_career_interlude`
* `yuuka_c18b_habit_of_you`
* `yuuka_c18c_long_distance_interlude`

---

# CHAPTER 16 (work_c16_project_crisis) — Khủng hoảng dự án

## POV

Tâm/Huyền/Minh tùy route.

## Nội dung

Dự án công ty gặp lỗi lớn. Deadline, khách hàng, truyền thông nội bộ, trách nhiệm đội nhóm — tất cả dồn lại. Đây là chương kiểm tra năng lực chứ không chỉ cảm xúc.

Quân gây áp lực mạnh. Minh nhìn ra gốc vấn đề. Tâm có cơ hội thể hiện kỹ năng quản lý nếu đã học từ Thiên An. Huyền có cơ hội đối đầu Quân một cách trưởng thành.

## Outcomes

### Tâm Career Win

```text
Condition:
career_tam >= threshold
tam_project_management_skill unlocked

Effects:
+3 career_tam
+1 minh_respect_tam
+1 quan_respect_tam
unlock: tam_promotion_ending_support
```

### Huyền — Quân Bond

```text
Condition:
huyen_quan_interest >= 1

Effects:
Quân bảo vệ Huyền trước một lỗi không hoàn toàn do cô.
+2 trust_huyen_quan
unlock: huyen_quan_after_work
```

### Minh — Tâm Bond

```text
Condition:
tam_minh_drawn >= 2 AND Tâm not locked with Hoàng

Effects:
+2 trust_tam_minh
unlock: tam_minh_late_night_work
```

### Failure

```text
Condition:
wrong choices / low career

Effects:
+1 stress_all
-1 career_tam
-1 trust_quan_team
unlock: repair_project_extra
```

## Unlock

* `hoang_h05_shadow_of_minh`
* `yuuka_c18` branches unlock

---

# CHAPTER 17 (hoang_h05_shadow_of_minh) — Hoàng dưới cái bóng của Minh

## POV

Hoàng.

## Nội dung

Hoàng phải đối diện cảm giác mình lại bị đặt cạnh Minh. Nếu Tâm nghiêng về Minh, vết này đau rõ. Nếu Hoàng-Huyền route, nó nhẹ hơn nhưng vẫn còn: Hoàng nhận ra nhiều người xung quanh mình đều bị Minh ảnh hưởng.

Hoàng không ghét Minh. Anh thương anh trai, kính trọng anh, nhưng vẫn có khoảnh khắc khó chịu vì cái bóng ấy quá lớn.

## Branches

### Canon Repair: Hoàng & Tâm

```text
Condition:
tam_hoang_open active
trust_tam_hoang >= threshold

Hoàng nói thật một phần nỗi bất an.
Tâm không phủ nhận, cũng không dỗ ngọt rẻ tiền.
Cô ở lại.

Effects:
+3 trust_tam_hoang
set hoang_jealousy_resolved
unlock: tam_hoang_stable_path
```

### Break Path

```text
Condition:
distance_tam_hoang high

Hoàng chủ động lùi.
Không trách Tâm, nhưng không thể giả vờ.

Effects:
set tam_hoang_break
unlock: tam_minh_route_02
unlock: hoang_huyen_late_path
```

### Hoàng-Huyền Path

Huyền không an ủi kiểu mềm. Cô chọc Hoàng một câu hơi đau nhưng đúng. Hoàng bật cười, rồi đỡ hơn.

```text
Effects:
+2 trust_hoang_huyen
+1 intimacy_hoang_huyen
set hoang_direction: hoang_huyen_open
```

### Friend Path

Hoàng học cách không cần thắng Minh để có giá trị riêng.

```text
Effects:
+1 hoang_self_acceptance
unlock: hoang_independent_ending_support
```

## Unlock

* `yuuka_c18a_career_interlude` / `yuuka_c18b_habit_of_you` / `yuuka_c18c_long_distance_interlude`

---

# CHAPTER 18 (yuuka_c18a_b_c) — Yuuka: The Habit of You (3 branches)

## POV

Yuuka.

## Nội dung

Một flashback/montage playable về những năm Yuuka xa Minh. Có thể không cần làm đủ 21 chương như tiểu thuyết, nhưng nên chia thành các node lớn. Tuyến chia xa vốn đã có khung rõ: Yuuka trở về Nhật, cố sống bình thường, nhận ra Minh đã ngấm vào cách cô nghĩ và làm việc; càng trưởng thành càng thấy cái bóng anh lớn hơn; cuối cùng ngừng chạy và quay lại. 

## Playable Sections

### Section A — Tokyo

Yuuka ở cùng Akiko và Tetsuya, thấy sự chăm sóc đời thường của họ và nhớ Minh.

```text
Choice:
- Né tránh → +1 yuuka_avoidance
- Thừa nhận với Akiko rằng mình nhớ Minh → +1 yuuka_honesty
```

### Section B — Công việc đầu tiên

Yuuka xử lý công việc theo cách rất “Minh”: gọn, tỉnh, logic.

```text
Choice:
- Xem đó là trưởng thành của riêng mình → +1 yuuka_independence
- Nhận ra dấu Minh trong mình → +1 yuuka_accepts_love
```

### Section C — Ayumi

Ayumi xuất hiện, feedback sắc. Yuuka bị kéo lên một mặt bằng chuyên nghiệp cao hơn.

```text
Choice:
- Tự ái → +1 yuuka_pride
- Học từ Ayumi → +2 career_yuuka
```

### Section D — Điểm đáy

Yuuka kiệt sức, cô đơn, nhưng không còn muốn chạy khỏi tình yêu này.

```text
Choice:
- Cắt Minh ra khỏi đời mình → set yuuka_single_possible
- Biến nỗi nhớ thành kỷ luật → set yuuka_return_standing
```

## Unlock

* `c19a_city_after_festival_old_friends`
* `c19b_city_after_festival_ex_lovers`
* `c19c_city_after_festival_still_lovers`

---

# CHAPTER 19 (c19a_b_c) — Thành phố sau festival (3 branches)

## POV

Minh/Yuuka.

## Nội dung

Sau festival, Yuuka và Minh có một khoảng đi cùng nhau trong thành phố. Không cần hôn. Không cần ôm. Chỉ cần đủ nguy hiểm.

Họ nói về phim, về Việt Nam, về những năm đã qua. Nhưng câu thật nằm dưới câu khác.

Yuuka có thể hỏi:

> “Anh vẫn giữ thói quen uống cà phê không đường à?”

Bề mặt là cà phê. Thực chất là: **anh có còn là người em từng biết không?**

Minh có thể đáp:

> “Có vài thứ đổi rồi. Vài thứ thì không.”

Bề mặt là thói quen. Thực chất là: **anh vẫn còn yêu em, nhưng đừng bắt anh nói ngay.**

## Branches

### Reopen

```text
Condition:
yuuka_return_standing active
distance_minh_yuuka <= threshold
past unresolved not too high

Effects:
set minh_direction: minh_yuuka_reopen
+2 intimacy_minh_yuuka
unlock: minh_yuuka_finale_path
```

### Guarded

```text
Condition:
minh_boundary_high OR yuuka_avoidance

Effects:
set minh_yuuka_guarded
unlock: late_reunion_path
```

### Break Again

```text
Condition:
wrong choices + high avoidance

Effects:
set yuuka_single_possible
set minh_solitude_possible
```

## Unlock

* `tam_c20b_admiration_vs_love`
* `thienan_c21a_minh_possible`
* `thienan_c21b_choose_own_path`

---

# CHAPTER 20 (tam_c20b_admiration_vs_love) — Tâm và Minh: Có phải tình yêu không?

## POV

Tâm/Minh.

## Condition

Chỉ mở nếu:

```text
tam_minh_drawn high
tam_hoang_break active OR tam_hoang_never_started
minh_yuuka_reopen NOT active
```

## Nội dung

Tâm và Minh có một chương riêng để kiểm tra bản chất cảm xúc.

Đây là tuyến nguy hiểm. Nếu viết không khéo sẽ biến Tâm thành người thay thế Yuuka, Minh thành người đàn ông “ai cũng được miễn là chữa lành”. Không ổn. Rất không ổn. Cần cho họ đối diện thẳng:

* Tâm bị Minh hút vì anh sâu, an toàn, khó đọc.
* Minh quý Tâm vì cô ấm, thật, có độ bình yên.
* Nhưng giữa họ có thật sự là tình yêu, hay là hai người đang đi tìm thứ mình thiếu?

## Choices

```text
A. Tâm hỏi thẳng Minh có đang nhìn cô như chính cô không
+2 tam_maturity
if minh_yuuka_closed:
    unlock tam_minh_possible_ending
else:
    Minh lùi lại, +1 bittersweet

B. Tâm nhận ra mình từng bị ấn tượng, không phải yêu
set tam_self_clarity
unlock tam_independent_or_hoang_repair

C. Minh bước tới
Condition: minh_yuuka_reopen false, trust_tam_minh high, tam_hoang free
set minh_tam_open
unlock tam_minh_ending_path
```

## Ending Support

* Tâm-Minh possible ending.
* Tâm độc lập/career ending.
* Tâm-Hoàng repair if Hoàng still open.

---

# CHAPTER 21 (thienan_c21a_minh_possible + thienan_c21b_choose_own_path) — Thiên An: hai con đường

## POV

Thiên An.

## Condition

Mở nếu:

```text
thienan_minh_residue >= threshold
Minh not locked with Yuuka/Tâm
```

## Nội dung

Thiên An gặp lại Minh trong một bối cảnh công việc/gia đình. Hai người từng có quá khứ, nhưng không cần biến thành melodrama.

Thiên An không phải tình địch rẻ tiền của Yuuka. Cô là bằng chứng rằng có những người rất tốt, rất xứng đáng, nhưng tình yêu vẫn không chọn họ.

Nếu Minh đang mở với Yuuka, Thiên An nhận ra và lùi. Nếu Minh đã đóng Yuuka và Tâm, cô có thể có một nhánh chậm với anh — nhưng rất khó, rất nhiều tự trọng, rất nhiều điều không nói.

## Branches

### Thiên An — Quang Canon

```text
Condition:
trust_thienan_quang high

Thiên An nhìn Minh, khựng một nhịp, rồi quay về phía Quang.
Không phải vì Quang thắng Minh.
Mà vì cô cuối cùng chọn người đã ở lại trong đời thật của mình.

Effects:
set thienan_quang_open
lock thienan_minh
```

### Thiên An — Minh Possible

```text
Condition:
minh_yuuka_closed
tam_minh_closed
thienan_minh_residue high
thienan_quang_open false

Effects:
unlock thienan_minh_late_path
```

### Thiên An Single

```text
Choice:
Thiên An không chọn ai, cũng không để gia đình chọn hộ.

Effects:
set thienan_single
+2 career_thienan
```

### Arranged Marriage

```text
Condition:
family_pressure_thienan high
trust_thienan_quang low
thienan_self_assertion low

Effects:
set thienan_family_arranged
unlock arranged_marriage_ending
```

---

# CHAPTER 22 (huyen_c22_quan_or_hoang) — Huyền và Quân

## POV

Huyền.

## Nội dung

Huyền route rõ hơn. Quân không còn chỉ là trưởng phòng khó tính. Anh có nguyên tắc, có tiêu chuẩn, và càng quan sát càng thấy anh không lạnh vô lý.

Huyền có thể bị hấp dẫn bởi một người khiến cô phải nghiêm túc hơn. Quân bị hấp dẫn bởi một người dám cãi nhưng không cãi ngu. Ừ, nghe khô nhưng hợp. Rất hợp.

## Branches

### Canon Huyền — Quân

```text
Condition:
trust_huyen_quan >= threshold
huyen_hoang_interest low or resolved

Effects:
set huyen_direction: huyen_quan_interest
unlock huyen_quan_finale
```

### Hoàng — Huyền

```text
Condition:
hoang_huyen_open active
trust_hoang_huyen high

Effects:
set hoang_huyen_finale
lock huyen_quan
```

### Huyền Independent

```text
Condition:
career_huyen high
no romance lock

Effects:
set huyen_independent
```

## Unlock

* `minyuu_c23a_old_friends_resolution`
* `minyuu_c23b_ex_lovers_resolution`
* `minyuu_c23c_still_lovers_resolution`

---

# CHAPTER 23 (minyuu_c23a_b_c) — Minyuu: Không chạy nữa (3 branches)

## POV

Yuuka/Minh.

## Condition

Mở nếu:

```text
yuuka_return_standing active
minh_yuuka_reopen active
trust_minh_yuuka high
distance_minh_yuuka low
```

## Nội dung

Đây là chương tái hợp chính. Không nên cho họ giải thích hết bằng lời. Cần có một cảnh đời thường: Minh nấu ăn, Yuuka giúp dọn, một cái bát đặt sai chỗ, một món cô thích được mua sẵn.

Yuuka nhận ra anh vẫn nhớ.

Minh nhận ra cô không còn là cô gái chỉ biết bám vào anh để đứng vững. Cô đã có đời mình, nghề mình, trục sống của mình. Đây là điều làm Minh dám mở cửa lại.

## Choices

```text
A. Yuuka nói thẳng: “Em không quay lại để được anh cứu.”
+2 yuuka_return_standing
+2 minh_trust_yuuka

B. Minh thừa nhận anh vẫn sợ làm cô yếu đi
+2 intimacy_minh_yuuka
-1 avoidance_minh

C. Hai người chọn ở cạnh nhau nhưng không vội kết hôn
unlock: late_non_marriage_reunion_ending

D. Hai người chính thức quay lại
unlock: canon_reunion_ending
```

## Notes

Canon có thể là Minh-Yuuka quay lại sâu sắc. Nhưng một possible ending rất đẹp là:

> Minh và Yuuka đến với nhau rất lâu sau đó, không kết hôn.

Ending này hợp nếu quá khứ chọn “cần thời gian”, hiện tại chọn “không ép danh phận”, và cả hai đặt sự tự do/trưởng thành lên trước hình thức.

---

# CHAPTER 24 (final_c24_last_choices) — Những lựa chọn cuối cùng

## POV

Multi-route.

## Nội dung

Chương gom các route trước finale. Mỗi nhân vật có một lựa chọn cuối:

## Tâm

```text
- Chọn Hoàng
- Chọn Minh
- Chọn bản thân/career
- Làm lành với chính cảm giác từng lệch nhịp
```

## Hoàng

```text
- Chọn Tâm
- Chọn Huyền
- Chọn độc thân trưởng thành hơn
- Hòa giải với cái bóng của Minh
```

## Minh

```text
- Chọn Yuuka
- Chọn Tâm
- Chọn Thiên An
- Chọn độc thân
- Chọn muộn với Yuuka, không ràng buộc hôn nhân
```

## Yuuka

```text
- Ở lại với Minh
- Rời đi nhưng không chạy
- Chọn sự nghiệp và độc thân
- Hẹn một ngày khác, khi cả hai đủ yên
```

## Huyền

```text
- Chọn Quân
- Chọn Hoàng
- Chọn độc lập
```

## Thiên An

```text
- Chọn Quang
- Chọn Minh
- Chọn độc thân
- Chấp nhận hôn nhân sắp xếp
```

---

# CHAPTER 25 — Finale / Ending Resolution

## Ending Priority

Ending nên resolve theo thứ tự ưu tiên để tránh conflict:

```text
1. Doom Ending
2. Canon True Ending
3. Major Alternative Pair Endings
4. Late Reunion Endings
5. Single/Independent Endings
6. Arranged Marriage Ending
7. Open Ending
```

---

# IV. Ending Rules

The game has 24 endings (e01-e24), each with a `can_get_*` condition helper defined in `game/ending_rules.rpy`. Ending resolution is handled by `resolve_story_ending()` in the same file.

## Ending Priority (resolve order)

```text
1. e24_doom                    — Doom ending (doom_score >= 8)
2. e01_canon_true              — Canon true ending (all 4 pairs)
3. e13_minyuu_public_lovers    — Minyuu public lovers (still_lovers branch)
4. e14_minyuu_non_marriage      — Minyuu non-marriage (still_lovers)
5. e15_minyuu_long_distance     — Minyuu long-distance (still_lovers)
6. e12_minyuu_private_lovers    — Minyuu private lovers (still_lovers fallback)
7. e10_minyuu_reunion           — Minyuu reunion (ex_lovers branch)
8. e11_minyuu_late_reunion      — Minyuu late reunion (ex_lovers)
9. e18_minyuu_mutual_single     — Minyuu mutual single (ex_lovers)
10. e03_tam_minh                — Tâm-Minh (old_close_friends branch)
11. e07_thienan_minh            — Thiên An-Minh (old_close_friends)
12. e20_minyuu_friendship       — Minyuu friendship (old_close_friends)
13. e02_tam_hoang               — Tâm-Hoàng
14. e04_hoang_huyen             — Hoàng-Huyền
15. e05_huyen_quan              — Huyền-Quân
16. e06_thienan_quang           — Thiên An-Quang
17. e19_yuuka_career            — Yuuka career
18. e21_tam_independent         — Tâm independent
19. e22_huyen_independent       — Huyền independent
20. e23_hoang_single_growth     — Hoàng single growth
21. e08_thienan_single          — Thiên An single
22. e09_thienan_arranged        — Thiên An arranged marriage
23. e16_minh_single             — Minh single
24. e17_yuuka_single            — Yuuka single
```

## Key State Variables for Ending Conditions

```text
minh_yuuka_relation:  # Determines which Minyuu ending branch to use
  - "old_close_friends"        # Stayed friends after separation
  - "ex_lovers_long_separated" # Separated as ex-lovers, long time apart
  - "still_lovers"             # Never stopped loving each other

doom_score:  # Accumulated through poor choices
  - doom_score >= 5: can_get_canon_true becomes false
  - doom_score >= 8: forced doom ending

minh_romance_lock:  # When True, Minh cannot romance Tâm or Thiên An
yuuka_romance_lock: # When True, Yuuka cannot romance others

ending_support:  # List of ending IDs that the current playthrough supports
  # Set by late-game choices; checked via story_has_ending_support()
```

## 1. e01_canon_true — Canon True Ending

```text
Pairs: Tâm-Hoàng, Yuuka-Minh, Huyền-Quân, Thiên An-Quang

Required:
  hoang_tam_trust >= 5
  minh_yuuka_relation in ["ex_lovers_long_separated", "still_lovers"]
  minh_yuuka_trust >= 5
  huyen_quan_trust >= 4
  thienan_quang_trust >= 4
  doom_score < 5
  story_has_ending_support("e01_canon_true")
```

## 2. e02_tam_hoang — Tâm-Hoàng Ending

```text
Required:
  hoang_tam_trust >= 5
  NOT direction "tam_minh_commit"
  hoang_insecurity < 6
  story_has_ending_support("e02_tam_hoang")
```

## 3. e03_tam_minh — Tâm-Minh Ending

```text
Required:
  minh_yuuka_relation == "old_close_friends"
  NOT minh_romance_lock
  tam_minh_drawn >= 4
  direction "tam_minh_commit"
  story_has_ending_support("e03_tam_minh")
```

## 4. e04_hoang_huyen — Hoàng-Huyền Ending

```text
Required:
  hoang_huyen_interest >= 4
  huyen_hoang_interest >= 4
  NOT direction "tam_hoang_commit"
  story_has_ending_support("e04_hoang_huyen")
```

## 5. e05_huyen_quan — Huyền-Quân Ending

```text
Required:
  huyen_quan_trust >= 4
  NOT direction "huyen_hoang_commit"
  story_has_ending_support("e05_huyen_quan")
```

## 6. e06_thienan_quang — Thiên An-Quang Ending

```text
Required:
  thienan_quang_trust >= 4
  family_pressure_thienan < 6
  story_has_ending_support("e06_thienan_quang")
```

## 7. e07_thienan_minh — Thiên An-Minh Ending

```text
Required:
  minh_yuuka_relation == "old_close_friends"
  NOT minh_romance_lock
  thienan_minh_residue >= 4
  direction "thienan_minh_commit"
  story_has_ending_support("e07_thienan_minh")
```

## 8. e08_thienan_single — Thiên An Single

```text
Required:
  thienan_self_assertion >= 4
  story_has_ending_support("e08_thienan_single")
```

## 9. e09_thienan_arranged — Thiên An Arranged Marriage

```text
Required:
  family_pressure_thienan >= 5
  story_has_ending_support("e09_thienan_arranged")
```

## 10-15. Minyuu Endings (route-dependent)

Resolved by `resolve_ex_lovers_ending()` or `resolve_still_lovers_ending()` based on `minh_yuuka_relation`:

### Still Lovers Branch:
- e12_minyuu_private_lovers   — Private lovers (fallback)
- e13_minyuu_public_lovers    — Public lovers
- e14_minyuu_non_marriage     — Non-marriage commitment
- e15_minyuu_long_distance    — Long-distance relationship

### Ex-Lovers Branch:
- e10_minyuu_reunion          — Full reunion (trust >= 5)
- e11_minyuu_late_reunion     — Late reunion (trust >= 3)
- e18_minyuu_mutual_single    — Both single, may or may not reunite

### Old Close Friends Branch:
- e20_minyuu_friendship       — Minyuu maintain friendship

## 16. e16_minh_single — Minh Single

```text
Required:
  minh_yuuka_relation in ["old_close_friends", "ex_lovers_long_separated"]
  story_has_ending_support("e16_minh_single")
```

## 17. e17_yuuka_single — Yuuka Single

```text
Required:
  (complex conditions — see ending_rules.rpy)
  story_has_ending_support("e17_yuuka_single")
```

## 18. e18_minyuu_mutual_single — Minyuu Mutual Single (see above)

## 19. e19_yuuka_career — Yuuka Career Ending

```text
Required:
  career_yuuka >= 4
  story_has_ending_support("e19_yuuka_career")
```

## 20. e20_minyuu_friendship — Minyuu Friendship (see above)

## 21. e21_tam_independent — Tâm Independent

```text
Required:
  tam_self_clarity >= 4
  story_has_ending_support("e21_tam_independent")
```

## 22. e22_huyen_independent — Huyền Independent

```text
Required:
  career_huyen >= 3
  story_has_ending_support("e22_huyen_independent")
```

## 23. e23_hoang_single_growth — Hoàng Single Growth

```text
Required:
  hoang_self_acceptance >= 4
  story_has_ending_support("e23_hoang_single_growth")
```

## 24. e24_doom — Doom Ending

```text
Triggered by:
  doom_score >= 8
  OR last-resort fallback when no ending conditions met
```

---

---

# V. 36-Chapter Metadata IDs (Actual)

The following is the complete list of all 36 chapter IDs as defined in `game/progression_data.rpy` under `CHAPTER_ORDER`. Each chapter has metadata for prerequisites, route assignment, timeline position, exclusions, and unlock conditions.

```text
# Prologue
prologue_rain_dream                          # Tâm — Default unlocked

# Tâm Route (early)
tam_c01_interview_day                        # Tâm — Prereq: prologue
tam_c02_company_party                        # Tâm — Prereq: tam_c01
tam_c03_thienan_family                       # Tâm — Prereq: tam_c02

# Hoàng POV
hoang_h01_brother_house                      # Hoàng — Prereq: tam_c03

# Tâm Route (mid)
tam_c05_sunday_date                          # Tâm — Prereq: hoang_h01
tam_c06_minh_returns                         # Tâm — Prereq: tam_c05
tam_c07_minh_at_company                      # Tâm — Prereq: tam_c06

# Yuuka Arrival
yuuka_c08_festival_arrival                   # Yuuka — Prereq: tam_c07

# Flashback Minyuu (5 chapters)
fb_minyuu_01_first_frame                     # Minh — Prereq: yuuka_c08
fb_minyuu_02_working_rhythm                  # Minh — Prereq: fb_minyuu_01
fb_minyuu_03_door_left_open                  # Minh — Prereq: fb_minyuu_02
fb_minyuu_04a_old_friends                    # Minh — Branch A (prereq: fb_minyuu_03)
fb_minyuu_04b_living_together                # Minh — Branch B (prereq: fb_minyuu_03)
fb_minyuu_04c_no_breakup                     # Minh — Branch C (prereq: fb_minyuu_03)
fb_minyuu_05b_separation                     # Minh — Prereq: fb_minyuu_04b only

# Present-Day Midgame
yuuka_c09_yuukas_work                        # Yuuka — Prereq: any fb_minyuu_04
work_c10_project_festival_overlap            # Work — Prereq: yuuka_c09
group_c11_social_dinner                      # Group — Prereq: work_c10
work_c16_project_crisis                      # Work — Prereq: group_c11

# Hoàng Shadow
hoang_h05_shadow_of_minh                     # Hoàng — Prereq: work_c16

# Yuuka Present-Day (3 parallel branches)
yuuka_c18a_career_interlude                  # Yuuka — Prereq: hoang_h05
yuuka_c18b_habit_of_you                      # Yuuka — Prereq: hoang_h05
yuuka_c18c_long_distance_interlude           # Yuuka — Prereq: hoang_h05

# City After Festival (3 parallel branches)
c19a_city_after_festival_old_friends         # Minh — Prereq: yuuka_c18a
c19b_city_after_festival_ex_lovers           # Minh — Prereq: yuuka_c18b
c19c_city_after_festival_still_lovers        # Minh — Prereq: yuuka_c18c

# Tâm Late-Game
tam_c20a_tam_minh_possible                   # Tâm — Prereq: c19 (any)
tam_c20b_admiration_vs_love                  # Tâm — Prereq: c19 (any)

# Thiên An Late-Game
thienan_c21a_minh_possible                   # Thiên An — Prereq: tam_c20b
thienan_c21b_choose_own_path                 # Thiên An — Prereq: tam_c20b

# Huyền Route
huyen_c22_quan_or_hoang                      # Huyền — Prereq: tam_c20b or thienan_c21b

# Minyuu Resolution (3 branches)
minyuu_c23a_old_friends_resolution           # Minh — Prereq: c19a
minyuu_c23b_ex_lovers_resolution             # Minh — Prereq: c19b
minyuu_c23c_still_lovers_resolution          # Minh — Prereq: c19c

# Final Chapter
final_c24_last_choices                       # Final — Prereq: minyuu_c23 (any)
# After final chapter: jump to ending_resolver label
```

---

---

# VI. Route Exclusion Groups

Exclusion groups are defined in the progression system via the `excludes` field on each chapter's metadata. When one chapter in a group is completed, the others are locked for that playthrough. The actual exclusion rules operate through the chapter prerequisite graph rather than named groups, but the following logical groups emerge:

```text
# Minh-Yuuka relation branches (mutually exclusive direction sets)
Group: minyuu_relationship_seed
  - old_friend_seed     (fb_minyuu_04a → old_close_friends)
  - ex_lover_seed       (fb_minyuu_04b + fb_05b → ex_lovers_long_separated)
  - still_lover_seed    (fb_minyuu_04c → still_lovers)

# Minh romance lock (prevents non-Yuuka romantic endings)
minh_romance_lock = True
  blocks: e03_tam_minh, e07_thienan_minh

# Tâm romantic directions (mutually exclusive in a single playthrough)
Group: tam_romance_main
  - tam_hoang_commit    (leads to e02_tam_hoang)
  - tam_minh_commit     (leads to e03_tam_minh, requires old_close_friends)
  - tam_career_focus    (leads to e21_tam_independent)

# Hoàng romantic directions
Group: hoang_romance_main
  - hoang_tam_open (leads to e02_tam_hoang)
  - hoang_huyen_open (leads to e04_hoang_huyen)

# Huyền romantic directions
Group: huyen_romance_main
  - huyen_hoang_commit (leads to e04_hoang_huyen)
  - NOT huyen_hoang_commit (leads to e05_huyen_quan)

# Thiên An directions
Group: thienan_resolution
  - thienan_minh_commit (leads to e07_thienan_minh)
  - thienan_self_assertion high (leads to e08_thienan_single)
  - family_pressure_thienan high (leads to e09_thienan_arranged)
```

---

---

# VII. Clean Canon Route Summary

The canonical path through the story (default narrative without player deviation):

```text
prologue_rain_dream:
  Tâm dreams of a stranger in the rain (Minh, unrecognised).

tam_c01_interview_day:
  Tâm and Huyền interview at their future company. First sighting of Hoàng.

tam_c02_company_party:
  Tâm talks to Hoàng at the company party. Huyền interacts with everyone.

tam_c03_thienan_family:
  Family dinner introduces Thiên An. Tâm sees her sister's hidden fatigue.

hoang_h01_brother_house:
  Hoàng POV — living in Minh's house. Calls Minh for gift advice.

tam_c05_sunday_date:
  Hoàng and Tâm's first Sunday date. Relationship upgrades.

tam_c06_minh_returns:
  Minh returns to Vietnam. Tâm meets him — emotional shock. Four-person dinner.

tam_c07_minh_at_company:
  Minh as project advisor. Tâm and Hoàng have first subtle friction.

yuuka_c08_festival_arrival:
  Yuuka arrives for the film festival. Minh loses composure.

fb_minyuu_01-03:
  Flashback — first meeting, working together, living together decision.

fb_minyuu_04a/b/c + fb_05b:
  Flashback — living together deepens. Separation point (branch).

yuuka_c09_yuukas_work:
  Present day — Yuuka's work, film screening, cold-yet-warm conversation with Minh.

work_c10 + group_c11 + work_c16:
  Project pressure at work. Quân-Huyền dynamic forms. Crisis deepens.

hoang_h05_shadow_of_minh:
  Hoàng confronts his brother's shadow. Tâm either stays or drifts.

yuuka_c18a/b/c:
  Yuuka's years away from Minh. Tokyo, work, realisation.

c19a/b/c:
  Minh and Yuuka walk through the city after the festival. Old doors reopen.

tam_c20a/b:
  Tâm's late-game choices — her feelings, her clarity.

thienan_c21a/b:
  Thiên An's path — Minh, Quang, or self.

huyen_c22_quan_or_hoang:
  Huyền chooses between Quân and Hoàng.

minyuu_c23a/b/c:
  Minyuu resolution — friendship, reunion, or long-distance.

final_c24_last_choices:
  All characters make their final choice.

ending_resolver:
  Routes to the correct ending label based on all accumulated variables.
```

---

Bản timeline này đã được cập nhật để phản ánh đúng story flow hiện tại trong codebase. Xem `game/progression_data.rpy` cho metadata đầy đủ của 36 chapters, `game/ending_rules.rpy` cho 24 endings, và `game/story_state.rpy` cho runtime variables.
