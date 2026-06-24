# FILE: game/story/prologue/prologue_rain_dream/s01_rain_meeting.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label prologue_rain_dream_s01_rain_meeting:
    "MVP: Tâm dreams of a rainy street and a quiet man whose face she cannot fully remember."
    menu:
        "What remains after the dream?"

        "The man's face":
            $ story_add('tam_minh_drawn', 1)
            $ story_flag('dream_remembered_face')

        "The sound of rain":
            $ story_add('tam_self_clarity', 1)
            $ story_flag('dream_remembered_rain')

        "Nothing clear":
            $ story_add('doom_score', 1)
            $ story_flag('dream_ignored')
    return
