# FILE: game/story/hoang/hoang_h05_shadow_of_minh/s01_hoang_insecurity_or_clarity.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label hoang_h05_shadow_of_minh_s01_hoang_insecurity_or_clarity:
    "MVP: Hoàng reacts to Minh's presence and Yuuka's state."
    if story_relation_is('old_close_friends'):
        "MVP: Hoàng may fear being compared to Minh."
        $ story_add('hoang_insecurity', 1)
    elif story_relation_is('ex_lovers_long_separated'):
        "MVP: Hoàng is more upset about Minh and Yuuka than about romantic rivalry."
        $ story_add('hoang_self_acceptance', 1)
    elif story_relation_is('still_lovers'):
        "MVP: Hoàng understands Minh is not a rival route."
        $ story_add('hoang_self_acceptance', 2)
    return
