# FILE: game/story/tam/tam_c04_between_work_and_hearts/s108_w19_monday_phone_pulse.rpy

label tam_c04_w19_s01_monday_phone_pulse:
    $ story_flag("tam_c04_w19_started")
    $ phone_refresh_all()
    scene bg_tam_room_morning
    with fade
    if story_has_flag("tam_c04_tam_hoang_dating"):
        "Tin đầu tuần của Hoàng không còn hỏi Tâm có rảnh không. Anh gửi lịch của mình và hỏi cô muốn giữ tối nào."
    elif story_has_flag("tam_c04_tam_quang_confirmed"):
        "Quang gửi địa chỉ một quán nhỏ, không kèm tên Thiên An hay bất kỳ việc nhà nào."
    else:
        "Điện thoại yên. Tâm thấy nhẹ hơn, không trống hơn."
    return
