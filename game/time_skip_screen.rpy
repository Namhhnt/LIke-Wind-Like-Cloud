screen time_passage_loading_screen(duration=2.0, title=None, body=None):
    tag menu
    modal True

    on "show" action [SetVariable("quick_menu", False), SetVariable("_map_rollback_saved", config.rollback_enabled), SetVariable("config.rollback_enabled", False)]
    on "hide" action [SetVariable("quick_menu", True), SetVariable("config.rollback_enabled", _map_rollback_saved)]

    default elapsed = 0.0
    $ safe_duration = max(0.25, float(duration or 0.25))
    $ progress_ratio = min(1.0, elapsed / safe_duration)
    timer 0.05 repeat True action If(
        elapsed < safe_duration,
        true=SetScreenVariable("elapsed", min(safe_duration, elapsed + 0.05)),
        false=Return(True),
    )

    fixed:
        xysize (1920, 1080)

        add Solid("#050403cc")

        frame:
            xalign 0.5
            yalign 0.5
            xsize 820
            ysize 280
            background ui_frame_or_solid("gui/library/panel.png", "#15100cf2", 28)
            padding (34, 30)

            vbox:
                spacing 20
                xfill True

                text (title if title else _("Time Passes")):
                    style "interactive_map_panel_title"

                text (body if body else _("Letting the routine play out...")):
                    style "interactive_map_panel_body"

                frame:
                    xfill True
                    ysize 28
                    background Solid("#2a2118")
                    padding (4, 4)

                    fixed:
                        xfill True
                        yfill True

                        add Solid("#7c5940"):
                            xsize int(772 * progress_ratio)
                            ysize 20

                text ("%d%%" % int(progress_ratio * 100)):
                    style "interactive_map_panel_body"
                    xalign 0.5


screen time_skip_screen():
    tag menu
    modal True

    on "show" action [SetVariable("quick_menu", False), SetVariable("_map_rollback_saved", config.rollback_enabled), SetVariable("config.rollback_enabled", False)]
    on "hide" action [SetVariable("quick_menu", True), SetVariable("config.rollback_enabled", _map_rollback_saved)]

    $ s = ensure_activity_state()
    $ can_choose_any_day = time_skip_can_choose_any_day()
    $ day_choices = time_skip_target_day_choices()
    $ routine_actions = time_skip_get_routine_actions()
    default selected_mode = "next_day"
    default selected_day = day_choices[-1] if day_choices else s.get("period_day", 1)
    default selected_plan_ids = time_skip_default_plan_ids()
    default expanded_detail_ids = []
    $ normalized_plan_ids = time_skip_normalize_plan(selected_plan_ids)
    $ estimate = time_skip_build_estimate(selected_mode, selected_day, normalized_plan_ids)
    $ confirm_action = Return({"mode": selected_mode, "target_day": selected_day, "routine_plan": normalized_plan_ids}) if estimate.get("can_skip") else NullAction()

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1180
        ysize 860
        background ui_frame_or_solid("gui/library/panel.png", "#15100cf2", 28)
        padding (28, 24)

        hbox:
            spacing 24
            xfill True

            vbox:
                spacing 16
                xsize 600

                text _("Time Skip"):
                    style "interactive_map_panel_title"

                text _("Build a repeatable routine for the skip period."):
                    style "interactive_map_panel_body"

                hbox:
                    spacing 16

                    text time_get_header_line():
                        style "interactive_map_panel_body"

                    text time_get_secondary_header_line():
                        style "interactive_map_panel_body"
                        color "#d1b89f"

                text _("Skip Target"):
                    style "interactive_map_panel_title"

                hbox:
                    spacing 12
                    xfill True

                    textbutton _("1 Day"):
                        style "interactive_map_secondary_button"
                        text_style "interactive_map_secondary_button_text"
                        xfill False
                        xminimum 165
                        action SetScreenVariable("selected_mode", "next_day")

                    textbutton _("Next Event"):
                        style "interactive_map_secondary_button"
                        text_style "interactive_map_secondary_button_text"
                        xfill False
                        xminimum 165
                        action SetScreenVariable("selected_mode", "to_next_event")

                    if len(day_choices) > 1:
                        textbutton _("Selected Day"):
                            style "interactive_map_secondary_button"
                            text_style "interactive_map_secondary_button_text"
                            xfill False
                            xminimum 180
                            sensitive can_choose_any_day
                            action (SetScreenVariable("selected_mode", "to_target_day") if can_choose_any_day else NullAction())

                if len(day_choices) > 1 and not can_choose_any_day:
                    text _("Selected Day is unavailable in this story period. You can only skip one day at a time or continue until the next event."):
                        style "interactive_map_panel_body"
                        color "#b9a692"

                if can_choose_any_day and len(day_choices) > 1:
                    vbox:
                        spacing 8

                        text _("Choose a target period day"):
                            style "interactive_map_panel_body"

                        bar value ScreenVariableValue("selected_day", max(1, day_choices[-1]), step=1):
                            xmaximum 560

                        text ("Day %d" % selected_day):
                            style "interactive_map_panel_body"

                hbox:
                    spacing 12
                    xfill True

                    text _("Routine Tasks"):
                        style "interactive_map_panel_title"

                    null:
                        xfill True

                    text ("(Per day: %d / 24 hours)" % time_skip_total_time_cost(normalized_plan_ids)):
                        style "interactive_map_panel_body"
                        color "#d1b89f"
                        yalign 0.5

                if routine_actions:
                    frame:
                        xfill True
                        ysize 350
                        background Solid("#120d0acc")
                        padding (10, 10)

                        viewport:
                            xfill True
                            yfill True
                            draggable True
                            mousewheel True
                            scrollbars "vertical"
                            clipping True

                            vbox:
                                spacing 10
                                xfill True

                                for action in routine_actions:
                                    $ is_selected = action.get("id") in normalized_plan_ids
                                    $ is_expanded = action.get("id") in expanded_detail_ids
                                    $ tag_bits = []
                                    if action.get("weekday_only"):
                                        $ tag_bits.append("Weekday")
                                    if action.get("weekend_only"):
                                        $ tag_bits.append("Weekend")
                                    if action.get("ends_day"):
                                        $ tag_bits.append("Ends Day")
                                    if action.get("marks_work_completed"):
                                        $ tag_bits.append("Counts as Work")
                                    $ tag_line = " | ".join(tag_bits)

                                    frame:
                                        background Solid("#3a2a1fdd" if is_selected else "#241b15dd")
                                        padding (16, 14)
                                        xfill True

                                        vbox:
                                            spacing 6
                                            xfill True

                                            hbox:
                                                spacing 8
                                                xfill True

                                                button:
                                                    background None
                                                    hover_background Solid("#4b382a88")
                                                    xmaximum 452
                                                    xfill True
                                                    yminimum 42
                                                    action SetScreenVariable("selected_plan_ids", time_skip_toggle_plan_ids(normalized_plan_ids, action.get("id")))

                                                    hbox:
                                                        spacing 12
                                                        xfill True

                                                        text action.get("title", action.get("id", "Action")):
                                                            style "interactive_map_panel_body"
                                                            color "#f5e7d7"
                                                            yalign 0.5

                                                        null:
                                                            xfill True

                                                        text ("%sh" % action.get("time_cost", 0)):
                                                            style "interactive_map_panel_body"
                                                            color "#cda885"
                                                            yalign 1.0

                                                textbutton (_("^") if is_expanded else _("v")):
                                                    style "time_skip_compact_button"
                                                    text_style "time_skip_compact_button_text"
                                                    xfill False
                                                    xsize 42
                                                    ysize 42
                                                    action SetScreenVariable(
                                                        "expanded_detail_ids",
                                                        [detail_id for detail_id in expanded_detail_ids if detail_id != action.get("id")]
                                                        if action.get("id") in expanded_detail_ids
                                                        else expanded_detail_ids + [action.get("id")]
                                                    )

                                            if is_expanded:
                                                vbox:
                                                    spacing 4
                                                    xfill True

                                                    text action.get("summary", ""):
                                                        style "interactive_map_panel_body"
                                                        color "#d1b89f"

                                                    text ("Category: %s" % action.get("category", "Action")):
                                                        style "interactive_map_panel_body"
                                                        color "#cda885"

                                                    if tag_line:
                                                        text tag_line:
                                                            style "interactive_map_panel_body"
                                                            color "#c68f73"
                else:
                    text _("No automated routine actions are available in this period yet."):
                        style "interactive_map_panel_body"


            frame:
                xsize 500
                yfill True
                background Solid("#120d0acc")
                padding (22, 20)

                vbox:
                    spacing 14
                    xfill True

                    text _("Projected Outcome"):
                        style "interactive_map_panel_title"

                    text ("Selected tasks: %d | Estimated skip: %d day(s)" % (time_skip_selected_action_count(normalized_plan_ids), estimate.get("days_skipped", 0))):
                        style "interactive_map_panel_body"

                    text ("Progress bar time: %.1f seconds" % estimate.get("loading_seconds", 0.0)):
                        style "interactive_map_panel_body"

                    if estimate.get("reason"):
                        text estimate.get("reason"):
                            style "interactive_map_panel_body"
                            color "#e59a80"

                    if estimate.get("negative_rows"):
                        text _("Blocked statuses"):
                            style "interactive_map_panel_title"

                        for row in estimate.get("negative_rows", []):
                            text ("%s: %s" % (row.get("label", row.get("key", "Stat")), row.get("final", 0))):
                                style "interactive_map_panel_body"
                                color "#f09b82"

                    text _("Stats"):
                        style "interactive_map_panel_title"

                    if estimate.get("activity_rows"):
                        for row in estimate.get("activity_rows", []):
                            $ row_color = "#f09b82" if row.get("delta", 0) < 0 else "#cfe6b8"
                            text ("%s  %s -> %s" % (row.get("label", row.get("key", "Stat")), time_skip_format_delta(row.get("delta", 0)), row.get("final", 0))):
                                style "interactive_map_panel_body"
                                color row_color
                    else:
                        text _("No tracked stat changes."):
                            style "interactive_map_panel_body"

                    text _("Character Scores"):
                        style "interactive_map_panel_title"

                    if estimate.get("story_rows"):
                        viewport:
                            draggable True
                            mousewheel True
                            xsize 496
                            ysize 280

                            vbox:
                                spacing 8
                                xfill False

                                for row in estimate.get("story_rows", []):
                                    $ row_color = "#f09b82" if row.get("delta", 0) < 0 else "#cfe6b8"
                                    text ("%s  %s -> %s" % (row.get("label", row.get("key", "Score")), time_skip_format_delta(row.get("delta", 0)), row.get("final", 0))):
                                        style "interactive_map_panel_body"
                                        color row_color
                    else:
                        text _("No tracked character score changes."):
                            style "interactive_map_panel_body"

                    null:
                        yfill True

                    hbox:
                        spacing 2
                        xfill True

                        null:
                            xfill True

                        textbutton _("Back"):
                            style "interactive_map_secondary_button"
                            text_style "interactive_map_secondary_button_text"
                            xfill False
                            xsize 220
                            ysize 54
                            action Return(None)

                        textbutton _("Start Routine Skip"):
                            style "interactive_map_secondary_button"
                            text_style "interactive_map_secondary_button_text"
                            xfill False
                            xsize 220
                            ysize 54
                            action confirm_action


style time_skip_compact_button is button:
    background Solid("#1a1510cc")
    hover_background Solid("#3a2c1ecc")
    insensitive_background Solid("#17120dcc")
    xfill False
    xpadding 0
    ypadding 0

style time_skip_compact_button_text is button_text:
    size 22
    color "#f5e5cb"
    hover_color "#ffddaa"
    text_align 0.5
    xalign 0.5
    yalign 0.5
