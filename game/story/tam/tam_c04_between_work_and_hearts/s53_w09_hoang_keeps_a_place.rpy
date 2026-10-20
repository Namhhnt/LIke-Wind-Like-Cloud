# Week 09 — Hoàng reserves a place without assuming Tâm must fill it.
label tam_c04_w09_s03_hoang_keeps_a_place:
    $ _active = story_state.get("tam_hoang_interest", 0) >= 55 or story_has_flag("tam_c04_m02_hoang_holding") or story_has_flag("tam_c04_m02_hoang_deepening")
    if not _active:
        $ story_add("career_hoang", 5)
        $ story_add("hoang_self_acceptance", 3)
        $ story_flag("tam_c04_w09_hoang_scene_skipped")
        return

    scene bg_hoangminh_villa_living_room_day
    with dissolve
    "Tối thứ Tư, trên bàn ăn nhà Hoàng có hai bộ bát đũa."
    scene cg_tam_c04_hoang_home
    with dissolve
    "Bộ thứ hai chưa được dọn thức ăn. Chỉ có một cốc nước ấm."
    scene bg_hoangminh_villa_living_room_day
    with dissolve
    tam neutral "Anh chuẩn bị trước à?"
    hoang neutral "Anh để chỗ. Chuẩn bị khác."
    tam confused "Khác thế nào?"
    hoang neutral "Nếu em không tới, chỗ đó vẫn chỉ là một cái ghế."

    menu:
        "Ngồi xuống mà không hỏi thêm":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_sub("tam_insecurity", 3)
            $ story_flag("tam_c04_w09_tam_takes_hoang_kept_place")
            "Tâm kéo ghế."
            "Hoàng mới quay vào bếp lấy bát canh."

        "Nói Hoàng có thể chuẩn bị phần của Tâm từ lần sau":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_add("hoang_self_acceptance", 5)
            $ story_add("tam_self_clarity", 3)
            $ story_flag("tam_c04_w09_tam_allows_hoang_to_expect")
            tam neutral "Lần sau anh cứ chuẩn bị phần em. Nếu không đến, em sẽ báo."
            "Hoàng dừng tay ở quai nồi."
            hoang neutral "Được."

        "Nói hôm nay Tâm chỉ ghé một lúc":
            $ story_add("hoang_tam_trust", 5)
            $ story_add("career_tam", 5)
            $ story_add("tam_self_clarity", 3)
            $ story_flag("tam_c04_w09_tam_keeps_visit_short")
            tam neutral "Em chỉ ở lại một lúc."
            hoang neutral "Anh biết. Canh còn nóng là đủ."

    "Chiếc ghế không còn trống."
    "Hoàng vẫn không nhìn nó như một điều hiển nhiên."
    return
