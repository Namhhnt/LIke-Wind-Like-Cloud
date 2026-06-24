# FILE: game/story/thienan/thienan_c21a_minh_possible/s03_thienan_choice.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label thienan_c21a_minh_possible_s03_thienan_choice:
    "MVP: Thiên An chooses between old residue, Quang, family pressure, or herself."
    menu:
        "Thiên An chooses..."

        "Explore Minh route":
            $ story_add_direction('thienan', 'thienan_minh_commit')
            $ story_add('thienan_minh_residue', 2)
            $ story_add_ending_support('e07_thienan_minh')

        "Choose Quang":
            $ story_add('thienan_quang_trust', 3)
            $ story_add_ending_support('e06_thienan_quang')

        "Yield to family pressure":
            $ story_add('family_pressure_thienan', 3)
            $ story_add_ending_support('e09_thienan_arranged')

        "Choose herself":
            $ story_add('thienan_self_assertion', 3)
            $ story_add_ending_support('e08_thienan_single')
    return
