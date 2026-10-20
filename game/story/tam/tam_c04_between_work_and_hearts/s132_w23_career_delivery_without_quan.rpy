# FILE: game/story/tam/tam_c04_between_work_and_hearts/s132_w23_career_delivery_without_quan.rpy

label tam_c04_w23_s04_career_delivery_without_quan:
    scene bg_meeting_room_day
    with dissolve
    scene cg_tam_c04_tam_huyen_work
    with dissolve
    "Tâm và Huyền phải gửi bản cuối khi Quân vẫn đang ở sân bay."
    scene bg_company_open_office_day
    with dissolve
    menu:
        "Tâm ký phần của mình, Huyền ký phần của cô":
            $ story_add("career_tam", 10)
            $ story_add("career_huyen", 10)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 5)
            $ story_flag("tam_c04_w23_dual_signoff")
        "Tâm đứng ra nhận toàn bộ trách nhiệm":
            $ story_add("career_tam", 15)
            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_c04_w23_tam_full_signoff")
        "Huyền dẫn buổi gửi và xử lý phản hồi":
            $ story_add("career_huyen", 15)
            $ story_add("huyen_quan_trust", 5)
            $ story_flag("tam_c04_w23_huyen_full_signoff")
    return
