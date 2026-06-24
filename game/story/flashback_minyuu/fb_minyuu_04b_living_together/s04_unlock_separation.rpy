# FILE: game/story/flashback_minyuu/fb_minyuu_04b_living_together/s04_unlock_separation.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_04b_living_together_s04_unlock_separation:
    "MVP: This route now requires a separation chapter to finalize as ex lovers."
    $ story_add_direction('minyuu', 'ex_lovers_need_separation')
    menu:
        "What pressure enters the relationship?"

        "Career distance":
            $ story_add('minh_yuuka_unresolved', 1)

        "Minh's responsibility":
            $ story_add('boundary_score', 1)

        "Yuuka's fear of being held back":
            $ story_add('minh_yuuka_unresolved', 1)
    return
