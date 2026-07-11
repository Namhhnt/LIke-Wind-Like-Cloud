# FILE: game/data/phone_social_tam_c04_w05.rpy
# Week 05 social posts.

init -5 python:
    PHONE_SOCIAL_POSTS.update({
        "huyen_c04_w05_ownership_post": {
            "id": "huyen_c04_w05_ownership_post", "author": "huyen",
            "content": "Khi tên mình đứng một mình ở dòng phụ trách, cái file tự nhiên nặng hơn khoảng hai ký.",
            "image": None, "unlock_conditions": ["flag:tam_c04_w05_completed"], "sort_order": 735,
            "comments": [
                {"author": "tam", "text": "Hai ký đó là trách nhiệm."},
                {"author": "huyen", "text": "Tao đang tìm cách nén file."},
            ],
            "effects_on_read": {"flags": ["read_huyen_c04_w05_ownership_post"]}, "effects_on_like": {},
        },
        "hoang_c04_w05_house_post": {
            "id": "hoang_c04_w05_house_post", "author": "hoang",
            "content": "Có người sắp tới nhà nên mới nhận ra một chiếc ghế đã đặt sai hướng khá lâu.",
            "image": None, "unlock_conditions": ["flag:tam_c04_w05_tam_accepts_hoang_house_invitation"], "sort_order": 745,
            "comments": [
                {"author": "tam", "text": "Người đó khó tính vậy à?"},
                {"author": "hoang", "text": "Không. Người chuẩn bị hơi lo thôi."},
            ],
            "effects_on_read": {"flags": ["read_hoang_c04_w05_house_post"]},
            "effects_on_like": {"story_add": {"tam_hoang_interest": 1}, "flags": ["liked_hoang_c04_w05_house_post"]},
        },
        "thienan_c04_w05_schedule_post": {
            "id": "thienan_c04_w05_schedule_post", "author": "thienan",
            "content": "Có người tự gửi lịch trình trước khi được hỏi. Ít nhất lần này có giờ cụ thể.",
            "image": None, "unlock_conditions": ["flag:tam_c04_w05_tam_leaves_quang_to_speak"], "sort_order": 740,
            "comments": [
                {"author": "tam", "text": "Tiến bộ rồi."},
                {"author": "thienan", "text": "Em đừng chấm điểm."},
            ],
            "effects_on_read": {"flags": ["read_thienan_c04_w05_schedule_post"]}, "effects_on_like": {},
        },
    })
