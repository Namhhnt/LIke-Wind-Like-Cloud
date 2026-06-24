# FILE: game/story/minyuu/minyuu_c23c_still_lovers_resolution/s01_define_relationship.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label minyuu_c23c_still_lovers_resolution_s01_define_relationship:
    "MVP: Still-lovers route. Minh and Yuuka define the shape of an ongoing relationship."
    menu:
        "What needs definition?"

        "Privacy":
            $ story_add_ending_support('e12_minyuu_private_lovers')

        "Visibility":
            $ story_add_ending_support('e13_minyuu_public_lovers')

        "Marriage expectations":
            $ story_add_ending_support('e14_minyuu_non_marriage')

        "Distance":
            $ story_add_ending_support('e15_minyuu_long_distance')
    return
