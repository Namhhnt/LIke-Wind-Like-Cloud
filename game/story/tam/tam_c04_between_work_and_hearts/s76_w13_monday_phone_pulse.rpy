# FILE: game/story/tam/tam_c04_between_work_and_hearts/s76_w13_monday_phone_pulse.rpy

label tam_c04_w13_s01_monday_phone_pulse:
    $ story_flag("tam_c04_w13_started")
    $ phone_refresh_all()
    scene bg_tam_room_morning
    with fade
    scene cg_tam_c04_phone_morning
    with dissolve
    "Sáng thứ Hai, điện thoại rung trước chuông báo thức hai phút."
    scene bg_tam_room_morning
    with dissolve
    "Một tin về chuyến công tác. Một tin hỏi tối thứ Tư. Một tin chỉ có địa chỉ trường học."
    return
