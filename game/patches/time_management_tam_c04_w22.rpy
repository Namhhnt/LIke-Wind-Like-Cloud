# FILE: game/patches/time_management_tam_c04_w22.rpy
# Week 22 weekend period registration.
init 100 python:
    _periods = globals().get("INTER_CHAPTER_PERIODS")
    _mapping = globals().get("PERIOD_BY_COMPLETED_CHAPTER")
    if not isinstance(_periods, dict):
        raise Exception("time_management_tam_c04_w22.rpy: INTER_CHAPTER_PERIODS is unavailable.")
    if not isinstance(_mapping, dict):
        raise Exception("time_management_tam_c04_w22.rpy: PERIOD_BY_COMPLETED_CHAPTER is unavailable.")
    _periods["after_tam_c04_w22"] = {
        "id": "after_tam_c04_w22",
        "title": "Cuối tuần",
        "source_chapter_id": "tam_c04_w22_when_work_interrupts",
        "duration_days": 2,
        "start_weekday_index": 5,
        "next_event_chapter_id": "tam_c04_w23_new_balance",
        "warning_days_remaining": [1],
        "employment_expected": False,
    }
    _mapping["tam_c04_w22_when_work_interrupts"] = "after_tam_c04_w22"
