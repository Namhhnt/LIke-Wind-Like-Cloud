# FILE: game/story/yuuka/yuuka_c09_yuukas_work/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label yuuka_c09_yuukas_work:
    call yuuka_c09_yuukas_work_s01_screening
    call yuuka_c09_yuukas_work_s02_qa_session
    call yuuka_c09_yuukas_work_s03_state_sensitive_minh_yuuka_moment
    call yuuka_c09_yuukas_work_s04_tam_or_huyen_observation
    $ story_complete_chapter('yuuka_c09_yuukas_work')
    $ activity_start_free_time_session(40)
    if renpy.has_label('route_map'):
        jump route_map
    return
