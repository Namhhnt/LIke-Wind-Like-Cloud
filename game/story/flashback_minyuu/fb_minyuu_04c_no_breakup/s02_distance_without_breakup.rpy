# FILE: game/story/flashback_minyuu/fb_minyuu_04c_no_breakup/s02_distance_without_breakup.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_04c_no_breakup_s02_distance_without_breakup:
    "MVP Flashback: They separate physically, but do not break up."
    menu:
        "What creates distance?"

        "Yuuka's career":
            $ story_add_ending_support('e15_minyuu_long_distance')

        "Minh's responsibility":
            $ story_add_ending_support('e12_minyuu_private_lovers')

        "Both agree to wait":
            $ story_add('minh_yuuka_trust', 2)
    return
