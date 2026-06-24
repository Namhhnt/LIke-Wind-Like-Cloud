# FILE: game/story/endings/e05_huyen_quan.rpy
# MVP ending placeholder. Replace with full ending scene later.

label e05_huyen_quan:
    scene black
    "MVP Ending: Huyền-Quân Ending."
    "Ending ID: e05_huyen_quan"
    if not hasattr(persistent, 'unlocked_endings') or persistent.unlocked_endings is None:
        $ persistent.unlocked_endings = []
    $ add_unique(persistent.unlocked_endings, 'e05_huyen_quan')
    return
