# FILE: game/patches/time_management_tam_c04_w07.rpy
# Week 07 weekend period registration.

init 100 python:

    _tam_c04_w07_periods = globals().get("INTER_CHAPTER_PERIODS")
    _tam_c04_w07_period_mapping = globals().get("PERIOD_BY_COMPLETED_CHAPTER")

    if not isinstance(_tam_c04_w07_periods, dict):
        raise Exception(
            "time_management_tam_c04_w07.rpy: INTER_CHAPTER_PERIODS is unavailable. "
            "Load this patch after game/time_management_data.rpy."
        )

    if not isinstance(_tam_c04_w07_period_mapping, dict):
        raise Exception(
            "time_management_tam_c04_w07.rpy: PERIOD_BY_COMPLETED_CHAPTER is unavailable. "
            "Load this patch after game/time_management_data.rpy."
        )

    _tam_c04_w07_periods["after_tam_c04_w07"] = {
        "id": "after_tam_c04_w07",
        "title": "Cuối tuần",
        "source_chapter_id": "tam_c04_w07_someone_notices_first",
        "duration_days": 2,
        "start_weekday_index": 5,
        "next_event_chapter_id": "tam_c04_w08_month_two_review",
        "warning_days_remaining": [1],
        "employment_expected": False,
    }

    _tam_c04_w07_period_mapping[
        "tam_c04_w07_someone_notices_first"
    ] = "after_tam_c04_w07"
