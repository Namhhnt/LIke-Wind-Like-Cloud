# FILE: game/story/flashback_minyuu/fb_minyuu_01_first_frame/s02_professional_friction.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_01_first_frame_s02_professional_friction:
    "MVP Flashback: Minh gives precise feedback on Yuuka's early film work."
    menu:
        "How does Yuuka respond?"

        "Argue back":
            $ story_add('minh_yuuka_trust', 1)
            $ story_add('romantic_score', 1)

        "Take notes silently":
            $ story_add('old_friend_score', 1)
            $ story_add('career_tam', 0)

        "Ask him to explain properly":
            $ story_add('minh_yuuka_trust', 2)
    return
