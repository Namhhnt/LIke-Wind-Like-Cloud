# FILE: game/patches/time_management_tam_c04_w02.rpy
# Week 02 weekend period registration.
#
# This is intentionally a fresh period definition. Cloning a previous period can
# carry stale absolute date fields into the new checkpoint and rewind the map
# calendar.

init 100 python:

    _tam_c04_w02_periods = globals().get("INTER_CHAPTER_PERIODS")
    _tam_c04_w02_period_mapping = globals().get("PERIOD_BY_COMPLETED_CHAPTER")

    if not isinstance(_tam_c04_w02_periods, dict):
        raise Exception(
            "time_management_tam_c04_w02.rpy: INTER_CHAPTER_PERIODS is unavailable. "
            "Load this patch after game/time_management_data.rpy."
        )

    if not isinstance(_tam_c04_w02_period_mapping, dict):
        raise Exception(
            "time_management_tam_c04_w02.rpy: PERIOD_BY_COMPLETED_CHAPTER is unavailable. "
            "Load this patch after game/time_management_data.rpy."
        )

    _tam_c04_w02_periods["after_tam_c04_w02"] = {
        "id": "after_tam_c04_w02",
        "title": "Cuối tuần",
        "source_chapter_id": "tam_c04_w02_first_priorities",
        "duration_days": 2,
        "start_weekday_index": 5,
        "next_event_chapter_id": "tam_c04_w03_pressure_and_distance",
        "warning_days_remaining": [1],
        "employment_expected": False,
    }

    _tam_c04_w02_period_mapping[
        "tam_c04_w02_first_priorities"
    ] = "after_tam_c04_w02"
