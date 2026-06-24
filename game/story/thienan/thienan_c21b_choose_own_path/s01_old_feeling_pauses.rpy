# FILE: game/story/thienan/thienan_c21b_choose_own_path/s01_old_feeling_pauses.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label thienan_c21b_choose_own_path_s01_old_feeling_pauses:
    "MVP: Minh is not available. Thiên An may pause at old feelings, but this is not a romance route."
    menu:
        "What does the pause become?"

        "Closure":
            $ story_add('thienan_self_assertion', 2)

        "Frustration":
            $ story_add('doom_score', 1)

        "A quiet goodbye to the old self":
            $ story_add('thienan_self_assertion', 2)
    return
