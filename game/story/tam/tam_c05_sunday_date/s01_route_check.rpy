# FILE: game/story/tam/tam_c05_sunday_date/s01_route_check.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c05_sunday_date_s01_route_check:
    "MVP: Sunday plans depend on the current Hoàng/Tâm/Huyền setup."
    if story_has_direction('hoang', 'hoang_huyen_open') and story_state['hoang_huyen_interest'] > story_state['hoang_tam_trust']:
        "MVP: The day leans toward a Hoàng-Huyền possibility."
    elif story_state['hoang_tam_trust'] >= 2:
        "MVP: The day leans toward Tâm-Hoàng."
    else:
        "MVP: The day becomes a friend-group outing."
    return
