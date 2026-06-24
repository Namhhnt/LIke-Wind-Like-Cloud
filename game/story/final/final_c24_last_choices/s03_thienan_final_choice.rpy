# FILE: game/story/final/final_c24_last_choices/s03_thienan_final_choice.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label final_c24_last_choices_s03_thienan_final_choice:
    "MVP: Final Thiên An choice."
    menu:
        "Thiên An's final direction:"

        "Thiên An-Quang":
            $ story_add_ending_support('e06_thienan_quang')
            $ story_add('thienan_quang_trust', 2)

        "Thiên An-Minh" if story_relation_is('old_close_friends') and not story_state['minh_romance_lock']:
            $ story_add_direction('thienan', 'thienan_minh_commit')
            $ story_add_ending_support('e07_thienan_minh')
            $ story_add('thienan_minh_residue', 2)

        "Thiên An single":
            $ story_add_ending_support('e08_thienan_single')
            $ story_add('thienan_self_assertion', 2)

        "Arranged marriage":
            $ story_add_ending_support('e09_thienan_arranged')
            $ story_add('family_pressure_thienan', 2)
    return
