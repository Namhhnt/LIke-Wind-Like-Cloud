# FILE: game/data/phone_threads_tam_c04_w06.rpy
# Week 06 private messages.

init -5 python:

    PHONE_THREADS.update({
        "tam_c04_w06_huyen_empty_chair": {
            "id": "tam_c04_w06_huyen_empty_chair",
            "type": "chat",
            "contact_id": "huyen",
            "title": "Huyền",
            "unlock_conditions": ["flag:tam_c04_w06_started"],
            "sort_order": 810,
            "messages": [
                {"id": "m01", "sender": "huyen", "text": "Anh Quân đi ngoài hai ngày.", "time": "07:01"},
                {"id": "m02", "sender": "player", "text": "Tao cũng nhận email.", "time": "07:02"},
                {"id": "m03", "sender": "huyen", "text": "Tao chỉ thông báo. Không có ý gì khác.", "time": "07:03"},
            ],
            "effects_on_read": {"flags": ["read_tam_c04_w06_huyen_empty_chair"]},
        },
        "tam_c04_w06_hoang_after_house": {
            "id": "tam_c04_w06_hoang_after_house",
            "type": "chat",
            "contact_id": "hoang",
            "title": "Hoàng",
            "unlock_conditions": ["flag:tam_c04_w06_started", "flag:tam_c04_w05_tam_accepts_hoang_house_invitation"],
            "sort_order": 820,
            "messages": [
                {"id": "m01", "sender": "hoang", "text": "Anh đã sửa cái tủ bếp.", "time": "21:05"},
                {"id": "m02", "sender": "player", "text": "Em chưa kịp phàn nàn mà.", "time": "21:07"},
                {"id": "m03", "sender": "hoang", "text": "Anh thấy em nhìn nó hai lần.", "time": "21:08"},
            ],
            "effects_on_read": {"flags": ["read_tam_c04_w06_hoang_after_house"]},
        },
        "tam_c04_w06_quang_family_errand": {
            "id": "tam_c04_w06_quang_family_errand",
            "type": "chat",
            "contact_id": "quang",
            "title": "Quang",
            "unlock_conditions": ["flag:tam_c04_w06_started"],
            "sort_order": 815,
            "messages": [
                {"id": "m01", "sender": "quang", "text": "Ngăn kéo hồ sơ vẫn hay kẹt à?", "time": "19:22"},
                {"id": "m02", "sender": "player", "text": "Anh còn nhớ cả chuyện đó?", "time": "19:24"},
                {"id": "m03", "sender": "quang", "text": "Anh từng sửa rồi.", "time": "19:25"},
            ],
            "effects_on_read": {"flags": ["read_tam_c04_w06_quang_family_errand"]},
        },
    })

    PHONE_REPLY_CHOICES.update({
        "tam_c04_w06_huyen_empty_chair": [
            {
                "id": "tell_huyen_use_standard",
                "text": "Mày biết tiêu chuẩn rồi. Cứ làm như ổng đang ở đó.",
                "once": True,
                "effects": {"story_add": {"career_huyen": 1, "huyen_quan_trust": 1}, "flags": ["tam_c04_w06_phone_huyen_uses_standard"]},
                "response_messages": [{"id": "r01", "sender": "huyen", "text": "Câu đó không làm tao dễ chịu hơn.", "time": "07:05"}],
            },
            {
                "id": "tease_huyen_missing_quan",
                "text": "Mới đọc email đã nhớ người ta rồi à?",
                "once": True,
                "effects": {"story_add": {"huyen_quan_interest": 1}, "flags": ["tam_c04_w06_phone_teases_huyen_missing_quan"]},
                "response_messages": [{"id": "r01", "sender": "huyen", "text": "Tao nhớ người chịu trách nhiệm review. Đừng bịa.", "time": "07:05"}],
            },
        ],
        "tam_c04_w06_hoang_after_house": [
            {
                "id": "say_hoang_notices_too_much",
                "text": "Anh để ý hơi nhiều rồi đấy.",
                "once": True,
                "effects": {"story_add": {"tam_hoang_interest": 1, "hoang_tam_trust": 1}, "flags": ["tam_c04_w06_phone_says_hoang_notices"]},
                "response_messages": [{"id": "r01", "sender": "hoang", "text": "Anh sẽ cố để ý kín đáo hơn.", "time": "21:10"}],
            },
            {
                "id": "ask_keep_chair",
                "text": "Đừng đổi vị trí chiếc ghế nhé.",
                "once": True,
                "effects": {"story_add": {"tam_hoang_interest": 1, "hoang_self_acceptance": 1}, "flags": ["tam_c04_w06_phone_keeps_hoang_chair"]},
                "response_messages": [{"id": "r01", "sender": "hoang", "text": "Anh không định đổi.", "time": "21:10"}],
            },
        ],
        "tam_c04_w06_quang_family_errand": [
            {
                "id": "ask_quang_when_repaired",
                "text": "Anh sửa lúc nào? Em không nhớ.",
                "once": True,
                "effects": {"story_add": {"tam_quang_interest": 1}, "tam_c04_extended_story_add": {"quang_tam_warmth": 1, "quang_tam_awareness": 1}, "flags": ["tam_c04_w06_phone_asks_quang_memory"]},
                "response_messages": [{"id": "r01", "sender": "quang", "text": "Lúc em còn học đại học. Em đang bận thi.", "time": "19:28"}],
            },
            {
                "id": "tell_quang_take_to_an",
                "text": "Vậy tối nay anh tự mang hồ sơ cho chị An nhé.",
                "once": True,
                "effects": {"story_add": {"thienan_quang_trust": 1, "quang_persistence": 1}, "tam_c04_extended_story_add": {"quang_thienan_resolve": 1}, "flags": ["tam_c04_w06_phone_quang_direct_to_an"]},
                "response_messages": [{"id": "r01", "sender": "quang", "text": "Anh biết rồi.", "time": "19:28"}],
            },
        ],
    })
