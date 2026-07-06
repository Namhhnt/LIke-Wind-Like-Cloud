# FILE: game/story/tam/tam_c03_thienan_family/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label tam_c03_thienan_family:
    call tam_c03_thienan_family_s00_thienan_intro
    call tam_c03_thienan_family_s01_quang_visit_home
    call tam_c03_thienan_family_s02_business_trip_preparation
    call tam_c03_thienan_family_s03_family_pressure
    call tam_c03_thienan_family_s04_private_sisters_talk
    call tam_c03_thienan_family_s05_tam_observes_quang
    call tam_c03_thienan_family_s06_support_choice
    call tam_c03_thienan_family_s07_career_seed

    $ story_complete_chapter('tam_c03_thienan_family')
    $ time_start_period_after_chapter('tam_c03_thienan_family')

    if renpy.has_label('route_map'):
        jump route_map

    return
