screen debug_progression():
    tag menu

    use game_menu(_("Progress Debug"), scroll="viewport"):

        vbox:
            spacing 22

            text _("Prototype and progression diagnostics are grouped here so the player-facing route map stays clean."):
                style "route_map_summary"

            $ spoiler_reveal_label = "ON" if progression_debug_reveal_spoilers() else "OFF"
            $ completed_summary = chapter_list_safe_summary(progress["completed"])
            $ available_summary = chapter_list_safe_summary(progress["available"])
            $ excluded_summary = chapter_list_safe_summary(progress["excluded"])
            $ hidden_summary = chapter_list_safe_summary(progress["hidden"])

            text _("Spoiler Reveal: [spoiler_reveal_label]") style "route_map_summary"
            text _("Completed: [completed_summary]") style "route_map_summary"
            text _("Available: [available_summary]") style "route_map_summary"
            text _("Excluded: [excluded_summary]") style "route_map_summary"
            text _("Hidden: [hidden_summary]") style "route_map_summary"
            text _("Play Order: [get_play_order_summary()]") style "route_map_summary"
            text _("Unlocked Choices: [get_unlocked_choice_summary()]") style "route_map_summary"
            text _("Eligible Endings: [get_ending_summary()]") style "route_map_summary"
            text _("Validation: [get_validation_summary()]") style "route_map_summary"
            text _("Acceptance: [get_acceptance_summary()]") style "route_map_summary"

            hbox:
                spacing 18

                textbutton _("Toggle Spoiler Reveal") action Function(debug_toggle_spoiler_reveal)
                textbutton _("Refresh Validation") action Function(refresh_validation_state)
                textbutton _("Reset Progress") action Function(debug_reset_progress)
                textbutton _("Open Route Map") action Jump("route_map")

            null height 10

            for route_id in ROUTE_ORDER:
                frame:
                    style "route_map_panel"

                    vbox:
                        spacing 10

                        text ROUTES[route_id]["title"]:
                            style "route_map_route_title"

                        text _("Focus: [get_route_focus_summary(route_id)]"):
                            style "route_map_summary"

                        text _("Direction: [get_relationship_direction_summary(route_id)]"):
                            style "route_map_summary"

            null height 12

            text _("Complete Chapter") style "route_map_route_title"
            text _("Locked chapter names stay masked here too. Toggle spoiler reveal before using chapter-specific debug completion.") style "route_map_summary"

            grid 3 12:
                spacing 10

                for chapter_id in CHAPTER_ORDER:
                    textbutton chapter_safe_display_title(chapter_id):
                        action Function(debug_complete, chapter_id)
