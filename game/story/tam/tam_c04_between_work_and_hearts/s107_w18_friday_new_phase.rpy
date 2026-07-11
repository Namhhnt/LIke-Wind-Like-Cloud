# FILE: game/story/tam/tam_c04_between_work_and_hearts/s107_w18_friday_new_phase.rpy

label tam_c04_w18_s05_friday_new_phase:
    scene black
    with fade
    if story_has_flag("tam_c04_tam_hoang_dating"):
        "Tối thứ Sáu, tên Hoàng nằm trên đầu lịch cuối tuần thay vì ở cuối danh sách thông báo."
        $ relationship_mark_contact("tam_hoang", "tam_c04_w18", source="phase_start")
    elif story_has_flag("tam_c04_tam_quang_confirmed"):
        "Quang nhắn: 'Mai mình đi đâu đó không liên quan tới gia đình nhé.'"
        "Tâm nhìn chữ 'mình' lâu hơn cần thiết."
    else:
        "Tâm để cuối tuần trống. Không phải chờ ai lấp vào."
    return
