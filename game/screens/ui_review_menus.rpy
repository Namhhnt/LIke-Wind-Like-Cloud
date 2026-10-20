# Isolated review samples. Live Preferences and Library screens stay unchanged.

style ui_review_menu_text is default:
    font gui.interface_text_font
    color "#f5e8d2"
    size 32

style ui_review_menu_heading is ui_review_menu_text:
    color "#d6b477"
    size 34

style ui_review_menu_option is button:
    padding (22, 10)
    background ui_panel("#241e19ee", "#8f7755", radius=14)
    hover_background ui_panel("#51402efc", "#d6b477", radius=14)
    selected_background ui_panel("#604b31fc", "#d6b477", radius=14)
    insensitive_background ui_panel("#241e19ee", "#655644", radius=14)

style ui_review_menu_option_text is ui_review_menu_text:
    size 30
    hover_color "#fff6e7"
    selected_color "#ffe1a8"
    insensitive_color "#8f806d"

style ui_review_menu_slider is bar:
    ysize 44
    left_bar Fixed(Transform(ui_panel("#d6b477", "#d6b477", radius=6), ysize=12, yalign=0.5))
    right_bar Fixed(Transform(ui_panel("#241e19", "#8f7755", radius=6), ysize=12, yalign=0.5))
    thumb Transform(ui_panel("#f5e8d2", "#8f7755", radius=9), xysize=(32, 44))
    thumb_shadow None
    thumb_offset 0
    thumb_align 0.5

style ui_review_menu_touch_slider is ui_review_menu_slider:
    ysize 104
    thumb Fixed(Transform(ui_panel("#f5e8d2", "#8f7755", radius=12), xysize=(48, 48), yalign=0.5), xysize=(48, 104))

screen ui_review_preference_option(caption, option_action, width=362, compact=False, check=False):
    button:
        style "ui_review_menu_option"
        xysize (width, 104 if compact else 68)
        action option_action
        hbox:
            yalign 0.5
            spacing 18
            text (("\u25a0" if renpy.is_selected(option_action) else "\u25a1") if check else ("\u25cf" if renpy.is_selected(option_action) else "\u25cb")):
                font "DejaVuSans.ttf"
                size (40 if compact and width < 600 else 44 if compact else 24 if width < 300 else 30)
                color "#d6b477"
            text caption:
                style "ui_review_menu_option_text"
                size (40 if compact and width < 600 else 44 if compact else 24 if width < 300 else 30)
                yalign 0.5

screen ui_review_preference_slider(caption, preference_name, compact=False, width=752):
    vbox:
        spacing (12 if compact else 10)
        xsize width
        text caption:
            style "ui_review_menu_text"
            size (44 if compact else 30)
        bar:
            style ("ui_review_menu_touch_slider" if compact else "ui_review_menu_slider")
            xsize width
            value Preference(preference_name)

screen ui_review_settings(compact=False):
    tag menu
    default review_settings_tab = "display"

    use ui_review_shell(_("Preferences"), compact):
        if compact:
            vbox:
                spacing 24
                hbox:
                    spacing 24
                    for tab_id, tab_caption in (("display", _("Display")), ("text", _("Reading")), ("audio", _("Audio"))):
                        textbutton tab_caption:
                            id ("review_tab_" + tab_id)
                            style "ui_review_menu_option"
                            text_style "ui_review_menu_option_text"
                            text_size 44
                            xysize (560, 104)
                            text_xalign 0.5
                            selected review_settings_tab == tab_id
                            action SetScreenVariable("review_settings_tab", tab_id)
                frame:
                    xysize (1728, 676)
                    padding (40, 32)
                    background ui_panel("#322920f2", "#8f7755", radius=22)
                    if review_settings_tab == "display":
                        vbox:
                            spacing 30
                            text _("Display") style "ui_review_menu_heading" size 48
                            hbox:
                                spacing 24
                                use ui_review_preference_option(_("Window"), Preference("display", "window"), width=800, compact=True)
                                use ui_review_preference_option(_("Fullscreen"), Preference("display", "fullscreen"), width=800, compact=True)
                            null height 20
                            text _("Language") style "ui_review_menu_heading" size 48
                            hbox:
                                spacing 24
                                use ui_review_preference_option("English", Language("english"), width=528, compact=True)
                                use ui_review_preference_option(_("Vietnamese"), Language("vietnamese"), width=528, compact=True)
                                use ui_review_preference_option(_("Japanese"), Language("japanese"), width=528, compact=True)
                    elif review_settings_tab == "text":
                        vbox:
                            spacing 22
                            use ui_review_preference_slider(_("Text Speed"), "text speed", compact=True, width=1648)
                            use ui_review_preference_slider(_("Auto-Forward Time"), "auto-forward time", compact=True, width=1648)
                            text _("Skip") style "ui_review_menu_heading" size 48
                            hbox:
                                spacing 24
                                use ui_review_preference_option(_("Unseen Text"), Preference("skip", "toggle"), width=528, compact=True, check=True)
                                use ui_review_preference_option(_("After Choices"), Preference("after choices", "toggle"), width=528, compact=True, check=True)
                                use ui_review_preference_option(_("Transitions"), InvertSelected(Preference("transitions", "toggle")), width=528, compact=True, check=True)
                    else:
                        hbox:
                            spacing 40
                            vbox:
                                spacing 18
                                if config.has_music:
                                    use ui_review_preference_slider(_("Music Volume"), "music volume", compact=True, width=1040)
                                if config.has_sound:
                                    use ui_review_preference_slider(_("Sound Volume"), "sound volume", compact=True, width=1040)
                                if config.has_voice:
                                    use ui_review_preference_slider(_("Voice Volume"), "voice volume", compact=True, width=1040)
                            use ui_review_preference_option(_("Mute All"), Preference("all mute", "toggle"), width=568, compact=True, check=True)
        else:
            hbox:
                spacing 28
                frame:
                    xysize (850, 790)
                    padding (40, 32)
                    background ui_panel("#322920f2", "#8f7755", radius=22)
                    vbox:
                        spacing 18
                        text _("Display") style "ui_review_menu_heading"
                        hbox:
                            spacing 20
                            use ui_review_preference_option(_("Window"), Preference("display", "window"))
                            use ui_review_preference_option(_("Fullscreen"), Preference("display", "fullscreen"))
                        null height 10
                        text _("Language") style "ui_review_menu_heading"
                        hbox:
                            spacing 16
                            use ui_review_preference_option("English", Language("english"), width=246)
                            use ui_review_preference_option(_("Vietnamese"), Language("vietnamese"), width=246)
                            use ui_review_preference_option(_("Japanese"), Language("japanese"), width=246)
                        null height 10
                        text _("Skip") style "ui_review_menu_heading"
                        use ui_review_preference_option(_("Unseen Text"), Preference("skip", "toggle"), width=770, check=True)
                        use ui_review_preference_option(_("After Choices"), Preference("after choices", "toggle"), width=770, check=True)
                        use ui_review_preference_option(_("Transitions"), InvertSelected(Preference("transitions", "toggle")), width=770, check=True)
                frame:
                    xysize (850, 790)
                    padding (40, 32)
                    background ui_panel("#322920f2", "#8f7755", radius=22)
                    vbox:
                        spacing 22
                        use ui_review_preference_slider(_("Text Speed"), "text speed", width=770)
                        use ui_review_preference_slider(_("Auto-Forward Time"), "auto-forward time", width=770)
                        if config.has_music:
                            use ui_review_preference_slider(_("Music Volume"), "music volume", width=770)
                        if config.has_sound:
                            use ui_review_preference_slider(_("Sound Volume"), "sound volume", width=770)
                        if config.has_voice:
                            use ui_review_preference_slider(_("Voice Volume"), "voice volume", width=770)
                        use ui_review_preference_option(_("Mute All"), Preference("all mute", "toggle"), width=770, check=True)

screen ui_review_library_card(category, compact=False):
    button:
        xysize ((836, 340) if compact else (560, 380))
        padding (0, 0)
        background ui_panel("#322920f2", "#8f7755", radius=22)
        hover_background ui_panel("#51402efc", "#d6b477", radius=22)
        action NullAction()
        fixed:
            if compact:
                add ui_icon(category["id"], medallion=False) xpos 30 ypos 26 xysize (78, 78)
                text _(category["title"]):
                    style "ui_review_menu_heading"
                    pos (132, 36)
                    xsize 672
                    size 44
                text _(category["subtitle"]):
                    style "ui_review_menu_text"
                    pos (32, 126)
                    xsize 772
                    size 40
                    color "#cdbb9e"
                text library_get_progress_text(category["id"]):
                    style "ui_review_menu_text"
                    pos (32, 264)
                    size 40
                text "\u2192" font "DejaVuSans.ttf" color "#d6b477" size 46 pos (738, 254)
            else:
                add ui_icon(category["id"], medallion=False) xpos 32 ypos 28 xysize (96, 96)
                text _(category["title"]):
                    style "ui_review_menu_heading"
                    pos (32, 144)
                    xsize 496
                text _(category["subtitle"]):
                    style "ui_review_menu_text"
                    pos (32, 208)
                    xsize 496
                    size 27
                    color "#cdbb9e"
                text library_get_progress_text(category["id"]):
                    style "ui_review_menu_text"
                    pos (32, 316)
                    size 28
                text "\u2192" font "DejaVuSans.ttf" color "#d6b477" size 36 pos (486, 305)

screen ui_review_library(compact=False):
    tag menu
    use ui_review_shell(_("Library"), compact):
        if compact:
            viewport:
                id "review_library_scroll"
                xysize (1728, 820)
                mousewheel True
                draggable True
                scrollbars "vertical"
                grid 2 3:
                    xspacing 24
                    yspacing 24
                    for category in LIBRARY_CATEGORIES:
                        use ui_review_library_card(category, compact=True)
        else:
            grid 3 2:
                xspacing 24
                yspacing 26
                for category in LIBRARY_CATEGORIES:
                    use ui_review_library_card(category)
