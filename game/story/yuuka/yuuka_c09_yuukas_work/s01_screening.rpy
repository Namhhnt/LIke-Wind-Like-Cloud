# FILE: game/story/yuuka/yuuka_c09_yuukas_work/s01_screening.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label yuuka_c09_yuukas_work_s01_screening:
    "MVP: Yuuka's film is screened. The chapter centers her work."
    menu:
        "What does the player focus on?"

        "The film's craft":
            $ story_add('tam_respect_yuuka', 1)
            $ story_add('career_tam', 1)

        "The audience response":
            $ story_add('tam_observation', 1)

        "Minh watching quietly":
            $ story_add('minh_yuuka_intimacy', 1)
    return
