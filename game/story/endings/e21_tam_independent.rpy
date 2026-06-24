# FILE: game/story/endings/e21_tam_independent.rpy
# MVP ending placeholder. Replace with full ending scene later.

label e21_tam_independent:
    scene black
    "MVP Ending: Tâm Independent Ending."
    "Ending ID: e21_tam_independent"
    if not hasattr(persistent, 'unlocked_endings') or persistent.unlocked_endings is None:
        $ persistent.unlocked_endings = []
    $ add_unique(persistent.unlocked_endings, 'e21_tam_independent')
    return
