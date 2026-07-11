# FILE: game/story/tam/tam_c04_between_work_and_hearts/s50_w08_month_two_snapshot.rpy
# Week 08 — Persist a non-locking Month 02 route-health snapshot.

label tam_c04_w08_s07_month_two_snapshot:
    $ tam_c04_ensure_extended_story_state()

    if story_state.get("tam_hoang_interest", 0) >= 75 and story_state.get("hoang_tam_trust", 0) >= 70:
        $ story_flag("tam_c04_m02_hoang_deepening")
    elif story_state.get("tam_hoang_interest", 0) >= 55:
        $ story_flag("tam_c04_m02_hoang_holding")
    else:
        $ story_flag("tam_c04_m02_hoang_drifting")

    if (
        story_state.get("huyen_quan_trust", 0) >= 55
        and story_state.get("huyen_quan_interest", 0) >= 15
    ):
        $ story_flag("tam_c04_m02_huyen_quan_personal_progress")
    elif story_state.get("huyen_quan_trust", 0) >= 40:
        $ story_flag("tam_c04_m02_huyen_quan_work_familiarity")
    else:
        $ story_flag("tam_c04_m02_huyen_quan_unsettled")

    if (
        story_state.get("thienan_quang_trust", 0) >= 70
        and story_state.get("quang_thienan_resolve", 0) >= 70
    ):
        $ story_flag("tam_c04_m02_quang_thienan_direct")
        $ story_add_direction("quang", "quang_thienan_open")
        $ story_add_direction("thienan", "thienan_quang_open")
    elif story_state.get("thienan_quang_trust", 0) >= 50:
        $ story_flag("tam_c04_m02_quang_thienan_holding")
    else:
        $ story_flag("tam_c04_m02_quang_thienan_distant")

    if (
        story_state.get("tam_quang_interest", 0) >= 25
        and story_state.get("quang_tam_awareness", 0) >= 20
        and story_state.get("quang_tam_warmth", 0) >= 55
    ):
        $ story_flag("tam_c04_m02_tam_quang_personal_progress")
        $ story_add_direction("quang", "quang_tam_open")
    elif story_state.get("tam_quang_interest", 0) >= 15:
        $ story_flag("tam_c04_m02_tam_quang_unanswered")
    else:
        $ story_flag("tam_c04_m02_tam_quang_familiar_only")

    if (
        story_has_flag("tam_c04_m02_quang_thienan_direct")
        and story_has_flag("tam_c04_m02_tam_quang_personal_progress")
    ):
        $ story_flag("tam_c04_m02_quang_crosscurrent_stronger")
    elif (
        story_has_flag("tam_c04_m02_quang_thienan_holding")
        and story_has_flag("tam_c04_m02_tam_quang_unanswered")
    ):
        $ story_flag("tam_c04_m02_quang_crosscurrent_unresolved")

    $ _tam_c04_m02_career_tam_progress = career_bonus_get_progress_since_chapter_start("tam_c04_between_work_and_hearts", "tam")
    $ _tam_c04_m02_career_huyen_progress = career_bonus_get_progress_since_chapter_start("tam_c04_between_work_and_hearts", "huyen")

    if _tam_c04_m02_career_tam_progress >= 150:
        $ story_flag("tam_c04_m02_tam_career_accelerating")
    elif _tam_c04_m02_career_tam_progress >= 100:
        $ story_flag("tam_c04_m02_tam_career_level_ready")
    elif _tam_c04_m02_career_tam_progress >= 70:
        $ story_flag("tam_c04_m02_tam_career_steady")
    else:
        $ story_flag("tam_c04_m02_tam_career_needs_focus")

    if _tam_c04_m02_career_huyen_progress >= 130:
        $ story_flag("tam_c04_m02_huyen_career_accelerating")
    elif _tam_c04_m02_career_huyen_progress >= 90:
        $ story_flag("tam_c04_m02_huyen_career_level_ready")
    else:
        $ story_flag("tam_c04_m02_huyen_career_steady")

    $ story_flag("tam_c04_m02_snapshot_recorded")
    $ phone_refresh_all()

    return
