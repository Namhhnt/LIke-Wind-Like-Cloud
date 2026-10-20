testsuite ui_menu_refresh:
    parameter language = [None, "vietnamese"]
    parameter window_size = [(1920, 1080), (1280, 720)]

    setup:
        $ _test.timeout = 25.0
        $ _test.transition_timeout = 0.1
        $ _test.screenshot_directory = "tests/screenshots/ui_menu_refresh"
        run Language(language)
        $ renpy.set_physical_size(window_size)
        $ menu_test_suffix = (language or "english") + "_" + str(window_size[0])
        $ initialize_progression()

    testcase menu_and_reader:
        run ShowMenu("preferences")
        pause 0.5
        assert screen "preferences"
        screenshot ("01_settings_" + menu_test_suffix + ".png")
        $ menu_prior_text_speed = _preferences.text_cps
        click id "pref_text_speed"
        assert eval 0 < _preferences.text_cps < 200
        $ _preferences.text_cps = menu_prior_text_speed
        scroll amount 12 pos (1000, 600)
        pause 0.3
        assert eval renpy.get_widget("preferences", "menu_content_scroll").yadjustment.value > 0
        screenshot ("01_settings_scrolled_" + menu_test_suffix + ".png")
        run ShowMenu("load")
        pause 0.8
        assert screen "load"
        screenshot ("02_load_" + menu_test_suffix + ".png")
        # ShowMenu intentionally disables Save at the title screen; inspect its
        # layout directly without performing a save or changing player data.
        run Show("save")
        pause 0.8
        assert screen "save"
        screenshot ("02_save_" + menu_test_suffix + ".png")
        run ShowMenu("about")
        pause 0.8
        assert screen "about"
        screenshot ("03_about_" + menu_test_suffix + ".png")
        run ShowMenu("help")
        pause 0.8
        assert screen "help"
        screenshot ("04_help_" + menu_test_suffix + ".png")
        run ShowMenu("history")
        pause 0.8
        assert screen "history"
        screenshot ("05_history_" + menu_test_suffix + ".png")
        run ShowMenu("library")
        pause 0.8
        screenshot ("06_library_" + menu_test_suffix + ".png")
        run ShowMenu("library_story_reader", content_id="yuuka_minh_sunday_market")
        pause 0.8
        assert screen "library_story_reader"
        assert eval not renpy.get_widget("library_story_reader", "story_previous").is_sensitive()
        click id "story_next"
        click id "story_next"
        click id "story_next"
        assert eval renpy.get_screen_variable("page_index", screen="library_story_reader") == 3
        pause 0.3
        screenshot ("07_reader_" + menu_test_suffix + ".png")
        click id "story_previous"
        assert eval renpy.get_screen_variable("page_index", screen="library_story_reader") == 2
        keysym "game_menu"
        assert screen "library_stories"
        run Show("confirm", message=_("Quit"), yes_action=Hide("confirm"), no_action=Hide("confirm"))
        pause 0.5
        assert screen "confirm"
        screenshot ("08_confirm_" + menu_test_suffix + ".png")
        keysym "game_menu"
        assert eval renpy.get_screen("confirm") is None
