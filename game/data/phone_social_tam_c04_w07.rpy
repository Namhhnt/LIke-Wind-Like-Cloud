# FILE: game/data/phone_social_tam_c04_w07.rpy
# Week 07 social posts.

init -5 python:
    PHONE_SOCIAL_POSTS.update({
        "huyen_c04_w07_reason_post": {
            "id": "huyen_c04_w07_reason_post", "author": "huyen",
            "content": "Tranh luận có lý do vẫn mệt. Nhưng ít nhất sau đó không phải giả vờ mình chỉ đang khó chịu.",
            "image": None, "unlock_conditions": ["flag:tam_c04_w07_completed"], "sort_order": 935,
            "comments": [
                {"author": "tam", "text": "Mày vừa trưởng thành à?"},
                {"author": "huyen", "text": "Không. Tao chỉ có phụ lục."},
            ],
            "effects_on_read": {"flags": ["read_huyen_c04_w07_reason_post"]}, "effects_on_like": {},
        },
        "hoang_c04_w07_food_post": {
            "id": "hoang_c04_w07_food_post", "author": "hoang",
            "content": "Nhắc người khác ăn không khó. Khó là làm như mình không để ý họ đã bỏ bữa.",
            "image": None, "unlock_conditions": ["flag:tam_c04_w07_tam_admits_skipped_lunch_to_hoang"], "sort_order": 945,
            "comments": [
                {"author": "tam", "text": "Anh làm không giống lắm."},
                {"author": "hoang", "text": "Anh đang thiếu kinh nghiệm giả vờ."},
            ],
            "effects_on_read": {"flags": ["read_hoang_c04_w07_food_post"]},
            "effects_on_like": {"story_add": {"tam_hoang_interest": 1}, "flags": ["liked_hoang_c04_w07_food_post"]},
        },
        "thienan_c04_w07_notice_post": {
            "id": "thienan_c04_w07_notice_post", "author": "thienan",
            "content": "Giúp người khác không có nghĩa là được quyền tự đổi lịch của họ. Báo trước là một kỹ năng.",
            "image": None, "unlock_conditions": ["flag:tam_c04_w07_tam_refuses_to_interpret_thienan"], "sort_order": 940,
            "comments": [
                {"author": "tam", "text": "Có người đã gọi xin lỗi chưa?"},
                {"author": "thienan", "text": "Em nhiều chuyện vừa thôi."},
            ],
            "effects_on_read": {"flags": ["read_thienan_c04_w07_notice_post"]}, "effects_on_like": {},
        },
    })
