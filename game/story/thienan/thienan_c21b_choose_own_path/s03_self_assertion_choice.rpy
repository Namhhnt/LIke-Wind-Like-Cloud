# FILE: game/story/thienan/thienan_c21b_choose_own_path/s03_self_assertion_choice.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label thienan_c21b_choose_own_path_s03_self_assertion_choice:
    "MVP: Thiên An chooses her path without Minh as a romance option."
    menu:
        "Thiên An chooses..."

        "Quang":
            $ story_add('thienan_quang_trust', 3)
            $ story_add_ending_support('e06_thienan_quang')

        "Single self-direction":
            $ story_add('thienan_self_assertion', 3)
            $ story_add_ending_support('e08_thienan_single')

        "Family arrangement":
            $ story_add('family_pressure_thienan', 3)
            $ story_add_ending_support('e09_thienan_arranged')
    return
