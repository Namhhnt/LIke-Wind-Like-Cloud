# FILE: game/story/yuuka/yuuka_c08_festival_arrival/s01_festival_briefing.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label yuuka_c08_festival_arrival_s01_festival_briefing:
    "MVP: The company is briefed about the Film Festival. Yuuka Nakamura is listed as a guest director."
    menu:
        "What does Tâm focus on?"

        "The professional importance of the festival":
            $ story_add('career_tam', 1)

        "Yuuka's film profile":
            $ story_add('tam_respect_yuuka', 1)

        "Hoàng's reaction to Yuuka's name":
            $ story_add('tam_observation', 1)
    return
