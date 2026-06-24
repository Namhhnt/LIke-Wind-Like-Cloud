# FILE: game/story/minyuu/minyuu_c23b_ex_lovers_resolution/s01_no_more_running.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label minyuu_c23b_ex_lovers_resolution_s01_no_more_running:
    "MVP: Ex-lovers route. Yuuka and Minh stop running from the old wound."
    menu:
        "Who stops first?"

        "Yuuka":
            $ story_add('minh_yuuka_trust', 1)

        "Minh":
            $ story_add('minh_yuuka_trust', 1)

        "Both, awkwardly":
            $ story_add('minh_yuuka_trust', 2)
    return
