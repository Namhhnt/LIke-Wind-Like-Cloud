# FILE: game/story/group/group_c11_social_dinner/s03_state_sensitive_dinner.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label group_c11_social_dinner_s03_state_sensitive_dinner:
    "MVP: The meaning of dinner changes based on Minh-Yuuka relation."
    if story_relation_is('old_close_friends'):
        "MVP: Dinner feels like old friends reconnecting."
        $ story_add('minh_yuuka_trust', 1)
    elif story_relation_is('ex_lovers_long_separated'):
        "MVP: Dinner carries quiet unresolved history."
        $ story_add('minh_yuuka_unresolved', 1)
    elif story_relation_is('still_lovers'):
        "MVP: Dinner feels like private familiarity hidden in plain sight."
        $ story_add('minh_yuuka_trust', 1)
    return
