# FILE: game/story/tam/tam_c04_between_work_and_hearts/s44_w08_monday_phone_pulse.rpy
# Week 08 — Monday pulse before the second monthly review.

label tam_c04_w08_s01_monday_phone_pulse:
    scene bg_tam_room_morning
    with fade

    $ story_flag("tam_c04_w08_started")
    $ phone_refresh_all()

    scene cg_tam_c04_phone_morning
    with dissolve
    "Sáng thứ Hai cuối tháng hai, Tâm mở lịch trước khi mở tin nhắn."
    scene bg_tam_room_morning
    with dissolve

    "Buổi review nằm ở chiều thứ Ba."

    if story_state.get("huyen_quan_trust", 0) >= 55:
        "Huyền nhắn rằng cô đã tự chuẩn bị ba câu Quân có thể hỏi."
        if story_state.get("huyen_quan_interest", 0) >= 15:
            "Tin thứ hai đến sau đó: nhưng nếu ổng đổi câu hỏi thì không tính."
    else:
        "Huyền gửi một tin ngắn: chiều mai nhớ ngồi gần tao."

    if story_state.get("tam_hoang_interest", 0) >= 75 and story_state.get("hoang_tam_trust", 0) >= 70:
        "Hoàng không hỏi cuối tuần Tâm có rảnh không. Anh hỏi thứ Sáu cô tan làm lúc mấy giờ."
    elif story_state.get("tam_hoang_interest", 0) >= 55:
        "Hoàng gửi lời chúc review, đúng giờ nhưng không thêm lời mời."

    if (
        story_state.get("thienan_quang_trust", 0) >= 70
        and story_state.get("quang_thienan_resolve", 0) >= 70
    ):
        "Thiên An gửi một lịch hẹn có tên Quang nằm ở dòng người tham gia."
    elif (
        story_state.get("tam_quang_interest", 0) >= 25
        and story_state.get("quang_tam_awareness", 0) >= 20
    ):
        "Quang hỏi Tâm có về nhà sau buổi review không. Không nhắc Thiên An."

    "Mỗi thông báo đều ngắn."

    "Nhưng tháng thứ hai đã khiến người ta bớt dùng những câu thừa để che câu chính."

    return
