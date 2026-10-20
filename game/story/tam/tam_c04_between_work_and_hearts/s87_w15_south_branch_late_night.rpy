# FILE: game/story/tam/tam_c04_between_work_and_hearts/s87_w15_south_branch_late_night.rpy

label tam_c04_w15_s02_south_branch_late_night:
    scene bg_meeting_room_night
    with dissolve
    "Ở chi nhánh miền Nam, phòng họp chỉ còn Thiên An và Quang."
    scene cg_tam_c04_south_late_night
    with dissolve
    "Thiên An tháo kính, day nhẹ giữa trán. Quang đặt cốc nước ấm cạnh tay cô."
    scene bg_meeting_room_night
    with dissolve
    thienan tired "Anh không cần ngồi lại."
    quang "Anh biết."
    thienan neutral "Vậy sao chưa về?"
    menu:
        "Quang nói anh muốn ở lại":
            $ story_add("thienan_quang_trust", 7)
            $ story_add("quang_persistence", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 7)
            $ story_flag("tam_c04_w15_quang_stays_by_choice")
            quang "Vì anh muốn ở đây. Không phải vì em cần người trực."
            "Thiên An không bảo anh đi nữa."
        "Quang chỉ kéo phần tài liệu về phía mình":
            $ story_add("thienan_quang_trust", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_flag("tam_c04_w15_quang_shares_work_silently")
            "Hai người làm tiếp. Chiếc cốc nước nguội chậm hơn bình thường."
        "Quang nhắn Tâm trước khi trả lời":
            $ story_add("tam_quang_interest", 3)
            $ tam_c04_add_extended_score("quang_tam_awareness", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 3)
            $ story_flag("tam_c04_w15_quang_seeks_tam_first")
            "Màn hình hiện một dòng chưa gửi: 'Anh nên ở lại không?'"
            "Quang xóa nó. Nhưng đã quá muộn để giả vờ anh không nghĩ đến Tâm."
    return
