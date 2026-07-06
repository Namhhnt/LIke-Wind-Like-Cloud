screen interactive_map_daily_hud(context_id="act1_default", title_override=None):
    $ main_today_summary = time_get_main_today_summary()
    $ context = MAP_CONTEXTS.get(context_id, MAP_CONTEXTS["act1_default"])

    frame:
        xpos 58
        ypos 48
        xsize 620
        ysize 206
        background ui_frame_or_solid("gui/library/panel.png", "#201812f0", 26)

        vbox:
            spacing 6
            xfill True

            text (title_override if title_override else _(context.get("title", "City Map"))):
                style "interactive_map_panel_title"

            text _(context.get("subtitle", "Choose where the story goes next.")):
                style "interactive_map_panel_body"

            text time_get_header_line():
                style "interactive_map_title"

            text time_get_secondary_header_line():
                style "interactive_map_subtitle"

            text time_get_points_header_line():
                style "interactive_map_panel_body"

    if main_today_summary:
        frame:
            xpos 58
            ypos 272
            xsize 620
            ysize 92
            background ui_frame_or_solid("gui/library/panel.png", "#100c09d8", 18)

            vbox:
                spacing 6

                text _("Main Today"):
                    style "interactive_map_panel_title"

                text main_today_summary:
                    style "interactive_map_panel_body"
