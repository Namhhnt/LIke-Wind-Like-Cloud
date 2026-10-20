# FILE: game/story/tam/tam_c04_between_work_and_hearts/s124_w22_monday_phone_pulse.rpy

label tam_c04_w22_s01_monday_phone_pulse:
    $ story_flag("tam_c04_w22_started")
    $ phone_refresh_all()
    scene bg_tam_room_morning
    with fade
    scene cg_tam_c04_phone_morning
    with dissolve
    "Tuần này công việc chen vào đúng nơi người ta vừa tạo được một thói quen mới."
    scene bg_tam_room_morning
    with dissolve
    return
