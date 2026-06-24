# FILE: game/story/flashback_minyuu/fb_minyuu_04b_living_together/s01_shared_home.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_04b_living_together_s01_shared_home:
    "MVP Flashback: Minh and Yuuka live under the same roof temporarily."
    menu:
        "What defines the shared home?"

        "House rules":
            $ story_add('boundary_score', 1)
            $ story_add('ex_lover_score', 1)

        "Small habits":
            $ story_add('romantic_score', 2)
            $ story_add('minh_yuuka_intimacy', 1)

        "Unspoken dependence":
            $ story_add('minh_yuuka_unresolved', 1)
    return
