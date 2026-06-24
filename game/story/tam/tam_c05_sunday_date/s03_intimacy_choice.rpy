# FILE: game/story/tam/tam_c05_sunday_date/s03_intimacy_choice.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c05_sunday_date_s03_intimacy_choice:
    "MVP: A small moment asks whether the relationship deepens."
    menu:
        "How close does the moment become?"

        "Tâm lets Hoàng closer":
            $ story_add('hoang_tam_trust', 2)

        "Tâm keeps it light":
            $ story_add('tam_self_clarity', 1)

        "Huyền interrupts with a joke":
            $ story_add('huyen_hoang_interest', 1)
    return
