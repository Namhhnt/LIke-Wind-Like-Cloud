# FILE: game/data/phone_social_tam_c04_w02.rpy
# Week 02 social posts. Posts communicate route health through subtext.

init -5 python:

    PHONE_SOCIAL_POSTS.update({
        "huyen_c04_w02_predicted_comment_post": {
            "id": "huyen_c04_w02_predicted_comment_post",
            "author": "huyen",
            "content": "Đáng sợ không phải là bị bắt lỗi. Đáng sợ là mình bắt đầu biết người ta sẽ bắt lỗi ở đâu.",
            "image": None,
            "unlock_conditions": [
                "flag:tam_c04_w02_started",
            ],
            "sort_order": 430,
            "comments": [
                {
                    "author": "tam",
                    "text": "Tao tưởng đó gọi là tiến bộ.",
                },
                {
                    "author": "huyen",
                    "text": "Từ ngữ tích cực không thay đổi được bản chất đáng ngờ.",
                },
            ],
            "effects_on_read": {
                "flags": ["read_huyen_c04_w02_predicted_comment_post"],
            },
            "effects_on_like": {
                "flags": ["liked_huyen_c04_w02_predicted_comment_post"],
            },
        },

        "huyen_c04_w02_one_word_post": {
            "id": "huyen_c04_w02_one_word_post",
            "author": "huyen",
            "content": "Hôm nay được cấp trên nói đúng một chữ: “Được.” Tạm thời chưa biết nên ăn mừng hay kiểm tra thính lực.",
            "image": None,
            "unlock_conditions": [
                "flag:tam_c04_w02_completed",
                "score_gte:huyen_quan_trust:20",
            ],
            "sort_order": 445,
            "comments": [
                {
                    "author": "tam",
                    "text": "Tao xác nhận mày nghe đúng.",
                },
                {
                    "author": "huyen",
                    "text": "Không ai hỏi nhân chứng.",
                },
            ],
            "effects_on_read": {
                "flags": ["read_huyen_c04_w02_one_word_post"],
                "known_info_add": {
                    "huyen": [
                        "Sự công nhận rất ngắn của Quân đã bắt đầu có trọng lượng với Huyền, dù cô vẫn giấu nó sau lời than.",
                    ],
                },
            },
            "effects_on_like": {},
        },

        "hoang_c04_w02_two_cups_post": {
            "id": "hoang_c04_w02_two_cups_post",
            "author": "hoang",
            "content": "Mua hai phần đôi khi chỉ là tính toán kém. Đôi khi không phải.",
            "image": None,
            "unlock_conditions": [
                "flag:tam_c04_w02_started",
                "score_gte:tam_hoang_interest:55",
            ],
            "sort_order": 440,
            "comments": [
                {
                    "author": "tam",
                    "text": "Bài đăng này có quyền giữ im lặng.",
                },
                {
                    "author": "hoang",
                    "text": "Tôi xin sử dụng quyền đó.",
                },
            ],
            "effects_on_read": {
                "flags": ["read_hoang_c04_w02_two_cups_post"],
            },
            "effects_on_like": {
                "story_add": {
                    "tam_hoang_interest": 1,
                },
                "flags": ["liked_hoang_c04_w02_two_cups_post"],
            },
        },

        "thienan_c04_w02_late_dinner_post": {
            "id": "thienan_c04_w02_late_dinner_post",
            "author": "thienan",
            "content": "Một ngày dài vẫn nên kết thúc bằng bữa tối. Dù hơi muộn.",
            "image": None,
            "unlock_conditions": [
                "flag:tam_c04_w02_completed",
                "score_gte:thienan_quang_trust:45",
            ],
            "sort_order": 435,
            "comments": [
                {
                    "author": "tam",
                    "text": "Cuối cùng chị cũng chịu ăn.",
                },
                {
                    "author": "thienan",
                    "text": "Em bớt báo cáo tình hình của chị đi.",
                },
            ],
            "effects_on_read": {
                "flags": ["read_thienan_c04_w02_late_dinner_post"],
                "known_info_add": {
                    "thienan": [
                        "Thiên An đã bắt đầu tiếp nhận sự chăm sóc của Quang, dù cô không công khai nhắc đến anh.",
                    ],
                },
            },
            "effects_on_like": {},
        },
    })
