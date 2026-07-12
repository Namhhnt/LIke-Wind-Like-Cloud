# FILE: game/story/tam/tam_c05_sunday_date/_chapter.rpy
# Full chapter wrapper.
#
# C04 has already established the relationship direction.
# hoang_h01_brother_house prepares the anniversary and sets:
#   story_state["hoang_anniversary_route"] = "tam" | "huyen" | "friend_group"
#
# C05 pays off that route. It does not choose the romance again.

label tam_c05_sunday_date:
    call tam_c05_sunday_date_s01_route_check
    call tam_c05_sunday_date_s02_date_or_group
    call tam_c05_sunday_date_s03_intimacy_choice
    call tam_c05_sunday_date_s04_commit_or_keep_open

    $ story_flag("one_year_anniversary_outing_complete")
    $ story_complete_chapter("tam_c05_sunday_date")
    $ activity_start_free_time_session(40)

    if renpy.has_label("route_map"):
        jump route_map

    return
