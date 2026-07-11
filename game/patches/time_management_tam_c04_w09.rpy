# FILE: game/patches/time_management_tam_c04_w09.rpy
# Week 09 weekend period registration.
init 100 python:
    _periods = globals().get("INTER_CHAPTER_PERIODS")
    _mapping = globals().get("PERIOD_BY_COMPLETED_CHAPTER")
    if not isinstance(_periods, dict):
        raise Exception("time_management_tam_c04_w09.rpy: INTER_CHAPTER_PERIODS is unavailable.")
    if not isinstance(_mapping, dict):
        raise Exception("time_management_tam_c04_w09.rpy: PERIOD_BY_COMPLETED_CHAPTER is unavailable.")
    _periods["after_tam_c04_w09"] = {
        "id": "after_tam_c04_w09",
        "title": "Cuối tuần",
        "source_chapter_id": "tam_c04_w09_named_gaps",
        "duration_days": 2,
        "start_weekday_index": 5,
        "next_event_chapter_id": "tam_c04_w10_no_one_stands_in",
        "warning_days_remaining": [1],
        "employment_expected": False,
    }
    _mapping["tam_c04_w09_named_gaps"] = "after_tam_c04_w09"
