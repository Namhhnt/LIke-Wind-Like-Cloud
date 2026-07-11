# FILE: game/story/tam/tam_c04_between_work_and_hearts/_chapter.rpy
# Chapter 04 entry wrapper and weekly checkpoint wrappers.
# Weekly checkpoints remain internal; only the final C04 checkpoint completes the chapter.
# Wrapper version: 1.9 — includes Week 13–24 (Months 04–06) and final phase transition.

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
    if not story_has_flag("tam_c04_w05_completed"):
        jump tam_c04_w05_new_month
    if not story_has_flag("tam_c04_w06_completed"):
        jump tam_c04_w06_the_empty_chair
    if not story_has_flag("tam_c04_w07_completed"):
        jump tam_c04_w07_someone_notices_first
    if not story_has_flag("tam_c04_w08_completed"):
        jump tam_c04_w08_month_two_review
    if not story_has_flag("tam_c04_w09_completed"):
        jump tam_c04_w09_named_gaps
    if not story_has_flag("tam_c04_w10_completed"):
        jump tam_c04_w10_no_one_stands_in
    if not story_has_flag("tam_c04_w11_completed"):
        jump tam_c04_w11_cannot_pretend
    if not story_has_flag("tam_c04_w12_completed"):
        jump tam_c04_w12_three_month_review
    if not story_has_flag("tam_c04_w13_completed"):
        jump tam_c04_w13_departures
    if not story_has_flag("tam_c04_w14_completed"):
        jump tam_c04_w14_quiet_house
    if not story_has_flag("tam_c04_w15_completed"):
        jump tam_c04_w15_distance_has_weight
    if not story_has_flag("tam_c04_w16_completed"):
        jump tam_c04_w16_month_four_review
    if not story_has_flag("tam_c04_w17_completed"):
        jump tam_c04_w17_returns
    if not story_has_flag("tam_c04_w18_completed"):
        jump tam_c04_w18_choose_an_answer
    if not story_has_flag("tam_c04_w19_completed"):
        jump tam_c04_w19_after_the_answer
    if not story_has_flag("tam_c04_w20_completed"):
        jump tam_c04_w20_month_five_review
    if not story_has_flag("tam_c04_w21_completed"):
        jump tam_c04_w21_new_routine
    if not story_has_flag("tam_c04_w22_completed"):
        jump tam_c04_w22_when_work_interrupts
    if not story_has_flag("tam_c04_w23_completed"):
        jump tam_c04_w23_new_balance
    if not story_has_flag("tam_c04_w24_completed"):
        jump tam_c04_w24_six_month_finale

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

label tam_c04_w05_new_month:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_begin_checkpoint("tam_c04_w05")
    if story_has_flag("tam_c04_w04_completed") and not story_has_flag("tam_c04_w04_calendar_advanced"):
        call career_bonus_process_checkpoint("tam_c04_w04")
    $ time_story_advance_days_once("tam_c04_w04_calendar_advanced", 5)
    $ time_story_begin_workweek("tam_c04_w05_calendar_started")
    call tam_c04_w05_s01_monday_phone_pulse
    call tam_c04_w05_s02_separate_ownership
    call tam_c04_w05_s03_hoang_house_invitation
    call tam_c04_w05_s04_quang_two_cups
    call tam_c04_w05_s05_huyen_first_client_lead
    call tam_c04_w05_s06_friday_new_month_priority
    call career_bonus_process_checkpoint("tam_c04_w05")
    $ time_story_advance_days_once("tam_c04_w05_calendar_advanced", 5)
    $ story_flag("tam_c04_w05_completed")
    $ story_flag("tam_c04_w05_weekend_open")
    $ phone_refresh_all()
    $ time_start_period_after_chapter("tam_c04_w05_new_month")
    jump route_map

label tam_c04_w06_the_empty_chair:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_begin_checkpoint("tam_c04_w06")
    if story_has_flag("tam_c04_w05_completed") and not story_has_flag("tam_c04_w05_calendar_advanced"):
        call career_bonus_process_checkpoint("tam_c04_w05")
    $ time_story_advance_days_once("tam_c04_w05_calendar_advanced", 5)
    $ time_story_begin_workweek("tam_c04_w06_calendar_started")
    call tam_c04_w06_s01_monday_phone_pulse
    call tam_c04_w06_s02_quan_empty_chair
    call tam_c04_w06_s03_tam_scope_change
    call tam_c04_w06_s04_hoang_house_evening
    call tam_c04_w06_s05_quang_family_errand
    call tam_c04_w06_s06_friday_absence_priority
    call career_bonus_process_checkpoint("tam_c04_w06")
    $ time_story_advance_days_once("tam_c04_w06_calendar_advanced", 5)
    $ story_flag("tam_c04_w06_completed")
    $ story_flag("tam_c04_w06_weekend_open")
    $ phone_refresh_all()
    $ time_start_period_after_chapter("tam_c04_w06_the_empty_chair")
    jump route_map

label tam_c04_w07_someone_notices_first:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_begin_checkpoint("tam_c04_w07")
    if story_has_flag("tam_c04_w06_completed") and not story_has_flag("tam_c04_w06_calendar_advanced"):
        call career_bonus_process_checkpoint("tam_c04_w06")
    $ time_story_advance_days_once("tam_c04_w06_calendar_advanced", 5)
    $ time_story_begin_workweek("tam_c04_w07_calendar_started")
    call tam_c04_w07_s01_monday_phone_pulse
    call tam_c04_w07_s02_huyen_disagrees_with_reasons
    call tam_c04_w07_s03_hoang_notices_first
    call tam_c04_w07_s04_quang_lunch_box
    call tam_c04_w07_s05_thienan_no_interpreter
    call tam_c04_w07_s06_friday_small_truth
    call career_bonus_process_checkpoint("tam_c04_w07")
    $ time_story_advance_days_once("tam_c04_w07_calendar_advanced", 5)
    $ story_flag("tam_c04_w07_completed")
    $ story_flag("tam_c04_w07_weekend_open")
    $ phone_refresh_all()
    $ time_start_period_after_chapter("tam_c04_w07_someone_notices_first")
    jump route_map

label tam_c04_w08_month_two_review:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_begin_checkpoint("tam_c04_w08")
    if story_has_flag("tam_c04_w07_completed") and not story_has_flag("tam_c04_w07_calendar_advanced"):
        call career_bonus_process_checkpoint("tam_c04_w07")
    $ time_story_advance_days_once("tam_c04_w07_calendar_advanced", 5)
    $ time_story_begin_workweek("tam_c04_w08_calendar_started")
    call tam_c04_w08_s01_monday_phone_pulse
    call tam_c04_w08_s02_second_monthly_review
    call tam_c04_w08_s03_hoang_asks_when
    call tam_c04_w08_s04_quang_choose_a_door
    call tam_c04_w08_s05_huyen_stays_without_tam
    call tam_c04_w08_s06_month_two_priority
    call tam_c04_w08_s07_month_two_snapshot
    call career_bonus_process_checkpoint("tam_c04_w08")
    $ time_story_advance_days_once("tam_c04_w08_calendar_advanced", 5)
    $ story_flag("tam_c04_w08_completed")
    $ story_flag("tam_c04_month_02_completed")
    $ story_flag("tam_c04_w08_weekend_open")
    $ phone_refresh_all()
    $ time_start_period_after_chapter("tam_c04_w08_month_two_review")
    jump route_map

label tam_c04_w09_named_gaps:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_begin_checkpoint("tam_c04_w09")
    if story_has_flag("tam_c04_w08_completed") and not story_has_flag("tam_c04_w08_calendar_advanced"):
        call career_bonus_process_checkpoint("tam_c04_w08")
    $ time_story_advance_days_once("tam_c04_w08_calendar_advanced", 5)
    $ time_story_begin_workweek("tam_c04_w09_calendar_started")
    call tam_c04_w09_s01_monday_phone_pulse
    call tam_c04_w09_s02_authority_without_shadow
    call tam_c04_w09_s03_hoang_keeps_a_place
    call tam_c04_w09_s04_quang_wrong_recipient
    call tam_c04_w09_s05_huyen_send_it
    call tam_c04_w09_s06_friday_named_priority
    call career_bonus_process_checkpoint("tam_c04_w09")
    $ time_story_advance_days_once("tam_c04_w09_calendar_advanced", 5)
    $ story_flag("tam_c04_w09_completed")
    $ story_flag("tam_c04_w09_weekend_open")
    $ phone_refresh_all()
    $ time_start_period_after_chapter("tam_c04_w09_named_gaps")
    jump route_map

label tam_c04_w10_no_one_stands_in:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_begin_checkpoint("tam_c04_w10")
    if story_has_flag("tam_c04_w09_completed") and not story_has_flag("tam_c04_w09_calendar_advanced"):
        call career_bonus_process_checkpoint("tam_c04_w09")
    $ time_story_advance_days_once("tam_c04_w09_calendar_advanced", 5)
    $ time_story_begin_workweek("tam_c04_w10_calendar_started")
    call tam_c04_w10_s01_monday_phone_pulse
    call tam_c04_w10_s02_client_incident
    call tam_c04_w10_s03_hoang_does_not_wait_forever
    call tam_c04_w10_s04_quang_respects_the_closed_door
    call tam_c04_w10_s05_huyen_notices_quan_tired
    call tam_c04_w10_s06_friday_no_substitute
    call career_bonus_process_checkpoint("tam_c04_w10")
    $ time_story_advance_days_once("tam_c04_w10_calendar_advanced", 5)
    $ story_flag("tam_c04_w10_completed")
    $ story_flag("tam_c04_w10_weekend_open")
    $ phone_refresh_all()
    $ time_start_period_after_chapter("tam_c04_w10_no_one_stands_in")
    jump route_map

label tam_c04_w11_cannot_pretend:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_begin_checkpoint("tam_c04_w11")
    if story_has_flag("tam_c04_w10_completed") and not story_has_flag("tam_c04_w10_calendar_advanced"):
        call career_bonus_process_checkpoint("tam_c04_w10")
    $ time_story_advance_days_once("tam_c04_w10_calendar_advanced", 5)
    $ time_story_begin_workweek("tam_c04_w11_calendar_started")
    call tam_c04_w11_s01_monday_phone_pulse
    call tam_c04_w11_s02_tam_owns_the_mistake
    call tam_c04_w11_s03_hoang_not_leftover_time
    call tam_c04_w11_s04_huyen_catches_quan_error
    call tam_c04_w11_s05_thienan_asks_who_tam_is_helping
    call tam_c04_w11_s06_friday_one_real_answer
    call career_bonus_process_checkpoint("tam_c04_w11")
    $ time_story_advance_days_once("tam_c04_w11_calendar_advanced", 5)
    $ story_flag("tam_c04_w11_completed")
    $ story_flag("tam_c04_w11_weekend_open")
    $ phone_refresh_all()
    $ time_start_period_after_chapter("tam_c04_w11_cannot_pretend")
    jump route_map

label tam_c04_w12_three_month_review:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_begin_checkpoint("tam_c04_w12")
    if story_has_flag("tam_c04_w11_completed") and not story_has_flag("tam_c04_w11_calendar_advanced"):
        call career_bonus_process_checkpoint("tam_c04_w11")
    $ time_story_advance_days_once("tam_c04_w11_calendar_advanced", 5)
    $ time_story_begin_workweek("tam_c04_w12_calendar_started")
    call tam_c04_w12_s01_monday_phone_pulse
    call tam_c04_w12_s02_three_month_work_review
    call tam_c04_w12_s03_hoang_asks_for_clear_no
    call tam_c04_w12_s04_quang_at_family_dinner
    call tam_c04_w12_s05_huyen_after_quarter_review
    call tam_c04_w12_s06_month_three_priority
    call tam_c04_w12_s07_month_three_snapshot
    call career_bonus_process_checkpoint("tam_c04_w12")
    $ time_story_advance_days_once("tam_c04_w12_calendar_advanced", 5)
    $ story_flag("tam_c04_w12_completed")
    $ story_flag("tam_c04_month_03_completed")
    $ story_flag("tam_c04_w12_weekend_open")
    $ phone_refresh_all()
    $ time_start_period_after_chapter("tam_c04_w12_three_month_review")
    jump route_map

label tam_c04_w13_departures:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_begin_checkpoint("tam_c04_w13")
    if story_has_flag("tam_c04_w12_completed") and not story_has_flag("tam_c04_w12_calendar_advanced"):
        call career_bonus_process_checkpoint("tam_c04_w12")
    $ time_story_advance_days_once("tam_c04_w12_calendar_advanced", 5)
    $ time_story_begin_workweek("tam_c04_w13_calendar_started")
    call tam_c04_w13_s01_monday_phone_pulse
    call tam_c04_w13_s02_south_assignment
    call tam_c04_w13_s03_hoang_fixed_evening
    call tam_c04_w13_s04_quan_asks_huyen_pickup
    call tam_c04_w13_s05_friday_departures
    call career_bonus_process_checkpoint("tam_c04_w13")
    $ time_story_advance_days_once("tam_c04_w13_calendar_advanced", 5)
    $ story_flag("tam_c04_w13_completed")
    $ story_flag("tam_c04_w13_weekend_open")
    $ phone_refresh_all()
    $ time_start_period_after_chapter("tam_c04_w13_departures")
    jump route_map

label tam_c04_w14_quiet_house:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_begin_checkpoint("tam_c04_w14")
    if story_has_flag("tam_c04_w13_completed") and not story_has_flag("tam_c04_w13_calendar_advanced"):
        call career_bonus_process_checkpoint("tam_c04_w13")
    $ time_story_advance_days_once("tam_c04_w13_calendar_advanced", 5)
    $ time_story_begin_workweek("tam_c04_w14_calendar_started")
    call tam_c04_w14_s01_monday_phone_pulse
    call tam_c04_w14_s02_huyen_meets_anh_nhi
    call tam_c04_w14_s03_hoang_missed_call
    call tam_c04_w14_s04_tam_carries_own_work
    call tam_c04_w14_s05_friday_quiet_house
    call career_bonus_process_checkpoint("tam_c04_w14")
    $ time_story_advance_days_once("tam_c04_w14_calendar_advanced", 5)
    $ story_flag("tam_c04_w14_completed")
    $ story_flag("tam_c04_w14_weekend_open")
    $ phone_refresh_all()
    $ time_start_period_after_chapter("tam_c04_w14_quiet_house")
    jump route_map

label tam_c04_w15_distance_has_weight:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_begin_checkpoint("tam_c04_w15")
    if story_has_flag("tam_c04_w14_completed") and not story_has_flag("tam_c04_w14_calendar_advanced"):
        call career_bonus_process_checkpoint("tam_c04_w14")
    $ time_story_advance_days_once("tam_c04_w14_calendar_advanced", 5)
    $ time_story_begin_workweek("tam_c04_w15_calendar_started")
    call tam_c04_w15_s01_monday_phone_pulse
    call tam_c04_w15_s02_south_branch_late_night
    call tam_c04_w15_s03_quang_message_after_midnight
    call tam_c04_w15_s04_huyen_weekend_with_anh_nhi
    call tam_c04_w15_s05_friday_distance_choice
    call career_bonus_process_checkpoint("tam_c04_w15")
    $ time_story_advance_days_once("tam_c04_w15_calendar_advanced", 5)
    $ story_flag("tam_c04_w15_completed")
    $ story_flag("tam_c04_w15_weekend_open")
    $ phone_refresh_all()
    $ time_start_period_after_chapter("tam_c04_w15_distance_has_weight")
    jump route_map

label tam_c04_w16_month_four_review:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_begin_checkpoint("tam_c04_w16")
    if story_has_flag("tam_c04_w15_completed") and not story_has_flag("tam_c04_w15_calendar_advanced"):
        call career_bonus_process_checkpoint("tam_c04_w15")
    $ time_story_advance_days_once("tam_c04_w15_calendar_advanced", 5)
    $ time_story_begin_workweek("tam_c04_w16_calendar_started")
    call tam_c04_w16_s01_monday_phone_pulse
    call tam_c04_w16_s02_trip_return_delay
    call tam_c04_w16_s03_hoang_one_evening
    call tam_c04_w16_s04_quan_returns_home
    call tam_c04_w16_s05_month_four_priority
    call tam_c04_w16_s06_month_four_snapshot
    call career_bonus_process_checkpoint("tam_c04_w16")
    $ time_story_advance_days_once("tam_c04_w16_calendar_advanced", 5)
    $ story_flag("tam_c04_w16_completed")
    $ story_flag("tam_c04_month_04_completed")
    $ story_flag("tam_c04_w16_weekend_open")
    $ phone_refresh_all()
    $ time_start_period_after_chapter("tam_c04_w16_month_four_review")
    jump route_map

label tam_c04_w17_returns:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_begin_checkpoint("tam_c04_w17")
    if story_has_flag("tam_c04_w16_completed") and not story_has_flag("tam_c04_w16_calendar_advanced"):
        call career_bonus_process_checkpoint("tam_c04_w16")
    $ time_story_advance_days_once("tam_c04_w16_calendar_advanced", 5)
    $ time_story_begin_workweek("tam_c04_w17_calendar_started")
    call tam_c04_w17_s01_monday_phone_pulse
    call tam_c04_w17_s02_south_return
    call tam_c04_w17_s03_quang_chooses_conversation
    call tam_c04_w17_s04_huyen_knows_the_house
    call tam_c04_w17_s05_hoang_sunday_plan
    call tam_c04_w17_s06_friday_before_answer
    call career_bonus_process_checkpoint("tam_c04_w17")
    $ time_story_advance_days_once("tam_c04_w17_calendar_advanced", 5)
    $ story_flag("tam_c04_w17_completed")
    $ story_flag("tam_c04_w17_weekend_open")
    $ phone_refresh_all()
    $ time_start_period_after_chapter("tam_c04_w17_returns")
    jump route_map

label tam_c04_w18_choose_an_answer:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_begin_checkpoint("tam_c04_w18")
    if story_has_flag("tam_c04_w17_completed") and not story_has_flag("tam_c04_w17_calendar_advanced"):
        call career_bonus_process_checkpoint("tam_c04_w17")
    $ time_story_advance_days_once("tam_c04_w17_calendar_advanced", 5)
    $ time_story_begin_workweek("tam_c04_w18_calendar_started")
    call tam_c04_w18_s01_monday_phone_pulse
    call tam_c04_w18_s02_tam_romance_decision
    call tam_c04_w18_s03_after_decision
    call tam_c04_w18_s04_career_ownership
    call tam_c04_w18_s05_friday_new_phase
    call career_bonus_process_checkpoint("tam_c04_w18")
    $ time_story_advance_days_once("tam_c04_w18_calendar_advanced", 5)
    $ story_flag("tam_c04_w18_completed")
    $ story_flag("tam_c04_w18_weekend_open")
    $ phone_refresh_all()
    $ time_start_period_after_chapter("tam_c04_w18_choose_an_answer")
    jump route_map

label tam_c04_w19_after_the_answer:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_begin_checkpoint("tam_c04_w19")
    if story_has_flag("tam_c04_w18_completed") and not story_has_flag("tam_c04_w18_calendar_advanced"):
        call career_bonus_process_checkpoint("tam_c04_w18")
    $ time_story_advance_days_once("tam_c04_w18_calendar_advanced", 5)
    $ time_story_begin_workweek("tam_c04_w19_calendar_started")
    call tam_c04_w19_s01_monday_phone_pulse
    call tam_c04_w19_s02_first_week_after_choice
    call tam_c04_w19_s03_quang_thienan_no_longer_refuses
    call tam_c04_w19_s04_huyen_anh_nhi_school_project
    call tam_c04_w19_s05_hoang_contact_or_silence
    call tam_c04_w19_s06_friday_phase_check
    call career_bonus_process_checkpoint("tam_c04_w19")
    if relationship_get_phase("tam_hoang") == "dating":
        $ relationship_resolve_contact_period("tam_hoang", "tam_c04_w19")
    $ time_story_advance_days_once("tam_c04_w19_calendar_advanced", 5)
    $ story_flag("tam_c04_w19_completed")
    $ story_flag("tam_c04_w19_weekend_open")
    $ phone_refresh_all()
    $ time_start_period_after_chapter("tam_c04_w19_after_the_answer")
    jump route_map

label tam_c04_w20_month_five_review:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_begin_checkpoint("tam_c04_w20")
    if story_has_flag("tam_c04_w19_completed") and not story_has_flag("tam_c04_w19_calendar_advanced"):
        call career_bonus_process_checkpoint("tam_c04_w19")
    $ time_story_advance_days_once("tam_c04_w19_calendar_advanced", 5)
    $ time_story_begin_workweek("tam_c04_w20_calendar_started")
    call tam_c04_w20_s01_monday_phone_pulse
    call tam_c04_w20_s02_relationship_maintenance_result
    call tam_c04_w20_s03_quang_thienan_month_five_choice
    call tam_c04_w20_s04_huyen_quan_or_hoang_seed_check
    call tam_c04_w20_s05_month_five_snapshot
    call career_bonus_process_checkpoint("tam_c04_w20")
    # if relationship_get_phase("tam_hoang") == "dating":
    #     $ relationship_resolve_contact_period("tam_hoang", "tam_c04_w20")
    $ time_story_advance_days_once("tam_c04_w20_calendar_advanced", 5)
    $ story_flag("tam_c04_w20_completed")
    $ story_flag("tam_c04_month_05_completed")
    $ story_flag("tam_c04_w20_weekend_open")
    $ phone_refresh_all()
    $ time_start_period_after_chapter("tam_c04_w20_month_five_review")
    jump route_map

label tam_c04_w21_new_routine:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_begin_checkpoint("tam_c04_w21")
    if story_has_flag("tam_c04_w20_completed") and not story_has_flag("tam_c04_w20_calendar_advanced"):
        call career_bonus_process_checkpoint("tam_c04_w20")
    $ time_story_advance_days_once("tam_c04_w20_calendar_advanced", 5)
    $ time_story_begin_workweek("tam_c04_w21_calendar_started")
    call tam_c04_w21_s01_monday_phone_pulse
    call tam_c04_w21_s02_ordinary_day_after_labels
    call tam_c04_w21_s03_quan_second_trip_request
    call tam_c04_w21_s04_independent_opportunity
    call tam_c04_w21_s05_friday_new_routine
    call career_bonus_process_checkpoint("tam_c04_w21")
    if relationship_get_phase("tam_hoang") == "dating":
        $ relationship_resolve_contact_period("tam_hoang", "tam_c04_w21")
    $ time_story_advance_days_once("tam_c04_w21_calendar_advanced", 5)
    $ story_flag("tam_c04_w21_completed")
    $ story_flag("tam_c04_w21_weekend_open")
    $ phone_refresh_all()
    $ time_start_period_after_chapter("tam_c04_w21_new_routine")
    jump route_map

label tam_c04_w22_when_work_interrupts:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_begin_checkpoint("tam_c04_w22")
    if story_has_flag("tam_c04_w21_completed") and not story_has_flag("tam_c04_w21_calendar_advanced"):
        call career_bonus_process_checkpoint("tam_c04_w21")
    $ time_story_advance_days_once("tam_c04_w21_calendar_advanced", 5)
    $ time_story_begin_workweek("tam_c04_w22_calendar_started")
    call tam_c04_w22_s01_monday_phone_pulse
    call tam_c04_w22_s02_route_specific_busy_week
    call tam_c04_w22_s03_thienan_keeps_door_open
    call tam_c04_w22_s04_huyen_anh_nhi_sleepover
    call tam_c04_w22_s05_friday_maintenance
    call career_bonus_process_checkpoint("tam_c04_w22")
    if relationship_get_phase("tam_hoang") == "dating":
        $ relationship_resolve_contact_period("tam_hoang", "tam_c04_w22")
    $ time_story_advance_days_once("tam_c04_w22_calendar_advanced", 5)
    $ story_flag("tam_c04_w22_completed")
    $ story_flag("tam_c04_w22_weekend_open")
    $ phone_refresh_all()
    $ time_start_period_after_chapter("tam_c04_w22_when_work_interrupts")
    jump route_map

label tam_c04_w23_new_balance:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_begin_checkpoint("tam_c04_w23")
    if story_has_flag("tam_c04_w22_completed") and not story_has_flag("tam_c04_w22_calendar_advanced"):
        call career_bonus_process_checkpoint("tam_c04_w22")
    $ time_story_advance_days_once("tam_c04_w22_calendar_advanced", 5)
    $ time_story_begin_workweek("tam_c04_w23_calendar_started")
    call tam_c04_w23_s01_monday_phone_pulse
    call tam_c04_w23_s02_group_dinner_new_balance
    call tam_c04_w23_s03_huyen_hoang_friend_seed
    call tam_c04_w23_s04_career_delivery_without_quan
    call tam_c04_w23_s05_friday_before_final_review
    call career_bonus_process_checkpoint("tam_c04_w23")
    if relationship_get_phase("tam_hoang") == "dating":
        $ relationship_resolve_contact_period("tam_hoang", "tam_c04_w23")
    $ time_story_advance_days_once("tam_c04_w23_calendar_advanced", 5)
    $ story_flag("tam_c04_w23_completed")
    $ story_flag("tam_c04_w23_weekend_open")
    $ phone_refresh_all()
    $ time_start_period_after_chapter("tam_c04_w23_new_balance")
    jump route_map

label tam_c04_w24_six_month_finale:
    $ tam_c04_ensure_extended_story_state()
    $ career_bonus_begin_checkpoint("tam_c04_w24")
    if story_has_flag("tam_c04_w23_completed") and not story_has_flag("tam_c04_w23_calendar_advanced"):
        call career_bonus_process_checkpoint("tam_c04_w23")
    $ time_story_advance_days_once("tam_c04_w23_calendar_advanced", 5)
    $ time_story_begin_workweek("tam_c04_w24_calendar_started")
    call tam_c04_w24_s01_monday_phone_pulse
    call tam_c04_w24_s02_six_month_work_review
    call tam_c04_w24_s03_tam_route_finale
    call tam_c04_w24_s04_quang_thienan_finale
    call tam_c04_w24_s05_huyen_quan_finale
    call tam_c04_w24_s06_final_snapshot
    call tam_c04_w24_s07_chapter_close
    call career_bonus_process_checkpoint("tam_c04_w24")
    # if relationship_get_phase("tam_hoang") == "dating":
    #     $ relationship_resolve_contact_period("tam_hoang", "tam_c04_w24")
    $ time_story_advance_days_once("tam_c04_w24_calendar_advanced", 5)
    $ story_flag("tam_c04_w24_completed")
    $ story_flag("tam_c04_month_06_completed")
    $ story_complete_chapter("tam_c04_between_work_and_hearts")
    $ phone_refresh_all()
    $ time_start_period_after_chapter("tam_c04_w24_six_month_finale")
    jump route_map

label tam_c04_post_season_handoff:
    $ story_flag("tam_c04_post_season_ready")
    $ phone_refresh_all()
    jump route_map
