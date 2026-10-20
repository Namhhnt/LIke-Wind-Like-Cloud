# FILE: game/story/tam/tam_c04_between_work_and_hearts/s123_w21_friday_new_routine.rpy

label tam_c04_w21_s05_friday_new_routine:
    scene bg_company_open_office_day
    with fade
    scene cg_tam_c04_tam_work_evening
    with dissolve
    "Một mối quan hệ mới không thay hết lịch sống. Nó chỉ buộc người ta thôi giả vờ rằng lịch ấy không ảnh hưởng tới ai."
    scene bg_company_open_office_day
    with dissolve
    if story_has_flag("tam_c04_tam_hoang_dating") and relationship_contact_was_maintained("tam_hoang", "tam_c04_w21"):
        "Tâm và Hoàng đổi lịch một lần. Không ai biến mất."
    elif story_has_flag("tam_c04_tam_quang_confirmed"):
        "Quang nhắn trước khi ghé. Một việc rất nhỏ, nhưng khác hẳn cách anh từng bước vào nhà như người thân."
    else:
        "Tâm đặt cuối tuần cho mình và không giải thích với ai."
    return
