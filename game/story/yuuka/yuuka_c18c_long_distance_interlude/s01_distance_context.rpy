# FILE: game/story/yuuka/yuuka_c18c_long_distance_interlude/s01_distance_context.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label yuuka_c18c_long_distance_interlude_s01_distance_context:
    "MVP: Still-lovers route. Minh and Yuuka are apart, but not broken up."
    menu:
        "What defines the distance?"

        "Career":
            $ story_add_ending_support('e15_minyuu_long_distance')

        "Safety/private life":
            $ story_add_ending_support('e12_minyuu_private_lovers')

        "Timing":
            $ story_add_ending_support('e14_minyuu_non_marriage')
    return
