label tam_c04_w12_s01_monday_phone_pulse:
    scene bg_tam_room_morning
    with fade
    $ story_flag("tam_c04_w12_started")
    $ phone_refresh_all()
    scene cg_tam_c04_phone_morning
    with dissolve
    "Sáng thứ Hai cuối tháng ba, mail đánh giá ba tháng đầu nằm trên cùng hộp thư."
    scene bg_tam_room_morning
    with dissolve
    "Người ký lịch review là Quân."
    if story_state.get("tam_hoang_interest", 0) >= 80 and story_state.get("hoang_tam_trust", 0) >= 75:
        "Hoàng nhắn: xong review thì báo anh. Không cần vui mới báo."
    if story_state.get("huyen_quan_trust", 0) >= 65:
        "Huyền không đoán câu hỏi nữa. Cô gửi Tâm bản tự đánh giá đã hoàn thành từ tối qua."
    if story_state.get("quang_thienan_resolve", 0) >= 75:
        "Quang đã có tên trong lịch ăn tối gia đình thứ Năm."
    elif story_state.get("quang_tam_awareness", 0) >= 30:
        "Quang hỏi Tâm muốn anh đợi sau buổi review hay không."
    "Ba tháng đủ dài để một vài điều được gọi đúng tên."
    "Chưa đủ dài để mọi người đều sẵn sàng gọi."
    return
