# FILE: game/story/flashback_minyuu/fb_minyuu_02_working_rhythm/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label fb_minyuu_02_working_rhythm:
    call fb_minyuu_02_working_rhythm_s01_shared_project
    call fb_minyuu_02_working_rhythm_s02_yuuka_learning
    call fb_minyuu_02_working_rhythm_s03_minh_care_or_boundary
    call fb_minyuu_02_working_rhythm_s04_score_branch
    $ story_complete_chapter('fb_minyuu_02_working_rhythm')
    if renpy.has_label('route_map'):
        jump route_map
    return
