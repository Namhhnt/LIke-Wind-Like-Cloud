# FILE: game/story/flashback_minyuu/fb_minyuu_05b_separation/s01_distance_starts.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_05b_separation_s01_distance_starts:
    "MVP Flashback: Distance starts between Minh and Yuuka."
    menu:
        "What starts the distance?"

        "Minh chooses responsibility over comfort":
            $ story_add('boundary_score', 2)
            $ story_add('minh_yuuka_unresolved', 1)

        "Yuuka chooses career movement":
            $ story_add('minh_yuuka_trust', 1)
            $ story_add('minh_yuuka_unresolved', 1)

        "Both wait for the other to speak":
            $ story_add('minh_yuuka_unresolved', 2)
    return
