screen library_menu_shell(page_title, page_subtitle, back_action=ShowMenu("main_menu"), back_label=_("Back")):

    add (mm_theme_asset("background_full.png") if mm_loadable(mm_theme_asset("background_full.png")) else Solid("#15120f")) fit "cover"
    add Solid("#00000066")

    key "game_menu" action back_action
    key "K_ESCAPE" action back_action

    fixed:
        xysize (1920, 1080)

        vbox:
            xpos 72
            ypos 58
            spacing 6

            text page_title style "library_title_text"
            text page_subtitle style "library_subtitle_text"

        frame:
            xpos 72
            ypos 210
            xsize 1760
            ysize 740
            background ui_frame_or_solid(mm_theme_asset("content_panel_frame.png"), LIB_PANEL_SOFT, 40)

            fixed:
                xpos 42
                ypos 36
                xsize 1676
                ysize 668

                transclude

        textbutton back_label:
            xpos 72
            ypos 972
            action back_action
            text_style "library_back_button_text"

    use main_menu_top_controls


screen library():

    tag menu

    use library_menu_shell(
        page_title=_("Library"),
        page_subtitle=_("Explore special contents of Like Wind, Like Cloud")
    ):

        hbox:
            spacing 38
            vbox:
                xsize 370
                spacing 20
                textbutton _("Start") action Show("main_menu_start_prompt") text_style "library_back_button_text"
                textbutton _("Continue") action ShowMenu("load") text_style "library_back_button_text"
                textbutton _("Story Chapters") action Start("route_map_timeline") text_style "library_back_button_text"
                text _("Library") style "library_back_button_text" color LIB_GOLD
                textbutton _("Settings") action ShowMenu("preferences") text_style "library_back_button_text"

            grid 3 2:
                spacing 24
                for category in LIBRARY_CATEGORIES:
                    use library_category_card(category)


screen library_category_card(category):

    $ unlocked = library_category_is_unlocked(category["id"])
    $ progress_text = library_get_progress_text(category["id"])
    $ empty_category = progress_text.replace(" ", "") == "0/0"
    $ action = ShowMenu(category["screen"]) if unlocked else NullAction()
    $ idle_background = ui_frame_or_solid("gui/library/card_idle.png", LIB_PANEL, 24)
    $ hover_background = ui_frame_or_solid("gui/library/card_hover.png", LIB_PANEL_HOVER, 24)

    button:
        xsize 382
        ysize 292
        action action
        sensitive unlocked
        background idle_background
        hover_background hover_background
        insensitive_background idle_background

        vbox:
            xpos 28
            ypos 24
            xsize 326
            ysize 236
            spacing 12

            text category["icon_text"]:
                style "library_card_icon_text"
                color (LIB_GOLD if unlocked and not empty_category else LIB_DISABLED)

            text _(category["title"]):
                style "library_card_title"
                color (LIB_TEXT if unlocked and not empty_category else LIB_DISABLED)

            text _(category["subtitle"]):
                style "library_card_subtitle"
                color (LIB_MUTED if unlocked else LIB_DISABLED)

            null height 12

            hbox:
                xfill True
                yalign 1.0

                text (_("No content yet") if empty_category else progress_text):
                    style "library_card_progress"
                    color (LIB_GOLD if unlocked else LIB_DISABLED)

                null xfill True

                text ("›" if unlocked else _("Locked")):
                    style "library_card_arrow"
                    color (LIB_GOLD if unlocked else LIB_DISABLED)
