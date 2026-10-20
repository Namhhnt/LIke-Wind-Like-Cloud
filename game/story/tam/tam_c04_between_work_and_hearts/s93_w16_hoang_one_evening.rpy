# FILE: game/story/tam/tam_c04_between_work_and_hearts/s93_w16_hoang_one_evening.rpy

label tam_c04_w16_s03_hoang_one_evening:
    $ _active = story_state.get("tam_hoang_interest", 0) >= 60
    if not _active:
        return
    scene bg_luxury_restaurant_evening
    with dissolve
    scene cg_tam_c04_hoang_restaurant
    with dissolve
    "Hoàng đến trước nhưng không gọi món. Tâm ngồi xuống đúng giờ."
    scene bg_luxury_restaurant_evening
    with dissolve
    hoang neutral "Anh đã nghĩ em sẽ lại quên."
    tam neutral "Em cũng nghĩ vậy."
    hoang neutral "Nhưng em vẫn tới."
    menu:
        "Nói Tâm muốn giữ một chỗ thật cho Hoàng":
            $ story_add("tam_hoang_interest", 7)
            $ story_add("hoang_tam_trust", 7)
            $ story_sub("tam_insecurity", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_c04_w16_hoang_ready")
            tam neutral "Em không muốn anh chỉ là người em gặp khi xong hết mọi việc."
            hoang neutral "Vậy mình đừng xếp anh sau mọi việc nữa."
        "Nói Tâm vẫn chưa đủ chắc":
            $ story_add("hoang_tam_trust", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_c04_w16_hoang_still_waits_for_answer")
            tam neutral "Em chưa đủ chắc để gọi nó là gì."
            hoang neutral "Anh có thể chờ câu trả lời. Không chờ sự im lặng."
        "Chỉ cảm ơn vì Hoàng vẫn đến":
            $ story_add("tam_hoang_interest", 3)
            $ story_add("hoang_self_acceptance", 5)
            $ story_flag("tam_c04_w16_hoang_kind_but_unresolved")
            hoang neutral "Anh đến vì muốn gặp em. Không phải vì tốt bụng."
    return
