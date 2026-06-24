# FILE: game/story/tam/tam_c06_minh_returns/s04_unlock_minh_route.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c06_minh_returns_s04_unlock_minh_route:
    "MVP: Minh route visibility is unlocked after his return."
    $ story_flag('minh_route_unlocked')
    menu:
        "What tone should the route take next?"

        "Professional first":
            $ story_add('career_tam', 1)

        "Personal curiosity":
            $ story_add('tam_minh_drawn', 1)

        "Guard the existing Tâm-Hoàng bond":
            $ story_add('hoang_tam_trust', 1)
    return
