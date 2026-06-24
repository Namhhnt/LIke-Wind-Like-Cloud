# FILE: game/story/minyuu/c19b_city_after_festival_ex_lovers/s03_reunion_or_late_or_single_choice.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label c19b_city_after_festival_ex_lovers_s03_reunion_or_late_or_single_choice:
    "MVP: Ex-lovers route picks the resolution direction."
    menu:
        "What do they choose?"

        "Try again now":
            $ story_add_ending_support('e10_minyuu_reunion')
            $ story_add('minh_yuuka_trust', 2)

        "Do not rush; leave a future open":
            $ story_add_ending_support('e11_minyuu_late_reunion')

        "Forgive, but do not return":
            $ story_add_ending_support('e18_minyuu_mutual_single')

        "Say too little":
            $ story_add('minh_yuuka_unresolved', 3)
            $ story_add_ending_support('e24_doom')
    return
