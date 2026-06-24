# FILE: game/story/group/group_c11_social_dinner/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label group_c11_social_dinner:
    call group_c11_social_dinner_s01_invitation
    call group_c11_social_dinner_s02_group_table
    call group_c11_social_dinner_s03_state_sensitive_dinner
    call group_c11_social_dinner_s04_observation_choice
    $ story_complete_chapter('group_c11_social_dinner')
    if renpy.has_label('route_map'):
        jump route_map
    return
