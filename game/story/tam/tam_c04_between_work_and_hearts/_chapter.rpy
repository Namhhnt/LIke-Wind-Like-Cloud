# FILE: game/story/tam/tam_c04_between_work_and_hearts/_chapter.rpy
# Chapter 04 entry wrapper and weekly checkpoint wrappers.
#
# Design notes:
# - Chapter 04 remains one visible progression chapter.
# - Weekly checkpoints are internal labels and do NOT call story_complete_chapter().
# - Authored Monday-Friday scenes advance the real time-management calendar by
#   five days before a two-day weekend period begins.
# - Each weekly checkpoint opens a two-day weekend period, then returns to route_map.
# - Week 04 records a month-one snapshot but does not lock any route.
# - The final Chapter 04 checkpoint will complete tam_c04_between_work_and_hearts.

label tam_c04_between_work_and_hearts:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_capture_chapter_start("tam_c04_between_work_and_hearts", ["tam", "huyen"])

    if not story_has_flag("tam_c04_started"):
        $ story_flag("tam_c04_started")

    if not story_has_flag("tam_c04_w01_completed"):
        jump tam_c04_w01_new_rhythm

    if not story_has_flag("tam_c04_w02_completed"):
        jump tam_c04_w02_first_priorities

    if not story_has_flag("tam_c04_w03_completed"):
        jump tam_c04_w03_pressure_and_distance

    if not story_has_flag("tam_c04_w04_completed"):
        jump tam_c04_w04_month_one_review

    # Month two begins here once its content is implemented.
    if renpy.has_label("tam_c04_w05_new_month"):
        jump tam_c04_w05_new_month

    jump route_map


label tam_c04_w01_new_rhythm:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_begin_checkpoint("tam_c04_w01")
    $ time_story_begin_workweek("tam_c04_w01_calendar_started")

    call tam_c04_w01_s01_monday_phone_pulse
    call tam_c04_w01_s02_new_work_rhythm
    call tam_c04_w01_s03_report_review
    call tam_c04_w01_s04_quang_after_work
    call tam_c04_w01_s05_friday_first_priority

    call career_bonus_process_checkpoint("tam_c04_w01")

    $ time_story_advance_days_once("tam_c04_w01_calendar_advanced", 5)

    $ story_flag("tam_c04_w01_completed")
    $ story_flag("tam_c04_w01_weekend_open")
    $ phone_refresh_all()

    $ time_start_period_after_chapter("tam_c04_w01_new_rhythm")
    jump route_map


label tam_c04_w02_first_priorities:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_begin_checkpoint("tam_c04_w02")
    if story_has_flag("tam_c04_w01_completed") and not story_has_flag("tam_c04_w01_calendar_advanced"):
        call career_bonus_process_checkpoint("tam_c04_w01")

    $ time_story_advance_days_once("tam_c04_w01_calendar_advanced", 5)

    $ time_story_begin_workweek("tam_c04_w02_calendar_started")

    call tam_c04_w02_s01_monday_phone_pulse
    call tam_c04_w02_s02_hoang_small_followup
    call tam_c04_w02_s03_huyen_knows_the_mark
    call tam_c04_w02_s04_quang_stops_asking_around
    call tam_c04_w02_s05_client_brief_rehearsal
    call tam_c04_w02_s06_friday_second_priority

    call career_bonus_process_checkpoint("tam_c04_w02")

    $ time_story_advance_days_once("tam_c04_w02_calendar_advanced", 5)

    $ story_flag("tam_c04_w02_completed")
    $ story_flag("tam_c04_w02_weekend_open")
    $ phone_refresh_all()

    $ time_start_period_after_chapter("tam_c04_w02_first_priorities")
    jump route_map


label tam_c04_w03_pressure_and_distance:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_begin_checkpoint("tam_c04_w03")
    # Save migration for builds that completed Week 02 before calendar sync.
    if story_has_flag("tam_c04_w02_completed") and not story_has_flag("tam_c04_w02_calendar_advanced"):
        call career_bonus_process_checkpoint("tam_c04_w02")

    $ time_story_advance_days_once("tam_c04_w02_calendar_advanced", 5)

    $ time_story_begin_workweek("tam_c04_w03_calendar_started")

    call tam_c04_w03_s01_monday_phone_pulse
    call tam_c04_w03_s02_client_meeting_pressure
    call tam_c04_w03_s03_hoang_changed_plan
    call tam_c04_w03_s04_huyen_defends_the_standard
    call tam_c04_w03_s05_quang_at_the_door
    call tam_c04_w03_s06_friday_pressure_choice

    call career_bonus_process_checkpoint("tam_c04_w03")

    $ time_story_advance_days_once("tam_c04_w03_calendar_advanced", 5)

    $ story_flag("tam_c04_w03_completed")
    $ story_flag("tam_c04_w03_weekend_open")
    $ phone_refresh_all()

    $ time_start_period_after_chapter("tam_c04_w03_pressure_and_distance")
    jump route_map


label tam_c04_w04_month_one_review:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_begin_checkpoint("tam_c04_w04")
    if story_has_flag("tam_c04_w03_completed") and not story_has_flag("tam_c04_w03_calendar_advanced"):
        call career_bonus_process_checkpoint("tam_c04_w03")

    $ time_story_advance_days_once("tam_c04_w03_calendar_advanced", 5)

    $ time_story_begin_workweek("tam_c04_w04_calendar_started")

    call tam_c04_w04_s01_monday_phone_pulse
    call tam_c04_w04_s02_monthly_work_review
    call tam_c04_w04_s03_hoang_waits_less
    call tam_c04_w04_s04_quang_family_table
    call tam_c04_w04_s05_huyen_after_review
    call tam_c04_w04_s06_month_one_priority
    call tam_c04_w04_s07_month_one_snapshot

    call career_bonus_process_checkpoint("tam_c04_w04")

    $ time_story_advance_days_once("tam_c04_w04_calendar_advanced", 5)

    $ story_flag("tam_c04_w04_completed")
    $ story_flag("tam_c04_month_01_completed")
    $ story_flag("tam_c04_w04_weekend_open")
    $ phone_refresh_all()

    $ time_start_period_after_chapter("tam_c04_w04_month_one_review")
    jump route_map


# Safe development hand-off. The Week 04 weekend can finish without a missing-label
# crash while Month 02 is still being authored.
label tam_c04_w05_new_month:
    $ story_flag("tam_c04_month_02_pending")
    $ phone_refresh_all()
    jump route_map
