# FILE: game/story/flashback_minyuu/fb_minyuu_04c_no_breakup/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label fb_minyuu_04c_no_breakup:
    call fb_minyuu_04c_no_breakup_s01_lovers_confirmed
    call fb_minyuu_04c_no_breakup_s02_distance_without_breakup
    call fb_minyuu_04c_no_breakup_s03_private_or_public_seed
    call fb_minyuu_04c_no_breakup_s04_finalize_still_lovers
    $ story_complete_chapter('fb_minyuu_04c_no_breakup')
    if renpy.has_label('route_map'):
        jump route_map
    return
