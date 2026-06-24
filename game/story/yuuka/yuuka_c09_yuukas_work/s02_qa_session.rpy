# FILE: game/story/yuuka/yuuka_c09_yuukas_work/s02_qa_session.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label yuuka_c09_yuukas_work_s02_qa_session:
    "MVP: Yuuka answers questions after the screening."
    menu:
        "Which answer matters most?"

        "Her answer about silence in film":
            $ story_add('tam_respect_yuuka', 1)

        "Her answer about ordinary details":
            $ story_add('career_tam', 1)

        "Her refusal to over-explain herself":
            $ story_add('tam_self_clarity', 1)
    return
