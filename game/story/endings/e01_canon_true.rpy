# FILE: game/story/endings/e01_canon_true.rpy
# MVP ending placeholder. Replace with full ending scene later.

label e01_canon_true:
    scene black
    "MVP Ending: Canon True Ending: Tâm-Hoàng / Minh-Yuuka / Huyền-Quân / Thiên An-Quang."
    "Ending ID: e01_canon_true"
    if not hasattr(persistent, 'unlocked_endings') or persistent.unlocked_endings is None:
        $ persistent.unlocked_endings = []
    $ add_unique(persistent.unlocked_endings, 'e01_canon_true')
    return
