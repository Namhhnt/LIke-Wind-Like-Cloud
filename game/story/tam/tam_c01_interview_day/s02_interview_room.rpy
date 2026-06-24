# FILE: game/story/tam/tam_c01_interview_day/s02_interview_room.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c01_interview_day_s02_interview_room:
    "Tâm faces the interview panel. Quân is mentioned through office rumors."
    call tam_c01_speech_game

    if tam_salary_tier == "high":
        $ story_add('career_tam', 2)
        $ story_add('tam_self_clarity', 1)
    elif has_player_flag("tam_interview_passed"):
        $ story_add('career_tam', 1)
    else:
        $ story_add('doom_score', 1)
    return
