# FILE: game/story/endings/e11_minyuu_late_reunion.rpy
# MVP ending placeholder. Replace with full ending scene later.

label e11_minyuu_late_reunion:
    scene black
    "MVP Ending: Minh-Yuuka Late Reunion Ending."
    "Ending ID: e11_minyuu_late_reunion"
    if not hasattr(persistent, 'unlocked_endings') or persistent.unlocked_endings is None:
        $ persistent.unlocked_endings = []
    $ add_unique(persistent.unlocked_endings, 'e11_minyuu_late_reunion')
    return
