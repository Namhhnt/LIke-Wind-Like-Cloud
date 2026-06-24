# FILE: game/story/tam/tam_c01_interview_day/s04_celebration_dinner.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c01_interview_day_s04_celebration_dinner:
    "MVP: Tâm and Huyền celebrate at a nice restaurant. Hoàng appears in the same space but they do not formally know him yet."
    menu:
        "Who notices Hoàng first?"

        "Tâm":
            $ story_add('tam_hoang_interest', 1)
            $ story_flag('tam_notices_hoang_first')

        "Huyền":
            $ story_add('huyen_hoang_interest', 1)
            $ story_flag('huyen_notices_hoang_first')

        "Neither of them pays much attention":
            $ story_add('career_tam', 1)
    return
