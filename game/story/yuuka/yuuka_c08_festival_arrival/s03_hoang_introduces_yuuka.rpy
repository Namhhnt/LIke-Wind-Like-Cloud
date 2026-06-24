# FILE: game/story/yuuka/yuuka_c08_festival_arrival/s03_hoang_introduces_yuuka.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label yuuka_c08_festival_arrival_s03_hoang_introduces_yuuka:
    "MVP: Hoàng greets Yuuka and introduces her as an old friend of Minh and Hoàng."
    menu:
        "How does the player read this introduction?"

        "Neutral old friendship":
            $ story_add('boundary_score', 1)

        "There may be history, but it is unclear":
            $ story_add('tam_observation', 1)

        "Ask Hoàng later":
            $ story_flag('ask_hoang_about_yuuka_later')
    return
