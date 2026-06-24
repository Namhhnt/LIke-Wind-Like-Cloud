# FILE: game/story/yuuka/yuuka_c18b_habit_of_you/s02_work_and_absence.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label yuuka_c18b_habit_of_you_s02_work_and_absence:
    "MVP: Yuuka works, but Minh's absence remains part of her rhythm."
    menu:
        "How does Yuuka handle absence?"

        "Turn it into discipline":
            $ story_add('minh_yuuka_trust', 1)
            $ story_add_ending_support('e11_minyuu_late_reunion')

        "Avoid thinking about it":
            $ story_add('minh_yuuka_unresolved', 2)
            $ story_add('doom_score', 1)

        "Admit she still cares":
            $ story_add('minh_yuuka_intimacy', 1)
            $ story_add_ending_support('e10_minyuu_reunion')
    return
