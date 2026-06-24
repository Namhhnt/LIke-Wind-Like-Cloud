# FILE: game/story/yuuka/yuuka_c09_yuukas_work/s04_tam_or_huyen_observation.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label yuuka_c09_yuukas_work_s04_tam_or_huyen_observation:
    "MVP: Tâm and Huyền process Yuuka after the event."
    menu:
        "Who interprets Yuuka most clearly?"

        "Tâm respects her professionally":
            $ story_add('career_tam', 1)
            $ story_add('tam_respect_yuuka', 1)

        "Huyền notices the social tension":
            $ story_add('career_huyen', 1)

        "Both avoid talking about Minh":
            $ story_add('doom_score', 1)
    return
