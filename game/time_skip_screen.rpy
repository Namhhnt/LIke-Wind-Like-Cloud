screen time_skip_screen():
    tag menu
    modal True

    $ s = ensure_activity_state()
    $ can_choose_any_day = time_skip_can_choose_any_day()
    $ day_choices = time_skip_target_day_choices()
    default selected_day = day_choices[-1] if day_choices else s.get("period_day", 1)

    frame:
        xalign 0.5
        yalign 0.5
        xsize 760
        ysize 520
        background ui_frame_or_solid("gui/library/panel.png", "#15100cf2", 28)
        padding (28, 24)

        vbox:
            spacing 18
            xfill True

            text _("Time Skip"):
                style "interactive_map_panel_title"

            text _("Automate routine days until tomorrow or the next story deadline."):
                style "interactive_map_panel_body"

            text time_get_header_line():
                style "interactive_map_panel_body"

            text time_get_secondary_header_line():
                style "interactive_map_panel_body"

            hbox:
                spacing 14

                textbutton _("Skip 1 Day"):
                    style "interactive_map_secondary_button"
                    text_style "interactive_map_secondary_button_text"
                    action Return({"mode": "next_day"})

                textbutton _("Skip to Next Event"):
                    style "interactive_map_secondary_button"
                    text_style "interactive_map_secondary_button_text"
                    action Return({"mode": "to_next_event"})

            if can_choose_any_day and len(day_choices) > 1:
                vbox:
                    spacing 10

                    text _("Choose a target period day"):
                        style "interactive_map_panel_body"

                    bar value ScreenVariableValue("selected_day", max(1, day_choices[-1]), step=1):
                        xmaximum 620

                    text ("Day %d" % selected_day):
                        style "interactive_map_panel_body"

                    textbutton _("Skip to Selected Day"):
                        style "interactive_map_secondary_button"
                        text_style "interactive_map_secondary_button_text"
                        action Return({"mode": "to_target_day", "target_day": selected_day})

            null:
                yfill True

            textbutton _("Back"):
                style "interactive_map_secondary_button"
                text_style "interactive_map_secondary_button_text"
                action Return(None)
