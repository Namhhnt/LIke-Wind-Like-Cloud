# FILE: game/story/flashback_minyuu/fb_minyuu_03_door_left_open/s01_problem_setup.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_03_door_left_open_s01_problem_setup:
    "MVP Flashback: A practical problem forces Minh to decide how deeply to let Yuuka into his life."
    menu:
        "What kind of problem is it?"

        "Housing / safety":
            $ story_add('minh_yuuka_trust', 1)

        "Work pressure":
            $ story_add('old_friend_score', 1)

        "Emotional exhaustion":
            $ story_add('romantic_score', 1)
    return
