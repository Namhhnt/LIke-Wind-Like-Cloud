# FILE: game/story/prologue/prologue_rain_dream/s03_tell_or_hide.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label prologue_rain_dream_s03_tell_or_hide:
    "MVP: Tâm has a chance to tell Huyền about the strange dream."
    menu:
        "Does Tâm tell Huyền?"

        "Tell Huyền":
            $ story_flag('huyen_knows_dream')
            $ story_add('career_huyen', 1)

        "Keep it private":
            $ story_flag('tam_keeps_dream_private')
            $ story_add('tam_self_clarity', 1)

        "Joke about it":
            $ story_flag('huyen_teases_dream')
            $ story_add('tam_hoang_interest', 1)
    return
