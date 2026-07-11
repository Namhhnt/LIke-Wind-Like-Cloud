# FILE: game/story/tam/tam_c04_between_work_and_hearts/s118_w20_month_five_snapshot.rpy

label tam_c04_w20_s05_month_five_snapshot:
    if story_has_flag("tam_c04_tam_hoang_dating"):
        $ story_flag("tam_c04_m05_tam_route_hoang")
    elif story_has_flag("tam_c04_tam_quang_confirmed"):
        $ story_flag("tam_c04_m05_tam_route_quang")
    else:
        $ story_flag("tam_c04_m05_tam_route_independent")
    if story_has_flag("tam_c04_quang_thienan_committed"):
        $ story_flag("tam_c04_m05_quang_thienan_closer_phase")
    elif story_has_flag("tam_c04_tam_quang_confirmed"):
        $ story_flag("tam_c04_m05_quang_tam_confirmed_phase")
    else:
        $ story_flag("tam_c04_m05_quang_unresolved")
    if story_has_flag("tam_c04_huyen_quan_deep_trust"):
        $ story_flag("tam_c04_m05_huyen_quan_deep_trust_phase")
    else:
        $ story_flag("tam_c04_m05_huyen_route_open")
    $ story_flag("tam_c04_m05_snapshot_recorded")
    $ phone_refresh_all()
    return
