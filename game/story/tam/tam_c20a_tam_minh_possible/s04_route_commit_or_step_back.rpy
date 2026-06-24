# FILE: game/story/tam/tam_c20a_tam_minh_possible/s04_route_commit_or_step_back.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c20a_tam_minh_possible_s04_route_commit_or_step_back:
    "MVP: Finalize Tâm's branch seed."
    menu:
        "Confirm Tâm's direction."

        "Tâm-Minh":
            $ story_add_direction('tam', 'tam_minh_commit')
            $ story_add_ending_support('e03_tam_minh')

        "Tâm-Hoàng":
            $ story_add_direction('tam', 'tam_hoang_commit')
            $ story_add_ending_support('e02_tam_hoang')

        "Tâm independent":
            $ story_add_ending_support('e21_tam_independent')
            $ story_add('tam_self_clarity', 2)
    return
