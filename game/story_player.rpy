init -1 python:
    def story_sprite_xpos(position):
        if position == "left":
            return 0.24
        if position == "right":
            return 0.76
        return 0.5

    def story_sprite_is_side_image(sprite):
        display_name = sprite.get("display_name") or ""
        return display_name.startswith("side ")

    def story_sprite_lane(sprite):
        lane = sprite.get("position") or "center"
        if lane not in ["left", "center", "right"]:
            lane = "center"

        if story_sprite_is_side_image(sprite) and lane == "center":
            return "left"

        return lane

    def story_sprite_render_xpos(sprite):
        lane = story_sprite_lane(sprite)
        if lane == "left":
            return 0.03
        if lane == "right":
            return 0.97
        return 0.5

    def story_sprite_render_xpixel(sprite):
        return int(1206 * story_sprite_render_xpos(sprite))

    def story_sprite_render_ypos(sprite):
        lane = story_sprite_lane(sprite)
        if lane == "center":
            return 484
        return 640

    def story_sprite_render_xanchor(sprite):
        lane = story_sprite_lane(sprite)
        if lane == "left":
            return 0.0
        if lane == "right":
            return 1.0
        return 0.5

    def story_sprite_render_zoom(sprite):
        lane = story_sprite_lane(sprite)
        if lane == "center":
            return 0.9
        if story_sprite_is_side_image(sprite):
            return 0.65
        return 0.84


screen library_story_reader(content_id):

    tag menu

    default page_index = 0

    $ item = get_library_item(content_id)
    $ parsed_story = load_and_parse_library_story(item) if item else None
    $ story_pages = parsed_story.get("pages", []) if parsed_story else []
    $ page = story_pages[page_index] if story_pages else None

    on "show" action Function(mark_library_content_read, content_id)

    use library_menu_shell(
        page_title=(item.get("title") if item else _("Original Stories")),
        page_subtitle=(item.get("series") if item else _("Read side stories and original materials.")),
        back_action=ShowMenu("library_stories"),
        back_label=_("Back to Stories")
    ):

        if not item:
            vbox:
                spacing 20

                text _("This story could not be found."):
                    style "library_placeholder_title"

                text _("Return to the Library and try another story."):
                    style "library_placeholder_body"

        elif not is_library_content_unlocked(content_id):
            vbox:
                spacing 20

                text _("This story is locked."):
                    style "library_placeholder_title"

                text get_library_prerequisite_text(item):
                    style "library_placeholder_body"

        elif not story_pages:
            vbox:
                spacing 20

                text _("This story could not be loaded."):
                    style "library_placeholder_title"

                text _("The file may be missing or invalid."):
                    style "library_placeholder_body"

        else:
            fixed:
                xsize 1206
                ysize 676

                frame:
                    xsize 1206
                    ysize 676
                    background ui_frame_or_solid("gui/library/panel.png", "#120f0ccc", 24)

                    fixed:
                        xsize 1206
                        ysize 676

                        if page["background_display"]:
                            add page["background_display"]:
                                xsize 1206
                                ysize 676
                                fit "cover"
                        else:
                            add Solid("#1D1611")

                        add Solid("#00000055")

                        frame:
                            xpos 36
                            ypos 28
                            xsize 1134
                            background Solid("#120d0ab8")
                            padding (22, 14)

                            hbox:
                                xfill True

                                text item["title"]:
                                    style "library_story_player_title"

                                null xfill True

                                text _("Page %(current)s/%(total)s") % {"current": page_index + 1, "total": len(story_pages)}:
                                    style "library_story_meta"

                        frame:
                            xpos 36
                            ypos 470
                            xsize 1134
                            ysize 170
                            background Solid("#0B0806D9")
                            padding (174, 18)

                            vbox:
                                spacing 10

                                if page["speaker"]:
                                    text page["speaker"]:
                                        style "library_story_speaker"

                                text page["text"]:
                                    style "library_story_text"

                        for sprite in page["sprites"]:
                            if sprite["display_name"]:
                                add sprite["display_name"]:
                                    xpos story_sprite_render_xpixel(sprite)
                                    xanchor story_sprite_render_xanchor(sprite)
                                    ypos story_sprite_render_ypos(sprite)
                                    yanchor 1.0
                                    zoom story_sprite_render_zoom(sprite)

                hbox:
                    xpos 0
                    ypos 648
                    xsize 1506
                    spacing 16

                    textbutton _("Previous"):
                        style_prefix "library_story_button"
                        action SetScreenVariable("page_index", max(0, page_index - 1))
                        sensitive page_index > 0

                    null xfill True

                    textbutton _("Next"):
                        style_prefix "library_story_button"
                        action SetScreenVariable("page_index", min(len(story_pages) - 1, page_index + 1))
                        sensitive page_index < len(story_pages) - 1
