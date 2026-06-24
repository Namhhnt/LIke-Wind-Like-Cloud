# FILE: game/story/flashback_minyuu/fb_minyuu_01_first_frame/s03_first_choice.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_01_first_frame_s03_first_choice:
    "MVP Flashback: The first meeting creates the earliest route seed."
    menu:
        "Which seed is stronger?"

        "Respect before affection":
            $ story_add('old_friend_score', 2)
            $ story_add('boundary_score', 1)

        "Curiosity before distance":
            $ story_add('romantic_score', 2)
            $ story_add('minh_yuuka_intimacy', 1)

        "Distance before anything else":
            $ story_add('boundary_score', 2)
    return
