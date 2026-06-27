screen library_placeholder_page(category_id):

    $ category = library_get_category(category_id)
    $ category_title = _(category["title"]) if category else _("Library")
    $ category_subtitle = _(category["subtitle"]) if category else _("Explore special contents of Like Wind, Like Cloud")

    use library_menu_shell(
        page_title=category_title,
        page_subtitle=category_subtitle,
        back_action=ShowMenu("library")
    ):

        vbox:
            spacing 26

            text category_title:
                style "library_placeholder_title"

            text _("This section is now connected to the Library and ready for real content."):
                style "library_placeholder_body"

            text _("For now, this placeholder keeps the menu flow complete while profiles, galleries, music, and bonus materials are still being authored."):
                style "library_placeholder_body"

            frame:
                xsize 1160
                ysize 250
                background ui_frame_or_solid("gui/library/panel.png", "#120f0ccc", 24)

                vbox:
                    xpos 28
                    ypos 24
                    spacing 14

                    text _("Current status"):
                        style "library_placeholder_title"
                        size 30

                    text _("Unlocked progress: [library_get_progress_text(category_id)]"):
                        style "library_placeholder_body"

                    text _("Use this page as the future entry point for category-specific content and filters."):
                        style "library_placeholder_body"


screen library_characters():
    tag menu

    use library_menu_shell(
        page_title=_("Character Profiles"),
        page_subtitle=_("Learn about the characters in the story."),
        back_action=ShowMenu("library")
    ):

        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            ysize 620

            vbox:
                spacing 18

                for profile in CHARACTER_PROFILES:
                    use library_character_card(profile)


screen library_character_card(profile):

    $ unlocked = is_character_unlocked(profile)
    $ sprite_ref = profile.get("sprite", "")
    $ tags_text = ", ".join(profile.get("tags", []))
    $ has_route = profile.get("route") is not None

    frame:
        xsize 1148
        background ui_frame_or_solid("gui/library/panel.png", "#120f0ccc", 24)
        padding (24, 22)

        hbox:
            spacing 24

            # Character sprite / locked placeholder
            if unlocked and sprite_ref:
                add sprite_ref:
                    xysize (200, 200)
                    yalign 0.5
            elif unlocked:
                null width 200
            else:
                frame:
                    xysize (200, 200)
                    background Solid("#1A1511CC")
                    padding (0, 0)

                    text "?":
                        color LIB_DISABLED
                        size 58
                        xalign 0.5
                        yalign 0.5

            vbox:
                spacing 8
                xsize 950

                hbox:
                    spacing 12

                    text profile["name"]:
                        style "library_story_card_title"
                        color (LIB_TEXT if unlocked else LIB_DISABLED)

                    if has_route:
                        text "[" + profile["route"].title() + "]":
                            substitute False
                            style "library_story_meta"
                            color (LIB_GOLD if unlocked else LIB_DISABLED)
                    else:
                        text "[" + _("Supporting") + "]":
                            substitute False
                            style "library_story_meta"
                            color (LIB_MUTED if unlocked else LIB_DISABLED)

                text profile["description"]:
                    style "library_story_summary_text"
                    color (LIB_TEXT if unlocked else LIB_MUTED)

                null height 2

                text tags_text:
                    style "library_story_meta"
                    color (LIB_MUTED if unlocked else LIB_DISABLED)

                if not unlocked:
                    null height 6
                    text _("Complete a chapter in this character's route to unlock their profile."):
                        style "library_story_status_text"
                        color LIB_DISABLED


screen library_story_card(item):

    $ story_state = get_library_story_state(item)
    $ action_label = get_library_story_action_text(item)
    $ status_text = get_library_story_status_text(item)
    $ read_status = _("Read") if item["id"] in persistent.read_library_content else _("Unread")

    frame:
        xsize 1148
        background ui_frame_or_solid("gui/library/panel.png", "#120f0ccc", 24)
        padding (24, 22)

        vbox:
            spacing 16

            hbox:
                xfill True

                vbox:
                    spacing 8

                    text item["title"]:
                        style "library_story_card_title"

                    text item.get("series") or _("Original Stories"):
                        style "library_story_card_subtitle"

                null xfill True

                text status_text:
                    style "library_story_status_text"

            grid 2 3:
                xfill True
                spacing 16

                text _("Series") + ": " + (item.get("series") or _("Original Stories")):
                    style "library_story_meta"

                text _("Type") + ": " + item.get("type", "original_story").replace("_", " ").title():
                    style "library_story_meta"

                text _("Size") + ": " + item.get("size", "small").title():
                    style "library_story_meta"

                text _("Points") + ": " + str(item.get("point_cost", 0)):
                    style "library_story_meta"

                text _("Story Gate") + ": " + get_library_prerequisite_text(item):
                    style "library_story_meta"

                text _("Read status") + ": " + read_status:
                    style "library_story_meta"

            hbox:
                xfill True

                null xfill True

                if story_state in ["available", "read"]:
                    textbutton action_label:
                        style_prefix "library_story_button"
                        action ShowMenu("library_story_reader", content_id=item["id"])

                elif story_state == "unlockable":
                    textbutton action_label:
                        style_prefix "library_story_button"
                        action Show("library_story_unlock_confirm", content_id=item["id"])

                else:
                    textbutton action_label:
                        style_prefix "library_story_button"
                        action NullAction()
                        sensitive False


screen library_stories():
    tag menu

    $ story_items = get_library_story_items()

    use library_menu_shell(
        page_title=_("Original Stories"),
        page_subtitle=_("Read side stories and original materials."),
        back_action=ShowMenu("library")
    ):

        vbox:
            spacing 18

            text _("Spend points on optional side stories while core route progression stays chapter-based."):
                style "library_placeholder_body"

            hbox:
                xfill True

                text _("Investment Points: %(points)s") % {"points": persistent.investment_points}:
                    style "library_story_summary_text"

                null xfill True

                text _("Read status: %(status)s") % {"status": get_story_library_progress_text()}:
                    style "library_story_summary_text"

            if not story_items:
                text _("No original stories are available yet."):
                    style "library_placeholder_body"

            else:
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    ysize 566

                    vbox:
                        spacing 18

                        for item in story_items:
                            use library_story_card(item)


screen library_story_unlock_confirm(content_id):

    modal True
    zorder 250

    $ item = get_library_item(content_id)
    $ cost = item.get("point_cost", 0) if item else 0
    $ balance = persistent.investment_points
    $ remaining = max(0, balance - cost)

    add Solid("#00000088")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 720
        background ui_frame_or_solid("gui/library/panel.png", "#120f0cf2", 24)
        padding (34, 30)

        vbox:
            spacing 18

            text (_("Unlock “%(title)s”?") % {"title": item.get("title", "") if item else ""}):
                style "library_story_player_title"

            text (_("Cost: %(cost)s Investment Point(s)") % {"cost": cost}):
                style "library_story_meta"

            text (_("Current balance: %(balance)s") % {"balance": balance}):
                style "library_story_meta"

            text (_("Remaining after unlock: %(remaining)s") % {"remaining": remaining}):
                style "library_story_meta"

            hbox:
                spacing 18
                xalign 1.0

                textbutton _("Unlock"):
                    style_prefix "library_story_button"
                    action [
                        Function(attempt_unlock_library_content, content_id),
                        Hide("library_story_unlock_confirm")
                    ]

                textbutton _("Cancel"):
                    style_prefix "library_story_button"
                    action Hide("library_story_unlock_confirm")


screen library_cg():
    tag menu
    use library_placeholder_page("cg")


screen library_music():
    tag menu

    $ category = library_get_category("music")
    $ category_title = _(category["title"]) if category else _("Music Room")
    $ category_subtitle = _(category["subtitle"]) if category else _("Listen to unlocked music tracks.")
    $ music_items = get_music_library_items()

    use library_menu_shell(
        page_title=category_title,
        page_subtitle=category_subtitle,
        back_action=ShowMenu("library")
    ):

        vbox:
            spacing 26

            text category_title:
                style "library_placeholder_title"

            text _("Tracks unlock when you complete their linked story chapter for the first time."):
                style "library_placeholder_body"

            if not music_items:
                frame:
                    xsize 1160
                    ysize 120
                    background ui_frame_or_solid("gui/library/panel.png", "#120f0ccc", 24)
                    padding (28, 24)

                    text _("No music tracks were found in the music folder."):
                        style "library_placeholder_body"

            else:
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    ysize 560

                    vbox:
                        spacing 16

                        for item in music_items:
                            use library_music_card(item)


screen library_music_card(item):

    $ is_unlocked = is_library_content_unlocked(item["id"])
    $ prereq_text = get_library_prerequisite_text(item)
    $ is_playing = is_library_music_playing(item["id"])

    frame:
        xsize 1148
        background ui_frame_or_solid("gui/library/panel.png", "#120f0ccc", 24)
        padding (24, 22)

        vbox:
            spacing 16

            hbox:
                xfill True

                vbox:
                    spacing 8

                    text item["title"]:
                        style "library_story_card_title"

                    text item.get("series") or _("Original Soundtrack"):
                        style "library_story_card_subtitle"

                null xfill True

                if is_unlocked:
                    if is_playing:
                        text _("Playing") style "library_story_status_text"
                    else:
                        text _("Unlocked") style "library_story_status_text"
                else:
                    text _("Locked") style "library_story_status_text"

            grid 2 2:
                xfill True
                spacing 16

                text _("Story Gate") + ": " + prereq_text:
                    style "library_story_meta"

                text _("Status") + ": " + (_("Unlocked") if is_unlocked else _("Locked")):
                    style "library_story_meta"

            hbox:
                xfill True
                spacing 18

                null xfill True

                if is_unlocked and is_playing:
                    textbutton _("Stop"):
                        style_prefix "library_story_button"
                        action Function(stop_library_music_preview)

                if is_unlocked:
                    textbutton (_("Play Again") if is_playing else _("Play")):
                        style_prefix "library_story_button"
                        action Function(play_library_music_track, item["id"])
                else:
                    textbutton _("Locked"):
                        style_prefix "library_story_button"
                        action NullAction()


screen library_minigames():
    tag menu

    $ category = library_get_category("minigames")
    $ category_title = _(category["title"]) if category else _("Minigames")
    $ category_subtitle = _(category["subtitle"]) if category else _("Replay special minigames.")

    use library_menu_shell(
        page_title=category_title,
        page_subtitle=category_subtitle,
        back_action=ShowMenu("library")
    ):

        vbox:
            spacing 26

            text category_title:
                style "library_placeholder_title"

            text _("Replay minigames you have encountered in the story. Each minigame becomes available after you play it in the main route."):
                style "library_placeholder_body"

            # List all minigame library items
            $ minigame_items = [item for item in library_items.values() if item.get("category") == "minigames"]
            $ minigame_items.sort(key=lambda item: (item.get("series", ""), item.get("title", "")))

            if not minigame_items:
                frame:
                    xsize 1160
                    ysize 120
                    background ui_frame_or_solid("gui/library/panel.png", "#120f0ccc", 24)
                    padding (28, 24)

                    text _("No minigames are available yet. Play through the story to unlock them."):
                        style "library_placeholder_body"

            else:
                for item in minigame_items:
                    use library_minigame_card(item)


screen library_minigame_card(item):

    $ is_unlocked = is_library_content_unlocked(item["id"])
    $ prereq_text = get_library_prerequisite_text(item)
    $ replay_info = get_minigame_library_replay_info(item["id"])
    $ can_replay = is_unlocked and replay_info is not None

    frame:
        xsize 1148
        background ui_frame_or_solid("gui/library/panel.png", "#120f0ccc", 24)
        padding (24, 22)

        vbox:
            spacing 16

            hbox:
                xfill True

                vbox:
                    spacing 8

                    text item["title"]:
                        style "library_story_card_title"

                    text item.get("series") or _("Minigame"):
                        style "library_story_card_subtitle"

                null xfill True

                if is_unlocked:
                    text _("Available") style "library_story_status_text"
                else:
                    text _("Locked") style "library_story_status_text"

            grid 2 3:
                xfill True
                spacing 16

                text _("Series") + ": " + (item.get("series") or _("Minigame")):
                    style "library_story_meta"

                text _("Type") + ": " + item.get("type", "minigame").replace("_", " ").title():
                    style "library_story_meta"

                text _("Size") + ": " + item.get("size", "small").title():
                    style "library_story_meta"

                text _("Points") + ": " + str(item.get("point_cost", 0)):
                    style "library_story_meta"

                text _("Story Gate") + ": " + prereq_text:
                    style "library_story_meta"

                text _("Status") + ": " + (_("Unlocked") if is_unlocked else _("Locked")):
                    style "library_story_meta"

            hbox:
                xfill True

                null xfill True

                if can_replay:
                    textbutton _("Play"):
                        style_prefix "library_story_button"
                        action Call(replay_info["replay_label"], content_id=item["id"])
                elif is_unlocked:
                    textbutton _("No replay"):
                        style_prefix "library_story_button"
                        action NullAction()
                else:
                    textbutton _("Locked"):
                        style_prefix "library_story_button"
                        action NullAction()


screen library_extras():
    tag menu

    $ secret_list = list(SECRET_DEFINITIONS.items()) if "SECRET_DEFINITIONS" in globals() else []
    $ unlocked_count = get_unlocked_secret_count()

    use library_menu_shell(
        page_title=_("Extras"),
        page_subtitle=_("Bonus content and special materials."),
        back_action=ShowMenu("library")
    ):

        vbox:
            spacing 22

            text _("Secrets & Achievements"):
                style "library_placeholder_title"

            if unlocked_count == 0:
                text _("No secrets discovered yet. Keep playing to find hidden moments."):
                    style "library_placeholder_body"

                text _("(Total: %(total)d secrets)") % {"total": len(secret_list)}:
                    style "library_story_meta"

            else:
                text _("You have found %(count)d out of %(total)d secrets.") % {"count": unlocked_count, "total": len(secret_list)}:
                    style "library_placeholder_body"

                null height 8

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    ysize 520

                    vbox:
                        spacing 12

                        for secret_id, secret_def in secret_list:
                            $ is_unlocked = has_unlocked_secret(secret_id)
                            $ icon = secret_def.get("icon", "★")
                            $ title = secret_def.get("title", secret_id)
                            $ desc = secret_def.get("description", "")

                            frame:
                                xsize 1148
                                background ui_frame_or_solid("gui/library/panel.png", "#120f0ccc", 24)
                                padding (24, 18)

                                hbox:
                                    xfill True
                                    yfill True

                                    text icon:
                                        min_width 48
                                        size 40
                                        color (LIB_GOLD if is_unlocked else LIB_DISABLED)
                                        yalign 0.5

                                    vbox:
                                        xsize 1020
                                        spacing 6
                                        yalign 0.5

                                        if is_unlocked:
                                            text _(title):
                                                style "library_story_card_title"
                                                size 28

                                            text _(desc):
                                                style "library_story_meta"
                                        else:
                                            text _("???"):
                                                style "library_story_card_title"
                                                size 28
                                                color LIB_DISABLED

                                            text _("Not yet discovered"):
                                                style "library_story_meta"
                                                color LIB_DISABLED
