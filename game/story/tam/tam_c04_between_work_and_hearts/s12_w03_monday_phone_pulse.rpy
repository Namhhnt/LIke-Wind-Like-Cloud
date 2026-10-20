# FILE: game/story/tam/tam_c04_between_work_and_hearts/s12_w03_monday_phone_pulse.rpy
# Week 03 — Monday pulse: earlier priorities begin producing pressure and distance.

label tam_c04_w03_s01_monday_phone_pulse:
    scene bg_tam_room_morning
    with fade

    $ story_flag("tam_c04_w03_started")
    $ phone_refresh_all()

    scene cg_tam_c04_phone_morning
    with dissolve
    "Sáng thứ Hai, Tâm tỉnh dậy khi điện thoại rung một lần rồi im."
    scene bg_tam_room_morning
    with dissolve

    "Không phải chuỗi tin nhắn dồn dập. Chỉ là những lời nhắc ngắn, mỗi lời nằm ở một góc khác nhau trong ngày của cô."

    "Huyền gửi bản slide đã sửa lúc sáu giờ bốn mươi tám."

    huyen neutral "Tao bỏ được hai câu thừa trước khi anh Quân nhìn thấy. Có tính là tự cứu không?"

    tam tired "Có. Nhưng mày gửi tao lúc chưa tới bảy giờ thì chưa chắc."

    if story_has_flag("tam_c04_w02_focus_hoang") or story_state.get("tam_hoang_interest", 0) >= 60:
        "Hoàng hỏi tối thứ Tư cô có rảnh không. Phía sau câu hỏi có thêm địa điểm và thời gian cụ thể."
        "Anh bắt đầu bớt để mọi thứ ở dạng có thể rút lại."
    elif story_state.get("tam_hoang_interest", 0) >= 45:
        "Hoàng gửi ảnh một quán ăn mới, không kèm lời mời."
        "Đủ để Tâm biết anh đã nghĩ đến cô. Chưa đủ để biết anh có định bước thêm không."

    if story_has_flag("tam_c04_w02_focus_quang_thienan") or story_state.get("thienan_quang_trust", 0) >= 50:
        "Quang không hỏi tình hình Thiên An nữa. Anh chỉ nhắn rằng chiều nay sẽ mang hồ sơ qua nhà."
    elif story_has_flag("tam_c04_w02_focus_quang_personal") or story_state.get("tam_quang_interest", 0) >= 10:
        "Quang gửi một tin nhắn riêng cho Tâm, nhắc cô đừng quên chiếc ô đã để ở xe anh từ cuối tuần."
        "Một việc rất cũ. Cách anh nhớ cũng rất cũ."

    if story_state.get("career_tam", 0) >= 45:
        "Email công việc nằm cuối danh sách: khách hàng xác nhận buổi trình bày chính thức vào chiều mai."
        "Tên Tâm được đặt trong phần người trình bày, không còn trong danh sách hỗ trợ."

    "Tâm đặt điện thoại xuống, buộc lại tóc."

    "Hai tuần trước, các tin nhắn chỉ báo rằng ai đó đang ở gần."

    "Tuần này, chúng bắt đầu hỏi cô có đủ chỗ cho họ hay không."

    return
