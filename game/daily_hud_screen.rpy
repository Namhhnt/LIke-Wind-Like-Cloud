screen interactive_map_daily_hud(context_id="act1_default", title_override=None, phone_action=None, skip_action=None):
    $ main_today_summary = time_get_main_today_summary()
    $ context = MAP_CONTEXTS.get(context_id, MAP_CONTEXTS["act1_default"])

    frame:
        pos (58, 32)
        xysize (1804, 136)
        padding (28, 18)
        background ui_frame_or_solid("gui/library/panel.png", "#201812ed", 26)
        hbox:
            spacing 32
            vbox:
                xsize 650
                spacing 8
                text (title_override if title_override else _(context.get("title", "City Map"))) style "interactive_map_panel_title"
                text time_get_header_line() style "interactive_map_subtitle"
                text (time_get_clock_header_line() + "  ·  " + time_get_points_header_line()) style "interactive_map_panel_body"
            vbox:
                xsize 660
                spacing 8
                text _("Main Today") style "interactive_map_panel_title"
                text (main_today_summary or time_get_secondary_header_line()) style "interactive_map_panel_body"
            vbox:
                spacing 8
                xsize 330
                if phone_action:
                    textbutton _("Phone"):
                        style "interactive_map_secondary_button"
                        text_style "interactive_map_secondary_button_text"
                        action phone_action
                if skip_action:
                    textbutton _("Skip time"):
                        style "interactive_map_secondary_button"
                        text_style "interactive_map_secondary_button_text"
                        action skip_action

