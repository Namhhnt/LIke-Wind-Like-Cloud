# Isolated review samples. Nothing here calls progression, read, reply, or save APIs.
init -1 python:
    def ui_review_reading_pages():
        with renpy.file("stories/yuuka/sunday_market.md") as source:
            parsed = parse_story_text(source.read().decode("utf-8-sig"))
        return build_story_reader_pages(parsed)

    def ui_review_phone_messages(thread_id, reply_id):
        # Build a fresh list: the authored dictionaries are never extended.
        messages = list(PHONE_THREADS[thread_id].get("messages", []))
        for reply in PHONE_REPLY_CHOICES.get(thread_id, []):
            if reply.get("id") == reply_id:
                messages += [{"sender": "player", "text": reply["text"], "time": "22:53"}]
                messages += list(reply.get("response_messages", []))
        return messages


style ui_review_read_text is default:
    font "fonts/NotoSerif-Regular.ttf"
    color "#f5e8d2"

style ui_review_read_button is button:
    background ui_panel("#322920f2", "#8f7755", radius=18)
    hover_background ui_panel("#5a4634", "#d6b477", radius=18)
    selected_background ui_panel("#5a4634", "#d6b477", radius=18)
    insensitive_background ui_panel("#241e19ee", "#655541", radius=18)
    padding (20, 12)

style ui_review_read_button_text is button_text:
    font "fonts/NotoSerif-Regular.ttf"
    size 30
    color "#f5e8d2"
    hover_color "#ffffff"
    insensitive_color "#8f806c"
    text_align 0.5
    align (0.5, 0.5)


screen ui_review_phone(compact=False):
    tag menu
    style_prefix "ui_review_read"
    default selected_thread = "tam_hoang_after_party_01"
    default selected_reply = None
    default compact_list = False
    $ thread = PHONE_THREADS[selected_thread]
    $ messages = ui_review_phone_messages(selected_thread, selected_reply)
    $ reply_choices = PHONE_REPLY_CHOICES.get(selected_thread, [])
    $ phone_width = 1728 if compact else 720
    $ phone_x = 0 if compact else 760
    $ font_size = 40 if compact else 30
    $ bubble_width = 1300 if compact else 580

    use ui_review_shell(_("Phone"), compact):
        fixed:
            xysize (1728, 820)

            if not compact or compact_list:
                frame:
                    pos ((0 if compact else 140), 0)
                    xysize ((1728 if compact else 580), 820)
                    padding (24, 20)
                    background ui_panel("#241e19ee", "#8f7755", radius=28)
                    vbox:
                        spacing 20
                        hbox:
                            spacing 14
                            add ui_icon("messages", medallion=False) xysize (56, 56)
                            text _("Messages") size (44 if compact else 36) color "#f5e8d2" yalign 0.5
                        viewport:
                            ysize 700
                            xfill True
                            mousewheel True
                            draggable True
                            scrollbars "vertical"
                            vbox:
                                spacing 16
                                xfill True
                                for thread_id, row in PHONE_THREADS.items():
                                    button:
                                        style "ui_review_read_button"
                                        xfill True
                                        ysize (156 if compact else 142)
                                        selected selected_thread == thread_id
                                        action [SetScreenVariable("selected_thread", thread_id), SetScreenVariable("selected_reply", None), SetScreenVariable("compact_list", False)]
                                        vbox:
                                            spacing 8
                                            text row["title"] size font_size color "#f5e8d2"
                                            text row["messages"][-1]["text"]:
                                                size (40 if compact else 26)
                                                color "#cdbb9e"
                                                xmaximum (1600 if compact else 460)
                                                layout "subtitle"
                                                ymaximum (54 if compact else 66)

            if not compact or not compact_list:
                frame:
                    pos (phone_x, 0)
                    xysize (phone_width, 820)
                    padding (0, 0)
                    background ui_panel("#241e19ee", "#8f7755", radius=30)
                    fixed:
                        xysize (phone_width, 820)
                        hbox:
                            pos (24, 16)
                            spacing 16
                            if compact:
                                button:
                                    id "review_phone_list"
                                    style "ui_review_read_button"
                                    xysize (104, 104)
                                    action SetScreenVariable("compact_list", True)
                                    add ui_icon("back", medallion=False) xysize (64, 64) align (0.5, 0.5)
                            else:
                                add ui_icon("messages", medallion=False) xysize (72, 72)
                            vbox:
                                yalign 0.5
                                text thread["title"] size (46 if compact else 36) color "#f5e8d2"
                                text _("Messages") size font_size color "#cdbb9e"

                        viewport:
                            id "ui_review_message_scroll"
                            pos (24, 136)
                            xysize (phone_width - 48, 352 if reply_choices else 642)
                            yinitial 1.0
                            mousewheel True
                            draggable True
                            scrollbars "vertical"
                            vbox:
                                spacing 18
                                xfill True
                                for message in messages:
                                    $ outgoing = message.get("sender") == "player"
                                    vbox:
                                        xfill True
                                        spacing 5
                                        frame:
                                            xalign (1.0 if outgoing else 0.0)
                                            xmaximum bubble_width
                                            padding (20, 14)
                                            background ui_panel("#594432f2" if outgoing else "#322920f2", "#8f7755", radius=20)
                                            text message["text"]:
                                                size font_size
                                                color "#f5e8d2"
                                                xmaximum bubble_width - 48
                                        text ((renpy.translate_string(_("You")) if outgoing else PHONE_CONTACTS.get(message.get("sender"), {}).get("display_name", message.get("sender", ""))) + "  ·  " + message.get("time", "")):
                                            xalign (1.0 if outgoing else 0.0)
                                            size (40 if compact else 24)
                                            color "#cdbb9e"

                        if reply_choices:
                            frame:
                                pos (16, 508)
                                xysize (phone_width - 32, 296)
                                padding (16, 10)
                                background ui_panel("#322920f2", "#8f7755", radius=22)
                                vbox:
                                    spacing 10
                                    text _("Reply once") size font_size color "#d6b477"
                                    viewport:
                                        ysize 218
                                        xfill True
                                        mousewheel True
                                        draggable True
                                        scrollbars "vertical"
                                        vbox:
                                            spacing 10
                                            xfill True
                                            for reply in reply_choices:
                                                textbutton reply["text"]:
                                                    style "ui_review_read_button"
                                                    text_size font_size
                                                    xfill True
                                                    yminimum 104
                                                    selected selected_reply == reply["id"]
                                                    action SetScreenVariable("selected_reply", reply["id"])


screen ui_review_reader(compact=False):
    tag menu
    style_prefix "ui_review_read"
    default pages = ui_review_reading_pages()
    default page_index = 12
    default reading_hidden = False
    $ page = pages[page_index]
    $ artwork = page.get("background_display") or "images/assets/cg/cg_yuuka_minh_market_walk.webp"
    if compact:
        fixed:
            xysize (1920, 1080)
            add Solid("#241e19")
            add artwork xysize (1920, 1080) fit "contain"
            if reading_hidden:
                button:
                    id "review_show_ui"
                    style "ui_review_read_button"
                    pos (1712, 24)
                    xysize (112, 112)
                    alt _("Show UI")
                    tooltip _("Show UI")
                    action SetScreenVariable("reading_hidden", False)
                    add ui_icon("stories", medallion=False) xysize (72, 72) align (0.5, 0.5)
            else:
                frame:
                    pos (240, 24)
                    xysize (1456, 112)
                    padding (24, 12)
                    background ui_panel("#241e19bb", "#8f775566", radius=20)
                    fixed:
                        xfill True
                        yfill True
                        text _("Sunday Market") size 44 color "#f5e8d2" yalign 0.5
                        text renpy.translate_string(_("Page %(current)s/%(total)s")) % {"current": page_index + 1, "total": len(pages)}:
                            size 40
                            color "#cdbb9e"
                            align (1.0, 0.5)
                button:
                    id "review_reader_back"
                    style "ui_review_read_button"
                    pos (96, 24)
                    xysize (112, 112)
                    alt _("Back")
                    tooltip _("Back")
                    action ShowMenu("ui_review_hub", compact=True)
                    add ui_icon("back", medallion=False) xysize (72, 72) align (0.5, 0.5)
                button:
                    id "review_hide_ui"
                    style "ui_review_read_button"
                    pos (1712, 24)
                    xysize (112, 112)
                    alt _("Hide UI")
                    tooltip _("Hide UI")
                    action SetScreenVariable("reading_hidden", True)
                    add ui_icon("cg", medallion=False) xysize (72, 72) align (0.5, 0.5)

                frame:
                    pos (96, 700)
                    xysize (1728, 240)
                    padding (32, 20)
                    background ui_panel("#241e19dd", "#8f7755", radius=24)
                    vbox:
                        spacing 8
                        if page["speaker"]:
                            text page["speaker"] size 44 color "#d6b477"
                        viewport:
                            id "ui_review_reading_text_compact"
                            xfill True
                            ysize (136 if page["speaker"] else 200)
                            mousewheel True
                            draggable True
                            scrollbars "vertical"
                            text page["text"] size 42 color "#f5e8d2" xmaximum 1624 line_spacing 8
                button:
                    id "review_previous"
                    style "ui_review_read_button"
                    pos (96, 952)
                    xysize (112, 112)
                    alt _("Previous")
                    tooltip _("Previous")
                    sensitive page_index > 0
                    action SetScreenVariable("page_index", page_index - 1)
                    add ui_icon("back", medallion=False) xysize (72, 72) align (0.5, 0.5)
                button:
                    id "review_next"
                    style "ui_review_read_button"
                    pos (1712, 952)
                    xysize (112, 112)
                    alt _("Next")
                    tooltip _("Next")
                    sensitive page_index < len(pages) - 1
                    action SetScreenVariable("page_index", page_index + 1)
                    add Transform(ui_icon("back", medallion=False), xzoom=-1) xysize (72, 72) align (0.5, 0.5)

    else:
        use ui_review_shell(_("Sunday Market"), compact):
            fixed:
                xysize (1728, 820)
                frame:
                    pos ((136 if reading_hidden else 0), 0)
                    xysize (1456, 819)
                    padding (0, 0)
                    background "#241e19ee"
                    add artwork xysize (1456, 819) fit "contain"
                if reading_hidden:
                    textbutton _("Show UI"):
                        id "review_show_ui"
                        style "ui_review_read_button"
                        text_size 30
                        pos (1280, 696)
                        xysize (424, 104)
                        action SetScreenVariable("reading_hidden", False)
                else:
                    frame:
                        pos (32, 560)
                        xysize (1392, 228)
                        padding (28, 18)
                        background ui_panel("#241e19ee", "#8f7755", radius=22)
                        vbox:
                            spacing 8
                            if page["speaker"]:
                                text page["speaker"] size 34 color "#d6b477"
                            viewport:
                                id "ui_review_reading_text_desktop"
                                xfill True
                                ysize (134 if page["speaker"] else 186)
                                mousewheel True
                                draggable True
                                scrollbars "vertical"
                                text page["text"] size 32 color "#f5e8d2" xmaximum 1312 line_spacing 6
                    vbox:
                        pos (1480, 0)
                        xsize 248
                        spacing 18
                        add ui_icon("stories", medallion=False) xysize (96, 96) xalign 0.5
                        text renpy.translate_string(_("Page %(current)s/%(total)s")) % {"current": page_index + 1, "total": len(pages)}:
                            size 28
                            color "#cdbb9e"
                            xalign 0.5
                        textbutton _("Previous"):
                            id "review_previous"
                            style "ui_review_read_button"
                            xysize (248, 104)
                            sensitive page_index > 0
                            action SetScreenVariable("page_index", page_index - 1)
                        textbutton _("Next"):
                            id "review_next"
                            style "ui_review_read_button"
                            xysize (248, 104)
                            sensitive page_index < len(pages) - 1
                            action SetScreenVariable("page_index", page_index + 1)
                        textbutton _("Hide UI"):
                            id "review_hide_ui"
                            style "ui_review_read_button"
                            xysize (248, 104)
                            action SetScreenVariable("reading_hidden", True)

    key "K_h" action ToggleScreenVariable("reading_hidden")
    key "K_RIGHT" action SetScreenVariable("page_index", min(len(pages) - 1, page_index + 1))
    key "K_LEFT" action SetScreenVariable("page_index", max(0, page_index - 1))
