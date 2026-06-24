# FILE: game/story/flashback_minyuu/fb_minyuu_04c_no_breakup/s03_private_or_public_seed.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_04c_no_breakup_s03_private_or_public_seed:
    "MVP Flashback: The route chooses whether their love stays private or may become public."
    menu:
        "What future seed is created?"

        "Private lovers":
            $ story_add_ending_support('e12_minyuu_private_lovers')

        "Public later":
            $ story_add_ending_support('e13_minyuu_public_lovers')

        "No marriage, still together":
            $ story_add_ending_support('e14_minyuu_non_marriage')
    return
