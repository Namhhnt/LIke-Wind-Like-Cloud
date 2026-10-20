# FILE: game/story/tam/tam_c04_between_work_and_hearts/s99_w17_quang_chooses_conversation.rpy

label tam_c04_w17_s03_quang_chooses_conversation:
    scene bg_tam_family_hallway_night
    with dissolve
    "Chiều hôm đó, Quang đứng ở ngã rẽ giữa phòng Thiên An và ban công nơi Tâm đang phơi khăn."
    menu:
        "Quang gõ cửa phòng Thiên An":
            $ story_add("thienan_quang_trust", 7)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 7)
            $ story_flag("tam_c04_w17_quang_chooses_thienan_conversation")
            quang "Anh muốn nói về những ngày ở trong đó. Không phải báo cáo."
            thienan neutral "Vào đi."
        "Quang ra ban công với Tâm":
            $ story_add("tam_quang_interest", 7)
            $ tam_c04_add_extended_score("quang_tam_awareness", 7)
            $ tam_c04_add_extended_score("quang_tam_warmth", 5)
            $ story_flag("tam_c04_w17_quang_chooses_tam_conversation")
            quang "Anh nghĩ tới em nhiều hơn anh nên nghĩ."
            tam neutral "Ai quy định là nên bao nhiêu?"
            quang "Anh đang cố tìm câu trả lời."
        "Quang để cả hai nghỉ":
            $ story_add("tam_self_clarity", 5)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w17_quang_delays_conversation")
            "Anh đặt túi quà trên bàn rồi về. Lần đầu tiên sự cẩn thận trông giống một bước lùi."
    return
