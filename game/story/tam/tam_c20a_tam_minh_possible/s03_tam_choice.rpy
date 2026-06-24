# FILE: game/story/tam/tam_c20a_tam_minh_possible/s03_tam_choice.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c20a_tam_minh_possible_s03_tam_choice:
    "MVP: Tâm chooses whether to move toward Minh."
    menu:
        "Tâm chooses..."

        "Commit to exploring Minh route":
            $ story_add_direction('tam', 'tam_minh_commit')
            $ story_add_ending_support('e03_tam_minh')
            $ story_add('tam_minh_drawn', 2)

        "Step back and choose Hoàng":
            $ story_add_direction('tam', 'tam_hoang_commit')
            $ story_add_ending_support('e02_tam_hoang')
            $ story_add('hoang_tam_trust', 2)

        "Choose herself":
            $ story_add_ending_support('e21_tam_independent')
            $ story_add('tam_self_clarity', 2)
    return
