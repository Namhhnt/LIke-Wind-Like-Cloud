# FILE: game/story/prologue/prologue_rain_dream/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label prologue_rain_dream:
    call prologue_rain_dream_s01_rain_meeting
    call prologue_rain_dream_s02_wake_up
    call prologue_rain_dream_s03_tell_or_hide
    $ story_complete_chapter('prologue_rain_dream')
    if renpy.has_label('route_map'):
        jump route_map
    return
