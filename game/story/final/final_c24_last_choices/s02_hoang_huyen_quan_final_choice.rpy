# FILE: game/story/final/final_c24_last_choices/s02_hoang_huyen_quan_final_choice.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label final_c24_last_choices_s02_hoang_huyen_quan_final_choice:
    "MVP: Final Hoàng/Huyền/Quân choice."
    menu:
        "Side relationship final direction:"

        "Huyền-Quân":
            $ story_add_ending_support('e05_huyen_quan')
            $ story_add('huyen_quan_trust', 2)

        "Hoàng-Huyền" if not story_has_direction('tam', 'tam_hoang_commit'):
            $ story_add_ending_support('e04_hoang_huyen')
            $ story_add('hoang_huyen_interest', 2)
            $ story_add('huyen_hoang_interest', 2)

        "Huyền independent":
            $ story_add_ending_support('e22_huyen_independent')
            $ story_add('career_huyen', 2)

        "Hoàng single growth":
            $ story_add_ending_support('e23_hoang_single_growth')
            $ story_add('hoang_self_acceptance', 2)
    return
