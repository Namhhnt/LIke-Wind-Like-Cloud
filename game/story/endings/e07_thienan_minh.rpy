# FILE: game/story/endings/e07_thienan_minh.rpy
# MVP ending placeholder. Replace with full ending scene later.

label e07_thienan_minh:
    scene black
    "MVP Ending: Thiên An-Minh Ending."
    "Ending ID: e07_thienan_minh"
    if not hasattr(persistent, 'unlocked_endings') or persistent.unlocked_endings is None:
        $ persistent.unlocked_endings = []
    $ add_unique(persistent.unlocked_endings, 'e07_thienan_minh')
    return
