# FILE: game/story/tam/tam_c04_between_work_and_hearts/s80_w13_friday_departures.rpy

label tam_c04_w13_s05_friday_departures:
    scene bg_company_open_office_day
    with fade
    scene cg_tam_c04_tam_work_evening
    with dissolve
    "Thứ Sáu, ba lịch trình cùng mở ra trên màn hình Tâm."
    scene bg_company_open_office_day
    with dissolve
    "Máy bay của Thiên An và Quang cất cánh lúc sáu giờ. Hoàng giữ bàn lúc bảy giờ. Huyền gửi ảnh một chiếc ba lô trẻ con đặt trên ghế phụ."
    menu:
        "Nhắn Hoàng rằng Tâm sẽ đến đúng giờ":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_flag("tam_c04_w13_priority_hoang")
        "Nhắn Quang khi máy bay hạ cánh phải báo":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 5)
            $ tam_c04_add_extended_score("quang_tam_awareness", 3)
            $ story_flag("tam_c04_w13_priority_quang")
        "Gọi Huyền hỏi Ánh Nhi có chịu ăn không":
            $ story_add("huyen_quan_trust", 5)
            $ story_add("career_huyen", 3)
            $ story_flag("tam_c04_w13_priority_huyen_anhni")
        "Tắt điện thoại và hoàn thành bản dự toán":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_c04_w13_priority_career")
    return
