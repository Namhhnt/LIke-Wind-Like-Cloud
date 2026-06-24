# FILE: game/story/minyuu/c19a_city_after_festival_old_friends/s03_friendship_resolution_choice.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label c19a_city_after_festival_old_friends_s03_friendship_resolution_choice:
    "MVP: Old-friends route resolution seed."
    menu:
        "What remains after the walk?"

        "Friendship ending seed":
            $ story_add_ending_support('e20_minyuu_friendship')

        "Yuuka career ending seed":
            $ story_add_ending_support('e19_yuuka_career')

        "Minh single seed":
            $ story_add_ending_support('e16_minh_single')
    return
