# FILE: game/story/tam/tam_c04_between_work_and_hearts/s43_w07_friday_small_truth.rpy
# Week 07 — Friday asks which small truth Tâm will stop avoiding first.

label tam_c04_w07_s06_friday_small_truth:
    scene bg_company_open_office_day
    with dissolve

    scene cg_tam_c04_tam_work_evening
    with dissolve
    "Thứ Sáu, màn hình Tâm sáng lên khi cô đang cài lại chiếc cúc tay áo."
    scene bg_company_open_office_day
    with dissolve

    "Huyền vừa gửi bản cuối."

    "Hoàng hỏi túi bánh có cứu được buổi chiều không."

    "Quang gửi một dấu chấm rồi xóa."

    menu:
        "Nói với Hoàng rằng anh đã nhận ra trước Tâm":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_sub("tam_insecurity", 3)
            $ story_add_direction("tam", "tam_hoang_open")
            $ story_flag("tam_c04_w07_focus_hoang")

        "Nói với Huyền rằng cách cô tranh luận đã khác":
            $ story_add("career_huyen", 5)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 3)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w07_focus_huyen_quan")

        "Cùng Huyền hoàn thiện phụ lục":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 5)
            $ story_flag("tam_c04_w07_focus_huyen")

        "Bảo Quang gọi Thiên An ngay tối nay":
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_add_direction("quang", "quang_thienan_open")
            $ story_flag("tam_c04_w07_focus_quang_thienan")

        "Hỏi Quang dấu chấm vừa xóa là gì":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 3)
            $ tam_c04_add_extended_score("quang_tam_awareness", 5)
            $ story_add_direction("quang", "quang_tam_open")
            $ story_flag("tam_c04_w07_focus_quang_personal")

        "Đóng chat và gửi bản scope cuối":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_add("tam_observation", 3)
            $ story_add_direction("tam", "tam_career_focus")
            $ story_flag("tam_c04_w07_focus_career")

    "Tâm gửi đi một câu."

    "Không câu nào đủ lớn để đổi một mối quan hệ."

    "Nhưng có những điều chỉ cần được nói sớm hơn một tuần là đã khác."

    return
