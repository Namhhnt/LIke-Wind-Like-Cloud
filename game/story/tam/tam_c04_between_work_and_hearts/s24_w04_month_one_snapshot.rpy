# FILE: game/story/tam/tam_c04_between_work_and_hearts/s24_w04_month_one_snapshot.rpy
# Week 04 — Persist a non-locking Month 01 route-health snapshot.

label tam_c04_w04_s07_month_one_snapshot:
    $ tam_c04_ensure_extended_story_state()

    # These flags are historical snapshots. They do not lock routes and are not
    # cleared later; Month 02 can compare against them to show movement.

    if story_state.get("tam_hoang_interest", 0) >= 65 and story_state.get("hoang_tam_trust", 0) >= 55:
        $ story_flag("tam_c04_m01_hoang_strong")
    elif story_state.get("tam_hoang_interest", 0) >= 45:
        $ story_flag("tam_c04_m01_hoang_warm")
    else:
        $ story_flag("tam_c04_m01_hoang_quiet")

    if story_state.get("huyen_quan_trust", 0) >= 35:
        $ story_flag("tam_c04_m01_huyen_quan_progressing")
    elif story_state.get("huyen_quan_trust", 0) >= 20:
        $ story_flag("tam_c04_m01_huyen_quan_resisting_but_learning")
    else:
        $ story_flag("tam_c04_m01_huyen_quan_distant")

    if story_state.get("huyen_quan_interest", 0) >= 8:
        $ story_flag("tam_c04_m01_huyen_quan_personal_seed")

    if (
        story_state.get("thienan_quang_trust", 0) >= 55
        and story_state.get("quang_thienan_resolve", 0) >= 55
    ):
        $ story_flag("tam_c04_m01_quang_thienan_progressing")
        $ story_add_direction("quang", "quang_thienan_open")
        $ story_add_direction("thienan", "thienan_quang_open")
    else:
        $ story_flag("tam_c04_m01_quang_thienan_unsettled")

    if (
        story_state.get("tam_quang_interest", 0) >= 15
        and story_state.get("quang_tam_awareness", 0) >= 10
        and story_state.get("quang_tam_warmth", 0) >= 45
    ):
        $ story_flag("tam_c04_m01_tam_quang_awareness")
        $ story_flag("tam_c04_m01_quang_tam_personal_seed")
        $ story_add_direction("quang", "quang_tam_open")
    elif story_state.get("tam_quang_interest", 0) >= 8:
        $ story_flag("tam_c04_m01_tam_quang_uncertain_shift")
    else:
        $ story_flag("tam_c04_m01_tam_quang_familiar_only")

    if (
        story_has_flag("tam_c04_m01_quang_thienan_progressing")
        and story_has_flag("tam_c04_m01_quang_tam_personal_seed")
    ):
        $ story_flag("tam_c04_m01_quang_crosscurrent")

    # Career score may reset after a promotion. Route health therefore uses
    # progress earned since C04 began: level gains * 100 + remaining score delta.
    $ _tam_c04_m01_career_tam_progress = career_bonus_get_progress_since_chapter_start("tam_c04_between_work_and_hearts", "tam")
    $ _tam_c04_m01_career_huyen_progress = career_bonus_get_progress_since_chapter_start("tam_c04_between_work_and_hearts", "huyen")

    if _tam_c04_m01_career_tam_progress >= 60:
        $ story_flag("tam_c04_m01_tam_career_strong")
    elif _tam_c04_m01_career_tam_progress >= 40:
        $ story_flag("tam_c04_m01_tam_career_steady")
    else:
        $ story_flag("tam_c04_m01_tam_career_needs_focus")

    if _tam_c04_m01_career_huyen_progress >= 40:
        $ story_flag("tam_c04_m01_huyen_career_strong")

    $ story_flag("tam_c04_m01_snapshot_recorded")
    $ phone_refresh_all()

    return
