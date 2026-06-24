# FILE: game/story/hoang/hoang_h05_shadow_of_minh/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label hoang_h05_shadow_of_minh:
    call hoang_h05_shadow_of_minh_s01_hoang_insecurity_or_clarity
    call hoang_h05_shadow_of_minh_s02_tam_confrontation
    call hoang_h05_shadow_of_minh_s03_huyen_or_minh_context
    call hoang_h05_shadow_of_minh_s04_growth_choice
    $ story_complete_chapter('hoang_h05_shadow_of_minh')
    if renpy.has_label('route_map'):
        jump route_map
    return
