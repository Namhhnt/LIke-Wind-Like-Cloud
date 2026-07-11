# FILE: game/story/tam/tam_c04_between_work_and_hearts/s136_w24_tam_route_finale.rpy

label tam_c04_w24_s03_tam_route_finale:
    scene black
    with dissolve
    if story_has_flag("tam_c04_tam_hoang_dating"):
        $ _missed_w21 = relationship_resolve_contact_period("tam_hoang", "tam_c04_w21") == "missed"
        $ _missed_w22 = relationship_resolve_contact_period("tam_hoang", "tam_c04_w22") == "missed"
        hoang neutral "Anh không cần mình gặp mỗi ngày. Nhưng anh không muốn tình yêu chỉ tồn tại vào tuần em rảnh."
        if _missed_w21 and _missed_w22:
            tam neutral "Em đã nghĩ có tên rồi thì anh sẽ hiểu."
            hoang neutral "Anh hiểu em bận. Anh không đồng ý với việc bị bỏ ngoài cuộc."
            menu:
                "Cam kết sửa cách liên lạc":
                    $ story_add("hoang_tam_trust", 5)
                    $ story_add("tam_self_clarity", 7)
                    $ story_flag("tam_c04_final_hoang_repair_commitment")
                    tam neutral "Em muốn tiếp tục. Và em sẽ không bắt anh đoán nữa."
                "Thừa nhận Tâm chưa sẵn sàng cho nhịp hẹn hò":
                    $ story_sub("hoang_tam_trust", 7)
                    $ story_add("tam_self_clarity", 7)
                    $ story_flag("tam_c04_final_hoang_dating_fragile")
                    tam neutral "Em đã chọn anh, nhưng có lẽ em chưa biết cách ở trong một mối quan hệ."
        else:
            tam neutral "Em biết. Nên em mới báo anh cả những ngày không có gì để kể."
            hoang neutral "Anh thích những ngày đó."
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_flag("tam_c04_final_hoang_dating_stable")
    elif story_has_flag("tam_c04_tam_quang_confirmed"):
        "Quang đứng ở cửa nhưng không bước vào như mọi lần."
        quang "Anh tới đón em. Nếu em vẫn muốn đi cùng anh."
        tam neutral "Anh không cần hỏi lại mỗi lần."
        quang "Anh cần. Vì trước đây anh chưa từng hỏi."
        tam neutral "Vậy hôm nay em muốn."
        $ story_add("tam_quang_interest", 7)
        $ tam_c04_add_extended_score("quang_tam_awareness", 7)
        $ tam_c04_add_extended_score("quang_tam_warmth", 5)
        $ relationship_set_phase("tam_quang", "mutual_direction")
        $ story_flag("tam_c04_final_quang_tam_mutual_direction")
    else:
        "Tâm ký tên vào bản nhận workstream mới."
        "Không có ai bị từ chối để cô chứng minh mình mạnh. Chỉ có một lựa chọn được giữ đúng nghĩa của nó."
        $ story_add("career_tam", 15)
        $ story_add("tam_self_clarity", 10)
        $ story_flag("tam_c04_final_independent_direction")
    return
