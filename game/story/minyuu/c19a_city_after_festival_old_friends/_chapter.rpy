# FILE: game/story/minyuu/c19a_city_after_festival_old_friends/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label c19a_city_after_festival_old_friends:
    call c19a_city_after_festival_old_friends_s01_cafe_or_walk
    call c19a_city_after_festival_old_friends_s02_old_almost_question
    call c19a_city_after_festival_old_friends_s03_friendship_resolution_choice
    $ story_complete_chapter('c19a_city_after_festival_old_friends')
    $ activity_start_free_time_session(40)
    if renpy.has_label('route_map'):
        jump route_map
    return
