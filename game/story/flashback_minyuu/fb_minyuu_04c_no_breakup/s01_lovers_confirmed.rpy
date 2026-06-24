# FILE: game/story/flashback_minyuu/fb_minyuu_04c_no_breakup/s01_lovers_confirmed.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_04c_no_breakup_s01_lovers_confirmed:
    "MVP Flashback: Minh and Yuuka are confirmed as lovers."
    menu:
        "How is the relationship confirmed?"

        "Privately and quietly":
            $ story_add('still_lover_score', 2)
            $ story_add('minh_yuuka_trust', 1)

        "By mutual promise":
            $ story_add('still_lover_score', 2)
            $ story_add('minh_yuuka_intimacy', 1)

        "Through everyday certainty":
            $ story_add('still_lover_score', 1)
            $ story_add('romantic_score', 1)
    return
