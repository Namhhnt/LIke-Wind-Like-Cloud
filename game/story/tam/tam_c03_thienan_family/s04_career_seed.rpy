# FILE: game/story/tam/tam_c03_thienan_family/s04_career_seed.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c03_thienan_family_s04_career_seed:
    "MVP: Thiên An gives Tâm a small career-oriented advice."
    menu:
        "How does Tâm take the advice?"

        "Use it seriously":
            $ story_add('career_tam', 2)

        "Feel compared to Thiên An":
            $ story_add('tam_insecurity', 1)

        "Thank her honestly":
            $ story_add('thienan_self_assertion', 1)
    return
