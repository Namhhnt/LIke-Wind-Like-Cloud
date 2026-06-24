# FILE: game/story/yuuka/yuuka_c09_yuukas_work/s03_state_sensitive_minh_yuuka_moment.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label yuuka_c09_yuukas_work_s03_state_sensitive_minh_yuuka_moment:
    "MVP: Minh-Yuuka interaction changes based on their finalized relation."
    if story_relation_is('old_close_friends'):
        "MVP: Minh and Yuuka speak like old friends with professional warmth."
        $ story_add('minh_yuuka_trust', 1)
    elif story_relation_is('ex_lovers_long_separated'):
        "MVP: Minh notices one detail in the film that only someone close would catch."
        $ story_add('minh_yuuka_intimacy', 1)
        $ story_add('minh_yuuka_unresolved', 1)
    elif story_relation_is('still_lovers'):
        "MVP: Yuuka briefly looks at Minh before answering a difficult question."
        $ story_add('minh_yuuka_trust', 1)
    else:
        "MVP: Their past remains unclear."
    return
