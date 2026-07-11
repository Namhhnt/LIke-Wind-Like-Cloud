label tam_c04_w11_s06_friday_one_real_answer:
    scene bg_company_open_office_day
    with dissolve
    "Thứ Sáu, bảy giờ lẻ hai."
    "Tâm có thể tiếp tục trả lời nửa câu cho nhiều người, hoặc trả lời trọn một câu cho một người."
    menu:
        "Giữ tối thứ Sáu cho Hoàng như một lịch thật":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_sub("tam_insecurity", 3)
            $ story_flag("tam_c04_w11_focus_hoang")
        "Để Huyền mang file đã sửa sang bàn Quân":
            $ story_add("career_huyen", 5)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 5)
            $ story_flag("tam_c04_w11_focus_huyen_quan")
        "Ở lại cùng Huyền kiểm tra phần còn lại":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 5)
            $ story_flag("tam_c04_w11_focus_huyen")
        "Nói rõ với Thiên An rằng Tâm sẽ không dịch hộ Quang":
            $ story_add("thienan_quang_trust", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_add("quang_persistence", 5)
            $ story_flag("tam_c04_w11_focus_quang_thienan")
        "Nhắn Quang rằng Tâm cần một câu trả lời không vòng qua Thiên An":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_awareness", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 3)
            $ story_flag("tam_c04_w11_focus_quang_personal")
        "Sửa decision log và ghi rõ lỗi của chính Tâm":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_add("tam_observation", 3)
            $ story_flag("tam_c04_w11_focus_career")
    "Tâm nhấn gửi."
    "Một câu trả lời thật không giải quyết tất cả. Nó chỉ khiến những câu còn lại khó giả vờ hơn."
    return
