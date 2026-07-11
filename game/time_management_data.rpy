init -5 python:

    WEEKDAY_NAMES = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    DEFAULT_PERIOD_DURATION_DAYS = 14
    DEFAULT_EVENT_SPAN_DAYS = 1

    CHAPTER_TIME_METADATA = {
        "prologue_rain_dream": {
            "event_span_days": 0,
            "free_duration_days": 0,
            "is_flashback": False,
            "skip_behavior": "none",
        },
        "tam_c01_interview_day": {
            "event_span_days": 1,
            "free_duration_days": 7,
            "is_flashback": False,
            "skip_behavior": "next_chapter_only",
        },
        "tam_c02_company_party": {
            "event_span_days": 21,
            "free_duration_days": 7,
            "is_flashback": False,
            "skip_behavior": "next_chapter_only",
        },
        "tam_c03_thienan_family": {
            "event_span_days": 7,
            "free_duration_days": 30,
            "is_flashback": False,
            "skip_behavior": "pick_any_day",
        },
    }

    INTER_CHAPTER_PERIODS = {
        "after_tam_c01": {
            "id": "after_tam_c01",
            "start_after": "tam_c01_interview_day",
            "next_event": "tam_c02_company_party",
            "duration_days": 7,
            "force_trigger": True,
            "allow_skip_to_any_day": False,
            "warning_days": [3, 1],
            "allowed_main_actions": ["library_study_work_skill", "sleep_8h_home"],
            "important_interactions": ["visit_huyen_after_first_job"],
            "player_is_employed": False,
        },
        "after_tam_c02": {
            "id": "after_tam_c02",
            "start_after": "tam_c02_company_party",
            "next_event": "tam_c03_thienan_family",
            "duration_days": 7,
            "force_trigger": True,
            "allow_skip_to_any_day": False,
            "warning_days": [7, 3, 1],
            "important_interactions": [
                "visit_huyen_after_company_party",
                "visit_hoang_house_casual_followup",
            ],
            "player_is_employed": True,
        },
        "after_tam_c03": {
            "id": "after_tam_c03",
            "start_after": "tam_c03_thienan_family",
            "next_event": "hoang_h01_brother_house",
            "duration_days": 30,
            "force_trigger": True,
            "allow_skip_to_any_day": True,
            "warning_days": [14, 7, 3, 1],
            "important_interactions": [],
            "player_is_employed": True,
        },
    }

    PERIOD_BY_COMPLETED_CHAPTER = {
        period["start_after"]: period_id
        for period_id, period in INTER_CHAPTER_PERIODS.items()
    }


init -1 python:

    def chapter_time_metadata(chapter_id):
        metadata = {
            "event_span_days": DEFAULT_EVENT_SPAN_DAYS,
            "free_duration_days": DEFAULT_PERIOD_DURATION_DAYS,
            "is_flashback": False,
            "skip_behavior": "pick_any_day",
        }
        metadata.update(CHAPTER_TIME_METADATA.get(chapter_id, {}))
        return metadata


    def normalize_chapter_time_metadata():
        chapters = globals().get("CHAPTERS", {})
        for chapter_id, chapter in chapters.items():
            metadata = chapter_time_metadata(chapter_id)
            chapter.setdefault("event_span_days", metadata["event_span_days"])
            chapter.setdefault("free_duration_days", metadata["free_duration_days"])
            chapter.setdefault("is_flashback", metadata["is_flashback"])
            chapter.setdefault("skip_behavior", metadata["skip_behavior"])


    normalize_chapter_time_metadata()
