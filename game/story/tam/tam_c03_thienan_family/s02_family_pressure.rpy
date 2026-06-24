# FILE: game/story/tam/tam_c03_thienan_family/s02_family_pressure.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c03_thienan_family_s02_family_pressure:
    "MVP: Family marriage pressure around Thiên An is introduced."
    menu:
        "How does Tâm respond?"

        "Question the pressure gently":
            $ story_add('thienan_self_assertion', 2)

        "Stay silent":
            $ story_add('family_pressure_thienan', 2)

        "Deflect with work talk":
            $ story_add('career_tam', 1)
    return
