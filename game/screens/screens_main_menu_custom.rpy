################################################################################
## Custom PC-first Main/Game Menus
################################################################################

default _mm_quote_text = _("“Some memories are like the wind,\npassing by quietly, yet never truly forgotten.”")


screen main_menu():

    tag menu

    if renpy.variant("touch"):
        use main_menu_touch
    else:
        use main_menu_pc


screen main_menu_pc():

    tag menu

    add (mm_theme_asset("background_full.png") if mm_loadable(mm_theme_asset("background_full.png")) else Solid("#15120f")) fit "cover"

    use main_menu_logo
    use main_menu_navigation
    use main_menu_top_controls
    use main_menu_bottom_text
    use main_menu_asset_debug


screen main_menu_touch():

    tag menu

    add gui.main_menu_background

    frame:
        style "main_menu_frame"

    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


screen main_menu_logo():

    fixed:
        xpos 96
        ypos 68
        xsize 760
        ysize 320

        if mm_loadable(mm_theme_asset("title_pc.png")):
            add mm_theme_asset("title_pc.png")
        else:
            vbox:
                spacing 4

                text _("Like wind,"):
                    size 88
                    color "#fff0d6"
                    italic True
                    outlines [(2, "#00000088", 0, 2)]

                text _("like cloud"):
                    size 88
                    color "#fff0d6"
                    italic True
                    outlines [(2, "#00000088", 0, 2)]

        text _("Yuuka Story  •  Minh Story  •  Tam Story"):
            xpos 50
            ypos 238
            size 25
            color "#efe1cb"
            outlines [(1, "#00000088", 0, 1)]


screen main_menu_navigation():

    frame:
        xpos 96
        ypos 410
        xsize 560
        ysize 430
        background (Frame(mm_theme_asset("menu_panel_frame.png"), 36, 36) if mm_loadable(mm_theme_asset("menu_panel_frame.png")) else Solid("#2d261fc4"))

        vbox:
            xpos 30
            ypos 26
            spacing 4

            use main_menu_nav_button(
                label=_("Start"),
                action=Start(),
                primary=True,
                icon_text="❧"
            )

            use main_menu_nav_button(
                label=_("Continue"),
                action=ShowMenu("load"),
                icon_text="◷"
            )

            use main_menu_nav_button(
                label=_("Story Chapters"),
                action=Start("route_map"),
                icon_text="▦"
            )

            use main_menu_nav_button(
                label=_("Library"),
                action=ShowMenu("library"),
                icon_text="▧"
            )

            use main_menu_nav_button(
                label=_("Settings"),
                action=ShowMenu("preferences"),
                icon_text="⚙"
            )

            use main_menu_nav_button(
                label=_("Quit"),
                action=Quit(confirm=True),
                icon_text="⇱"
            )


screen main_menu_nav_button(label, action, primary=False, icon_text="•"):

    $ idle_bg = mm_theme_asset("menu_button_active_frame.png") if primary and mm_loadable(mm_theme_asset("menu_button_active_frame.png")) else (mm_theme_asset("menu_button_frame.png") if mm_loadable(mm_theme_asset("menu_button_frame.png")) else Solid("#00000000"))
    $ hover_bg = mm_theme_asset("menu_button_hover_frame.png") if mm_loadable(mm_theme_asset("menu_button_hover_frame.png")) else Solid("#ffffff16")

    button:
        xsize 500
        ysize 62
        background idle_bg
        hover_background hover_bg
        action action

        hbox:
            xfill True
            yalign 0.5
            spacing 18

            text icon_text:
                min_width 34
                size 27
                color "#efe4d4"
                yalign 0.5

            text label:
                size 29
                color "#efe4d4"
                hover_color "#fff4dd"
                yalign 0.5

            if primary:
                null xfill True

                text "›":
                    size 40
                    color "#fff2d0"
                    xalign 1.0
                    yalign 0.5


screen main_menu_top_controls():

    fixed:
        xpos 1430
        ypos 34
        xsize 400
        ysize 78

        if mm_loadable(mm_theme_asset("bgm_locale.png")):
            add mm_theme_asset("bgm_locale.png")
        else:
            frame:
                xsize 400
                ysize 60
                background (Frame(mm_theme_asset("menu_panel_frame.png"), 28, 28) if mm_loadable(mm_theme_asset("menu_panel_frame.png")) else Solid("#2d261fb0"))

        hbox:
            xpos 24
            ypos 16
            spacing 18

            textbutton _("♪  BG.Music"):
                text_size 23
                text_color "#efe4d4"
                text_hover_color "#ffffff"
                action Preference("music mute", "toggle")

            text "|":
                size 24
                color "#efe4d477"
                yalign 0.5

            textbutton _("◎  Language"):
                text_size 23
                text_color "#efe4d4"
                text_hover_color "#ffffff"
                action ShowMenu("language_menu")


screen language_menu():

    tag menu

    add (mm_theme_asset("background_full.png") if mm_loadable(mm_theme_asset("background_full.png")) else Solid("#15120f")) fit "cover"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 560
        ysize 340
        background (Frame(mm_theme_asset("menu_panel_frame.png"), 36, 36) if mm_loadable(mm_theme_asset("menu_panel_frame.png")) else Solid("#2d261fd8"))

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20

            text _("Language"):
                size 36
                color "#fff1dc"
                xalign 0.5

            textbutton _("Vietnamese"):
                xalign 0.5
                action Language("vietnamese")

            textbutton "English":
                xalign 0.5
                action Language(None)

            textbutton _("Return"):
                xalign 0.5
                action Return()


screen main_menu_bottom_text():

    text _mm_quote_text:
        xpos 96
        ypos 914
        size 24
        color "#e9dcc7cc"
        italic True
        line_spacing 10
        outlines [(1, "#00000088", 0, 1)]

    text _("Press to begin"):
        xalign 0.63
        ypos 744
        size 31
        color "#f2e1c8"
        italic True
        outlines [(1, "#00000088", 0, 1)]

    text "v[config.version]":
        xpos 1760
        ypos 952
        size 22
        color "#e9dcc7cc"

    text _("LIKE WIND, LIKE CLOUD   © 2024  |  All rights reserved."):
        xpos 1390
        ypos 1012
        size 18
        color "#e9dcc7aa"


screen main_menu_asset_debug():

    if config.developer:
        $ missing = mm_missing_assets([
            mm_theme_asset("background_full.png"),
            mm_theme_asset("title_pc.png"),
            mm_theme_asset("menu_panel_frame.png"),
            mm_theme_asset("menu_button_frame.png"),
            mm_theme_asset("menu_button_hover_frame.png"),
            mm_theme_asset("menu_button_active_frame.png"),
            mm_theme_asset("bgm_locale.png"),
            mm_theme_asset("content_panel_frame.png"),
        ])

        if missing:
            frame:
                xpos 20
                ypos 20
                background Solid("#000000aa")

                vbox:
                    spacing 4

                    text _("Missing Main Menu Assets:"):
                        size 18
                        color "#ffcc66"

                    for item in missing:
                        text item:
                            size 14
                            color "#ffffffcc"


screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    tag menu

    if renpy.variant("touch"):
        use game_menu_touch(title, scroll, yinitial, spacing):
            transclude
    else:
        use game_menu_pc(title, scroll, yinitial, spacing):
            transclude


screen game_menu_pc(title, scroll=None, yinitial=0.0, spacing=0):

    tag menu
    style_prefix "game_menu"

    add (gui.main_menu_background if main_menu else gui.game_menu_background)

    frame:
        xpos 72
        ypos 92
        xsize 500
        ysize 890
        background (Frame(mm_theme_asset("menu_panel_frame.png"), 36, 36) if mm_loadable(mm_theme_asset("menu_panel_frame.png")) else Solid("#2d261fc0"))

        use game_menu_navigation_contents

    frame:
        xpos 590
        ypos 92
        xsize 1258
        ysize 890
        background (Frame(mm_theme_asset("content_panel_frame.png"), 40, 40) if mm_loadable(mm_theme_asset("content_panel_frame.png")) else Solid("#201a16dd"))

        vbox:
            xpos 46
            ypos 34
            spacing 26

            text title:
                size 42
                color "#fff0d6"
                outlines [(1, "#00000088", 0, 1)]

            if scroll == "viewport":

                viewport:
                    xsize 1164
                    ysize 748
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    vbox:
                        spacing spacing

                        transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    xsize 1164
                    ysize 748
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True
                    spacing spacing

                    transclude

            else:

                fixed:
                    xsize 1164
                    ysize 748

                    transclude

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


screen game_menu_touch(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True
                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"
        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


screen game_menu_navigation_contents():

    vbox:
        xpos 28
        ypos 34
        spacing 10

        if _in_replay:
            use game_menu_nav_button(_("End Replay"), EndReplay(confirm=True))
        else:
            use game_menu_nav_button(_("History"), ShowMenu("history"))

            if not main_menu:
                use game_menu_nav_button(_("Save"), ShowMenu("save"))

        use game_menu_nav_button(_("Load"), ShowMenu("load"))
        use game_menu_nav_button(_("Preferences"), ShowMenu("preferences"))

        if not main_menu:
            use game_menu_nav_button(_("Main Menu"), MainMenu())

        use game_menu_nav_button(_("About"), ShowMenu("about"))

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            use game_menu_nav_button(_("Help"), ShowMenu("help"))

        if renpy.variant("pc"):
            use game_menu_nav_button(_("Quit"), Quit(confirm=not main_menu))

        null height 18

        use game_menu_nav_button(_("Return"), Return(), primary=True)


screen game_menu_nav_button(label, action, primary=False):

    $ idle_bg = mm_theme_asset("menu_button_active_frame.png") if primary and mm_loadable(mm_theme_asset("menu_button_active_frame.png")) else (mm_theme_asset("menu_button_frame.png") if mm_loadable(mm_theme_asset("menu_button_frame.png")) else Solid("#00000000"))
    $ hover_bg = mm_theme_asset("menu_button_hover_frame.png") if mm_loadable(mm_theme_asset("menu_button_hover_frame.png")) else Solid("#ffffff16")

    button:
        xsize 440
        ysize 58
        background idle_bg
        hover_background hover_bg
        action action

        text label:
            xalign 0.08
            yalign 0.5
            size 26
            color "#efe4d4"
            hover_color "#fff4dd"
