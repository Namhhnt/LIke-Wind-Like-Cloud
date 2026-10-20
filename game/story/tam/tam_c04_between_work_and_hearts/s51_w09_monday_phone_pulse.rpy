# Week 09 — Monday pulse: strong routes gain small privileges; weak routes become quieter.
label tam_c04_w09_s01_monday_phone_pulse:
    scene bg_tam_room_morning
    with fade
    $ story_flag("tam_c04_w09_started")
    $ phone_refresh_all()

    scene cg_tam_c04_phone_morning
    with dissolve
    "Sáng thứ Hai đầu tháng ba, điện thoại của Tâm không nhiều thông báo hơn."
    scene bg_tam_room_morning
    with dissolve
    "Chúng chỉ bớt giống những lời báo trước chung chung."

    if story_has_flag("tam_c04_m02_hoang_deepening"):
        "Hoàng gửi thẳng một giờ hẹn và thêm: nếu em không muốn, nói anh biết trước chiều thứ Sáu."
    elif story_has_flag("tam_c04_m02_hoang_holding"):
        "Hoàng hỏi cuối tuần này Tâm có còn bận như tuần trước không."
    else:
        "Không có tin của Hoàng. Bài đăng mới của anh là một bản phác thảo đã hoàn thiện."

    if story_has_flag("tam_c04_m02_huyen_quan_personal_progress"):
        "Huyền gửi ảnh một file đã được Quân trả lại mà không có vệt đỏ nào. Cô chỉ nhắn: đáng sợ."
    else:
        "Huyền nhắc Tâm về cuộc họp sáng thứ Ba và bảo cô đừng đến muộn."

    if story_has_flag("tam_c04_m02_quang_crosscurrent_stronger"):
        "Quang gửi một tin rồi thu hồi trước khi Tâm đọc hết. Tên Thiên An vẫn còn trong dòng đầu."
    elif story_has_flag("tam_c04_m02_quang_thienan_direct"):
        "Thiên An chuyển tiếp lịch làm việc mà Quang đã tự xác nhận với cô."
    elif story_has_flag("tam_c04_m02_tam_quang_personal_progress"):
        "Quang hỏi Tâm có nhớ mang ô không. Trời hôm nay không mưa."

    "Tâm đặt điện thoại xuống."
    "Hai tháng đầu tạo ra lựa chọn. Tháng thứ ba bắt đầu tạo ra thói quen được người khác trông chờ."
    return
