# FILE: game/data/phone_social_tam_c04_w03.rpy
# Week 03 social posts: pressure makes route movement more visible.

init -5 python:

    PHONE_SOCIAL_POSTS.update({
        "huyen_c04_w03_standard_post": {
            "id": "huyen_c04_w03_standard_post",
            "author": "huyen",
            "content": "Tệ nhất không phải là người ta khó tính. Tệ nhất là một ngày mình phát hiện người ta khó tính có lý.",
            "image": None,
            "unlock_conditions": ["flag:tam_c04_w03_completed", "score_gte:huyen_quan_trust:25"],
            "sort_order": 535,
            "comments": [
                {"author": "tam", "text": "Tao sẽ lưu bài này làm bằng chứng."},
                {"author": "huyen", "text": "Bài đăng đã bị hiểu sai mục đích."},
            ],
            "effects_on_read": {"flags": ["read_huyen_c04_w03_standard_post"]},
            "effects_on_like": {},
        },
        "hoang_c04_w03_waiting_post": {
            "id": "hoang_c04_w03_waiting_post",
            "author": "hoang",
            "content": "Kế hoạch lệch một chút không có nghĩa là phải bỏ cả ngày.",
            "image": None,
            "unlock_conditions": ["flag:tam_c04_w03_completed", "score_gte:hoang_tam_trust:55"],
            "sort_order": 540,
            "comments": [
                {"author": "tam", "text": "Nghe như kinh nghiệm thực tế."},
                {"author": "hoang", "text": "Tôi xin không bình luận thêm."},
            ],
            "effects_on_read": {"flags": ["read_hoang_c04_w03_waiting_post"]},
            "effects_on_like": {"story_add": {"tam_hoang_interest": 1}, "flags": ["liked_hoang_c04_w03_waiting_post"]},
        },
        "thienan_c04_w03_airport_post": {
            "id": "thienan_c04_w03_airport_post",
            "author": "thienan",
            "content": "Đi sớm không làm chuyến công tác ngắn hơn. Chỉ làm cà phê sân bay đắt hơn.",
            "image": None,
            "unlock_conditions": ["flag:tam_c04_w03_completed", "score_gte:thienan_quang_trust:50"],
            "sort_order": 530,
            "comments": [
                {"author": "tam", "text": "Ít nhất chị có ăn sáng không?"},
                {"author": "thienan", "text": "Có người kiểm tra rồi."},
            ],
            "effects_on_read": {
                "flags": ["read_thienan_c04_w03_airport_post"],
                "known_info_add": {"thienan": ["Thiên An bắt đầu để Quang tham gia vào những chuẩn bị nhỏ quanh công việc của cô."]},
            },
            "effects_on_like": {},
        },
    })
