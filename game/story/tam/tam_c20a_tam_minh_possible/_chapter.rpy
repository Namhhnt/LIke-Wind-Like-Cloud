# FILE: game/story/tam/tam_c20a_tam_minh_possible/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label tam_c20a_tam_minh_possible:
    call tam_c20a_tam_minh_possible_s01_tam_recognizes_interest
    call tam_c20a_tam_minh_possible_s02_minh_boundary_or_openness
    call tam_c20a_tam_minh_possible_s03_tam_choice
    call tam_c20a_tam_minh_possible_s04_route_commit_or_step_back
    $ story_complete_chapter('tam_c20a_tam_minh_possible')
    $ activity_start_free_time_session(40)
    if renpy.has_label('route_map'):
        jump route_map
    return
