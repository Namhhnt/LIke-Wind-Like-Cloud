# FILE: game/story/endings/e09_thienan_arranged.rpy
# MVP ending placeholder. Replace with full ending scene later.

label e09_thienan_arranged:
    scene black
    "MVP Ending: Thiên An Arranged Marriage Ending."
    "Ending ID: e09_thienan_arranged"
    if not hasattr(persistent, 'unlocked_endings') or persistent.unlocked_endings is None:
        $ persistent.unlocked_endings = []
    $ add_unique(persistent.unlocked_endings, 'e09_thienan_arranged')
    return
