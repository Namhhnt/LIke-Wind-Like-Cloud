# FILE: game/story/minyuu/c19c_city_after_festival_still_lovers/s02_private_or_public.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label c19c_city_after_festival_still_lovers_s02_private_or_public:
    "MVP: They discuss whether to remain private or become more visible."
    menu:
        "What shape do they choose?"

        "Stay private":
            $ story_add_ending_support('e12_minyuu_private_lovers')

        "Tell the close circle":
            $ story_add_ending_support('e13_minyuu_public_lovers')

        "Keep commitment without marriage pressure":
            $ story_add_ending_support('e14_minyuu_non_marriage')
    return
