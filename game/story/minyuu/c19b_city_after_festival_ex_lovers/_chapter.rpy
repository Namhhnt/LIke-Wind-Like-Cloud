# FILE: game/story/minyuu/c19b_city_after_festival_ex_lovers/_chapter.rpy
# Chapter wrapper. Calls scene labels only; no heavy story content here.

label c19b_city_after_festival_ex_lovers:
    call c19b_city_after_festival_ex_lovers_s01_private_conversation
    call c19b_city_after_festival_ex_lovers_s02_unresolved_past
    call c19b_city_after_festival_ex_lovers_s03_reunion_or_late_or_single_choice
    $ story_complete_chapter('c19b_city_after_festival_ex_lovers')
    if renpy.has_label('route_map'):
        jump route_map
    return
