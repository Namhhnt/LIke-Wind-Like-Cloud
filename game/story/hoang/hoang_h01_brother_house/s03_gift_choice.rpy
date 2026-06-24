# FILE: game/story/hoang/hoang_h01_brother_house/s03_gift_choice.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label hoang_h01_brother_house_s03_gift_choice:
    "MVP: Hoàng chooses the tone of the gift."
    menu:
        "What kind of gift does Hoàng prepare?"

        "Small and thoughtful":
            $ story_add('hoang_tam_trust', 2)
            $ story_add('hoang_self_acceptance', 1)

        "Stylish and expensive":
            $ story_add('hoang_insecurity', 1)

        "Practical for work":
            $ story_add('hoang_professional_credit', 1)
            $ story_add('career_tam', 1)
    return
