init -5 python:

    def career_level(level, title, salary, required_flags=None, required_scores=None, required_max_scores=None, required_completed_chapters=None):
        return {
            "level": level,
            "title": title,
            "salary": int(salary),
            "required_flags": list(required_flags or []),
            "required_scores": dict(required_scores or {}),
            "required_max_scores": dict(required_max_scores or {}),
            "required_completed_chapters": list(required_completed_chapters or []),
        }

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

    CHARACTER_CAREER_TRACKS = {
        "tam": {
            "score_key": "career_tam",
            "sync_activity_salary": True,
            "levels": [
                career_level(1, "Junior Staff I", 12000000),
                career_level(2, "Junior Staff II", 14000000),
                career_level(3, "Junior Staff III", 16000000),
                career_level(4, "Senior Staff I", 19000000),
                career_level(5, "Senior Staff II", 22000000),
                career_level(6, "Senior Staff III", 25000000),
                career_level(7, "Lead Staff", 30000000, ["career_tam_lead_track_unlocked"], {"tam_observation": 45}),
                career_level(8, "Team Manager", 36000000, ["career_tam_management_track_unlocked"], {"tam_self_clarity": 55}),
                career_level(9, "Department Director", 45000000, ["career_tam_director_track_unlocked"], {"tam_respect_yuuka": 30}, None, ["work_c10_project_festival_overlap"]),
            ],
            "salary_flag_overrides": {
                "tam_perfect_interview": {
                    1: 15000000,
                    2: 17000000,
                    3: 19000000,
                    4: 22000000,
                    5: 25000000,
                    6: 28000000,
                    7: 33000000,
                    8: 39000000,
                    9: 48000000,
                },
            },
        },
        "huyen": {
            "score_key": "career_huyen",
            "levels": [
                career_level(1, "Junior Staff I", 12000000),
                career_level(2, "Junior Staff II", 13500000),
                career_level(3, "Junior Staff III", 15000000),
                career_level(4, "Senior Staff I", 17500000),
                career_level(5, "Senior Staff II", 20000000),
                career_level(6, "Senior Staff III", 23000000),
                career_level(7, "Lead Staff", 27000000, ["career_huyen_lead_track_unlocked"], {"huyen_quan_trust": 20}),
                career_level(8, "Team Manager", 32000000, ["career_huyen_management_track_unlocked"], {"huyen_hoang_interest": 20}),
                career_level(9, "Department Director", 39000000, ["career_huyen_director_track_unlocked"], {"career_huyen": 100}),
            ],
        },
        "hoang": {
            "score_key": "career_hoang",
            "levels": [
                career_level(1, "Junior Designer I", 14000000),
                career_level(2, "Junior Designer II", 16000000),
                career_level(3, "Junior Designer III", 18000000),
                career_level(4, "Senior Designer I", 21000000),
                career_level(5, "Senior Designer II", 24000000),
                career_level(6, "Senior Designer III", 27000000),
                career_level(7, "Lead Architect", 32000000, ["career_hoang_lead_track_unlocked"], {"hoang_professional_credit": 50}),
                career_level(8, "Principal Architect", 48000000, ["career_hoang_management_track_unlocked"], {"hoang_self_acceptance": 45}),
                career_level(9, "Design Director", 60000000, ["career_hoang_director_track_unlocked"], {"hoang_tam_trust": 45}),
            ],
        },
        "minh": {
            "score_key": "career_minh",
            "levels": [
                career_level(1, "Junior Advisor I", 180000000),
                career_level(2, "Junior Advisor II", 205000000),
                career_level(3, "Junior Advisor III", 230000000),
                career_level(4, "Senior Advisor I", 260000000),
                career_level(5, "Senior Advisor II", 295000000),
                career_level(6, "Senior Advisor III", 330000000),
                career_level(7, "Lead Consultant", 390000000, ["career_minh_lead_track_unlocked"], {"minh_yuuka_trust": 25}),
                career_level(8, "Strategy Manager", 450000000, ["career_minh_management_track_unlocked"], None, {"boundary_score": 40}),
                career_level(9, "Executive Advisor", 550000000, ["career_minh_director_track_unlocked"], {"romantic_score": 20}),
            ],
            "salary_flag_overrides": {
                "minh_alex_shadow": {
                    1: 215000000,
                    2: 317000000,
                    3: 419000000,
                    4: 522000000,
                    5: 625000000,
                    6: 728000000,
                    7: 833000000,
                    8: 939000000,
                    9: 1480000000,
                },
            },
        },
        "yuuka": {
            "score_key": "career_yuuka",
            "levels": [
                career_level(1, "Junior Producer I", 70000000),
                career_level(2, "Junior Producer II", 95000000),
                career_level(3, "Junior Producer III", 120000000),
                career_level(4, "Senior Producer I", 250000000),
                career_level(5, "Senior Producer II", 285000000),
                career_level(6, "Senior Producer III", 320000000),
                career_level(7, "Lead Producer", 380000000, ["career_yuuka_lead_track_unlocked"], {"minh_yuuka_intimacy": 20}),
                career_level(8, "Creative Director", 450000000, ["career_yuuka_management_track_unlocked"], {"old_friend_score": 20}),
                career_level(9, "Studio Director", 540000000, ["career_yuuka_director_track_unlocked"], {"still_lover_score": 15}),
            ],
            "salary_flag_overrides": {
                "yuuka_superstar": {
                    1: 75000000,
                    2: 117000000,
                    3: 139000000,
                    4: 202000000,
                    5: 245000000,
                    6: 328000000,
                    7: 493000000,
                    8: 539000000,
                    9: 680000000,
                },
            },
        },
        "thienan": {
            "score_key": "career_thienan",
            "levels": [
                career_level(1, "Junior Coordinator I", 13000000),
                career_level(2, "Junior Coordinator II", 15000000),
                career_level(3, "Junior Coordinator III", 18000000),
                career_level(4, "Senior Coordinator I", 25000000),
                career_level(5, "Senior Coordinator II", 30000000),
                career_level(6, "Senior Coordinator III", 40000000),
                career_level(7, "Lead Coordinator", 50000000, ["career_thienan_lead_track_unlocked"], {"thienan_self_assertion": 45}),
                career_level(8, "Operations Manager", 64000000, ["career_thienan_management_track_unlocked"], {"thienan_quang_trust": 45}),
                career_level(9, "Operations Director", 80000000, ["career_thienan_director_track_unlocked"], None, {"family_pressure_thienan": 35}),
            ],
        },
    }

    CAREER_SCORE_TO_CHARACTER = {}
    for career_character_id, career_track in CHARACTER_CAREER_TRACKS.items():
        CAREER_SCORE_TO_CHARACTER[career_track.get("score_key")] = career_character_id
