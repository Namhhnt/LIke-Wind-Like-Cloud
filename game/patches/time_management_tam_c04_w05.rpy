# FILE: game/patches/time_management_tam_c04_w05.rpy
# Week 05 weekend period registration.

init 100 python:

    _tam_c04_w05_periods = globals().get("INTER_CHAPTER_PERIODS")
    _tam_c04_w05_period_mapping = globals().get("PERIOD_BY_COMPLETED_CHAPTER")

    if not isinstance(_tam_c04_w05_periods, dict):
        raise Exception(
            "time_management_tam_c04_w05.rpy: INTER_CHAPTER_PERIODS is unavailable. "
            "Load this patch after game/time_management_data.rpy."
        )

    if not isinstance(_tam_c04_w05_period_mapping, dict):
        raise Exception(
            "time_management_tam_c04_w05.rpy: PERIOD_BY_COMPLETED_CHAPTER is unavailable. "
            "Load this patch after game/time_management_data.rpy."
        )

    _tam_c04_w05_periods["after_tam_c04_w05"] = {
        "id": "after_tam_c04_w05",
        "title": "Cuối tuần",
        "source_chapter_id": "tam_c04_w05_new_month",
        "duration_days": 2,
        "start_weekday_index": 5,
        "next_event_chapter_id": "tam_c04_w06_the_empty_chair",
        "warning_days_remaining": [1],
        "employment_expected": False,
    }

    _tam_c04_w05_period_mapping[
        "tam_c04_w05_new_month"
    ] = "after_tam_c04_w05"
