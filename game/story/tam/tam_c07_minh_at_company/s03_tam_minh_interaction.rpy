# FILE: game/story/tam/tam_c07_minh_at_company/s03_tam_minh_interaction.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c07_minh_at_company_s03_tam_minh_interaction:
    "MVP: Tâm and Minh have a short one-on-one professional exchange."
    menu:
        "Where does the exchange lean?"

        "Professional respect":
            $ story_add('career_tam', 2)

        "Quiet personal curiosity":
            $ story_add('tam_minh_drawn', 2)

        "Tâm steps back because of Hoàng":
            $ story_add('hoang_tam_trust', 1)
            $ story_add('tam_self_clarity', 1)
    return
