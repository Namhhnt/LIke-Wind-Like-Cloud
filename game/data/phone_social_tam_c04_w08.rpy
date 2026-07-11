# FILE: game/data/phone_social_tam_c04_w08.rpy
# Week 08 and Month 02 snapshot social posts.

init -5 python:
    PHONE_SOCIAL_POSTS.update({
        "huyen_c04_w08_review_post": {
            "id": "huyen_c04_w08_review_post", "author": "huyen",
            "content": "Tháng thứ hai: bị góp ý ít hơn, nhưng mỗi câu khó chịu hơn vì mình hiểu nó đúng ở đâu.",
            "image": None, "unlock_conditions": ["flag:tam_c04_w08_completed"], "sort_order": 1035,
            "comments": [
                {"author": "tam", "text": "Tiến bộ có tác dụng phụ."},
                {"author": "huyen", "text": "Tao muốn đọc kỹ điều khoản trước khi tiến tiếp."},
            ],
            "effects_on_read": {"flags": ["read_huyen_c04_w08_review_post"]}, "effects_on_like": {},
        },
        "hoang_c04_m02_deepening_post": {
            "id": "hoang_c04_m02_deepening_post", "author": "hoang",
            "content": "Có những người không cần hỏi lại họ có tới không. Chỉ cần nhớ đúng giờ họ đã nói.",
            "image": None, "unlock_conditions": ["flag:tam_c04_m02_hoang_deepening"], "sort_order": 1048,
            "comments": [
                {"author": "tam", "text": "Nghe tự tin hơn trước rồi."},
                {"author": "hoang", "text": "Có người đã cho anh đủ dữ liệu."},
            ],
            "effects_on_read": {"flags": ["read_hoang_c04_m02_deepening_post"]},
            "effects_on_like": {"story_add": {"tam_hoang_interest": 1}, "flags": ["liked_hoang_c04_m02_deepening_post"]},
        },
        "huyen_c04_m02_personal_post": {
            "id": "huyen_c04_m02_personal_post", "author": "huyen",
            "content": "Tự làm được không có nghĩa là không nhận ra ai đã ngồi lại xem bản cuối.",
            "image": None, "unlock_conditions": ["flag:tam_c04_m02_huyen_quan_personal_progress"], "sort_order": 1045,
            "comments": [
                {"author": "tam", "text": "Ai cơ?"},
                {"author": "huyen", "text": "Người review. Đừng diễn."},
            ],
            "effects_on_read": {
                "flags": ["read_huyen_c04_m02_personal_post"],
                "known_info_add": {"huyen": ["Huyền đã bắt đầu để ý sự hiện diện của Quân ngoài giá trị công việc, nhưng vẫn chỉ gọi đó là review."]},
            },
            "effects_on_like": {},
        },
        "thienan_c04_m02_direct_post": {
            "id": "thienan_c04_m02_direct_post", "author": "thienan",
            "content": "Báo trước. Hỏi trước. Rồi mới giúp. Có người cuối cùng cũng học đúng thứ tự.",
            "image": None, "unlock_conditions": ["flag:tam_c04_m02_quang_thienan_direct"], "sort_order": 1042,
            "comments": [
                {"author": "tam", "text": "Em nghe như lời khen."},
                {"author": "thienan", "text": "Không phải việc gì cũng cần em xác nhận."},
            ],
            "effects_on_read": {"flags": ["read_thienan_c04_m02_direct_post"]}, "effects_on_like": {},
        },
        "tam_c04_m02_quang_post": {
            "id": "tam_c04_m02_quang_post", "author": "tam",
            "content": "Có những câu hỏi người ta không trả lời ngay. Khó chịu nhất là khi mình biết họ không quên.",
            "image": None, "unlock_conditions": ["flag:tam_c04_m02_tam_quang_personal_progress"], "sort_order": 1040,
            "comments": [
                {"author": "huyen", "text": "Nghe mơ hồ đáng ngờ."},
                {"author": "tam", "text": "Tao đang nói về công việc."},
            ],
            "effects_on_read": {"flags": ["read_tam_c04_m02_quang_post"]}, "effects_on_like": {},
        },
        "tam_c04_m02_career_post": {
            "id": "tam_c04_m02_career_post", "author": "tam",
            "content": "Được quyền quyết định nghe nhẹ hơn chịu trách nhiệm cho quyết định. Hai thứ thường đi cùng một dòng.",
            "image": None, "unlock_conditions": ["flag:tam_c04_m02_tam_career_level_ready"], "sort_order": 1050,
            "comments": [
                {"author": "huyen", "text": "Ít nhất chức danh mới sẽ dài hơn."},
                {"author": "tam", "text": "Tao chưa nói là được tăng chức."},
            ],
            "effects_on_read": {"flags": ["read_tam_c04_m02_career_post"]}, "effects_on_like": {},
        },
    })
