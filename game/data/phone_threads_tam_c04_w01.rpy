# FILE: game/data/phone_threads_tam_c04_w01.rpy
# Week 01 private-message content. All Vietnamese text intentionally uses full diacritics.

init -5 python:

    PHONE_THREADS.update({
        "tam_c04_w01_huyen_monday": {
            "id": "tam_c04_w01_huyen_monday",
            "type": "chat",
            "contact_id": "huyen",
            "title": "Huyền",
            "unlock_conditions": [
                "flag:tam_c04_w01_started",
            ],
            "sort_order": 310,
            "messages": [
                {
                    "id": "m01",
                    "sender": "huyen",
                    "text": "Tao vừa mở mail. Anh Quân gửi lúc 06:12.",
                    "time": "06:58",
                },
                {
                    "id": "m02",
                    "sender": "player",
                    "text": "Có gì bất thường?",
                    "time": "06:59",
                },
                {
                    "id": "m03",
                    "sender": "huyen",
                    "text": "Có. Ổng dùng dấu chấm hết ở tiêu đề.",
                    "time": "07:00",
                },
                {
                    "id": "m04",
                    "sender": "huyen",
                    "text": "Tao thấy bị đe dọa.",
                    "time": "07:00",
                },
            ],
            "effects_on_read": {
                "flags": ["read_tam_c04_w01_huyen_monday"],
                "known_info_add": {
                    "huyen": [
                        "Huyền phản ứng mạnh với tiêu chuẩn khắt khe của Quân, nhưng vẫn đọc kỹ mọi yêu cầu anh gửi.",
                    ],
                },
            },
        },

        "tam_c04_w01_hoang_monday": {
            "id": "tam_c04_w01_hoang_monday",
            "type": "chat",
            "contact_id": "hoang",
            "title": "Hoàng",
            "unlock_conditions": [
                "flag:tam_c04_w01_started",
                "score_gte:tam_hoang_interest:40",
            ],
            "sort_order": 320,
            "messages": [
                {
                    "id": "m01",
                    "sender": "hoang",
                    "text": "Sáng nay em có kịp ăn gì không?",
                    "time": "07:14",
                },
                {
                    "id": "m02",
                    "sender": "player",
                    "text": "Em đang cân nhắc xem cà phê có được tính là bữa sáng không.",
                    "time": "07:16",
                },
                {
                    "id": "m03",
                    "sender": "hoang",
                    "text": "Nếu em phải cân nhắc thì chắc là không.",
                    "time": "07:17",
                },
            ],
            "effects_on_read": {
                "flags": ["read_tam_c04_w01_hoang_monday"],
            },
        },

        "tam_c04_w01_quang_check_thienan": {
            "id": "tam_c04_w01_quang_check_thienan",
            "type": "chat",
            "contact_id": "quang",
            "title": "Quang",
            "unlock_conditions": [
                "flag:tam_c04_w01_started",
                "score_gte:thienan_quang_trust:35",
            ],
            "sort_order": 315,
            "messages": [
                {
                    "id": "m01",
                    "sender": "quang",
                    "text": "Tâm, tối qua chị An về nhà lúc mấy giờ?",
                    "time": "21:06",
                },
                {
                    "id": "m02",
                    "sender": "player",
                    "text": "Anh hỏi chị ấy chưa?",
                    "time": "21:08",
                },
                {
                    "id": "m03",
                    "sender": "quang",
                    "text": "Hỏi rồi. Chị ấy nói không muộn.",
                    "time": "21:09",
                },
                {
                    "id": "m04",
                    "sender": "player",
                    "text": "Vậy là muộn rồi.",
                    "time": "21:09",
                },
            ],
            "effects_on_read": {
                "flags": ["read_tam_c04_w01_quang_check_thienan"],
            },
        },
    })

    PHONE_REPLY_CHOICES.update({
        "tam_c04_w01_huyen_monday": [
            {
                "id": "offer_to_review_mail",
                "text": "Gửi tao xem. Có gì thì cùng làm.",
                "once": True,
                "effects": {
                    "story_add": {
                        "career_tam": 1,
                        "career_huyen": 1,
                    },
                    "flags": ["tam_c04_w01_offered_huyen_help_by_phone"],
                },
                "response_messages": [
                    {
                        "id": "r01",
                        "sender": "huyen",
                        "text": "Được. Nhưng nếu mày cũng thấy đáng sợ thì nhớ đứng về phía tao.",
                        "time": "07:03",
                    },
                ],
            },
            {
                "id": "tease_huyen_about_quan",
                "text": "Mày nhớ giờ gửi mail của anh ấy kỹ quá nhỉ.",
                "once": True,
                "effects": {
                    "story_add": {
                        "huyen_quan_trust": 1,
                    },
                    "flags": ["tam_c04_w01_teased_huyen_about_quan"],
                },
                "response_messages": [
                    {
                        "id": "r01",
                        "sender": "huyen",
                        "text": "Tao ghi nhớ giờ xảy ra tai nạn. Rất bình thường.",
                        "time": "07:03",
                    },
                ],
            },
        ],

        "tam_c04_w01_hoang_monday": [
            {
                "id": "accept_breakfast_reminder",
                "text": "Rồi, em sẽ ăn. Anh hài lòng chưa?",
                "once": True,
                "effects": {
                    "story_add": {
                        "hoang_tam_trust": 1,
                    },
                    "flags": ["tam_c04_w01_accepted_hoang_breakfast_reminder"],
                },
                "response_messages": [
                    {
                        "id": "r01",
                        "sender": "hoang",
                        "text": "Tạm thời. Anh không muốn đầu tuần đã phải nghi ngờ khả năng tự chăm sóc của em.",
                        "time": "07:19",
                    },
                ],
            },
            {
                "id": "ask_hoang_same_question",
                "text": "Còn anh thì ăn chưa?",
                "once": True,
                "effects": {
                    "story_add": {
                        "tam_hoang_interest": 1,
                        "hoang_tam_trust": 1,
                    },
                    "flags": ["tam_c04_w01_asked_hoang_breakfast"],
                },
                "response_messages": [
                    {
                        "id": "r01",
                        "sender": "hoang",
                        "text": "Rồi. Anh hỏi người khác sau khi đã tự làm gương. Khá chuyên nghiệp.",
                        "time": "07:19",
                    },
                ],
            },
        ],

        "tam_c04_w01_quang_check_thienan": [
            {
                "id": "tell_quang_to_ask_directly",
                "text": "Anh lo thì tự gọi chị ấy đi.",
                "once": True,
                "effects": {
                    "story_add": {
                        "thienan_quang_trust": 1,
                        "quang_persistence": 1,
                    },
                    "flags": ["tam_c04_w01_phone_support_quang_thienan"],
                },
                "response_messages": [
                    {
                        "id": "r01",
                        "sender": "quang",
                        "text": "Em nói nghe đơn giản thật.",
                        "time": "21:12",
                    },
                    {
                        "id": "r02",
                        "sender": "player",
                        "text": "Vì người phức tạp là anh, không phải cuộc gọi.",
                        "time": "21:13",
                    },
                ],
            },
            {
                "id": "tease_quang_for_asking_tam",
                "text": "Lần nào anh cũng vòng qua em. Em bắt đầu tính phí đấy.",
                "once": True,
                "effects": {
                    "story_add": {
                        "tam_quang_interest": 1,
                    },
                    "flags": ["tam_c04_w01_phone_teased_quang"],
                },
                "response_messages": [
                    {
                        "id": "r01",
                        "sender": "quang",
                        "text": "Ghi sổ đi. Cuối tháng anh thanh toán bằng trà gừng.",
                        "time": "21:12",
                    },
                ],
            },
        ],
    })
