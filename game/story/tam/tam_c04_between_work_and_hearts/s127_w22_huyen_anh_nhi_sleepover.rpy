# FILE: game/story/tam/tam_c04_between_work_and_hearts/s127_w22_huyen_anh_nhi_sleepover.rpy

label tam_c04_w22_s04_huyen_anh_nhi_sleepover:
    scene bg_c04_huyen_home_night
    with dissolve
    scene cg_tam_c04_huyen_nhi_huyen_home
    with dissolve
    "Ánh Nhi ngủ ở nhà Huyền đêm thứ hai. Chiếc bàn nhỏ đầy bút màu và tài liệu công ty bị đẩy sang một góc."
    scene bg_c04_huyen_home_night
    with dissolve
    anhni "Cô Huyền, bố cháu có hay làm cô tức không?"
    huyen neutral "Có."
    anhni "Thế sao cô vẫn giúp bố?"
    menu:
        "Huyền nói vì Quân đáng tin":
            $ story_add("huyen_quan_trust", 7)
            $ story_add("huyen_quan_interest", 3)
            $ story_flag("tam_c04_w22_huyen_says_quan_reliable")
            huyen neutral "Vì bố cháu khó chịu nhưng giữ lời."
        "Huyền nói vì Ánh Nhi":
            $ story_add("huyen_quan_trust", 5)
            $ story_flag("tam_c04_w22_huyen_says_for_anhni")
            huyen neutral "Vì cháu không ăn hành mà vẫn phải ăn tối."
        "Huyền đánh trống lảng":
            $ story_add("huyen_quan_interest", 3)
            $ story_flag("tam_c04_w22_huyen_avoids_anhni_question")
            huyen neutral "Trẻ con không được phỏng vấn người lớn lúc mười giờ."
    return
