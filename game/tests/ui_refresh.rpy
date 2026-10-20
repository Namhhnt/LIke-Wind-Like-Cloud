# Run with the installed Windows SDK (8.5+) and an isolated --savedir.
# Fixtures exist only during tests; never unlock content in the player's save.
testsuite global:
    teardown:
        exit

testsuite ui_refresh:
    parameter language = [None, "vietnamese"]
    parameter window_size = [(1920, 1080), (1280, 720)]

    setup:
        $ _test.timeout = 12.0
        $ _test.transition_timeout = 0.1
        $ _test.screenshot_directory = "tests/screenshots/ui_refresh"
        run Language(language)
        $ renpy.set_physical_size(window_size)
        $ ui_test_suffix = (language or "english") + "_" + str(window_size[0])
        $ initialize_progression()
        $ phone_ensure_state()
        $ phone_state["unlocked_threads"] = list(PHONE_THREADS)

    teardown:
        run ShowMenu("main_menu")

    testcase approved_screens:
        run ShowMenu("main_menu")
        pause 0.5
        assert screen "main_menu"
        screenshot ("01_menu_" + ui_test_suffix + ".png")
        run ShowMenu("library")
        pause 0.5
        assert screen "library"
        if eval language == "vietnamese":
            assert eval renpy.translate_string("CG Gallery", language="vietnamese") == "Bộ sưu tập CG"
            assert eval renpy.translate_string("Extras", language="vietnamese") == "Nội dung thêm"
        screenshot ("04_library_" + ui_test_suffix + ".png")
        run ShowMenu("library_characters")
        pause 0.5
        assert screen "library_characters"
        screenshot ("05_profiles_" + ui_test_suffix + ".png")
        run ShowMenu("phone_home")
        pause 0.5
        assert screen "phone_home"
        screenshot ("06_phone_" + ui_test_suffix + ".png")
        click id "phone_app_messages"
        pause 0.5
        screenshot ("07_messages_" + ui_test_suffix + ".png")
        $ ui_test_thread = next(iter(PHONE_REPLY_CHOICES))
        $ renpy.set_screen_variable("selected_thread_id", ui_test_thread, screen="phone_home")
        $ renpy.restart_interaction()
        pause 0.5
        assert eval renpy.get_screen_variable("selected_thread_id", screen="phone_home") == ui_test_thread
        screenshot ("08_conversation_" + ui_test_suffix + ".png")
        keysym "game_menu"
        assert eval renpy.get_screen_variable("selected_thread_id", screen="phone_home") is None
        $ progress["completed"] = ["prologue_rain_dream", "tam_c01_interview_day", "tam_c02_company_party"]
        $ initialize_progression()
        run ShowMenu("timeline_chapter_map")
        pause 0.5
        assert screen "timeline_chapter_map"
        screenshot ("03_timeline_" + ui_test_suffix + ".png")
        $ initialize_progression()
        $ ui_test_entries = build_map_entries(context_id="act1_default")
        run ShowMenu("interactive_map_screen", entries=ui_test_entries, allow_timeline=True)
        pause 0.5
        assert screen "interactive_map_screen"
        click id ("map_location_" + ui_test_entries[0]["id"])
        assert eval renpy.get_screen_variable("focus_target_entry", screen="interactive_map_screen")["id"] == ui_test_entries[0]["id"]
        move pos (10, 10)
        pause 0.1
        screenshot ("02_map_" + ui_test_suffix + ".png")
        $ ui_activity_fixture = ensure_activity_state()
        $ ui_prior_activity_fixture = dict(ui_activity_fixture)
        $ ui_activity_fixture["work_expected_today"] = True
        $ ui_activity_fixture["work_completed_today"] = False
        $ ui_activity_fixture["current_period_id"] = next(iter(INTER_CHAPTER_PERIODS))
        $ renpy.restart_interaction()
        pause 0.4
        assert eval bool(time_get_main_today_summary()) and time_skip_is_available()
        screenshot ("10_map_active_" + ui_test_suffix + ".png")
        $ ui_activity_fixture.clear()
        $ ui_activity_fixture.update(ui_prior_activity_fixture)
        $ renpy.restart_interaction()
        $ ui_locked_entry = next((entry for entry in ui_test_entries if entry.get("state") == "locked"), None)
        if eval ui_locked_entry is not None:
            $ renpy.set_screen_variable("focus_target_entry", ui_locked_entry, screen="interactive_map_screen")
            $ renpy.restart_interaction()
            pause 0.2
            assert eval not renpy.get_widget("interactive_map_screen", "map_go_to_location").is_sensitive()
        run ShowMenu("main_menu")
        pause 0.6
        run Show("main_menu_start_prompt")
        pause 0.6
        screenshot ("09_start_prompt_" + ui_test_suffix + ".png")
        run Hide("main_menu_start_prompt")
