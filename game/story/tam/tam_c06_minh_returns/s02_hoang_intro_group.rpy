# FILE: game/story/tam/tam_c06_minh_returns/s02_hoang_intro_group.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c06_minh_returns_s02_hoang_intro_group:
    "MVP: Hoàng introduces Tâm/Huyền to Minh depending on current social route."
    menu:
        "How does Hoàng introduce them?"

        "As Tâm, someone important":
            $ story_add('hoang_tam_trust', 1)
            $ story_add('hoang_insecurity', 1)

        "As friends from work":
            $ story_add('career_tam', 1)

        "Let Huyền carry the conversation":
            $ story_add('career_huyen', 1)
    return
