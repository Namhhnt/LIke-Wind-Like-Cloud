# FILE: game/story/tam/tam_c04_between_work_and_hearts/s37_w06_friday_absence_priority.rpy
# Week 06 — Friday priority after the week of an empty chair.

label tam_c04_w06_s06_friday_absence_priority:
    scene bg_company_open_office_day
    with dissolve

    scene cg_tam_c04_tam_work_evening
    with dissolve
    "Thứ Sáu, Quân đã trở lại."
    scene bg_company_open_office_day
    with dissolve

    "Chiếc ghế không còn trống. Huyền không nhìn sang đó lần nào trong mười phút đầu."

    "Đến phút thứ mười một, Quân gửi lại tài liệu với đúng một comment."

    huyen neutral "Ổng chỉ sửa một chỗ."

    tam teasing "Mày thất vọng à?"

    huyen irritated "Tao đang đánh giá chất lượng review."

    menu:
        "Trêu Huyền rằng cô đã quen có Quân ở đó":
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 5)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w06_focus_huyen_quan")

            tam teasing "Hai ngày không có người khoanh đỏ, mày buồn nhỉ."

            huyen neutral "Tao buồn vì không ai chịu trách nhiệm cho tiêu chuẩn."

            tam smile "Ừ."

        "Cùng Huyền chốt hai phần việc trước cuối tuần":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 5)
            $ story_add("tam_self_clarity", 3)
            $ story_flag("tam_c04_w06_focus_huyen")

        "Nhắn Hoàng cảm ơn vì chiếc ghế":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_sub("tam_insecurity", 3)
            $ story_add_direction("tam", "tam_hoang_open")
            $ story_flag("tam_c04_w06_focus_hoang")

        "Nhắn Quang rằng anh nên tự mang hồ sơ tới Thiên An":
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_add_direction("quang", "quang_thienan_open")
            $ story_flag("tam_c04_w06_focus_quang_thienan")

        "Hỏi Quang vì sao anh nhớ chiếc ngăn kéo":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 3)
            $ tam_c04_add_extended_score("quang_tam_awareness", 5)
            $ story_add_direction("quang", "quang_tam_open")
            $ story_flag("tam_c04_w06_focus_quang_personal")

        "Gửi quyết định scope change cho Quân":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_add("tam_observation", 3)
            $ story_add_direction("tam", "tam_career_focus")
            $ story_flag("tam_c04_w06_focus_career")

    "Ngoài cửa kính, trời bắt đầu mưa nhẹ."

    "Huyền đóng tài liệu, nhưng vẫn để cửa sổ chat với Quân mở ở góc màn hình."

    return
