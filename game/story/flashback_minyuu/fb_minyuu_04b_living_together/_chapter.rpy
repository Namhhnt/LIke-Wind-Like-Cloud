# FILE: game/story/flashback_minyuu/fb_minyuu_04b_living_together/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label fb_minyuu_04b_living_together:
    call fb_minyuu_04b_living_together_s01_shared_home
    call fb_minyuu_04b_living_together_s02_small_habits
    call fb_minyuu_04b_living_together_s03_confession_or_action
    call fb_minyuu_04b_living_together_s04_unlock_separation
    $ story_complete_chapter('fb_minyuu_04b_living_together')
    $ activity_start_free_time_session(40)
    if renpy.has_label('route_map'):
        jump route_map
    return
