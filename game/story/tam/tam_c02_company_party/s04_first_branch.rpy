# FILE: game/story/tam/tam_c02_company_party/s04_first_branch.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c02_company_party_s04_first_branch:
    "MVP: The party sets the first social direction."
    menu:
        "What does Tâm do before leaving?"

        "Exchange contact with Hoàng":
            $ story_add('hoang_tam_trust', 2)
            $ story_add_direction('tam', 'tam_hoang_open')

        "Let Huyền keep teasing Hoàng":
            $ story_add('huyen_hoang_interest', 1)
            $ story_add('hoang_huyen_interest', 1)

        "Leave early to rest for work":
            $ story_add('career_tam', 2)
    return
