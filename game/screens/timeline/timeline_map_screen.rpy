screen timeline_chapter_map(route_id=None, selected_node_id=None):
    tag menu
    modal True

    on "show" action [SetVariable("quick_menu", False), SetVariable("_map_rollback_saved", config.rollback_enabled), SetVariable("config.rollback_enabled", False)]
    on "hide" action [SetVariable("quick_menu", True), SetVariable("config.rollback_enabled", _map_rollback_saved)]

    default selected_route = timeline_normalize_route_id(route_id)
    default active_node_id = selected_node_id if selected_node_id else timeline_get_first_selectable_node(selected_route)

    $ screen_state = timeline_build_screen_state(selected_route, active_node_id, 1744)
    $ nodes = screen_state["nodes"]
    $ active_node_id = screen_state["active_node_id"]
    $ selected_node = screen_state["resolved_node"]
    $ selected_chapter_id = screen_state["selected_chapter_id"]
    $ selected_node_state = screen_state["selected_node_state"]
    $ selected_can_play = screen_state["selected_can_play"]
    $ canvas_w, canvas_h = screen_state["canvas_size"]
    $ viewport_xinitial = screen_state["viewport_xinitial"]
    $ node_render_positions = screen_state["node_render_positions"]
    $ node_states = screen_state["node_states"]
    $ viewport_yinitial = max(0.0, min(1.0, float((selected_node or {}).get("y", 0) - 80) / max(1, canvas_h - 450)))

    fixed:
        xysize (1920, 1080)

        add timeline_get_background_displayable()
        add Solid("#00000099")

        text _("Story Timeline"):
            style "timeline_title"
            xpos 80
            ypos 42

        text _("Your journey through the story"):
            style "timeline_subtitle"
            xpos 84
            ypos 118

        textbutton _("Back"):
            style "timeline_back_button"
            text_style "timeline_back_button_text"
            xpos 1670
            ypos 48
            action MainMenu(confirm=False)

        hbox:
            xpos 80
            ypos 158
            spacing 14

            for route in (TIMELINE_ROUTES if len(TIMELINE_ROUTES) > 1 else []):
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
                text _("Drag horizontally to travel through the story chronology"):
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
                    xinitial viewport_xinitial
                    yinitial viewport_yinitial

                    fixed:
                        xysize (canvas_w, canvas_h)

                        if nodes:
                            for label in screen_state["visible_lane_labels"]:
                                use timeline_lane_label(label)

                            for connection in screen_state["visible_connections"]:
                                use timeline_connection_line(connection)

                            for node in screen_state["visible_nodes"]:
                                $ render_x = node_render_positions.get(node["id"], node.get("x", 0))
                                if timeline_node_is_marker(node):
                                    use timeline_time_marker(node, render_x)
                                else:
                                    use timeline_node_card(node, active_node_id, render_x, node_states.get(node["id"]))
                        else:
                            text _("This timeline does not have nodes yet."):
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

                text _("Select a chapter to inspect it."):
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

                    text _("Actions") style "timeline_legend_title"

                    textbutton _("Play Chapter"):
                        style "timeline_play_button"
                        text_style "timeline_play_button_text"
                        sensitive selected_can_play
                        action Return(("play", selected_chapter_id, selected_route, selected_node["id"]))

                    textbutton _("Preview"):
                        style "timeline_secondary_button"
                        text_style "timeline_secondary_button_text"
                        sensitive bool(selected_chapter_id)
                        action Return(("preview", selected_chapter_id, selected_route, selected_node["id"]))

                    if selected_chapter_id and timeline_is_bookmarked(selected_chapter_id):
                        textbutton _("Remove Bookmark"):
                            style "timeline_secondary_button"
                            text_style "timeline_secondary_button_text"
                            action Return(("bookmark", selected_chapter_id, selected_route, selected_node["id"]))
                    else:
                        textbutton _("Bookmark"):
                            style "timeline_secondary_button"
                            text_style "timeline_secondary_button_text"
                            sensitive bool(selected_chapter_id)
                            action Return(("bookmark", selected_chapter_id, selected_route, selected_node["id"]))

        text "LIKE WIND, LIKE CLOUD":
            style "timeline_footer_text"
            xpos 80
            ypos 1038

        text _("Timeline positions are chronological; unrevealed structure is hidden from the player view."):
            style "timeline_footer_hint"
            xalign 0.5
            ypos 1038


screen timeline_lane_label(label):
    frame:
        style "timeline_lane_label_frame"
        xpos label.get("render_x", label.get("x", 0))
        ypos label.get("y", 0)
        xysize (label.get("w", 300), 34)

        text label.get("text", ""):
            style "timeline_lane_label_text"
            xalign 0.5
            yalign 0.5


screen timeline_time_marker(node, render_x=0):
    $ marker_w = node.get("w", 150)
    $ marker_h = node.get("h", 150)

    fixed:
        xpos render_x
        ypos node["y"]
        xysize (marker_w, marker_h)

        add Solid("#730f2fee"):
            xysize (marker_w, marker_h)

        add Solid("#f5d7a666"):
            xpos 4
            ypos 4
            xsize marker_w - 8
            ysize 3

        text node.get("title", ""):
            style "timeline_time_marker_text"
            xalign 0.5
            yalign 0.5
            text_align 0.5
            xmaximum marker_w - 20


screen timeline_node_card(node, selected_node_id, render_x=0, node_state=None):
    $ state = node_state if node_state is not None else timeline_get_node_state(node)
    $ is_selected = node["id"] == selected_node_id
    $ node_type = node.get("type", "core")
    $ is_revealed = timeline_should_reveal_node(node)
    $ node_style = "timeline_node_selected" if is_selected else "timeline_node"
    $ node_w = node["w"] + 44
    $ node_h = node["h"] + 44
    $ node_title = timeline_get_node_display_title(node)

    button:
        xpos render_x
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
                ysize 128

            add Solid("#00000099"):
                xpos 10
                ypos 10
                xsize node_w - 20
                ysize 128

            text timeline_get_safe_node_code(node):
                style "timeline_node_code"
                xpos 18
                ypos 18

            add Solid("#000000b0"):
                xpos 10
                ypos 138
                xsize node_w - 20
                ysize node_h - 148

            text node_title:
                style "timeline_node_title"
                xpos 16
                ypos 148
                xmaximum node_w - 32
                ymaximum 48

            hbox:
                xpos 16
                ypos 206
                spacing 6

                if state == "completed":
                    text "✓" style "timeline_status_completed_icon"
                    text _("Completed") style "timeline_status_completed_text"
                elif state == "current":
                    text "◷" style "timeline_status_current_icon"
                    text _("Current") style "timeline_status_current_text"
                else:
                    text "○" style "timeline_status_locked_icon"
                    text _("Locked") style "timeline_status_locked_text"

            if timeline_is_bookmarked(node.get("chapter_id")):
                text _("Saved"):
                    style "timeline_badge_bonus"
                    xpos node_w - 82
                    ypos 14

            if is_revealed:
                if node_type == "bonus":
                    text _("Bonus"):
                        style "timeline_badge_bonus"
                        xpos 16
                        ypos 112
                elif node_type == "pov":
                    text _("POV"):
                        style "timeline_badge_pov"
                        xpos 16
                        ypos 112


screen timeline_connection_line(connection):
    $ style_name = connection.get("style", "normal")
    $ line_color = connection.get("line_color", "#f0cc72" if style_name in ["branch", "merge", "dashed"] else "#d7b77d")
    $ dot_color = connection.get("dot_color", "#f5d7a6")
    $ from_x = connection.get("from_x")
    $ from_y = connection.get("from_y")
    $ to_x = connection.get("to_x")
    $ to_y = connection.get("to_y")
    $ mid_x = connection.get("mid_x")
    $ horizontal_width = connection.get("horizontal_width", 1)

    if from_x is not None and from_y is not None and to_x is not None and to_y is not None and mid_x is not None:
        if abs(from_y - to_y) < 20:
            if style_name == "dashed":
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
    $ route_label = timeline_get_route_label(node.get("origin_route", route_id))

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

                text "Track [route_label]" style "timeline_detail_meta"

                if state == "locked":
                    text _("Locked") style "timeline_detail_meta_locked"
                elif state == "completed":
                    text _("Completed") style "timeline_detail_meta"
                else:
                    text _("Unlocked") style "timeline_detail_meta"

            text _("Unlock Requirements"):
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
            #     text _("Planned Stat Modifiers"):
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
