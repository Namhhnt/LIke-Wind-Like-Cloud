# FILE: game/story/tam/tam_c05_sunday_date/s04_commit_or_keep_open.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c05_sunday_date_s04_commit_or_keep_open:
    "MVP: The outing sets the first romantic commitment seed."
    menu:
        "What does this day become?"

        "A clear Tâm-Hoàng beginning":
            $ story_add_direction('tam', 'tam_hoang_commit')
            $ story_add_ending_support('e02_tam_hoang')
            $ story_add('hoang_tam_trust', 2)

        "A possible Hoàng-Huyền route":
            $ story_add_direction('huyen', 'huyen_hoang_open')
            $ story_add('huyen_hoang_interest', 2)
            $ story_add('hoang_huyen_interest', 2)

        "No commitment yet":
            $ story_add('tam_self_clarity', 1)
            $ story_add('hoang_self_acceptance', 1)
    return
