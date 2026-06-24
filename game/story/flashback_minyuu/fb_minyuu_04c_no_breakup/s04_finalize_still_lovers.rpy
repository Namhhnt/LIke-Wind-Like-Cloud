# FILE: game/story/flashback_minyuu/fb_minyuu_04c_no_breakup/s04_finalize_still_lovers.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_04c_no_breakup_s04_finalize_still_lovers:
    "MVP: Finalize Minh-Yuuka as still lovers. Other Minh/Yuuka romance routes are locked."
    $ story_set_minyuu_relation('still_lovers')
    menu:
        "What is their present tension?"

        "Keep it private":
            $ story_add_ending_support('e12_minyuu_private_lovers')

        "Eventually acknowledge it":
            $ story_add_ending_support('e13_minyuu_public_lovers')

        "Continue balancing love and distance":
            $ story_add_ending_support('e15_minyuu_long_distance')
    return
