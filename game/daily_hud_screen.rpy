screen interactive_map_daily_hud(context_id="act1_default", title_override=None, phone_action=None, skip_action=None, timeline_action=None, back_action=None):
    $ main_today_summary = time_get_main_today_summary()
    $ context = MAP_CONTEXTS.get(context_id, MAP_CONTEXTS["act1_default"])

    frame:
        pos (58, 32)
        xysize (1804, 136)
        padding (28, 18)
        background ui_panel("#211a15bb", "#b89a6b88")
        fixed:
            xfill True
            yfill True
            vbox:
                pos (0, 0)
                xsize 310
                text (title_override if title_override else _(context.get("title", "City Map"))) style "interactive_map_panel_title" size 64 font "fonts/NotoSerif-Italic.ttf"
            vbox:
                pos (340, 16)
                xsize 700
                spacing 10
                text time_get_header_line() style "interactive_map_subtitle"
                text (time_get_clock_header_line() + "  ·  " + time_get_points_header_line()) style "interactive_map_panel_body"
            hbox:
                pos (1040, 24)
                spacing 12
                if phone_action:
                    textbutton _("Phone"):
                        style "interactive_map_secondary_button"
                        text_style "interactive_map_secondary_button_text"
                        xsize 140
                        ysize 52
                        text_size 18
                        action phone_action
                if timeline_action:
                    textbutton _("Open Timeline View"):
                        style "interactive_map_secondary_button"
                        text_style "interactive_map_secondary_button_text"
                        xsize 260
                        ysize 52
                        text_size 18
                        action timeline_action
                if back_action:
                    textbutton _("Back"):
                        style "interactive_map_secondary_button"
                        text_style "interactive_map_secondary_button_text"
                        xsize 120
                        ysize 52
                        text_size 18
                        action back_action
                if skip_action:
                    textbutton _("Skip time"):
                        style "interactive_map_secondary_button"
                        text_style "interactive_map_secondary_button_text"
                        xsize 140
                        ysize 52
                        text_size 18
                        action skip_action

