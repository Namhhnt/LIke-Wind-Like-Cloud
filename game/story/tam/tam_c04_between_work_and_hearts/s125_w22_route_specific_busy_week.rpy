# FILE: game/story/tam/tam_c04_between_work_and_hearts/s125_w22_route_specific_busy_week.rpy

label tam_c04_w22_s02_route_specific_busy_week:
    scene black
    with dissolve
    if story_has_flag("tam_c04_tam_hoang_dating"):
        "Hoàng phải đi gặp khách hàng hai ngày. Tâm lại có deadline vào tối anh trở về."
        menu:
            "Gọi mười phút trước khi cả hai ngủ":
                $ relationship_mark_contact("tam_hoang", "tam_c04_w22", source="story")
                $ story_add("hoang_tam_trust", 3)
                $ story_flag("tam_c04_w22_hoang_tam_ten_minute_call")
                hoang tired "Anh không cần em kể hết. Chỉ muốn biết hôm nay của em đã qua thế nào."
            "Hẹn cuối tuần và giữ đúng lịch":
                $ relationship_mark_contact("tam_hoang", "tam_c04_w22", source="story")
                $ story_add("tam_hoang_interest", 3)
                $ story_flag("tam_c04_w22_hoang_tam_weekend_kept")
            "Để qua deadline rồi tính":
                $ story_add("career_tam", 7)
                $ story_flag("tam_c04_w22_hoang_contact_missed")
    elif story_has_flag("tam_c04_tam_quang_confirmed"):
        "Quang hẹn Tâm ở một quán cách xa nhà hai người."
        quang "Anh muốn có một nơi mà mình không tự động nói chuyện về chị An."
        tam neutral "Anh đang làm tốt đấy. Mười phút rồi chưa nhắc."
        quang "Em vừa nhắc."
        $ story_add("tam_quang_interest", 5)
        $ tam_c04_add_extended_score("quang_tam_awareness", 5)
        $ story_flag("tam_c04_w22_quang_tam_deliberate_space")
    else:
        "Tâm dành ba tối liên tiếp cho dự án. Cô mệt, nhưng không dùng sự bận rộn để trốn một câu trả lời nào."
        $ story_add("career_tam", 12)
        $ story_add("tam_self_clarity", 3)
        $ story_flag("tam_c04_w22_independent_busy_week")
    return
