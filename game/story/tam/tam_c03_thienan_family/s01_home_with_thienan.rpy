# FILE: game/story/tam/tam_c03_thienan_family/s01_home_with_thienan.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c03_thienan_family_s01_home_with_thienan:
    "MVP: Thiên An is introduced as Tâm's older sister: capable, controlled, and under family pressure."
    menu:
        "How does Tâm see Thiên An tonight?"

        "As someone strong but tired":
            $ story_add('thienan_self_assertion', 1)

        "As someone impossible to reach":
            $ story_add('tam_insecurity', 1)

        "As someone she wants to support":
            $ story_flag('tam_supports_thienan')
            $ story_add('thienan_quang_trust', 1)
    return
