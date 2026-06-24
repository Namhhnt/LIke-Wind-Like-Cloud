# FILE: game/story/flashback_minyuu/fb_minyuu_03_door_left_open/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label fb_minyuu_03_door_left_open:
    call fb_minyuu_03_door_left_open_s01_problem_setup
    call fb_minyuu_03_door_left_open_s02_help_choice
    call fb_minyuu_03_door_left_open_s03_living_together_or_not
    call fb_minyuu_03_door_left_open_s04_branch_unlock
    $ story_complete_chapter('fb_minyuu_03_door_left_open')
    if renpy.has_label('route_map'):
        jump route_map
    return
