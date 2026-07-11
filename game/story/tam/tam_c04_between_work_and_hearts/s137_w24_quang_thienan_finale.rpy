# FILE: game/story/tam/tam_c04_between_work_and_hearts/s137_w24_quang_thienan_finale.rpy

label tam_c04_w24_s04_quang_thienan_finale:
    if story_has_flag("tam_c04_tam_quang_confirmed"):
        return
    if not story_has_flag("tam_c04_quang_thienan_committed") and not tam_c04_quang_thienan_breakthrough_ready():
        return
    scene black
    with dissolve
    "Thiên An làm việc ở bàn ăn. Quang đặt một cốc nước xuống rồi ngồi ở ghế đối diện."
    thienan neutral "Anh không hỏi tôi có cần không nữa à?"
    quang "Em vẫn có thể bảo anh về."
    "Thiên An nhìn cánh cửa đang mở, rồi kéo tập hồ sơ sang một bên."
    thienan neutral "Muộn rồi. Ở lại ăn đi."
    $ tam_c04_commit_quang_thienan()
    $ relationship_set_phase("quang_thienan", "accepted_closeness")
    $ story_add("thienan_quang_trust", 7)
    $ tam_c04_add_extended_score("quang_thienan_resolve", 7)
    $ story_flag("tam_c04_final_quang_thienan_accepted_closeness")
    return
