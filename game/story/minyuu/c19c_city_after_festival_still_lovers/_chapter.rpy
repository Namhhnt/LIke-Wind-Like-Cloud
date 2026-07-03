# FILE: game/story/minyuu/c19c_city_after_festival_still_lovers/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label c19c_city_after_festival_still_lovers:
    call c19c_city_after_festival_still_lovers_s01_lovers_reunion
    call c19c_city_after_festival_still_lovers_s02_private_or_public
    call c19c_city_after_festival_still_lovers_s03_future_shape_choice
    $ story_complete_chapter('c19c_city_after_festival_still_lovers')
    $ activity_start_free_time_session(40)
    if renpy.has_label('route_map'):
        jump route_map
    return
