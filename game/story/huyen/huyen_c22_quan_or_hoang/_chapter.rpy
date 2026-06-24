# FILE: game/story/huyen/huyen_c22_quan_or_hoang/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label huyen_c22_quan_or_hoang:
    call huyen_c22_quan_or_hoang_s01_huyen_route_check
    call huyen_c22_quan_or_hoang_s02_quan_professional_respect
    call huyen_c22_quan_or_hoang_s03_hoang_huyen_option
    call huyen_c22_quan_or_hoang_s04_huyen_choice
    $ story_complete_chapter('huyen_c22_quan_or_hoang')
    if renpy.has_label('route_map'):
        jump route_map
    return
