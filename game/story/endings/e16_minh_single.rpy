# FILE: game/story/endings/e16_minh_single.rpy
# MVP ending placeholder. Replace with full ending scene later.

label e16_minh_single:
    scene black
    "MVP Ending: Minh Single Ending."
    "Ending ID: e16_minh_single"
    if not hasattr(persistent, 'unlocked_endings') or persistent.unlocked_endings is None:
        $ persistent.unlocked_endings = []
    $ add_unique(persistent.unlocked_endings, 'e16_minh_single')
    return
