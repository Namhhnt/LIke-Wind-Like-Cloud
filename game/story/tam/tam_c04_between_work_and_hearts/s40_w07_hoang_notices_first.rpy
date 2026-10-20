# FILE: game/story/tam/tam_c04_between_work_and_hearts/s40_w07_hoang_notices_first.rpy
# Week 07 — Hoàng notices Tâm's exhaustion before she names it.

label tam_c04_w07_s03_hoang_notices_first:
    $ _tam_c04_w07_hoang_active = (
        story_has_flag("tam_c04_w06_focus_hoang")
        or story_has_flag("tam_c04_w06_tam_notices_hoang_seat")
        or story_has_flag("tam_c04_w06_tam_sees_hoang_at_home")
        or story_state.get("tam_hoang_interest", 0) >= 65
    )

    if not _tam_c04_w07_hoang_active:
        $ story_add("career_hoang", 5)
        $ story_add("hoang_self_acceptance", 5)
        $ story_flag("tam_c04_w07_hoang_notices_scene_skipped")
        return

    scene bg_company_lobby_afternoon
    with dissolve

    scene cg_tam_c04_hoang_lobby
    with dissolve
    "Chiều thứ Tư, Hoàng gặp Tâm ở sảnh."
    scene bg_company_lobby_afternoon
    with dissolve

    "Cô nói mình ổn trước khi anh hỏi."

    hoang neutral "Anh chưa hỏi."

    tam neutral "Mặt anh hỏi rồi."

    "Hoàng nhìn chiếc cúc tay áo Tâm cài lệch."

    "Anh không đưa tay sửa. Chỉ chỉ nhẹ."

    hoang neutral "Cúc."

    "Tâm nhìn xuống, tháo ra cài lại."

    menu:
        "Thừa nhận Tâm đã bỏ bữa trưa":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_sub("tam_insecurity", 3)
            $ story_flag("tam_c04_w07_tam_admits_skipped_lunch_to_hoang")

            tam neutral "Em chưa ăn trưa."

            hoang neutral "Anh biết."

            tam confused "Sao anh biết?"

            hoang neutral "Em trả lời nhanh hơn bình thường. Và cài sai cúc."

            "Hoàng đưa cô một túi bánh nhỏ."

        "Trêu rằng Hoàng quan sát quá kỹ":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("tam_observation", 5)
            $ story_add("hoang_self_acceptance", 5)
            $ story_flag("tam_c04_w07_tam_teases_hoang_observation")

            tam teasing "Anh nhìn em kỹ quá đấy."

            hoang neutral "Anh có thể giả vờ không thấy."

            tam smile "Muộn rồi."

            "Hoàng cười, nhưng không rút lại túi bánh."

        "Nói Tâm cần về làm tiếp":
            $ story_add("hoang_tam_trust", 5)
            $ story_add("career_tam", 5)
            $ story_add("tam_self_clarity", 3)
            $ story_flag("tam_c04_w07_tam_sets_work_boundary_with_hoang")

            tam neutral "Em phải về làm tiếp."

            hoang neutral "Được. Mang cái này theo."

            "Anh đưa túi bánh, không đề nghị đi cùng."

            hoang neutral "Ăn rồi làm."

    "Tâm cầm túi bánh."

    "Nó nhẹ. Nhưng đủ để cô nhận ra mình đã quên một việc nhỏ đến mức nào."

    return
