# FILE: game/story/tam/tam_c05_sunday_date/s02_date_or_group.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c05_sunday_date_s02_date_or_group:
    "MVP: The outing begins."
    menu:
        "What shape does the outing take?"

        "Tâm and Hoàng spend time privately":
            $ story_add('hoang_tam_trust', 2)
            $ story_add_direction('tam', 'tam_hoang_open')

        "Hoàng and Huyền accidentally pair up":
            $ story_add('hoang_huyen_interest', 2)
            $ story_add('huyen_hoang_interest', 2)

        "The three keep it casual":
            $ story_add('career_tam', 1)
            $ story_add('career_huyen', 1)
    return
