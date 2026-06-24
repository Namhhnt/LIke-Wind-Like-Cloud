# FILE: game/story/yuuka/yuuka_c08_festival_arrival/s02_yuuka_as_director.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label yuuka_c08_festival_arrival_s02_yuuka_as_director:
    "MVP: Yuuka is introduced through her work as a young Japanese film director, not through romance."
    menu:
        "What does Yuuka's presence establish first?"

        "Her career":
            $ story_add('tam_respect_yuuka', 2)
            $ story_add('career_tam', 1)

        "Her beauty":
            $ story_add('tam_insecurity', 1)

        "Her discipline with details":
            $ story_add('tam_observation', 1)
            $ story_add('tam_respect_yuuka', 1)
    return
