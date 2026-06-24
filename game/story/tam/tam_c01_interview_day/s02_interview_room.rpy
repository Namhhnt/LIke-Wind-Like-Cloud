# FILE: game/story/tam/tam_c01_interview_day/s02_interview_room.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c01_interview_day_s02_interview_room:
    "MVP: Tâm faces the interview panel. Quân is mentioned through office rumors."
    menu:
        "How does Tâm answer the difficult question?"

        "Structured and practical":
            $ story_add('career_tam', 2)

        "Honest about what she does not know":
            $ story_add('tam_self_clarity', 1)
            $ story_add('career_tam', 1)

        "Over-explain to sound impressive":
            $ story_add('doom_score', 1)
    return
