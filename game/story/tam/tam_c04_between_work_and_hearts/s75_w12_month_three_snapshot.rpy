label tam_c04_w12_s07_month_three_snapshot:
    $ tam_c04_ensure_extended_story_state()

    if story_state.get("tam_hoang_interest", 0) >= 85 and story_state.get("hoang_tam_trust", 0) >= 80:
        $ story_flag("tam_c04_m03_hoang_mutual_habit")
    elif story_state.get("tam_hoang_interest", 0) >= 65 and story_state.get("hoang_tam_trust", 0) >= 60:
        $ story_flag("tam_c04_m03_hoang_needs_clarity")
    else:
        $ story_flag("tam_c04_m03_hoang_steps_back")

    if story_state.get("huyen_quan_trust", 0) >= 70 and story_state.get("huyen_quan_interest", 0) >= 25:
        $ story_flag("tam_c04_m03_huyen_quan_mutual_notice")
    elif story_state.get("huyen_quan_trust", 0) >= 50:
        $ story_flag("tam_c04_m03_huyen_quan_reliable_pair")
    else:
        $ story_flag("tam_c04_m03_huyen_quan_professional_only")

    if story_state.get("thienan_quang_trust", 0) >= 80 and story_state.get("quang_thienan_resolve", 0) >= 80:
        $ story_flag("tam_c04_m03_quang_thienan_shared_space")
        $ story_add_direction("quang", "quang_thienan_open")
        $ story_add_direction("thienan", "thienan_quang_open")
    elif story_state.get("thienan_quang_trust", 0) >= 60:
        $ story_flag("tam_c04_m03_quang_thienan_learning_space")
    else:
        $ story_flag("tam_c04_m03_quang_thienan_not_chosen")

    if story_state.get("tam_quang_interest", 0) >= 40 and story_state.get("quang_tam_awareness", 0) >= 35 and story_state.get("quang_tam_warmth", 0) >= 65:
        $ story_flag("tam_c04_m03_tam_quang_personal_tension")
        $ story_add_direction("quang", "quang_tam_open")
    elif story_state.get("tam_quang_interest", 0) >= 25:
        $ story_flag("tam_c04_m03_tam_quang_question_open")
    else:
        $ story_flag("tam_c04_m03_tam_quang_family_familiarity")

    if story_has_flag("tam_c04_m03_quang_thienan_shared_space") and story_has_flag("tam_c04_m03_tam_quang_personal_tension"):
        $ story_flag("tam_c04_m03_quang_crosscurrent_visible")
    elif story_has_flag("tam_c04_m03_quang_thienan_learning_space") and story_has_flag("tam_c04_m03_tam_quang_question_open"):
        $ story_flag("tam_c04_m03_quang_crosscurrent_unsettled")

    $ _tam_c04_m03_career_tam_progress = career_bonus_get_progress_since_chapter_start("tam_c04_between_work_and_hearts", "tam")
    $ _tam_c04_m03_career_huyen_progress = career_bonus_get_progress_since_chapter_start("tam_c04_between_work_and_hearts", "huyen")

    if _tam_c04_m03_career_tam_progress >= 260:
        $ story_flag("tam_c04_m03_tam_career_fast_track")
    elif _tam_c04_m03_career_tam_progress >= 180:
        $ story_flag("tam_c04_m03_tam_career_advancing")
    else:
        $ story_flag("tam_c04_m03_tam_career_developing")

    if _tam_c04_m03_career_huyen_progress >= 230:
        $ story_flag("tam_c04_m03_huyen_career_fast_track")
    elif _tam_c04_m03_career_huyen_progress >= 160:
        $ story_flag("tam_c04_m03_huyen_career_advancing")
    else:
        $ story_flag("tam_c04_m03_huyen_career_developing")

    $ story_flag("tam_c04_m03_snapshot_recorded")
    $ phone_refresh_all()
    return
