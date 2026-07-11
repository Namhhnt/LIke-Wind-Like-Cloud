# FILE: game/story/tam/tam_c04_between_work_and_hearts/s102_w17_friday_before_answer.rpy

label tam_c04_w17_s06_friday_before_answer:
    scene black
    with fade
    "Tối thứ Sáu, Tâm mở ba cuộc trò chuyện rồi không gõ chữ nào."
    "Một người đã xin một ngày Chủ Nhật. Một người vừa trở về với câu nói chưa hoàn tất. Còn cô đã dùng ba tháng để trì hoãn việc gọi tên điều mình muốn."
    menu:
        "Chuẩn bị trả lời Hoàng":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_c04_w17_prepares_hoang_answer")
        "Hẹn Quang nói chuyện trực tiếp":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_awareness", 5)
            $ story_flag("tam_c04_w17_prepares_quang_answer")
        "Không chọn ai chỉ vì đã đến hạn":
            $ story_add("career_tam", 5)
            $ story_add("tam_self_clarity", 7)
            $ story_flag("tam_c04_w17_prepares_independent_answer")
    return
