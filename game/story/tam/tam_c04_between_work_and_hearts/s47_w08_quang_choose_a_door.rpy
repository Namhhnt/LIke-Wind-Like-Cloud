# FILE: game/story/tam/tam_c04_between_work_and_hearts/s47_w08_quang_choose_a_door.rpy
# Week 08 — Quang arrives and must choose which conversation he is actually seeking.

label tam_c04_w08_s04_quang_choose_a_door:
    scene black
    with fade

    "Tối thứ Năm, Quang đứng trước cửa nhà Tâm."

    "Anh mang một tập hồ sơ cho Thiên An và một hộp thức ăn cho Tâm."

    "Hai thứ nằm trên hai tay khác nhau."

    tam neutral "Anh đến gặp ai?"

    "Quang nhìn cô."

    "Câu hỏi vốn có thể trả lời rất dễ."

    menu:
        "Mở cửa và bảo Quang tự mang hồ sơ lên cho Thiên An":
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_add_direction("quang", "quang_thienan_open")
            $ story_add_direction("thienan", "thienan_quang_open")
            $ story_flag("tam_c04_w08_quang_chooses_thienan_door")

            tam neutral "Chị An ở trên. Anh tự mang lên đi."

            "Quang gật đầu."

            "Anh đưa hộp thức ăn cho Tâm, rồi bước vào mà không hỏi cô đi cùng."

        "Giữ Quang lại và hỏi câu trả lời thật":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 5)
            $ tam_c04_add_extended_score("quang_tam_awareness", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_add_direction("quang", "quang_tam_open")
            $ story_flag("tam_c04_w08_quang_chooses_tam_conversation")

            tam neutral "Hồ sơ là cho chị An. Còn anh đứng đây vì ai?"

            "Quang im lặng."

            quang "Anh chưa biết cách trả lời mà không làm mọi thứ khó hơn."

            tam neutral "Ít nhất anh biết câu hỏi rồi."

            quang "Ừ."

        "Nhận cả hai thứ rồi không ép Quang chọn":
            $ tam_c04_add_extended_score("quang_tam_warmth", 3)
            $ story_add("thienan_quang_trust", 3)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 3)
            $ story_add("tam_observation", 3)
            $ story_flag("tam_c04_w08_quang_door_unresolved")

            tam neutral "Đưa em. Em mang lên."

            quang "Tâm."

            tam neutral "Muộn rồi."

            "Quang buông tay khỏi tập hồ sơ chậm hơn bình thường."

    "Cánh cửa vẫn mở."

    "Chỉ có người đứng trước nó chưa chắc mình định bước vào căn phòng nào."

    return
