# FILE: game/story/yuuka/yuuka_c18b_habit_of_you/s04_late_reunion_seed.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label yuuka_c18b_habit_of_you_s04_late_reunion_seed:
    "MVP: The late reunion or single path is seeded."
    menu:
        "What does Yuuka leave open?"

        "A direct reunion":
            $ story_add_ending_support('e10_minyuu_reunion')

        "A much later reunion":
            $ story_add_ending_support('e11_minyuu_late_reunion')

        "A mutual single ending":
            $ story_add_ending_support('e18_minyuu_mutual_single')
    return
