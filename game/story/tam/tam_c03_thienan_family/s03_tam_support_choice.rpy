# FILE: game/story/tam/tam_c03_thienan_family/s03_tam_support_choice.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c03_thienan_family_s03_tam_support_choice:
    "MVP: Tâm and Thiên An have a private moment."
    menu:
        "What does Tâm ask?"

        "Ask if Thiên An is happy":
            $ story_add('thienan_self_assertion', 1)
            $ story_flag('tam_asked_thienan_happiness')

        "Ask about Minh, vaguely":
            $ story_add('thienan_minh_residue', 1)
            $ story_flag('tam_heard_minh_hint')

        "Ask nothing and sit with her":
            $ story_add('thienan_quang_trust', 1)
    return
