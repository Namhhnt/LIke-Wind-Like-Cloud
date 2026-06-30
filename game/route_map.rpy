# FILE: game/route_map.rpy
# Purpose: Safe route-map entry label for the full skeleton chapter map.
# It keeps the existing screen contract:
#   timeline_chapter_map returns (action, chapter_id, route_id, node_id)

label route_map(selected_route=DEFAULT_ROUTE_ID, selected_node=None):
    if selected_route != DEFAULT_ROUTE_ID or selected_node is not None:
        call route_map_timeline(selected_route=selected_route, selected_node=selected_node)
        return

    $ resolved_context_id = resolve_story_map_context()
    call story_hub(context_id=resolved_context_id)
    return


label route_map_timeline(selected_route=DEFAULT_ROUTE_ID, selected_node=None):
    window hide
    $ initialize_progression()
    $ current_route, current_node = timeline_resolve_route_selection(selected_route, selected_node)
    $ next_action = None
    $ next_chapter = None

    python:
        while True:
            result = renpy.call_screen(
                "timeline_chapter_map",
                route_id=current_route,
                selected_node_id=current_node,
            )

            if not result:
                next_action = "exit"
                break

            action, chapter_id, returned_route, returned_node = result
            current_route = returned_route or current_route
            current_node = returned_node or current_node

            if action == "play":
                if chapter_id not in CHAPTERS:
                    renpy.notify("Unknown chapter: %s" % chapter_id)
                    continue

                label_name = CHAPTERS[chapter_id].get("label", chapter_id)
                if not renpy.has_label(label_name):
                    renpy.notify("Missing label: %s" % label_name)
                    continue

                next_action = "play"
                next_chapter = label_name
                break

            if action == "preview":
                node = timeline_find_node(current_route, current_node)
                if node:
                    renpy.notify(timeline_get_preview_text(node))
                else:
                    renpy.notify("No chapter preview is available.")
                continue

            if action == "bookmark":
                added = timeline_toggle_bookmark(chapter_id)
                if added:
                    renpy.notify("Bookmark saved.")
                else:
                    renpy.notify("Bookmark removed.")
                continue

            if action == "change_route":
                current_route, current_node = timeline_resolve_route_selection(current_route, current_node)
                continue

            next_action = "exit"
            break

    if next_action == "play":
        jump expression next_chapter

    return
