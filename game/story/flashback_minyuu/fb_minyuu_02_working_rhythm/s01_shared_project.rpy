# FILE: game/story/flashback_minyuu/fb_minyuu_02_working_rhythm/s01_shared_project.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_02_working_rhythm_s01_shared_project:
    "MVP Flashback: Minh and Yuuka work on a project rhythm together."
    menu:
        "What rhythm forms?"

        "Efficient and professional":
            $ story_add('old_friend_score', 2)
            $ story_add('minh_yuuka_trust', 1)

        "Quietly intimate":
            $ story_add('romantic_score', 2)
            $ story_add('minh_yuuka_intimacy', 1)

        "Uneven but honest":
            $ story_add('minh_yuuka_trust', 2)
    return
