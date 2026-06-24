# FILE: game/story/endings/e08_thienan_single.rpy
# MVP ending placeholder. Replace with full ending scene later.

label e08_thienan_single:
    scene black
    "MVP Ending: Thiên An Single Ending."
    "Ending ID: e08_thienan_single"
    if not hasattr(persistent, 'unlocked_endings') or persistent.unlocked_endings is None:
        $ persistent.unlocked_endings = []
    $ add_unique(persistent.unlocked_endings, 'e08_thienan_single')
    return
