# FILE: game/story/tam/tam_c20b_admiration_vs_love/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label tam_c20b_admiration_vs_love:
    call tam_c20b_admiration_vs_love_s01_tam_confusion
    call tam_c20b_admiration_vs_love_s02_minh_is_not_available
    call tam_c20b_admiration_vs_love_s03_tam_self_clarity_choice
    $ story_complete_chapter('tam_c20b_admiration_vs_love')
    $ activity_start_free_time_session(40)
    if renpy.has_label('route_map'):
        jump route_map
    return
