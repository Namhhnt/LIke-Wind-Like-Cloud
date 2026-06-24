# FILE: game/story/minyuu/c19c_city_after_festival_still_lovers/s01_lovers_reunion.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label c19c_city_after_festival_still_lovers_s01_lovers_reunion:
    "MVP: Still-lovers route. Minh and Yuuka meet privately as people who never truly broke up."
    menu:
        "What is the emotional tone?"

        "Quiet certainty":
            $ story_add_ending_support('e12_minyuu_private_lovers')

        "Need for acknowledgment":
            $ story_add_ending_support('e13_minyuu_public_lovers')

        "Career-first distance":
            $ story_add_ending_support('e15_minyuu_long_distance')
    return
