# FILE: game/story/tam/tam_c04_between_work_and_hearts/s31_w05_friday_new_month_priority.rpy
# Week 05 — First priority choice of Month 02.

label tam_c04_w05_s06_friday_new_month_priority:
    scene bg_company_open_office_day
    with dissolve

    "Thứ Sáu, sáu giờ mười bảy."

    "Huyền đang sửa biên bản cuộc họp."

    "Hoàng vừa gửi lại địa chỉ nhà anh."

    "Quang nhắn rằng Thiên An đã đồng ý xem lịch làm việc mới."

    "Brief của Tâm còn một mục chưa chốt."

    menu:
        "Xác nhận cuối tuần sẽ đến nhà Hoàng":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_sub("tam_insecurity", 3)
            $ story_add("career_huyen", 3)
            $ story_add("huyen_quan_trust", 3)
            $ story_add("thienan_quang_trust", 3)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 3)
            $ story_add_direction("tam", "tam_hoang_open")
            $ story_flag("tam_c04_w05_focus_hoang")

        "Ngồi lại review chéo với Huyền":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 5)
            $ story_add("huyen_quan_trust", 3)
            $ story_add_direction("tam", "tam_support_huyen")
            $ story_flag("tam_c04_w05_focus_huyen")

        "Để Huyền tự gửi biên bản cho Quân":
            $ story_add("career_huyen", 5)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 3)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w05_focus_huyen_quan")

        "Nhắn Quang rằng lần sau đừng mang Tâm ra làm cớ":
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_add_direction("quang", "quang_thienan_open")
            $ story_add_direction("thienan", "thienan_quang_open")
            $ story_flag("tam_c04_w05_focus_quang_thienan")

        "Hỏi Quang cốc của Tâm là tiện đường thật hay không":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 3)
            $ tam_c04_add_extended_score("quang_tam_awareness", 5)
            $ story_add_direction("quang", "quang_tam_open")
            $ story_flag("tam_c04_w05_focus_quang_personal")

        "Chốt mục cuối trong brief của mình":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_add("tam_observation", 3)
            $ story_add_direction("tam", "tam_career_focus")
            $ story_flag("tam_c04_w05_focus_career")

    "Tâm chọn một cửa sổ trên màn hình."

    "Những cửa sổ còn lại không biến mất. Chúng chỉ nằm xuống thanh tác vụ, chờ lần mở tiếp theo."

    return
