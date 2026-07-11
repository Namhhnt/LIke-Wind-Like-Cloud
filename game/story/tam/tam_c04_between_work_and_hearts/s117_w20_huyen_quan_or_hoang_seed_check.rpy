# FILE: game/story/tam/tam_c04_between_work_and_hearts/s117_w20_huyen_quan_or_hoang_seed_check.rpy

label tam_c04_w20_s04_huyen_quan_or_hoang_seed_check:
    scene bg_company_open_office_day
    with dissolve
    if tam_c04_huyen_quan_deep_trust_ready():
        "Quân đưa Huyền lịch công tác tháng sau và lịch học của Ánh Nhi trong cùng một email."
        huyen neutral "Anh gộp hai file này làm gì?"
        quan neutral "Vì cả hai đều liên quan tới cô."
        menu:
            "Huyền nhận trách nhiệm mà không đùa":
                $ tam_c04_commit_huyen_quan_deep_trust()
                $ story_add("huyen_quan_trust", 7)
                $ story_add("huyen_quan_interest", 3)
                $ story_flag("tam_c04_w20_huyen_accepts_deep_trust")
                huyen neutral "Em sẽ sắp xếp."
            "Huyền chỉ nhận phần công việc":
                $ story_add("career_huyen", 7)
                $ story_add("huyen_quan_trust", 3)
                $ story_flag("tam_c04_w20_huyen_keeps_professional_boundary")
    else:
        "Huyền và Hoàng cùng chờ Tâm ngoài công ty, nói chuyện về một bản thiết kế khách hàng vừa trả lại."
        $ story_add("huyen_hoang_interest", 3)
        $ story_add("hoang_huyen_interest", 3)
        $ story_flag("tam_c04_w20_huyen_hoang_friend_lane_visible")
    return
