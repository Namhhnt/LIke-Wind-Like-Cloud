# FILE: game/story/thienan/thienan_c21a_minh_possible/s02_quang_presence.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label thienan_c21a_minh_possible_s02_quang_presence:
    "MVP: Quang's presence provides a grounded alternative."
    menu:
        "How does Thiên An see Quang?"

        "As reliable":
            $ story_add('thienan_quang_trust', 2)

        "As too familiar to notice":
            $ story_add('family_pressure_thienan', 1)

        "As someone she may hurt":
            $ story_add('thienan_self_assertion', 1)
    return
