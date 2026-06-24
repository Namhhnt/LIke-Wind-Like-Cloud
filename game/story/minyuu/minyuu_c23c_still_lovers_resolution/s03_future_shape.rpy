# FILE: game/story/minyuu/minyuu_c23c_still_lovers_resolution/s03_future_shape.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label minyuu_c23c_still_lovers_resolution_s03_future_shape:
    "MVP: Still-lovers final ending seed."
    menu:
        "Final still-lovers direction:"

        "Keep private":
            $ story_add_ending_support('e12_minyuu_private_lovers')

        "Acknowledge publicly":
            $ story_add_ending_support('e13_minyuu_public_lovers')

        "Choose each other without marriage":
            $ story_add_ending_support('e14_minyuu_non_marriage')

        "Keep loving across distance":
            $ story_add_ending_support('e15_minyuu_long_distance')
    return
