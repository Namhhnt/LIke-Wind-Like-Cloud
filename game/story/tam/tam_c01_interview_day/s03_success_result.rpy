# FILE: game/story/tam/tam_c01_interview_day/s03_success_result.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c01_interview_day_s03_success_result:
    "MVP: Tâm and Huyền both pass the interview."
    menu:
        "How do they react?"

        "Celebrate together":
            $ story_flag('tam_huyen_strong_bond')
            $ story_add('career_huyen', 1)

        "Call Thiên An first":
            $ story_add('thienan_self_assertion', 1)

        "Keep the joy quiet":
            $ story_add('tam_self_clarity', 1)
    return
