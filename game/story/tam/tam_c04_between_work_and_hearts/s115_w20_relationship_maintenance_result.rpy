# FILE: game/story/tam/tam_c04_between_work_and_hearts/s115_w20_relationship_maintenance_result.rpy

label tam_c04_w20_s02_relationship_maintenance_result:
    if not story_has_flag("tam_c04_tam_hoang_dating"):
        return
    $ _result = relationship_resolve_contact_period("tam_hoang", "tam_c04_w19")
    scene black
    with dissolve
    if _result == "maintained":
        "Hoàng đặt điện thoại xuống khi Tâm đến."
        hoang neutral "Tuần trước không dễ. Nhưng anh không phải tự đoán."
        tam neutral "Em đang học."
        hoang neutral "Anh cũng vậy."
    else:
        "Hoàng vẫn đến, nhưng không đặt sẵn cốc nước phía Tâm."
        tam neutral "Anh giận à?"
        hoang neutral "Có. Không phải vì em bận. Vì em để anh biết sau cùng."
        menu:
            "Nhận lỗi và đề nghị một quy tắc liên lạc":
                $ story_add("hoang_tam_trust", 3)
                $ story_add("tam_self_clarity", 5)
                $ story_flag("tam_c04_w20_hoang_repair_rule")
                tam neutral "Từ giờ nếu trễ quá một tiếng em sẽ báo. Không cần đợi."
            "Nói Hoàng đang đòi hỏi quá nhiều":
                $ story_sub("hoang_tam_trust", 5)
                $ story_add("tam_insecurity", 3)
                $ story_flag("tam_c04_w20_hoang_conflict_unrepaired")
                hoang neutral "Có thể. Nhưng đây là điều anh cần. Em cũng có quyền nói mình không muốn."
    return
