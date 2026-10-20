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
        return int(1280 * story_sprite_render_xpos(sprite))

    def story_sprite_render_ypos(sprite):
        lane = story_sprite_lane(sprite)
        if lane == "center":
            return 484
        return 656

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
    default reading_hidden = False

    $ compact = ui_is_compact()
    $ item = get_library_item(content_id)
    $ parsed_story = load_and_parse_library_story(item) if item else None
    $ story_pages = parsed_story.get("pages", []) if parsed_story else []
    $ page = story_pages[page_index] if story_pages else None

    on "show" action Function(mark_library_content_read, content_id)

    if compact and item and is_library_content_unlocked(content_id) and story_pages:
        use library_story_fullscreen(item, story_pages, page, page_index, reading_hidden)
    else:
        use library_story_desktop(content_id, item, story_pages, page, page_index, reading_hidden)

    key "K_h" action ToggleScreenVariable("reading_hidden")
    if story_pages:
        key "K_RIGHT" action SetScreenVariable("page_index", min(len(story_pages) - 1, page_index + 1))
        key "K_LEFT" action SetScreenVariable("page_index", max(0, page_index - 1))


style story_reader_icon_button is button:
    background ui_panel("#241e19dd", "#8f7755", radius=22)
    hover_background ui_panel("#594432ee", "#d6b477", radius=22)
    insensitive_background ui_panel("#241e1977", "#8f775555", radius=22)
    xysize (112, 112)
    padding (20, 20)


style story_reader_text is default:
    font gui.interface_text_font
    color "#f5e8d2"

screen library_story_fullscreen(item, story_pages, page, page_index, reading_hidden):
    style_prefix "story_reader"
    key "game_menu" action ShowMenu("library_stories")
    add Solid("#241e19")
    if page["background_display"]:
        add page["background_display"] xysize (1920, 1080) fit "contain"

    # CGs already contain their characters; ordinary backgrounds keep the
    # authored sprite directions, scaled with the 16:9 stage.
    if "cg_" not in (page.get("background_display") or ""):
        for sprite in page["sprites"]:
            if sprite["display_name"]:
                add sprite["display_name"]:
                    xpos int(story_sprite_render_xpixel(sprite) * 1.5)
                    xanchor story_sprite_render_xanchor(sprite)
                    ypos int(story_sprite_render_ypos(sprite) * 1.5)
                    yanchor 1.0
                    zoom story_sprite_render_zoom(sprite) * 1.5

    if reading_hidden:
        button:
            id "story_show_ui"
            style "story_reader_icon_button"
            pos (1712, 24)
            alt _("Show UI")
            tooltip _("Show UI")
            action SetScreenVariable("reading_hidden", False)
            add ui_icon("stories", medallion=False) xysize (72, 72)
    else:
        frame:
            pos (240, 24)
            xysize (1456, 112)
            padding (24, 12)
            background ui_panel("#241e19bb", "#8f775566", radius=20)
            fixed:
                xfill True
                yfill True
                text item["title"] size 44 color "#f5e8d2" yalign 0.5 xmaximum 1000
                text renpy.translate_string(_("Page %(current)s/%(total)s")) % {"current": page_index + 1, "total": len(story_pages)}:
                    size 40
                    color "#cdbb9e"
                    align (1.0, 0.5)
        button:
            id "story_back"
            style "story_reader_icon_button"
            pos (96, 24)
            alt _("Back to Stories")
            tooltip _("Back to Stories")
            action ShowMenu("library_stories")
            add ui_icon("back", medallion=False) xysize (72, 72)
        button:
            id "story_hide_ui"
            style "story_reader_icon_button"
            pos (1712, 24)
            alt _("Hide UI")
            tooltip _("Hide UI")
            action SetScreenVariable("reading_hidden", True)
            add ui_icon("cg", medallion=False) xysize (72, 72)
        # Keep paging beside the dialogue instead of adding a second control
        # row below it. The narrow buttons still retain a mobile-safe hit area.
        frame:
            pos (208, 650)
            xysize (1504, 382)
            padding (36, 24)
            background ui_panel("#241e19dd", "#8f7755", radius=24)
            vbox:
                spacing 12
                if page["speaker"]:
                    text page["speaker"] size 44 color "#d6b477"
                viewport:
                    id "story_compact_text"
                    xfill True
                    ysize (270 if page["speaker"] else 326)
                    mousewheel True
                    draggable True
                    scrollbars "vertical"
                    text page["text"] size 42 color "#f5e8d2" xmaximum 1396 line_spacing 8
        button:
            id "story_previous"
            style "story_reader_icon_button"
            pos (96, 755)
            xysize (96, 172)
            padding (0, 0)
            alt _("Previous")
            tooltip _("Previous")
            sensitive page_index > 0
            action SetScreenVariable("page_index", page_index - 1)
            text "‹" font "DejaVuSans.ttf" size 72 color "#f3d6a1" align (0.5, 0.5)
        button:
            id "story_next"
            style "story_reader_icon_button"
            pos (1728, 755)
            xysize (96, 172)
            padding (0, 0)
            alt _("Next")
            tooltip _("Next")
            sensitive page_index < len(story_pages) - 1
            action SetScreenVariable("page_index", page_index + 1)
            text "›" font "DejaVuSans.ttf" size 72 color "#f3d6a1" align (0.5, 0.5)


screen library_story_desktop(content_id, item, story_pages, page, page_index, reading_hidden):
    use library_menu_shell(
        page_title=(item.get("title") if item else _("Original Stories")),
        page_subtitle=(item.get("series") if item else _("Read side stories and original materials.")),
        back_action=ShowMenu("library_stories"),
        back_label=_("Back to Stories"),
        cinema=True
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
                id "story_stage"
                xysize (1280, 720)

                frame:
                    xysize (1280, 720)
                    padding (0, 0)
                    background None

                    fixed:
                        xysize (1280, 720)
                        clipping True

                        if page["background_display"]:
                            add page["background_display"]:
                                xysize (1280, 720)
                                fit "contain"
                        else:
                            add Solid("#1D1611")

                        if "cg_" not in (page.get("background_display") or ""):
                            for sprite in page["sprites"]:
                                if sprite["display_name"]:
                                    add sprite["display_name"]:
                                        xpos story_sprite_render_xpixel(sprite)
                                        xanchor story_sprite_render_xanchor(sprite)
                                        ypos story_sprite_render_ypos(sprite)
                                        yanchor 1.0
                                        zoom story_sprite_render_zoom(sprite)

                        frame:
                            xpos 36
                            ypos 486
                            xsize 1208
                            ysize 170
                            background ui_panel("#0B0806D9", radius=18)
                            padding (28, 18)

                            vbox:
                                spacing 10

                                if page["speaker"]:
                                    text page["speaker"]:
                                        style "library_story_speaker"

                                viewport:
                                    xfill True
                                    ysize (92 if page["speaker"] else 134)
                                    mousewheel True
                                    draggable True
                                    scrollbars "vertical"
                                    text page["text"]:
                                        style "library_story_text"

                fixed:
                    xpos 36
                    ypos 664
                    xsize 1208
                    ysize 52

                    button:
                        id "story_previous"
                        style "library_story_button_button"
                        action SetScreenVariable("page_index", max(0, page_index - 1))
                        sensitive page_index > 0
                        text _("Previous") style "library_story_button_text"

                    button:
                        id "story_next"
                        xalign 1.0
                        style "library_story_button_button"
                        action SetScreenVariable("page_index", min(len(story_pages) - 1, page_index + 1))
                        sensitive page_index < len(story_pages) - 1
                        text _("Next") style "library_story_button_text"
