# FILE: game/story/group/group_c11_social_dinner/s02_group_table.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label group_c11_social_dinner_s02_group_table:
    "MVP: The group table includes Tâm, Huyền, Hoàng, Minh, and Yuuka."
    menu:
        "Who anchors the table?"

        "Hoàng keeps it warm":
            $ story_add('hoang_self_acceptance', 1)

        "Huyền keeps it light":
            $ story_add('career_huyen', 1)

        "Minh keeps it practical":
            $ story_add('career_tam', 1)
    return
