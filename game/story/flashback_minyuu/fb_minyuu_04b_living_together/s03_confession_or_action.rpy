# FILE: game/story/flashback_minyuu/fb_minyuu_04b_living_together/s03_confession_or_action.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_04b_living_together_s03_confession_or_action:
    "MVP Flashback: The relationship becomes romantic."
    menu:
        "How is love confirmed?"

        "Yuuka says it first":
            $ story_add('ex_lover_score', 2)
            $ story_add('minh_yuuka_intimacy', 1)

        "Minh confirms through action":
            $ story_add('ex_lover_score', 2)
            $ story_add('minh_yuuka_trust', 1)

        "They both avoid the word but live as lovers":
            $ story_add('minh_yuuka_unresolved', 1)
            $ story_add('ex_lover_score', 1)
    return
