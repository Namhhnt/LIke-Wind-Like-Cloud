label tam_c04_w11_s01_monday_phone_pulse:
    scene bg_tam_room_morning
    with fade
    $ story_flag("tam_c04_w11_started")
    $ phone_refresh_all()
    "Sáng thứ Hai, Tâm phát hiện lịch tuần có một khoảng trống đúng vào tối thứ Sáu."
    if story_state.get("tam_hoang_interest", 0) >= 75:
        "Hoàng hỏi khoảng trống đó có thật sự dành cho anh không."
    if story_state.get("huyen_quan_interest", 0) >= 20:
        "Huyền gửi ảnh một cốc cà phê đặt cạnh bàn Quân và viết: tao chỉ mua dư."
    if story_has_flag("tam_c04_m02_quang_crosscurrent_stronger") or (story_state.get("quang_tam_awareness", 0) >= 25 and story_state.get("quang_thienan_resolve", 0) >= 65):
        "Thiên An hỏi Tâm tối nay có về ăn cơm không. Không nhắc Quang, nhưng đặt ba cái bát lên bàn."
    "Có vài điều đã đi quá xa để tiếp tục giả vờ chỉ là tiện đường."
    return
