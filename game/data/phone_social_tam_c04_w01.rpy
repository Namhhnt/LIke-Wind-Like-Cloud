# FILE: game/data/phone_social_tam_c04_w01.rpy
# Week 01 social posts. Route strength controls how much public information appears.

init -5 python:

    PHONE_SOCIAL_POSTS.update({
        "huyen_c04_w01_red_mark_post": {
            "id": "huyen_c04_w01_red_mark_post",
            "author": "huyen",
            "content": "Có những người không cần lớn tiếng. Họ chỉ cần khoanh đỏ đúng chỗ là mình tự thấy cuộc đời hơi sai.",
            "image": None,
            "unlock_conditions": [
                "flag:tam_c04_w01_started",
            ],
            "sort_order": 330,
            "comments": [
                {
                    "author": "tam",
                    "text": "Nghe như một lời cầu cứu.",
                },
                {
                    "author": "huyen",
                    "text": "Không. Là biên bản hiện trường.",
                },
            ],
            "effects_on_read": {
                "flags": ["read_huyen_c04_w01_red_mark_post"],
            },
            "effects_on_like": {
                "flags": ["liked_huyen_c04_w01_red_mark_post"],
            },
        },

        "huyen_c04_w01_quan_standard_post": {
            "id": "huyen_c04_w01_quan_standard_post",
            "author": "huyen",
            "content": "Khó chịu nhất là lúc người khó tính nói đúng. Mình không cãi được, chỉ có thể về sửa file.",
            "image": None,
            "unlock_conditions": [
                "flag:tam_c04_w01_completed",
                "score_gte:huyen_quan_trust:15",
            ],
            "sort_order": 335,
            "comments": [
                {
                    "author": "tam",
                    "text": "Tao sẽ lưu bài này lại.",
                },
                {
                    "author": "huyen",
                    "text": "Mày sẽ bị chặn.",
                },
            ],
            "effects_on_read": {
                "flags": ["read_huyen_c04_w01_quan_standard_post"],
                "known_info_add": {
                    "huyen": [
                        "Huyền bắt đầu thừa nhận tiêu chuẩn của Quân có lý, dù cô vẫn phản kháng cách anh thể hiện nó.",
                    ],
                },
            },
            "effects_on_like": {},
        },

        "hoang_c04_w01_quiet_morning_post": {
            "id": "hoang_c04_w01_quiet_morning_post",
            "author": "hoang",
            "content": "Đầu tuần sửa được một góc phòng. Chưa sửa được lịch ngủ.",
            "image": None,
            "unlock_conditions": [
                "flag:tam_c04_w01_started",
                "score_gte:tam_hoang_interest:50",
            ],
            "sort_order": 325,
            "comments": [
                {
                    "author": "tam",
                    "text": "Ít nhất anh còn biết phần nào cần sửa.",
                },
                {
                    "author": "hoang",
                    "text": "Biết và làm là hai giai đoạn khác nhau.",
                },
            ],
            "effects_on_read": {
                "flags": ["read_hoang_c04_w01_quiet_morning_post"],
            },
            "effects_on_like": {
                "story_add": {
                    "tam_hoang_interest": 1,
                },
                "flags": ["liked_hoang_c04_w01_quiet_morning_post"],
            },
        },
    })
