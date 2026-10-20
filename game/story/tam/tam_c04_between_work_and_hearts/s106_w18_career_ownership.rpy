# FILE: game/story/tam/tam_c04_between_work_and_hearts/s106_w18_career_ownership.rpy

label tam_c04_w18_s04_career_ownership:
    scene bg_meeting_room_day
    with dissolve
    scene cg_tam_c04_tam_work_day
    with dissolve
    "Quân giao cho Tâm và Huyền hai quyết định tách biệt. Không ai được ký thay người kia."
    scene bg_company_open_office_day
    with dissolve
    menu:
        "Tâm nhận phần có rủi ro cao hơn":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_c04_w18_tam_takes_higher_risk")
        "Huyền nhận phần đối ngoại":
            $ story_add("career_huyen", 10)
            $ story_add("huyen_quan_trust", 5)
            $ story_flag("tam_c04_w18_huyen_owns_external")
        "Hai người review chéo nhưng không cứu nhau":
            $ story_add("career_tam", 7)
            $ story_add("career_huyen", 7)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 5)
            $ story_flag("tam_c04_w18_peer_ownership")
    return
