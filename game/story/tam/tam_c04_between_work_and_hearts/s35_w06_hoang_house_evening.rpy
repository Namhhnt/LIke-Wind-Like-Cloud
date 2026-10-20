# FILE: game/story/tam/tam_c04_between_work_and_hearts/s35_w06_hoang_house_evening.rpy
# Week 06 — A quiet visit to Hoàng's house; affection appears through prepared space.

label tam_c04_w06_s04_hoang_house_evening:
    $ _tam_c04_w06_hoang_active = (
        story_has_flag("tam_c04_w05_tam_accepts_hoang_house_invitation")
        or story_has_flag("tam_c04_w05_tam_notices_hoang_no_exit")
        or story_has_flag("tam_c04_w05_focus_hoang")
        or story_state.get("tam_hoang_interest", 0) >= 65
    )

    if not _tam_c04_w06_hoang_active:
        $ story_add("career_hoang", 5)
        $ story_add("hoang_self_acceptance", 5)
        $ story_flag("tam_c04_w06_hoang_house_scene_skipped")
        return

    scene bg_hoangminh_villa_living_room_day
    with fade

    "Chiều thứ Năm, Tâm đến nhà Hoàng sau giờ làm."

    "Cổng mở trước khi cô kịp nhắn lần thứ hai."

    scene cg_tam_c04_hoang_home
    with dissolve
    "Trong phòng khách, một chiếc cốc đã đặt trên bàn. Nước nóng vừa đủ, không có đá."
    scene bg_hoangminh_villa_living_room_day
    with dissolve

    tam neutral "Anh chuẩn bị từ bao giờ?"

    hoang neutral "Trước khi em tới."

    tam teasing "Câu trả lời rất chính xác."

    "Hoàng kéo chiếc ghế không quay lưng ra cửa về phía cô."

    "Tâm dừng tay trên quai túi."

    menu:
        "Hỏi Hoàng có nhớ cả việc Tâm không thích ngồi quay lưng ra cửa":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_add("tam_observation", 5)
            $ story_sub("tam_insecurity", 3)
            $ story_flag("tam_c04_w06_tam_notices_hoang_seat")

            tam neutral "Anh nhớ cả chuyện này à?"

            hoang confused "Chuyện gì?"

            "Tâm đặt túi xuống chiếc ghế anh vừa kéo."

            tam smile "Không có gì."

            "Hoàng nhìn cô một lúc, rồi không hỏi tiếp."

        "Nói thẳng rằng căn nhà khiến Tâm thấy Hoàng khác ở công ty":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_add("hoang_self_acceptance", 5)
            $ story_flag("tam_c04_w06_tam_sees_hoang_at_home")

            tam neutral "Ở đây anh yên hơn."

            hoang neutral "Ở công ty anh ồn ào à?"

            tam teasing "Anh dùng nhiều lời hơn để giấu ít chuyện hơn."

            "Hoàng bật cười, cúi xuống chỉnh mép khăn trải bàn."

            hoang neutral "Còn ở đây?"

            tam neutral "Anh quên giấu vài thứ."

        "Giữ buổi tối nhẹ nhàng, không hỏi thêm":
            $ story_add("hoang_tam_trust", 5)
            $ story_add("tam_self_clarity", 3)
            $ story_add("hoang_self_acceptance", 3)
            $ story_flag("tam_c04_w06_tam_keeps_hoang_house_light")

            "Tâm ngồi xuống."

            "Hai người nói về một bộ phim dở, cây trong sân và cái tủ bếp đóng không khít."

            "Không câu nào quan trọng. Không câu nào cần được cố làm sâu."

    "Khi Tâm về, Hoàng đứng trong cổng cho đến khi xe cô rẽ khỏi con đường."

    "Anh không nhắn hỏi đã về chưa ngay."

    "Tin nhắn đến sau đó mười phút, đúng lúc Tâm vừa tháo giày."

    return
