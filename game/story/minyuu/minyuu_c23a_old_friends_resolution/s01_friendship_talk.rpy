# FILE: game/story/minyuu/minyuu_c23a_old_friends_resolution/s01_friendship_talk.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label minyuu_c23a_old_friends_resolution_s01_friendship_talk:
    "MVP: Old-friends route. Minh and Yuuka define the old friendship."
    menu:
        "What do they keep?"

        "Respect":
            $ story_add('minh_yuuka_trust', 1)
            $ story_add_ending_support('e20_minyuu_friendship')

        "Distance":
            $ story_add_ending_support('e16_minh_single')

        "Yuuka's career focus":
            $ story_add_ending_support('e19_yuuka_career')
    return
