# FILE: game/story/tam/tam_c06_minh_returns/s03_tam_reaction.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c06_minh_returns_s03_tam_reaction:
    "MVP: Tâm reacts to Minh's presence."
    menu:
        "What does Tâm do?"

        "Leave early because something feels off":
            $ story_add('tam_minh_drawn', 1)
            $ story_add('doom_score', 1)

        "Stay and observe":
            $ story_add('tam_observation', 2)

        "Focus on Hoàng instead":
            $ story_add('hoang_tam_trust', 2)
    return
