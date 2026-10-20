# FILE: game/story/tam/tam_c04_between_work_and_hearts/s33_w06_quan_empty_chair.rpy
# Week 06 — Huyền realizes that Quân's absence changes the room.

label tam_c04_w06_s02_quan_empty_chair:
    scene bg_company_open_office_day
    with dissolve

    "Sáng thứ Ba, ghế của Quân trống."

    "Huyền làm việc nhanh hơn thường lệ trong một giờ đầu."

    scene cg_tam_c04_empty_chair
    with dissolve
    "Đến mười giờ, cô đứng dậy đi lấy nước rồi nhìn về phía chiếc ghế đó lần thứ ba."
    scene bg_company_open_office_day
    with dissolve

    tam neutral "Mày tìm gì à?"

    huyen neutral "Không."

    tam teasing "Ghế ổng không tự mọc chân về đâu."

    huyen irritated "Tao đang kiểm tra xem có ai review bản này chưa."

    tam neutral "Anh Quân bảo thứ Tư mới xem."

    huyen frustrated "Biết."

    "Cô ngồi xuống, tự khoanh đỏ một dòng trong tài liệu."

    menu:
        "Nói Huyền đã biết cách Quân sẽ review":
            $ story_add("career_huyen", 5)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 3)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w06_tam_says_huyen_knows_quan_review")

            tam neutral "Mày biết ổng sẽ hỏi gì rồi. Cứ làm như ổng đang ngồi đó."

            huyen neutral "Nghe đáng sợ."

            tam teasing "Nhưng hiệu quả."

            "Huyền kéo trang đầu lại, đổi thứ tự hai mục."

        "Ngồi review cùng Huyền":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 5)
            $ story_add("tam_self_clarity", 3)
            $ story_flag("tam_c04_w06_tam_reviews_with_huyen")

            tam neutral "Tao xem một lượt. Mày giữ quyết định cuối."

            huyen neutral "Được. Nhưng đừng sửa giọng văn của tao thành giọng mày."

            tam smile "Tao chưa đủ rảnh."

        "Không nói gì, để Huyền tự hoàn tất":
            $ story_add("career_huyen", 10)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 2)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w06_tam_leaves_huyen_with_empty_chair")

            "Tâm quay lại màn hình."

            "Mười lăm phút sau, Huyền tự gửi bản nháp cho Quân."

            "Cô nhìn trạng thái đã gửi lâu hơn mức cần thiết."

    "Buổi trưa, Huyền kéo ghế của mình lệch sang trái một chút."

    "Từ góc đó, cô không còn nhìn thẳng thấy chiếc ghế trống."

    return
