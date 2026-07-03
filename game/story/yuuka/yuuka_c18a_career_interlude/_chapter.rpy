# FILE: game/story/yuuka/yuuka_c18a_career_interlude/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label yuuka_c18a_career_interlude:
    call yuuka_c18a_career_interlude_s01_festival_afterglow
    call yuuka_c18a_career_interlude_s02_yuuka_career_choice
    call yuuka_c18a_career_interlude_s03_friendship_balance
    $ story_complete_chapter('yuuka_c18a_career_interlude')
    $ activity_start_free_time_session(40)
    if renpy.has_label('route_map'):
        jump route_map
    return
