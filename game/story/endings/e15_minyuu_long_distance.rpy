# FILE: game/story/endings/e15_minyuu_long_distance.rpy
# MVP ending placeholder. Replace with full ending scene later.

label e15_minyuu_long_distance:
    scene black
    "MVP Ending: Minh-Yuuka Long-Distance Lovers Ending."
    "Ending ID: e15_minyuu_long_distance"
    if not hasattr(persistent, 'unlocked_endings') or persistent.unlocked_endings is None:
        $ persistent.unlocked_endings = []
    $ add_unique(persistent.unlocked_endings, 'e15_minyuu_long_distance')
    return
