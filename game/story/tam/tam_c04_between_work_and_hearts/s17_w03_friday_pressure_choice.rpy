# FILE: game/story/tam/tam_c04_between_work_and_hearts/s17_w03_friday_pressure_choice.rpy
# Week 03 — Priority choice under actual pressure, not empty free time.

label tam_c04_w03_s06_friday_pressure_choice:
    scene bg_company_open_office_day
    with dissolve

    scene cg_tam_c04_tam_work_evening
    with dissolve
    "Thứ Sáu, sáu giờ ba mươi sáu phút."
    scene bg_company_open_office_day
    with dissolve

    "Bản họp khách đã được gửi. Nhưng việc xong không làm tuần nhẹ lại ngay."

    "Huyền muốn kiểm tra thêm một bảng trước khi về. Quân đang ở phòng họp, chờ phần giải trình cuối."

    "Hoàng nhắn rằng anh đi ngang qua khu này, không nói mình có định ghé hay không."

    "Quang báo Thiên An vừa nhận thêm lịch công tác vào tuần sau."

    "Trong email, Quân giao Tâm chuẩn bị đề xuất cho một phần việc có thể tách riêng khỏi Huyền."

    "Không còn lựa chọn nào hoàn toàn nhẹ."

    menu:
        "Nhắn Hoàng ghé qua, dù chỉ gặp một lúc":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_add("tam_self_clarity", 3)
            $ story_add("huyen_quan_trust", 3)
            $ story_add("career_huyen", 3)
            $ story_add("thienan_quang_trust", 3)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 3)
            $ story_add_direction("tam", "tam_hoang_open")
            $ story_flag("tam_c04_w03_focus_hoang")

            tam "Nếu anh đang gần đây thì ghé đi. Em còn khoảng hai mươi phút."

            hoang "Hai mươi phút cũng là một kế hoạch."

            "Tâm đọc câu trả lời, khóe miệng dịu xuống."

        "Ở lại chốt bảng cùng Huyền":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_add("hoang_self_acceptance", 3)
            $ story_add("thienan_quang_trust", 3)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 3)
            $ story_add_direction("tam", "tam_support_huyen")
            $ story_flag("tam_c04_w03_focus_huyen")

            tam neutral "Mở bảng đi. Tao kiểm phần thay đổi, mày kiểm lý do."

            huyen neutral "Mày không về à?"

            tam teasing "Tao đang cố để thứ Hai không có thêm một bài đăng bi kịch của mày."

        "Để Huyền tự mang phần giải trình vào cho Quân":
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 2)
            $ story_add("career_huyen", 5)
            $ story_add("tam_observation", 5)
            $ story_add("hoang_self_acceptance", 3)
            $ story_add("thienan_quang_trust", 3)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 3)
            $ story_flag("tam_c04_w03_focus_huyen_quan")
            $ story_flag("tam_c04_w03_tam_steps_back_under_pressure")

            tam neutral "Phần đó là lập luận của mày. Mày tự trình bày đi."

            huyen tired "Mày có niềm tin vào tao hơi đúng lúc đáng ghét."

            tam smile "Tao biết."

            "Huyền cầm laptop đi về phía phòng họp. Bước chân vẫn nhanh, nhưng không còn chần chừ ở cửa."

        "Nhắc Quang chuẩn bị cho lịch công tác của Thiên An":
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_add("career_huyen", 3)
            $ story_add_direction("tam", "tam_support_quang_thienan")
            $ story_flag("tam_c04_w03_focus_quang_thienan")

            tam "Chị An đi tuần sau. Anh đừng đợi tới tối trước ngày đi mới hỏi chị ấy cần gì."

            quang "Anh đã xin lịch trình rồi."

            tam teasing "Tiến bộ nhanh vậy?"

            quang "Có người than làm tổng đài mệt."

        "Hỏi Quang có mang trả chiếc ô chỉ để gặp Tâm không":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 3)
            $ tam_c04_add_extended_score("quang_tam_awareness", 5)
            $ story_add("tam_observation", 5)
            $ story_add("quang_persistence", 3)
            $ story_add_direction("quang", "quang_tam_open")
            $ story_flag("quang_tam_old_habit_reframed")
            $ story_add("career_huyen", 3)
            $ story_flag("tam_c04_w03_focus_quang_personal")

            tam "Hôm qua anh mang ô qua vì tiện thật à?"

            "Tin nhắn được xem gần như ngay lập tức."

            quang "Em muốn nghe câu trả lời nào?"

            tam teasing "Câu thật."

            "Ba dấu chấm hiện lên khá lâu."

            quang "Anh chưa nghĩ xong cách nói."

        "Nhận phần việc độc lập Quân vừa giao":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_add("tam_observation", 3)
            $ story_add("huyen_quan_trust", 3)
            $ story_add("career_huyen", 3)
            $ story_add("hoang_self_acceptance", 3)
            $ story_add("thienan_quang_trust", 3)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 3)
            $ story_add_direction("tam", "tam_career_focus")
            $ story_flag("tam_c04_w03_focus_career")

            "Tâm mở email, trả lời rằng cô nhận phần đề xuất."

            "Không copy Huyền. Không hỏi trước xem mình có làm được không."

            "Sau khi gửi, cô mới nhận ra vai mình đã thẳng hơn một chút."

    "Tâm thu dọn bàn."

    "Ba tuần chưa đủ để một người trở thành quan trọng."

    "Nhưng đủ để sự vắng mặt của họ bắt đầu có hình dạng."

    return
