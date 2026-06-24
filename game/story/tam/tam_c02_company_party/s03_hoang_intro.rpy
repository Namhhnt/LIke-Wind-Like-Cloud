# FILE: game/story/tam/tam_c02_company_party/s03_hoang_intro.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c02_company_party_s03_hoang_intro:
    "MVP: Hoàng is introduced as a young architect/designer connected to the company project."
    menu:
        "Who opens the conversation?"

        "Tâm approaches Hoàng":
            $ story_add('tam_hoang_interest', 2)
            $ story_add('hoang_tam_trust', 2)
            $ story_add_direction('tam', 'tam_hoang_open')

        "Hoàng approaches Tâm first":
            $ story_add('tam_hoang_interest', 1)
            $ story_add('hoang_tam_trust', 1)
            $ story_add_direction('hoang', 'hoang_tam_open')

        "Huyền talks to Hoàng first":
            $ story_add('huyen_hoang_interest', 2)
            $ story_add('hoang_huyen_interest', 1)
            $ story_add_direction('huyen', 'huyen_hoang_open')

        "No meaningful conversation happens":
            $ story_add('career_tam', 1)
    return
