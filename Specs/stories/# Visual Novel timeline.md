Rõ rồi, Sir. Bản dưới đây là **Game Timeline v0.2 — Narrative + Branch Design**, viết lại chi tiết từ Prologue đến Endgame, có đủ canon path, branch path, unlock route, condition, flag/relationship direction để sau này đưa vào Ren’Py progression system. Cơ chế đang có sẵn hỗ trợ `core / pov / bonus / extra`, unlock route bằng `unlocks/prerequisites`, mutual exclusion bằng `exclusion_group/excludes`, và ending rule bằng completed chapters / directions / emotional values nên timeline này bám được vào hệ thống hiện tại. 

---

# GAME TIMELINE — *Tựa Gió, Tựa Mây*

## 0. Core Design Philosophy

Game không nên là kiểu “chọn sai vẫn bị kéo về canon”. Canon chỉ là **mạch cảm xúc chuẩn**, còn game route phải cho người chơi thật sự tác động vào:

* Ai bước tới trước.
* Ai giữ khoảng cách.
* Ai hiểu nhầm.
* Ai nhường ai.
* Ai trưởng thành đủ để buông.
* Ai ích kỷ một chút và phải trả giá.

Theme chính:

> **Coincidence opens the door. Choice decides who stays. Every decision has a price.**

Canon pair:

* Tâm — Hoàng
* Yuuka — Minh
* Huyền — Quân
* Thiên An — Quang

Possible endings:

* Tâm — Hoàng
* Tâm — Minh
* Hoàng — Huyền
* Yuuka — Minh
* Thiên An — Minh
* Thiên An — Quang
* Minh độc thân
* Yuuka độc thân
* Thiên An độc thân
* Thiên An kết hôn theo sắp xếp
* Minh và Yuuka đến với nhau rất lâu sau, không kết hôn
* Doom Ending: không ai trong dàn chính thành đôi

---

# 1. Global Progression Variables

## 1.1. Player Stats — Tâm-centered

Dù có nhiều route, player nên khởi đầu từ Tâm. Vì vậy các chỉ số chính vẫn phản ánh cách Tâm sống và lựa chọn.

```renpy
tam_courage       # Dám bước tới, dám nói thật, dám chọn tình cảm.
tam_empathy       # Đọc cảm xúc người khác, không vô tình làm tổn thương bạn bè.
tam_clarity       # Nhận ra mình thật sự muốn gì.
tam_career        # Năng lực công việc, quản lý dự án, xử lý áp lực.
tam_restraint     # Biết lùi lại đúng lúc.
tam_intuition     # Cảm giác mơ hồ với Minh / giấc mơ / các tín hiệu bất thường.
```

## 1.2. Relationship Values

```renpy
rel_tam_hoang
rel_tam_minh
rel_tam_huyen
rel_hoang_huyen
rel_minh_yuuka
rel_thienan_quang
rel_thienan_minh
rel_huyen_quan
```

## 1.3. Emotional Axes

Các biến này quan trọng hơn “điểm tình cảm” đơn thuần.

```renpy
trust_hoang
trust_minh
trust_yuuka
trust_huyen

tension_tam_hoang
tension_minh_yuuka
tension_tam_yuuka
tension_thienan_family

guilt_tam
guilt_hoang
guilt_minh
guilt_yuuka

career_pressure
family_pressure
```

## 1.4. Relationship Direction Flags

```renpy
direction_tam_hoang_romance
direction_tam_hoang_friendship
direction_tam_minh_seed
direction_tam_minh_romance
direction_hoang_huyen_seed
direction_hoang_huyen_romance
direction_minh_yuuka_unresolved
direction_minh_yuuka_reconcile
direction_minh_yuuka_parting
direction_thienan_quang_slowburn
direction_thienan_minh_seed
direction_thienan_arranged
direction_huyen_quan_romance
direction_doom_drift
```

---

# 2. Route Unlock Structure

## Initial Route

```renpy
tam_route = visible from start
```

## Unlock Order

```renpy
tam_c01 -> tam_c02 -> tam_c03
tam_c02 or tam_c03 -> hoang_h01
tam_c06 -> minh_m01
tam_c08 -> yuuka_y01
tam_c03 -> thienan_a01
tam_c07 or huyen_bonus_01 -> huyen_h01
```

Recommended route visibility:

| Route    | Unlock Condition                             | Narrative Reason                                  |
| -------- | -------------------------------------------- | ------------------------------------------------- |
| Tâm      | Default                                      | Main lens of Act 1                                |
| Hoàng    | After player sees him beyond “love interest” | His POV reveals family, Minh, emotional restraint |
| Minh     | After dinner / company project               | He becomes active force in story                  |
| Yuuka    | After her arrival                            | Her past with Minh reframes everything            |
| Huyền    | After she becomes more than “best friend”    | Opens Quân / Hoàng-Huyền / loyalty routes         |
| Thiên An | After family chapter                         | Opens adult-love / family-pressure route          |

---

# 3. Timeline Overview

## Act 0 — Dream Before Rain

Purpose: Seed mystery.

* Tâm dreams of rain.
* A young man appears under the blur of water and streetlight.
* She cannot clearly see his face.
* He gives her an umbrella / catches her before she falls / says one sentence she forgets after waking.
* This man is Minh.
* Player does not know yet.

Flag:

```renpy
flag_dream_minh = True
tam_intuition += 1
```

This prologue should feel like “maybe memory, maybe dream, maybe destiny being dramatic again.” A little suspicious, but not fantasy-hard.

---

# 4. Detailed Chapter Timeline

---

## PROLOGUE — `tam_p00`

### Title: **Giấc mơ trong mưa**

**POV:** Tâm
**Type:** core / prologue
**Purpose:** Foreshadow Minh and the hidden emotional axis of the story.

### Content

Tâm mơ thấy mình đứng dưới một cơn mưa rất cũ. Không phải cơn mưa hiện tại, mà như một đoạn ký ức bị bỏ quên trong ngăn kéo. Cô còn nhỏ hơn bây giờ, yếu đuối hơn, hoặc chỉ là cảm giác như vậy. Một chàng trai cao gầy đứng trước mặt cô, cầm chiếc ô lệch về phía cô nhiều hơn phía mình.

Cô không nhìn rõ mặt anh.

Chỉ nhớ bàn tay. Giọng nói. Và cảm giác kỳ lạ rằng người này từng ở rất gần mình, rồi biến mất.

### Choices

1. **Cố nhìn rõ mặt người đó**

   ```renpy
   tam_intuition += 2
   flag_tam_chases_dream = True
   ```

   Later unlocks stronger reaction to Minh.

2. **Gọi anh lại**

   ```renpy
   tam_courage += 1
   flag_tam_called_rain_man = True
   ```

   Later unlocks direct dialogue option with Minh.

3. **Đứng yên dưới mưa**

   ```renpy
   tam_restraint += 1
   flag_tam_accepts_uncertainty = True
   ```

   Later unlocks quieter, more introspective options.

### Unlock

```renpy
unlocks = ["tam_c01"]
```

---

## CHAPTER 1 — `tam_c01`

### Title: **Ngày phỏng vấn và buổi tối ăn mừng**

**POV:** Tâm
**Type:** core
**Purpose:** Introduce Tâm, Huyền, company, first sighting of Hoàng.

### Content

Tâm và Huyền cùng đi phỏng vấn. Đây là chương đời thường, có chút áp lực, chút hài, chút thân tình. Huyền là bạn thân kiểu nói thẳng, đủ tinh để thấy Tâm lo nhưng không vạch trần cô quá sớm.

Hai người đều trúng tuyển.

Tối đó, họ đi ăn mừng ở một nhà hàng sang trọng hơn mức bình thường của hai cô gái mới đi làm. Huyền bảo: “Lâu lâu phải sống như nữ chính phim truyền hình một chút, không thì đời văn phòng khô quá.”

Ở nhà hàng, Hoàng lần đầu nhìn thấy Tâm và Huyền. Hai cô chưa quen anh. Với Hoàng, ấn tượng đầu là nụ cười của Tâm — chi tiết canon quan trọng. Canon gốc sau này cho thấy Hoàng là người có phần “phòng thủ”, còn Tâm thường là người chủ động mở đường trong mối quan hệ. 

### Key Scenes

* Mini-game phỏng vấn:

  * Chọn câu trả lời chuyên nghiệp.
  * Chọn phản ứng khi Huyền hơi căng thẳng.
  * Chọn cách Tâm nói về bản thân: khiêm tốn, tự tin, hay quá an toàn.

* Nhà hàng:

  * Tâm và Huyền ăn mừng.
  * Hoàng ở bàn khác với trưởng phòng / đối tác.
  * Hoàng chú ý Tâm nhưng không tiếp cận.
  * Tâm có thể thoáng nhìn lại, hoặc hoàn toàn không biết.

* End beat:

  * Tâm về nhà, mơ hồ thấy hôm nay có điều gì đó “sắp bắt đầu”.
  * Nếu `tam_intuition >= 2`, cô lại nhớ cơn mưa trong mơ.

### Branch Choices

#### Choice A — Trong buổi tiệc công ty sau đó, Tâm chủ động bắt chuyện với Hoàng

Canon path.

```renpy
rel_tam_hoang += 2
tam_courage += 1
direction_tam_hoang_seed = True
flag_tam_first_approach_hoang = True
```

#### Choice B — Tâm không bắt chuyện, nhưng giữ ánh mắt lâu hơn một chút

Hoàng chủ động làm quen sau đó.

```renpy
rel_tam_hoang += 1
trust_hoang += 1
flag_hoang_first_approach_tam = True
```

#### Choice C — Tâm ở cạnh Huyền cả buổi, không tạo cơ hội riêng

Hoàng vẫn nhớ Tâm, nhưng duyên bị chậm lại.

```renpy
rel_tam_huyen += 2
rel_tam_hoang += 0
flag_no_first_contact_hoang = True
```

#### Choice D — Tâm giới thiệu Huyền vào cuộc trò chuyện với Hoàng nhiều hơn

Early Hoàng-Huyền seed.

```renpy
rel_hoang_huyen += 1
rel_tam_huyen += 1
flag_huyen_hoang_first_spark = True
```

### Unlock

```renpy
unlocks = ["tam_c02"]
```

---

## CHAPTER 2 — `tam_c02`

### Title: **Khoảng cách vừa đủ gần**

**POV:** Tâm
**Type:** core
**Purpose:** Establish Hoàng as young architect/designer; relationship triangle Tâm-Hoàng-Huyền.

### Content

Hoàng xuất hiện với vai trò nhà thiết kế kiến trúc trẻ có tài, bạn của trưởng phòng, được mời hợp tác trong một dự án của công ty. Anh không phải nhân viên chính thức nhưng thường xuyên có mặt.

Chương này cần có nhịp tiếp xúc đều:

* Tâm làm việc với Hoàng về yêu cầu dự án.
* Huyền phụ trách phần điều phối / tài liệu / deadline.
* Hoàng thể hiện năng lực qua cách nhìn không gian, ánh sáng, thói quen người dùng.
* Tâm nhận ra anh không chỉ “đẹp trai dễ nói chuyện”, mà có nghề thật.
* Huyền nhận ra Hoàng không khó gần như vẻ ngoài.

### Key Scenes

1. Meeting đầu tiên:

   * Quân — trưởng phòng khó tính — giới thiệu Hoàng.
   * Quân nghiêm, ít khen, tạo áp lực cho Tâm và Huyền.
   * Huyền ghét kiểu “đã đẹp trai lại còn được mời riêng” nhưng sau đó phải công nhận Hoàng giỏi.

2. Tâm và Hoàng ở lại sau giờ:

   * Hoàng chỉnh một bản layout.
   * Tâm hỏi vì sao anh đổi vị trí lối vào.
   * Hoàng trả lời bằng logic rất đời: “Người ta thường đi theo nơi họ thấy an toàn trước, rồi mới đi theo nơi đẹp.”

3. Huyền chen vào:

   * Nếu player chọn đẩy thuyền, Tâm tạo cơ hội cho Huyền nói chuyện riêng với Hoàng.
   * Nếu canon, Huyền sớm nhận ra Tâm thích Hoàng và trêu.

### Branch Core Choice

#### Path 2A — Tâm tiến gần Hoàng

```renpy
rel_tam_hoang += 2
tam_courage += 1
direction_tam_hoang_romance = True
```

Unlock later confession option.

#### Path 2B — Tâm giữ bạn bè

```renpy
rel_tam_hoang += 1
tam_restraint += 1
direction_tam_hoang_friendship = True
```

Prevents early canon but keeps Hoàng available.

#### Path 2C — Tâm đẩy thuyền Huyền-Hoàng

```renpy
rel_hoang_huyen += 2
rel_tam_huyen += 1
direction_hoang_huyen_seed = True
flag_tam_wingwoman_huyen = True
```

#### Path 2D — Tâm tập trung công việc, không ưu tiên tình cảm

```renpy
tam_career += 2
rel_tam_hoang += 0
rel_hoang_huyen += 0
flag_tam_career_first = True
```

### Unlock

```renpy
unlocks = ["tam_c03", "hoang_h01"]
```

---

## CHAPTER 3 — `tam_c03`

### Title: **Chị gái không chịu hạnh phúc**

**POV:** Tâm
**Type:** core
**Purpose:** Introduce Thiên An, family axis, career growth system.

### Content

Thiên An là chị gái Tâm: xinh đẹp, tài giỏi, trưởng thành, có sức hút rõ nhưng chuyện tình duyên không trọn vẹn. Mẹ hay giục cô đi xem mắt. Các đối tượng đều tốt trên giấy: học vấn tốt, gia đình tốt, công việc tốt, “rất hợp để cưới”. Nhưng Thiên An không thấy gì.

Tâm thương chị. Không phải thương kiểu “chị ế tội nghiệp”, mà là thương vì thấy chị luôn sống đúng, sống giỏi, sống tử tế — nhưng lại không có ai khiến chị được yếu mềm.

Chương này mở thêm side progression: Tâm học quản lý dự án từ Thiên An.

### Key Scenes

1. Bữa cơm gia đình:

   * Mẹ nhắc chuyện xem mắt.
   * Thiên An né bằng vẻ bình thản chuyên nghiệp.
   * Tâm quan sát thấy chị chỉ mệt, không giận.

2. Đêm chị em:

   * Thiên An hỏi công việc của Tâm.
   * Tâm kể chuyện dự án, Quân, Hoàng, Huyền.
   * Thiên An chỉ ra điểm Tâm đang thiếu: biết làm chưa đủ, phải biết “đứng mũi chịu sào”.

3. Optional training:

   * Mini-game quản lý task/deadline/stakeholder.
   * Nếu làm tốt: `tam_career += 2`, unlock later “Project Lead” option.

### Choices

#### Choice A — Tâm hỏi thẳng chị có cô đơn không

```renpy
tam_courage += 1
rel_tam_thienan += 2
flag_tam_knows_thienan_loneliness = True
```

Unlock later Thiên An emotional route.

#### Choice B — Tâm không hỏi, chỉ ở cạnh chị

```renpy
tam_empathy += 1
rel_tam_thienan += 1
flag_tam_gentle_support_thienan = True
```

Good for Thiên An-Quang slowburn.

#### Choice C — Tâm hứa sẽ tìm người tốt cho chị

```renpy
tam_courage += 1
family_pressure += 1
flag_tam_matchmaker_thienan = True
```

Can open Thiên An-Minh accidentally later.

#### Choice D — Tâm chỉ tập trung học kỹ năng

```renpy
tam_career += 2
flag_tam_project_growth = True
```

Unlocks stronger company outcomes.

### Unlock

```renpy
unlocks = ["tam_c04", "thienan_a01"]
```

---

## CHAPTER 4 — `hoang_h01`

### Title: **Người sống trong nhà của anh trai**

**POV:** Hoàng
**Type:** pov
**Purpose:** Reveal Hoàng’s background, Minh as older brother, gift branch.

### Content

Hoàng sống một mình trong căn biệt thự của Minh. Gia thế được hé lộ nhưng không nói lộ liễu: cha mẹ làm nhà nước, có vị trí, gia đình có quy tắc, nhưng Hoàng không muốn đời mình bị định nghĩa bằng họ.

Minh đang ở xa. Hai anh em tương tác qua chat/call. Minh là người anh từng chăm Hoàng từ nhỏ, gần như “làm anh, làm bạn, đôi lúc kiêm luôn cha mẹ” — đây là trục rất mạnh trong backstory Minh-Hoàng. 

Hoàng hỏi Minh tư vấn chọn quà.

### Conditional Gift Logic

#### If `direction_tam_hoang_romance == True`

Hoàng chọn quà cho Tâm.

* Canon: món quà tinh tế, không quá đắt lộ liễu.
* Minh khuyên: “Đừng mua thứ khiến người nhận thấy mắc nợ.”
* Hoàng chọn thứ liên quan đến thói quen của Tâm: sổ tay, khăn, phụ kiện nhỏ, hoặc vật dụng công việc.

```renpy
flag_gift_for_tam = True
trust_hoang += 1
rel_tam_hoang += 1
```

#### If `direction_hoang_huyen_seed == True`

Hoàng phân vân chọn quà cho Huyền.

* Huyền không thích thứ “bánh bèo”.
* Minh khuyên chọn thứ thực dụng nhưng có ý riêng.
* Quà có thể là bút tốt, kẹp tài liệu, hoặc món liên quan đến cà phê.

```renpy
flag_gift_for_huyen = True
rel_hoang_huyen += 1
```

#### If no romance direction

Hoàng mua quà chung cho cả nhóm.

* Vé triển lãm / workshop / bữa ăn.
* Giữ thế bạn bè hợp cạ.

```renpy
flag_group_gift = True
rel_tam_hoang += 1
rel_hoang_huyen += 1
```

### Branch Choice — Hoàng nói gì với Minh?

1. **“Em nghĩ em thích Tâm.”**

   ```renpy
   direction_tam_hoang_romance = True
   guilt_hoang -= 1
   ```

2. **“Em không chắc giữa Tâm và Huyền.”**

   ```renpy
   flag_hoang_confused = True
   tension_tam_huyen += 1
   ```

3. **“Chỉ là bạn thôi.”**

   ```renpy
   direction_tam_hoang_friendship = True
   ```

### Unlock

```renpy
unlocks = ["tam_c05"]
```

---

## CHAPTER 5 — `tam_c05`

### Title: **Buổi hẹn đặc biệt ngày Chủ Nhật**

**POV:** Tâm
**Type:** core
**Purpose:** Relationship upgrade / group bond / Hoàng trust.

Canon gốc đã có tinh thần rất rõ: Chủ Nhật là ngày đặc biệt, Hoàng chủ động hẹn, Tâm sửa soạn kỹ khác thường, và mối quan hệ hai người đã vượt khỏi mức bạn bè. 

### Conditional Structure

#### Case 5A — Tâm là bạn gái Hoàng

Private date.

Content:

* Hoàng mặc lịch sự.
* Tâm bất ngờ vì anh đi xe hơi.
* Hai người ăn sáng, đi một nơi Hoàng đã chuẩn bị.
* Hoàng không giỏi nói lời hoa mỹ, nhưng từng hành động cho thấy anh đã suy nghĩ nhiều.
* Tâm cảm nhận: lần đầu Hoàng chủ động thật sự.

Outcome:

```renpy
rel_tam_hoang += 3
trust_hoang += 2
direction_tam_hoang_romance = True
flag_tam_hoang_level_up = True
```

#### Case 5B — Huyền là người Hoàng đang nghiêng về

Private / semi-private date với Huyền.

Tâm không đi, nhưng có đoạn Tâm-Huyền nói chuyện trước/sau buổi hẹn. Huyền vừa đắc ý vừa hơi áy náy.

Outcome:

```renpy
rel_hoang_huyen += 3
rel_tam_huyen += 1
direction_hoang_huyen_romance = True
flag_huyen_hoang_level_up = True
```

#### Case 5C — Không ai hẹn hò

Buổi đi chơi ba người.

Hoàng hơi thích Tâm hơn, nhưng Tâm không bật đèn xanh. Huyền nhận ra nhưng không chen vào nếu player không đẩy. Đây là nhánh “ấm mà lửng”.

Outcome:

```renpy
rel_tam_hoang += 1
rel_hoang_huyen += 1
rel_tam_huyen += 1
flag_triad_friendship = True
```

### Important Choice

Tâm có thể:

1. **Đáp lại sự chủ động của Hoàng**

   ```renpy
   direction_tam_hoang_romance = True
   rel_tam_hoang += 2
   ```

2. **Giữ khoảng cách dịu dàng**

   ```renpy
   direction_tam_hoang_friendship = True
   tam_restraint += 1
   ```

3. **Quan sát Hoàng và Huyền**

   ```renpy
   direction_hoang_huyen_seed = True
   tam_empathy += 1
   ```

### Unlock

```renpy
unlocks = ["tam_c06"]
```

---

# ACT II — Người trong mưa trở về

---

## CHAPTER 6 — `tam_c06`

### Title: **Người anh trai trở về**

**POV:** Tâm
**Type:** core
**Purpose:** Minh enters present timeline. Unlock Minh route.

### Setup

Minh về nước. Hoàng đưa “bạn” về giới thiệu với anh.

Minh phải tạo cảm giác: rất bình thản, rất tử tế, nhưng có một khoảng cách khiến người khác khó bước vào. Anh không lạnh vì vô cảm, mà lạnh vì đã quen tự kiểm soát.

### Conditional Dinner Structure

#### Case 6A — Canon: Tâm đang hẹn hò Hoàng

Hoàng đưa Tâm về gặp Minh.

Tâm nhìn thấy Minh và chấn động. Người trong mưa. Người trong giấc mơ. Hoặc một phần ký ức cô không chắc có thật.

Nếu `tam_intuition >= 2` hoặc `flag_tam_chases_dream`:

```renpy
flag_tam_recognizes_minh = True
tension_tam_hoang += 2
rel_tam_minh += 1
```

Tâm bất ngờ bỏ về / xin phép về sớm.

Sau đó mở “lần hẹn thứ hai”: bàn ăn bốn người với Hoàng, Tâm, Minh, Huyền.

#### Case 6B — Hoàng đang gần Huyền

Hoàng đưa Huyền về gặp Minh.

Huyền thấy Minh thú vị: không phải kiểu dễ gần, nhưng nói câu nào cũng có trọng lượng.

Huyền kéo Tâm đến bữa tối lần sau vì:

* tò mò,
* muốn Tâm gặp người “khó phân loại” này,
* hoặc linh cảm Tâm sẽ có phản ứng.

```renpy
rel_huyen_minh += 1
flag_huyen_invites_tam_to_minh_dinner = True
```

#### Case 6C — Không ai hẹn hò

Hoàng mời cả Tâm và Huyền đến nhà ăn tối với Minh như hai người bạn thân trong công việc.

Không có drama bỏ về, nhưng Tâm vẫn có phản ứng mơ hồ nếu đã tăng `tam_intuition`.

```renpy
flag_four_person_dinner_neutral = True
rel_tam_minh += 1
rel_huyen_minh += 1
```

### Unlock

```renpy
unlocks = ["minh_m01", "tam_c07"]
```

---

## CHAPTER 7 — `tam_c07` / `minh_m01`

### Title: **Người giám sát từ tập đoàn đối tác**

**POV:** Tâm hoặc Minh
**Type:** mutually exclusive POV
**Purpose:** Minh enters workplace. Tâm-Minh axis begins.

Chương này nên có hai version loại trừ nhau, đúng như ý anh: **Tâm POV** và **Minh POV**. Hệ thống hiện tại hỗ trợ mutual exclusion bằng `exclusion_group/excludes`, rất hợp cho đoạn này. 

---

## Option 7A — `tam_c07`

### Title: **Tâm POV — Một người khó đọc**

Tâm gặp Minh ở công ty với vai trò giám sát/cố vấn dự án từ tập đoàn đối tác lớn. Minh không cố tạo quyền lực, nhưng ai cũng tự động nghiêm túc hơn khi anh bước vào phòng.

### Core Scenes

* Minh review dự án.
* Quân nghiêm nhưng vẫn nể Minh.
* Tâm trả lời một câu tốt nếu player có `tam_career >= 2`.
* Minh nhớ chi tiết nhỏ Tâm từng nói ở bữa tối.
* Hoàng nhận ra Tâm để ý Minh nhiều hơn bình thường.

### Choices

1. **Tâm giữ chuyên nghiệp tuyệt đối**

   ```renpy
   tam_career += 1
   trust_minh += 1
   rel_tam_minh += 1
   ```

2. **Tâm chủ động hỏi Minh sau meeting**

   ```renpy
   rel_tam_minh += 2
   tam_courage += 1
   direction_tam_minh_seed = True
   tension_tam_hoang += 1 if direction_tam_hoang_romance
   ```

3. **Tâm né Minh vì sợ cảm giác lạ**

   ```renpy
   tam_restraint += 1
   guilt_tam += 1
   flag_tam_avoids_minh = True
   ```

4. **Tâm kể thật với Hoàng về cảm giác quen Minh**

   ```renpy
   trust_hoang += 2
   tension_tam_hoang -= 1
   flag_tam_honest_about_minh = True
   ```

5. **Tâm giấu Hoàng**

   ```renpy
   tension_tam_hoang += 2
   guilt_tam += 1
   ```

---

## Option 7B — `minh_m01`

### Title: **Minh POV — Người giống một cơn mưa cũ**

Minh nhìn Tâm và nhận ra điều gì đó. Không phải yêu ngay. Không nên rẻ tiền như thế. Mà là cảm giác cô gái này xuất hiện đúng vào vùng đời anh đang cố giữ yên.

### Core Scenes

* Minh đánh giá Tâm có năng lực nhưng dễ bị cảm xúc kéo lệch.
* Anh nhận ra Hoàng quan tâm Tâm.
* Nếu Tâm-Hoàng canon: Minh chủ động giữ khoảng cách.
* Nếu Hoàng-Huyền: Minh thoải mái hơn khi nói chuyện với Tâm.
* Nếu no romance: Minh xem Tâm như nhân tố đáng chú ý.

### Choices

1. **Minh giúp Tâm nhưng không để lại dấu vết**

   ```renpy
   trust_minh += 1
   rel_tam_minh += 1
   direction_minh_guarded = True
   ```

2. **Minh trực tiếp góp ý nghiêm khắc**

   ```renpy
   tam_career += 1
   tension_tam_minh += 1
   trust_minh += 1
   ```

3. **Minh hỏi Hoàng về Tâm**

   ```renpy
   flag_minh_asks_hoang_about_tam = True
   tension_tam_hoang += 1 if direction_tam_hoang_romance
   ```

4. **Minh tự nhắc mình không được bước vào**

   ```renpy
   tam_restraint += 0
   guilt_minh += 1
   direction_tam_minh_forbidden = True
   ```

### Unlock

```renpy
unlocks = ["tam_c08", "yuuka_y01"]
```

---

## CHAPTER 8 — `yuuka_y01`

### Title: **Cô gái từ sân bay**

**POV:** Tâm / Yuuka mixed
**Type:** core + route unlock
**Purpose:** Yuuka appears. Minh-Yuuka past becomes active.

### Content

Yuuka đến Việt Nam vì Liên hoan phim Châu Á - Thái Bình Dương. Trong canon cũ, Yuuka gặp lại Minh với kiểu thân mật rất đặc trưng: gọi Minh là “Otou-chan”, bị Minh chặn đầu lại, rồi lao vào ôm anh như một đứa trẻ lâu ngày gặp lại người thân; lời thoại cũng xác nhận cô đến vì festival nhưng vẫn trêu là đến để gặp anh. 

Chương này nên bắt đầu từ góc nhìn Tâm:

* Tâm thấy Yuuka trước ở sân bay / khách sạn / nhà Hoàng.
* Cô nhận ra Yuuka quá đẹp, quá sáng, quá tự nhiên trong cách bước vào không gian của người khác.
* Tâm chưa biết Yuuka là ai.
* Nếu Tâm đang yêu Hoàng, cô có thể hiểu lầm Yuuka liên quan đến Hoàng.
* Khi Yuuka nhìn thấy Minh, mọi giả định của Tâm bị đảo ngược.

### Core Emotional Function

Yuuka không chỉ là “tình địch”. Cô là **quá khứ sống** của Minh.

Cô xuất hiện để buộc tất cả nhân vật đối mặt với điều này:

* Tâm không phải người đầu tiên làm Minh dao động.
* Hoàng không biết hết quá khứ của anh trai.
* Minh không quên được Yuuka.
* Yuuka không đến chỉ để dự festival.
* Huyền là người đầu tiên nhìn ra: “Mấy người này không đơn giản.”

### Choices

#### Choice A — Tâm quan sát Yuuka với thiện cảm

```renpy
trust_yuuka += 1
tam_empathy += 1
tension_tam_yuuka -= 1
```

Unlock later friendship route Tâm-Yuuka.

#### Choice B — Tâm thấy khó chịu nhưng không nói

```renpy
tension_tam_yuuka += 1
guilt_tam += 1
```

Good for jealousy branch.

#### Choice C — Tâm hỏi thẳng Hoàng về Yuuka

```renpy
trust_hoang += 1
flag_tam_asks_about_yuuka = True
```

If Hoàng answers honestly, reduces later conflict.

#### Choice D — Tâm hỏi Minh riêng

```renpy
rel_tam_minh += 1
tension_minh_yuuka += 1
direction_tam_minh_seed = True
```

Dangerous path.

### Unlock

```renpy
unlocks = ["yuuka_y02", "tam_c09", "minh_m02"]
```

---

# ACT III — Những lựa chọn bắt đầu có giá

---

## CHAPTER 9 — `tam_c09`

### Title: **Bàn ăn có quá nhiều điều chưa nói**

**POV:** Tâm
**Type:** core
**Purpose:** Four-person dinner / emotional triangulation.

### Participants vary:

* Canon: Hoàng — Tâm — Minh — Yuuka, with Huyền arriving later or being referenced.
* Huyền-Hoàng path: Hoàng — Huyền — Minh — Tâm.
* Neutral path: Hoàng — Tâm — Huyền — Minh, then Yuuka interrupts / joins.

### Core Scenes

* Bữa ăn tưởng bình thường nhưng ai cũng đang quan sát ai.
* Minh nấu / chuẩn bị món có liên quan đến Yuuka.
* Yuuka nhận ra ngay.
* Tâm nhận ra Minh là kiểu người nhớ rất kỹ những điều nhỏ.
* Hoàng lặng đi vì thấy anh trai sống động hơn khi ở cạnh Yuuka.
* Huyền nếu có mặt sẽ là người phá băng.

### Key Branches

#### If Tâm-Hoàng canon

Tâm bắt đầu dao động.

```renpy
tension_tam_hoang += 2
rel_tam_minh += 1
guilt_tam += 1
```

Player can reduce damage by honesty.

#### If Hoàng-Huyền

Tâm tự do quan sát Minh hơn.

```renpy
rel_tam_minh += 2
direction_tam_minh_seed = True
```

#### If neutral friendship

All routes remain open.

```renpy
rel_tam_hoang += 1
rel_tam_minh += 1
rel_hoang_huyen += 1
```

### Major Choice

1. **Ngồi cạnh Hoàng**

   ```renpy
   rel_tam_hoang += 1
   trust_hoang += 1
   ```

2. **Ngồi cạnh Minh**

   ```renpy
   rel_tam_minh += 2
   tension_tam_hoang += 1 if romance_tam_hoang
   ```

3. **Ngồi cạnh Huyền**

   ```renpy
   rel_tam_huyen += 1
   tam_restraint += 1
   ```

4. **Giúp Yuuka trong bếp**

   ```renpy
   trust_yuuka += 2
   tension_tam_yuuka -= 1
   unlock_choice_yuuka_private_talk = True
   ```

---

## CHAPTER 10 — `minh_m02` / `yuuka_y02`

### Title: **Người cũ không nằm yên trong quá khứ**

**POV:** Minh or Yuuka
**Type:** mutually exclusive POV
**Purpose:** Reveal Minh-Yuuka unresolved history.

### Option A — Minh POV

Minh biết Yuuka đến không đơn giản. Anh cố giữ thái độ đùa cợt vừa đủ để tránh phải nói thật. Yuuka càng tự nhiên, Minh càng phải kiểm soát.

Core:

* Minh nhớ thời họ từng sống gần nhau / làm việc cùng nhau.
* Anh nhớ Yuuka từng muốn hiểu nơi anh lớn lên.
* Anh nhớ họ chia xa không phải vì hết yêu.
* Anh nhìn Tâm và thấy một khả năng khác — nhưng khả năng ấy nguy hiểm, vì Hoàng.

Choice:

```renpy
minh_keep_boundary
minh_soften_to_yuuka
minh_notice_tam
minh_prioritize_hoang
```

### Option B — Yuuka POV

Yuuka trở lại Việt Nam với tư cách người đã trưởng thành hơn, có sự nghiệp, có tên tuổi. Nhưng trước Minh, cô vẫn có phần giống cô gái năm xưa.

Core:

* Yuuka nhận ra Minh vẫn nhớ thói quen của mình.
* Cô nhìn Tâm và hiểu ngay: cô gái này có thể bước vào vùng mà Minh đang cố khóa lại.
* Yuuka không ghét Tâm. Điều đó còn khó chịu hơn, vì nếu ghét được thì đã dễ.

Choice:

```renpy
yuuka_claims_past
yuuka_respects_distance
yuuka_tests_minh
yuuka_befriends_tam
```

### Branch Result

#### Minh-Yuuka revive seed

```renpy
rel_minh_yuuka += 2
direction_minh_yuuka_unresolved = True
```

#### Minh-Yuuka boundary

```renpy
guilt_minh += 1
direction_minh_yuuka_parting = True
```

#### Tâm-Minh danger

```renpy
rel_tam_minh += 1
tension_minh_yuuka += 1
```

---

## CHAPTER 11 — `huyen_h01`

### Title: **Trưởng phòng khó tính và cô gái không chịu lép vế**

**POV:** Huyền
**Type:** pov / support route
**Purpose:** Develop Huyền-Quân canon path; preserve Hoàng-Huyền alternate.

### Content

Quân là trưởng phòng khó tính. Anh không ác, nhưng tiêu chuẩn cao, nói ít, sửa thẳng, dễ làm người khác tự ái.

Huyền ban đầu rất khó chịu với Quân. Nhưng khi một crisis dự án xảy ra, Quân là người đứng ra nhận trách nhiệm với cấp trên, còn Huyền phát hiện anh không đẩy lỗi cho cấp dưới.

### Branches

#### If `direction_hoang_huyen_romance == True`

Huyền route focuses on choosing between comfort and challenge.

* Hoàng dịu hơn.
* Quân khó hơn.
* Huyền phải tự hỏi mình cần người khiến mình được chiều, hay người khiến mình lớn lên.

Choices can keep Hoàng-Huyền or shift to Huyền-Quân.

#### If no Hoàng-Huyền

Huyền-Quân grows naturally.

```renpy
rel_huyen_quan += 2
direction_huyen_quan_romance = True
```

#### If Tâm neglected friendship

Huyền becomes distant.

```renpy
rel_tam_huyen -= 1
flag_huyen_feels_left_behind = True
```

### Key Choice

1. **Huyền cãi lại Quân bằng lý lẽ**

   ```renpy
   rel_huyen_quan += 2
   huyen_confidence += 1
   ```

2. **Huyền nhịn cho qua**

   ```renpy
   huyen_restraint += 1
   rel_huyen_quan += 0
   ```

3. **Huyền tìm Hoàng để than**

   ```renpy
   rel_hoang_huyen += 1
   direction_hoang_huyen_romance = True if previous seed
   ```

4. **Huyền tìm Tâm**

   ```renpy
   rel_tam_huyen += 2
   ```

---

## CHAPTER 12 — `thienan_a01`

### Title: **Người phụ nữ không cần được cứu**

**POV:** Thiên An
**Type:** core / support route
**Purpose:** Introduce Quang; seed Thiên An’s possible endings.

### Content

Quang là trợ lý của Thiên An. Bề ngoài là người làm việc cẩn thận, kín tiếng, năng lực tốt, kiên nhẫn đến hơi đáng ngờ. Sau đó hé lộ anh là thiếu gia của một tập đoàn lớn nhưng từ chối thừa kế sản nghiệp, chọn ở bên Thiên An với vai trò trợ lý suốt sáu năm.

Quang không “cứu” Thiên An. Anh chỉ ở đó, đủ lâu để sự hiện diện của mình trở thành một phần trong đời cô.

### Core Scenes

* Thiên An xử lý một cuộc họp khó.
* Quang chuẩn bị tài liệu cô chưa kịp yêu cầu.
* Mẹ gọi nhắc xem mắt.
* Quang nghe thấy nhưng không xen vào.
* Thiên An hỏi: “Cậu không có gì muốn nói à?”
* Quang đáp: “Có. Nhưng em nói lúc chị muốn nghe, không phải lúc chị đang mệt.”

### Branches

#### Thiên An-Quang slowburn

```renpy
rel_thienan_quang += 2
direction_thienan_quang_slowburn = True
```

#### Thiên An-Minh seed

Triggered if:

```renpy
flag_tam_matchmaker_thienan == True
and rel_tam_minh >= 2
and direction_minh_yuuka_reconcile == False
```

Thiên An gặp Minh qua công việc / gia đình / dự án. Hai người có sự đồng cảm của kiểu người trưởng thành, giỏi chịu đựng.

```renpy
rel_thienan_minh += 1
direction_thienan_minh_seed = True
```

#### Arranged marriage pressure

```renpy
family_pressure += 2
direction_thienan_arranged = True
```

---

## CHAPTER 13 — `tam_c13`

### Title: **Tin đồn**

**POV:** Tâm
**Type:** core
**Purpose:** Force consequences of ambiguity.

### Content

Tin đồn trong công ty bắt đầu lan:

* Tâm được Minh ưu ái.
* Hoàng và Tâm rạn nứt.
* Huyền có gì đó với Hoàng / Quân.
* Yuuka là người yêu cũ của Minh.
* Thiên An có đối tượng gia đình sắp xếp.

Đây là chapter rất hợp để tạo áp lực xã hội và buộc player chọn cách xử lý.

### Main Choice

#### 13A — Tâm đối diện trực tiếp

```renpy
tam_courage += 2
tam_clarity += 1
trust_hoang += 1
trust_minh += 1
career_pressure += 1
```

#### 13B — Tâm im lặng chịu đựng

```renpy
tam_restraint += 1
guilt_tam += 1
tension_tam_hoang += 1
```

#### 13C — Tâm nhờ Huyền giúp

```renpy
rel_tam_huyen += 2
trust_huyen += 1
```

#### 13D — Tâm tìm Minh

```renpy
rel_tam_minh += 2
tension_tam_hoang += 2 if direction_tam_hoang_romance
tension_minh_yuuka += 1
```

#### 13E — Tâm tìm Hoàng

```renpy
rel_tam_hoang += 2
trust_hoang += 2
direction_tam_hoang_romance stays viable
```

### Unlock

```renpy
unlocks = ["tam_c14", "hoang_h02", "minh_m03", "yuuka_y03"]
```

---

## CHAPTER 14 — `hoang_h02`

### Title: **Người đứng giữa hai lối rẽ**

**POV:** Hoàng
**Type:** pov
**Purpose:** Hoàng chooses maturity or avoidance.

### Content

Hoàng nhận ra mọi thứ không còn đơn giản. Nếu là canon, anh yêu Tâm nhưng cảm nhận cô đang bị Minh kéo về một vùng cảm xúc mà anh không chạm tới. Nếu là Hoàng-Huyền, anh phải phân biệt giữa cảm giác được Huyền hiểu và việc anh có thật sự yêu cô không. Nếu neutral, Hoàng phải quyết định có bước tới hay để mọi người trôi qua.

### Choices

1. **Hoàng hỏi thẳng Tâm**

   ```renpy
   trust_hoang += 2
   tension_tam_hoang -= 1
   flag_hoang_confronts_gently = True
   ```

2. **Hoàng lùi lại để Tâm tự chọn**

   ```renpy
   tam_restraint += 0
   guilt_hoang += 1
   direction_hoang_restraint = True
   ```

3. **Hoàng tìm Huyền**

   ```renpy
   rel_hoang_huyen += 2
   direction_hoang_huyen_romance = True
   ```

4. **Hoàng hỏi Minh**

   ```renpy
   trust_minh += 1
   tension_hoang_minh += 1
   flag_hoang_questions_minh = True
   ```

### Critical Branch

If Hoàng asks Minh while `direction_tam_minh_seed == True`, Minh’s response depends on `guilt_minh`:

* Low guilt: Minh tells Hoàng to trust Tâm.
* High guilt: Minh avoids answering clearly.
* Very high guilt + high Tâm-Minh relation: Hoàng realizes something.

---

## CHAPTER 15 — `yuuka_y03`

### Title: **Người đến sau, người ở lại trước**

**POV:** Yuuka
**Type:** core route
**Purpose:** Yuuka decides whether to fight, wait, or release Minh.

### Content

Festival week approaches. Yuuka is busy, shining in public, chaotic in private. She has achieved what younger Yuuka wanted: to be seen for her work, not just her beauty. But Minh remains the one person before whom she cannot fully perform.

This echoes Yuuka’s core wound: she wanted someone to see her beyond appearance, beyond “ánh mặt trời bất đắc dĩ.” 

### Choices

1. **Yuuka asks Minh for a real answer**

   ```renpy
   rel_minh_yuuka += 2
   tension_minh_yuuka += 1
   direction_minh_yuuka_reconcile possible
   ```

2. **Yuuka befriends Tâm**

   ```renpy
   trust_yuuka += 2
   tension_tam_yuuka -= 2
   unlock_choice_tam_yuuka_honest_talk = True
   ```

3. **Yuuka provokes Tâm**

   ```renpy
   tension_tam_yuuka += 2
   guilt_yuuka += 1
   ```

4. **Yuuka chooses dignity**

   ```renpy
   direction_minh_yuuka_parting = True
   yuuka_self_respect += 2
   ```

### Conditional Outcome

If:

```renpy
rel_minh_yuuka >= 5
trust_yuuka >= 3
guilt_minh <= 2
```

then unlock:

```renpy
yuuka_y04_reconcile
```

If:

```renpy
rel_tam_minh >= 5
direction_tam_minh_romance == True
```

then Yuuka route shifts to:

```renpy
yuuka_y04_let_go
```

---

## CHAPTER 16 — `minh_m03`

### Title: **Người không được phép muốn quá nhiều**

**POV:** Minh
**Type:** core
**Purpose:** Minh’s decisive internal chapter.

### Content

Minh is the hardest route because his choices affect too many people:

* Hoàng is his brother.
* Yuuka is his unresolved past.
* Tâm is possible present/future.
* Thiên An is a mirror of adult loneliness.
* His family history makes him responsible to the point of self-erasure.

His childhood/backstory supports this: he grew up with responsibility early, cared for Hoàng, and learned to be capable, controlled, emotionally restrained. 

### Choices

1. **Minh chooses Yuuka**
   Conditions:

   ```renpy
   rel_minh_yuuka >= 5
   direction_minh_yuuka_unresolved == True
   guilt_minh <= 3
   ```

   Effects:

   ```renpy
   direction_minh_yuuka_reconcile = True
   direction_tam_minh_romance = False
   ```

2. **Minh chooses distance from everyone**

   ```renpy
   direction_minh_solo = True
   guilt_minh += 1
   rel_minh_yuuka -= 1
   rel_tam_minh -= 1
   ```

3. **Minh admits feelings for Tâm**
   Conditions:

   ```renpy
   rel_tam_minh >= 5
   direction_tam_hoang_romance == False or trust_hoang <= 2
   direction_minh_yuuka_reconcile == False
   ```

   Effects:

   ```renpy
   direction_tam_minh_romance = True
   tension_tam_hoang += 3 if rel_tam_hoang > 2
   guilt_minh += 2
   ```

4. **Minh opens up to Thiên An**
   Conditions:

   ```renpy
   direction_thienan_minh_seed == True
   rel_thienan_minh >= 3
   direction_minh_yuuka_reconcile == False
   direction_tam_minh_romance == False
   ```

   Effects:

   ```renpy
   direction_thienan_minh_possible = True
   ```

---

## CHAPTER 17 — `tam_c17`

### Title: **Ngày dự án khép lại**

**POV:** Tâm
**Type:** core
**Purpose:** Career climax + emotional pre-ending.

### Content

Dự án công ty hoàn tất. Đây là nơi Tâm chứng minh mình đã lớn lên.

Nếu player đầu tư `tam_career`, Tâm có thể được giao lead một phần trình bày. Nếu không, cô vẫn hoàn thành vai trò nhưng ít tỏa sáng hơn.

### Routes Reflected

#### Tâm-Hoàng canon

Hoàng đến xem / đợi cô sau buổi tổng kết. Hai người nói chuyện thật. Không còn là Tâm đẩy, Hoàng né, mà là cả hai cùng chọn.

#### Tâm-Minh

Minh là người đánh giá dự án. Sự công nhận của anh khiến Tâm vui, nhưng cũng khiến cô phải tự hỏi: cô thích Minh vì anh nhìn thấy năng lực của cô, hay vì anh giống cơn mưa cũ cô chưa từng hiểu?

#### Hoàng-Huyền

Huyền và Hoàng có một scene nhẹ sau dự án. Tâm nhìn họ, thấy lòng mình không đau — nếu player chọn buông thật.

#### Huyền-Quân

Quân khen Huyền bằng một câu rất khó nghe như lời khen. Huyền hiểu, và lần đầu không cãi.

#### Thiên An

Thiên An xuất hiện / gọi điện chúc mừng. Quang ở bên cạnh cô. Hoặc không. Tùy route.

### Major Choice — Tâm chọn điều cần bảo vệ

1. **Bảo vệ tình yêu**

   ```renpy
   tam_courage += 1
   ending_priority_romance = True
   ```

2. **Bảo vệ tình bạn**

   ```renpy
   tam_empathy += 1
   ending_priority_friendship = True
   ```

3. **Bảo vệ chính mình**

   ```renpy
   tam_clarity += 2
   ending_priority_self = True
   ```

4. **Bảo vệ sự yên ổn**

   ```renpy
   tam_restraint += 2
   direction_doom_drift += possible
   ```

---

## CHAPTER 18 — `finale_c18`

### Title: **Tựa gió, tựa mây**

**POV:** Dynamic
**Type:** finale
**Purpose:** Ending resolver.

This chapter should be modular, not one fixed finale.

Structure:

1. Opening: Tâm returns to rain motif.
2. Route resolution scenes.
3. Final pair confirmation / separation.
4. Epilogue montage.
5. Ending title card.

---

# 5. Ending Conditions

## Ending 01 — Canon Ending: **Be True to Your Feelings**

Pairs:

* Tâm — Hoàng
* Minh — Yuuka
* Huyền — Quân
* Thiên An — Quang

Conditions:

```renpy
direction_tam_hoang_romance == True
rel_tam_hoang >= 7
trust_hoang >= 5
direction_minh_yuuka_reconcile == True
rel_minh_yuuka >= 7
direction_huyen_quan_romance == True
direction_thienan_quang_slowburn == True
```

Tone:

Ấm, trưởng thành, hơi nhiều dư vị. Không cần cưới hết. Chỉ cần ai cũng đã chọn đúng người, đúng cách.

---

## Ending 02 — Tâm — Minh: **Cơn mưa không thuộc về quá khứ**

Conditions:

```renpy
direction_tam_minh_romance == True
rel_tam_minh >= 7
direction_tam_hoang_romance == False or trust_hoang <= 2
direction_minh_yuuka_reconcile == False
```

Necessary emotional cost:

```renpy
guilt_tam >= 1
guilt_minh >= 2
```

This ending should not feel “clean”. It can be beautiful, but must carry a price.

Hoàng either:

* accepts and steps away maturely if `trust_hoang >= 4`,
* or cuts contact if `trust_hoang <= 2`.

---

## Ending 03 — Hoàng — Huyền: **Người ở cạnh lúc không ai diễn nữa**

Conditions:

```renpy
direction_hoang_huyen_romance == True
rel_hoang_huyen >= 7
rel_tam_huyen >= 5
direction_tam_hoang_romance == False
```

Tone:

Warm, witty, less poetic, more “hai người này cãi nhau cả đời chắc cũng vui”.

Tâm must actively bless them or at least not sabotage.

---

## Ending 04 — Minh — Yuuka Late Ending: **Không kết hôn cũng không rời xa**

Conditions:

```renpy
direction_minh_yuuka_parting == True
rel_minh_yuuka >= 6
yuuka_self_respect >= 3
guilt_minh <= 4
```

They do not immediately reconcile. Years later, they meet again. No wedding. No dramatic promise. Just two people finally old enough to stop forcing love into the shape society expects.

This ending is excellent for a bittersweet adult route.

---

## Ending 05 — Thiên An — Minh: **Hai người giỏi chịu đựng**

Conditions:

```renpy
direction_thienan_minh_possible == True
rel_thienan_minh >= 6
direction_minh_yuuka_reconcile == False
direction_tam_minh_romance == False
direction_thienan_quang_slowburn == False
```

Tone:

Quiet, mature, potentially controversial. It should feel less like passion and more like recognition: “người này hiểu sự mệt mỏi của mình mà không cần mình giải thích.”

Risk:

Quang’s route becomes tragic unless handled with dignity.

---

## Ending 06 — Thiên An — Quang: **Sáu năm không phải chờ vô ích**

Conditions:

```renpy
direction_thienan_quang_slowburn == True
rel_thienan_quang >= 7
family_pressure <= 5
```

Tone:

Elegant, adult, slow burn. Quang should not “win” because he waited long. He wins only if Thiên An finally sees him as a man, not as một người luôn ở đó.

---

## Ending 07 — Thiên An arranged marriage: **Một lựa chọn đúng trên giấy**

Conditions:

```renpy
direction_thienan_arranged == True
family_pressure >= 7
rel_thienan_quang < 5
rel_thienan_minh < 5
```

Tone:

Not villain ending. More like a life that looks stable but emotionally muted.

---

## Ending 08 — Minh Solo: **Người giữ cửa**

Conditions:

```renpy
direction_minh_solo == True
direction_minh_yuuka_reconcile == False
direction_tam_minh_romance == False
direction_thienan_minh_possible == False
```

Tone:

Minh chooses not to enter anyone’s life romantically. He remains important, respected, loved in some ways, but alone.

This ending should hurt quietly.

---

## Ending 09 — Yuuka Solo: **Ánh sáng tự chọn nơi chiếu xuống**

Conditions:

```renpy
direction_minh_yuuka_parting == True
yuuka_self_respect >= 5
direction_minh_yuuka_reconcile == False
```

Tone:

Yuuka leaves Vietnam with pain, but not defeat. She chooses herself, her film, her life.

---

## Ending 10 — Doom Ending: **Không ai kịp nói thật**

Conditions:

```renpy
trust_hoang <= 2
trust_minh <= 2
trust_yuuka <= 2
rel_tam_huyen <= 2
tam_clarity <= 2
guilt_tam >= 5
direction_doom_drift == True
```

Or triggered if player repeatedly chooses avoidance / silence / half-truth.

Result:

* Tâm and Hoàng drift apart.
* Minh closes himself again.
* Yuuka leaves.
* Huyền gives up interfering.
* Thiên An accepts a safe but loveless path or remains single.
* No main couple forms.

Tone:

Không bi kịch kiểu tai nạn, chết chóc. Chỉ là người ta bỏ lỡ nhau bằng những lần im lặng rất hợp lý. Tàn nhẫn hơn, mà rẻ hơn chi phí sản xuất CG.

---

# 6. Recommended Bonus / Extra Chapters

## `tam_bonus_rain_memory`

Unlock if:

```renpy
tam_intuition >= 3
```

Content: Tâm tìm lại ký ức cơn mưa.
Effect:

```renpy
choice_unlocks = ["ask_minh_about_rain"]
rel_tam_minh += 1
```

---

## `hoang_bonus_gift`

Unlock after Hoàng POV.

Mutual variants:

```renpy
hoang_bonus_gift_tam
hoang_bonus_gift_huyen
hoang_bonus_group_gift
```

Use same `exclusion_group = "hoang_gift_direction"`.

---

## `yuuka_bonus_private_talk`

Unlock if Tâm helps Yuuka or treats her kindly.

Content: Yuuka and Tâm speak honestly without Minh/Hoàng.
Effect:

```renpy
trust_yuuka += 2
tension_tam_yuuka -= 2
```

This is important to prevent Yuuka from becoming a cheap “rival woman”.

---

## `huyen_bonus_after_work`

Unlock after Chapter 11.

Content: Huyền decompresses with either Tâm, Hoàng, or Quân.
Branches:

* Tâm friendship repair.
* Hoàng-Huyền romance.
* Huyền-Quân canon.

---

## `thienan_bonus_six_years`

Unlock after Thiên An route starts.

Content: Quang’s six-year pursuit shown through restrained flashbacks.
Effect:

```renpy
rel_thienan_quang += 2
choice_unlocks = ["thienan_notice_quang"]
```

---

# 7. Suggested Chapter Metadata Skeleton

```python
CHAPTERS = {
    "tam_p00": {
        "id": "tam_p00",
        "route": "tam",
        "type": "core",
        "timeline_position": 0,
        "title": "Giấc mơ trong mưa",
        "label": "tam_p00",
        "prerequisites": [],
        "unlocks": ["tam_c01"],
    },

    "tam_c01": {
        "id": "tam_c01",
        "route": "tam",
        "type": "core",
        "timeline_position": 10,
        "title": "Ngày phỏng vấn và buổi tối ăn mừng",
        "label": "tam_c01",
        "prerequisites": ["tam_p00"],
        "unlocks": ["tam_c02"],
    },

    "tam_c02": {
        "id": "tam_c02",
        "route": "tam",
        "type": "core",
        "timeline_position": 20,
        "title": "Khoảng cách vừa đủ gần",
        "label": "tam_c02",
        "prerequisites": ["tam_c01"],
        "unlocks": ["tam_c03", "hoang_h01"],
    },

    "tam_c03": {
        "id": "tam_c03",
        "route": "tam",
        "type": "core",
        "timeline_position": 30,
        "title": "Chị gái không chịu hạnh phúc",
        "label": "tam_c03",
        "prerequisites": ["tam_c02"],
        "unlocks": ["tam_c05", "thienan_a01"],
    },

    "hoang_h01": {
        "id": "hoang_h01",
        "route": "hoang",
        "type": "pov",
        "timeline_position": 40,
        "title": "Người sống trong nhà của anh trai",
        "label": "hoang_h01",
        "prerequisites": ["tam_c02"],
        "unlocks": ["tam_c05"],
    },

    "tam_c05": {
        "id": "tam_c05",
        "route": "tam",
        "type": "core",
        "timeline_position": 50,
        "title": "Buổi hẹn đặc biệt ngày Chủ Nhật",
        "label": "tam_c05",
        "prerequisites": ["tam_c03"],
        "unlocks": ["tam_c06"],
    },

    "tam_c06": {
        "id": "tam_c06",
        "route": "tam",
        "type": "core",
        "timeline_position": 60,
        "title": "Người anh trai trở về",
        "label": "tam_c06",
        "prerequisites": ["tam_c05"],
        "unlocks": ["tam_c07", "minh_m01"],
    },

    "tam_c07": {
        "id": "tam_c07",
        "route": "tam",
        "type": "core",
        "timeline_position": 70,
        "title": "Một người khó đọc",
        "label": "tam_c07",
        "prerequisites": ["tam_c06"],
        "exclusion_group": "chapter_07_pov",
        "excludes": ["minh_m01"],
        "unlocks": ["yuuka_y01"],
    },

    "minh_m01": {
        "id": "minh_m01",
        "route": "minh",
        "type": "pov",
        "timeline_position": 71,
        "title": "Người giống một cơn mưa cũ",
        "label": "minh_m01",
        "prerequisites": ["tam_c06"],
        "exclusion_group": "chapter_07_pov",
        "excludes": ["tam_c07"],
        "unlocks": ["yuuka_y01"],
    },

    "yuuka_y01": {
        "id": "yuuka_y01",
        "route": "yuuka",
        "type": "core",
        "timeline_position": 80,
        "title": "Cô gái từ sân bay",
        "label": "yuuka_y01",
        "prerequisites": ["tam_c06"],
        "unlocks": ["tam_c09", "minh_m02", "yuuka_y02"],
    },

    "tam_c09": {
        "id": "tam_c09",
        "route": "tam",
        "type": "core",
        "timeline_position": 90,
        "title": "Bàn ăn có quá nhiều điều chưa nói",
        "label": "tam_c09",
        "prerequisites": ["yuuka_y01"],
        "unlocks": ["tam_c13", "huyen_h01"],
    },

    "huyen_h01": {
        "id": "huyen_h01",
        "route": "huyen",
        "type": "pov",
        "timeline_position": 110,
        "title": "Trưởng phòng khó tính và cô gái không chịu lép vế",
        "label": "huyen_h01",
        "prerequisites": ["tam_c09"],
        "unlocks": ["tam_c13"],
    },

    "thienan_a01": {
        "id": "thienan_a01",
        "route": "thienan",
        "type": "pov",
        "timeline_position": 115,
        "title": "Người phụ nữ không cần được cứu",
        "label": "thienan_a01",
        "prerequisites": ["tam_c03"],
        "unlocks": ["tam_c13"],
    },

    "tam_c13": {
        "id": "tam_c13",
        "route": "tam",
        "type": "core",
        "timeline_position": 130,
        "title": "Tin đồn",
        "label": "tam_c13",
        "prerequisites": ["tam_c09"],
        "unlocks": ["hoang_h02", "yuuka_y03", "minh_m03", "tam_c17"],
    },

    "tam_c17": {
        "id": "tam_c17",
        "route": "tam",
        "type": "core",
        "timeline_position": 170,
        "title": "Ngày dự án khép lại",
        "label": "tam_c17",
        "prerequisites": ["tam_c13"],
        "unlocks": ["finale_c18"],
    },

    "finale_c18": {
        "id": "finale_c18",
        "route": "finale",
        "type": "core",
        "timeline_position": 180,
        "title": "Tựa gió, tựa mây",
        "label": "finale_c18",
        "prerequisites": ["tam_c17"],
        "unlocks": [],
    },
}
```

---

# 8. Important Design Notes

## 8.1. Không nên cho Tâm-Minh quá dễ thắng

Tâm-Minh là route hấp dẫn, nhưng nếu mở quá dễ sẽ phá canon và làm Hoàng thành “starter boyfriend”. Nên yêu cầu:

```renpy
rel_tam_minh high
tam_clarity high
trust_hoang low OR no Tâm-Hoàng romance
direction_minh_yuuka_reconcile == False
```

Nếu Tâm đang yêu Hoàng mà vẫn theo Minh, ending phải có guilt cost.

## 8.2. Yuuka không được bị viết như tình địch rẻ tiền

Yuuka nên là nhân vật có dignity. Cô có quyền ích kỷ, có quyền đau, có quyền muốn Minh trở lại, nhưng không nên biến thành người phá hoại trẻ con.

Route đẹp nhất của Yuuka có hai hướng:

* Reconcile with Minh.
* Let go and become whole.

Cả hai đều mạnh.

## 8.3. Huyền cần agency riêng

Nếu Huyền chỉ là “bạn thân để Tâm tâm sự” thì phí. Huyền nên có 3 vai:

* Mirror của Tâm.
* Possible partner của Hoàng.
* Canon slowburn với Quân.

Huyền-Hoàng nên là nhánh “ấm và hợp”, nhưng Huyền-Quân mới là nhánh “va chạm để trưởng thành”.

## 8.4. Thiên An route nên trưởng thành hơn các route khác

Thiên An không nên có route quá teen. Cô là người đã mệt với việc được người khác đánh giá là “tốt để cưới”. Vì vậy route của cô nên xoay quanh:

* Tự do lựa chọn.
* Áp lực gia đình.
* Sự kiên nhẫn của Quang.
* Sự đồng cảm nguy hiểm với Minh.
* Khả năng sống độc thân mà không bị xem là thất bại.

## 8.5. Doom Ending phải công bằng

Doom Ending không nên là “bad ending vì chọn sai đáp án”. Nó nên là kết quả của:

* Né tránh quá nhiều.
* Không nói thật.
* Không đủ trust.
* Không đủ clarity.
* Ưu tiên yên ổn trước mắt đến mức đánh mất tất cả.

Nói cách khác: không ai ác. Chỉ là ai cũng im lặng hơi đúng lúc. Và thế là xong.
