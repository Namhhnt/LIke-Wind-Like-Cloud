# FILE: game/story/tam/tam_c04_between_work_and_hearts/s113_w19_friday_phase_check.rpy

label tam_c04_w19_s06_friday_phase_check:
    scene bg_company_open_office_day
    with fade
    if story_has_flag("tam_c04_tam_hoang_dating"):
        if relationship_contact_was_maintained("tam_hoang", "tam_c04_w19"):
            scene cg_tam_c04_tam_work_evening
            with dissolve
            "Tuần đầu hẹn hò không có pháo hoa. Chỉ có hai lần đổi giờ và không ai phải đoán người kia đã biến đi đâu."
            scene bg_company_open_office_day
            with dissolve
        else:
            "Tuần đầu hẹn hò kết thúc bằng một cuộc trò chuyện chưa được trả lời. Sự có tên không tự khiến một mối quan hệ được chăm sóc."
    elif story_has_flag("tam_c04_tam_quang_confirmed"):
        "Tâm và Quang đã nói rõ. Điều khó hơn là học cách không quay lại vai cũ mỗi khi ngượng."
    else:
        "Tâm làm xong việc sớm hơn một tiếng. Cô không dùng nó để chờ tin nhắn của ai."
    return
