# FILE: game/story/hoang/hoang_h01_brother_house/_chapter.rpy
# Full chapter wrapper.
#
# Timeline:
# - C04 resolves the relationship direction.
# - Three months pass off-screen.
# - This interlude prepares the one-year anniversary outing.
# - The chapter continues directly into C05.

label hoang_h01_brother_house:
    call hoang_h01_brother_house_s01_three_months_later
    call hoang_h01_brother_house_s02_minh_remote_presence
    call hoang_h01_brother_house_s03_gift_choice
    call hoang_h01_brother_house_s04_send_invitation

    $ story_flag("hoang_anniversary_preparation_complete")
    $ story_complete_chapter("hoang_h01_brother_house")

    # This interlude and C05 are one continuous story beat.
    if renpy.has_label("tam_c05_sunday_date"):
        jump tam_c05_sunday_date

    # Safe fallback while C05 is still being implemented.
    if renpy.has_label("route_map"):
        jump route_map

    return
