# FILE: game/story/tam/tam_c04_between_work_and_hearts/s90_w15_friday_distance_choice.rpy

label tam_c04_w15_s05_friday_distance_choice:
    scene black
    with fade
    "Khoảng cách không lấy mất cả tuần. Nó chỉ làm một vài câu hỏi trở nên rõ hơn."
    menu:
        "Giữ lịch gọi với Hoàng":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_flag("tam_c04_w15_priority_hoang_contact")
        "Chờ tin Quang sau giờ làm":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_awareness", 5)
            $ story_flag("tam_c04_w15_priority_quang_distance")
        "Để chuyến đi thuộc về Quang và Thiên An":
            $ story_add("thienan_quang_trust", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_flag("tam_c04_w15_priority_quang_thienan")
        "Ở cùng Huyền và Ánh Nhi":
            $ story_add("huyen_quan_trust", 5)
            $ story_add("career_huyen", 3)
            $ story_flag("tam_c04_w15_priority_huyen_anhni")
        "Nhận thêm đầu việc độc lập":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_c04_w15_priority_independent")
    return
