# FILE: game/story/tam/tam_c04_between_work_and_hearts/s29_w05_quang_two_cups.rpy
# Week 05 — Two cups reveal which habit Quang is trying to stop hiding behind.

label tam_c04_w05_s04_quang_two_cups:
    scene bg_tam_family_dining_room_evening
    with fade

    scene cg_tam_c04_family_table
    with dissolve
    "Tối thứ Năm, Quang mang hồ sơ tới nhà."
    scene bg_tam_family_dining_room_evening
    with dissolve

    "Trên tay anh có hai cốc nước ấm."

    "Một cốc ít đường, đặt gần chỗ Tâm thường ngồi. Cốc còn lại không có đá, đặt trước ghế Thiên An."

    "Anh làm cả hai việc tự nhiên đến mức gần như không nhìn."

    thienan neutral "Anh đến đưa hồ sơ hay mở quầy nước?"

    quang "Tiện đường."

    tam teasing "Anh đi qua hai quán khác nhau mà vẫn tiện đường à?"

    "Quang đặt nắp cốc xuống. Một chiếc hơi lệch."

    menu:
        "Đẩy cốc của Thiên An về phía chị, để Quang tự nói":
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_add_direction("quang", "quang_thienan_open")
            $ story_add_direction("thienan", "thienan_quang_open")
            $ story_flag("tam_c04_w05_tam_leaves_quang_to_speak")
            $ story_flag("quang_thienan_two_cups")

            "Tâm đẩy cốc không đá về phía Thiên An rồi cầm cốc của mình lên."

            "Cô không đỡ lời."

            "Quang mở hồ sơ, tự nói lịch làm việc tuần sau. Thiên An không ngắt lời cho đến khi anh nói hết."

        "Hỏi vì sao Quang vẫn nhớ phần của Tâm":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 5)
            $ tam_c04_add_extended_score("quang_tam_awareness", 5)
            $ story_add("tam_observation", 5)
            $ story_add_direction("quang", "quang_tam_open")
            $ story_flag("tam_c04_w05_tam_asks_about_her_cup")
            $ story_flag("quang_tam_two_cups")

            tam neutral "Anh đến gặp chị An. Sao vẫn mua phần của em?"

            quang "Vì anh biết em ở nhà."

            tam neutral "Chỉ vậy thôi?"

            "Quang chỉnh chiếc nắp cốc lệch lại."

            quang "Em muốn anh trả lời thế nào?"

            tam teasing "Em đang hỏi anh mà."

        "Nhận cốc rồi đổi chủ đề":
            $ tam_c04_add_extended_score("quang_tam_warmth", 3)
            $ story_add("thienan_quang_trust", 3)
            $ story_add("tam_self_clarity", 3)
            $ story_flag("tam_c04_w05_tam_keeps_quang_familiar")

            tam neutral "Cảm ơn anh."

            "Tâm cầm cốc lên, hỏi Thiên An về chuyến đi tuần sau."

            "Quang không nói thêm. Nhưng khi ngồi xuống, anh kéo ghế gần bàn hơn mọi lần."

    "Hai cốc nước nguội chậm ở hai phía khác nhau."

    "Không cốc nào bị bỏ lại."

    return
