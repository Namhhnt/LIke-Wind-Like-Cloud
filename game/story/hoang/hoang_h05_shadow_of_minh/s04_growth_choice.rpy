# FILE: game/story/hoang/hoang_h05_shadow_of_minh/s04_growth_choice.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label hoang_h05_shadow_of_minh_s04_growth_choice:
    "MVP: Hoàng's growth direction is set."
    menu:
        "Hoàng chooses to..."

        "Fight for Tâm with maturity":
            $ story_add('hoang_tam_trust', 2)
            $ story_add_ending_support('e02_tam_hoang')

        "Open his eyes to Huyền":
            $ story_add('hoang_huyen_interest', 2)
            $ story_add_direction('hoang', 'hoang_huyen_open')

        "Stand on his own first":
            $ story_add('hoang_self_acceptance', 3)
            $ story_add_ending_support('e23_hoang_single_growth')
    return
