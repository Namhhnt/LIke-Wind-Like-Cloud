# FILE: game/story/prologue/prologue_rain_dream/s02_wake_up.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label prologue_rain_dream_s02_wake_up:
    "MVP: Tâm wakes up and prepares for the interview day."
    menu:
        "How does Tâm treat the dream?"

        "Take it seriously":
            $ story_add('tam_observation', 1)

        "Dismiss it as stress":
            $ story_add('career_tam', 1)

        "Feel unsettled but say nothing":
            $ story_add('doom_score', 1)
    return
