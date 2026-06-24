# FILE: game/story/tam/tam_c20a_tam_minh_possible/s01_tam_recognizes_interest.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c20a_tam_minh_possible_s01_tam_recognizes_interest:
    "MVP: Old-friends state only. Tâm can examine whether her feeling for Minh is real love."
    menu:
        "What does Tâm recognize?"

        "A real pull toward Minh":
            $ story_add('tam_minh_drawn', 2)

        "Admiration, not love":
            $ story_add('tam_self_clarity', 2)

        "Confusion she keeps avoiding":
            $ story_add('doom_score', 1)
    return
