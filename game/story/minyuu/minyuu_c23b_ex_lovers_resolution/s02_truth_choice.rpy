# FILE: game/story/minyuu/minyuu_c23b_ex_lovers_resolution/s02_truth_choice.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label minyuu_c23b_ex_lovers_resolution_s02_truth_choice:
    "MVP: The truth choice determines whether reunion is possible."
    menu:
        "What truth is spoken?"

        "They still love each other":
            $ story_add('minh_yuuka_trust', 2)
            $ story_add_ending_support('e10_minyuu_reunion')

        "They need more time":
            $ story_add_ending_support('e11_minyuu_late_reunion')

        "Love remains, but return is not right":
            $ story_add_ending_support('e18_minyuu_mutual_single')

        "They avoid it again":
            $ story_add('minh_yuuka_unresolved', 3)
            $ story_add_ending_support('e24_doom')
    return
