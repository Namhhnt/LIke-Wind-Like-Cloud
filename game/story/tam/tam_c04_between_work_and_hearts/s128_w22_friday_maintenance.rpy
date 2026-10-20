# FILE: game/story/tam/tam_c04_between_work_and_hearts/s128_w22_friday_maintenance.rpy

label tam_c04_w22_s05_friday_maintenance:
    scene bg_company_open_office_day
    with fade
    if story_has_flag("tam_c04_tam_hoang_dating"):
        if relationship_contact_was_maintained("tam_hoang", "tam_c04_w22"):
            scene cg_tam_c04_tam_work_evening
            with dissolve
            "Khoảng cách tuần này được giữ bằng một cuộc gọi mười phút. Không lãng mạn lắm. Nhưng thật."
            scene bg_company_open_office_day
            with dissolve
        else:
            "Hoàng không nhắn thêm sau tối thứ Ba. Không phải để trừng phạt. Anh chỉ ngừng làm người duy nhất giữ nhịp."
    elif story_has_flag("tam_c04_tam_quang_confirmed"):
        "Tâm và Quang có một nơi không ai gọi họ là người nhà. Cả hai vẫn ngượng, nhưng không lùi."
    else:
        "Tâm gửi bản đề xuất trước hạn. Cuối tuần của cô không còn là phần thưởng ai khác phải trao."
    return
