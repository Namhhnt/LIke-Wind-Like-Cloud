# FILE: game/story/flashback_minyuu/fb_minyuu_04a_old_friends/s01_almost_said.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_04a_old_friends_s01_almost_said:
    "MVP Flashback: Minh and Yuuka nearly say something more, but the moment passes."
    menu:
        "How does the moment end?"

        "With a joke":
            $ story_add('old_friend_score', 2)

        "With silence":
            $ story_add('minh_yuuka_unresolved', 1)

        "With professional focus":
            $ story_add('boundary_score', 1)
    return
