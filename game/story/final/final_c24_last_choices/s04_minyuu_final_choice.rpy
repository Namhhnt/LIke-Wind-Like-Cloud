# FILE: game/story/final/final_c24_last_choices/s04_minyuu_final_choice.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label final_c24_last_choices_s04_minyuu_final_choice:
    "MVP: Final Minh-Yuuka choice, depending on relation state."
    if story_relation_is('old_close_friends'):
        menu:
            "Old friends final direction:"

            "Friendship":
                $ story_add_ending_support('e20_minyuu_friendship')
                $ story_add('minh_yuuka_trust', 2)

            "Yuuka career":
                $ story_add_ending_support('e19_yuuka_career')

            "Minh single":
                $ story_add_ending_support('e16_minh_single')

            "Yuuka single":
                $ story_add_ending_support('e17_yuuka_single')

    elif story_relation_is('ex_lovers_long_separated'):
        menu:
            "Ex lovers final direction:"

            "Reunion":
                $ story_add_ending_support('e10_minyuu_reunion')
                $ story_add('minh_yuuka_trust', 2)

            "Late reunion":
                $ story_add_ending_support('e11_minyuu_late_reunion')

            "Mutual single":
                $ story_add_ending_support('e18_minyuu_mutual_single')

            "Minh single":
                $ story_add_ending_support('e16_minh_single')

    elif story_relation_is('still_lovers'):
        menu:
            "Still lovers final direction:"

            "Private lovers":
                $ story_add_ending_support('e12_minyuu_private_lovers')

            "Public lovers":
                $ story_add_ending_support('e13_minyuu_public_lovers')

            "Non-marriage lovers":
                $ story_add_ending_support('e14_minyuu_non_marriage')

            "Long-distance lovers":
                $ story_add_ending_support('e15_minyuu_long_distance')
    else:
        "MVP: Missing Minh-Yuuka relation. This should not happen in a normal run."
        $ story_add_ending_support('e24_doom')
    return
