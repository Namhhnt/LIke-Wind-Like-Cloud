# FILE: game/data/phone_social_tam_c04_w06.rpy
# Week 06 social posts.

init -5 python:
    PHONE_SOCIAL_POSTS.update({
        "huyen_c04_w06_empty_chair_post": {
            "id": "huyen_c04_w06_empty_chair_post", "author": "huyen",
            "content": "Văn phòng yên hơn không đồng nghĩa với dễ làm việc hơn. Đôi khi chỉ thiếu người khoanh đỏ đúng chỗ.",
            "image": None, "unlock_conditions": ["flag:tam_c04_w06_completed"], "sort_order": 835,
            "comments": [
                {"author": "tam", "text": "Tao tưởng mày thích yên."},
                {"author": "huyen", "text": "Yên có cấu trúc khác yên vô tổ chức."},
            ],
            "effects_on_read": {"flags": ["read_huyen_c04_w06_empty_chair_post"]}, "effects_on_like": {},
        },
        "hoang_c04_w06_chair_post": {
            "id": "hoang_c04_w06_chair_post", "author": "hoang",
            "content": "Có vài thứ trong nhà không cần sửa. Chỉ cần đặt đúng chỗ cho đúng người.",
            "image": None, "unlock_conditions": ["flag:tam_c04_w06_tam_notices_hoang_seat"], "sort_order": 845,
            "comments": [
                {"author": "tam", "text": "Nghe như anh vừa sửa cả nhà."},
                {"author": "hoang", "text": "Anh chỉ đổi một chiếc ghế."},
            ],
            "effects_on_read": {"flags": ["read_hoang_c04_w06_chair_post"]},
            "effects_on_like": {"story_add": {"hoang_tam_trust": 1}, "flags": ["liked_hoang_c04_w06_chair_post"]},
        },
        "tam_c04_w06_scope_post": {
            "id": "tam_c04_w06_scope_post", "author": "tam",
            "content": "Từ chối một việc không nằm trong phạm vi khó hơn làm thêm nó. Nhưng đôi khi đó mới là phần việc cần làm.",
            "image": None, "unlock_conditions": ["flag:tam_c04_w06_tam_rejects_scope_change"], "sort_order": 850,
            "comments": [
                {"author": "huyen", "text": "Cuối cùng cũng học được cách nói không."},
                {"author": "tam", "text": "Tao đang học cách nói có điều kiện."},
            ],
            "effects_on_read": {"flags": ["read_tam_c04_w06_scope_post"]}, "effects_on_like": {},
        },
    })
