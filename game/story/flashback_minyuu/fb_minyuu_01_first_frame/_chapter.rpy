# FILE: game/story/flashback_minyuu/fb_minyuu_01_first_frame/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label fb_minyuu_01_first_frame:
    call fb_minyuu_01_first_frame_s01_first_context
    call fb_minyuu_01_first_frame_s02_professional_friction
    call fb_minyuu_01_first_frame_s03_first_choice
    $ story_complete_chapter('fb_minyuu_01_first_frame')
    if renpy.has_label('route_map'):
        jump route_map
    return
