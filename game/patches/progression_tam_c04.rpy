# FILE: game/patches/progression_tam_c04.rpy
# Progression migration for the Chapter 04 season arc.
#
# IMPORTANT:
# progression_data.rpy creates CHAPTERS / CHAPTER_ORDER during Ren'Py init.
# This patch must run after the base progression registry exists.

init 100 python:

    _tam_c04_chapters = globals().get("CHAPTERS")
    _tam_c04_chapter_order = globals().get("CHAPTER_ORDER")

    if not isinstance(_tam_c04_chapters, dict):
        raise Exception(
            "progression_tam_c04.rpy: CHAPTERS is unavailable. "
            "Load this patch after game/progression_data.rpy."
        )

    if not isinstance(_tam_c04_chapter_order, list):
        raise Exception(
            "progression_tam_c04.rpy: CHAPTER_ORDER is unavailable or is not a list. "
            "Load this patch after game/progression_data.rpy."
        )

    _tam_c04_chapters["tam_c04_between_work_and_hearts"] = {
        "id": "tam_c04_between_work_and_hearts",
        "route": "tam",
        "type": "core",
        "timeline_position": 40,
        "title": "Những ngày lệch nhịp",
        "label": "tam_c04_between_work_and_hearts",
        "prerequisites": ["tam_c03_thienan_family"],
        "prerequisites_any": [],
        "unlocks": ["tam_c05_sunday_date"],
        "flags_set": ["tam_c04_completed"],
        "character_flags_set": {},
        "relationship_directions_set": {},
        "emotional_effects": {},
        "choice_unlocks": [],
        "exclusion_group": None,
        "excludes": [],
        "soft_hide_until_any_completed": [],
        "required_directions": {},
        "optional_conditions": [],
    }

    # Replace the old direct C03 -> Hoàng H01 transition with the C04 season arc.
    if "tam_c03_thienan_family" in _tam_c04_chapters:
        _tam_c04_c03_unlocks = list(
            _tam_c04_chapters["tam_c03_thienan_family"].get("unlocks", [])
        )
        _tam_c04_c03_unlocks = [
            _chapter_id
            for _chapter_id in _tam_c04_c03_unlocks
            if _chapter_id != "hoang_h01_brother_house"
        ]

        if "tam_c04_between_work_and_hearts" not in _tam_c04_c03_unlocks:
            _tam_c04_c03_unlocks.append("tam_c04_between_work_and_hearts")

        _tam_c04_chapters["tam_c03_thienan_family"]["unlocks"] = _tam_c04_c03_unlocks

    # Insert C04 directly after C03 without duplicating it on reload.
    if "tam_c04_between_work_and_hearts" not in _tam_c04_chapter_order:
        try:
            _tam_c04_c03_index = _tam_c04_chapter_order.index(
                "tam_c03_thienan_family"
            )
            _tam_c04_chapter_order.insert(
                _tam_c04_c03_index + 1,
                "tam_c04_between_work_and_hearts",
            )
        except ValueError:
            _tam_c04_chapter_order.append("tam_c04_between_work_and_hearts")
