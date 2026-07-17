# FILE: game/story/tam/tam_c07_minh_at_company/_chapter.rpy
# Chapter wrapper.

# Chapter-only supporting speakers.
# Trường works in IT.
# Quân is the existing department head defined in common.rpy.
define c07_linh = Character("Linh", image="linh")
define c07_truong = Character("Trường", image="truong")
define c07_mai = Character("Mai", image="mai")


label tam_c07_minh_at_company:
    # Route snapshot for this chapter.
    # "High clarity" is intentionally stricter than the baseline ending threshold.
    $ c07_tam_hoang_commit = story_has_direction("tam", "tam_hoang_commit")
    $ c07_tam_hoang_open = story_has_direction("tam", "tam_hoang_open")
    $ c07_tam_minh_commit = story_has_direction("tam", "tam_minh_commit")
    $ c07_tam_quang_commit = story_has_direction("tam", "tam_quang_commit") or story_has_direction("quang", "quang_tam_commit")
    $ c07_tam_high_clarity = story_state.get("tam_self_clarity", 0) >= 60

    if c07_tam_hoang_commit and c07_tam_high_clarity:
        $ c07_tam_mode = "hoang_clear"

    elif c07_tam_hoang_commit or c07_tam_hoang_open:
        # Includes the canon-in-progress path when C05/C06 opened Hoàng,
        # but a later chapter has not committed it yet.
        $ c07_tam_mode = "hoang_uncertain"

    elif not c07_tam_minh_commit and not c07_tam_quang_commit:
        $ c07_tam_mode = "uncommitted"

    else:
        $ c07_tam_mode = "other_commit"

    $ c07_huyen_hoang_commit = story_has_direction("huyen", "huyen_hoang_commit")
    $ c07_huyen_quan_commit = story_has_direction("huyen", "huyen_quan_commit")
    $ c07_huyen_knows_dream = story_has_flag("huyen_knows_dream") or story_has_flag("huyen_teases_dream")
    $ c07_work_choice = ""

    call tam_c07_minh_at_company_s01_monday_morning
    call tam_c07_minh_at_company_s02_northbridge_arrival
    call tam_c07_minh_at_company_s03_working_logic
    call tam_c07_minh_at_company_s04_recognition_and_huyen
    call tam_c07_minh_at_company_s05_evening_routes

    $ story_flag("tam_c07_minh_at_company_complete")
    $ story_complete_chapter("tam_c07_minh_at_company")

    $ time_start_period_after_chapter("tam_c07_minh_at_company")

    if renpy.has_label("route_map"):
        jump route_map

    return