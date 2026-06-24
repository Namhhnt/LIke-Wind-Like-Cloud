# FILE: game/story/yuuka/yuuka_c18c_long_distance_interlude/s02_private_messages.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label yuuka_c18c_long_distance_interlude_s02_private_messages:
    "MVP: Their connection survives through sparse but precise contact."
    menu:
        "What kind of message matters?"

        "A practical reminder":
            $ story_add('minh_yuuka_trust', 1)
            $ story_add_ending_support('e12_minyuu_private_lovers')

        "A career encouragement":
            $ story_add_ending_support('e15_minyuu_long_distance')

        "A quiet promise":
            $ story_add_ending_support('e13_minyuu_public_lovers')
    return
