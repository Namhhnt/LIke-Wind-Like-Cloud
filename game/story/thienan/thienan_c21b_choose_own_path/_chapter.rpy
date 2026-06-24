# FILE: game/story/thienan/thienan_c21b_choose_own_path/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label thienan_c21b_choose_own_path:
    call thienan_c21b_choose_own_path_s01_old_feeling_pauses
    call thienan_c21b_choose_own_path_s02_quang_or_family_pressure
    call thienan_c21b_choose_own_path_s03_self_assertion_choice
    $ story_complete_chapter('thienan_c21b_choose_own_path')
    if renpy.has_label('route_map'):
        jump route_map
    return
