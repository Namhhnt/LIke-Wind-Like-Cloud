# FILE: game/data/phone_threads_tam_c04_w02.rpy
# Week 02 private messages and reply choices. Vietnamese text uses full diacritics.

init -5 python:

    PHONE_THREADS.update({
        "tam_c04_w02_huyen_preemptive_fix": {
            "id": "tam_c04_w02_huyen_preemptive_fix",
            "type": "chat",
            "contact_id": "huyen",
            "title": "Huyền",
            "unlock_conditions": [
                "flag:tam_c04_w02_started",
            ],
            "sort_order": 410,
            "messages": [
                {
                    "id": "m01",
                    "sender": "huyen",
                    "text": "Tao đã sửa trước ba chỗ anh Quân có thể sẽ hỏi.",
                    "time": "06:54",
                },
                {
                    "id": "m02",
                    "sender": "player",
                    "text": "Mày đang khoe hay đang cầu cứu?",
                    "time": "06:56",
                },
                {
                    "id": "m03",
                    "sender": "huyen",
                    "text": "Chưa quyết định. Đợi ổng review xong rồi tao báo.",
                    "time": "06:57",
                },
            ],
            "effects_on_read": {
                "flags": ["read_tam_c04_w02_huyen_preemptive_fix"],
                "known_info_add": {
                    "huyen": [
                        "Huyền bắt đầu chủ động kiểm tra công việc theo tiêu chuẩn của Quân trước khi bị anh nhắc.",
                    ],
                },
            },
        },

        "tam_c04_w02_hoang_bought_extra": {
            "id": "tam_c04_w02_hoang_bought_extra",
            "type": "chat",
            "contact_id": "hoang",
            "title": "Hoàng",
            "unlock_conditions": [
                "flag:tam_c04_w02_started",
                "score_gte:tam_hoang_interest:50",
            ],
            "sort_order": 420,
            "messages": [
                {
                    "id": "m01",
                    "sender": "hoang",
                    "text": "Anh mua dư một hộp bánh.",
                    "time": "07:09",
                },
                {
                    "id": "m02",
                    "sender": "player",
                    "text": "Dư thật hay là một kế hoạch có chuẩn bị?",
                    "time": "07:12",
                },
                {
                    "id": "m03",
                    "sender": "hoang",
                    "text": "Anh đang cố giữ quyền không tự buộc tội mình.",
                    "time": "07:13",
                },
            ],
            "effects_on_read": {
                "flags": ["read_tam_c04_w02_hoang_bought_extra"],
            },
        },

        "tam_c04_w02_quang_called_directly": {
            "id": "tam_c04_w02_quang_called_directly",
            "type": "chat",
            "contact_id": "quang",
            "title": "Quang",
            "unlock_conditions": [
                "flag:tam_c04_w02_started",
                "score_gte:thienan_quang_trust:40",
            ],
            "sort_order": 415,
            "messages": [
                {
                    "id": "m01",
                    "sender": "quang",
                    "text": "Anh đã gọi thẳng cho chị An rồi.",
                    "time": "21:18",
                },
                {
                    "id": "m02",
                    "sender": "player",
                    "text": "Và anh vẫn còn sống để báo cáo. Tốt đấy.",
                    "time": "21:20",
                },
                {
                    "id": "m03",
                    "sender": "quang",
                    "text": "Chị ấy cúp máy sau bốn phút.",
                    "time": "21:21",
                },
                {
                    "id": "m04",
                    "sender": "player",
                    "text": "Với chị An thì bốn phút là một cuộc trò chuyện dài rồi.",
                    "time": "21:22",
                },
            ],
            "effects_on_read": {
                "flags": ["read_tam_c04_w02_quang_called_directly"],
            },
        },
    })

    PHONE_REPLY_CHOICES.update({
        "tam_c04_w02_huyen_preemptive_fix": [
            {
                "id": "review_with_huyen",
                "text": "Gửi tao xem trước. Hai đứa kiểm lại cho chắc.",
                "once": True,
                "effects": {
                    "story_add": {
                        "career_tam": 1,
                        "career_huyen": 1,
                    },
                    "flags": ["tam_c04_w02_phone_offered_huyen_review"],
                },
                "response_messages": [
                    {
                        "id": "r01",
                        "sender": "huyen",
                        "text": "Được. Nhưng nếu mày cũng đoán đúng câu ổng hỏi thì tao sẽ thấy hơi đáng sợ.",
                        "time": "07:00",
                    },
                ],
            },
            {
                "id": "let_huyen_test_her_prediction",
                "text": "Cứ để vậy xem mày đoán đúng được bao nhiêu.",
                "once": True,
                "effects": {
                    "story_add": {
                        "huyen_quan_trust": 1,
                        "career_huyen": 1,
                    },
                    "flags": ["tam_c04_w02_phone_let_huyen_test_quan_standard"],
                },
                "response_messages": [
                    {
                        "id": "r01",
                        "sender": "huyen",
                        "text": "Tao ghét việc chuyện này bắt đầu giống một trò chơi.",
                        "time": "07:00",
                    },
                ],
            },
        ],

        "tam_c04_w02_hoang_bought_extra": [
            {
                "id": "accept_hoang_bread",
                "text": "Chiều anh mang qua đi. Em sẽ giả vờ tin là mua dư.",
                "once": True,
                "effects": {
                    "story_add": {
                        "tam_hoang_interest": 1,
                        "hoang_tam_trust": 1,
                    },
                    "flags": ["tam_c04_w02_phone_accepts_hoang_bread"],
                },
                "response_messages": [
                    {
                        "id": "r01",
                        "sender": "hoang",
                        "text": "Cảm ơn em đã hợp tác bảo vệ lời khai.",
                        "time": "07:15",
                    },
                ],
            },
            {
                "id": "tell_hoang_not_to_wait",
                "text": "Em chưa chắc xuống được. Anh đừng đợi nhé.",
                "once": True,
                "effects": {
                    "story_add": {
                        "career_tam": 1,
                        "hoang_self_acceptance": 1,
                    },
                    "flags": ["tam_c04_w02_phone_tells_hoang_not_to_wait"],
                },
                "response_messages": [
                    {
                        "id": "r01",
                        "sender": "hoang",
                        "text": "Ừ. Anh ghé được thì ghé, không thì hộp bánh sẽ được trở về nơi nó sinh ra.",
                        "time": "07:15",
                    },
                ],
            },
        ],

        "tam_c04_w02_quang_called_directly": [
            {
                "id": "encourage_quang_directness",
                "text": "Ít nhất lần này anh hỏi đúng người rồi.",
                "once": True,
                "effects": {
                    "story_add": {
                        "thienan_quang_trust": 1,
                        "quang_persistence": 1,
                    },
                    "tam_c04_extended_story_add": {
                        "quang_thienan_resolve": 1,
                    },
                    "flags": ["tam_c04_w02_phone_encouraged_quang_directness"],
                },
                "response_messages": [
                    {
                        "id": "r01",
                        "sender": "quang",
                        "text": "Anh sẽ cố giữ thói quen mới này.",
                        "time": "21:25",
                    },
                ],
            },
            {
                "id": "tease_quang_four_minutes",
                "text": "Anh nhớ chính xác bốn phút cơ à?",
                "once": True,
                "effects": {
                    "story_add": {
                        "tam_quang_interest": 1,
                    },
                    "tam_c04_extended_story_add": {
                        "quang_tam_awareness": 1,
                    },
                    "flags": ["tam_c04_w02_phone_teased_quang_call_duration"],
                },
                "response_messages": [
                    {
                        "id": "r01",
                        "sender": "quang",
                        "text": "Ba phút năm mươi hai giây. Anh đã làm tròn để đỡ đáng ngờ.",
                        "time": "21:25",
                    },
                ],
            },
        ],
    })
