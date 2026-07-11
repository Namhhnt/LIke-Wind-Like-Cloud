# FILE: game/story/tam/tam_c04_between_work_and_hearts/s100_w17_huyen_knows_the_house.rpy

label tam_c04_w17_s04_huyen_knows_the_house:
    scene black
    with dissolve
    "Huyền quay lại nhà Quân để trả chìa khóa dự phòng."
    "Cô biết bình nước ở ngăn nào, thuốc dị ứng của Ánh Nhi nằm đâu, chiếc đèn hành lang hay chập lúc mưa."
    quan neutral "Cô có thể giữ chìa khóa."
    huyen surprised "Anh không sợ em bán nhà à?"
    quan neutral "Cô sẽ mất thời gian kê khai tài sản."
    menu:
        "Huyền nhận chìa khóa":
            $ story_add("huyen_quan_trust", 7)
            $ story_add("huyen_quan_interest", 5)
            $ story_flag("tam_c04_w17_huyen_keeps_quan_key")
            huyen neutral "Em giữ vì Ánh Nhi."
            quan neutral "Tôi không hỏi lý do."
        "Huyền chỉ nhận khi Quân đi công tác":
            $ story_add("huyen_quan_trust", 5)
            $ story_add("career_huyen", 3)
            $ story_flag("tam_c04_w17_huyen_key_for_trips_only")
        "Huyền trả lại nhưng ghi mã khóa":
            $ story_add("huyen_quan_trust", 3)
            $ story_add("tam_observation", 3)
            $ story_flag("tam_c04_w17_huyen_keeps_boundary")
    return
