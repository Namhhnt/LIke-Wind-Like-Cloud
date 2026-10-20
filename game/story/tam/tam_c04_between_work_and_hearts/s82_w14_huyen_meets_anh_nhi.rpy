# FILE: game/story/tam/tam_c04_between_work_and_hearts/s82_w14_huyen_meets_anh_nhi.rpy

label tam_c04_w14_s02_huyen_meets_anh_nhi:
    scene bg_c04_school_gate
    with dissolve
    scene cg_tam_c04_school_pickup
    with dissolve
    "Ánh Nhi đứng trước cổng trường, ôm chiếc cặp lớn gần bằng nửa người."
    scene bg_c04_school_gate
    with dissolve
    anhni "Cô là đồng nghiệp của bố cháu à?"
    huyen neutral "Cô là người bố cháu tin là sẽ không làm mất cháu."
    anhni "Thế cô có biết nấu ăn không?"
    huyen neutral "Hai việc đó không liên quan."
    "Con bé nhìn cô thêm vài giây rồi đưa tay."
    menu:
        "Để Huyền tự xoay xở":
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 3)
            $ story_add("career_huyen", 5)
            $ story_flag("tam_c04_w14_huyen_handles_anhni_alone")
            "Tâm chỉ nhận được ảnh hai hộp cơm không còn hành lá."
        "Ghé qua mang đồ ăn":
            $ story_add("career_tam", 3)
            $ story_add("career_huyen", 3)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 3)
            $ story_flag("tam_c04_w14_tam_brings_food")
            tam neutral "Tao mua dư."
            huyen neutral "Ừ. Dư đúng hai phần."
        "Hỏi Ánh Nhi về Quân ở nhà":
            $ story_add("tam_observation", 5)
            $ story_add("huyen_quan_trust", 3)
            $ story_flag("tam_c04_w14_tam_learns_quan_home")
            anhni "Bố cháu hay để cơm nguội rồi quên ăn."
            "Huyền đóng nắp hộp hơi mạnh."
    $ story_flag("tam_c04_huyen_met_anh_nhi")
    return
