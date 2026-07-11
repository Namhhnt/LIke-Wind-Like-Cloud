# FILE: game/story/tam/tam_c04_between_work_and_hearts/s49_w08_month_two_priority.rpy
# Week 08 — Final priority choice of Month 02. Still no hard route lock.

label tam_c04_w08_s06_month_two_priority:
    scene bg_company_open_office_day
    with dissolve

    "Thứ Sáu, bảy giờ mười ba."

    "Hai tháng không kết thúc bằng một lời xác nhận."

    "Chỉ có một lịch hẹn của Hoàng, một bản trình bày Huyền đang sửa cùng Quân, một tập hồ sơ Quang chưa biết nên tự mang lên hay gửi lại, và đầu việc mới mang tên Tâm."

    menu:
        "Nói với Hoàng rằng Tâm sẽ xuất hiện, không cần anh hỏi lại":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_sub("tam_insecurity", 3)
            $ story_add_direction("tam", "tam_hoang_open")
            $ story_flag("tam_c04_w08_focus_hoang")

        "Để Huyền tự ở lại với Quân":
            $ story_add("career_huyen", 5)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 5)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w08_focus_huyen_quan")

        "Gửi Huyền file review chéo trước khi về":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 5)
            $ story_add_direction("tam", "tam_support_huyen")
            $ story_flag("tam_c04_w08_focus_huyen")

        "Bảo Quang tự bước lên cầu thang":
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_add_direction("quang", "quang_thienan_open")
            $ story_add_direction("thienan", "thienan_quang_open")
            $ story_flag("tam_c04_w08_focus_quang_thienan")

        "Hỏi Quang khi nào anh định trả lời Tâm":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 3)
            $ tam_c04_add_extended_score("quang_tam_awareness", 5)
            $ story_add_direction("quang", "quang_tam_open")
            $ story_flag("quang_tam_route_seeded")
            $ story_flag("tam_c04_w08_focus_quang_personal")

        "Mở đầu việc có quyền quyết định mới":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_add("tam_observation", 3)
            $ story_add_direction("tam", "tam_career_focus")
            $ story_flag("tam_c04_w08_focus_career")

    "Tâm gửi câu trả lời."

    "Tháng thứ hai đã khiến vài lựa chọn bớt giống lựa chọn nhất thời."

    "Chúng bắt đầu giống cách cô thường sống."

    return
