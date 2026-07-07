init -1 python:
    def interactive_map_focus_entry(entry, map_zoom, canvas_size, viewport_size, focus_center):
        if not entry:
            return

        viewport = renpy.get_widget(None, "interactive_map_canvas")
        if viewport is None:
            return

        marker_x = int(entry.get("x", 960) * map_zoom)
        marker_y = int(entry.get("y", 540) * map_zoom)

        target_x = marker_x - focus_center[0]
        target_y = marker_y - focus_center[1]

        max_x = max(0, canvas_size[0] - viewport_size[0])
        max_y = max(0, canvas_size[1] - viewport_size[1])

        viewport.xadjustment.value = min(max(target_x, 0), max_x)
        viewport.yadjustment.value = min(max(target_y, 0), max_y)
        renpy.restart_interaction()


    def interactive_map_label_entries(entries):
        labels = []
        first_entries_by_location = {}
        hub_entries_by_location = {}
        ordered_location_ids = []

        for entry in entries:
            location_id = entry.get("location_id")
            if not location_id:
                continue

            if location_id not in first_entries_by_location:
                first_entries_by_location[location_id] = entry
                ordered_location_ids.append(location_id)

            if entry.get("kind") == "location_hub":
                hub_entries_by_location[location_id] = entry

        for location_id in ordered_location_ids:
            if not fixed_location_is_unlocked(location_id):
                continue

            entry = hub_entries_by_location.get(location_id, first_entries_by_location.get(location_id))
            if not entry:
                continue

            location = FIXED_MAP_LOCATIONS.get(location_id, {})
            labels.append({
                "id": "label_%s" % location_id,
                "title": location.get("name", entry.get("title", entry.get("name", location_id))),
                "x": location.get("x", entry.get("x", 960)),
                "y": location.get("y", entry.get("y", 540)),
                "state": entry.get("state", "available"),
                "source_entry": entry,
            })

        for entry in entries:
            state = entry.get("state", "available")
            if state != "available":
                continue

            if entry.get("category") == "temporary" or entry.get("kind") == "temporary":
                labels.append({
                    "id": "label_%s" % entry.get("id", len(labels)),
                    "title": entry.get("title", entry.get("name", "Temporary Location")),
                    "x": entry.get("x", 960),
                    "y": entry.get("y", 540),
                    "state": state,
                    "source_entry": entry,
                })

        return labels


screen interactive_map_screen(entries, context_id="act1_default", allow_back=True, allow_timeline=False, title_override=None):
    tag menu
    modal True

    on "show" action SetVariable("quick_menu", False)
    on "hide" action SetVariable("quick_menu", True)

    $ context = MAP_CONTEXTS.get(context_id, MAP_CONTEXTS["act1_default"])
    $ bg = time_get_map_background(context.get("background", "images/maps/city_map_day.png"))
    $ panel_bg = ui_frame_or_solid("gui/library/panel.png", "#140f0be6", 26)
    $ frame_bg = ui_frame_or_solid("gui/library/panel.png", "#201812f0", 26)
    $ map_zoom = 2.0
    $ map_canvas_size = (3344, 1882)
    $ map_viewport_size = (1920, 1080)
    $ map_focus_center = (760, 460)

    default hovered_entry = None
    default focus_target_entry = next((entry for entry in entries if entry.get("state") == "available"), entries[0] if entries else None)
    default events_panel_collapsed = False

    $ focus_entry = hovered_entry if hovered_entry else focus_target_entry
    $ events_panel_height = 158 if events_panel_collapsed else 798
    $ events_viewport_height = 0 if events_panel_collapsed else 544

    fixed:
        xysize (1920, 1080)

        if renpy.loadable(bg):
            add bg fit "cover"
        elif renpy.loadable("images/maps/city_map_day.png"):
            add "images/maps/city_map_day.png" fit "cover"
        else:
            add (mm_theme_asset("background_full.png") if mm_loadable(mm_theme_asset("background_full.png")) else Solid("#15120f")) fit "cover"

        add Solid("#05040355")
        add Solid("#1a120755") ypos 760 ysize 320

        viewport:
            id "interactive_map_canvas"
            xpos 0
            ypos 0
            xsize map_viewport_size[0]
            ysize map_viewport_size[1]
            draggable True
            xinitial 0.18
            yinitial 0.18

            fixed:
                xysize map_canvas_size

                if renpy.loadable(bg):
                    add Transform(bg, zoom=map_zoom)
                elif renpy.loadable("images/maps/city_map_day.png"):
                    add Transform("images/maps/city_map_day.png", zoom=map_zoom)
                else:
                    add Solid("#15120f")

                add Solid("#0806031c")

                for entry in entries:
                    use interactive_map_marker(entry, hovered_entry=hovered_entry, map_zoom=map_zoom)

                for label_entry in interactive_map_label_entries(entries):
                    use interactive_map_label_button(label_entry, hovered_entry=hovered_entry, map_zoom=map_zoom)

        use interactive_map_daily_hud(context_id=context_id, title_override=title_override)

        frame:
            xpos 58
            ypos 376
            xsize 620
            ysize 58
            background ui_frame_or_solid("gui/library/panel.png", "#100c09d8", 18)

            text _("Drag the map to explore the city. Use Focus to jump back to the current point of interest."):
                style "interactive_map_drag_hint"

        button:
            xpos 58
            ypos 456
            style "interactive_map_phone_button"
            action Return({"_action": "phone"})

            text "📱":
                xalign 0.5
                yalign 0.5
                style "interactive_map_phone_button_icon"

        if time_skip_is_available():
            button:
                xpos 58
                ypos 530
                style "interactive_map_phone_button"
                action Return({"_action": "time_skip"})

                text "⏭":
                    xalign 0.5
                    yalign 0.5
                    style "interactive_map_phone_button_icon"

        frame:
            xpos 1492
            ypos 48
            xsize 370
            ysize events_panel_height
            background panel_bg

            vbox:
                spacing 16
                xfill True

                hbox:
                    xfill True
                    spacing 12

                    text _("Map Locations & Story Events"):
                        style "interactive_map_panel_title"

                    null:
                        xfill True

                    textbutton (" + " if events_panel_collapsed else " - "):
                        style "interactive_map_panel_toggle_button"
                        text_style "interactive_map_panel_toggle_button_text"
                        action SetScreenVariable("events_panel_collapsed", not events_panel_collapsed)

                if not events_panel_collapsed:
                    text _("Pick a story event, or click an unlocked location to spend free time."):
                        style "interactive_map_panel_body"

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        ysize events_viewport_height

                        vbox:
                            spacing 10

                            for entry in entries:
                                $ state = entry.get("state", "available")
                                $ title = entry.get("title", entry.get("name", ""))
                                $ description = entry.get("description", "")
                                $ route_line = _("Location Hub") if entry.get("kind") == "location_hub" else (route_title(entry.get("route_id")) if entry.get("route_id") else _("Location"))
                                $ list_action = Return(entry) if state == "available" else NullAction()

                                button:
                                    style "interactive_map_list_button"
                                    hovered [SetScreenVariable("hovered_entry", entry), SetScreenVariable("focus_target_entry", entry)]
                                    unhovered SetScreenVariable("hovered_entry", None)
                                    sensitive state == "available"
                                    action list_action

                                    vbox:
                                        spacing 4
                                        xfill True

                                        text title:
                                            style ("interactive_map_list_title_locked" if state != "available" else "interactive_map_list_title")

                                        text route_line:
                                            style "interactive_map_list_meta"

                                        if state == "locked":
                                            text entry.get("lock_reason", _("Locked.")):
                                                style "interactive_map_list_meta_locked"
                                        elif description:
                                            text description:
                                                style "interactive_map_list_meta"

                if allow_timeline:
                    textbutton _("Open Timeline View"):
                        style "interactive_map_secondary_button"
                        text_style "interactive_map_secondary_button_text"
                        action Return({"_action": "timeline"})

                if allow_back:
                    textbutton _("Back"):
                        style "interactive_map_secondary_button"
                        text_style "interactive_map_secondary_button_text"
                        action Return(None)

        if hovered_entry:
            use map_hover_panel(hovered_entry, empty_prompt=False, focus_entry=focus_entry, map_zoom=map_zoom, map_canvas_size=map_canvas_size, map_viewport_size=map_viewport_size, map_focus_center=map_focus_center)
        elif entries:
            use map_hover_panel(entries[0], empty_prompt=True, focus_entry=focus_entry, map_zoom=map_zoom, map_canvas_size=map_canvas_size, map_viewport_size=map_viewport_size, map_focus_center=map_focus_center)


screen interactive_map_marker(entry, hovered_entry=None, map_zoom=1.0):
    $ state = entry.get("state", "available")
    $ kind = entry.get("kind", "extra")
    $ glyph = "◎" if kind == "location_hub" else ("◆" if kind == "main" else ("●" if kind in ["character", "bonus", "extra"] else "◌"))
    $ marker_style = "interactive_map_marker_main" if kind == "main" else ("interactive_map_marker_locked" if state != "available" else "interactive_map_marker")
    $ marker_text_style = "interactive_map_marker_text_locked" if state != "available" else ("interactive_map_marker_text_main" if kind == "main" else "interactive_map_marker_text")
    $ marker_action = Return(entry) if state == "available" else NullAction()

    button:
        style marker_style
        pos (int(entry.get("x", 960) * map_zoom), int(entry.get("y", 540) * map_zoom))
        anchor (0.5, 0.5)
        hovered [SetScreenVariable("hovered_entry", entry), SetScreenVariable("focus_target_entry", entry)]
        unhovered SetScreenVariable("hovered_entry", None)
        sensitive state == "available"
        action marker_action

        text glyph:
            style marker_text_style


screen interactive_map_label_button(label_entry, hovered_entry=None, map_zoom=1.0):
    $ entry = label_entry.get("source_entry")
    $ state = label_entry.get("state", "available")
    $ label_action = Return(entry) if state == "available" else NullAction()

    textbutton label_entry.get("title", ""):
        xpos int(label_entry.get("x", 960) * map_zoom)
        ypos int(label_entry.get("y", 540) * map_zoom) + 34
        xanchor 0.5
        style "interactive_map_marker_label_button"
        text_style "interactive_map_marker_label_button_text"
        hovered [SetScreenVariable("hovered_entry", entry), SetScreenVariable("focus_target_entry", entry)]
        unhovered SetScreenVariable("hovered_entry", None)
        sensitive state == "available"
        action label_action


screen map_hover_panel(entry, empty_prompt=False, focus_entry=None, map_zoom=1.0, map_canvas_size=(3344, 1882), map_viewport_size=(1920, 1080), map_focus_center=(760, 460)):
    $ state = entry.get("state", "available")
    $ title = entry.get("title", entry.get("name", ""))
    $ route_line = _("Location Hub") if entry.get("kind") == "location_hub" else (route_title(entry.get("route_id")) if entry.get("route_id") else _("Location"))

    frame:
        xpos 58
        ypos 900
        xsize 1336
        ysize 150
        background ui_frame_or_solid("gui/library/panel.png", "#120f0cf2", 24)

        hbox:
            spacing 24
            xfill True

            text ("◆" if entry.get("kind") == "main" else "●"):
                style "interactive_map_hover_icon"

            vbox:
                spacing 6
                xfill True

                text title:
                    style "interactive_map_hover_title"

                text route_line:
                    style "interactive_map_hover_meta"

                if state == "locked":
                    text entry.get("lock_reason", _("Locked.")):
                        style "interactive_map_hover_locked"
                elif entry.get("description"):
                    text entry.get("description"):
                        style "interactive_map_hover_body"
                elif empty_prompt:
                    text _("Choose an active marker to continue the story."):
                        style "interactive_map_hover_body"

            if focus_entry:
                textbutton _("Focus"):
                    style "interactive_map_focus_button"
                    text_style "interactive_map_focus_button_text"
                    yalign 0.5
                    action Function(interactive_map_focus_entry, focus_entry, map_zoom, map_canvas_size, map_viewport_size, map_focus_center)


style interactive_map_title is gui_text
style interactive_map_subtitle is gui_text
style interactive_map_panel_title is gui_text
style interactive_map_panel_body is gui_text
style interactive_map_panel_toggle_button is button
style interactive_map_panel_toggle_button_text is button_text
style interactive_map_canvas_frame is frame
style interactive_map_drag_hint is gui_text
style interactive_map_focus_button is button
style interactive_map_focus_button_text is button_text
style interactive_map_list_button is button
style interactive_map_list_title is gui_text
style interactive_map_list_title_locked is gui_text
style interactive_map_list_meta is gui_text
style interactive_map_list_meta_locked is gui_text
style interactive_map_secondary_button is button
style interactive_map_secondary_button_text is button_text
style interactive_map_phone_button is button
style interactive_map_phone_button_icon is gui_text
style interactive_map_marker is button
style interactive_map_marker_main is button
style interactive_map_marker_locked is button
style interactive_map_marker_text is gui_text
style interactive_map_marker_text_main is gui_text
style interactive_map_marker_text_locked is gui_text
style interactive_map_marker_label_button is button
style interactive_map_marker_label_button_text is button_text
style interactive_map_hover_icon is gui_text
style interactive_map_hover_title is gui_text
style interactive_map_hover_meta is gui_text
style interactive_map_hover_body is gui_text
style interactive_map_hover_locked is gui_text

style interactive_map_title:
    size 34
    bold True
    color "#ffbc51"
    outlines [(2, "#1a0e05", 0, 0)]

style interactive_map_subtitle:
    size 21
    color "#e7d8c0"
    outlines [(1, "#00000099", 0, 0)]

style interactive_map_panel_title:
    size 30
    bold True
    color "#ff6434"

style interactive_map_panel_body:
    size 19
    color "#ddccb5"
    line_spacing 2

style interactive_map_panel_toggle_button:
    background Solid("#1a1510cc")
    hover_background Solid("#3a2c1ecc")
    xsize 52
    ysize 42
    xpadding 0
    ypadding 0

style interactive_map_panel_toggle_button_text:
    size 24
    bold False
    color "#f5e5cb"
    hover_color "#ffddaa"
    text_align 0.5

style interactive_map_drag_hint:
    size 19
    color "#ead9c1"
    outlines [(1, "#00000088", 0, 0)]
    xalign 0.0
    yalign 0.5

style interactive_map_focus_button:
    background Solid("#1a1510d8")
    hover_background Solid("#3a2c1ef0")
    xsize 156
    ysize 56
    xpadding 18
    ypadding 10

style interactive_map_focus_button_text:
    size 24
    bold True
    color "#f5e5cb"
    hover_color "#ffddaa"

style interactive_map_list_button:
    background Solid("#211912cc")
    hover_background Solid("#3a2a1dde")
    insensitive_background Solid("#17110ccc")
    xfill True
    ypadding 12
    xpadding 16

style interactive_map_list_title:
    size 24
    bold True
    color "#f7e6c8"

style interactive_map_list_title_locked:
    size 24
    bold True
    color "#a99783"

style interactive_map_list_meta:
    size 18
    color "#d1c0a8"

style interactive_map_list_meta_locked:
    size 18
    color "#ad9b8a"

style interactive_map_secondary_button:
    background Solid("#1a1510cc")
    hover_background Solid("#3a2c1ecc")
    insensitive_background Solid("#17120dcc")
    xfill True
    ypadding 12
    xpadding 18

style interactive_map_secondary_button_text:
    size 22
    color "#f5e5cb"
    hover_color "#ffddaa"

style interactive_map_phone_button:
    background Solid("#1a1510e6")
    hover_background Solid("#3a2c1ee6")
    insensitive_background Solid("#17120dcc")
    xsize 64
    ysize 84
    xpadding 0
    ypadding 0

style interactive_map_phone_button_icon:
    size 64
    color "#ffcf84"
    hover_color "#fff0bf"
    outlines [(1, "#130c08cc", 0, 0)]

style interactive_map_marker:
    background None
    hover_background None
    insensitive_background None
    xysize (64, 64)

style interactive_map_marker_main:
    background None
    hover_background None
    insensitive_background None
    xysize (78, 78)

style interactive_map_marker_locked:
    background None
    hover_background None
    insensitive_background None
    xysize (60, 60)

style interactive_map_marker_text:
    size 44
    color "#ffd792"
    hover_color "#fff1c8"
    outlines [(2, "#1a0c00cc", 0, 0)]

style interactive_map_marker_text_main:
    size 56
    bold True
    color "#ffca62"
    hover_color "#fff0bf"
    outlines [(2, "#1a0c00dd", 0, 0)]

style interactive_map_marker_text_locked:
    size 40
    color "#8a7c70"
    outlines [(2, "#120d09dd", 0, 0)]

style interactive_map_marker_label_button:
    background Solid("#120d0988")
    hover_background Solid("#3b2a1ee8")
    xpadding 16
    ypadding 8
    xmaximum 300
    

style interactive_map_marker_label_button_text:
    size 16
    bold True
    color "#f6e3c4"
    hover_color "#ffddaa"
    text_align 0.5
    layout "subtitle"

style interactive_map_hover_icon:
    size 44
    color "#ffcf75"
    yalign 0.5

style interactive_map_hover_title:
    size 30
    bold True
    color "#f6e3c4"

style interactive_map_hover_meta:
    size 20
    color "#d7c5ac"

style interactive_map_hover_body:
    size 21
    color "#efe2cf"

style interactive_map_hover_locked:
    size 21
    color "#c4b4a1"
