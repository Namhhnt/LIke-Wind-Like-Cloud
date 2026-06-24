# FILE: game/story/huyen/huyen_c22_quan_or_hoang/s04_huyen_choice.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label huyen_c22_quan_or_hoang_s04_huyen_choice:
    "MVP: Huyền's ending seed is confirmed."
    menu:
        "Huyền chooses..."

        "Quân":
            $ story_add_ending_support('e05_huyen_quan')
            $ story_add('huyen_quan_trust', 2)

        "Hoàng":
            $ story_add_ending_support('e04_hoang_huyen')
            $ story_add('hoang_huyen_interest', 2)
            $ story_add('huyen_hoang_interest', 2)

        "Independence":
            $ story_add_ending_support('e22_huyen_independent')
            $ story_add('career_huyen', 3)
    return
