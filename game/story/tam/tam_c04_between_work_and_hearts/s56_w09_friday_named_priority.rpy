# Week 09 — Weekly priority after route privileges become visible.
label tam_c04_w09_s06_friday_named_priority:
    scene bg_company_open_office_day
    with dissolve
    "Thứ Sáu, sáu giờ bốn mươi."
    "Hoàng đã để một chỗ. Huyền vừa gửi file không cần sửa. Quang vẫn còn một tin nhắn gửi nhầm. Đầu việc của Tâm chờ quyết định cuối."
    menu:
        "Báo Hoàng giờ Tâm sẽ đến, không để anh tự đoán":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_sub("tam_insecurity", 3)
            $ story_add_direction("tam", "tam_hoang_open")
            $ story_flag("tam_c04_w09_focus_hoang")
        "Để Huyền tự theo dõi phản hồi cùng Quân":
            $ story_add("career_huyen", 5)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 5)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w09_focus_huyen_quan")
        "Gửi Huyền checklist review chéo":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 5)
            $ story_flag("tam_c04_w09_focus_huyen")
        "Bảo Quang sửa đúng người nhận":
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_flag("tam_c04_w09_focus_quang_thienan")
        "Hỏi Quang câu anh chưa trả lời":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 3)
            $ tam_c04_add_extended_score("quang_tam_awareness", 5)
            $ story_flag("tam_c04_w09_focus_quang_personal")
        "Chốt decision log của riêng Tâm":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_add("tam_observation", 3)
            $ story_flag("tam_c04_w09_focus_career")
    "Tâm chọn việc mình sẽ trả lời trước."
    "Lần này, những việc còn lại đã có người nhận ra mình bị để sau."
    return
