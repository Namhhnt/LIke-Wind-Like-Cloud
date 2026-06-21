style route_map_root_frame is empty
style route_map_panel is frame
style route_map_title is gui_text
style route_map_summary is gui_text
style route_map_route_title is gui_text
style route_map_route_status is gui_text
style route_map_chapter_button is button
style route_map_chapter_button_text is button_text
style route_map_recommended_text is gui_text
style route_map_completed_text is gui_text
style route_map_locked_text is gui_text

style route_map_panel:
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
    xpadding 24
    ypadding 24

style route_map_title:
    size 54
    color gui.selected_color
    text_align 0.5

style route_map_summary:
    size 22
    color gui.idle_small_color
    text_align 0.5

style route_map_route_title:
    size 34
    color gui.selected_color

style route_map_route_status:
    size 22
    color gui.accent_color

style route_map_chapter_button:
    properties gui.button_properties("button")
    xfill True

style route_map_chapter_button_text:
    properties gui.text_properties("button")
    xalign 0.0

style route_map_recommended_text:
    size 20
    color gui.hover_color

style route_map_completed_text:
    size 24
    color gui.idle_small_color

style route_map_locked_text:
    size 24
    color gui.insensitive_color

screen route_map():
    modal True

    add gui.game_menu_background

    frame:
        style "route_map_root_frame"
        background Solid("#050507aa")
        xfill True
        yfill True

    viewport:
        xalign 0.5
        yalign 0.5
        xsize 1560
        ysize 860
        draggable True
        mousewheel True

        vbox:
            spacing 24

            text _("Route Map"):
                style "route_map_title"
                xalign 0.5

            if progress["recommended_next"]:
                text _("Recommended Next: [', '.join(chapter_title(chapter_id) for chapter_id in progress['recommended_next'])]"):
                    style "route_map_summary"
                    xalign 0.5

            for route_id in ROUTE_ORDER:
                $ route = ROUTES[route_id]
                $ route_chapters = get_route_chapters(route_id)
                $ route_status = get_route_status_label(route_id)

                frame:
                    style "route_map_panel"

                    vbox:
                        spacing 14

                        text route["title"]:
                            style "route_map_route_title"

                        if route_status == "completed":
                            text _("Completed") style "route_map_route_status"
                        elif route_status == "partially_unlocked":
                            text _("In Progress") style "route_map_route_status"
                        elif route_status == "available":
                            text _("Available") style "route_map_route_status"
                        else:
                            text _("Locked") style "route_map_route_status"

                        if route_chapters:
                            for chapter_id in route_chapters:
                                $ chapter_state = get_chapter_state(chapter_id)

                                if chapter_state == "available":
                                    textbutton chapter_title(chapter_id):
                                        style "route_map_chapter_button"
                                        action Return(chapter_id)

                                    if is_recommended_chapter(chapter_id):
                                        text _("Recommended next chapter"):
                                            style "route_map_recommended_text"

                                elif chapter_state == "completed":
                                    text "[chapter_title(chapter_id)] - [_(\"Completed\")]":
                                        style "route_map_completed_text"

                                elif chapter_state == "excluded":
                                    text "[chapter_title(chapter_id)] - [_(\"Excluded\")]":
                                        style "route_map_locked_text"

                                else:
                                    text "[chapter_title(chapter_id)] - [_(\"Locked\")]":
                                        style "route_map_locked_text"
                        else:
                            text _("No chapters are configured for this route yet."):
                                style "route_map_locked_text"

            if not progress["available"] and not progress["completed"]:
                text _("No chapters are available yet."):
                    style "route_map_summary"
                    xalign 0.5

            hbox:
                xalign 0.5
                spacing 18

                textbutton _("Main Menu") action MainMenu(confirm=False)
                textbutton _("Load") action ShowMenu("load")


label route_map:
    $ initialize_progression()
    $ selected_chapter = renpy.call_screen("route_map")

    if selected_chapter:
        jump expression selected_chapter

    return
