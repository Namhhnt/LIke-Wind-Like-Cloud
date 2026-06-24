screen library_menu_shell(page_title, page_subtitle, back_action=ShowMenu("main_menu"), back_label=_("Back")):

    add (mm_theme_asset("background_full.png") if mm_loadable(mm_theme_asset("background_full.png")) else Solid("#15120f")) fit "cover"
    add Solid("#00000066")

    use main_menu_top_controls

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
            ypos 225
            xsize 460
            ysize 505
            background (Frame(mm_theme_asset("menu_panel_frame.png"), 36, 36) if mm_loadable(mm_theme_asset("menu_panel_frame.png")) else Solid(LIB_PANEL))

            vbox:
                xpos 26
                ypos 24
                spacing 4

                use main_menu_nav_button(label=_("Start"), action=Start(), icon_text="❧")
                use main_menu_nav_button(label=_("Continue"), action=ShowMenu("load"), icon_text="◷")
                use main_menu_nav_button(label=_("Story Chapters"), action=Start("route_map"), icon_text="▦")
                use main_menu_nav_button(label=_("Library"), action=NullAction(), primary=True, icon_text="▧")
                use main_menu_nav_button(label=_("Settings"), action=ShowMenu("preferences"), icon_text="⚙")
                use main_menu_nav_button(label=_("Quit"), action=Quit(confirm=True), icon_text="⇱")

        frame:
            xpos 560
            ypos 210
            xsize 1290
            ysize 760
            background (Frame(mm_theme_asset("content_panel_frame.png"), 40, 40) if mm_loadable(mm_theme_asset("content_panel_frame.png")) else Solid(LIB_PANEL_SOFT))

            fixed:
                xpos 42
                ypos 36
                xsize 1206
                ysize 676

                transclude

        vbox:
            xpos 72
            ypos 805
            spacing 4

            text _("“Some memories are like the wind,"):
                color "#D8C9AD"
                size 24
                italic True
                outlines [(1, "#00000088", 0, 1)]

            text _("passing by quietly, yet never truly forgotten.”"):
                color "#D8C9AD"
                size 24
                italic True
                outlines [(1, "#00000088", 0, 1)]

        textbutton back_label:
            xpos 72
            ypos 972
            action back_action
            text_style "library_back_button_text"

    use main_menu_asset_debug


screen library():

    tag menu

    use library_menu_shell(
        page_title=_("Library"),
        page_subtitle=_("Explore special contents of Like Wind, Like Cloud")
    ):

        vbox:
            spacing 22

            text _("Browse unlocked side materials, memories, and replayable moments."):
                style "library_placeholder_body"

            grid 3 2:
                spacing 28

                for category in LIBRARY_CATEGORIES:
                    use library_category_card(category)


screen library_category_card(category):

    $ unlocked = library_category_is_unlocked(category["id"])
    $ progress_text = library_get_progress_text(category["id"])
    $ action = ShowMenu(category["screen"]) if unlocked else NullAction()
    $ idle_background = ui_frame_or_solid("gui/library/card_idle.png", LIB_PANEL, 24)
    $ hover_background = ui_frame_or_solid("gui/library/card_hover.png", LIB_PANEL_HOVER, 24)

    button:
        xsize 382
        ysize 292
        action action
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
                color (LIB_GOLD if unlocked else LIB_DISABLED)

            text _(category["title"]):
                style "library_card_title"
                color (LIB_TEXT if unlocked else LIB_DISABLED)

            text _(category["subtitle"]):
                style "library_card_subtitle"
                color (LIB_MUTED if unlocked else LIB_DISABLED)

            null height 12

            hbox:
                xfill True
                yalign 1.0

                text progress_text:
                    style "library_card_progress"
                    color (LIB_GOLD if unlocked else LIB_DISABLED)

                null xfill True

                text ("›" if unlocked else _("Locked")):
                    style "library_card_arrow"
                    color (LIB_GOLD if unlocked else LIB_DISABLED)
