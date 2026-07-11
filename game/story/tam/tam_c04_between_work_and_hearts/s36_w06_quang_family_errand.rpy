# FILE: game/story/tam/tam_c04_between_work_and_hearts/s36_w06_quang_family_errand.rpy
# Week 06 — Quang takes over a small family errand and Tâm notices where he belongs.

label tam_c04_w06_s05_quang_family_errand:
    scene black
    with dissolve

    "Tối thứ Năm, mẹ Tâm nhờ người tới lấy một bộ giấy tờ."

    "Quang đến trước giờ hẹn mười phút."

    "Anh biết chìa khóa ngăn kéo nào bị kẹt. Biết bìa hồ sơ màu nào Thiên An đã dùng. Biết mẹ Tâm sẽ hỏi anh có ăn tối không."

    "Tâm đứng tựa cửa bếp, nhìn anh tìm đúng tập giấy mà không cần ai chỉ."

    menu:
        "Bảo Quang tự giao tận tay Thiên An":
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_add_direction("quang", "quang_thienan_open")
            $ story_add_direction("thienan", "thienan_quang_open")
            $ story_flag("tam_c04_w06_tam_sends_quang_directly_to_thienan")

            tam neutral "Anh mang tới tận nơi đi. Đừng gửi qua trợ lý."

            quang "Muộn rồi."

            tam neutral "Anh đã tới đây lúc muộn rồi."

            "Quang nhìn đồng hồ, sau đó cầm thêm chiếc áo khoác."

        "Hỏi từ bao giờ Quang biết nhà này rõ hơn Tâm nghĩ":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 5)
            $ tam_c04_add_extended_score("quang_tam_awareness", 5)
            $ story_add("tam_observation", 5)
            $ story_add_direction("quang", "quang_tam_open")
            $ story_flag("tam_c04_w06_tam_notices_quang_family_place")

            tam neutral "Anh nhớ cả ngăn kéo này à?"

            quang "Anh từng sửa nó."

            tam confused "Bao giờ?"

            quang "Lúc em còn học đại học."

            "Tâm không nhớ ngày đó. Quang thì nhớ chiếc ngăn kéo."

        "Đưa hồ sơ cho Quang rồi quay lại công việc":
            $ story_add("career_tam", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 3)
            $ story_add("thienan_quang_trust", 3)
            $ story_flag("tam_c04_w06_tam_keeps_family_errand_practical")

            tam neutral "Đủ giấy rồi. Anh kiểm tra lại giúp em."

            "Quang gật đầu."

            "Trước khi đi, anh đặt một hộp thức ăn cạnh laptop của Tâm mà không nói."

    "Cửa khép lại."

    "Trên bàn vẫn còn một chiếc ghế được kéo ra rồi chưa đẩy vào."

    return
