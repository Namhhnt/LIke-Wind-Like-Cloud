# Production menu screenshot and smoke coverage. Run with an isolated --savedir.
testsuite ui_consistency_localization:
    testcase formatted_labels:
        run Language("vietnamese")
        $ renpy.set_physical_size((800, 450))
        $ _test.screenshot_directory = "tests/screenshots/ui_consistency_live"
        $ initialize_progression()
        assert eval ui_translate("Series") != "Series"
        assert eval ui_translate("Read status: %(status)s") != "Read status: %(status)s"
        run ShowMenu("library_stories")
        pause 0.7
        assert screen "library_stories"
        screenshot "09_library_stories_vietnamese_800x450.png"

testsuite ui_consistency_live:
    parameter language = [None, "vietnamese"]
    parameter window_size = [(1920, 1080), (800, 450)]

    setup:
        $ _test.timeout = 60.0
        $ _test.transition_timeout = 0.1
        $ _test.screenshot_directory = "tests/screenshots/ui_consistency_live"
        run Language(language)
        $ renpy.set_physical_size(window_size)
        $ ui_live_suffix = (language or "english") + "_" + str(window_size[0]) + "x" + str(window_size[1])
        $ ui_live_compact = ui_is_compact()
        $ initialize_progression()
        $ phone_ensure_state()
        $ phone_state["unlocked_threads"] = list(PHONE_THREADS)

    testcase production_menu_screens:
        run ShowMenu("main_menu")
        pause 0.8
        assert screen "main_menu"
        screenshot ("01_main_" + ui_live_suffix + ".png")

        run ShowMenu("preferences")
        pause 0.8
        assert screen "preferences"
        screenshot ("02_preferences_" + ui_live_suffix + ".png")
        if eval ui_live_compact:
            click id "preferences_tab_text"
            assert eval renpy.get_screen_variable("preferences_tab", screen="preferences") == "text"
            screenshot ("02b_reading_" + ui_live_suffix + ".png")
            click id "preferences_tab_audio"
            assert eval renpy.get_screen_variable("preferences_tab", screen="preferences") == "audio"
            screenshot ("02c_audio_" + ui_live_suffix + ".png")
            click id "menu_navigation_toggle"
            pause 0.3
            screenshot ("02d_navigation_" + ui_live_suffix + ".png")

        run ShowMenu("load")
        pause 0.8
        assert screen "load"
        screenshot ("03_load_" + ui_live_suffix + ".png")
        run Show("save")
        pause 0.4
        assert screen "save"
        screenshot ("03b_save_" + ui_live_suffix + ".png")

        run ShowMenu("help")
        pause 0.8
        assert screen "help"
        screenshot ("04_help_" + ui_live_suffix + ".png")

        run ShowMenu("about")
        pause 0.8
        assert screen "about"
        screenshot ("05_about_" + ui_live_suffix + ".png")

        run ShowMenu("history")
        pause 0.8
        assert screen "history"
        screenshot ("06_history_" + ui_live_suffix + ".png")

        run ShowMenu("library")
        pause 0.8
        assert screen "library"
        screenshot ("07_library_" + ui_live_suffix + ".png")

        run ShowMenu("library_characters")
        pause 0.8
        assert screen "library_characters"
        screenshot ("08_library_characters_" + ui_live_suffix + ".png")

        run ShowMenu("library_stories")
        pause 0.8
        assert screen "library_stories"
        screenshot ("09_library_stories_" + ui_live_suffix + ".png")

        run ShowMenu("library_cg")
        pause 0.8
        assert screen "library_cg"
        screenshot ("10_library_cg_" + ui_live_suffix + ".png")

        run ShowMenu("library_music")
        pause 0.8
        assert screen "library_music"
        screenshot ("11_library_music_" + ui_live_suffix + ".png")

        run ShowMenu("library_minigames")
        pause 0.8
        assert screen "library_minigames"
        screenshot ("12_library_minigames_" + ui_live_suffix + ".png")

        run ShowMenu("library_extras")
        pause 0.8
        assert screen "library_extras"
        screenshot ("13_library_extras_" + ui_live_suffix + ".png")
        run ShowMenu("timeline_chapter_map")
        pause 0.5
        assert screen "timeline_chapter_map"
        screenshot ("13b_timeline_" + ui_live_suffix + ".png")

        run ShowMenu("library_story_reader", content_id="yuuka_minh_sunday_market")
        pause 0.8
        assert screen "library_story_reader"
        assert eval not renpy.get_widget("library_story_reader", "story_previous").is_sensitive()
        screenshot ("14_reader_" + ui_live_suffix + ".png")
        click id "story_next"
        assert eval renpy.get_screen_variable("page_index", screen="library_story_reader") == 1
        click id "story_previous"
        assert eval renpy.get_screen_variable("page_index", screen="library_story_reader") == 0
        $ renpy.set_screen_variable("page_index", 12, screen="library_story_reader")
        $ renpy.restart_interaction()
        pause 0.4
        screenshot ("14c_reader_cg_" + ui_live_suffix + ".png")
        if eval ui_live_compact:
            click id "story_hide_ui"
            assert eval renpy.get_screen_variable("reading_hidden", screen="library_story_reader")
            pause 0.3
            screenshot ("14b_reader_artwork_" + ui_live_suffix + ".png")
            click id "story_show_ui"
            assert eval not renpy.get_screen_variable("reading_hidden", screen="library_story_reader")

        run ShowMenu("phone_home")
        pause 0.8
        assert screen "phone_home"
        screenshot ("15_phone_" + ui_live_suffix + ".png")
        click id "phone_app_messages"
        pause 0.3
        assert eval renpy.get_screen_variable("active_tab", screen="phone_home") == "messages"
        screenshot ("15b_phone_messages_" + ui_live_suffix + ".png")
        keysym "game_menu"
        assert eval renpy.get_screen_variable("active_tab", screen="phone_home") == "home"
        if eval ui_live_compact:
            click id "phone_close"
        else:
            keysym "game_menu"
        assert eval renpy.get_screen("phone_home") is None

        run Show("confirm", message=_("Quit"), yes_action=Hide("confirm"), no_action=Hide("confirm"))
        pause 0.8
        assert screen "confirm"
        screenshot ("16_confirm_" + ui_live_suffix + ".png")
        keysym "game_menu"
        assert eval renpy.get_screen("confirm") is None
