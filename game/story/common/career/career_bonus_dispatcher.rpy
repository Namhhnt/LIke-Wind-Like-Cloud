# FILE: game/story/common/career/career_bonus_dispatcher.rpy
# Shared career promotion dispatcher. Reusable from any chapter.

label career_bonus_process_checkpoint(checkpoint_id, character_ids=None):
    $ career_bonus_scan_checkpoint(checkpoint_id, character_ids)

    while career_bonus_queue:
        $ career_bonus_current = career_bonus_queue.pop(0)
        $ _career_bonus_label = career_bonus_current.get("label")

        if _career_bonus_label and renpy.has_label(_career_bonus_label):
            call expression _career_bonus_label
        else:
            call career_bonus_generic_promotion

        $ career_bonus_finalize_current()
        $ career_bonus_current = None

    return


# Compatibility entry points for code that previously called one generic scene
# per character. They now dispatch by target level.
label career_bonus_tam_promotion:
    $ _career_bonus_level = int(career_bonus_current.get("target_level", 0) or 0)
    $ _career_bonus_specific = CAREER_BONUS_SCENE_LABELS.get("tam", {}).get(_career_bonus_level)

    if _career_bonus_specific and renpy.has_label(_career_bonus_specific):
        call expression _career_bonus_specific
    else:
        call career_bonus_generic_promotion
    return


label career_bonus_huyen_promotion:
    $ _career_bonus_level = int(career_bonus_current.get("target_level", 0) or 0)
    $ _career_bonus_specific = CAREER_BONUS_SCENE_LABELS.get("huyen", {}).get(_career_bonus_level)

    if _career_bonus_specific and renpy.has_label(_career_bonus_specific):
        call expression _career_bonus_specific
    else:
        call career_bonus_generic_promotion
    return


label career_bonus_generic_promotion:
    scene bg_meeting_room_day
    with dissolve

    $ _career_bonus_character = career_bonus_current.get("character_id")
    $ _career_bonus_title = career_bonus_current.get("title") or "vị trí mới"
    $ _career_bonus_salary = int(career_bonus_current.get("salary", 0) or 0)
    $ _career_bonus_salary_text = career_bonus_format_salary(_career_bonus_salary)

    "Cuối buổi, Quân đặt một quyết định đã ký lên bàn."

    if _career_bonus_character == "tam":
        quan neutral "Từ kỳ tới, chức danh của em được cập nhật thành [_career_bonus_title]."
        if _career_bonus_salary > 0:
            quan neutral "Mức lương mới là [_career_bonus_salary_text]."
        tam neutral "Vâng. Em sẽ xem kỹ phạm vi công việc."
    elif _career_bonus_character == "huyen":
        quan neutral "Từ kỳ tới, chức danh của em được cập nhật thành [_career_bonus_title]."
        if _career_bonus_salary > 0:
            quan neutral "Mức lương mới là [_career_bonus_salary_text]."
        huyen neutral "Em nghe rõ rồi ạ. Chỉ là hơi chưa quen với phần không bị sửa."
    else:
        "Quyết định có hiệu lực từ kỳ làm việc tiếp theo."

    return
