label tam_c04_w12_s04_quang_at_family_dinner:
    scene black
    with fade
    "Tối thứ Năm, trên bàn ăn có ba cái bát."
    "Quang đến đúng giờ, mang món Thiên An thích và loại trà Tâm thường uống."
    thienan neutral "Anh chuẩn bị kỹ nhỉ."
    quang "Anh đi ngang qua."
    tam teasing "Anh nên đổi câu khác rồi."
    "Quang đặt túi xuống."
    menu:
        "Để Quang ngồi cạnh Thiên An":
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_add_direction("quang", "quang_thienan_open")
            $ story_flag("tam_c04_w12_quang_sits_by_thienan")
            "Tâm kéo ghế phía đối diện."
            "Quang ngồi cạnh Thiên An mà không nhìn Tâm xin phép."
        "Hỏi Quang loại trà của Tâm cũng là tiện đường à":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 5)
            $ tam_c04_add_extended_score("quang_tam_awareness", 5)
            $ story_add("tam_self_clarity", 3)
            $ story_add_direction("quang", "quang_tam_open")
            $ story_flag("tam_c04_w12_tam_questions_quang_tea")
            tam neutral "Trà của em cũng tiện đường à?"
            quang "Không. Anh nhớ nên mua."
            "Thiên An đặt đũa xuống rất nhẹ."
        "Ngồi xuống và để bữa ăn tự trả lời":
            $ story_add("thienan_quang_trust", 3)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 3)
            $ tam_c04_add_extended_score("quang_tam_warmth", 3)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w12_family_dinner_unresolved")
            "Tâm rót trà."
            "Quang gắp món ăn về phía Thiên An trước, rồi đẩy cốc trà về phía Tâm."
    "Bữa cơm tiếp tục."
    "Ba người đều biết sự chu đáo không còn là một thứ vô danh."
    return
