# FILE: game/story/yuuka/yuuka_c18c_long_distance_interlude/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label yuuka_c18c_long_distance_interlude:
    call yuuka_c18c_long_distance_interlude_s01_distance_context
    call yuuka_c18c_long_distance_interlude_s02_private_messages
    call yuuka_c18c_long_distance_interlude_s03_career_and_love_balance
    $ story_complete_chapter('yuuka_c18c_long_distance_interlude')
    if renpy.has_label('route_map'):
        jump route_map
    return
