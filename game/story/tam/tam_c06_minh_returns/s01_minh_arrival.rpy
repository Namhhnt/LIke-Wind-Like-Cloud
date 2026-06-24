# FILE: game/story/tam/tam_c06_minh_returns/s01_minh_arrival.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c06_minh_returns_s01_minh_arrival:
    "MVP: Minh returns to Vietnam."
    menu:
        "How is Minh first framed?"

        "Through Hoàng's respect":
            $ story_add('hoang_insecurity', 1)

        "Through professional reputation":
            $ story_add('career_tam', 1)

        "Through Tâm's strange recognition":
            $ story_add('tam_minh_drawn', 1)
    return
