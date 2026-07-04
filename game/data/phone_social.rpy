init -5 python:

    PHONE_SOCIAL_POSTS = {
        "huyen_party_post_01": {
            "id": "huyen_party_post_01",
            "author": "huyen",
            "content": "Co nhung buoi tiec khong met vi ruou, ma met vi phai cuoi dung luc.",
            "image": None,
            "unlock_conditions": ["completed:tam_c02_company_party"],
            "sort_order": 100,
            "comments": [
                {
                    "author": "tam",
                    "text": "Nghe nguy hiem vay.",
                },
                {
                    "author": "huyen",
                    "text": "Khong. Chi la giay cao qua thoi.",
                },
            ],
            "effects_on_read": {
                "flags": ["read_huyen_party_post"],
            },
            "effects_on_like": {
                "flags": ["liked_huyen_party_post"],
            },
        },
        "yuuka_festival_post_01": {
            "id": "yuuka_festival_post_01",
            "author": "yuuka",
            "content": "Some places only become honest after dark.",
            "image": None,
            "unlock_conditions": ["completed:yuuka_c08_festival_arrival"],
            "sort_order": 90,
            "comments": [
                {
                    "author": "tam",
                    "text": "That sounds beautiful and a little lonely.",
                },
            ],
            "effects_on_read": {
                "known_info_add": {
                    "yuuka": ["Publicly polished, but her posts leave room for distance."],
                },
            },
            "effects_on_like": {},
        },
    }
