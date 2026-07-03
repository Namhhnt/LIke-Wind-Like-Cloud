# FILE: game/story/work/work_c16_project_crisis/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label work_c16_project_crisis:
    call work_c16_project_crisis_s01_crisis_setup
    call work_c16_project_crisis_s02_tam_solution
    call work_c16_project_crisis_s03_huyen_quan_interaction
    call work_c16_project_crisis_s04_minh_boundary_check
    $ story_complete_chapter('work_c16_project_crisis')
    $ activity_start_free_time_session(40)
    if renpy.has_label('route_map'):
        jump route_map
    return
