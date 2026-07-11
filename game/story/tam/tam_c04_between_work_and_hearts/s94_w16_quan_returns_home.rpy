# FILE: game/story/tam/tam_c04_between_work_and_hearts/s94_w16_quan_returns_home.rpy

label tam_c04_w16_s04_quan_returns_home:
    scene black
    with dissolve
    "Quân về nhà sau mười giờ. Ánh Nhi đã ngủ. Huyền ngồi dưới sàn phòng khách, dựa lưng vào sofa."
    "Trên bàn là bình nước đã thay nắp mới."
    quan neutral "Cô chưa về?"
    huyen tired "Em ngủ quên năm phút. Có thể là bốn mươi."
    quan neutral "Tôi đưa cô về."
    huyen neutral "Anh vừa xuống máy bay à?"
    quan neutral "Ừ."
    huyen neutral "Vậy anh ngồi xuống trước đi."
    menu:
        "Huyền rót nước cho Quân":
            $ story_add("huyen_quan_trust", 7)
            $ story_add("huyen_quan_interest", 5)
            $ story_flag("tam_c04_w16_huyen_pours_quan_water")
            "Quân nhận cốc. Lần đầu tiên anh không nói mình không cần."
        "Tâm nhắn Huyền cứ về trước":
            $ story_add("career_huyen", 3)
            $ story_add("tam_observation", 3)
            $ story_flag("tam_c04_w16_tam_gives_huyen_exit")
            "Huyền đọc tin nhưng không đứng dậy ngay."
        "Ánh Nhi thức dậy gọi cả hai":
            $ story_add("huyen_quan_trust", 5)
            $ story_flag("tam_c04_w16_anhni_calls_huyen_from_room")
            anhni "Cô Huyền chưa về à?"
            "Quân nhìn về phía Huyền. Cô đã đứng lên trước anh."
    return
