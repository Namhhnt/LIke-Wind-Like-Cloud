# FILE: game/story/tam/tam_c01_interview_day/s01_tam_huyen_morning.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c01_interview_day_s01_tam_huyen_morning:
    "MVP: Tâm and Huyền arrive for their interview together."
    menu:
        "What does Tâm prioritize before the interview?"

        "Calm Huyền down":
            $ story_add('career_huyen', 1)
            $ story_flag('tam_supports_huyen')

        "Review the portfolio again":
            $ story_add('career_tam', 2)

        "Hide her nervousness with a joke":
            $ story_add('tam_self_clarity', 1)
    return
