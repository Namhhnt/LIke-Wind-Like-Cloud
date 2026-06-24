# FILE: game/story/flashback_minyuu/fb_minyuu_04a_old_friends/s03_finalize_old_friends.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_04a_old_friends_s03_finalize_old_friends:
    "MVP: Finalize Minh-Yuuka as old close friends."
    $ story_set_minyuu_relation('old_close_friends')
    $ story_add_ending_support('e20_minyuu_friendship')
    menu:
        "What does this unlock emotionally?"

        "Minh is free to love someone else later":
            $ story_flag('minh_romance_open_after_yuuka')

        "Yuuka keeps her own path":
            $ story_add_ending_support('e19_yuuka_career')

        "Both keep a warm old friendship":
            $ story_add('minh_yuuka_trust', 2)
    return
