# FILE: game/story/tam/tam_c04_between_work_and_hearts/s88_w15_quang_message_after_midnight.rpy

label tam_c04_w15_s03_quang_message_after_midnight:
    scene bg_tam_room_morning
    with dissolve
    "Tâm đọc tin nhắn của Quang sau nửa đêm."
    quang "Hôm nay ổn. Chị An chịu ăn tối."
    menu:
        "Hỏi Quang thì sao":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 5)
            $ tam_c04_add_extended_score("quang_tam_awareness", 5)
            $ story_flag("tam_c04_w15_tam_asks_quang_himself")
            tam neutral "Em hỏi anh. Anh có ổn không?"
            quang "Giờ thì có."
        "Bảo Quang tiếp tục chăm Thiên An":
            $ story_add("thienan_quang_trust", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_flag("tam_c04_w15_tam_supports_south_pair")
            tam neutral "Anh ở cạnh chị ấy là được."
            quang "Ừ."
        "Chỉ thả một biểu tượng đã đọc":
            $ story_add("tam_self_clarity", 3)
            $ tam_c04_add_extended_score("quang_tam_awareness", 3)
            $ story_flag("tam_c04_w15_tam_leaves_quang_unanswered")
            "Ba phút sau, Quang không gửi thêm."
    return
