# FILE: game/story/yuuka/yuuka_c08_festival_arrival/s04_minh_neutral_pause.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label yuuka_c08_festival_arrival_s04_minh_neutral_pause:
    "MVP: Minh and Yuuka greet each other. The scene stays neutral; their past is not confirmed."
    menu:
        "What does Tâm notice?"

        "The tiny pause":
            $ story_flag('noticed_minyuu_pause')
            $ story_add('tam_observation', 1)

        "The professional setting":
            $ story_add('career_tam', 1)

        "Nothing unusual":
            $ story_add('tam_self_clarity', 1)
    return
