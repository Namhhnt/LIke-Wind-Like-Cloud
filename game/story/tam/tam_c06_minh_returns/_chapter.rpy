# FILE: game/story/tam/tam_c06_minh_returns/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label tam_c06_minh_returns:
    call tam_c06_minh_returns_s01_minh_arrival
    call tam_c06_minh_returns_s02_hoang_intro_group
    call tam_c06_minh_returns_s03_tam_reaction
    call tam_c06_minh_returns_s04_unlock_minh_route
    $ story_complete_chapter('tam_c06_minh_returns')
    $ activity_start_free_time_session(40)
    if renpy.has_label('route_map'):
        jump route_map
    return
