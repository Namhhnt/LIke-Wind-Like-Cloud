# FILE: game/story/tam/tam_c04_between_work_and_hearts/s86_w15_monday_phone_pulse.rpy

label tam_c04_w15_s01_monday_phone_pulse:
    $ story_flag("tam_c04_w15_started")
    $ phone_refresh_all()
    scene bg_tam_room_morning
    with fade
    scene cg_tam_c04_phone_morning
    with dissolve
    "Tin nhắn từ miền Nam đến lúc 00:47. Tin của Hoàng đến lúc 21:10. Tin của Huyền chỉ là ảnh một bài toán lớp ba bị sửa ba lần."
    scene bg_tam_room_morning
    with dissolve
    return
