# FILE: game/story/tam/tam_c04_between_work_and_hearts/s98_w17_south_return.rpy

label tam_c04_w17_s02_south_return:
    scene bg_company_lobby_morning
    with dissolve
    scene cg_tam_c04_return_luggage
    with dissolve
    "Thiên An bước ra khỏi thang máy trước. Quang kéo theo hai chiếc vali."
    scene bg_company_lobby_morning
    with dissolve
    thienan neutral "Một cái là của tôi."
    quang "Anh biết."
    thienan neutral "Vậy sao anh kéo cả hai?"
    quang "Vì tay em đang cầm hồ sơ."
    "Thiên An không giành lại tay kéo."
    menu:
        "Đón Thiên An trước":
            $ story_add("thienan_quang_trust", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_flag("tam_c04_w17_tam_greets_thienan_first")
            tam neutral "Chị về rồi."
            thienan neutral "Ừ. Nhà còn cây nào sống không?"
        "Hỏi Quang có nhớ nhà không":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 5)
            $ tam_c04_add_extended_score("quang_tam_awareness", 5)
            $ story_flag("tam_c04_w17_tam_asks_quang_missed_home")
            quang "Có. Nhưng không chỉ nhớ nhà."
        "Nhận một chiếc vali và đi cùng cả hai":
            $ story_add("tam_observation", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 3)
            $ story_add("thienan_quang_trust", 3)
            $ story_flag("tam_c04_w17_three_return_together")
    return
