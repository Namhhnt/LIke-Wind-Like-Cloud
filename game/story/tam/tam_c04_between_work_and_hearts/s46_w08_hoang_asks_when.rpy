# FILE: game/story/tam/tam_c04_between_work_and_hearts/s46_w08_hoang_asks_when.rpy
# Week 08 — Hoàng asks when, not whether.

label tam_c04_w08_s03_hoang_asks_when:
    $ _tam_c04_w08_hoang_active = (
        story_has_flag("tam_c04_w07_focus_hoang")
        or story_has_flag("tam_c04_w07_tam_admits_skipped_lunch_to_hoang")
        or story_has_flag("tam_c04_w07_tam_teases_hoang_observation")
        or story_state.get("tam_hoang_interest", 0) >= 70
    )

    if not _tam_c04_w08_hoang_active:
        $ story_add("career_hoang", 5)
        $ story_add("hoang_self_acceptance", 5)
        $ story_flag("tam_c04_w08_hoang_asks_when_skipped")
        return

    scene bg_company_lobby_afternoon
    with dissolve

    "Chiều thứ Tư, Hoàng nhắn: hôm nay em tan làm lúc mấy giờ?"

    "Không có câu hỏi em có muốn gặp không."

    scene cg_tam_c04_hoang_lobby
    with dissolve
    "Tâm xuống sảnh lúc sáu giờ hai mươi."
    scene bg_company_lobby_afternoon
    with dissolve

    hoang neutral "Anh đoán gần đúng."

    tam teasing "Nếu em nói tám giờ thì sao?"

    hoang neutral "Anh quay lại lúc tám giờ."

    menu:
        "Nói Tâm thích việc Hoàng bắt đầu tin cô sẽ xuất hiện":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_add("hoang_self_acceptance", 5)
            $ story_sub("tam_insecurity", 3)
            $ story_flag("tam_c04_w08_tam_says_hoang_trusts_her_arrival")

            tam neutral "Anh bắt đầu tin em sẽ xuống rồi à?"

            hoang neutral "Anh đang tập."

            tam smile "Tập tốt đấy."

        "Hỏi Hoàng có sợ mình đang tiến quá nhanh không":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_c04_w08_tam_asks_hoang_pace")

            tam neutral "Anh không sợ mình đi nhanh quá à?"

            "Hoàng nhìn cô, rồi nhìn cửa kính phía sau."

            hoang neutral "Có. Nhưng đi chậm không có nghĩa là phải đứng yên."

        "Nói hôm nay Tâm chỉ có ba mươi phút":
            $ story_add("hoang_tam_trust", 5)
            $ story_add("career_tam", 5)
            $ story_add("tam_self_clarity", 3)
            $ story_flag("tam_c04_w08_tam_gives_hoang_thirty_minutes")

            tam neutral "Em chỉ có ba mươi phút."

            hoang neutral "Vậy mình dùng hai mươi lăm."

            tam confused "Còn năm phút?"

            hoang smile "Để em về đúng giờ."

    "Hoàng đi bên cạnh Tâm."

    "Không ai gọi đó là một cuộc hẹn."

    "Cũng không còn giống một cuộc gặp tình cờ."

    return
