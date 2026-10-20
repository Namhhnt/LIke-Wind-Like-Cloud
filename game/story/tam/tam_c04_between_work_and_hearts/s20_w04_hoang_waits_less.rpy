# FILE: game/story/tam/tam_c04_between_work_and_hearts/s20_w04_hoang_waits_less.rpy
# Week 04 — Hoàng becomes more direct without becoming demanding.

label tam_c04_w04_s03_hoang_waits_less:
    $ _tam_c04_w04_hoang_active = (
        story_has_flag("tam_c04_w03_focus_hoang")
        or story_has_flag("tam_c04_w03_tam_keeps_short_plan_with_hoang")
        or story_has_flag("tam_c04_w03_tam_honest_about_exhaustion")
        or story_state.get("tam_hoang_interest", 0) >= 60
        or story_state.get("hoang_tam_trust", 0) >= 55
    )

    if not _tam_c04_w04_hoang_active:
        $ story_add("career_hoang", 3)
        $ story_add("hoang_self_acceptance", 3)
        $ story_flag("tam_c04_w04_hoang_scene_skipped")
        return

    scene bg_company_lobby_afternoon
    with dissolve

    "Chiều thứ Tư, Hoàng không nhắn rằng anh đang ở gần."

    "Anh nhắn thẳng: sáu giờ anh chờ em ở quán lần trước. Nếu họp kéo dài thì báo anh đổi giờ."

    "Tâm đọc lại hai lần. Không có đường lui được đặt sẵn. Chỉ có cách xử lý nếu kế hoạch thay đổi."

    "Cô xuống sảnh đúng giờ hơn dự kiến năm phút."

    scene cg_tam_c04_hoang_lobby
    with dissolve
    "Hoàng đã đứng ngoài cửa, nhưng lần này không mang túi giấy hay một lý do nào khác."
    scene bg_company_lobby_afternoon
    with dissolve

    tam teasing "Hôm nay không mua dư gì à?"

    hoang smile "Anh hết ngân sách cho lời khai giả rồi."

    menu:
        "Nói rằng Tâm thích cách anh rủ lần này hơn":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_add("hoang_self_acceptance", 5)
            $ story_flag("tam_c04_w04_tam_likes_hoang_directness")

            tam neutral "Em thích cách anh nói lần này hơn."

            hoang confused "Ít đáng ngờ hơn à?"

            tam smile "Ít giống như anh đã chuẩn bị sẵn để em từ chối."

            "Hoàng nhìn cô, nụ cười dịu đi một chút."

            hoang neutral "Anh đang sửa."

        "Trêu rằng Hoàng đã bớt phòng thủ":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("tam_observation", 5)
            $ story_add("hoang_self_acceptance", 3)
            $ story_flag("tam_c04_w04_tam_teases_hoang_less_defensive")

            tam teasing "Hôm nay anh không chừa sẵn đường chạy nữa à?"

            hoang teasing "Có. Nhưng anh giấu kỹ hơn."

            tam smile "Tiến bộ rồi."

            hoang neutral "Anh sẽ nhận lời khen trước khi em đổi ý."

        "Giữ cuộc hẹn ngắn vì còn việc tháng sau":
            $ story_add("hoang_tam_trust", 5)
            $ story_add("career_tam", 5)
            $ story_add("tam_self_clarity", 3)
            $ story_flag("tam_c04_w04_tam_sets_boundary_with_hoang")

            tam neutral "Em đi được, nhưng tám giờ em phải về xem brief mới."

            hoang neutral "Được. Bảy giờ năm mươi anh nhắc."

            tam confused "Anh không thấy mất hứng à?"

            hoang neutral "Có giới hạn rõ còn dễ chịu hơn để em ngồi đó mà đầu ở chỗ khác."

    "Hai người bước ra ngoài."

    "Hoàng không đi trước để dẫn đường, cũng không chậm lại quá rõ để chờ."

    "Anh chỉ giữ một khoảng vừa đủ để Tâm đi cạnh."

    return
