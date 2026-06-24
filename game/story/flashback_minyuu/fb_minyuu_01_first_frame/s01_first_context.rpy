# FILE: game/story/flashback_minyuu/fb_minyuu_01_first_frame/s01_first_context.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_01_first_frame_s01_first_context:
    "MVP Flashback: Minh and Yuuka meet for the first time in a film/academic context."
    menu:
        "What is the first impression?"

        "Professional friction":
            $ story_add('boundary_score', 1)
            $ story_add('old_friend_score', 1)

        "Emotional recognition":
            $ story_add('romantic_score', 1)
            $ story_add('minh_yuuka_intimacy', 1)

        "Mutual respect":
            $ story_add('minh_yuuka_trust', 1)
            $ story_add('old_friend_score', 1)
    return
