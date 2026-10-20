# FILE: game/story/tam/tam_c04_between_work_and_hearts/s85_w14_friday_quiet_house.rpy

label tam_c04_w14_s05_friday_quiet_house:
    scene bg_c04_quan_home_night
    with fade
    "Cuối tuần, căn nhà của Quân sáng đèn nhưng yên hơn một căn nhà có trẻ con nên có."
    scene cg_tam_c04_huyen_nhi_quan_home
    with dissolve
    "Huyền gấp chiếc áo khoác nhỏ đặt trên ghế. Ánh Nhi ngủ trong phòng bên."
    scene bg_c04_quan_home_night
    with dissolve
    huyen tired "Tao cứ tưởng trông trẻ là giữ cho nó không chạy ra đường."
    tam neutral "Còn gì nữa?"
    huyen neutral "Nhớ nó không ăn hành. Nhớ mai có tiết mỹ thuật. Nhớ cái bình nước bị rò."
    menu:
        "Nói Quân đã giao Huyền cả những điều nhỏ":
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 3)
            $ story_add("tam_observation", 3)
            $ story_flag("tam_c04_w14_tam_names_quan_trust")
            huyen neutral "Đừng làm quá. Anh ấy hết người thôi."
        "Giúp Huyền chuẩn bị đồ sáng mai":
            $ story_add("career_tam", 3)
            $ story_add("career_huyen", 3)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 3)
            $ story_flag("tam_c04_w14_tam_helps_anhni_morning")
        "Để Huyền tự giữ nhịp của căn nhà":
            $ story_add("huyen_quan_trust", 5)
            $ story_add("career_huyen", 5)
            $ story_flag("tam_c04_w14_huyen_keeps_house_rhythm")
            "Tâm kéo cửa phòng khách khép lại. Không kín hẳn."
    return
