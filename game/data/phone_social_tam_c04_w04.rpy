# FILE: game/data/phone_social_tam_c04_w04.rpy
# Week 04 and Month 01 snapshot social posts.

init -5 python:

    PHONE_SOCIAL_POSTS.update({
        "huyen_c04_w04_review_post": {
            "id": "huyen_c04_w04_review_post",
            "author": "huyen",
            "content": "Bị nhận xét đúng không làm câu chữ bớt khó chịu. Chỉ làm mình khó phản bác hơn.",
            "image": None,
            "unlock_conditions": ["flag:tam_c04_w04_completed"],
            "sort_order": 635,
            "comments": [
                {"author": "tam", "text": "Tao tưởng mày đã tìm được một chỗ dùng từ hơi quá."},
                {"author": "huyen", "text": "Đang tiếp tục điều tra."},
            ],
            "effects_on_read": {"flags": ["read_huyen_c04_w04_review_post"]},
            "effects_on_like": {},
        },
        "hoang_c04_m01_strong_post": {
            "id": "hoang_c04_m01_strong_post",
            "author": "hoang",
            "content": "Có những kế hoạch không cần phương án rút lui. Chỉ cần phương án đổi giờ.",
            "image": None,
            "unlock_conditions": ["flag:tam_c04_m01_hoang_strong"],
            "sort_order": 645,
            "comments": [
                {"author": "tam", "text": "Nghe khá chuyên nghiệp."},
                {"author": "hoang", "text": "Tôi đã có một tháng thực tập."},
            ],
            "effects_on_read": {"flags": ["read_hoang_c04_m01_strong_post"]},
            "effects_on_like": {"story_add": {"tam_hoang_interest": 1}, "flags": ["liked_hoang_c04_m01_strong_post"]},
        },
        "huyen_c04_m01_quan_progress_post": {
            "id": "huyen_c04_m01_quan_progress_post",
            "author": "huyen",
            "content": "Tháng này học được một kỹ năng mới: nghe một chữ “được” mà tự hiểu đó là cả đoạn văn.",
            "image": None,
            "unlock_conditions": ["flag:tam_c04_m01_huyen_quan_progressing"],
            "sort_order": 642,
            "comments": [
                {"author": "tam", "text": "Tự tin vào khả năng đọc hiểu ghê."},
                {"author": "huyen", "text": "Tao có dữ liệu lặp lại đủ nhiều."},
            ],
            "effects_on_read": {
                "flags": ["read_huyen_c04_m01_quan_progress_post"],
                "known_info_add": {"huyen": ["Sự công nhận của Quân đã trở thành một thước đo mà Huyền để ý, dù cô vẫn giấu nó trong lời than."]},
            },
            "effects_on_like": {},
        },
        "thienan_c04_m01_quang_progress_post": {
            "id": "thienan_c04_m01_quang_progress_post",
            "author": "thienan",
            "content": "Có người gửi lịch trình trước cả khi mình kịp nói là không cần. Phiền, nhưng dùng được.",
            "image": None,
            "unlock_conditions": ["flag:tam_c04_m01_quang_thienan_progressing"],
            "sort_order": 640,
            "comments": [
                {"author": "tam", "text": "“Dùng được” là lời khen lớn rồi."},
                {"author": "thienan", "text": "Em bớt phiên dịch đi."},
            ],
            "effects_on_read": {"flags": ["read_thienan_c04_m01_quang_progress_post"]},
            "effects_on_like": {},
        },
        "tam_c04_m01_career_post": {
            "id": "tam_c04_m01_career_post",
            "author": "tam",
            "content": "Tên mình đứng một mình trên một dòng công việc trông hơi trống. Nhưng cũng khá ngay ngắn.",
            "image": None,
            "unlock_conditions": ["flag:tam_c04_m01_tam_career_strong"],
            "sort_order": 650,
            "comments": [
                {"author": "huyen", "text": "Ngay ngắn rồi thì nhớ làm cho xong."},
                {"author": "tam", "text": "Cảm ơn lời động viên rất có tình người."},
            ],
            "effects_on_read": {"flags": ["read_tam_c04_m01_career_post"]},
            "effects_on_like": {},
        },
    })
