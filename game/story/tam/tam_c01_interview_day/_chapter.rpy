# FILE: game/story/tam/tam_c01_interview_day/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label tam_c01_interview_day:
    call tam_c01_interview_day_s01_tam_huyen_morning
    $ initialize_progression()
    $ add_unique(progress["player_flags"], "opening_map_locations_unlocked")
    $ unlock_map_locations(["tam_apartment", "huyen_apartment", "company"])
    call tam_c01_interview_day_s02_interview_room
    call tam_c01_interview_day_s03_success_result
    call tam_c01_interview_day_s04_celebration_dinner
    $ story_complete_chapter('tam_c01_interview_day')
    $ activity_start_free_time_session(40)
    if renpy.has_label('route_map'):
        jump route_map
    return
