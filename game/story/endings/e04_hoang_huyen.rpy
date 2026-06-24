# FILE: game/story/endings/e04_hoang_huyen.rpy
# MVP ending placeholder. Replace with full ending scene later.

label e04_hoang_huyen:
    scene black
    "MVP Ending: Hoàng-Huyền Ending."
    "Ending ID: e04_hoang_huyen"
    if not hasattr(persistent, 'unlocked_endings') or persistent.unlocked_endings is None:
        $ persistent.unlocked_endings = []
    $ add_unique(persistent.unlocked_endings, 'e04_hoang_huyen')
    return
