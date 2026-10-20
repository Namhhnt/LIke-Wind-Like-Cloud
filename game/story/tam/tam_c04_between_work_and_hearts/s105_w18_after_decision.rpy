# FILE: game/story/tam/tam_c04_between_work_and_hearts/s105_w18_after_decision.rpy

label tam_c04_w18_s03_after_decision:
    scene bg_tam_family_hallway_night
    with dissolve
    if story_has_flag("tam_c04_tam_hoang_dating"):
        scene bg_luxury_restaurant_evening
        with dissolve
        "Tâm gặp Hoàng ở nơi anh đã hẹn từ tuần trước."
        tam neutral "Mình thử nghiêm túc nhé."
        hoang surprised "Em đang hỏi anh à?"
        tam neutral "Không. Em đang nói câu trả lời."
        hoang neutral "Vậy anh có một điều kiện. Bận thì báo. Giận thì nói. Đừng biến mất rồi gọi đó là cho nhau không gian."
        tam neutral "Anh cũng vậy."
        scene cg_tam_c04_hoang_hands
        with dissolve
        "Hoàng đưa tay qua mặt bàn. Tâm đặt tay mình lên đó, chỉ một lúc."
        scene bg_luxury_restaurant_evening
        with dissolve
    elif story_has_flag("tam_c04_tam_quang_confirmed"):
        "Tâm chặn Quang lại ở hành lang nhà."
        tam neutral "Anh nói anh nghĩ tới em nhiều hơn anh nên nghĩ. Em không muốn câu đó treo ở đó nữa."
        quang "Anh cũng không."
        tam neutral "Vậy nói đi."
        quang "Anh thích em. Không giống trước đây. Không phải vì em là em của chị An."
        tam neutral "Em cũng vậy."
        scene cg_tam_c04_quang_confession
        with dissolve
        "Cả hai đứng cách nhau chưa tới một cánh tay. Không ai giả vờ đó chỉ là thói quen nữa."
        scene bg_tam_family_hallway_night
        with dissolve
    else:
        scene bg_tam_room_morning
        with dissolve
        "Tâm gửi hai tin nhắn ngắn, không để lại một cánh cửa hé chỉ vì sợ làm ai buồn."
        tam neutral "Em chưa muốn bước vào một mối quan hệ. Không phải vì anh chưa đủ tốt."
        scene cg_tam_c04_independent_plan
        with dissolve
        "Cô đặt điện thoại xuống và mở lại bản kế hoạch công việc. Lần này sự yên lặng không phải trốn tránh."
        scene bg_company_open_office_day
        with dissolve
    return
