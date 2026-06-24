# FILE: game/story/minyuu/c19a_city_after_festival_old_friends/s02_old_almost_question.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label c19a_city_after_festival_old_friends_s02_old_almost_question:
    "MVP: Yuuka asks whether they once missed something."
    menu:
        "How does Minh answer?"

        "Honestly, but without romance":
            $ story_add('minh_yuuka_trust', 1)
            $ story_add_ending_support('e20_minyuu_friendship')

        "Avoid the question":
            $ story_add('doom_score', 1)

        "Admit the possibility but release it":
            $ story_add_ending_support('e17_yuuka_single')
            $ story_add_ending_support('e16_minh_single')
    return
