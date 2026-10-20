# FILE: game/story/tam/tam_c04_between_work_and_hearts/s79_w13_quan_asks_huyen_pickup.rpy

label tam_c04_w13_s04_quan_asks_huyen_pickup:
    scene bg_company_open_office_day
    with dissolve
    scene cg_tam_c04_huyen_quan_work
    with dissolve
    "Quân đứng cạnh bàn Huyền lâu hơn một nhịp. Trên tay anh không có tài liệu."
    scene bg_company_open_office_day
    with dissolve
    quan neutral "Chiều mai cô có thể ghé trường Trần Ánh Nhi không?"
    huyen surprised "Con gái anh?"
    quan neutral "Tôi có cuộc họp kéo dài. Người đón thường ngày đang nghỉ."
    "Huyền nhìn Tâm. Tâm cúi xuống màn hình."
    menu:
        "Để Huyền tự trả lời":
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 3)
            $ story_add("career_huyen", 5)
            $ story_flag("tam_c04_w13_huyen_accepts_pickup")
            huyen neutral "Anh gửi em giờ tan học và ảnh của con bé."
            quan neutral "Tôi gửi rồi."
        "Hỏi Quân vì sao lại tin Huyền":
            $ story_add("huyen_quan_trust", 3)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w13_tam_asks_quan_trust")
            tam neutral "Anh không có người khác à?"
            quan neutral "Có. Nhưng tôi hỏi cô ấy."
            "Huyền im hẳn."
        "Đề nghị đi cùng Huyền lần đầu":
            $ story_add("career_tam", 3)
            $ story_add("career_huyen", 3)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 3)
            $ story_flag("tam_c04_w13_tam_goes_pickup_first_time")
            tam neutral "Lần đầu để em đi cùng."
            huyen neutral "Tao tự đi được. Nhưng tùy mày."
    return
