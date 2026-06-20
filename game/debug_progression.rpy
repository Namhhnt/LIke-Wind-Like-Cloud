screen debug_progression():
    modal True

    frame:
        background Solid("#111111ee")
        xalign 0.5
        yalign 0.5
        xsize 1400
        ysize 820
        xpadding 28
        ypadding 28

        vbox:
            spacing 18

            text _("Progression Debug") style "route_map_title"

            text _("Completed: [', '.join(progress['completed']) if progress['completed'] else 'None']") style "route_map_summary"
            text _("Available: [', '.join(progress['available']) if progress['available'] else 'None']") style "route_map_summary"
            text _("Excluded: [', '.join(progress['excluded']) if progress['excluded'] else 'None']") style "route_map_summary"
            text _("Choices: [get_unlocked_choice_summary()]") style "route_map_summary"
            text _("Eligible Endings: [get_ending_summary()]") style "route_map_summary"

            text _("Complete Chapter") style "route_map_route_title"

            grid 3 3:
                spacing 10

                for chapter_id in CHAPTER_ORDER:
                    textbutton chapter_title(chapter_id):
                        action Function(debug_complete, chapter_id)

            hbox:
                spacing 18
                textbutton _("Reset Progress") action Function(debug_reset_progress)
                textbutton _("Close Debug") action Hide("debug_progression")
