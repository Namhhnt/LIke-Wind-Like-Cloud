# FILE: game/story/minyuu/c19a_city_after_festival_old_friends/s01_cafe_or_walk.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label c19a_city_after_festival_old_friends_s01_cafe_or_walk:
    "MVP: Old-friends route. Minh and Yuuka talk after the Festival as people who once knew each other well."
    menu:
        "Where does the talk go?"

        "Career and film":
            $ story_add_ending_support('e19_yuuka_career')

        "Old almost-feelings":
            $ story_add('minh_yuuka_unresolved', 1)

        "Warm friendship":
            $ story_add('minh_yuuka_trust', 2)
            $ story_add_ending_support('e20_minyuu_friendship')
    return
