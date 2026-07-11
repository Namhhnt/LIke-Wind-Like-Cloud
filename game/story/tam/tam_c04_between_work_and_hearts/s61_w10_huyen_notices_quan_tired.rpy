label tam_c04_w10_s05_huyen_notices_quan_tired:
    scene bg_company_open_office_day
    with dissolve
    "Cuối ngày, Quân đọc cùng một dòng hai lần."
    "Huyền nhìn thấy trước Tâm."
    huyen neutral "Anh chưa ăn trưa à?"
    quan neutral "Không liên quan đến bản này."
    huyen neutral "Có. Anh đang đọc sai dòng."
    "Quân dừng lại."
    menu:
        "Để Huyền tự xử lý":
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 5)
            $ story_add("career_huyen", 5)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w10_huyen_sends_quan_to_eat")
            huyen neutral "Anh đi ăn. Em tự kiểm tra phần còn lại."
            quan neutral "Hai mươi phút."
        "Đưa cả hai phần đồ ăn còn lại":
            $ story_add("career_tam", 3)
            $ story_add("career_huyen", 3)
            $ story_add("huyen_quan_trust", 3)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 3)
            $ story_flag("tam_c04_w10_tam_shares_food")
            tam neutral "Hai người chia đi. Em không muốn review lại vì hạ đường huyết."
        "Trêu Huyền rằng cô để ý nhanh thật":
            $ story_add("huyen_quan_interest", 5)
            $ story_add("tam_observation", 3)
            $ story_flag("tam_c04_w10_tam_notices_huyen_notices_quan")
            tam teasing "Mày nhìn ra nhanh thế."
            huyen neutral "Ổng đọc sai dòng. Ai cũng thấy."
            "Quân không nói rằng Tâm chưa hề nhìn vào màn hình của anh."
    return
