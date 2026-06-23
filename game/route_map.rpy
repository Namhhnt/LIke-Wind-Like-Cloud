label route_map(selected_route=DEFAULT_ROUTE_ID, selected_node=None):
    window hide
    $ initialize_progression()
    $ current_route = selected_route
    $ current_node = selected_node or timeline_get_first_selectable_node(current_route)
    $ next_action = None
    $ next_chapter = None

    python:
        while True:
            result = renpy.call_screen("timeline_chapter_map", route_id=current_route, selected_node_id=current_node)

            if not result:
                next_action = "exit"
                break

            action, chapter_id, current_route, current_node = result

            if action == "play":
                next_action = "play"
                next_chapter = chapter_id
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

            next_action = "exit"
            break

    if next_action == "play":
        jump expression next_chapter

    return
