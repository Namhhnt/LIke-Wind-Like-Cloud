# FILE: game/story/tam/tam_c04_between_work_and_hearts/s95_w16_month_four_priority.rpy

label tam_c04_w16_s05_month_four_priority:
    scene black
    with fade
    "Một tháng có người đi xa kết thúc bằng những điều họ chọn báo về."
    menu:
        "Tâm muốn trả lời Hoàng rõ ràng hơn":
            $ story_add("tam_hoang_interest", 7)
            $ story_add("hoang_tam_trust", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_c04_w16_priority_hoang_breakthrough")
        "Tâm muốn nghe Quang nói điều anh đang tránh":
            $ story_add("tam_quang_interest", 7)
            $ tam_c04_add_extended_score("quang_tam_awareness", 7)
            $ tam_c04_add_extended_score("quang_tam_warmth", 5)
            $ story_flag("tam_c04_w16_priority_quang_tam_clarity")
        "Tâm muốn Quang và Thiên An tự bước gần nhau":
            $ story_add("thienan_quang_trust", 7)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 7)
            $ story_flag("tam_c04_w16_priority_quang_thienan_closer")
        "Tâm muốn Huyền giữ vị trí riêng trong nhà Quân":
            $ story_add("huyen_quan_trust", 7)
            $ story_add("huyen_quan_interest", 3)
            $ story_flag("tam_c04_w16_priority_huyen_quan_deep")
        "Tâm chọn tiếp tục xây vị trí của mình":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 7)
            $ story_flag("tam_c04_w16_priority_independent")
    return
