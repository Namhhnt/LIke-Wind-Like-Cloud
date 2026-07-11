# FILE: game/patches/time_management_tam_c04_w16.rpy
# Week 16 weekend period registration.
init 100 python:
    _periods = globals().get("INTER_CHAPTER_PERIODS")
    _mapping = globals().get("PERIOD_BY_COMPLETED_CHAPTER")
    if not isinstance(_periods, dict):
        raise Exception("time_management_tam_c04_w16.rpy: INTER_CHAPTER_PERIODS is unavailable.")
    if not isinstance(_mapping, dict):
        raise Exception("time_management_tam_c04_w16.rpy: PERIOD_BY_COMPLETED_CHAPTER is unavailable.")
    _periods["after_tam_c04_w16"] = {
        "id": "after_tam_c04_w16",
        "title": "Cuối tuần",
        "source_chapter_id": "tam_c04_w16_month_four_review",
        "duration_days": 2,
        "start_weekday_index": 5,
        "next_event_chapter_id": "tam_c04_w17_returns",
        "warning_days_remaining": [1],
        "employment_expected": False,
    }
    _mapping["tam_c04_w16_month_four_review"] = "after_tam_c04_w16"
