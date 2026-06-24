# FILE: game/story/yuuka/yuuka_c18a_career_interlude/s01_festival_afterglow.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label yuuka_c18a_career_interlude_s01_festival_afterglow:
    "MVP: Old-friends route. Yuuka processes the Festival as a career milestone."
    menu:
        "What does Yuuka value most?"

        "Her film finding viewers":
            $ story_add_ending_support('e19_yuuka_career')

        "The old friendship with Minh":
            $ story_add('minh_yuuka_trust', 1)
            $ story_add_ending_support('e20_minyuu_friendship')

        "Her independence":
            $ story_add_ending_support('e17_yuuka_single')
    return
