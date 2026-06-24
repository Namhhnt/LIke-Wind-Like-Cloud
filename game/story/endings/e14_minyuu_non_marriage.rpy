# FILE: game/story/endings/e14_minyuu_non_marriage.rpy
# MVP ending placeholder. Replace with full ending scene later.

label e14_minyuu_non_marriage:
    scene black
    "MVP Ending: Minh-Yuuka Non-Marriage Lovers Ending."
    "Ending ID: e14_minyuu_non_marriage"
    if not hasattr(persistent, 'unlocked_endings') or persistent.unlocked_endings is None:
        $ persistent.unlocked_endings = []
    $ add_unique(persistent.unlocked_endings, 'e14_minyuu_non_marriage')
    return
