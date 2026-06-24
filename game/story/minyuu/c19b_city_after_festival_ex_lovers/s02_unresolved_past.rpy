# FILE: game/story/minyuu/c19b_city_after_festival_ex_lovers/s02_unresolved_past.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label c19b_city_after_festival_ex_lovers_s02_unresolved_past:
    "MVP: The old wound is named or avoided."
    menu:
        "What truth is faced?"

        "Yuuka admits she ran":
            $ story_add('minh_yuuka_trust', 2)
            $ story_add_ending_support('e10_minyuu_reunion')

        "Minh admits he cut too much away":
            $ story_add('minh_yuuka_trust', 2)
            $ story_add_ending_support('e10_minyuu_reunion')

        "They avoid the wound again":
            $ story_add('minh_yuuka_unresolved', 3)
            $ story_add('doom_score', 1)
    return
