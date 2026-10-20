# FILE: game/story/tam/tam_c04_between_work_and_hearts/s119_w21_monday_phone_pulse.rpy

label tam_c04_w21_s01_monday_phone_pulse:
    $ story_flag("tam_c04_w21_started")
    $ phone_refresh_all()
    scene bg_tam_room_morning
    with fade
    scene cg_tam_c04_phone_morning
    with dissolve
    "Tháng cuối bắt đầu không bằng một biến cố. Chỉ là cách mọi người gọi tên Tâm đã khác đi trong những việc rất nhỏ."
    scene bg_tam_room_morning
    with dissolve
    return
