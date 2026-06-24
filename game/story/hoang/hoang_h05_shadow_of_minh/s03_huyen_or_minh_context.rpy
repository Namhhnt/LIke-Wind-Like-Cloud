# FILE: game/story/hoang/hoang_h05_shadow_of_minh/s03_huyen_or_minh_context.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label hoang_h05_shadow_of_minh_s03_huyen_or_minh_context:
    "MVP: The scene can redirect Hoàng toward Tâm, Huyền, or self-growth."
    menu:
        "What does Hoàng learn?"

        "Tâm needs patience":
            $ story_add('hoang_tam_trust', 1)
            $ story_add('hoang_self_acceptance', 1)

        "Huyền sees him clearly":
            $ story_add('hoang_huyen_interest', 2)
            $ story_add('huyen_hoang_interest', 1)

        "He must stop competing with Minh":
            $ story_add('hoang_self_acceptance', 2)
    return
