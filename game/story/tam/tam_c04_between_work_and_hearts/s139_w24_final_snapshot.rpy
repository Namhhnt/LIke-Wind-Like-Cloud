# FILE: game/story/tam/tam_c04_between_work_and_hearts/s139_w24_final_snapshot.rpy

label tam_c04_w24_s06_final_snapshot:
    if story_has_flag("tam_c04_tam_hoang_dating"):
        $ story_flag("tam_c04_final_tam_romance_hoang")
    elif story_has_flag("tam_c04_tam_quang_confirmed"):
        $ story_flag("tam_c04_final_tam_romance_quang")
    else:
        $ story_flag("tam_c04_final_tam_independent")
    if story_has_flag("tam_c04_quang_thienan_committed"):
        $ story_flag("tam_c04_final_quang_thienan_closer")
    $ _tam_c04_huyen_lane_found = False
    if story_has_flag("tam_c04_huyen_quan_deep_trust") or story_has_flag("tam_c04_huyen_quan_deep_trust_available"):
        $ story_flag("tam_c04_final_huyen_quan_deep_trust")
        $ _tam_c04_huyen_lane_found = True
    if story_has_flag("tam_c04_huyen_hoang_future_open") or story_has_flag("tam_c04_huyen_hoang_future_seed"):
        $ story_flag("tam_c04_final_huyen_hoang_future_open")
        $ _tam_c04_huyen_lane_found = True
    elif story_has_flag("tam_c04_huyen_hoang_interest_developing"):
        $ story_flag("tam_c04_final_huyen_hoang_interest_developing")
        $ _tam_c04_huyen_lane_found = True
    if not _tam_c04_huyen_lane_found:
        $ story_flag("tam_c04_final_huyen_independent_career")
    $ _tam_c04_final_career_tam = career_bonus_get_progress_since_chapter_start("tam_c04_between_work_and_hearts", "tam")
    $ _tam_c04_final_career_huyen = career_bonus_get_progress_since_chapter_start("tam_c04_between_work_and_hearts", "huyen")
    if _tam_c04_final_career_tam >= 500:
        $ story_flag("tam_c04_final_tam_career_accelerated")
    else:
        $ story_flag("tam_c04_final_tam_career_steady")
    if _tam_c04_final_career_huyen >= 450:
        $ story_flag("tam_c04_final_huyen_career_accelerated")
    else:
        $ story_flag("tam_c04_final_huyen_career_steady")
    $ story_flag("tam_c04_final_snapshot_recorded")
    $ phone_refresh_all()
    return
