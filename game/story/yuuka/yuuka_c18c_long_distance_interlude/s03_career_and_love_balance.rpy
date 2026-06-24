# FILE: game/story/yuuka/yuuka_c18c_long_distance_interlude/s03_career_and_love_balance.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label yuuka_c18c_long_distance_interlude_s03_career_and_love_balance:
    "MVP: Yuuka decides what shape the ongoing relationship can take."
    menu:
        "Yuuka chooses..."

        "Keep private love":
            $ story_add_ending_support('e12_minyuu_private_lovers')

        "Let close people know":
            $ story_add_ending_support('e13_minyuu_public_lovers')

        "Keep love without marriage pressure":
            $ story_add_ending_support('e14_minyuu_non_marriage')

        "Continue long-distance":
            $ story_add_ending_support('e15_minyuu_long_distance')
    return
