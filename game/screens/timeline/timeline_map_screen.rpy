screen timeline_chapter_map(route_id="tam", selected_node_id=None):
    tag menu
    modal True

    on "show" action SetVariable("quick_menu", False)
    on "hide" action SetVariable("quick_menu", True)

    default selected_route = route_id
    default active_node_id = selected_node_id if selected_node_id else timeline_get_first_selectable_node(route_id)

    $ nodes = timeline_get_nodes(selected_route)
    $ resolved_node = timeline_resolve_selected_node(selected_route, active_node_id)
    $ active_node_id = resolved_node["id"] if resolved_node else None
    $ selected_node = resolved_node

    $ selected_chapter_id = selected_node["chapter_id"] if selected_node else None
    $ selected_node_state = timeline_get_node_state(selected_node) if selected_node else None
    $ selected_can_play = (selected_node_state == "current" and timeline_has_runtime_chapter(selected_chapter_id)) if selected_chapter_id else False

    fixed:
        xysize (1920, 1080)

        add timeline_get_background_displayable()
        add Solid("#00000099")

        text "Timeline Chapter Map":
            style "timeline_title"
            xpos 80
            ypos 42

        text "Track route progress, branches, and future chapters.":
            style "timeline_subtitle"
            xpos 84
            ypos 118

        textbutton "Back":
            style "timeline_back_button"
            text_style "timeline_back_button_text"
            xpos 1670
            ypos 48
            action MainMenu(confirm=False)

        hbox:
            xpos 80
            ypos 158
            spacing 14

            for route in TIMELINE_ROUTES:
                $ is_selected = route["id"] == selected_route
                $ route_style = "timeline_route_tab_selected" if is_selected else "timeline_route_tab"
                $ route_text_style = "timeline_route_tab_text_selected" if is_selected else "timeline_route_tab_text"

                textbutton route["label"]:
                    style route_style
                    text_style route_text_style
                    action [
                        SetScreenVariable("selected_route", route["id"]),
                        SetScreenVariable("active_node_id", timeline_get_first_selectable_node(route["id"]))
                    ]

        frame:
            style "timeline_map_panel"
            xpos 64
            ypos 210
            xysize (1792, 506)

            fixed:
                text "Drag horizontally to explore the route timeline":
                    style "timeline_scroll_hint"
                    xalign 0.5
                    ypos 16

                viewport:
                    id "timeline_map_viewport"
                    xpos 24
                    ypos 52
                    xsize 1744
                    ysize 450
                    draggable True
                    mousewheel True

                    fixed:
                        xysize (2560, 950)

                        if nodes:
                            for connection in timeline_get_connections(selected_route):
                                use timeline_connection_line(selected_route, connection)

                            for node in nodes:
                                use timeline_node_card(node, active_node_id)
                        else:
                            text "This route does not have timeline nodes yet.":
                                style "timeline_empty_state"
                                xpos 700
                                ypos 170

                bar:
                    value XScrollValue("timeline_map_viewport")
                    xpos 0
                    ypos 502
                    xsize 1792
                    ysize 8

        if selected_node:
            use timeline_detail_panel(selected_route, selected_node)
        else:
            frame:
                style "timeline_detail_panel"
                xpos 64
                ypos 730
                xysize (1430, 300)

                text "Select a route tab to inspect its chapters.":
                    style "timeline_empty_state"
                    xalign 0.5
                    yalign 0.5

        if selected_node:
            frame:
                style "timeline_legend_panel"
                xpos 1518
                ypos 730
                xysize (338, 300)

                vbox:
                    xpos 28
                    ypos 24
                    spacing 14

                    text "Actions" style "timeline_legend_title"

                    textbutton "Play Chapter":
                        style "timeline_play_button"
                        text_style "timeline_play_button_text"
                        sensitive selected_can_play
                        action Return(("play", selected_chapter_id, selected_route, selected_node["id"]))

                    textbutton "Preview":
                        style "timeline_secondary_button"
                        text_style "timeline_secondary_button_text"
                        action Return(("preview", selected_chapter_id, selected_route, selected_node["id"]))

                    if timeline_is_bookmarked(selected_chapter_id):
                        textbutton "Remove Bookmark":
                            style "timeline_secondary_button"
                            text_style "timeline_secondary_button_text"
                            action Return(("bookmark", selected_chapter_id, selected_route, selected_node["id"]))
                    else:
                        textbutton "Bookmark":
                            style "timeline_secondary_button"
                            text_style "timeline_secondary_button_text"
                            action Return(("bookmark", selected_chapter_id, selected_route, selected_node["id"]))

        text "LIKE WIND, LIKE CLOUD":
            style "timeline_footer_text"
            xpos 80
            ypos 1038

        text "Locked future nodes can still be previewed and bookmarked.":
            style "timeline_footer_hint"
            xalign 0.5
            ypos 1038

screen timeline_node_card(node, selected_node_id):
    $ state = timeline_get_node_state(node)
    $ is_selected = node["id"] == selected_node_id
    $ node_type = node.get("type", "core")
    $ node_style = "timeline_node_selected" if is_selected else "timeline_node"
    $ node_w = node["w"] + 44
    $ node_h = node["h"] + 44

    button:
        xpos node["x"]
        ypos node["y"]
        xysize (node_w, node_h)
        style node_style
        action SetScreenVariable("active_node_id", node["id"])

        fixed:
            xysize (node_w, node_h)

            add timeline_get_thumbnail_displayable(node):
                xpos 10
                ypos 10
                xsize node_w - 20
                ysize 136

            add Solid("#0000008f"):
                xpos 10
                ypos 136
                xsize node_w - 20
                ysize node_h - 146

            text node["code"]:
                style "timeline_node_code"
                xpos 116
                ypos 162

            hbox:
                xpos 16
                ypos 202
                spacing 6

                if state == "completed":
                    text "✓" style "timeline_status_completed_icon"
                    text "Completed" style "timeline_status_completed_text"
                elif state == "current":
                    text "◷" style "timeline_status_current_icon"
                    text "Current" style "timeline_status_current_text"
                else:
                    text "○" style "timeline_status_locked_icon"
                    text "Locked" style "timeline_status_locked_text"

            if timeline_is_bookmarked(node["chapter_id"]):
                text "Saved":
                    style "timeline_badge_bonus"
                    xpos node_w - 82
                    ypos 14

            if node_type == "bonus":
                text "Bonus":
                    style "timeline_badge_bonus"
                    xpos 16
                    ypos 204
            elif node_type == "pov":
                text "POV":
                    style "timeline_badge_pov"
                    xpos 16
                    ypos 204

screen timeline_connection_line(route_id, connection):
    $ from_node = timeline_find_node(route_id, connection["from"])
    $ to_node = timeline_find_node(route_id, connection["to"])
    $ line_color = "#f0cc72" if connection.get("style") == "dashed" else "#d7b77d"
    $ dot_color = "#f5d7a6"
    $ from_w = from_node["w"] + 44 if from_node else 0
    $ from_h = from_node["h"] + 38 if from_node else 0
    $ to_h = to_node["h"] + 38 if to_node else 0

    if from_node and to_node:
        $ from_x = from_node["x"] + from_w
        $ from_y = from_node["y"] + int(from_h / 2)
        $ to_x = to_node["x"]
        $ to_y = to_node["y"] + int(to_h / 2)
        $ mid_x = int((from_x + to_x) / 2)
        $ horizontal_width = max(1, to_x - from_x)

        if abs(from_y - to_y) < 20:
            if connection.get("style") == "dashed":
                for dash_x in range(from_x, to_x, 22):
                    add Solid(line_color):
                        xpos dash_x
                        ypos from_y
                        xsize min(12, max(0, to_x - dash_x))
                        ysize 3
            else:
                add Solid(line_color):
                    xpos from_x
                    ypos from_y
                    xsize horizontal_width
                    ysize 3

            add Solid(dot_color):
                xpos to_x - 5
                ypos to_y - 5
                xsize 10
                ysize 10
        else:
            add Solid(line_color):
                xpos from_x
                ypos from_y
                xsize max(1, mid_x - from_x)
                ysize 3

            add Solid(line_color):
                xpos mid_x
                ypos min(from_y, to_y)
                xsize 3
                ysize abs(to_y - from_y)

            add Solid(line_color):
                xpos mid_x
                ypos to_y
                xsize max(1, to_x - mid_x)
                ysize 3

            add Solid(dot_color):
                xpos to_x - 5
                ypos to_y - 5
                xsize 10
                ysize 10

screen timeline_detail_panel(route_id, node):
    $ state = timeline_get_node_state(node)
    $ requirements = timeline_get_requirement_lines(node)
    $ stat_modifiers = timeline_get_node_stat_modifiers(node)
    $ detail_title = timeline_get_detail_title(node)
    $ detail_summary = timeline_get_node_summary(node)

    frame:
        style "timeline_detail_panel"
        xpos 64
        ypos 730
        xysize (1430, 300)

        fixed:
            add timeline_get_thumbnail_displayable(node):
                xpos 24
                ypos 24
                xysize (380, 252)

            text "[detail_title]":
                style "timeline_detail_title"
                xpos 442
                ypos 34
                xmaximum 500

            text detail_summary:
                style "timeline_detail_summary"
                xpos 442
                ypos 118
                xmaximum 480

            hbox:
                xpos 442
                ypos 248
                spacing 24

                text "Time [node.get('duration', 'Approx. 20 min')]" style "timeline_detail_meta"

                if state == "locked":
                    text "Locked" style "timeline_detail_meta_locked"
                elif state == "completed":
                    text "Completed" style "timeline_detail_meta"
                else:
                    text "Unlocked" style "timeline_detail_meta"

            text "Unlock Requirements":
                style "timeline_requirements_title"
                xpos 960
                ypos 36
                xmaximum 460

            vbox:
                xpos 960
                ypos 80
                xmaximum 460
                spacing 9

                for done, label in requirements:
                    use timeline_requirement_line(done, label)

            # if stat_modifiers:
            #     text "Planned Stat Modifiers":
            #         style "timeline_requirements_title"
            #         xpos 960
            #         ypos 188

            #     vbox:
            #         xpos 960
            #         ypos 226
            #         spacing 7

            #         for stat_line in stat_modifiers[:3]:
            #             text stat_line:
            #                 style "timeline_stat_text"
            #                 xmaximum 300



screen timeline_requirement_line(done, label):
    hbox:
        spacing 8

        if done:
            text "✓" style "timeline_status_completed_icon"
        else:
            text "○" style "timeline_status_locked_icon"

        text label style "timeline_requirement_text"


