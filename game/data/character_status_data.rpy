init -5 python:

    CHARACTER_STATUS_BASE = {
        "tam": {
            "id": "tam",
            "name": "Tam",
            "profile_id": "tam",
            "public_title": "New Office Staff",
            "default_notes": [
                "Recently passed the interview.",
                "Still adjusting to the company environment.",
            ],
            "hidden_until": [],
        },
        "hoang": {
            "id": "hoang",
            "name": "Hoang",
            "profile_id": "hoang",
            "public_title": "Architecture Designer",
            "default_notes": [
                "Polite, observant, and more guarded than he first appears.",
            ],
            "hidden_until": ["completed:tam_c02_company_party"],
        },
        "huyen": {
            "id": "huyen",
            "name": "Huyen",
            "profile_id": "huyen",
            "public_title": "Close Friend",
            "default_notes": [
                "Socially quick, frank, and rarely careless with what she notices.",
            ],
            "hidden_until": ["completed:tam_c01_interview_day"],
        },
        "minh": {
            "id": "minh",
            "name": "Minh",
            "profile_id": "minh",
            "public_title": "Senior Advisor",
            "default_notes": [
                "Professional presence with a way of making pressure feel precise.",
            ],
            "hidden_until": ["completed:tam_c06_minh_returns"],
        },
        "yuuka": {
            "id": "yuuka",
            "name": "Yuuka",
            "profile_id": "yuuka",
            "public_title": "Festival Visitor",
            "default_notes": [
                "Elegant from a distance and difficult to read on purpose.",
            ],
            "hidden_until": ["completed:yuuka_c08_festival_arrival"],
        },
        "thienan": {
            "id": "thienan",
            "name": "Thien An",
            "profile_id": "thienan",
            "public_title": "Elder Sister",
            "default_notes": [
                "Reliable enough to sound calm even when carrying too much.",
            ],
            "hidden_until": ["completed:tam_c03_thienan_family"],
        },
    }

    STORY_ITEMS = {
        "tam_first_salary_envelope": {
            "id": "tam_first_salary_envelope",
            "name": "First Salary Envelope",
            "description": "Tam's first salary. Still unopened for longer than necessary.",
            "type": "keepsake",
            "visible": True,
        },
        "yuuka_old_bookmark": {
            "id": "yuuka_old_bookmark",
            "name": "Folded Bookmark",
            "description": "A bookmark with one corner folded too neatly.",
            "type": "memory",
            "visible": False,
        },
    }
