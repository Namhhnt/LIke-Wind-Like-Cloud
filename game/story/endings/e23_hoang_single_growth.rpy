# FILE: game/story/endings/e23_hoang_single_growth.rpy
# MVP ending placeholder. Replace with full ending scene later.

label e23_hoang_single_growth:
    scene black
    "MVP Ending: Hoàng Single Growth Ending."
    "Ending ID: e23_hoang_single_growth"
    if not hasattr(persistent, 'unlocked_endings') or persistent.unlocked_endings is None:
        $ persistent.unlocked_endings = []
    $ add_unique(persistent.unlocked_endings, 'e23_hoang_single_growth')
    return
