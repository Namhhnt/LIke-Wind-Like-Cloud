# FILE: game/story/tam/tam_c04_between_work_and_hearts/s122_w21_independent_opportunity.rpy

label tam_c04_w21_s04_independent_opportunity:
    scene bg_meeting_room_day
    with dissolve
    "Một dự án ngắn cần người đại diện nhóm làm việc trực tiếp với khách hàng."
    if story_has_flag("tam_c04_tam_independent"):
        quan neutral "Tôi đề cử cô. Không có người đi kèm."
        menu:
            "Nhận dự án":
                $ story_add("career_tam", 15)
                $ story_add("tam_self_clarity", 5)
                $ story_flag("tam_c04_w21_tam_accepts_independent_project")
                tam neutral "Em nhận."
            "Đề nghị Huyền review nội bộ":
                $ story_add("career_tam", 10)
                $ story_add("career_huyen", 5)
                $ tam_c04_add_extended_score("tam_huyen_work_sync", 5)
                $ story_flag("tam_c04_w21_tam_project_peer_review")
    else:
        "Tâm nhận phần chuẩn bị, không dùng mối quan hệ mới như lý do rút khỏi trách nhiệm."
        $ story_add("career_tam", 10)
        $ story_flag("tam_c04_w21_tam_keeps_career_after_romance")
    return
