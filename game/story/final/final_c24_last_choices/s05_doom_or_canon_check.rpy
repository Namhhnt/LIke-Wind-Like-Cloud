# FILE: game/story/final/final_c24_last_choices/s05_doom_or_canon_check.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label final_c24_last_choices_s05_doom_or_canon_check:
    "MVP: Final optional global ending nudge."
    menu:
        "Final global route target:"

        "Try Canon True Ending":
            $ story_add_ending_support('e01_canon_true')
            $ story_add_ending_support('e02_tam_hoang')
            $ story_add_ending_support('e05_huyen_quan')
            $ story_add_ending_support('e06_thienan_quang')
            if story_relation_is('ex_lovers_long_separated'):
                $ story_add_ending_support('e10_minyuu_reunion')
            elif story_relation_is('still_lovers'):
                $ story_add_ending_support('e13_minyuu_public_lovers')

        "Let current scores decide":
            $ story_flag('final_scores_decide')

        "Force Doom path":
            $ story_add_ending_support('e24_doom')
            $ story_add('doom_score', 8)
    return
