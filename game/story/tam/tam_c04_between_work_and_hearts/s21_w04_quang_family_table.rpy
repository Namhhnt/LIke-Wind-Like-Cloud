# FILE: game/story/tam/tam_c04_between_work_and_hearts/s21_w04_quang_family_table.rpy
# Week 04 — Quang occupies an old place at the family table, and Tâm sees it differently.

label tam_c04_w04_s04_quang_family_table:
    scene bg_tam_family_dining_room_evening
    with fade

    scene cg_tam_c04_family_table
    with dissolve
    "Tối thứ Năm, Thiên An trở về sau chuyến công tác ngắn."
    scene bg_tam_family_dining_room_evening
    with dissolve

    "Quang mang hồ sơ tới đúng lúc bữa cơm vừa được dọn. Mẹ Tâm giữ anh lại bằng một câu tự nhiên đến mức không ai kịp từ chối."

    "Anh ngồi ở vị trí gần đầu bàn, chỗ vẫn thường ngồi từ nhiều năm trước."

    "Không ai giới thiệu. Không ai hỏi anh ăn được gì. Bát cơm đã được đặt xuống trước khi anh kéo ghế."

    "Tâm nhìn cảnh đó và nhận ra có những người thân thuộc đến mức sự hiện diện của họ không tạo tiếng động."

    "Thiên An ăn chậm hơn thường lệ. Quang không hỏi chuyến đi thế nào, chỉ kéo đĩa thức ăn ít dầu lại gần cô."

    thienan neutral "Anh đừng làm như em bệnh."

    quang "Anh chưa nói gì."

    thienan neutral "Cách anh kéo đĩa nói rồi."

    "Quang dừng tay, nhưng không kéo đĩa lại."

    menu:
        "Đỡ lời để Quang và Thiên An bớt phòng thủ":
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_add("tam_observation", 3)
            $ story_add_direction("tam", "tam_support_quang_thienan")
            $ story_flag("tam_c04_w04_tam_supports_quang_at_family_table")

            tam teasing "Anh Quang kéo nhầm thôi. Nhưng chị ăn đi, kéo lại mất công."

            "Thiên An nhìn cô. Quang cúi xuống bát cơm để giấu một nụ cười rất nhẹ."

            thienan neutral "Hai người hợp nhau quá nhỉ."

            tam smile "Ở nhà lâu nên phối hợp tốt thôi."

        "Không chen vào cuộc đối đáp của hai người":
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_c04_w04_tam_leaves_quang_thienan_space")
            $ story_flag("quang_thienan_family_space")

            "Tâm cúi xuống gỡ một mảnh xương cá."

            "Một lúc sau, Thiên An vẫn gắp món từ chiếc đĩa Quang đã kéo tới."

            "Không ai nhắc lại câu vừa rồi."

            "Có lẽ họ không cần Tâm dịch mọi cử chỉ thành lời nữa."

        "Nhận ra Quang cũng luôn nhớ phần của Tâm":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 5)
            $ tam_c04_add_extended_score("quang_tam_awareness", 5)
            $ story_add("tam_observation", 5)
            $ story_add("quang_persistence", 3)
            $ story_flag("tam_c04_w04_tam_notices_quang_remembers_her_too")
            $ story_flag("quang_tam_remembers_small_habits")

            "Khi Tâm vừa đưa đũa về phía bát canh, Quang đã đặt chiếc muôi sang bên tay thuận của cô."

            "Một động tác không ai để ý. Chính cô cũng từng không để ý."

            tam neutral "Anh vẫn nhớ à?"

            quang "Nhớ gì?"

            tam neutral "Không có gì."

            "Tâm múc canh. Chiếc muôi nằm vừa tay đến mức câu hỏi của cô nghe hơi thừa."

    "Sau bữa cơm, Thiên An mang hồ sơ lên phòng. Quang đứng dậy định về."

    "Mẹ Tâm đưa anh một túi trái cây như mọi lần. Anh nhận như mọi lần."

    "Chỉ có Tâm nhìn theo lâu hơn mọi lần một chút."

    return
