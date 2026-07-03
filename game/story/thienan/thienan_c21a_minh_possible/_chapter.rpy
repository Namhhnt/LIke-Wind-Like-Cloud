# FILE: game/story/thienan/thienan_c21a_minh_possible/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label thienan_c21a_minh_possible:
    call thienan_c21a_minh_possible_s01_old_residue
    call thienan_c21a_minh_possible_s02_quang_presence
    call thienan_c21a_minh_possible_s03_thienan_choice
    call thienan_c21a_minh_possible_s04_route_commit_or_release
    $ story_complete_chapter('thienan_c21a_minh_possible')
    $ activity_start_free_time_session(40)
    if renpy.has_label('route_map'):
        jump route_map
    return
