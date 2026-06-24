# FILE: game/story/flashback_minyuu/fb_minyuu_05b_separation/s02_break_or_silent_distance.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_05b_separation_s02_break_or_silent_distance:
    "MVP Flashback: The breakup can be explicit or silent."
    menu:
        "How do they separate?"

        "A clear breakup":
            $ story_flag('minyuu_clean_break')
            $ story_add('boundary_score', 1)

        "Silent distance":
            $ story_flag('minyuu_silent_distance')
            $ story_add('minh_yuuka_unresolved', 2)

        "Yuuka leaves before Minh explains":
            $ story_flag('yuuka_left_first')
            $ story_add('minh_yuuka_unresolved', 2)
            $ story_add('doom_score', 1)
    return
