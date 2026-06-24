# FILE: game/story/flashback_minyuu/fb_minyuu_03_door_left_open/s04_branch_unlock.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_03_door_left_open_s04_branch_unlock:
    "MVP: After this chapter, the route map should show only the compatible Minh-Yuuka verdict chapter."
    menu:
        "Confirm the seeded direction?"

        "Keep this direction":
            $ story_add('minh_yuuka_trust', 1)

        "Make the past more unresolved":
            $ story_add('minh_yuuka_unresolved', 1)
            $ story_add('doom_score', 1)
    return
