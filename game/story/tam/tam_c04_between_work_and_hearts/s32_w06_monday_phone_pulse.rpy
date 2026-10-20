# FILE: game/story/tam/tam_c04_between_work_and_hearts/s32_w06_monday_phone_pulse.rpy
# Week 06 — Monday pulse before Quân's short absence.

label tam_c04_w06_s01_monday_phone_pulse:
    scene bg_tam_room_morning
    with fade

    $ story_flag("tam_c04_w06_started")
    $ phone_refresh_all()

    scene cg_tam_c04_phone_morning
    with dissolve
    "Thứ Hai bắt đầu bằng một email thông báo Quân sẽ làm việc bên ngoài trong hai ngày."
    scene bg_tam_room_morning
    with dissolve

    if story_state.get("huyen_quan_trust", 0) >= 45:
        "Huyền chuyển tiếp email cho Tâm dù cả hai đều nằm trong danh sách nhận."
        huyen neutral "Tao chỉ đảm bảo mày đã đọc."
    else:
        "Huyền gửi một sticker ăn mừng rồi xóa nó sau chưa đầy một phút."

    if story_has_flag("tam_c04_w05_focus_hoang") or story_state.get("tam_hoang_interest", 0) >= 65:
        "Hoàng gửi ảnh chiếc cốc được đặt sẵn trên bàn ăn nhà anh. Không có người trong ảnh."
    elif story_state.get("tam_hoang_interest", 0) >= 45:
        "Hoàng hỏi cuối tuần của Tâm có đỡ bận hơn không. Câu hỏi dừng ở đó."

    if story_state.get("quang_thienan_resolve", 0) >= 60:
        "Quang nhắn trong nhóm gia đình rằng anh sẽ thay Thiên An đi nhận một bộ giấy tờ."
    elif story_state.get("quang_tam_awareness", 0) >= 12:
        "Quang nhắn riêng hỏi Tâm tuần này có về nhà ăn tối không."

    "Tâm đặt điện thoại xuống."

    "Một chiếc ghế trống trong hai ngày nghe không giống sự kiện gì lớn."

    "Nhưng có người đã để ý trước khi ngày làm việc bắt đầu."

    return
