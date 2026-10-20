label tam_c04_w11_s02_tam_owns_the_mistake:
    scene bg_meeting_room_day
    with dissolve
    scene cg_tam_c04_team_review
    with dissolve
    "Sáng thứ Ba, một quyết định của Tâm làm bản demo thiếu một trường hợp biên."
    scene bg_meeting_room_day
    with dissolve
    "Không nghiêm trọng. Nhưng đủ để khách hàng hỏi ngay trong cuộc họp."
    quan neutral "Ai chốt phạm vi này?"
    menu:
        "Nhận trách nhiệm và đưa phương án sửa ngay":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_add("tam_observation", 3)
            $ story_flag("tam_c04_w11_tam_owns_scope_mistake")
            tam neutral "Em. Em bỏ trường hợp này khỏi phạm vi. Em sẽ bổ sung mock trước ba giờ và cập nhật decision log."
            quan neutral "Làm đi."
        "Nhờ Huyền giữ cuộc họp để Tâm sửa phần thiếu":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 5)
            $ story_flag("tam_c04_w11_tam_huyen_recover_mistake")
            tam neutral "Huyền, kéo phần Q&A thêm năm phút. Tao sửa mock."
            huyen neutral "Nợ tao một bữa."
        "Để Huyền giải thích tác động với khách hàng":
            $ story_add("career_huyen", 10)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w11_huyen_explains_tam_mistake")
            tam neutral "Huyền, nói giúp tao phần tác động. Quyết định là của tao."
            huyen neutral "Được. Nhưng mày tự nói câu cuối."
    "Cuộc họp tiếp tục."
    "Quân không cứu Tâm khỏi câu hỏi tiếp theo."
    "Anh cũng không lấy lại quyền quyết định đã giao."
    return
