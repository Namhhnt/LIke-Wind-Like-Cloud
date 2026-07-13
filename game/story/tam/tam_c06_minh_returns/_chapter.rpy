# FILE: game/story/tam/tam_c06_minh_returns/_chapter.rpy
# Full Chapter 06 wrapper.
#
# Major branch:
# - Committed Tâm–Hoàng: Minh is first met at Hoàng's house.
# - No Tâm–Hoàng commitment: C06 only builds company-side anticipation.
#   Minh's direct company appearance is reserved for C07.

label tam_c06_minh_returns:
    call tam_c06_minh_returns_s01_minh_arrival
    call tam_c06_minh_returns_s02_hoang_intro_group
    call tam_c06_minh_returns_s03_tam_reaction
    call tam_c06_minh_returns_s04_unlock_minh_route

    $ story_flag("minh_return_chapter_complete")
    $ story_complete_chapter("tam_c06_minh_returns")
    $ activity_start_free_time_session(40)

    if renpy.has_label("route_map"):
        jump route_map

    return
