# FILE: game/story/tam/tam_c20b_admiration_vs_love/s02_minh_is_not_available.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c20b_admiration_vs_love_s02_minh_is_not_available:
    "MVP: The route states clearly that Minh is not available for Tâm in this branch."
    menu:
        "How does Tâm handle the boundary?"

        "Respect it":
            $ story_add('tam_self_clarity', 2)

        "Feel hurt but accept":
            $ story_add('tam_self_clarity', 1)

        "Keep chasing the impossible":
            $ story_add('doom_score', 3)
    return
