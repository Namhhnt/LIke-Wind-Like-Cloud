# FILE: game/data/phone_threads_tam_c04_w08.rpy
# Week 08 private messages and Month 02 review signals.

init -5 python:

    PHONE_THREADS.update({
        "tam_c04_w08_huyen_review_questions": {
            "id": "tam_c04_w08_huyen_review_questions",
            "type": "chat",
            "contact_id": "huyen",
            "title": "Huyền",
            "unlock_conditions": ["flag:tam_c04_w08_started"],
            "sort_order": 1010,
            "messages": [
                {"id": "m01", "sender": "huyen", "text": "Tao chuẩn bị ba câu anh Quân có thể hỏi.", "time": "06:41"},
                {"id": "m02", "sender": "player", "text": "Nếu ổng hỏi câu thứ tư?", "time": "06:43"},
                {"id": "m03", "sender": "huyen", "text": "Thì ổng gian lận.", "time": "06:44"},
            ],
            "effects_on_read": {"flags": ["read_tam_c04_w08_huyen_review_questions"]},
        },
        "tam_c04_w08_hoang_asks_when": {
            "id": "tam_c04_w08_hoang_asks_when",
            "type": "chat",
            "contact_id": "hoang",
            "title": "Hoàng",
            "unlock_conditions": ["flag:tam_c04_w08_started", "score_gte:tam_hoang_interest:70"],
            "sort_order": 1020,
            "messages": [
                {"id": "m01", "sender": "hoang", "text": "Thứ Sáu em tan làm lúc mấy giờ?", "time": "07:02"},
                {"id": "m02", "sender": "player", "text": "Anh không hỏi em có rảnh à?", "time": "07:04"},
                {"id": "m03", "sender": "hoang", "text": "Anh đang hỏi để biết nên chờ lúc nào.", "time": "07:05"},
            ],
            "effects_on_read": {"flags": ["read_tam_c04_w08_hoang_asks_when"]},
        },
        "tam_c04_w08_quang_after_review": {
            "id": "tam_c04_w08_quang_after_review",
            "type": "chat",
            "contact_id": "quang",
            "title": "Quang",
            "unlock_conditions": ["flag:tam_c04_w08_started", "score_gte:quang_tam_awareness:15"],
            "sort_order": 1015,
            "messages": [
                {"id": "m01", "sender": "quang", "text": "Sau buổi review em có về nhà không?", "time": "08:11"},
                {"id": "m02", "sender": "player", "text": "Anh cần gặp chị An à?", "time": "08:13"},
                {"id": "m03", "sender": "quang", "text": "Anh đang hỏi em.", "time": "08:15"},
            ],
            "effects_on_read": {"flags": ["read_tam_c04_w08_quang_after_review"]},
        },
    })

    PHONE_REPLY_CHOICES.update({
        "tam_c04_w08_huyen_review_questions": [
            {
                "id": "tell_huyen_can_answer",
                "text": "Mày trả lời được. Không cần đoán hết.",
                "once": True,
                "effects": {"story_add": {"career_huyen": 1, "huyen_quan_trust": 1}, "flags": ["tam_c04_w08_phone_reassures_huyen"]},
                "response_messages": [{"id": "r01", "sender": "huyen", "text": "Tao biết. Chuẩn bị vẫn không thừa.", "time": "06:46"}],
            },
            {
                "id": "tease_huyen_knows_quan",
                "text": "Hai tháng đủ để mày học thuộc người review rồi nhỉ.",
                "once": True,
                "effects": {"story_add": {"huyen_quan_interest": 1}, "flags": ["tam_c04_w08_phone_teases_huyen_knows_quan"]},
                "response_messages": [{"id": "r01", "sender": "huyen", "text": "Học thuộc quy trình. Không phải người.", "time": "06:46"}],
            },
        ],
        "tam_c04_w08_hoang_asks_when": [
            {
                "id": "give_hoang_time",
                "text": "Khoảng sáu giờ hai mươi. Em sẽ xuống.",
                "once": True,
                "effects": {"story_add": {"tam_hoang_interest": 1, "hoang_tam_trust": 1}, "flags": ["tam_c04_w08_phone_gives_hoang_time"]},
                "response_messages": [{"id": "r01", "sender": "hoang", "text": "Được. Anh sẽ không hỏi lại.", "time": "07:07"}],
            },
            {
                "id": "ask_hoang_confident",
                "text": "Anh tự tin em sẽ gặp anh vậy à?",
                "once": True,
                "effects": {"story_add": {"hoang_tam_trust": 1, "hoang_self_acceptance": 1}, "flags": ["tam_c04_w08_phone_asks_hoang_confident"]},
                "response_messages": [{"id": "r01", "sender": "hoang", "text": "Anh đang cố tin vào những gì em đã nói.", "time": "07:07"}],
            },
        ],
        "tam_c04_w08_quang_after_review": [
            {
                "id": "ask_quang_why_tam",
                "text": "Vì sao anh cần biết em có về?",
                "once": True,
                "effects": {"story_add": {"tam_quang_interest": 1}, "tam_c04_extended_story_add": {"quang_tam_warmth": 1, "quang_tam_awareness": 2}, "flags": ["tam_c04_w08_phone_asks_quang_why_tam"]},
                "response_messages": [{"id": "r01", "sender": "quang", "text": "Tối nói được không?", "time": "08:18"}],
            },
            {
                "id": "tell_quang_an_schedule",
                "text": "Chị An về muộn. Anh tự nhắn chị ấy nhé.",
                "once": True,
                "effects": {"story_add": {"thienan_quang_trust": 1, "quang_persistence": 1}, "tam_c04_extended_story_add": {"quang_thienan_resolve": 1}, "flags": ["tam_c04_w08_phone_redirects_quang_an"]},
                "response_messages": [{"id": "r01", "sender": "quang", "text": "Anh biết lịch chị ấy. Anh hỏi em.", "time": "08:18"}],
            },
        ],
    })
