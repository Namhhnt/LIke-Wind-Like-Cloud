# FILE: game/story/flashback_minyuu/fb_minyuu_03_door_left_open/s02_help_choice.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_03_door_left_open_s02_help_choice:
    "MVP Flashback: Minh chooses the shape of help."
    menu:
        "How does Minh help?"

        "Find Yuuka a safe place elsewhere":
            $ story_add('old_friend_score', 3)
            $ story_add('boundary_score', 2)
            $ story_add_direction('minyuu', 'old_friend_seed')

        "Let Yuuka stay temporarily":
            $ story_add('romantic_score', 2)
            $ story_add('ex_lover_score', 2)
            $ story_add_direction('minyuu', 'ex_lover_seed')

        "They are already emotionally committed":
            $ story_add('romantic_score', 3)
            $ story_add('still_lover_score', 3)
            $ story_add_direction('minyuu', 'still_lover_seed')
    return
