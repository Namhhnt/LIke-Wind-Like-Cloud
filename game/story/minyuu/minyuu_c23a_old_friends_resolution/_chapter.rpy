# FILE: game/story/minyuu/minyuu_c23a_old_friends_resolution/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label minyuu_c23a_old_friends_resolution:
    call minyuu_c23a_old_friends_resolution_s01_friendship_talk
    call minyuu_c23a_old_friends_resolution_s02_missed_possibility
    call minyuu_c23a_old_friends_resolution_s03_friendship_or_late_possibility
    $ story_complete_chapter('minyuu_c23a_old_friends_resolution')
    $ activity_start_free_time_session(40)
    if renpy.has_label('route_map'):
        jump route_map
    return
