# FILE: game/story/tam/tam_c04_between_work_and_hearts/s105_w18_after_decision.rpy

label tam_c04_w18_s03_after_decision:
    scene black
    with dissolve
    if story_has_flag("tam_c04_tam_hoang_dating"):
        "Tâm gặp Hoàng ở nơi anh đã hẹn từ tuần trước."
        tam neutral "Mình thử nghiêm túc nhé."
        hoang surprised "Em đang hỏi anh à?"
        tam neutral "Không. Em đang nói câu trả lời."
        hoang neutral "Vậy anh có một điều kiện. Bận thì báo. Giận thì nói. Đừng biến mất rồi gọi đó là cho nhau không gian."
        tam neutral "Anh cũng vậy."
        "Hoàng đưa tay qua mặt bàn. Tâm đặt tay mình lên đó, chỉ một lúc."
    elif story_has_flag("tam_c04_tam_quang_confirmed"):
        "Tâm chặn Quang lại ở hành lang nhà."
        tam neutral "Anh nói anh nghĩ tới em nhiều hơn anh nên nghĩ. Em không muốn câu đó treo ở đó nữa."
        quang "Anh cũng không."
        tam neutral "Vậy nói đi."
        quang "Anh thích em. Không giống trước đây. Không phải vì em là em của chị An."
        tam neutral "Em cũng vậy."
        "Cả hai đứng cách nhau chưa tới một cánh tay. Không ai giả vờ đó chỉ là thói quen nữa."
    else:
        "Tâm gửi hai tin nhắn ngắn, không để lại một cánh cửa hé chỉ vì sợ làm ai buồn."
        tam neutral "Em chưa muốn bước vào một mối quan hệ. Không phải vì anh chưa đủ tốt."
        "Cô đặt điện thoại xuống và mở lại bản kế hoạch công việc. Lần này sự yên lặng không phải trốn tránh."
    return
