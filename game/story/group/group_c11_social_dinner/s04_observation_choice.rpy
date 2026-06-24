# FILE: game/story/group/group_c11_social_dinner/s04_observation_choice.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label group_c11_social_dinner_s04_observation_choice:
    "MVP: Tâm chooses what to do with what she observes."
    menu:
        "Tâm chooses to..."

        "Focus on Hoàng":
            $ story_add('hoang_tam_trust', 2)

        "Ask Yuuka about film":
            $ story_add('tam_respect_yuuka', 2)
            $ story_add('career_tam', 1)

        "Watch Minh and Yuuka quietly":
            $ story_add('tam_observation', 1)
            $ story_add('doom_score', 1)
    return
