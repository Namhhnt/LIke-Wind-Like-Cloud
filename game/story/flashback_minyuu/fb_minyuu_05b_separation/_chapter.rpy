# FILE: game/story/flashback_minyuu/fb_minyuu_05b_separation/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label fb_minyuu_05b_separation:
    call fb_minyuu_05b_separation_s01_distance_starts
    call fb_minyuu_05b_separation_s02_break_or_silent_distance
    call fb_minyuu_05b_separation_s03_yuuka_leaves_or_minh_cuts
    call fb_minyuu_05b_separation_s04_finalize_ex_lovers
    $ story_complete_chapter('fb_minyuu_05b_separation')
    $ activity_start_free_time_session(40)
    if renpy.has_label('route_map'):
        jump route_map
    return
