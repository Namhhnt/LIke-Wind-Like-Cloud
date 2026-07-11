# FILE: game/story/tam/tam_c04_between_work_and_hearts/s26_w05_monday_phone_pulse.rpy
# Week 05 — Month 02 begins with route-health signals from Month 01.

label tam_c04_w05_s01_monday_phone_pulse:
    scene bg_tam_room_morning
    with fade

    $ story_flag("tam_c04_w05_started")
    $ story_flag("tam_c04_month_02_started")
    $ phone_refresh_all()

    "Sáng thứ Hai đầu tiên của tháng mới, Tâm thức dậy vì điện thoại rung trên mặt bàn."

    "Không có thông báo nào nói thẳng rằng tháng trước đã thay đổi điều gì."

    "Chúng chỉ đến từ những người khác nhau, vào những giờ khác nhau."

    if story_has_flag("tam_c04_m01_hoang_strong"):
        "Hoàng gửi một địa chỉ và hỏi Tâm thích trà nóng hay cà phê. Không giải thích địa chỉ đó là nhà anh."
    elif story_has_flag("tam_c04_m01_hoang_warm"):
        "Hoàng gửi lời chúc đầu tháng, sau đó xóa một tin nhắn trước khi Tâm kịp đọc."
    else:
        "Trang cá nhân của Hoàng có một bức ảnh góc phòng khách vừa được sửa lại. Không có lời mời nào đi cùng."

    if story_has_flag("tam_c04_m01_huyen_quan_progressing"):
        "Huyền gửi outline trước bảy giờ, rồi nhắn thêm rằng cô đã tự đoán được Quân sẽ hỏi gì."
    else:
        "Huyền gửi một ảnh chụp màn hình với bốn dấu hỏi đỏ và lời tuyên bố rằng tháng mới bắt đầu bằng bạo lực tinh thần."

    if story_has_flag("tam_c04_m01_quang_thienan_progressing"):
        "Thiên An nhắn vào nhóm gia đình rằng Quang sẽ qua lấy một tập hồ sơ vào tối nay. Câu chữ tỉnh bơ đến mức giống như chuyện đó đã quen từ lâu."
    elif story_has_flag("tam_c04_m01_quang_tam_personal_seed"):
        "Quang hỏi Tâm còn giữ chiếc ô cũ không. Anh vẫn chưa giải thích vì sao câu hỏi ấy cần được hỏi vào sáu giờ bốn mươi."

    "Tâm kéo rèm."

    "Thành phố ngoài cửa sổ vẫn như cũ. Chỉ có những thói quen đã bắt đầu tìm chỗ đứng riêng."

    return
