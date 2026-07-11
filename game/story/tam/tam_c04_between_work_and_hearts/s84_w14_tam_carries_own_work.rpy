# FILE: game/story/tam/tam_c04_between_work_and_hearts/s84_w14_tam_carries_own_work.rpy

label tam_c04_w14_s04_tam_carries_own_work:
    scene bg_meeting_room_day
    with dissolve
    "Quân chuyển cho Tâm một đầu việc không có tên Huyền trong phần người phụ trách."
    quan neutral "Cô tự chốt. Tôi chỉ xem bản cuối."
    menu:
        "Nhận quyền quyết định":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_c04_w14_tam_owns_delivery")
            tam neutral "Được. Em sẽ gửi trước năm giờ."
        "Xin Huyền review chéo, không chia lại ownership":
            $ story_add("career_tam", 7)
            $ story_add("career_huyen", 5)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 5)
            $ story_flag("tam_c04_w14_peer_review_only")
            huyen neutral "Tao chỉ khoanh chỗ không rõ. Không cứu mày."
        "Hỏi rõ giới hạn phê duyệt":
            $ story_add("career_tam", 7)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w14_tam_clarifies_authority")
            quan neutral "Trong phạm vi ngân sách này, cô quyết định."
    return
