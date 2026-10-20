# FILE: game/story/tam/tam_c04_between_work_and_hearts/s78_w13_hoang_fixed_evening.rpy

label tam_c04_w13_s03_hoang_fixed_evening:
    $ _active = story_state.get("tam_hoang_interest", 0) >= 55
    if not _active:
        $ story_add("career_hoang", 5)
        $ story_add("hoang_self_acceptance", 5)
        $ story_flag("tam_c04_w13_hoang_keeps_friend_distance")
        return
    scene bg_luxury_restaurant_evening
    with dissolve
    scene cg_tam_c04_hoang_restaurant
    with dissolve
    "Hoàng đặt cốc nước sang phía Tâm. Không hỏi cô có bận cuối tuần không."
    scene bg_luxury_restaurant_evening
    with dissolve
    hoang neutral "Tối thứ Tư. Một tiếng. Nếu em không tới được, báo trước."
    tam neutral "Anh đang đặt lịch với em à?"
    hoang neutral "Ừ. Anh không muốn tiếp tục sống bằng phần thời gian còn thừa của em."
    menu:
        "Giữ tối thứ Tư cho Hoàng":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_sub("tam_insecurity", 3)
            $ story_flag("tam_c04_w13_hoang_fixed_evening_kept")
            tam neutral "Được. Nếu có thay đổi em sẽ báo."
            hoang neutral "Thế là đủ."
        "Nói Tâm chưa thể hứa đều đặn":
            $ story_add("hoang_tam_trust", 3)
            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_c04_w13_hoang_fixed_evening_uncertain")
            tam neutral "Em chưa biết mình có giữ được đều như vậy không."
            hoang neutral "Vậy đừng hứa đều. Chỉ cần đừng biến mất."
        "Đánh trống lảng bằng chuyện chuyến công tác":
            $ story_add("tam_observation", 3)
            $ story_add("hoang_self_acceptance", 5)
            $ story_flag("tam_c04_w13_tam_avoids_hoang_schedule")
            tam neutral "Tuần này ai cũng đi đâu đó nhỉ."
            hoang neutral "Em đang ở đây. Anh đang hỏi chuyện đó."
    return
