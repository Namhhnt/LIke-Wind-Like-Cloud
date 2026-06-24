# FILE: game/story/huyen/huyen_c22_quan_or_hoang/s01_huyen_route_check.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label huyen_c22_quan_or_hoang_s01_huyen_route_check:
    "MVP: Huyền's route checks whether Quân, Hoàng, or independence is strongest."
    menu:
        "Where does Huyền's attention go?"

        "Quân":
            $ story_add('huyen_quan_trust', 2)

        "Hoàng":
            $ story_add('huyen_hoang_interest', 2)
            $ story_add('hoang_huyen_interest', 2)

        "Her own work":
            $ story_add('career_huyen', 2)
    return
