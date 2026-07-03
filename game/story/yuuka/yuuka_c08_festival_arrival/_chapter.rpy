# FILE: game/story/yuuka/yuuka_c08_festival_arrival/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label yuuka_c08_festival_arrival:
    call yuuka_c08_festival_arrival_s01_festival_briefing
    call yuuka_c08_festival_arrival_s02_yuuka_as_director
    call yuuka_c08_festival_arrival_s03_hoang_introduces_yuuka
    call yuuka_c08_festival_arrival_s04_minh_neutral_pause
    $ story_complete_chapter('yuuka_c08_festival_arrival')
    $ activity_start_free_time_session(40)
    if renpy.has_label('route_map'):
        jump route_map
    return
