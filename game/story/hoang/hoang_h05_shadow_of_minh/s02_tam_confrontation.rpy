# FILE: game/story/hoang/hoang_h05_shadow_of_minh/s02_tam_confrontation.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label hoang_h05_shadow_of_minh_s02_tam_confrontation:
    "MVP: Tâm and Hoàng confront emotional ambiguity."
    menu:
        "How honest is Tâm?"

        "Tell Hoàng she felt confused":
            $ story_add('hoang_tam_trust', 2)
            $ story_add('tam_self_clarity', 1)

        "Avoid the topic":
            $ story_add('doom_score', 2)
            $ story_add('hoang_insecurity', 1)

        "Say she chooses Hoàng":
            $ story_add('hoang_tam_trust', 3)
            $ story_add_direction('tam', 'tam_hoang_commit')
            $ story_add_ending_support('e02_tam_hoang')
    return
