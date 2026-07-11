label tam_c04_w12_s05_huyen_after_quarter_review:
    scene bg_company_open_office_day
    with dissolve
    "Sau giờ làm, Huyền vẫn ngồi lại với bản đánh giá."
    "Quân đi ngang qua, đặt một cốc nước xuống bàn cô."
    quan neutral "Đừng đọc lại lần thứ tư. Nội dung không đổi."
    huyen neutral "Em đang kiểm tra xem anh có cài câu nào khó chịu giữa các dòng không."
    quan neutral "Có. Nhưng em đã đọc thấy từ lần đầu."
    menu:
        "Để Tâm về trước":
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 5)
            $ story_add("career_huyen", 5)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w12_tam_leaves_huyen_quan_after_review")
            tam neutral "Tao về trước."
            huyen neutral "Ừ."
            "Lần này cô không hỏi Tâm có chắc không."
        "Rủ Huyền về cùng":
            $ story_add("career_tam", 3)
            $ story_add("career_huyen", 3)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 3)
            $ story_flag("tam_c04_w12_tam_huyen_leave_together")
            tam neutral "Đọc nữa cũng không tăng rank đâu. Về thôi."
            huyen neutral "Chờ tao lưu file."
        "Hỏi Huyền vui vì kết quả hay vì người ký":
            $ story_add("huyen_quan_interest", 5)
            $ story_add("huyen_quan_trust", 3)
            $ story_add("tam_observation", 3)
            $ story_flag("tam_c04_w12_tam_asks_huyen_result_or_signer")
            tam teasing "Mày vui vì kết quả hay vì người ký?"
            huyen neutral "Tao vui vì mày sắp về rồi."
            quan neutral "Cửa ở phía sau."
    return
