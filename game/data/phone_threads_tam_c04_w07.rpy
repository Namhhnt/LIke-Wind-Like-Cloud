# FILE: game/data/phone_threads_tam_c04_w07.rpy
# Week 07 private messages.

init -5 python:

    PHONE_THREADS.update({
        "tam_c04_w07_huyen_one_period": {
            "id": "tam_c04_w07_huyen_one_period",
            "type": "chat",
            "contact_id": "huyen",
            "title": "Huyền",
            "unlock_conditions": ["flag:tam_c04_w07_started", "score_gte:huyen_quan_trust:40"],
            "sort_order": 910,
            "messages": [
                {"id": "m01", "sender": "huyen", "text": "Anh Quân trả lời ‘được.’ Có dấu chấm.", "time": "06:58"},
                {"id": "m02", "sender": "player", "text": "Một dấu chấm bình thường.", "time": "07:00"},
                {"id": "m03", "sender": "huyen", "text": "Mày không hiểu dữ liệu lịch sử.", "time": "07:01"},
            ],
            "effects_on_read": {"flags": ["read_tam_c04_w07_huyen_one_period"]},
        },
        "tam_c04_w07_hoang_breakfast": {
            "id": "tam_c04_w07_hoang_breakfast",
            "type": "chat",
            "contact_id": "hoang",
            "title": "Hoàng",
            "unlock_conditions": ["flag:tam_c04_w07_started", "score_gte:tam_hoang_interest:60"],
            "sort_order": 920,
            "messages": [
                {"id": "m01", "sender": "hoang", "text": "Em ăn sáng chưa?", "time": "07:06"},
                {"id": "m02", "sender": "player", "text": "Rồi.", "time": "07:07"},
                {"id": "m03", "sender": "hoang", "text": "Trả lời nhanh quá. Anh không tin.", "time": "07:08"},
            ],
            "effects_on_read": {"flags": ["read_tam_c04_w07_hoang_breakfast"]},
        },
        "tam_c04_w07_quang_lunch_box": {
            "id": "tam_c04_w07_quang_lunch_box",
            "type": "chat",
            "contact_id": "quang",
            "title": "Quang",
            "unlock_conditions": ["flag:tam_c04_w07_started"],
            "sort_order": 915,
            "messages": [
                {"id": "m01", "sender": "quang", "text": "Hộp thức ăn của em còn ở chỗ anh.", "time": "20:16"},
                {"id": "m02", "sender": "player", "text": "Tuần trước anh bảo là hộp của anh.", "time": "20:18"},
                {"id": "m03", "sender": "quang", "text": "Anh nhớ nhầm.", "time": "20:19"},
            ],
            "effects_on_read": {"flags": ["read_tam_c04_w07_quang_lunch_box"]},
        },
    })

    PHONE_REPLY_CHOICES.update({
        "tam_c04_w07_huyen_one_period": [
            {
                "id": "say_huyen_knows_him",
                "text": "Mày hiểu cách ổng viết hơn trước rồi.",
                "once": True,
                "effects": {"story_add": {"huyen_quan_trust": 1, "huyen_quan_interest": 1}, "flags": ["tam_c04_w07_phone_huyen_knows_quan"]},
                "response_messages": [{"id": "r01", "sender": "huyen", "text": "Tao hiểu công việc. Không hiểu người.", "time": "07:03"}],
            },
            {
                "id": "tell_huyen_stop_counting",
                "text": "Đừng đếm dấu chấm nữa. Làm việc đi.",
                "once": True,
                "effects": {"story_add": {"career_huyen": 1}, "flags": ["tam_c04_w07_phone_huyen_back_to_work"]},
                "response_messages": [{"id": "r01", "sender": "huyen", "text": "Tao đang làm nghiên cứu định tính.", "time": "07:03"}],
            },
        ],
        "tam_c04_w07_hoang_breakfast": [
            {
                "id": "admit_no_breakfast",
                "text": "Chưa. Em sẽ ăn.",
                "once": True,
                "effects": {"story_add": {"tam_hoang_interest": 1, "hoang_tam_trust": 1}, "flags": ["tam_c04_w07_phone_admits_no_breakfast"]},
                "response_messages": [{"id": "r01", "sender": "hoang", "text": "Anh gửi quán gần công ty. Không cần báo cáo lại.", "time": "07:10"}],
            },
            {
                "id": "tease_hoang_reading_speed",
                "text": "Anh còn đo cả tốc độ trả lời à?",
                "once": True,
                "effects": {"story_add": {"tam_hoang_interest": 1, "hoang_self_acceptance": 1}, "flags": ["tam_c04_w07_phone_teases_hoang_speed"]},
                "response_messages": [{"id": "r01", "sender": "hoang", "text": "Chỉ khi em nói dối không kỹ.", "time": "07:10"}],
            },
        ],
        "tam_c04_w07_quang_lunch_box": [
            {
                "id": "ask_quang_added_fruit",
                "text": "Anh có bỏ thêm gì vào không?",
                "once": True,
                "effects": {"story_add": {"tam_quang_interest": 1}, "tam_c04_extended_story_add": {"quang_tam_warmth": 1, "quang_tam_awareness": 2}, "flags": ["tam_c04_w07_phone_asks_quang_fruit"]},
                "response_messages": [{"id": "r01", "sender": "quang", "text": "Không nhiều.", "time": "20:21"}],
            },
            {
                "id": "ask_quang_take_an_food",
                "text": "Nếu còn đồ ăn thì mang cho chị An giúp em.",
                "once": True,
                "effects": {"story_add": {"thienan_quang_trust": 1}, "tam_c04_extended_story_add": {"quang_thienan_resolve": 1}, "flags": ["tam_c04_w07_phone_quang_food_to_an"]},
                "response_messages": [{"id": "r01", "sender": "quang", "text": "Anh sẽ hỏi chị ấy trước.", "time": "20:21"}],
            },
        ],
    })
