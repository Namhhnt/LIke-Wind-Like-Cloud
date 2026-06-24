# FILE: game/story/endings/e06_thienan_quang.rpy
# MVP ending placeholder. Replace with full ending scene later.

label e06_thienan_quang:
    scene black
    "MVP Ending: Thiên An-Quang Ending."
    "Ending ID: e06_thienan_quang"
    if not hasattr(persistent, 'unlocked_endings') or persistent.unlocked_endings is None:
        $ persistent.unlocked_endings = []
    $ add_unique(persistent.unlocked_endings, 'e06_thienan_quang')
    return
