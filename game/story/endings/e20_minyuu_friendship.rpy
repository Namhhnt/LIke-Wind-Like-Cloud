# FILE: game/story/endings/e20_minyuu_friendship.rpy
# MVP ending placeholder. Replace with full ending scene later.

label e20_minyuu_friendship:
    scene black
    "MVP Ending: Minh-Yuuka Friendship Ending."
    "Ending ID: e20_minyuu_friendship"
    if not hasattr(persistent, 'unlocked_endings') or persistent.unlocked_endings is None:
        $ persistent.unlocked_endings = []
    $ add_unique(persistent.unlocked_endings, 'e20_minyuu_friendship')
    return
