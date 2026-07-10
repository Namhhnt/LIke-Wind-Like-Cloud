# Chapter 04 — Month 01 Route Recommendations (v1.5)

## Calculation assumptions

Scores are calculated from the current Month 01 package only:

- Weekday story scenes from Week 01–04
- One reply per available phone thread
- Hoàng social likes when they eventually unlock
- No weekend interactive-map actions
- No bonus score from future Month 02 content

Baseline used for the final-value column:

```text
tam_hoang_interest = 35
hoang_tam_trust = 35
tam_insecurity = 35

tam_quang_interest = 0
quang_tam_warmth = 35
quang_tam_awareness = 0

thienan_quang_trust = 35
quang_persistence = 60
quang_thienan_resolve = 35

huyen_quan_trust = 10
huyen_quan_interest = 0

career_tam = 15
career_huyen = 15
```

Career values are XP earned in the current career level. When the existing career system promotes a character, the level and salary become the source of truth and the current score may reset.

---

# Route A — Hoàng + Thiên An focus

Primary: Tâm–Hoàng  
Secondary: Quang–Thiên An  
Career posture: Tâm keeps enough independent work ownership to avoid becoming only a relationship mediator.

## Recommended choices

### Week 01

- Dựng khung trước rồi để Huyền bổ sung dữ liệu
- Nhận phần sửa về mình để cuộc họp kết thúc sớm
- Khuyên Quang tự mang hồ sơ tới cho Thiên An
- Trả lời Hoàng trước
- Phone Hoàng: “Còn anh thì ăn chưa?”
- Phone Quang: “Anh lo thì tự gọi chị ấy đi.”

### Week 02

- Ở lại nói chuyện với Hoàng thêm một lúc
- Bổ sung để cả hai cùng được ghi nhận
- Không làm người trung gian nữa
- Tâm trả lời và tự chịu phần phản biện
- Nhận lời ăn sáng với Hoàng
- Phone Hoàng: nhận hộp bánh
- Phone Quang: khuyến khích anh tiếp tục hỏi trực tiếp

### Week 03

- Tâm nhận phần phản biện
- Đổi kế hoạch thành một bữa ăn ngắn gần công ty
- Cùng Huyền bổ sung bằng chứng
- Để Quang tự quyết định có chờ hay không
- Nhắn Hoàng ghé qua, dù chỉ gặp một lúc
- Phone Hoàng: xác nhận kế hoạch cụ thể
- Phone Quang: chuyển anh về đúng phần việc với Thiên An

### Week 04

- Nhận một phần việc độc lập trong tháng sau
- Nói rằng Tâm thích cách Hoàng rủ lần này hơn
- Không chen vào cuộc đối đáp của Quang và Thiên An
- Ngồi xuống chia outline với Huyền
- Xác nhận kế hoạch cuối tuần với Hoàng
- Phone Hoàng: xác nhận giờ hẹn
- Phone Quang: nhắc anh trả lời Thiên An đúng lúc
- Like các post Hoàng khi chúng mở khóa

## Score result

| Score | Gain | Final from baseline |
|---|---:|---:|
| `tam_hoang_interest` | +43 | 78 |
| `hoang_tam_trust` | +39 | 74 |
| `tam_insecurity` | -17 | 18 |
| `thienan_quang_trust` | +36 | 71 |
| `quang_persistence` | +30 | 90 |
| `quang_thienan_resolve` | +36 | 71 |
| `career_tam` | +55 XP | 70 before any promotion reset |
| `career_huyen` | +27 XP | 42 |

This build produces both `tam_c04_m01_hoang_strong` and `tam_c04_m01_quang_thienan_progressing` without creating a Tâm–Quang personal seed.

---

# Route B — Hoàng + Huyền–Quân focus

Primary: Tâm–Hoàng  
Secondary: Huyền–Quân  
Career posture: Tâm gives Huyền room, but still performs one shared-work choice so her own career does not remain completely static.

## Recommended choices

### Week 01

- Cùng Huyền chia lại toàn bộ tài liệu
- Để Huyền tự trả lời Quân
- Nhận hồ sơ và chuyển giúp Quang
- Trả lời Hoàng trước
- Phone Huyền: trêu việc cô nhớ giờ gửi mail của Quân
- Phone Hoàng: hỏi anh đã ăn chưa

### Week 02

- Ở lại nói chuyện với Hoàng thêm một lúc
- Để khoảnh khắc được công nhận thuộc về Huyền
- Không làm người trung gian cho Quang nữa
- Để Huyền trả lời phần cô ấy hiểu rõ nhất
- Chỉ góp ý một lần rồi để Huyền tự chốt với Quân
- Phone Huyền: để cô tự kiểm nghiệm dự đoán
- Phone Hoàng: nhận hộp bánh

### Week 03

- Để Huyền trả lời phần cô ấy đã chuẩn bị
- Đổi kế hoạch thành một bữa ăn ngắn gần công ty
- Để Huyền tự chốt và nhìn phản ứng của Quân
- Để Quang tự quyết định có chờ hay không
- Nhắn Hoàng ghé qua, dù chỉ gặp một lúc
- Phone Huyền: để cô tự đối diện câu hỏi thứ tư
- Phone Hoàng: xác nhận kế hoạch cụ thể

### Week 04

- Để Huyền nhận phần đối ngoại dưới sự review của Quân
- Nói rằng Tâm thích cách Hoàng rủ lần này hơn
- Không chen vào Quang–Thiên An
- Hỏi Huyền có vui vì được Quân tin không
- Để Huyền tự gửi outline cho Quân
- Phone Huyền: hỏi cô lo review hay lo người review
- Phone Hoàng: xác nhận giờ hẹn
- Like các post Hoàng khi chúng mở khóa

## Score result

| Score | Gain | Final from baseline |
|---|---:|---:|
| `tam_hoang_interest` | +33 | 68 |
| `hoang_tam_trust` | +29 | 64 |
| `tam_insecurity` | -11 | 24 |
| `huyen_quan_trust` | +55 | 65 |
| `huyen_quan_interest` | +13 | 13 |
| `career_huyen` | +53 XP | 68 before any promotion reset |
| `career_tam` | +5 XP | 20 |
| `thienan_quang_trust` | +29 | 64 |
| `quang_thienan_resolve` | +27 | 62 |

Hoàng still reaches the strong Month 01 snapshot. Huyền–Quân gains both professional trust and the first personal-interest seed. Quang–Thiên An continues off-screen but is not framed as the selected secondary route.

---

# Route C — Quang + Huyền–Quân focus

Primary: Tâm–Quang  
Secondary: Huyền–Quân  
Career posture: Tâm keeps one shared assignment; Huyền owns most visible career moments.

## Recommended choices

### Week 01

- Cùng Huyền chia lại toàn bộ tài liệu
- Để Huyền tự trả lời Quân
- Trêu Quang vì vẫn vòng qua Tâm để hỏi Thiên An
- Lùi lại để Huyền tự làm việc với Quân
- Phone Huyền: trêu việc cô nhớ giờ gửi mail
- Phone Quang: tính phí vì anh luôn vòng qua Tâm

### Week 02

- Hoàng scene is skipped naturally if his route was not built earlier
- Để khoảnh khắc được công nhận thuộc về Huyền
- Chụp chiếc nắp bị lệch và trêu Quang
- Để Huyền trả lời phần cô ấy hiểu rõ nhất
- Trêu Quang về chiếc nắp lệch lần trước
- Phone Huyền: để cô tự kiểm nghiệm dự đoán
- Phone Quang: hỏi vì sao anh nhớ chính xác bốn phút

### Week 03

- Để Huyền trả lời phần cô ấy đã chuẩn bị
- Để Huyền tự chốt và nhìn phản ứng của Quân
- Nhận chiếc ô và hỏi vì sao Quang vẫn nhớ cách Tâm buộc
- Hỏi Quang có mang trả chiếc ô chỉ để gặp Tâm không
- Phone Huyền: để cô tự đối diện câu hỏi thứ tư
- Phone Quang: bảo anh mang chiếc ô qua

### Week 04

- Để Huyền nhận phần đối ngoại dưới sự review của Quân
- Nhận ra Quang cũng luôn nhớ phần của Tâm
- Hỏi Huyền có vui vì được Quân tin không
- Hỏi Quang khi nào anh định trả lời câu hỏi về chiếc ô
- Phone Huyền: hỏi cô lo review hay lo người review
- Phone Quang: cho anh thời gian trả lời

## Score result

| Score | Gain | Final from baseline |
|---|---:|---:|
| `tam_quang_interest` | +39 | 39 |
| `quang_tam_warmth` | +26 | 61 |
| `quang_tam_awareness` | +29 | 29 |
| `huyen_quan_trust` | +44 | 54 |
| `huyen_quan_interest` | +9 | 9 |
| `career_huyen` | +51 XP | 66 before any promotion reset |
| `career_tam` | +5 XP | 20 |
| `thienan_quang_trust` | +3 | 38 |
| `quang_thienan_resolve` | +3 | 38 |

This build deliberately keeps Quang–Thiên An below the progressing threshold and produces `tam_c04_m01_quang_tam_personal_seed`. It avoids the old ambiguity where only Tâm's interest changed while Quang had no mirrored state.

---

# Route D — Thiên An + Huyền–Quân focus

Primary: Quang–Thiên An  
Secondary: Huyền–Quân  
Tâm romance posture: neutral; she stops acting as a permanent middle person for both pairs.

## Recommended choices

### Week 01

- Cùng Huyền chia lại toàn bộ tài liệu
- Để Huyền tự trả lời Quân
- Khuyên Quang tự mang hồ sơ tới Thiên An
- Nhắn Quang, bảo anh đừng vòng qua Tâm nữa
- Phone Huyền: trêu việc cô nhớ giờ gửi mail
- Phone Quang: bảo anh tự gọi Thiên An

### Week 02

- Để khoảnh khắc được công nhận thuộc về Huyền
- Không làm người trung gian nữa
- Để Huyền trả lời phần cô ấy hiểu rõ nhất
- Chỉ góp ý một lần rồi để Huyền tự chốt với Quân
- Phone Huyền: để cô tự kiểm nghiệm dự đoán
- Phone Quang: khuyến khích anh tiếp tục hỏi trực tiếp

### Week 03

- Để Huyền trả lời phần cô ấy đã chuẩn bị
- Để Huyền tự chốt và nhìn phản ứng của Quân
- Để Quang tự quyết định có chờ hay không
- Nhắc Quang chuẩn bị cho lịch công tác của Thiên An
- Phone Huyền: để cô tự đối diện câu hỏi thứ tư
- Phone Quang: chuyển chiếc ô đi cùng hồ sơ của Thiên An

### Week 04

- Để Huyền nhận phần đối ngoại dưới sự review của Quân
- Không chen vào cuộc đối đáp của Quang và Thiên An
- Hỏi Huyền có vui vì được Quân tin không
- Để Huyền tự gửi outline cho Quân
- Phone Huyền: hỏi cô lo review hay lo người review
- Phone Quang: nhắc anh trả lời Thiên An đúng lúc

## Score result

| Score | Gain | Final from baseline |
|---|---:|---:|
| `thienan_quang_trust` | +40 | 75 |
| `quang_persistence` | +40 | 100, clamped |
| `quang_thienan_resolve` | +40 | 75 |
| `huyen_quan_trust` | +52 | 62 |
| `huyen_quan_interest` | +13 | 13 |
| `career_huyen` | +53 XP | 68 before any promotion reset |
| `career_tam` | +5 XP | 20 |
| `tam_quang_interest` | +0 | 0 |
| `quang_tam_awareness` | +0 | 0 |

This is the cleanest support route: both side couples progress, while Tâm does not accidentally seed a personal Quang route.

---

## Optional career-maintenance swap

For Routes B–D, Tâm's weekday career gain is intentionally low because she repeatedly gives ownership to Huyền. Weekend map actions should be the main compensation.

If the player wants more weekday career XP without materially breaking the route, replace one Huyền-facing choice with:

- `Dựng khung trước rồi để Huyền bổ sung dữ liệu` — `career_tam +5`
- `Hai người phối hợp trả lời` — `career_tam +5`, `career_huyen +5`
- `Đề nghị Tâm và Huyền tiếp tục đi cùng nhưng chia ownership rõ` — `career_tam +5`, `career_huyen +5`

Each swap costs a small amount of direct Huyền–Quân trust/interest, so it should be treated as career maintenance rather than a free bonus.
