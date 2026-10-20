# FILE: game/story/tam/tam_c04_between_work_and_hearts/s14_w03_hoang_changed_plan.rpy
# Week 03 — Work pressure forces Tâm and Hoàng to negotiate a changed plan.

label tam_c04_w03_s03_hoang_changed_plan:
    $ _tam_c04_w03_hoang_active = (
        story_has_flag("tam_c04_w02_focus_hoang")
        or story_has_flag("tam_c04_w02_tam_stays_with_hoang")
        or story_state.get("tam_hoang_interest", 0) >= 55
        or story_state.get("hoang_tam_trust", 0) >= 50
    )

    if not _tam_c04_w03_hoang_active:
        $ story_add("career_hoang", 3)
        $ story_add("hoang_self_acceptance", 3)
        $ story_flag("tam_c04_w03_hoang_scene_skipped")
        return

    scene bg_company_lobby_afternoon
    with dissolve

    "Chiều thứ Tư, cuộc họp nội bộ kéo dài quá giờ."

    "Khi Tâm xuống sảnh, đồng hồ đã muộn hơn lịch hẹn với Hoàng gần bốn mươi phút."

    scene cg_tam_c04_hoang_lobby
    with dissolve
    "Anh ngồi ở hàng ghế cạnh cửa kính, một tay giữ điện thoại, tay kia đặt trên túi giấy chưa mở."
    scene bg_company_lobby_afternoon
    with dissolve

    tam worried "Em xin lỗi. Em nhắn mà không biết anh có thấy không."

    hoang neutral "Anh thấy."

    tam confused "Sao anh vẫn ngồi đây?"

    "Hoàng đứng lên, kéo quai túi giấy cho khỏi mắc vào cạnh ghế."

    hoang neutral "Vì anh chưa vội về. Không phải vì em bắt anh đợi."

    "Anh nói rõ đến mức câu xin lỗi thứ hai của Tâm tự dừng lại."

    menu:
        "Đổi kế hoạch thành một bữa ăn ngắn gần công ty":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_sub("tam_insecurity", 3)
            $ story_flag("tam_c04_w03_tam_keeps_short_plan_with_hoang")

            tam neutral "Em không đi xa được nữa. Nhưng gần đây có quán vẫn còn mở."

            hoang smile "Anh tưởng em sẽ bảo để hôm khác."

            tam smile "Em cũng tưởng vậy."

            "Hoàng không hỏi cô đổi ý vì áy náy hay vì muốn ở lại. Anh chỉ đưa túi giấy sang tay còn trống của mình rồi đi chậm lại cho bằng bước cô."

        "Nói thật rằng hôm nay Tâm đã hết sức":
            $ story_add("hoang_tam_trust", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_add("hoang_self_acceptance", 3)
            $ story_flag("tam_c04_w03_tam_honest_about_exhaustion")

            tam tired "Hôm nay em không còn nói chuyện tử tế nổi nữa."

            "Hoàng nhìn cô một lúc."

            hoang neutral "Vậy mình không cần cố biến hôm nay thành một buổi hẹn tốt."

            tam confused "Anh không khó chịu à?"

            hoang neutral "Có hơi tiếc. Khác với khó chịu."

            "Anh đưa túi giấy cho cô. Bên trong là phần ăn tối đã được đóng kín."

            hoang neutral "Mang về ăn. Lần sau em báo sớm hơn là được."

        "Hỏi Hoàng vì sao không về khi đã phải đợi":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("tam_observation", 5)
            $ story_add("hoang_self_acceptance", 5)
            $ story_flag("tam_c04_w03_tam_questions_hoang_waiting")

            tam neutral "Anh có thể về mà."

            hoang neutral "Ừ."

            tam neutral "Nhưng anh không về."

            "Hoàng nhìn qua cửa kính. Bên ngoài, một chiếc xe vừa rời khỏi lề đường."

            hoang neutral "Anh đang thử không rút lui chỉ vì kế hoạch lệch một chút."

            tam neutral "Khó không?"

            hoang smile "Khó vừa đủ để anh không muốn em cười."

            tam teasing "Muộn rồi."

    "Tâm nhìn chiếc ghế Hoàng vừa ngồi. Trên mặt ghế còn một vệt lõm rất nhẹ."

    "Bốn mươi phút không phải chuyện lớn. Nhưng đủ lâu để một người có thể chọn rời đi."

    "Hoàng đã không làm vậy."

    return
