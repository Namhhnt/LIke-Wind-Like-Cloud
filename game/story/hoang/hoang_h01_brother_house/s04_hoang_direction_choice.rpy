# FILE: game/story/hoang/hoang_h01_brother_house/s04_hoang_direction_choice.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label hoang_h01_brother_house_s04_hoang_direction_choice:
    "MVP: Hoàng decides how directly he wants to approach his feelings."
    menu:
        "Hoàng chooses to..."

        "Ask Tâm out clearly":
            $ story_add_direction('hoang', 'hoang_tam_pursue')
            $ story_add('hoang_tam_trust', 2)

        "Keep things friendly":
            $ story_add_direction('hoang', 'hoang_friend_group')
            $ story_add('hoang_self_acceptance', 1)

        "Notice Huyền more than expected":
            $ story_add_direction('hoang', 'hoang_huyen_open')
            $ story_add('hoang_huyen_interest', 2)
    return
