# FILE: game/story/tam/tam_c05_sunday_date/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label tam_c05_sunday_date:
    call tam_c05_sunday_date_s01_route_check
    call tam_c05_sunday_date_s02_date_or_group
    call tam_c05_sunday_date_s03_intimacy_choice
    call tam_c05_sunday_date_s04_commit_or_keep_open
    $ story_complete_chapter('tam_c05_sunday_date')
    $ activity_start_free_time_session(40)
    if renpy.has_label('route_map'):
        jump route_map
    return
