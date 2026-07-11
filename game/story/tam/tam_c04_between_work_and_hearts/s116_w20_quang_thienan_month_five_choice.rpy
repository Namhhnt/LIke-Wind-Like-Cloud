# FILE: game/story/tam/tam_c04_between_work_and_hearts/s116_w20_quang_thienan_month_five_choice.rpy

label tam_c04_w20_s03_quang_thienan_month_five_choice:
    if story_has_flag("tam_c04_tam_quang_confirmed"):
        return
    if not tam_c04_quang_thienan_breakthrough_ready():
        return
    scene black
    with dissolve
    "Quang mang trả Thiên An chiếc thẻ phòng từ chuyến công tác."
    quang "Anh định giữ làm cớ gặp em."
    thienan neutral "Cớ hơi tệ."
    quang "Ừ. Nên anh trả và hỏi thẳng. Cuối tuần em có muốn ăn cùng anh không?"
    menu:
        "Thiên An đồng ý":
            $ tam_c04_commit_quang_thienan()
            $ story_add("thienan_quang_trust", 7)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 7)
            $ story_flag("tam_c04_w20_thienan_accepts_quang_date")
            thienan neutral "Được. Nhưng đừng nói là tiện đường."
        "Thiên An xin thêm thời gian nhưng không gạt đi":
            $ story_add("thienan_quang_trust", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_flag("tam_c04_w20_thienan_does_not_reject")
            thienan neutral "Tuần này chưa được. Tuần sau hỏi lại."
            quang "Anh sẽ hỏi."
    return
