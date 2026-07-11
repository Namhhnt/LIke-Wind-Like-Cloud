label tam_c04_w11_s03_hoang_not_leftover_time:
    $ _active = story_state.get("tam_hoang_interest", 0) >= 55
    if not _active:
        $ story_add("career_hoang", 5)
        $ story_add("hoang_self_acceptance", 5)
        $ story_flag("tam_c04_w11_hoang_stops_reserving_time")
        return
    scene black
    with dissolve
    "Tối thứ Tư, Hoàng đặt điện thoại úp xuống bàn."
    hoang neutral "Anh hỏi một câu hơi khó nghe nhé."
    tam neutral "Anh đã báo trước rồi."
    hoang neutral "Anh đang nằm trong lịch của em, hay chỉ nằm ở phần thời gian còn lại?"
    "Tâm giữ tay trên thành cốc."
    menu:
        "Nói Hoàng đã có một chỗ riêng trong lịch":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_sub("tam_insecurity", 3)
            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_c04_w11_tam_gives_hoang_real_time")
            tam neutral "Có chỗ riêng. Chỉ là em vẫn đang học cách giữ nó."
            hoang neutral "Anh có thể làm việc với câu đó."
        "Thừa nhận Tâm chưa sắp được Hoàng vào cuộc sống của mình":
            $ story_add("hoang_tam_trust", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_c04_w11_tam_admits_hoang_leftover_time")
            tam neutral "Có lúc đúng là phần còn lại. Em không muốn nói dối."
            hoang neutral "Anh không cần câu dễ nghe. Anh cần biết mình đang đứng đâu."
        "Hỏi Hoàng có muốn lùi lại không":
            $ story_add("tam_hoang_interest", 3)
            $ story_add("hoang_self_acceptance", 5)
            $ story_add("tam_self_clarity", 3)
            $ story_flag("tam_c04_w11_tam_asks_hoang_step_back")
            tam neutral "Anh muốn lùi lại không?"
            hoang neutral "Nếu anh muốn, anh đã không hỏi."
    "Món ăn nguội đi một chút."
    "Không ai cố làm câu trả lời đẹp hơn mức nó có thể."
    return
