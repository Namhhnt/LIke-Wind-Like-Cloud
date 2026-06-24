# FILE: game/story/flashback_minyuu/fb_minyuu_02_working_rhythm/s02_yuuka_learning.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_02_working_rhythm_s02_yuuka_learning:
    "MVP Flashback: Yuuka learns how Minh sees structure, consequence, and detail."
    menu:
        "What does Yuuka absorb most?"

        "Discipline":
            $ story_add('old_friend_score', 1)
            $ story_add('boundary_score', 1)

        "Care hidden inside criticism":
            $ story_add('romantic_score', 2)
            $ story_add('minh_yuuka_intimacy', 1)

        "Confidence in her own eye":
            $ story_add('minh_yuuka_trust', 1)
    return
