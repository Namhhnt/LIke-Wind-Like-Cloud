# FILE: game/story/endings/e03_tam_minh.rpy
# MVP ending placeholder. Replace with full ending scene later.

label e03_tam_minh:
    scene black
    "MVP Ending: Tâm-Minh Ending."
    "Ending ID: e03_tam_minh"
    if not hasattr(persistent, 'unlocked_endings') or persistent.unlocked_endings is None:
        $ persistent.unlocked_endings = []
    $ add_unique(persistent.unlocked_endings, 'e03_tam_minh')
    return
