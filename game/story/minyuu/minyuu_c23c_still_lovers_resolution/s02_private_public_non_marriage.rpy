# FILE: game/story/minyuu/minyuu_c23c_still_lovers_resolution/s02_private_public_non_marriage.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label minyuu_c23c_still_lovers_resolution_s02_private_public_non_marriage:
    "MVP: They choose relationship form."
    menu:
        "Choose relationship form:"

        "Private lovers":
            $ story_add_ending_support('e12_minyuu_private_lovers')

        "Public lovers":
            $ story_add_ending_support('e13_minyuu_public_lovers')

        "Non-marriage lovers":
            $ story_add_ending_support('e14_minyuu_non_marriage')

        "Long-distance lovers":
            $ story_add_ending_support('e15_minyuu_long_distance')
    return
