# FILE: game/story/tam/tam_c02_company_party/s01_company_rumors_about_quan.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c02_company_party_s01_company_rumors_about_quan:
    "MVP: Tâm and Huyền hear rumors about Quân: competent, strict, hard to impress."
    menu:
        "How does Tâm receive the rumor?"

        "Prepare seriously":
            $ story_add('career_tam', 1)

        "Let Huyền joke about it":
            $ story_add('career_huyen', 1)

        "Feel intimidated":
            $ story_add('doom_score', 1)
    return
