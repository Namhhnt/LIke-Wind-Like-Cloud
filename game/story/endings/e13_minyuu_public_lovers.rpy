# FILE: game/story/endings/e13_minyuu_public_lovers.rpy
# MVP ending placeholder. Replace with full ending scene later.

label e13_minyuu_public_lovers:
    scene black
    "MVP Ending: Minh-Yuuka Public Lovers Ending."
    "Ending ID: e13_minyuu_public_lovers"
    if not hasattr(persistent, 'unlocked_endings') or persistent.unlocked_endings is None:
        $ persistent.unlocked_endings = []
    $ add_unique(persistent.unlocked_endings, 'e13_minyuu_public_lovers')
    return
