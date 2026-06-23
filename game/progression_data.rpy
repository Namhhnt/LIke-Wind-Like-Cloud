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
            "entry_chapter": "hoang_h01",
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
        "hoang_h01",
        "hoang_bonus_restraint",
        "hoang_bonus_confession",
        "tam_c03",
        "hoang_h02",
    ]

    CHAPTERS = {
        "tam_c01": {
            "id": "tam_c01",
            "route": "tam",
            "type": "core",
            "timeline_position": 10,
            "title": "Ngay Dau Tien Gio Doi Chieu",
            "status": "locked",
            "label": "tam_c01",
            "prerequisites": [],
            "optional_conditions": [],
            "unlocks": ["tam_c02"],
            "excludes": [],
            "flags_set": ["tam_route_started", "canon_interview_day", "canon_dinner_corner_man", "canon_year_end_first_meeting"],
            "emotional_effects": {},
            "choice_unlocks": [],
        },
        "tam_c02": {
            "id": "tam_c02",
            "route": "tam",
            "type": "core",
            "timeline_position": 20,
            "title": "The Company Gathering",
            "status": "locked",
            "label": "tam_c02",
            "prerequisites": ["tam_c01"],
            "optional_conditions": [],
            "unlocks": ["hoang_h01"],
            "excludes": [],
            "flags_set": ["tam_company_gathering_seen", "quan_team_pressure_introduced"],
            "emotional_effects": {},
            "choice_unlocks": [],
        },
        "hoang_h01": {
            "id": "hoang_h01",
            "route": "hoang",
            "type": "pov",
            "timeline_position": 25,
            "title": "Hoang's Restraint",
            "status": "locked",
            "label": "hoang_h01",
            "prerequisites": ["tam_c02"],
            "optional_conditions": [],
            "unlocks": ["hoang_bonus_restraint", "hoang_bonus_confession"],
            "excludes": [],
            "flags_set": ["hoang_restraint_seen"],
            "character_flags_set": {
                "hoang": ["knows_tam_is_hesitating"],
            },
            "emotional_effects": {},
            "choice_unlocks": [],
        },
        "hoang_bonus_restraint": {
            "id": "hoang_bonus_restraint",
            "route": "hoang",
            "type": "bonus",
            "timeline_position": 27,
            "title": "Quiet Restraint",
            "status": "locked",
            "label": "hoang_bonus_restraint",
            "prerequisites": ["hoang_h01"],
            "optional_conditions": [],
            "unlocks": ["tam_c03", "hoang_h02"],
            "excludes": ["hoang_bonus_confession"],
            "exclusion_group": "hoang_direction_01",
            "flags_set": ["hoang_bonus_restraint_seen"],
            "character_flags_set": {
                "hoang": ["leans_restraint"],
            },
            "relationship_directions_set": {
                "hoang": ["restraint"],
            },
            "emotional_effects": {
                "distance": -1,
                "trust": 1,
            },
            "choice_unlocks": ["ask_gently"],
        },
        "hoang_bonus_confession": {
            "id": "hoang_bonus_confession",
            "route": "hoang",
            "type": "bonus",
            "timeline_position": 28,
            "title": "Sudden Confession",
            "status": "locked",
            "label": "hoang_bonus_confession",
            "prerequisites": ["hoang_h01"],
            "optional_conditions": [],
            "unlocks": ["tam_c03", "hoang_h02"],
            "excludes": ["hoang_bonus_restraint"],
            "exclusion_group": "hoang_direction_01",
            "flags_set": ["hoang_bonus_confession_seen"],
            "character_flags_set": {
                "hoang": ["leans_confession"],
            },
            "relationship_directions_set": {
                "hoang": ["confession"],
            },
            "emotional_effects": {
                "distance": 1,
                "trust": 2,
                "misunderstanding": 1,
            },
            "choice_unlocks": ["choose_direct_affection"],
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
            "required_directions": {
                "hoang": ["restraint", "confession"],
            },
            "optional_conditions": [],
            "unlocks": [],
            "excludes": [],
            "flags_set": ["tam_route_phase_one_complete"],
            "emotional_effects": {},
            "choice_unlocks": [],
        },
        "hoang_h02": {
            "id": "hoang_h02",
            "route": "hoang",
            "type": "core",
            "timeline_position": 35,
            "title": "Shared Silence",
            "status": "locked",
            "label": "hoang_h02",
            "prerequisites": ["hoang_h01", "tam_c03"],
            "soft_hide_until_any_completed": ["hoang_bonus_restraint", "hoang_bonus_confession"],
            "optional_conditions": [],
            "unlocks": [],
            "excludes": [],
            "flags_set": ["hoang_route_phase_two_complete"],
            "emotional_effects": {},
            "choice_unlocks": [],
        },
    }

    CHOICE_DEFINITIONS = {
        "ask_gently": {
            "label": "Ask gently",
            "type": "conditional",
            "conditions": ["direction_hoang_restraint"],
        },
        "choose_direct_affection": {
            "label": "Choose direct affection",
            "type": "directional",
            "conditions": ["direction_hoang_confession"],
        },
        "notice_subtle_reaction": {
            "label": "Notice the subtle reaction",
            "type": "insight",
            "conditions": ["flag_player_knows_hoang_restraint"],
        },
    }

    ENDING_RULES = {
        "ending_restraint": {
            "title": "Quiet Restraint",
            "requires_completed": ["hoang_h02"],
            "requires_directions_any": {
                "hoang": ["restraint"],
            },
            "emotional_max": {
                "misunderstanding": 1,
            },
        },
        "ending_confession": {
            "title": "Sudden Confession",
            "requires_completed": ["hoang_h02"],
            "requires_directions_any": {
                "hoang": ["confession"],
            },
        },
        "ending_shared_silence": {
            "title": "Shared Silence",
            "requires_completed": ["hoang_h02"],
            "emotional_min": {
                "trust": 3,
            },
            "emotional_max": {
                "distance": 0,
            },
        },
        "ending_focus_hoang": {
            "title": "Hoang Focus",
            "requires_completed": ["hoang_h02"],
            "route_focus_greater": ["hoang", "tam"],
        },
        "ending_true_convergence": {
            "title": "True Convergence",
            "requires_completed": ["hoang_h02"],
            "emotional_min": {
                "trust": 3,
            },
            "emotional_max": {
                "distance": 0,
            },
            "persistent_endings_all": ["ending_restraint", "ending_confession"],
        },
    }
