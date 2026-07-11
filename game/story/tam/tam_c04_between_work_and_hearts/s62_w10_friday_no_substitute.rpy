label tam_c04_w10_s06_friday_no_substitute:
    scene bg_company_open_office_day
    with dissolve
    "Thứ Sáu, sáu giờ hai mươi sáu."
    "Một lịch hẹn cần đặt lại. Một cánh cửa đã được tôn trọng. Một file còn chờ review."
    menu:
        "Đặt lại lịch với Hoàng bằng một giờ cụ thể":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_sub("tam_insecurity", 3)
            $ story_flag("tam_c04_w10_focus_hoang")
        "Để Huyền gửi bản cuối cho Quân một mình":
            $ story_add("career_huyen", 5)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 5)
            $ story_flag("tam_c04_w10_focus_huyen_quan")
        "Review chéo với Huyền trước khi cả hai về":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 5)
            $ story_flag("tam_c04_w10_focus_huyen")
        "Không nhắn thay Quang cho Thiên An":
            $ story_add("thienan_quang_trust", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_add("quang_persistence", 5)
            $ story_flag("tam_c04_w10_focus_quang_thienan")
        "Hỏi Quang đã về đến nhà chưa":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 5)
            $ tam_c04_add_extended_score("quang_tam_awareness", 3)
            $ story_flag("tam_c04_w10_focus_quang_personal")
        "Hoàn tất báo cáo incident của Tâm":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_c04_w10_focus_career")
    "Tâm gửi một tin, hoặc một file."
    "Không ai có thể làm thay phần đó mà kết quả vẫn giống nhau."
    return
