# FILE: game/data/phone_threads_tam_c04_w04.rpy
# Week 04 private messages and Month 01 status responses.

init -5 python:

    PHONE_THREADS.update({
        "tam_c04_w04_huyen_month_review": {
            "id": "tam_c04_w04_huyen_month_review",
            "type": "chat",
            "contact_id": "huyen",
            "title": "Huyền",
            "unlock_conditions": ["flag:tam_c04_w04_started"],
            "sort_order": 610,
            "messages": [
                {"id": "m01", "sender": "huyen", "text": "Chiều nay review tháng.", "time": "06:42"},
                {"id": "m02", "sender": "player", "text": "Tao biết. Mày gửi lịch cho tao từ tối qua rồi.", "time": "06:44"},
                {"id": "m03", "sender": "huyen", "text": "Tao đang đảm bảo ít nhất có một người cùng chịu áp lực.", "time": "06:45"},
            ],
            "effects_on_read": {"flags": ["read_tam_c04_w04_huyen_month_review"]},
        },
        "tam_c04_w04_hoang_fixed_time": {
            "id": "tam_c04_w04_hoang_fixed_time",
            "type": "chat",
            "contact_id": "hoang",
            "title": "Hoàng",
            "unlock_conditions": ["flag:tam_c04_w04_started", "score_gte:tam_hoang_interest:60"],
            "sort_order": 620,
            "messages": [
                {"id": "m01", "sender": "hoang", "text": "Thứ Bảy, chín giờ. Anh đón em ở chỗ cũ.", "time": "07:02"},
                {"id": "m02", "sender": "player", "text": "Không có câu nếu em bận thì thôi à?", "time": "07:04"},
                {"id": "m03", "sender": "hoang", "text": "Nếu em bận thì báo anh đổi giờ. Kế hoạch vẫn còn.", "time": "07:05"},
            ],
            "effects_on_read": {"flags": ["read_tam_c04_w04_hoang_fixed_time"]},
        },
        "tam_c04_w04_quang_umbrella_answer": {
            "id": "tam_c04_w04_quang_umbrella_answer",
            "type": "chat",
            "contact_id": "quang",
            "title": "Quang",
            "unlock_conditions": ["flag:tam_c04_w04_started", "score_gte:tam_quang_interest:12"],
            "sort_order": 615,
            "messages": [
                {"id": "m01", "sender": "player", "text": "Anh nghĩ xong câu trả lời về chiếc ô chưa?", "time": "21:11"},
                {"id": "m02", "sender": "quang", "text": "Chưa.", "time": "21:14"},
                {"id": "m03", "sender": "quang", "text": "Nhưng anh không quên câu hỏi.", "time": "21:15"},
            ],
            "effects_on_read": {"flags": ["read_tam_c04_w04_quang_umbrella_answer"]},
        },
    })

    PHONE_REPLY_CHOICES.update({
        "tam_c04_w04_huyen_month_review": [
            {
                "id": "reassure_huyen_review",
                "text": "Có gì thì cùng nghe. Nhưng phần của ai người đó nhận nhé.",
                "once": True,
                "effects": {"story_add": {"career_tam": 1, "career_huyen": 1}, "flags": ["tam_c04_w04_phone_sets_review_boundary"]},
                "response_messages": [{"id": "r01", "sender": "huyen", "text": "Nghe trưởng thành đáng ghét thật. Được.", "time": "06:48"}],
            },
            {
                "id": "tease_huyen_quan_review",
                "text": "Mày lo review hay lo người review?",
                "once": True,
                "effects": {"story_add": {"huyen_quan_trust": 1}, "flags": ["tam_c04_w04_phone_teases_huyen_review"]},
                "response_messages": [{"id": "r01", "sender": "huyen", "text": "Tao sẽ chặn mày trước giờ họp để giữ tinh thần ổn định.", "time": "06:48"}],
            },
        ],
        "tam_c04_w04_hoang_fixed_time": [
            {
                "id": "confirm_hoang_fixed_time",
                "text": "Được. Lần này em sẽ báo sớm nếu có gì đổi.",
                "once": True,
                "effects": {"story_add": {"tam_hoang_interest": 1, "hoang_tam_trust": 1}, "flags": ["tam_c04_w04_phone_confirms_hoang_time"]},
                "response_messages": [{"id": "r01", "sender": "hoang", "text": "Anh cũng vậy. Như người lớn có lịch trình hẳn hoi.", "time": "07:07"}],
            },
            {
                "id": "praise_hoang_directness",
                "text": "Cách này tốt hơn đấy.",
                "once": True,
                "effects": {"story_add": {"hoang_self_acceptance": 1, "hoang_tam_trust": 1}, "flags": ["tam_c04_w04_phone_praises_hoang_directness"]},
                "response_messages": [{"id": "r01", "sender": "hoang", "text": "Anh sẽ ghi nhận trước khi em bổ sung điều kiện.", "time": "07:07"}],
            },
        ],
        "tam_c04_w04_quang_umbrella_answer": [
            {
                "id": "give_quang_time",
                "text": "Được. Em chưa cần câu trả lời ngay.",
                "once": True,
                "effects": {"story_add": {"tam_quang_interest": 1, "quang_persistence": 1}, "flags": ["tam_c04_w04_phone_gives_quang_time"]},
                "response_messages": [{"id": "r01", "sender": "quang", "text": "Anh biết. Có lẽ vì vậy anh mới không muốn trả lời qua loa.", "time": "21:18"}],
            },
            {
                "id": "redirect_quang_to_thienan",
                "text": "Anh không cần trả lời em. Nhớ trả lời chị An đúng lúc là được.",
                "once": True,
                "effects": {"story_add": {"thienan_quang_trust": 1, "quang_persistence": 1}, "flags": ["tam_c04_w04_phone_redirects_quang_answer"]},
                "response_messages": [{"id": "r01", "sender": "quang", "text": "Hai câu hỏi không giống nhau đâu, Tâm.", "time": "21:18"}],
            },
        ],
    })
