init -5 python:

    PHONE_THREADS = {
        "tam_huyen_first_job": {
            "id": "tam_huyen_first_job",
            "type": "chat",
            "contact_id": "huyen",
            "title": "Huyen",
            "unlock_conditions": ["completed:tam_c01_interview_day"],
            "sort_order": 110,
            "messages": [
                {
                    "id": "m01",
                    "sender": "huyen",
                    "text": "Cau ve den nha chua? Hay van con dung o cong ty de tieu hoa niem vui?",
                    "time": "20:11",
                },
                {
                    "id": "m02",
                    "sender": "player",
                    "text": "Ve roi. Van thay moi thu dien ra nhanh qua.",
                    "time": "20:12",
                },
                {
                    "id": "m03",
                    "sender": "huyen",
                    "text": "Nhanh la tot. Cham moi de nghi lung tung.",
                    "time": "20:13",
                },
            ],
            "effects_on_read": {
                "flags": ["read_huyen_first_job_thread"],
            },
        },
        "group_company_party_recap": {
            "id": "group_company_party_recap",
            "type": "group_chat",
            "contact_id": None,
            "title": "After Party",
            "participants": ["tam", "huyen", "hoang"],
            "unlock_conditions": ["completed:tam_c02_company_party"],
            "sort_order": 100,
            "messages": [
                {
                    "id": "m01",
                    "sender": "huyen",
                    "text": "Toi xin phep tuyen bo: giay cao got la hinh thuc tra tan hop phap.",
                    "time": "23:16",
                },
                {
                    "id": "m02",
                    "sender": "tam",
                    "text": "Cau noi the sau khi dung ca toi van con dep nhat ban la hoi vo ly do.",
                    "time": "23:17",
                },
                {
                    "id": "m03",
                    "sender": "hoang",
                    "text": "Toi nghi phan cao got dang thang.",
                    "time": "23:18",
                },
            ],
            "effects_on_read": {
                "flags": ["read_group_party_recap"],
            },
        },
        "tam_hoang_after_party_01": {
            "id": "tam_hoang_after_party_01",
            "type": "chat",
            "contact_id": "hoang",
            "title": "Hoang",
            "unlock_conditions": ["completed:tam_c02_company_party"],
            "sort_order": 120,
            "messages": [
                {
                    "id": "m01",
                    "sender": "hoang",
                    "text": "Ve den nha chua?",
                    "time": "22:48",
                },
                {
                    "id": "m02",
                    "sender": "player",
                    "text": "Roi. Anh cung ve roi chu?",
                    "time": "22:49",
                },
                {
                    "id": "m03",
                    "sender": "hoang",
                    "text": "U. Nhung ca vat van chua song sot.",
                    "time": "22:50",
                },
            ],
            "effects_on_read": {
                "flags": ["read_hoang_after_party_message"],
            },
        },
        "tam_minh_return": {
            "id": "tam_minh_return",
            "type": "chat",
            "contact_id": "minh",
            "title": "Minh",
            "unlock_conditions": ["completed:tam_c06_minh_returns"],
            "sort_order": 95,
            "messages": [
                {
                    "id": "m01",
                    "sender": "minh",
                    "text": "Mai den som duoc khong? Anh muon xem qua brief truoc khi vao hop.",
                    "time": "21:04",
                },
                {
                    "id": "m02",
                    "sender": "player",
                    "text": "Duoc. Em se chuan bi tu toi nay.",
                    "time": "21:07",
                },
                {
                    "id": "m03",
                    "sender": "minh",
                    "text": "Tot. Dung de ap luc lam em bo sot dieu em da thay.",
                    "time": "21:08",
                },
            ],
            "effects_on_read": {
                "flags": ["read_minh_return_thread"],
            },
        },
    }

    PHONE_REPLY_CHOICES = {
        "tam_hoang_after_party_01": [
            {
                "id": "ask_if_ok",
                "text": "Anh on chu?",
                "once": True,
                "effects": {
                    "story_add": {"hoang_tam_trust": 1},
                    "flags": ["tam_asked_hoang_if_ok_after_party"],
                },
                "response_messages": [
                    {
                        "id": "r01",
                        "sender": "hoang",
                        "text": "On. Chi la hoi khong quen khi co nguoi hoi vay.",
                        "time": "22:54",
                    },
                ],
            },
            {
                "id": "tease_necktie",
                "text": "Em nghi ca vat do da hy sinh anh dung.",
                "once": True,
                "effects": {
                    "story_add": {"tam_hoang_interest": 1},
                    "flags": ["tam_teased_hoang_after_party"],
                },
                "response_messages": [
                    {
                        "id": "r01",
                        "sender": "hoang",
                        "text": "Anh se ghi nhan long thuong tiec muon mang nay.",
                        "time": "22:54",
                    },
                ],
            },
        ],
    }
