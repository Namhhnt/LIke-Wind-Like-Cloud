# FILE: game/story/tam/tam_c04_between_work_and_hearts/s77_w13_south_assignment.rpy

label tam_c04_w13_s02_south_assignment:
    scene bg_meeting_room_day
    with dissolve
    "Thiên An đặt tập hồ sơ chi nhánh miền Nam xuống bàn."
    thienan neutral "Ít nhất ba tuần. Có thể lâu hơn."
    quang "Anh đi cùng."
    thienan neutral "Tôi chưa hỏi."
    quang "Anh biết."
    "Tâm nhìn chiếc vé điện tử trên màn hình của Quang. Anh đã đặt chỗ từ tối qua."
    menu:
        "Bảo Quang đừng tiếp tục vòng qua Tâm":
            $ story_add("thienan_quang_trust", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_flag("tam_c04_w13_quang_goes_for_thienan")
            tam neutral "Lần này anh đi vì chị ấy thì nói với chị ấy. Đừng nhìn em."
            quang "Ừ."
            "Quang quay sang Thiên An."
            quang "Anh muốn đi cùng em."
        "Hỏi Quang có định báo Tâm trước khi đi không":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 5)
            $ tam_c04_add_extended_score("quang_tam_awareness", 5)
            $ story_flag("tam_c04_w13_tam_asks_quang_to_report")
            tam neutral "Còn em thì anh định để tới lúc thấy ảnh sân bay mới biết à?"
            quang "Anh định tối nay nói."
            tam neutral "Muộn rồi."
        "Chỉ hỏi ngày trở về":
            $ story_add("tam_observation", 5)
            $ story_add("thienan_quang_trust", 3)
            $ tam_c04_add_extended_score("quang_tam_warmth", 3)
            $ story_flag("tam_c04_w13_tam_asks_return_date")
            tam neutral "Ngày về?"
            thienan neutral "Chưa chốt."
            "Quang không thêm câu nào."
    $ story_flag("tam_c04_south_trip_started")
    return
