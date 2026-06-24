# FILE: game/story/tam/tam_c03_thienan_family/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label tam_c03_thienan_family:
    call tam_c03_thienan_family_s01_home_with_thienan
    call tam_c03_thienan_family_s02_family_pressure
    call tam_c03_thienan_family_s03_tam_support_choice
    call tam_c03_thienan_family_s04_career_seed
    $ story_complete_chapter('tam_c03_thienan_family')
    if renpy.has_label('route_map'):
        jump route_map
    return
