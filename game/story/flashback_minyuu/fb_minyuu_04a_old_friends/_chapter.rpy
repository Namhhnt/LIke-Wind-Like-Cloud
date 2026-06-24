# FILE: game/story/flashback_minyuu/fb_minyuu_04a_old_friends/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label fb_minyuu_04a_old_friends:
    call fb_minyuu_04a_old_friends_s01_almost_said
    call fb_minyuu_04a_old_friends_s02_keep_boundary
    call fb_minyuu_04a_old_friends_s03_finalize_old_friends
    $ story_complete_chapter('fb_minyuu_04a_old_friends')
    if renpy.has_label('route_map'):
        jump route_map
    return
