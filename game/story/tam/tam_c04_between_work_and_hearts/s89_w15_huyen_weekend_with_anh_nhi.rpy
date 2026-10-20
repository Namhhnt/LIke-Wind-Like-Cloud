# FILE: game/story/tam/tam_c04_between_work_and_hearts/s89_w15_huyen_weekend_with_anh_nhi.rpy

label tam_c04_w15_s04_huyen_weekend_with_anh_nhi:
    scene bg_c04_huyen_home_day
    with dissolve
    "Thứ Bảy, Ánh Nhi ôm gối đứng trước cửa căn hộ Huyền."
    anhni "Bố cháu nói tối mai mới về."
    huyen surprised "Bố cháu nói với cháu hay nhắn mỗi một dòng cho cô?"
    anhni "Cả hai."
    "Huyền tránh sang một bên."
    menu:
        "Để Ánh Nhi ở nhà Huyền cuối tuần":
            $ story_add("huyen_quan_trust", 7)
            $ story_add("huyen_quan_interest", 3)
            $ story_add("career_huyen", 3)
            $ story_flag("tam_c04_w15_anhni_stays_huyen_home")
            huyen neutral "Vào đi. Nhưng không được kể với bố cháu là cô cho ăn mì."
        "Đề nghị Tâm ở lại phụ một tối":
            $ story_add("career_tam", 3)
            $ story_add("career_huyen", 3)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 5)
            $ story_flag("tam_c04_w15_tam_stays_with_huyen_anhni")
            anhni "Cô Tâm có biết làm bài toán không?"
            tam neutral "Tùy bài."
        "Hỏi Ánh Nhi có nhớ bố không":
            $ story_add("tam_observation", 5)
            $ story_add("huyen_quan_trust", 3)
            $ story_flag("tam_c04_w15_anhni_says_missing_quan")
            anhni "Có. Nhưng bố đi làm thì sẽ về."
            "Huyền quay đi lấy thêm một chiếc cốc."
    return
