# FILE: game/story/hoang/hoang_h01_brother_house/s01_villa_intro.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label hoang_h01_brother_house_s01_villa_intro:
    "MVP: Hoàng is shown living in Minh's villa, under the quiet shadow of his older brother."
    menu:
        "What does Hoàng feel tonight?"

        "Comfort in the house":
            $ story_add('hoang_self_acceptance', 1)

        "Pressure from Minh's shadow":
            $ story_add('hoang_insecurity', 1)

        "Restlessness about his own path":
            $ story_add('hoang_professional_credit', 1)
    return
