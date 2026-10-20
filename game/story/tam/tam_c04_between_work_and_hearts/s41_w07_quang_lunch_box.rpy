# FILE: game/story/tam/tam_c04_between_work_and_hearts/s41_w07_quang_lunch_box.rpy
# Week 07 — Quang returns for a lunch box and reveals which absence he noticed.

label tam_c04_w07_s04_quang_lunch_box:
    scene bg_tam_family_dining_room_evening
    with fade

    "Tối thứ Năm, Quang tới trả một tập giấy cho Thiên An."

    "Anh mang theo hộp thức ăn Tâm đã để quên trong xe anh từ tuần trước."

    tam confused "Em tưởng anh bảo em chưa trả hộp của anh."

    quang "Anh nhớ nhầm."

    tam teasing "Anh nhớ nhầm cái hộp, nhưng nhớ em chưa ăn hết à?"

    "Quang đặt hộp xuống."

    "Bên trong có thêm một phần trái cây mới."

    menu:
        "Hỏi Quang đang chăm Tâm hay chỉ giữ thói quen cũ":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 5)
            $ tam_c04_add_extended_score("quang_tam_awareness", 5)
            $ story_add("tam_observation", 5)
            $ story_add_direction("quang", "quang_tam_open")
            $ story_flag("tam_c04_w07_tam_asks_quang_old_habit")

            tam neutral "Anh đang chăm em hay chỉ làm theo thói quen?"

            "Quang im một nhịp."

            quang "Có khác nhau à?"

            tam neutral "Em đang hỏi anh."

            "Anh nhìn chiếc hộp, không nhìn cô."

            quang "Có lẽ anh cũng đang nghĩ."

        "Nhờ Quang mang phần còn lại cho Thiên An":
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_add_direction("quang", "quang_thienan_open")
            $ story_add_direction("thienan", "thienan_quang_open")
            $ story_flag("tam_c04_w07_tam_redirects_quang_lunch_to_thienan")

            tam neutral "Chị An cũng chưa ăn tối. Anh mang phần này lên đi."

            quang "Em không ăn?"

            tam neutral "Em có phần của em rồi."

            "Tâm đóng nắp hộp, đẩy túi còn lại về phía anh."

        "Cảm ơn rồi giữ câu hỏi lại":
            $ tam_c04_add_extended_score("quang_tam_warmth", 3)
            $ story_add("tam_self_clarity", 3)
            $ story_add("tam_observation", 3)
            $ story_flag("tam_c04_w07_tam_keeps_quang_question_unsaid")

            tam neutral "Cảm ơn anh."

            quang "Ừ."

            "Tâm mở hộp. Trái cây đã được cắt nhỏ hơn cách cô thường cắt."

    "Quang ngồi lại thêm năm phút."

    "Không ai nói năm phút đó là để chờ ai."

    return
