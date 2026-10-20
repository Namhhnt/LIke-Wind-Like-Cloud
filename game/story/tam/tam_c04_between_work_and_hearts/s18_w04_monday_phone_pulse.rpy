# FILE: game/story/tam/tam_c04_between_work_and_hearts/s18_w04_monday_phone_pulse.rpy
# Week 04 — Monday pulse before the first monthly review.

label tam_c04_w04_s01_monday_phone_pulse:
    scene bg_tam_room_morning
    with fade

    $ story_flag("tam_c04_w04_started")
    $ phone_refresh_all()

    scene cg_tam_c04_phone_morning
    with dissolve
    "Sáng thứ Hai cuối cùng của tháng đầu tiên, Tâm thức dậy trước chuông báo thức hai phút."
    scene bg_tam_room_morning
    with dissolve

    "Màn hình điện thoại có ít thông báo hơn tuần trước. Nhưng mỗi cái rõ hơn."

    if story_state.get("huyen_quan_trust", 0) >= 30:
        "Huyền gửi ảnh bản báo cáo đã tự sửa, kèm một dòng ngắn."
        huyen neutral "Tao đoán đúng bốn trên năm chỗ. Chỗ thứ năm là ổng đổi cách hỏi. Gian lận."
    else:
        "Huyền gửi một chuỗi tin than về buổi review tháng. Cách cô gọi Quân vẫn đầy đủ họ tên trong từng câu."

    if story_state.get("tam_hoang_interest", 0) >= 65 or story_state.get("hoang_tam_trust", 0) >= 60:
        "Hoàng nhắn trước một thời gian cụ thể cho cuối tuần. Không còn câu 'nếu em bận thì thôi' ở phía sau."
        "Chỉ có thêm: nếu cần đổi giờ thì báo anh."
    elif story_state.get("tam_hoang_interest", 0) >= 45:
        "Hoàng gửi một lời chúc cho buổi review. Lịch sự, đúng lúc, và hơi xa hơn cách anh từng nhắn ở tuần trước."

    if story_state.get("thienan_quang_trust", 0) >= 55:
        "Thiên An đăng một bức ảnh ly cà phê ở sân bay. Trong góc ảnh có một tập tài liệu được đánh dấu bằng nét chữ của Quang."
    elif story_state.get("tam_quang_interest", 0) >= 15:
        "Quang nhắn Tâm hỏi chiếc ô dùng có ổn không. Một câu hỏi vô lý với một chiếc ô đã dùng nhiều năm."

    if story_state.get("career_tam", 0) >= 55:
        "Email review tháng đặt tên Tâm ở một dòng riêng, không còn ghép chung hoàn toàn với Huyền."

    "Tâm đọc lại lịch trong ngày."

    "Một tháng chưa kết thúc. Nhưng nhịp của nó đã đủ rõ để người ta biết mình thường nhìn về đâu khi điện thoại sáng."

    return
