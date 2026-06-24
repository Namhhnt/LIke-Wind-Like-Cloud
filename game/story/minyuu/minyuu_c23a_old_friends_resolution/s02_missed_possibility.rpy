# FILE: game/story/minyuu/minyuu_c23a_old_friends_resolution/s02_missed_possibility.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label minyuu_c23a_old_friends_resolution_s02_missed_possibility:
    "MVP: They acknowledge a missed possibility without turning it into romance."
    menu:
        "How do they name it?"

        "A beautiful almost":
            $ story_add_ending_support('e20_minyuu_friendship')

        "Something released":
            $ story_add_ending_support('e16_minh_single')
            $ story_add_ending_support('e17_yuuka_single')

        "Something that made Yuuka stronger":
            $ story_add_ending_support('e19_yuuka_career')
    return
