# FILE: game/story/thienan/thienan_c21b_choose_own_path/s02_quang_or_family_pressure.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label thienan_c21b_choose_own_path_s02_quang_or_family_pressure:
    "MVP: Quang and family pressure become Thiên An's real route fork."
    menu:
        "Which force grows stronger?"

        "Quang's patience":
            $ story_add('thienan_quang_trust', 2)

        "Family arrangement":
            $ story_add('family_pressure_thienan', 2)

        "Thiên An's self-respect":
            $ story_add('thienan_self_assertion', 2)
    return
