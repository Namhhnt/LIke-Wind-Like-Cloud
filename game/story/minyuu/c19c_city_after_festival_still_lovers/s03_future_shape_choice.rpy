# FILE: game/story/minyuu/c19c_city_after_festival_still_lovers/s03_future_shape_choice.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label c19c_city_after_festival_still_lovers_s03_future_shape_choice:
    "MVP: Still-lovers route selects future shape."
    menu:
        "Future shape:"

        "Private lovers":
            $ story_add_ending_support('e12_minyuu_private_lovers')

        "Public lovers":
            $ story_add_ending_support('e13_minyuu_public_lovers')

        "Non-marriage lovers":
            $ story_add_ending_support('e14_minyuu_non_marriage')

        "Long-distance lovers":
            $ story_add_ending_support('e15_minyuu_long_distance')
    return
