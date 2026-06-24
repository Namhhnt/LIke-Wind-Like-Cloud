# FILE: game/story/tam/tam_c07_minh_at_company/s01_project_briefing.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c07_minh_at_company_s01_project_briefing:
    "MVP: Minh appears as advisor/supervisor for a company project."
    menu:
        "What matters to Tâm in the briefing?"

        "Minh's standards":
            $ story_add('career_tam', 1)
            $ story_add('tam_minh_drawn', 1)

        "Quân's strict management":
            $ story_add('career_huyen', 1)
            $ story_add('huyen_quan_trust', 1)

        "Hoàng's design contribution":
            $ story_add('hoang_professional_credit', 1)
    return
