label tam_c04_w10_s04_quang_respects_the_closed_door:
    scene bg_tam_family_hallway_night
    with fade
    "Tối thứ Năm, cửa phòng Thiên An đóng."
    scene cg_tam_c04_quang_door
    with dissolve
    "Quang đứng ngoài hành lang với một túi tài liệu."
    scene bg_tam_family_hallway_night
    with dissolve
    thienan neutral "Em cần làm một mình tối nay."
    "Quang giữ quai túi, rồi gật đầu."
    menu:
        "Bảo Quang để tài liệu lại và về":
            $ story_add("thienan_quang_trust", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_add("quang_persistence", 3)
            $ story_flag("tam_c04_w10_quang_respects_thienan_space")
            tam neutral "Chị ấy đã nói rồi. Anh để lại rồi về đi."
            quang "Ừ."
            "Anh không hỏi Tâm có chắc không."
        "Đi xuống cùng Quang một đoạn":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 5)
            $ tam_c04_add_extended_score("quang_tam_awareness", 3)
            $ story_flag("tam_c04_w10_tam_walks_quang_down")
            tam neutral "Em tiễn anh xuống."
            quang "Không cần đâu."
            tam neutral "Em biết."
        "Không chen vào quyết định của họ":
            $ story_add("thienan_quang_trust", 3)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 3)
            $ tam_c04_add_extended_score("quang_tam_warmth", 3)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w10_tam_leaves_closed_door_choice")
            "Tâm quay vào bếp."
            "Một lát sau, tiếng bước chân Quang đi xuống cầu thang."
    "Cánh cửa vẫn đóng."
    "Lần đầu tiên, việc Quang rời đi không có nghĩa là anh bỏ cuộc."
    return
