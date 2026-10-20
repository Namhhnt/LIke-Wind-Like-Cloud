# FILE: game/story/tam/tam_c04_between_work_and_hearts/s91_w16_monday_phone_pulse.rpy

label tam_c04_w16_s01_monday_phone_pulse:
    $ story_flag("tam_c04_w16_started")
    $ phone_refresh_all()
    scene bg_tam_room_morning
    with fade
    scene cg_tam_c04_phone_morning
    with dissolve
    "Tuần cuối tháng bắt đầu bằng thông báo chuyến bay lùi hai ngày. Hoàng gửi lại lịch tối thứ Tư. Quân nhắn Huyền đúng bốn chữ: 'Cảm ơn cô. Tôi về.'"
    scene bg_tam_room_morning
    with dissolve
    return
