# Week 09 — A message lands in the wrong conversation and exposes Quang's split attention.
label tam_c04_w09_s04_quang_wrong_recipient:
    scene bg_asset_0007
    with fade
    scene cg_tam_c04_phone_night
    with dissolve
    "Chiều thứ Năm, Quang gửi cho Tâm một tấm ảnh lịch công tác của Thiên An."
    scene bg_asset_0007
    with dissolve
    "Tin nhắn dưới ảnh chỉ có bốn chữ: anh đã đổi rồi."
    "Ba giây sau, anh thu hồi cả hai."
    tam neutral "Gửi nhầm à?"
    quang "Ừ."
    tam neutral "Nhầm người hay nhầm câu?"

    menu:
        "Bảo Quang gửi lại cho Thiên An và tự giải thích":
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_add_direction("quang", "quang_thienan_open")
            $ story_flag("tam_c04_w09_quang_resends_to_thienan")
            tam neutral "Anh gửi lại cho chị ấy đi. Với cả nói rõ anh đổi cái gì."
            quang "Anh biết."
            tam neutral "Biết mà vẫn gửi nhầm."

        "Hỏi vì sao phản xạ đầu tiên của Quang vẫn là tìm Tâm":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 5)
            $ tam_c04_add_extended_score("quang_tam_awareness", 5)
            $ story_add("tam_self_clarity", 3)
            $ story_add_direction("quang", "quang_tam_open")
            $ story_flag("tam_c04_w09_tam_questions_quang_first_reflex")
            tam neutral "Sao người anh tìm đầu tiên vẫn là em?"
            "Quang không trả lời ngay."
            quang "Vì với em, anh không phải nghĩ trước từng câu."
            tam neutral "Đó không hẳn là câu trả lời an toàn đâu."

        "Giả vờ không thấy phần tin đã bị thu hồi":
            $ tam_c04_add_extended_score("quang_tam_warmth", 3)
            $ story_add("thienan_quang_trust", 3)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 3)
            $ story_add("tam_observation", 3)
            $ story_flag("tam_c04_w09_quang_wrong_recipient_unresolved")
            tam neutral "Anh đổi lịch gì vậy?"
            quang "Không có gì."
            "Câu trả lời đến quá nhanh."

    "Màn hình tắt."
    "Tin nhắn đã biến mất, nhưng người nhận đầu tiên thì không."
    return
