# FILE: game/story/endings/e24_doom.rpy
# MVP ending placeholder. Replace with full ending scene later.

label e24_doom:
    scene black
    "MVP Ending: Doom Ending."
    "Ending ID: e24_doom"
    if not hasattr(persistent, 'unlocked_endings') or persistent.unlocked_endings is None:
        $ persistent.unlocked_endings = []
    $ add_unique(persistent.unlocked_endings, 'e24_doom')
    return
