# FILE: game/story/minyuu/minyuu_c23b_ex_lovers_resolution/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label minyuu_c23b_ex_lovers_resolution:
    call minyuu_c23b_ex_lovers_resolution_s01_no_more_running
    call minyuu_c23b_ex_lovers_resolution_s02_truth_choice
    call minyuu_c23b_ex_lovers_resolution_s03_reunion_late_or_single
    $ story_complete_chapter('minyuu_c23b_ex_lovers_resolution')
    $ activity_start_free_time_session(40)
    if renpy.has_label('route_map'):
        jump route_map
    return
