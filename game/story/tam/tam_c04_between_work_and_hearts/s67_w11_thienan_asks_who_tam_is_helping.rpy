label tam_c04_w11_s05_thienan_asks_who_tam_is_helping:
    scene black
    with fade
    "Tối thứ Năm, Thiên An gấp tờ lịch Quang để lại thành đôi."
    thienan neutral "Em đang giúp ai vậy?"
    tam confused "Chị hỏi chuyện gì?"
    thienan neutral "Chuyện em cứ đứng giữa."
    "Câu hỏi không có vẻ giận. Chính vì thế nó khó né hơn."
    menu:
        "Nói Tâm muốn Quang và Thiên An tự chọn nhau":
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_add("tam_self_clarity", 3)
            $ story_flag("tam_c04_w11_tam_tells_an_supports_them")
            tam neutral "Em muốn hai người tự nói với nhau. Em không muốn chị phải đoán qua em nữa."
            thienan neutral "Vậy thì đừng dịch hộ anh ấy."
        "Nói Tâm không còn chắc mình hoàn toàn đứng ngoài":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_awareness", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 3)
            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_c04_w11_tam_admits_not_outside_quang")
            tam neutral "Em không chắc mình còn đứng ngoài được nữa."
            "Thiên An nhìn cô lâu hơn một nhịp."
            thienan neutral "Vậy đừng gọi nó là giúp chị."
        "Nói Tâm chưa biết và sẽ ngừng can thiệp":
            $ story_add("tam_self_clarity", 5)
            $ story_add("tam_observation", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 3)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 3)
            $ story_flag("tam_c04_w11_tam_stops_mediating_quang")
            tam neutral "Em chưa biết. Nên em sẽ không đứng giữa nữa."
            thienan neutral "Tốt."
    "Thiên An đặt tờ lịch xuống bàn."
    "Nếp gấp chạy đúng qua tên Quang."
    return
