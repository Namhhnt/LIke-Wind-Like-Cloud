# FILE: game/story/endings/e02_tam_hoang.rpy
# MVP ending placeholder. Replace with full ending scene later.

label e02_tam_hoang:
    scene black
    "MVP Ending: Tâm-Hoàng Ending."
    "Ending ID: e02_tam_hoang"
    if not hasattr(persistent, 'unlocked_endings') or persistent.unlocked_endings is None:
        $ persistent.unlocked_endings = []
    $ add_unique(persistent.unlocked_endings, 'e02_tam_hoang')
    return
