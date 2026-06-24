# FILE: game/story/tam/tam_c20b_admiration_vs_love/s03_tam_self_clarity_choice.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c20b_admiration_vs_love_s03_tam_self_clarity_choice:
    "MVP: Tâm chooses her own direction after recognizing Minh's boundary."
    menu:
        "Tâm chooses..."

        "Repair with Hoàng":
            $ story_add('hoang_tam_trust', 3)
            $ story_add_ending_support('e02_tam_hoang')

        "Choose independence":
            $ story_add('tam_self_clarity', 2)
            $ story_add_ending_support('e21_tam_independent')

        "Avoid both choices":
            $ story_add('doom_score', 3)
            $ story_add_ending_support('e24_doom')
    return
