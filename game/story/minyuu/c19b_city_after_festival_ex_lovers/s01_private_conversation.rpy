# FILE: game/story/minyuu/c19b_city_after_festival_ex_lovers/s01_private_conversation.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label c19b_city_after_festival_ex_lovers_s01_private_conversation:
    "MVP: Ex-lovers route. Minh and Yuuka finally speak privately."
    menu:
        "Who speaks first?"

        "Yuuka":
            $ story_add('minh_yuuka_trust', 1)

        "Minh":
            $ story_add('minh_yuuka_trust', 1)

        "Neither, at first":
            $ story_add('minh_yuuka_unresolved', 1)
    return
