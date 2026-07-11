# FILE: game/story/tam/tam_c04_between_work_and_hearts/s96_w16_month_four_snapshot.rpy

label tam_c04_w16_s06_month_four_snapshot:
    $ tam_c04_ensure_extended_story_state()
    if tam_c04_hoang_breakthrough_ready():
        $ story_flag("tam_c04_m04_hoang_ready")
    else:
        $ story_flag("tam_c04_m04_hoang_not_ready")
    if tam_c04_quang_tam_breakthrough_ready():
        $ story_flag("tam_c04_m04_quang_tam_ready")
    else:
        $ story_flag("tam_c04_m04_quang_tam_not_ready")
    if tam_c04_quang_thienan_breakthrough_ready():
        $ story_flag("tam_c04_m04_quang_thienan_closer")
    else:
        $ story_flag("tam_c04_m04_quang_thienan_holding")
    if tam_c04_huyen_quan_deep_trust_ready():
        $ story_flag("tam_c04_m04_huyen_quan_deep_ready")
    else:
        $ story_flag("tam_c04_m04_huyen_quan_work_only")
    $ story_flag("tam_c04_m04_snapshot_recorded")
    $ phone_refresh_all()
    return
