# FILE: game/data/phone_threads_tam_c04_w05.rpy
# Week 05 private messages.

init -5 python:

    PHONE_THREADS.update({
        "tam_c04_w05_huyen_own_outline": {
            "id": "tam_c04_w05_huyen_own_outline",
            "type": "chat",
            "contact_id": "huyen",
            "title": "Huyền",
            "unlock_conditions": ["flag:tam_c04_w05_started"],
            "sort_order": 710,
            "messages": [
                {"id": "m01", "sender": "huyen", "text": "Tao đã tự làm outline.", "time": "06:51"},
                {"id": "m02", "sender": "player", "text": "Chúc mừng. Mày muốn huy chương không?", "time": "06:53"},
                {"id": "m03", "sender": "huyen", "text": "Tao muốn biết anh Quân sẽ bắt lỗi ở dòng nào.", "time": "06:54"},
            ],
            "effects_on_read": {"flags": ["read_tam_c04_w05_huyen_own_outline"]},
        },
        "tam_c04_w05_hoang_house_address": {
            "id": "tam_c04_w05_hoang_house_address",
            "type": "chat",
            "contact_id": "hoang",
            "title": "Hoàng",
            "unlock_conditions": ["flag:tam_c04_w05_started", "score_gte:tam_hoang_interest:55"],
            "sort_order": 720,
            "messages": [
                {"id": "m01", "sender": "hoang", "text": "Anh gửi địa chỉ nhà.", "time": "07:03"},
                {"id": "m02", "sender": "player", "text": "Anh đang mời em à?", "time": "07:05"},
                {"id": "m03", "sender": "hoang", "text": "Ừ. Không kèm việc vặt.", "time": "07:06"},
            ],
            "effects_on_read": {"flags": ["read_tam_c04_w05_hoang_house_address"]},
        },
        "tam_c04_w05_quang_two_cups": {
            "id": "tam_c04_w05_quang_two_cups",
            "type": "chat",
            "contact_id": "quang",
            "title": "Quang",
            "unlock_conditions": ["flag:tam_c04_w05_started"],
            "sort_order": 715,
            "messages": [
                {"id": "m01", "sender": "quang", "text": "Tối nay em có ở nhà không?", "time": "18:12"},
                {"id": "m02", "sender": "player", "text": "Có. Anh đến gặp em hay gặp chị An?", "time": "18:14"},
                {"id": "m03", "sender": "quang", "text": "Anh mang hồ sơ.", "time": "18:16"},
            ],
            "effects_on_read": {"flags": ["read_tam_c04_w05_quang_two_cups"]},
        },
    })

    PHONE_REPLY_CHOICES.update({
        "tam_c04_w05_huyen_own_outline": [
            {
                "id": "tell_huyen_she_knows",
                "text": "Mày biết rồi còn gì. Vấn đề trước, giải pháp sau.",
                "once": True,
                "effects": {"story_add": {"career_huyen": 1, "huyen_quan_trust": 1}, "flags": ["tam_c04_w05_phone_huyen_knows_standard"]},
                "response_messages": [{"id": "r01", "sender": "huyen", "text": "Tao ghét việc mày nói đúng bằng giọng của ổng.", "time": "06:57"}],
            },
            {
                "id": "tease_huyen_waiting_for_quan",
                "text": "Mày muốn bắt đúng lỗi hay muốn ổng thấy mày bắt đúng?",
                "once": True,
                "effects": {"story_add": {"huyen_quan_trust": 1, "huyen_quan_interest": 1}, "flags": ["tam_c04_w05_phone_teases_huyen_attention"]},
                "response_messages": [{"id": "r01", "sender": "huyen", "text": "Tao sẽ không trả lời câu có ý đồ xấu.", "time": "06:57"}],
            },
        ],
        "tam_c04_w05_hoang_house_address": [
            {
                "id": "accept_house_invitation",
                "text": "Được. Em sẽ đến.",
                "once": True,
                "effects": {"story_add": {"tam_hoang_interest": 1, "hoang_tam_trust": 1}, "flags": ["tam_c04_w05_phone_accepts_house"]},
                "response_messages": [{"id": "r01", "sender": "hoang", "text": "Anh sẽ cố không sửa lại phòng khách thêm lần nữa.", "time": "07:08"}],
            },
            {
                "id": "ask_if_nervous",
                "text": "Anh căng thẳng à?",
                "once": True,
                "effects": {"story_add": {"hoang_self_acceptance": 1, "hoang_tam_trust": 1}, "flags": ["tam_c04_w05_phone_asks_hoang_nervous"]},
                "response_messages": [{"id": "r01", "sender": "hoang", "text": "Không. Anh chỉ đã đổi vị trí hai cái ghế ba lần.", "time": "07:08"}],
            },
        ],
        "tam_c04_w05_quang_two_cups": [
            {
                "id": "ask_quang_who",
                "text": "Hồ sơ không trả lời câu hỏi của em.",
                "once": True,
                "effects": {"story_add": {"tam_quang_interest": 1}, "tam_c04_extended_story_add": {"quang_tam_awareness": 2, "quang_tam_warmth": 1}, "flags": ["tam_c04_w05_phone_asks_quang_who"]},
                "response_messages": [{"id": "r01", "sender": "quang", "text": "Anh biết. Tối nói.", "time": "18:18"}],
            },
            {
                "id": "tell_quang_ask_an",
                "text": "Nếu là hồ sơ của chị An thì anh tự hỏi chị ấy nhé.",
                "once": True,
                "effects": {"story_add": {"thienan_quang_trust": 1, "quang_persistence": 1}, "tam_c04_extended_story_add": {"quang_thienan_resolve": 1}, "flags": ["tam_c04_w05_phone_redirects_quang"]},
                "response_messages": [{"id": "r01", "sender": "quang", "text": "Ừ. Anh sẽ hỏi.", "time": "18:18"}],
            },
        ],
    })
