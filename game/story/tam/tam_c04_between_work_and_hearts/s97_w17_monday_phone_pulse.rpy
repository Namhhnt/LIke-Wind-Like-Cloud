# FILE: game/story/tam/tam_c04_between_work_and_hearts/s97_w17_monday_phone_pulse.rpy

label tam_c04_w17_s01_monday_phone_pulse:
    $ story_flag("tam_c04_w17_started")
    $ phone_refresh_all()
    scene bg_tam_room_morning
    with fade
    scene cg_tam_c04_phone_morning
    with dissolve
    "Thiên An và Quang trở về vào sáng thứ Hai. Hoàng hỏi Tâm có giữ Chủ Nhật không. Huyền gửi ảnh Ánh Nhi bỏ quên một chiếc dây buộc tóc ở nhà cô."
    scene bg_tam_room_morning
    with dissolve
    return
