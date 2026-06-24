# FILE: game/story/group/group_c11_social_dinner/s01_invitation.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label group_c11_social_dinner_s01_invitation:
    "MVP: A group dinner/social gathering is arranged after Festival/project work."
    menu:
        "Why does Tâm go?"

        "For Hoàng":
            $ story_add('hoang_tam_trust', 1)

        "For work connections":
            $ story_add('career_tam', 1)

        "To understand Yuuka":
            $ story_add('tam_respect_yuuka', 1)
    return
