# FILE: game/story/tam/tam_c04_between_work_and_hearts/s24_w04_month_one_snapshot.rpy
# Week 04 — Persist a non-locking Month 01 route-health snapshot.

label tam_c04_w04_s07_month_one_snapshot:
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

    if story_state.get("thienan_quang_trust", 0) >= 55 and story_state.get("quang_persistence", 0) >= 35:
        $ story_flag("tam_c04_m01_quang_thienan_progressing")
    else:
        $ story_flag("tam_c04_m01_quang_thienan_unsettled")

    if story_state.get("tam_quang_interest", 0) >= 15:
        $ story_flag("tam_c04_m01_tam_quang_awareness")
    else:
        $ story_flag("tam_c04_m01_tam_quang_familiar_only")

    if story_state.get("career_tam", 0) >= 60:
        $ story_flag("tam_c04_m01_tam_career_strong")
    elif story_state.get("career_tam", 0) >= 40:
        $ story_flag("tam_c04_m01_tam_career_steady")
    else:
        $ story_flag("tam_c04_m01_tam_career_needs_focus")

    if story_state.get("career_huyen", 0) >= 55:
        $ story_flag("tam_c04_m01_huyen_career_strong")

    $ story_flag("tam_c04_m01_snapshot_recorded")
    $ phone_refresh_all()

    return
