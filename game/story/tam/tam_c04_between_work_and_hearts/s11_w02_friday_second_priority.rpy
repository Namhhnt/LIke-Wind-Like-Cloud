# FILE: game/story/tam/tam_c04_between_work_and_hearts/s11_w02_friday_second_priority.rpy
# Week 02 — The second priority choice confirms habits without locking routes.

label tam_c04_w02_s06_friday_second_priority:
    scene bg_company_open_office_day
    with dissolve

    scene cg_tam_c04_tam_work_evening
    with dissolve
    "Sáu giờ mười tám phút."
    scene bg_company_open_office_day
    with dissolve

    "Văn phòng chỉ còn tiếng điều hòa và vài bàn phím chưa chịu nghỉ."

    "Huyền gửi cho Tâm bản slide vừa sửa, kèm một dòng: xem giúp tao lần cuối."

    "Hoàng nhắn hỏi sáng mai cô có muốn đi ăn sáng không. Lần này anh thêm ngay phía sau: nếu em bận thì để tuần khác."

    "Quang gửi ảnh chiếc hộp giữ nhiệt đã được rửa sạch. Thiên An trả lại qua tài xế, không kèm lời nhắn."

    "Tab khóa học của Tâm còn một bài thực hành chưa nộp."

    "Các lựa chọn tuần trước đã quay lại. Không giống hệt. Chỉ gần giống đủ để thành thói quen."

    menu:
        "Nhận lời ăn sáng với Hoàng":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_sub("tam_insecurity", 3)
            $ story_add("huyen_quan_trust", 3)
            $ story_add("career_huyen", 3)
            $ story_add("thienan_quang_trust", 3)
            $ story_add("quang_persistence", 3)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 3)
            $ story_add_direction("tam", "tam_hoang_open")
            $ story_flag("tam_c04_w02_focus_hoang")

            "Tâm trả lời trước khi kịp cân nhắc câu chữ quá lâu."

            tam smile "Được. Nhưng em chọn chỗ."

            hoang "Anh đồng ý nhanh để em khỏi đổi ý."

            "Huyền vẫn tự sửa nốt slide. Quang vẫn phải tự hiểu chiếc hộp sạch có nghĩa gì."

        "Ở lại rà slide cùng Huyền":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_add("hoang_self_acceptance", 3)
            $ story_add("thienan_quang_trust", 3)
            $ story_add("quang_persistence", 3)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 3)
            $ story_add_direction("tam", "tam_support_huyen")
            $ story_flag("tam_c04_w02_focus_huyen")

            tam neutral "Gửi file gốc đây. Tao xem phần chuyển ý."

            huyen neutral "Biết ngay mày chưa về."

            tam teasing "Mày đang theo dõi tao à?"

            huyen irritated "Không. Chỉ người chưa về mới trả lời nhanh vậy."

            "Tin nhắn của Hoàng nằm yên thêm một lúc."

        "Chỉ góp ý một lần rồi để Huyền tự chốt với Quân":
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 1)
            $ story_add("career_huyen", 5)
            $ story_add("tam_observation", 5)
            $ story_add("hoang_self_acceptance", 3)
            $ story_add("thienan_quang_trust", 3)
            $ story_add("quang_persistence", 3)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 3)
            $ story_flag("tam_c04_w02_focus_huyen_quan")
            $ story_flag("tam_c04_w02_tam_steps_back_again")

            tam neutral "Slide bảy đang lặp ý. Còn lại mày tự chốt đi."

            huyen confused "Mày về thật à?"

            tam smile "Ừ. Mày biết anh Quân sẽ hỏi gì rồi mà."

            "Ba dấu chấm hiện lên khá lâu."

            huyen neutral "Biết một phần."

            tam neutral "Thế là đủ để bắt đầu."

        "Nhắc Quang đừng đọc quá nhiều vào chiếc hộp sạch":
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_add("huyen_quan_trust", 3)
            $ story_add("career_huyen", 3)
            $ story_add("hoang_self_acceptance", 3)
            $ story_add_direction("tam", "tam_support_quang_thienan")
            $ story_flag("tam_c04_w02_focus_quang_thienan")

            tam neutral "Hộp sạch chỉ có nghĩa là chị ấy đã dùng. Anh đừng tự viết thêm phần kết luận."

            quang "Anh biết."

            tam teasing "Anh mà biết thật thì đã không gửi ảnh cho em."

            "Quang không phủ nhận. Nhưng lần này anh cũng không hỏi Tâm nên làm gì tiếp."

        "Trêu Quang về chiếc nắp lệch lần trước":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 3)
            $ tam_c04_add_extended_score("quang_tam_awareness", 3)
            $ story_add("tam_observation", 5)
            $ story_add("quang_persistence", 3)
            $ story_flag("quang_tam_personal_attention")
            $ story_add("career_huyen", 3)
            $ story_add("hoang_self_acceptance", 3)
            $ story_flag("tam_c04_w02_focus_quang_personal")

            tam teasing "Lần này anh kiểm tra nắp chưa?"

            quang "Ba lần."

            tam smile "Em không biết nên thấy yên tâm hay thấy có lỗi."

            quang "Em chọn phương án im lặng cũng được."

            tam teasing "Anh biết là không được mà."

            "Câu trả lời của Quang đến chậm hơn một nhịp."

            quang "Ừ. Anh biết."

        "Nộp bài thực hành của mình":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_add("huyen_quan_trust", 3)
            $ story_add("career_huyen", 3)
            $ story_add("thienan_quang_trust", 3)
            $ story_add("quang_persistence", 3)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 3)
            $ story_add("hoang_self_acceptance", 3)
            $ story_add_direction("tam", "tam_career_focus")
            $ story_flag("tam_c04_w02_focus_career")

            "Tâm tắt các khung chat, mở bài thực hành còn dang dở."

            "Cô không làm vì giận ai hay muốn tránh ai."

            "Chỉ là có một phần đời của mình sẽ không tự tiến lên nếu cô cứ luôn đặt nó sau người khác."

            "Nút nộp bài chuyển sang màu xác nhận lúc sáu giờ năm mươi ba phút."

    "Tâm đóng laptop."

    "Trên bàn, túi bánh từ đầu tuần chỉ còn lại một chiếc khăn giấy chưa dùng."

    "Cô gấp nó làm đôi rồi cất vào ngăn kéo, không nghĩ nhiều về lý do."

    "Cuối tuần lại mở ra. Lần này, nó không còn hoàn toàn trống."

    return
