# FILE: game/story/huyen/huyen_c22_quan_or_hoang/s03_hoang_huyen_option.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label huyen_c22_quan_or_hoang_s03_hoang_huyen_option:
    "MVP: Hoàng-Huyền can open if Tâm-Hoàng is not committed."
    menu:
        "What happens between Hoàng and Huyền?"

        "They notice each other clearly":
            $ story_add('hoang_huyen_interest', 2)
            $ story_add('huyen_hoang_interest', 2)
            $ story_add_direction('huyen', 'huyen_hoang_commit')
            $ story_add_ending_support('e04_hoang_huyen')

        "They stay friends":
            $ story_add('career_huyen', 1)

        "They avoid the tension":
            $ story_add('doom_score', 1)
    return
