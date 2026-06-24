# FILE: game/story/yuuka/yuuka_c18a_career_interlude/s02_yuuka_career_choice.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label yuuka_c18a_career_interlude_s02_yuuka_career_choice:
    "MVP: Yuuka chooses how much career should define this route."
    menu:
        "Yuuka chooses..."

        "Career first":
            $ story_add_ending_support('e19_yuuka_career')

        "Friendship and career balanced":
            $ story_add_ending_support('e20_minyuu_friendship')

        "Leave romance unforced":
            $ story_add_ending_support('e17_yuuka_single')
    return
