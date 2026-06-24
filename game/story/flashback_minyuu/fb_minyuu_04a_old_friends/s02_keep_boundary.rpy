# FILE: game/story/flashback_minyuu/fb_minyuu_04a_old_friends/s02_keep_boundary.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_04a_old_friends_s02_keep_boundary:
    "MVP Flashback: They choose closeness without becoming lovers."
    menu:
        "What remains between them?"

        "Trust":
            $ story_add('minh_yuuka_trust', 2)

        "A small unanswered question":
            $ story_add('minh_yuuka_unresolved', 1)

        "Respectful distance":
            $ story_add('boundary_score', 2)
    return
