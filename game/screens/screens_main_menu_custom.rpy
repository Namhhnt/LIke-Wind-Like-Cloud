################################################################################
## Custom PC-first Main/Game Menus
################################################################################

default _mm_quote_text = _("“Some memories are like the wind,\npassing by quietly, yet never truly forgotten.”")


screen main_menu():

    tag menu

    use main_menu_pc


screen main_menu_pc():

    tag menu

    add (mm_theme_asset("background_full.png") if mm_loadable(mm_theme_asset("background_full.png")) else Solid("#15120f")) fit "cover"
    add Solid("#100b0633")

    use main_menu_logo
    use main_menu_navigation
    use main_menu_top_controls
    use main_menu_bottom_text


screen main_menu_touch():

    tag menu

    use main_menu_pc


screen main_menu_logo():

    fixed:
        xpos 96
        ypos (24 if ui_is_compact() else 68)
        xsize 600
        ysize 320

        if _preferences.language == "vietnamese":
            add "gui/theme/refined/title_vi.png":
                xysize (580, 290)
                fit "contain"
        elif mm_loadable(mm_theme_asset("title_pc.png")):
            add mm_theme_asset("title_pc.png")
        else:
            vbox:
                spacing 4

                text _("Like wind,"):
                    font "fonts/NotoSerif-Italic.ttf"
                    size 88
                    color "#fff0d6"
                    italic True
                    outlines [(2, "#00000088", 0, 2)]

                text _("like cloud"):
                    font "fonts/NotoSerif-Italic.ttf"
                    size 88
                    color "#fff0d6"
                    italic True
                    outlines [(2, "#00000088", 0, 2)]



screen main_menu_navigation():
    $ menu_columns = 2 if ui_is_compact() else 1
    $ menu_rows = 3 if ui_is_compact() else 6

    frame:
        xpos 96
        ypos (350 if ui_is_compact() else 382)
        xsize (1728 if ui_is_compact() else 560)
        ysize (540 if ui_is_compact() else 500)
        background ui_panel("#322920f2", "#8f7755", radius=24)

        grid menu_columns menu_rows:
            xpos 30
            ypos 26
            xspacing (40 if ui_is_compact() else 0)
            yspacing (24 if ui_is_compact() else 12)

            use main_menu_nav_button(
                label=_("Continue"),
                action=(FileLoad(progression_autosave_slot, confirm=False, slot=True) if has_progression_autosave() else ShowMenu("load")),
                primary=True,
                icon_text="◷"
            )

            use main_menu_nav_button(
                label=_("Start"),
                action=Show("main_menu_start_prompt"),
                icon_text="❧"
            )

            use main_menu_nav_button(
                label=_("Story Chapters"),
                action=Start("route_map_timeline"),
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

screen main_menu_nav_button(label, action, primary=False, icon_text="•", sensitive=True):

    $ idle_bg = mm_theme_asset("menu_button_active_frame.png") if primary and mm_loadable(mm_theme_asset("menu_button_active_frame.png")) else (mm_theme_asset("menu_button_frame.png") if mm_loadable(mm_theme_asset("menu_button_frame.png")) else Solid("#00000000"))
    $ hover_bg = mm_theme_asset("menu_button_hover_frame.png") if mm_loadable(mm_theme_asset("menu_button_hover_frame.png")) else Solid("#ffffff16")

    button:
        xsize (800 if ui_is_compact() else 500)
        ysize (140 if ui_is_compact() else 62)
        background (ui_panel("#96734599", "#f3d39ddd", radius=31) if primary else None)
        hover_background ui_panel("#96734599", "#f3d39ddd", radius=31)
        insensitive_background idle_bg
        sensitive sensitive
        action action

        fixed:
            xfill True
            yfill True

            add Transform(ui_icon({"◷": "continue", "❧": "start", "▦": "stories", "▧": "cg", "⚙": "settings", "⇱": "quit"}.get(icon_text, "start"), muted=not sensitive, medallion=False), xysize=((64,64) if ui_is_compact() else (46,46))):
                xpos 8
                yalign 0.5

            text label:
                font gui.interface_text_font
                xpos (96 if ui_is_compact() else 68)
                xanchor 0.0
                xsize (650 if ui_is_compact() else 370)
                text_align 0.0
                size (46 if ui_is_compact() else 29)
                color ("#efe4d4" if sensitive else "#9c9185")
                hover_color ("#fff4dd" if sensitive else "#9c9185")
                yalign 0.5

            if primary:
                text "›":
                    size 40
                    color ("#fff2d0" if sensitive else "#9c9185")
                    xpos (748 if ui_is_compact() else 460)
                    yalign 0.5


screen main_menu_start_prompt():

    modal True
    zorder 200

    $ panel_bg = Frame(mm_theme_asset("menu_panel_frame.png"), 36, 36) if mm_loadable(mm_theme_asset("menu_panel_frame.png")) else Solid("#2d261fe8")
    $ continue_enabled = has_progression_autosave()

    key "game_menu" action Hide("main_menu_start_prompt")
    key "K_ESCAPE" action Hide("main_menu_start_prompt")

    add Solid("#00000088")

    fixed:
        xysize (1920, 1080)

        button:
            background None
            hover_background None
            action Hide("main_menu_start_prompt")
            xfill True
            yfill True

        frame:
            xpos (200 if ui_is_compact() else 650)
            ypos (70 if ui_is_compact() else 230)
            xsize (1520 if ui_is_compact() else 620)
            ysize (940 if ui_is_compact() else 620)
            padding (42, 36)
            background ui_panel("#2d261ff5")

            viewport:
                mousewheel True
                draggable True
                scrollbars "vertical"
                vbox:
                    xsize (1400 if ui_is_compact() else 520)
                    spacing 16

                    text _("Choose how you want to begin."):
                        size (48 if ui_is_compact() else 34)
                        font gui.interface_text_font
                        color "#f4e4c5"

                    text _("Load the progression autosave created the last time you reached the map."):
                        size (40 if ui_is_compact() else 24)
                        color ("#d9c7ae" if continue_enabled else "#99897a")

                    use main_menu_nav_button(
                        label=_("Continue"),
                        action=[Hide("main_menu_start_prompt"), FileLoad(progression_autosave_slot, confirm=False, slot=True)],
                        primary=continue_enabled,
                        icon_text="◷",
                        sensitive=continue_enabled
                    )

                    if not continue_enabled:
                        text _("No map autosave has been created yet."):
                            size (36 if ui_is_compact() else 22)
                            color "#b8aa99"

                    null height 8

                    text _("Start over from the beginning and replace the current progression autosave."):
                        size (40 if ui_is_compact() else 24)
                        color "#d9c7ae"

                    use main_menu_nav_button(
                        label=_("New Game"),
                        action=[Function(clear_progression_autosave), Hide("main_menu_start_prompt"), Start("new_game_overwrite")],
                        icon_text="↺"
                    )

                    textbutton _("Back"):
                        style "ui_menu_option"
                        text_style "ui_menu_option_text"
                        yminimum (104 if ui_is_compact() else 62)
                        text_size (44 if ui_is_compact() else 28)
                        action Hide("main_menu_start_prompt")


screen main_menu_top_controls():

    fixed:
        xpos (1566 if ui_is_compact() else 1430)
        ypos 34
        xsize (264 if ui_is_compact() else 400)
        ysize (110 if ui_is_compact() else 78)

        if not ui_is_compact() and mm_loadable(mm_theme_asset("bgm_locale.png")):
            add mm_theme_asset("bgm_locale.png")
        else:
            frame:
                xsize (264 if ui_is_compact() else 400)
                ysize (110 if ui_is_compact() else 60)
                background ui_panel("#322920f2", "#8f7755", radius=24)

        hbox:
            xpos (12 if ui_is_compact() else 24)
            ypos (8 if ui_is_compact() else 16)
            spacing (16 if ui_is_compact() else 18)

            textbutton ("♪" if ui_is_compact() else _("♪  BG.Music")):
                alt _("♪  BG.Music")
                tooltip _("♪  BG.Music")
                xminimum (104 if ui_is_compact() else 0)
                text_font "DejaVuSans.ttf"
                text_size (38 if ui_is_compact() else 23)
                yminimum (96 if ui_is_compact() else 36)
                text_color "#efe4d4"
                text_hover_color "#ffffff"
                action Preference("music mute", "toggle")

            if not ui_is_compact():
                text "|":
                    size 24
                    color "#efe4d477"
                    yalign 0.5

            textbutton ("◎" if ui_is_compact() else _("◎  Language")):
                alt _("◎  Language")
                tooltip _("◎  Language")
                xminimum (104 if ui_is_compact() else 0)
                text_font "DejaVuSans.ttf"
                text_size (38 if ui_is_compact() else 23)
                yminimum (96 if ui_is_compact() else 36)
                text_color "#efe4d4"
                text_hover_color "#ffffff"
                action ShowMenu("language_menu")


screen language_menu():

    tag menu

    use game_menu(_("Language")):
        vbox:
            spacing 24
            use ui_preference_option(_("Vietnamese"), Language("vietnamese"), width=800 if ui_is_compact() else 560)
            use ui_preference_option("English", Language("english"), width=800 if ui_is_compact() else 560, selected_override=(_preferences.language in (None, "english")))
            use ui_preference_option(_("Japanese"), Language("japanese"), width=800 if ui_is_compact() else 560)


screen main_menu_bottom_text():


    text "v[config.version]":
        xpos 1760
        ypos 952
        size (32 if ui_is_compact() else 22)
        color "#e9dcc7cc"

    text _("LIKE WIND, LIKE CLOUD   © 2024  |  All rights reserved."):
        xpos 1848
        xanchor 1.0
        xmaximum 1100
        text_align 1.0
        ypos 1012
        size (30 if ui_is_compact() else 18)
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

    use game_menu_pc(title, scroll, yinitial, spacing):
        transclude


screen game_menu_pc(title, scroll=None, yinitial=0.0, spacing=0):

    tag menu
    style_prefix "game_menu"
    default compact_navigation = False
    $ compact = ui_is_compact()
    $ content_width = 1728 if compact else 1238
    $ content_height = 772 if compact else 668

    add Transform("gui/theme/refined/rainy_library_v2.png", blur=4) fit "cover"
    add Solid("#100b0677")

    text title:
        pos ((440, 58) if compact else (72, 58))
        style "library_title_text"
        size (56 if compact else 58)
        xmaximum (1000 if compact else 1200)

    if compact:
        button:
            id "menu_return"
            style "ui_menu_option"
            alt _("Return")
            tooltip _("Return")
            pos (72, 40)
            xysize (160, 104)
            action Return()
            add ui_icon("back", medallion=False) xysize (64, 64) align (0.5, 0.5)
        button:
            id "menu_navigation_toggle"
            style "ui_menu_option"
            alt _("Navigation")
            tooltip _("Navigation")
            pos (1656, 40)
            xysize (192, 104)
            action ToggleLocalVariable("compact_navigation")
            add ui_icon("menu", medallion=False) xysize (64, 64) align (0.5, 0.5)
    else:
        use main_menu_top_controls

        frame:
            xpos 72
            ypos 210
            xsize 420
            ysize 740
            padding (0, 0)
            background ui_panel("#322920f2", "#8f7755", radius=24)

            use game_menu_navigation_contents

    frame:
        xpos (72 if compact else 510)
        ypos (188 if compact else 210)
        xsize (1776 if compact else 1322)
        ysize (820 if compact else 740)
        padding (0, 0)
        background ui_panel("#322920f2", "#8f7755", radius=24)

        vbox:
            xpos (24 if compact else 42)
            ypos (24 if compact else 36)

            if scroll == "viewport":

                viewport:
                    id "menu_content_scroll"
                    style "viewport"
                    xsize content_width
                    ysize content_height
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    vbox:
                        xsize (content_width - 32)
                        spacing spacing

                        transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    xsize content_width
                    ysize content_height
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
                    xsize content_width
                    ysize content_height

                    transclude

    if compact and compact_navigation:
        button:
            xysize (1920, 1080)
            background Solid("#100b06aa")
            action SetLocalVariable("compact_navigation", False)
        frame:
            pos (920, 172)
            xysize (928, 860)
            padding (24, 24)
            background ui_panel("#322920ff", "#d6b477", radius=24)
            viewport:
                mousewheel True
                draggable True
                scrollbars "vertical"
                use game_menu_navigation_contents

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


screen game_menu_touch(title, scroll=None, yinitial=0.0, spacing=0):
    use game_menu_pc(title, scroll, yinitial, spacing):
        transclude


screen game_menu_navigation_contents():

    vbox:
        xpos 28
        ypos 34
        spacing 8

        if _in_replay:
            use game_menu_nav_button(_("End Replay"), EndReplay(confirm=True))
        else:
            use game_menu_nav_button(_("History"), ShowMenu("history"), icon="continue")

            if not main_menu:
                use game_menu_nav_button(_("Save"), ShowMenu("save"), icon="stories")

        use game_menu_nav_button(_("Load"), ShowMenu("load"), icon="continue")
        use game_menu_nav_button(_("Library"), ShowMenu("library"), icon="cg")
        use game_menu_nav_button(_("Preferences"), ShowMenu("preferences"), icon="settings")
        if not main_menu:
            use game_menu_nav_button(_("Main Menu"), MainMenu(), icon="home")

        use game_menu_nav_button(_("About"), ShowMenu("about"))

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            use game_menu_nav_button(_("Help"), ShowMenu("help"), icon="stories")

        if renpy.variant("pc"):
            use game_menu_nav_button(_("Quit"), Quit(confirm=not main_menu), icon="quit")

        null height 18

        use game_menu_nav_button(_("Return"), Return(), primary=True, icon="back")


screen game_menu_nav_button(label, action, primary=False, icon="extras"):

    button:
        xsize (800 if ui_is_compact() else 364)
        ysize (104 if ui_is_compact() else 58)
        padding (22, 8)
        background (ui_panel("#96734555", "#c3a67677", radius=28) if primary else None)
        hover_background ui_panel("#96734577", radius=28)
        selected_background ui_panel("#96734599", "#e4bf7abb", radius=28)
        action action

        hbox:
            spacing 18
            yalign 0.5
            add Transform(ui_icon(icon, medallion=False), xysize=((56, 56) if ui_is_compact() else (36, 36)))
            text label:
                yalign 0.5
                size (44 if ui_is_compact() else 26)
                font gui.interface_text_font
                color LIB_TEXT
                hover_color LIB_GOLD
                selected_color LIB_GOLD
