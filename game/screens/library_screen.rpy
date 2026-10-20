screen library_menu_shell(page_title, page_subtitle, back_action=ShowMenu("main_menu"), back_label=_("Back"), split=False, sidebar_height=740, cinema=False):

    $ compact_layout = ui_is_compact()

    add Transform("gui/theme/refined/rainy_library_v2.png", blur=4) fit "cover"
    add Solid("#100b0644")

    key "game_menu" action back_action
    key "K_ESCAPE" action back_action

    fixed:
        xysize (1920, 1080)

        vbox:
            xpos 72
            ypos 58
            spacing 6

            text page_title:
                style "library_title_text"
                size (64 if compact_layout else 72)
            text page_subtitle:
                style "library_subtitle_text"
                size (40 if compact_layout else 28)

        if split:
            add ui_panel("#3c332bb0", "#c3a676bb", radius=24):
                pos (72, 210)
                xysize (420, sidebar_height)
            add ui_panel("#302923ad", "#c3a676bb", radius=32, ornate=True):
                pos (510, 210)
                xysize (1322, 740)

        frame:
            xpos (296 if cinema else 72)
            ypos (194 if cinema else 210)
            xsize (1328 if cinema else 1760)
            ysize (768 if cinema else 740)
            padding (0, 0)
            background (None if split else ui_panel(LIB_PANEL_SOFT, radius=28))

            fixed:
                xpos (24 if cinema else 42)
                ypos (24 if cinema else 36)
                xsize (1280 if cinema else 1676)
                ysize (720 if cinema else 668)

                transclude

        if compact_layout:
            button:
                xpos 72
                ypos 952
                xysize (112, 112)
                alt back_label
                tooltip back_label
                action back_action
                background ui_panel("#4b3928f2", "#d7af72ee", radius=24)
                hover_background ui_panel("#6b5035f5", "#e1bc83", radius=24)
                text "←":
                    font "DejaVuSans.ttf"
                    size 64
                    color LIB_TEXT
                    align (0.5, 0.5)
        else:
            textbutton back_label:
                xpos 72
                ypos 972
                action back_action
                text_style "library_back_button_text"
                background ui_panel("#6c5034ee", "#d7af72ee")
                padding (24, 12)

    use main_menu_top_controls


screen library():

    tag menu
    $ compact_layout = ui_is_compact()

    use library_menu_shell(
        page_title=_("Library"),
        page_subtitle=_("Explore special contents of Like Wind, Like Cloud"),
        split=not compact_layout,
        sidebar_height=520
    ):

        if compact_layout:
            viewport:
                xysize (1676, 668)
                scrollbars "vertical"
                mousewheel True
                draggable True

                grid 2 3:
                    xalign 0.5
                    xspacing 24
                    yspacing 24
                    for category in LIBRARY_CATEGORIES:
                        use library_category_card(category, compact=True)
        else:
            hbox:
                spacing 68
                vbox:
                    xsize 370
                    spacing 10
                    use library_sidebar_item(_("Start"), "❧", Show("main_menu_start_prompt"))
                    use library_sidebar_item(_("Continue"), "◷", ShowMenu("load"))
                    use library_sidebar_item(_("Story Chapters"), "▦", Start("route_map_timeline"))
                    use library_sidebar_item(_("Library"), "▧", NullAction(), active=True)
                    use library_sidebar_item(_("Settings"), "⚙", ShowMenu("preferences"))
                    use library_sidebar_item(_("Quit"), "⇱", Quit(confirm=True))

                grid 3 2:
                    xspacing 40
                    yspacing 36
                    for category in LIBRARY_CATEGORIES:
                        use library_category_card(category)

            add Transform("gui/theme/refined/botanical_sprig_v2.png", alpha=0.55, rotate=-25):
                pos (-42, 516)
                xysize (88, 88)
            text _mm_quote_text:
                pos (42, 520)
                xmaximum 330
                font "fonts/NotoSerif-Italic.ttf"
                size 20
                color "#e2d2b9"
                line_spacing 5


screen library_category_card(category, compact=False):

    $ unlocked = library_category_is_unlocked(category["id"])
    $ progress_text = library_get_progress_text(category["id"])
    $ empty_category = progress_text.replace(" ", "") == "0/0"
    $ action = ShowMenu(category["screen"]) if unlocked else NullAction()
    $ idle_background = ui_panel("#3c3027ee", "#c3a676dd", radius=22)
    $ hover_background = ui_panel("#5a4531f5", "#e1bc83", radius=22)

    button:
        xsize (812 if compact else 386)
        ysize (280 if compact else 316)
        action action
        sensitive unlocked
        background idle_background
        hover_background hover_background
        insensitive_background idle_background

        if compact:
            fixed:
                xpos 28
                ypos 18
                xsize 756
                ysize 244

                add Transform(ui_icon(category["id"], muted=not unlocked or empty_category), xysize=(92, 92)):
                    pos (0, 8)

                text _(category["title"]):
                    style "library_compact_card_title"
                    color (LIB_TEXT if unlocked and not empty_category else LIB_DISABLED)
                    pos (112, 4)
                    xmaximum 644
                    ymaximum 104

                text _(category["subtitle"]):
                    style "library_compact_card_subtitle"
                    color (LIB_MUTED if unlocked else LIB_DISABLED)
                    pos (112, 88)
                    xmaximum 644
                    ymaximum 100

                text (_("No content yet") if empty_category else progress_text):
                    style "library_compact_card_progress"
                    color (LIB_GOLD if unlocked else LIB_DISABLED)
                    pos (0, 202)
                    xmaximum 650

                text ("›" if unlocked else _("Locked")):
                    style "library_compact_card_arrow"
                    color (LIB_GOLD if unlocked else LIB_DISABLED)
                    pos (710, 192)
        else:
            fixed:
                xpos 30
                ypos 24
                xsize 326
                ysize 268

                add Transform(ui_icon(category["id"], muted=not unlocked or empty_category), xysize=(112, 112)):
                    xalign 0.5

                text _(category["title"]):
                    style "library_card_title"
                    color (LIB_TEXT if unlocked and not empty_category else LIB_DISABLED)
                    xalign 0.5
                    ypos 128
                    xmaximum 326
                    text_align 0.5

                text _(category["subtitle"]):
                    style "library_card_subtitle"
                    color (LIB_MUTED if unlocked else LIB_DISABLED)
                    text_align 0.5
                    xalign 0.5
                    ypos 176
                    xmaximum 326
                    ymaximum 68

                fixed:
                    xysize (326, 40)
                    ypos 246

                    text (_("No content yet") if empty_category else progress_text):
                        style "library_card_progress"
                        color (LIB_GOLD if unlocked else LIB_DISABLED)

                    text ("›" if unlocked else _("Locked")):
                        style "library_card_arrow"
                        color (LIB_GOLD if unlocked else LIB_DISABLED)
                        xalign 1.0

screen library_sidebar_item(label, icon, action, active=False):
    button:
        xsize 360
        ysize 68
        padding (20, 12)
        background (ui_panel("#96734599", "#e4bf7abb", radius=30) if active else None)
        hover_background ui_panel("#96734577", radius=30)
        action action
        hbox:
            spacing 22
            add Transform(ui_icon({"◷": "continue", "❧": "start", "▦": "stories", "▧": "cg", "⚙": "settings", "⇱": "quit"}.get(icon, "extras"), medallion=False), xysize=(46,46))
            text label style "library_back_button_text"
