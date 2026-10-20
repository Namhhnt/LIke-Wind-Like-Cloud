# Week 09 — Quân trusts Huyền's client response without rewriting it.
label tam_c04_w09_s05_huyen_send_it:
    scene bg_company_open_office_day
    with dissolve
    "Chiều thứ Sáu, Huyền đặt bản phản hồi khách hàng lên bàn Quân."
    scene cg_tam_c04_huyen_quan_work
    with dissolve
    "Anh đọc từ đầu đến cuối."
    scene bg_company_open_office_day
    with dissolve
    "Con trỏ chuột dừng ở dòng cuối, nhưng anh không sửa."
    quan neutral "Gửi đi."
    huyen confused "Anh không sửa gì à?"
    quan neutral "Em muốn tôi sửa gì?"
    huyen neutral "Không. Em chỉ hỏi."

    menu:
        "Để Huyền tự nhận lấy câu trả lời":
            $ story_add("career_huyen", 10)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 3)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w09_huyen_sends_without_quan_edit")
            "Tâm quay lại màn hình của mình."
            "Phía sau, tiếng nhấp chuột của Huyền vang lên một lần."

        "Nhắc Huyền kiểm tra attachment trước khi gửi":
            $ story_add("career_tam", 3)
            $ story_add("career_huyen", 5)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 3)
            $ story_add("huyen_quan_trust", 3)
            $ story_flag("tam_c04_w09_tam_checks_huyen_attachment")
            tam neutral "Attachment."
            huyen neutral "Biết rồi."
            quan neutral "Để cô ấy tự kiểm tra."

        "Trêu Huyền rằng hôm nay không có mực đỏ":
            $ story_add("huyen_quan_trust", 3)
            $ story_add("huyen_quan_interest", 5)
            $ story_add("tam_observation", 3)
            $ story_flag("tam_c04_w09_tam_teases_huyen_no_red_marks")
            tam teasing "Hôm nay bút đỏ nghỉ phép à?"
            huyen neutral "Im."
            quan neutral "Tôi dùng comment điện tử."
            "Huyền nhìn anh. Quân vẫn nhìn màn hình."

    "Mail được gửi lúc năm giờ mười hai."
    "Huyền kiểm tra hộp thư đến thêm hai lần dù không có lỗi báo về."
    return
