# FILE: game/story/thienan/thienan_c21a_minh_possible/s01_old_residue.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label thienan_c21a_minh_possible_s01_old_residue:
    "MVP: Old-friends state only. Thiên An and Minh's old residue can become a possible route."
    menu:
        "What does Thiên An feel?"

        "Old respect":
            $ story_add('thienan_minh_residue', 1)

        "Old longing":
            $ story_add('thienan_minh_residue', 2)

        "A need to move on":
            $ story_add('thienan_self_assertion', 1)
    return
