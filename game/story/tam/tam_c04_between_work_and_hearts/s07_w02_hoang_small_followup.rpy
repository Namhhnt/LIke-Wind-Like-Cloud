# FILE: game/story/tam/tam_c04_between_work_and_hearts/s07_w02_hoang_small_followup.rpy
# Week 02 — Hoàng follows up without making his invitation a demand.

label tam_c04_w02_s02_hoang_small_followup:
    $ _tam_c04_w02_hoang_active = (story_has_flag("tam_c04_w01_first_focus_hoang") or story_state.get("tam_hoang_interest", 0) >= 50 or story_state.get("hoang_tam_trust", 0) >= 45)

    if not _tam_c04_w02_hoang_active:
        $ story_add("career_hoang", 3)
        $ story_add("hoang_self_acceptance", 3)
        $ story_flag("tam_c04_w02_hoang_scene_skipped")
        return

    scene bg_company_lobby_afternoon
    with dissolve

    "Chiều thứ Ba, Hoàng nhắn rằng anh đang ở gần công ty."

    "Khi Tâm xuống sảnh, anh đứng cạnh cửa kính với một túi giấy nhỏ trên tay."

    tam confused "Anh thật sự mua dư à?"

    hoang smile "Anh đang cố giữ lời khai nhất quán."

    "Hoàng đưa túi bánh cho cô. Miệng túi được gấp hai lần, ngay ngắn quá mức cần thiết."

    tam teasing "Nếu em không xuống thì sao?"

    hoang neutral "Anh mang về."

    tam neutral "Không giận à?"

    "Hoàng nhìn cô một thoáng, rồi quay sang dòng xe ngoài cửa."

    hoang neutral "Anh rủ em vì muốn gặp. Không phải để em mắc nợ một câu trả lời."

    "Câu nói được đặt xuống nhẹ như túi bánh giữa hai người."

    menu:
        "Ở lại nói chuyện với Hoàng thêm một lúc":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_sub("tam_insecurity", 3)
            $ story_flag("tam_c04_w02_tam_stays_with_hoang")

            tam smile "Em còn mười phút."

            hoang teasing "Mười phút nghe hơi giống lịch gặp khách hàng."

            tam teasing "Khách hàng không được ăn bánh của mình trước."

            "Hoàng mở túi, lấy ra một chiếc bánh nhỏ hơn."

            hoang smile "Vậy anh yên tâm rồi. Phân loại quan hệ khá rõ."

            "Hai người đứng cạnh cửa kính, chia nhau thứ vốn được khai là mua dư."

        "Nhận bánh rồi quay lại làm việc":
            $ story_add("hoang_tam_trust", 3)
            $ story_add("career_tam", 5)
            $ story_add("hoang_self_acceptance", 3)
            $ story_flag("tam_c04_w02_tam_returns_to_work_from_hoang")

            tam neutral "Em phải lên lại. Chiều nay còn một buổi review."

            hoang neutral "Ừ. Anh chỉ ghé đưa cái này thôi."

            tam teasing "Lần sau đừng mua dư nhiều quá."

            hoang smile "Anh sẽ cố tính chính xác hơn."

            "Anh không giữ cô lại. Nhưng lúc cửa thang máy khép, Tâm vẫn còn thấy anh đứng nguyên chỗ cũ."

        "Hỏi thẳng vì sao Hoàng luôn để đường lui":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("tam_observation", 5)
            $ story_add("hoang_self_acceptance", 5)
            $ story_flag("tam_c04_w02_tam_asks_hoang_about_distance")

            tam neutral "Anh lúc nào cũng để sẵn đường lui vậy à?"

            hoang confused "Cho ai?"

            tam neutral "Cho cả hai."

            "Hoàng giữ im lặng một nhịp. Ngón tay anh vuốt lại nếp gấp trên túi giấy."

            hoang neutral "Có lẽ vì anh không muốn người khác ở lại chỉ vì khó từ chối."

            tam neutral "Thế nếu người ta muốn ở lại thật thì sao?"

            hoang smile "Thì anh sẽ phải học cách tin."

    "Tâm mang túi bánh lên văn phòng."

    "Đến lúc đặt nó xuống bàn, cô mới thấy bên trong có hai chiếc khăn giấy được gấp riêng."

    "Một chi tiết nhỏ. Không cần thiết. Nhưng rõ ràng đã được nhớ tới."

    return
