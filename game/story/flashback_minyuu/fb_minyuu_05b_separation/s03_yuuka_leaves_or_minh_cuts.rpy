# FILE: game/story/flashback_minyuu/fb_minyuu_05b_separation/s03_yuuka_leaves_or_minh_cuts.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_05b_separation_s03_yuuka_leaves_or_minh_cuts:
    "MVP Flashback: The emotional wound is set."
    menu:
        "What wound remains?"

        "Minh thinks letting go protects Yuuka":
            $ story_add('boundary_score', 1)
            $ story_add('minh_yuuka_unresolved', 1)

        "Yuuka thinks Minh did not choose her":
            $ story_add('minh_yuuka_unresolved', 2)

        "Both know love was not the problem":
            $ story_add('minh_yuuka_trust', 1)
            $ story_add('minh_yuuka_intimacy', 1)
    return
