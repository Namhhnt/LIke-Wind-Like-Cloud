# FILE: game/story/flashback_minyuu/fb_minyuu_02_working_rhythm/s04_score_branch.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label fb_minyuu_02_working_rhythm_s04_score_branch:
    "MVP Flashback: The relationship direction remains open but gains weight."
    menu:
        "What does this period become?"

        "A strong friendship":
            $ story_add('old_friend_score', 2)

        "A romance beginning before they name it":
            $ story_add('romantic_score', 2)
            $ story_add('ex_lover_score', 1)

        "A bond that already feels committed":
            $ story_add('romantic_score', 1)
            $ story_add('still_lover_score', 2)
    return
