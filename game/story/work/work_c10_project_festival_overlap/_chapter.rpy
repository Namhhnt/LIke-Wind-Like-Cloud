# FILE: game/story/work/work_c10_project_festival_overlap/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label work_c10_project_festival_overlap:
    call work_c10_project_festival_overlap_s01_project_problem
    call work_c10_project_festival_overlap_s02_yuuka_feedback
    call work_c10_project_festival_overlap_s03_quan_team_pressure
    call work_c10_project_festival_overlap_s04_career_or_relationship_choice
    $ story_complete_chapter('work_c10_project_festival_overlap')
    $ activity_start_free_time_session(40)
    if renpy.has_label('route_map'):
        jump route_map
    return
