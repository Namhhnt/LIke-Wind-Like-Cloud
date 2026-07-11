# FILE: game/story/tam/tam_c04_between_work_and_hearts/s109_w19_first_week_after_choice.rpy

label tam_c04_w19_s02_first_week_after_choice:
    scene black
    with dissolve
    if story_has_flag("tam_c04_tam_hoang_dating"):
        "Hoàng đứng trước công ty với hai cốc nước."
        hoang neutral "Anh không biết em tan đúng giờ hay không. Nhưng anh biết hôm nay em chưa ăn chiều."
        menu:
            "Báo trước lịch bận và giữ một bữa tối muộn":
                $ relationship_mark_contact("tam_hoang", "tam_c04_w19", source="story")
                $ story_add("hoang_tam_trust", 3)
                $ story_flag("tam_c04_w19_hoang_contact_planned")
                tam neutral "Chín giờ. Nếu trễ em sẽ báo."
                hoang neutral "Được. Anh không cần em rảnh. Anh cần em có mặt trong lời em nói."
            "Nhận nước rồi quay lại làm, không hẹn gì":
                $ story_add("career_tam", 5)
                $ story_flag("tam_c04_w19_hoang_contact_deferred")
                "Hoàng không hỏi thêm."
    elif story_has_flag("tam_c04_tam_quang_confirmed"):
        "Tâm và Quang ngồi ở một quán không ai trong gia đình thường tới."
        quang "Anh không biết phải cư xử khác thế nào."
        tam neutral "Đừng cố khác. Chỉ đừng giả vờ như chưa nói gì."
        $ story_add("tam_quang_interest", 5)
        $ tam_c04_add_extended_score("quang_tam_awareness", 5)
        $ story_flag("tam_c04_w19_quang_tam_first_deliberate_outing")
    else:
        "Tâm nhận lời phụ trách một bản đề xuất mà trước đây cô sẽ chờ người khác cùng làm."
        $ story_add("career_tam", 10)
        $ story_add("tam_self_clarity", 5)
        $ story_flag("tam_c04_w19_independent_proposal")
    return
