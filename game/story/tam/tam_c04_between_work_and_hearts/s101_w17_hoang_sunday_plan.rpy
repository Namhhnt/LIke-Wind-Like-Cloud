# FILE: game/story/tam/tam_c04_between_work_and_hearts/s101_w17_hoang_sunday_plan.rpy

label tam_c04_w17_s05_hoang_sunday_plan:
    $ _active = story_state.get("tam_hoang_interest", 0) >= 60
    if not _active:
        return
    scene bg_luxury_restaurant_evening
    with dissolve
    hoang neutral "Chủ Nhật anh muốn đưa em đi một nơi. Không phải nhà anh. Không phải việc công ty."
    tam neutral "Nghe như anh đã loại hết cớ."
    hoang neutral "Ừ. Còn lại mỗi việc anh muốn đi cùng em."
    menu:
        "Giữ Chủ Nhật":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_flag("tam_c04_w17_tam_keeps_hoang_sunday")
            tam neutral "Em sẽ giữ."
        "Nói Tâm cần trả lời sau khi nói chuyện với Quang":
            $ story_add("tam_self_clarity", 7)
            $ story_sub("hoang_tam_trust", 3)
            $ story_flag("tam_c04_w17_tam_names_quang_before_hoang")
            "Hoàng im một lúc."
            hoang neutral "Ít nhất lần này em nói thật."
        "Từ chối để không giữ Hoàng trong mập mờ":
            $ story_add("hoang_self_acceptance", 7)
            $ story_add("tam_self_clarity", 7)
            $ story_flag("tam_c04_w17_tam_releases_hoang")
            tam neutral "Em không nên nhận lời khi chưa biết mình sẽ đến với tâm trạng nào."
            hoang neutral "Anh hiểu."
    return
