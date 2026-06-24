# FILE: game/story/tam/tam_c20a_tam_minh_possible/s02_minh_boundary_or_openness.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c20a_tam_minh_possible_s02_minh_boundary_or_openness:
    "MVP: Minh can either keep boundary or open slightly because Yuuka is only an old friend in this route."
    menu:
        "How does Minh respond?"

        "Open slightly":
            $ story_add('tam_minh_drawn', 2)

        "Keep a respectful boundary":
            $ story_add('tam_self_clarity', 1)

        "Avoid the topic":
            $ story_add('doom_score', 1)
    return
