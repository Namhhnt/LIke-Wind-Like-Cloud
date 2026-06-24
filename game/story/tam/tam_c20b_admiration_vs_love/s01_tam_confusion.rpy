# FILE: game/story/tam/tam_c20b_admiration_vs_love/s01_tam_confusion.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c20b_admiration_vs_love_s01_tam_confusion:
    "MVP: Minh is emotionally unavailable because of Yuuka. Tâm must separate admiration from love."
    menu:
        "What does Tâm admit?"

        "She admired Minh":
            $ story_add('tam_self_clarity', 2)

        "She was using Minh to avoid another feeling":
            $ story_add('tam_self_clarity', 2)
            $ story_add('hoang_tam_trust', 1)

        "She still avoids the truth":
            $ story_add('doom_score', 2)
    return
