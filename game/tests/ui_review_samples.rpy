# Screenshot-only review coverage for the four prototype screen layouts.
# Run with an isolated --savedir, following the other UI test suites.
testsuite ui_review_samples:
    parameter language = [None, "vietnamese"]
    parameter profile = [(1920, 1080, False), (960, 540, True), (800, 450, True)]

    setup:
        $ _test.timeout = 25.0
        $ _test.transition_timeout = 0.1
        $ _test.screenshot_directory = "tests/screenshots/ui_review_samples"
        run Language(language)
        $ renpy.set_physical_size((profile[0], profile[1]))
        $ ui_review_suffix = (language or "english") + "_" + str(profile[0]) + "x" + str(profile[1])
        $ ui_review_compact = profile[2]
        $ initialize_progression()
        $ phone_ensure_state()

    testcase prototype_screen_samples:
        run Show("ui_review_settings", compact=ui_review_compact)
        pause 0.8
        assert screen "ui_review_settings"
        screenshot ("01_settings_" + ui_review_suffix + ".png")
        if eval ui_review_compact:
            click id "review_tab_text"
            assert eval renpy.get_screen_variable("review_settings_tab", screen="ui_review_settings") == "text"
            pause 0.3
            screenshot ("01b_reading_settings_" + ui_review_suffix + ".png")
            click id "review_tab_audio"
            assert eval renpy.get_screen_variable("review_settings_tab", screen="ui_review_settings") == "audio"
            pause 0.3
            screenshot ("01c_audio_settings_" + ui_review_suffix + ".png")
        run Hide("ui_review_settings")

        run Show("ui_review_library", compact=ui_review_compact)
        pause 0.8
        assert screen "ui_review_library"
        screenshot ("02_library_" + ui_review_suffix + ".png")
        if eval ui_review_compact:
            scroll amount 10 pos (1100, 700)
            assert eval renpy.get_widget("ui_review_library", "review_library_scroll").yadjustment.value > 0
            pause 0.3
            screenshot ("02b_library_scrolled_" + ui_review_suffix + ".png")
        run Hide("ui_review_library")

        run Show("ui_review_phone", compact=ui_review_compact)
        pause 0.8
        assert screen "ui_review_phone"
        screenshot ("03_phone_" + ui_review_suffix + ".png")
        if eval ui_review_compact:
            click id "review_phone_list"
            assert eval renpy.get_screen_variable("compact_list", screen="ui_review_phone")
            pause 0.3
            screenshot ("03b_phone_list_" + ui_review_suffix + ".png")
        run Hide("ui_review_phone")

        run Show("ui_review_reader", compact=ui_review_compact)
        pause 0.8
        assert screen "ui_review_reader"
        screenshot ("04_reader_" + ui_review_suffix + ".png")
        click id "review_next"
        assert eval renpy.get_screen_variable("page_index", screen="ui_review_reader") == 13
        click id "review_previous"
        assert eval renpy.get_screen_variable("page_index", screen="ui_review_reader") == 12
        click id "review_hide_ui"
        assert eval renpy.get_screen_variable("reading_hidden", screen="ui_review_reader")
        pause 0.3
        screenshot ("04b_artwork_" + ui_review_suffix + ".png")
        click id "review_show_ui"
        assert eval not renpy.get_screen_variable("reading_hidden", screen="ui_review_reader")
        run Hide("ui_review_reader")
