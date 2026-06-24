# FILE: game/story/tam/tam_c07_minh_at_company/s04_professional_or_personal_choice.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c07_minh_at_company_s04_professional_or_personal_choice:
    "MVP: The chapter decides whether Tâm's Minh thread remains professional or becomes emotionally charged."
    menu:
        "Tâm chooses to..."

        "Learn from Minh professionally":
            $ story_add_direction('tam', 'tam_career_focus')
            $ story_add('career_tam', 2)

        "Admit she is curious about Minh":
            $ story_add_direction('tam', 'tam_minh_open')
            $ story_add('tam_minh_drawn', 2)

        "Invest more clearly in Hoàng":
            $ story_add_direction('tam', 'tam_hoang_commit')
            $ story_add('hoang_tam_trust', 2)
    return
