init -2 python:
    DEFAULT_ROUTE_ID = "tam"

    ROUTE_ORDER = [
        "tam",
        "hoang",
        "yuuka",
        "minh",
    ]

    ROUTES = {
        "tam": {
            "id": "tam",
            "title": "Tam",
            "entry_chapter": "tam_c01",
            "default_unlocked": True,
        },
        "hoang": {
            "id": "hoang",
            "title": "Hoang",
            "entry_chapter": None,
            "default_unlocked": False,
        },
        "yuuka": {
            "id": "yuuka",
            "title": "Yuuka",
            "entry_chapter": None,
            "default_unlocked": False,
        },
        "minh": {
            "id": "minh",
            "title": "Minh",
            "entry_chapter": None,
            "default_unlocked": False,
        },
    }

    CHAPTER_ORDER = [
        "tam_c01",
        "tam_c02",
        "tam_c03",
    ]

    CHAPTERS = {
        "tam_c01": {
            "id": "tam_c01",
            "route": "tam",
            "type": "core",
            "timeline_position": 10,
            "title": "First Morning",
            "status": "locked",
            "label": "tam_c01",
            "prerequisites": [],
            "optional_conditions": [],
            "unlocks": ["tam_c02"],
            "excludes": [],
            "flags_set": ["tam_intro_seen"],
            "emotional_effects": {},
            "choice_unlocks": [],
        },
        "tam_c02": {
            "id": "tam_c02",
            "route": "tam",
            "type": "core",
            "timeline_position": 20,
            "title": "Riverside Conversation",
            "status": "locked",
            "label": "tam_c02",
            "prerequisites": ["tam_c01"],
            "optional_conditions": [],
            "unlocks": ["tam_c03"],
            "excludes": [],
            "flags_set": ["tam_riverside_seen"],
            "emotional_effects": {},
            "choice_unlocks": [],
        },
        "tam_c03": {
            "id": "tam_c03",
            "route": "tam",
            "type": "core",
            "timeline_position": 30,
            "title": "Lingering Promise",
            "status": "locked",
            "label": "tam_c03",
            "prerequisites": ["tam_c02"],
            "optional_conditions": [],
            "unlocks": [],
            "excludes": [],
            "flags_set": ["tam_route_phase_one_complete"],
            "emotional_effects": {},
            "choice_unlocks": [],
        },
    }
