# FILE: game/story/flashback_minyuu/fb_minyuu_04b_living_together/s02_small_habits.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_04b_living_together_s02_small_habits:
    "MVP Flashback: Affection forms through repeated daily details."
    menu:
        "Which detail matters?"

        "Minh remembers what Yuuka does not eat":
            $ story_add('romantic_score', 1)
            $ story_add('minh_yuuka_trust', 1)

        "Yuuka leaves tea near Minh's desk":
            $ story_add('minh_yuuka_intimacy', 1)
            $ story_add('ex_lover_score', 1)

        "They avoid naming anything":
            $ story_add('minh_yuuka_unresolved', 1)
    return
