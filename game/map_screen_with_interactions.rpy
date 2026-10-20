init -1 python:
    _map_rollback_saved = True
    _interactive_map_view_model_cache = {}
    INTERACTIVE_MAP_BASE_SIZE = (1680, 945)
    INTERACTIVE_MAP_MAX_TEXTURE_SIZE = 4096

    def interactive_map_get_safe_zoom(base_size, desired_zoom, max_texture_size=INTERACTIVE_MAP_MAX_TEXTURE_SIZE):
        base_width, base_height = base_size
        if base_width <= 0 or base_height <= 0:
            return desired_zoom

        max_zoom_x = float(max_texture_size) / float(base_width)
        max_zoom_y = float(max_texture_size) / float(base_height)
        return min(desired_zoom, max_zoom_x, max_zoom_y)

    def interactive_map_get_canvas_size(base_size, zoom):
        base_width, base_height = base_size
        return (int(round(base_width * zoom)), int(round(base_height * zoom)))

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

        clamped_x = min(max(target_x, 0), max_x)
        clamped_y = min(max(target_y, 0), max_y)

        if int(viewport.xadjustment.value) == clamped_x and int(viewport.yadjustment.value) == clamped_y:
            return

        viewport.xadjustment.value = clamped_x
        viewport.yadjustment.value = clamped_y
        renpy.restart_interaction()


    def interactive_map_entries_signature(entries):
        return tuple(
            (
                entry.get("id"),
                entry.get("location_id"),
                entry.get("kind"),
                entry.get("category"),
                entry.get("state"),
                entry.get("title"),
                entry.get("name"),
                entry.get("route_id"),
                entry.get("x"),
                entry.get("y"),
                entry.get("description"),
                entry.get("lock_reason"),
            )
            for entry in entries
        )

    def interactive_map_build_view_model(entries):
        signature = interactive_map_entries_signature(entries)
        cached = _interactive_map_view_model_cache.get(signature)
        if cached:
            return cached

        labels = []
        first_entries_by_location = {}
        hub_entries_by_location = {}
        ordered_location_ids = []
        panel_entries = []

        for entry in entries:
            location_id = entry.get("location_id")
            if location_id:
                if location_id not in first_entries_by_location:
                    first_entries_by_location[location_id] = entry
                    ordered_location_ids.append(location_id)

                if entry.get("kind") == "location_hub":
                    hub_entries_by_location[location_id] = entry

            state = entry.get("state", "available")
            title = entry.get("title", entry.get("name", ""))
            description = entry.get("description", "")
            route_line = _("Location Hub") if entry.get("kind") == "location_hub" else (route_title(entry.get("route_id")) if entry.get("route_id") else _("Location"))

            panel_entries.append({
                "entry": entry,
                "state": state,
                "title": title,
                "description": description,
                "route_line": route_line,
            })

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

        view_model = {
            "default_focus_entry": next((entry for entry in entries if entry.get("state") == "available"), entries[0] if entries else None),
            "label_entries": labels,
            "panel_entries": panel_entries,
        }

        if len(_interactive_map_view_model_cache) >= 24:
            _interactive_map_view_model_cache.clear()
        _interactive_map_view_model_cache[signature] = view_model
        return view_model

    def interactive_map_get_default_focus_entry(entries):
        return interactive_map_build_view_model(entries).get("default_focus_entry")


    def interactive_map_label_entries(entries):
        return list(interactive_map_build_view_model(entries).get("label_entries", []))


screen interactive_map_screen(entries, context_id="act1_default", allow_back=True, allow_timeline=False, title_override=None):
    tag menu
    modal True

    on "show" action [SetVariable("quick_menu", False), SetVariable("_map_rollback_saved", config.rollback_enabled), SetVariable("config.rollback_enabled", False)]
    on "hide" action [SetVariable("quick_menu", True), SetVariable("config.rollback_enabled", _map_rollback_saved)]

    $ context = MAP_CONTEXTS.get(context_id, MAP_CONTEXTS["act1_default"])
    $ bg = time_get_map_background(context.get("background", "images/maps/city_map_extend_day.webp"))
    $ panel_bg = ui_panel("#352b22bb", "#bda178bb", radius=22)
    $ frame_bg = ui_frame_or_solid("gui/library/panel.png", "#201812f0", 26)
    $ map_zoom = interactive_map_get_safe_zoom(INTERACTIVE_MAP_BASE_SIZE, 1.0)
    $ map_canvas_size = interactive_map_get_canvas_size(INTERACTIVE_MAP_BASE_SIZE, map_zoom)
    $ map_viewport_size = (1350, 680)
    $ map_focus_center = (675, 340)

    default hovered_entry = None
    default focus_target_entry = interactive_map_get_default_focus_entry(entries)
    default events_panel_collapsed = False

    $ map_view_model = interactive_map_build_view_model(entries)
    $ focus_entry = hovered_entry if hovered_entry else focus_target_entry
    $ events_panel_height = 158 if events_panel_collapsed else 798
    $ events_viewport_height = 0 if events_panel_collapsed else 544

    fixed:
        xysize (1920, 1080)

        add Transform("gui/theme/refined/rainy_library_v2.png", blur=6) fit "cover"

        add Solid("#05040355")
        add Solid("#1a120755") ypos 760 ysize 320

        viewport:
            id "interactive_map_canvas"
            xpos 58
            ypos 190
            xsize map_viewport_size[0]
            ysize map_viewport_size[1]
            draggable True
            xinitial 0.18
            yinitial 0.18

            fixed:
                xysize map_canvas_size

                if renpy.loadable(bg):
                    add Transform(bg, zoom=map_zoom)
                elif renpy.loadable("images/maps/city_map_extend_day.webp"):
                    add Transform("images/maps/city_map_extend_day.webp", zoom=map_zoom)
                else:
                    add Solid("#15120f")

                add Solid("#0806031c")

                for entry index entry.get("id") in sorted(entries, key=lambda item, target=focus_target_entry: item == target):
                    use interactive_map_marker(entry, hovered_entry=hovered_entry, focus_target_entry=focus_target_entry, map_zoom=map_zoom)

                for label_entry in map_view_model["label_entries"]:
                    if focus_entry and label_entry["source_entry"].get("location_id") == focus_entry.get("location_id"):
                        use interactive_map_label_button(label_entry, hovered_entry=hovered_entry, focus_target_entry=focus_target_entry, map_zoom=map_zoom)

        use interactive_map_daily_hud(
            context_id=context_id,
            title_override=title_override,
            phone_action=Return({"_action": "phone"}),
            skip_action=(Return({"_action": "time_skip"}) if time_skip_is_available() else None),
            timeline_action=(Return({"_action": "timeline"}) if allow_timeline else None),
            back_action=(Return(None) if allow_back else None),
        )

        frame:
            xpos 78
            ypos 800
            xsize 620
            ysize 58
            background ui_frame_or_solid("gui/library/panel.png", "#100c0933", 18)

            text _("Drag the map to explore the city. Use Focus to jump back to the current point of interest."):
                style "interactive_map_drag_hint"

        frame:
            xpos 1432
            ypos 190
            xsize 430
            ysize (158 if events_panel_collapsed else 862)
            background panel_bg
            padding (28, 28)

            vbox:
                spacing 16
                xfill True

                if time_get_main_today_summary():
                    text _("Main Today") style "interactive_map_panel_title"
                    text time_get_main_today_summary() style "interactive_map_panel_body"

                hbox:
                    xfill True
                    spacing 12

                    text _("Map Locations & Story Events"):
                        style "interactive_map_panel_title"
                        xmaximum 300

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
                        xsize 374
                        ysize (400 if time_get_main_today_summary() else 500)

                        vbox:
                            # Keep text wrapping identical during scrollbar
                            # measurement and the final draw; otherwise every
                            # row is laid out repeatedly at different widths.
                            xsize 350
                            spacing 10

                            for panel_entry index panel_entry["entry"].get("id") in map_view_model["panel_entries"]:
                                use interactive_map_list_entry(panel_entry, hovered_entry, focus_target_entry, map_zoom, map_canvas_size, map_viewport_size, map_focus_center)

        if not events_panel_collapsed:
            add Transform("gui/theme/refined/botanical_sprig_v2.png", alpha=0.38):
                pos (1694, 886)
                xysize (142, 142)

        if hovered_entry:
            use map_hover_panel(hovered_entry, empty_prompt=False, focus_entry=focus_entry, map_zoom=map_zoom, map_canvas_size=map_canvas_size, map_viewport_size=map_viewport_size, map_focus_center=map_focus_center)
        elif focus_entry:
            use map_hover_panel(focus_entry, focus_entry=focus_entry, map_zoom=map_zoom, map_canvas_size=map_canvas_size, map_viewport_size=map_viewport_size, map_focus_center=map_focus_center)


# A parameterized row has its own stable local scope. Reassigning title/state
# in the parent loop invalidated every Text layout on every interaction.
screen interactive_map_list_entry(panel_entry, hovered_entry, focus_target_entry, map_zoom, map_canvas_size, map_viewport_size, map_focus_center):
    $ entry = panel_entry["entry"]
    $ state = panel_entry["state"]
    button:
        id ("map_location_" + entry["id"])
        style "interactive_map_list_button"
        hovered If(
            hovered_entry != entry or focus_target_entry != entry,
            true=[SetScreenVariable("hovered_entry", entry), SetScreenVariable("focus_target_entry", entry)],
            false=NullAction(),
        )
        unhovered If(hovered_entry is not None, true=SetScreenVariable("hovered_entry", None), false=NullAction())
        action [SetScreenVariable("focus_target_entry", entry), Function(interactive_map_focus_entry, entry, map_zoom, map_canvas_size, map_viewport_size, map_focus_center)]
        vbox:
            spacing 4
            xfill True
            text panel_entry["title"]:
                style ("interactive_map_list_title_locked" if state != "available" else "interactive_map_list_title")
            text panel_entry["route_line"] style "interactive_map_list_meta"
            if state == "locked":
                text entry.get("lock_reason", _("Locked.")) style "interactive_map_list_meta_locked"
            elif panel_entry["description"]:
                text panel_entry["description"] style "interactive_map_list_meta"


screen interactive_map_marker(entry, hovered_entry=None, focus_target_entry=None, map_zoom=1.0):
    $ state = entry.get("state", "available")
    $ kind = entry.get("kind", "extra")
    $ glyph = "◎" if kind == "location_hub" else ("◆" if kind == "main" else ("●" if kind in ["character", "bonus", "extra"] else "◌"))
    $ marker_style = "interactive_map_marker_locked" if state != "available" else ("interactive_map_marker_main" if kind == "main" else "interactive_map_marker")
    $ marker_text_style = "interactive_map_marker_text_locked" if state != "available" else ("interactive_map_marker_text_main" if kind == "main" else "interactive_map_marker_text")
    $ marker_action = SetScreenVariable("focus_target_entry", entry)

    button:
        style marker_style
        pos (int(entry.get("x", 960) * map_zoom), int(entry.get("y", 540) * map_zoom))
        anchor (0.5, 0.5)
        hovered If(
            hovered_entry != entry or focus_target_entry != entry,
            true=[SetScreenVariable("hovered_entry", entry), SetScreenVariable("focus_target_entry", entry)],
            false=NullAction(),
        )
        unhovered If(
            hovered_entry is not None,
            true=SetScreenVariable("hovered_entry", None),
            false=NullAction(),
        )
        action marker_action

        add ui_map_pin(locked=state != "available", selected=entry == focus_target_entry, kind={"company": "building", "airport": "plane", "cafe": "cup", "coffee_shop": "cup"}.get(entry.get("location_id"), "home")):
            align (0.5, 0.5)


screen interactive_map_label_button(label_entry, hovered_entry=None, focus_target_entry=None, map_zoom=1.0):
    $ entry = label_entry.get("source_entry")
    $ state = label_entry.get("state", "available")
    $ label_action = SetScreenVariable("focus_target_entry", entry)

    textbutton label_entry.get("title", ""):
        xpos int(label_entry.get("x", 960) * map_zoom)
        ypos int(label_entry.get("y", 540) * map_zoom) + 34
        xanchor 0.5
        style "interactive_map_marker_label_button"
        text_style "interactive_map_marker_label_button_text"
        hovered If(
            hovered_entry != entry or focus_target_entry != entry,
            true=[SetScreenVariable("hovered_entry", entry), SetScreenVariable("focus_target_entry", entry)],
            false=NullAction(),
        )
        unhovered If(
            hovered_entry is not None,
            true=SetScreenVariable("hovered_entry", None),
            false=NullAction(),
        )
        action label_action


screen map_hover_panel(entry, empty_prompt=False, focus_entry=None, map_zoom=1.0, map_canvas_size=(4096, 2305), map_viewport_size=(1920, 1080), map_focus_center=(760, 460)):
    $ state = entry.get("state", "available")
    $ title = entry.get("title", entry.get("name", ""))
    $ route_line = _("Location Hub") if entry.get("kind") == "location_hub" else (route_title(entry.get("route_id")) if entry.get("route_id") else _("Location"))
    $ preview_path = {"company": "images/assets/bg/bg_company_lobby_morning.webp", "airport": "images/assets/bg/bg_airport_arrival_day.webp", "nguyen_family_house": "images/assets/bg/bg_tam_family_entry_evening.webp", "tam_apartment": "images/assets/bg/bg_tam_living_room_morning.webp", "restaurant": "images/assets/bg/bg_luxury_restaurant_evening.webp"}.get(entry.get("location_id"), time_get_map_background("images/maps/city_map_extend_day.webp"))

    frame:
        xpos 58
        ypos 888
        xsize 1350
        ysize 164
        background ui_panel("#2a2018df", "#c3a06bba", ornate=True)
        padding (40, 24)

        hbox:
            spacing 24
            xfill True

            add preview_path:
                xysize (220, 116)
                fit "cover"

            vbox:
                spacing 6
                xsize 660

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
                vbox:
                    spacing 6
                    xsize 310
                    button:
                        id "map_go_to_location"
                        style "interactive_map_secondary_button"
                        background ui_panel("#a78148bb", "#f5d49bee", radius=30)
                        hover_background ui_panel("#bc965bcf", "#ffebc9", radius=30)
                        sensitive state == "available"
                        action Return(entry)
                        text _("Go to location"):
                            style "interactive_map_secondary_button_text"
                            color ("#ffcf83" if state == "available" else "#9b8a74")
                    textbutton _("Focus"):
                        # xpos 1136
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
style interactive_map_header_action_button is button
style interactive_map_header_action_button_text is button_text
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
    size 26
    bold False
    font "fonts/NotoSerif-Italic.ttf"
    color "#efe0c5"

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
    background ui_panel("#38291f88", "#c3a67688", radius=24)
    hover_background ui_panel("#604631aa", "#e4bf7abb", radius=24)
    xsize 156
    ysize 56
    xpadding 18
    ypadding 10

style interactive_map_focus_button_text:
    size 24
    bold False
    color "#fff0d6"
    hover_color "#fff8e8"

style interactive_map_list_button:
    background ui_panel("#34291fa0", "#a6885666", radius=14)
    hover_background ui_panel("#80613eaa", "#e4bf7abb", radius=14)
    insensitive_background Solid("#17110ccc")
    xfill True
    ypadding 12
    xpadding 16

style interactive_map_list_title:
    size 24
    bold False
    color "#f7e6c8"

style interactive_map_list_title_locked:
    size 24
    bold False
    color "#a99783"

style interactive_map_list_meta:
    size 18
    color "#d1c0a8"

style interactive_map_list_meta_locked:
    size 18
    color "#ad9b8a"

style interactive_map_secondary_button:
    background ui_panel("#60452d99", "#b8956388", radius=24)
    hover_background ui_panel("#89643eaa", "#e4bf7abb", radius=24)
    insensitive_background Solid("#17120dcc")
    xfill True
    ypadding 12
    xpadding 18

style interactive_map_secondary_button_text:
    size 22
    color "#ffcf83"
    hover_color "#ffddaa"
    xalign 0.5

style interactive_map_header_action_button:
    background Solid("#1a151000")
    hover_background Solid("#bd7d3df0")
    xysize (125, 125)
    xpadding 0
    ypadding 0

style interactive_map_header_action_button_text:
    size 80
    color "#ffcf84"
    hover_color "#fff0bf"
    text_align 0.5
    xalign 0.5
    yalign 0.5
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
    background ui_panel("#20170fbb", "#c3a67699", radius=8)
    hover_background ui_panel("#3b2a1ee8", "#e4bf7abb", radius=8)
    xpadding 16
    ypadding 8
    xmaximum 300
    

style interactive_map_marker_label_button_text:
    size 20
    bold False
    color "#f6e3c4"
    hover_color "#ffddaa"
    text_align 0.5
    layout "subtitle"

style interactive_map_hover_icon:
    size 44
    color "#ffcf75"
    yalign 0.5

style interactive_map_hover_title:
    size 34
    bold False
    font "fonts/NotoSerif-Italic.ttf"
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
