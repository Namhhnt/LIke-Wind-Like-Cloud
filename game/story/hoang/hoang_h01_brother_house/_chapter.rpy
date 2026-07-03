# FILE: game/story/hoang/hoang_h01_brother_house/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label hoang_h01_brother_house:
    call hoang_h01_brother_house_s01_villa_intro
    call hoang_h01_brother_house_s02_minh_remote_presence
    call hoang_h01_brother_house_s03_gift_choice
    call hoang_h01_brother_house_s04_hoang_direction_choice
    $ story_complete_chapter('hoang_h01_brother_house')
    $ activity_start_free_time_session(40)
    if renpy.has_label('route_map'):
        jump route_map
    return
