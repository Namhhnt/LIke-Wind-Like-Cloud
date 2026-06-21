screen debug_progression():
    tag menu

    use game_menu(_("Progress Debug"), scroll="viewport"):

        vbox:
            spacing 22

            text _("Prototype and progression diagnostics are grouped here so the player-facing route map stays clean."):
                style "route_map_summary"

            text _("Completed: [', '.join(progress['completed']) if progress['completed'] else 'None']") style "route_map_summary"
            text _("Available: [', '.join(progress['available']) if progress['available'] else 'None']") style "route_map_summary"
            text _("Excluded: [', '.join(progress['excluded']) if progress['excluded'] else 'None']") style "route_map_summary"
            text _("Play Order: [get_play_order_summary()]") style "route_map_summary"
            text _("Unlocked Choices: [get_unlocked_choice_summary()]") style "route_map_summary"
            text _("Eligible Endings: [get_ending_summary()]") style "route_map_summary"
            text _("Validation: [get_validation_summary()]") style "route_map_summary"
            text _("Acceptance: [get_acceptance_summary()]") style "route_map_summary"

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

            grid 3 3:
                spacing 10

                for chapter_id in CHAPTER_ORDER:
                    textbutton chapter_title(chapter_id):
                        action Function(debug_complete, chapter_id)

            hbox:
                spacing 18

                textbutton _("Refresh Validation") action Function(refresh_validation_state)
                textbutton _("Reset Progress") action Function(debug_reset_progress)
                textbutton _("Open Route Map") action Jump("route_map")
