# FILE: game/story/yuuka/yuuka_c18a_career_interlude/s03_friendship_balance.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label yuuka_c18a_career_interlude_s03_friendship_balance:
    "MVP: Yuuka and Minh's old friendship remains warm but not binding."
    menu:
        "What is the emotional conclusion?"

        "A clean friendship":
            $ story_add('minh_yuuka_trust', 2)
            $ story_add_ending_support('e20_minyuu_friendship')

        "An open life ahead":
            $ story_add_ending_support('e17_yuuka_single')

        "A career-forward ending seed":
            $ story_add_ending_support('e19_yuuka_career')
    return
