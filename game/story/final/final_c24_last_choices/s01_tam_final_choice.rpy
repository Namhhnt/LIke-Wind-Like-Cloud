# FILE: game/story/final/final_c24_last_choices/s01_tam_final_choice.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label final_c24_last_choices_s01_tam_final_choice:
    "MVP: Final Tâm choice."
    menu:
        "Tâm's final direction:"

        "Tâm-Hoàng" if not story_has_direction('tam', 'tam_minh_commit'):
            $ story_add_ending_support('e02_tam_hoang')
            $ story_add('hoang_tam_trust', 2)

        "Tâm-Minh" if story_relation_is('old_close_friends') and not story_state['minh_romance_lock']:
            $ story_add_direction('tam', 'tam_minh_commit')
            $ story_add_ending_support('e03_tam_minh')
            $ story_add('tam_minh_drawn', 2)

        "Tâm independent":
            $ story_add_ending_support('e21_tam_independent')
            $ story_add('tam_self_clarity', 2)

        "Avoid deciding":
            $ story_add('doom_score', 2)
    return
