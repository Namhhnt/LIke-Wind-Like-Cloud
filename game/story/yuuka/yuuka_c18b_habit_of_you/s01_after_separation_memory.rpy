# FILE: game/story/yuuka/yuuka_c18b_habit_of_you/s01_after_separation_memory.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label yuuka_c18b_habit_of_you_s01_after_separation_memory:
    "MVP: Ex-lovers route. Yuuka remembers the years after separation."
    menu:
        "What did separation leave behind?"

        "Habits learned from Minh":
            $ story_add('minh_yuuka_trust', 1)

        "Unresolved hurt":
            $ story_add('minh_yuuka_unresolved', 1)

        "Career discipline":
            $ story_add_ending_support('e19_yuuka_career')
    return
