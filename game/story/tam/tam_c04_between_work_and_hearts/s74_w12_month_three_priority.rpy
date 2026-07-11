label tam_c04_w12_s06_month_three_priority:
    scene bg_company_open_office_day
    with dissolve
    "Thứ Sáu, sáu giờ năm mươi tám."
    "Ba tháng đầu khép lại bằng một bản đánh giá, một quy tắc không để người khác đoán, một bữa cơm ba người và một cốc nước đặt đúng bàn."
    menu:
        "Giữ một lịch cố định với Hoàng trong tháng tới":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_sub("tam_insecurity", 3)
            $ story_add_direction("tam", "tam_hoang_open")
            $ story_flag("tam_c04_w12_focus_hoang")
        "Để Huyền và Quân tự kết thúc buổi review":
            $ story_add("career_huyen", 5)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 5)
            $ story_flag("tam_c04_w12_focus_huyen_quan")
        "Lên kế hoạch hai luồng công việc cùng Huyền":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 5)
            $ story_flag("tam_c04_w12_focus_huyen")
        "Để Quang có một chỗ rõ ràng bên cạnh Thiên An":
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_flag("tam_c04_w12_focus_quang_thienan")
        "Yêu cầu Quang trả lời Tâm bằng tên của chính cô":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 3)
            $ tam_c04_add_extended_score("quang_tam_awareness", 5)
            $ story_flag("tam_c04_w12_focus_quang_personal")
        "Nhận luồng công việc có quyền ký duyệt":
            $ story_add("career_tam", 15)
            $ story_add("tam_self_clarity", 5)
            $ story_add("tam_observation", 3)
            $ story_flag("tam_c04_w12_focus_career")
    "Tâm ghi lựa chọn vào lịch tháng tới."
    "Không còn là một việc cô làm lúc rảnh."
    return
