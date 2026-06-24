# FILE: game/story/flashback_minyuu/fb_minyuu_02_working_rhythm/s03_minh_care_or_boundary.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_02_working_rhythm_s03_minh_care_or_boundary:
    "MVP Flashback: Minh either cares through small actions or keeps clear boundaries."
    menu:
        "What does Minh do?"

        "Quietly fixes a practical problem for Yuuka":
            $ story_add('romantic_score', 2)
            $ story_add('ex_lover_score', 1)

        "Gives advice and steps back":
            $ story_add('old_friend_score', 2)
            $ story_add('boundary_score', 1)

        "Lets Yuuka solve it herself but stays nearby":
            $ story_add('minh_yuuka_trust', 2)
    return
