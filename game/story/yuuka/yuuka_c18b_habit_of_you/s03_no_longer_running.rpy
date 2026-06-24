# FILE: game/story/yuuka/yuuka_c18b_habit_of_you/s03_no_longer_running.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label yuuka_c18b_habit_of_you_s03_no_longer_running:
    "MVP: Yuuka decides whether she will keep running."
    menu:
        "Yuuka chooses to..."

        "Stop running":
            $ story_add('minh_yuuka_trust', 2)
            $ story_add_ending_support('e10_minyuu_reunion')

        "Move slowly, not immediately return":
            $ story_add_ending_support('e11_minyuu_late_reunion')

        "Forgive but choose herself":
            $ story_add_ending_support('e18_minyuu_mutual_single')
    return
