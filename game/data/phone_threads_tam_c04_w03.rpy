# FILE: game/data/phone_threads_tam_c04_w03.rpy
# Week 03 private messages and reply choices. Vietnamese text uses full diacritics.

init -5 python:

    PHONE_THREADS.update({
        "tam_c04_w03_huyen_fourth_question": {
            "id": "tam_c04_w03_huyen_fourth_question",
            "type": "chat",
            "contact_id": "huyen",
            "title": "Huyền",
            "unlock_conditions": ["flag:tam_c04_w03_started"],
            "sort_order": 510,
            "messages": [
                {"id": "m01", "sender": "huyen", "text": "Tao đoán được ba câu anh Quân sẽ hỏi trong cuộc họp mai.", "time": "06:48"},
                {"id": "m02", "sender": "player", "text": "Còn câu thứ tư?", "time": "06:50"},
                {"id": "m03", "sender": "huyen", "text": "Câu thứ tư luôn là lý do khiến tao muốn nghỉ việc.", "time": "06:51"},
            ],
            "effects_on_read": {
                "flags": ["read_tam_c04_w03_huyen_fourth_question"],
                "known_info_add": {
                    "huyen": ["Huyền đã bắt đầu chuẩn bị theo cách Quân phản biện, dù vẫn gọi đó là một mối đe dọa nghề nghiệp."],
                },
            },
        },
        "tam_c04_w03_hoang_specific_plan": {
            "id": "tam_c04_w03_hoang_specific_plan",
            "type": "chat",
            "contact_id": "hoang",
            "title": "Hoàng",
            "unlock_conditions": ["flag:tam_c04_w03_started", "score_gte:tam_hoang_interest:55"],
            "sort_order": 520,
            "messages": [
                {"id": "m01", "sender": "hoang", "text": "Tối thứ Tư, sáu giờ. Quán gần công ty em lần trước.", "time": "07:06"},
                {"id": "m02", "sender": "player", "text": "Lần này anh đưa lịch cụ thể luôn à?", "time": "07:09"},
                {"id": "m03", "sender": "hoang", "text": "Anh đang thử bớt để mọi thứ ở dạng có thể rút lại.", "time": "07:10"},
            ],
            "effects_on_read": {"flags": ["read_tam_c04_w03_hoang_specific_plan"]},
        },
        "tam_c04_w03_quang_returns_umbrella": {
            "id": "tam_c04_w03_quang_returns_umbrella",
            "type": "chat",
            "contact_id": "quang",
            "title": "Quang",
            "unlock_conditions": ["flag:tam_c04_w03_started", "score_gte:tam_quang_interest:8"],
            "sort_order": 515,
            "messages": [
                {"id": "m01", "sender": "quang", "text": "Chiếc ô của em vẫn ở xe anh.", "time": "21:14"},
                {"id": "m02", "sender": "player", "text": "Em quên từ bao giờ vậy?", "time": "21:17"},
                {"id": "m03", "sender": "quang", "text": "Từ hôm em bảo mình không quên gì cả.", "time": "21:18"},
            ],
            "effects_on_read": {"flags": ["read_tam_c04_w03_quang_returns_umbrella"]},
        },
    })

    PHONE_REPLY_CHOICES.update({
        "tam_c04_w03_huyen_fourth_question": [
            {
                "id": "prepare_fourth_with_huyen",
                "text": "Tối gửi tao xem. Hai đứa chuẩn bị luôn câu thứ tư.",
                "once": True,
                "effects": {"story_add": {"career_tam": 1, "career_huyen": 1}, "flags": ["tam_c04_w03_phone_prepares_with_huyen"]},
                "response_messages": [{"id": "r01", "sender": "huyen", "text": "Được. Nhưng mày chịu trách nhiệm tinh thần nếu câu thứ năm xuất hiện.", "time": "06:54"}],
            },
            {
                "id": "let_huyen_face_fourth",
                "text": "Câu thứ tư để mày tự xử. Tao tin mày sống được.",
                "once": True,
                "effects": {"story_add": {"huyen_quan_trust": 1, "career_huyen": 1}, "flags": ["tam_c04_w03_phone_lets_huyen_face_quan"]},
                "response_messages": [{"id": "r01", "sender": "huyen", "text": "Niềm tin của mày đến đúng lúc rất đáng ngờ.", "time": "06:54"}],
            },
        ],
        "tam_c04_w03_hoang_specific_plan": [
            {
                "id": "accept_specific_plan",
                "text": "Được. Nếu họp kéo dài em sẽ báo, không biến mất.",
                "once": True,
                "effects": {"story_add": {"tam_hoang_interest": 1, "hoang_tam_trust": 1}, "flags": ["tam_c04_w03_phone_accepts_hoang_specific_plan"]},
                "response_messages": [{"id": "r01", "sender": "hoang", "text": "Thế là đủ. Phần còn lại để lịch họp chịu trách nhiệm.", "time": "07:12"}],
            },
            {
                "id": "ask_hoang_if_nervous",
                "text": "Anh có hơi lo khi rủ thẳng vậy không?",
                "once": True,
                "effects": {"story_add": {"tam_hoang_interest": 1, "hoang_self_acceptance": 1}, "flags": ["tam_c04_w03_phone_asks_hoang_directness"]},
                "response_messages": [{"id": "r01", "sender": "hoang", "text": "Có. Nhưng anh đang cố không dùng sự lịch sự làm áo chống đạn nữa.", "time": "07:12"}],
            },
        ],
        "tam_c04_w03_quang_returns_umbrella": [
            {
                "id": "ask_quang_to_bring_umbrella",
                "text": "Tối anh mang qua nhé. Em lại sắp quên tiếp rồi.",
                "once": True,
                "effects": {"story_add": {"tam_quang_interest": 1}, "flags": ["tam_c04_w03_phone_asks_quang_bring_umbrella"]},
                "response_messages": [{"id": "r01", "sender": "quang", "text": "Anh biết. Đó là lý do anh chưa để nó xuống kho.", "time": "21:21"}],
            },
            {
                "id": "tell_quang_leave_with_thienan_files",
                "text": "Anh mang cùng hồ sơ của chị An đi. Đỡ phải tìm cớ hai lần.",
                "once": True,
                "effects": {"story_add": {"thienan_quang_trust": 1, "quang_persistence": 1}, "flags": ["tam_c04_w03_phone_redirects_quang_to_thienan"]},
                "response_messages": [{"id": "r01", "sender": "quang", "text": "Em nói như thể anh đang tìm cớ.", "time": "21:21"}],
            },
        ],
    })
