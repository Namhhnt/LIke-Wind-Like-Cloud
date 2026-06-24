# FILE: game/story/minyuu/minyuu_c23a_old_friends_resolution/s03_friendship_or_late_possibility.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label minyuu_c23a_old_friends_resolution_s03_friendship_or_late_possibility:
    "MVP: Old-friends resolution final seed."
    menu:
        "Final old-friends direction:"

        "Friendship ending":
            $ story_add_ending_support('e20_minyuu_friendship')
            $ story_add('minh_yuuka_trust', 2)

        "Yuuka career ending":
            $ story_add_ending_support('e19_yuuka_career')

        "Separate single paths":
            $ story_add_ending_support('e16_minh_single')
            $ story_add_ending_support('e17_yuuka_single')
    return
