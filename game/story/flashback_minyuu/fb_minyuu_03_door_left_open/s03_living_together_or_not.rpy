# FILE: game/story/flashback_minyuu/fb_minyuu_03_door_left_open/s03_living_together_or_not.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_03_door_left_open_s03_living_together_or_not:
    "MVP Flashback: The route branch is now seeded."
    if story_has_direction('minyuu', 'old_friend_seed'):
        "MVP: Old friends branch seeded."
    elif story_has_direction('minyuu', 'ex_lover_seed'):
        "MVP: Ex lovers branch seeded."
    elif story_has_direction('minyuu', 'still_lover_seed'):
        "MVP: Still lovers branch seeded."
    else:
        "MVP: No seed detected; defaulting to old friends."
        $ story_add_direction('minyuu', 'old_friend_seed')
    return
