# FILE: game/story/tam/tam_c07_minh_at_company/s02_minh_as_advisor.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c07_minh_at_company_s02_minh_as_advisor:
    "MVP: Minh corrects the team's direction with precise comments."
    menu:
        "How does Tâm respond to Minh's correction?"

        "Accept and revise":
            $ story_add('career_tam', 2)

        "Ask a direct follow-up":
            $ story_add('tam_minh_drawn', 1)
            $ story_add('career_tam', 1)

        "Feel embarrassed":
            $ story_add('tam_insecurity', 1)
    return
