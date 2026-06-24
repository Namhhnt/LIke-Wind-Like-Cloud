# FILE: game/story/endings/e22_huyen_independent.rpy
# MVP ending placeholder. Replace with full ending scene later.

label e22_huyen_independent:
    scene black
    "MVP Ending: Huyền Independent Ending."
    "Ending ID: e22_huyen_independent"
    if not hasattr(persistent, 'unlocked_endings') or persistent.unlocked_endings is None:
        $ persistent.unlocked_endings = []
    $ add_unique(persistent.unlocked_endings, 'e22_huyen_independent')
    return
