init -2:
    define PHONE_BG = "#120d0bf6"
    define PHONE_SHELL = "#1a1411f6"
    define PHONE_PANEL = "#221913f0"
    define PHONE_PANEL_ALT = "#2c2018f0"
    define PHONE_PANEL_HOVER = "#3a2a1ff0"
    define PHONE_TEXT = "#f5e8d0"
    define PHONE_MUTED = "#c8b69a"
    define PHONE_ACCENT = "#e4bf7a"
    define PHONE_BORDER = "#8d6740"
    define PHONE_UNREAD = "#d76752"

style phone_status_text is default:
    color PHONE_TEXT
    size 17
    font gui.interface_text_font

style phone_title_text is default:
    color PHONE_TEXT
    size 38
    font gui.interface_text_font
    outlines [(1, "#00000088", 0, 1)]

style phone_subtitle_text is default:
    color PHONE_MUTED
    size 17
    font gui.interface_text_font

style phone_nav_button is button:
    background Solid(PHONE_PANEL_ALT)
    hover_background Solid(PHONE_PANEL_HOVER)
    padding (14, 10)

style phone_nav_button_text is button_text:
    color PHONE_TEXT
    hover_color PHONE_ACCENT
    size 21
    font gui.interface_text_font

style phone_home_tile_button is button:
    background Solid(PHONE_PANEL)
    hover_background Solid(PHONE_PANEL_HOVER)
    insensitive_background Solid(PHONE_PANEL)
    xsize 166
    ysize 146
    padding (14, 14)

style phone_home_tile_button_text is button_text:
    color PHONE_TEXT
    hover_color PHONE_ACCENT
    size 22
    font gui.interface_text_font
    text_align 0.5

style phone_card_button is button:
    background Solid(PHONE_PANEL)
    hover_background Solid(PHONE_PANEL_HOVER)
    insensitive_background Solid(PHONE_PANEL)
    xfill True
    padding (16, 14)

style phone_card_button_text is button_text:
    color PHONE_TEXT
    hover_color PHONE_ACCENT
    size 20
    font gui.interface_text_font

style phone_card_title is default:
    color PHONE_TEXT
    size 22
    font gui.interface_text_font

style phone_card_meta is default:
    color PHONE_MUTED
    size 16
    font gui.interface_text_font

style phone_card_body is default:
    color PHONE_TEXT
    size 19
    font gui.interface_text_font
    line_spacing 4

style phone_badge_text is default:
    color "#fff6ea"
    size 16
    bold True
    font gui.interface_text_font

screen phone_home(initial_tab="home", focus_character_id=None, back_action=ShowMenu("main_menu"), back_label=_("Back")):
    tag menu

    on "show" action Function(phone_ensure_state)
    on "show" action Function(phone_refresh_all_if_needed)

    default active_tab = (initial_tab if initial_tab else "home")
    default selected_thread_id = None
    default selected_mail_id = None
    default selected_status_id = (focus_character_id if focus_character_id and phone_character_status_visible(focus_character_id) else None)

    $ title_map = {
        "home": _("Phone"),
        "messages": _("Messages"),
        "mail": _("Mail"),
        "social": _("Social"),
        "contacts": _("Contacts"),
        "status": _("Status"),
    }
    $ subtitle_map = {
        "home": _("Optional story fragments and public status."),
        "messages": _("Private threads and route-sensitive replies."),
        "mail": _("Official notices and direct follow-ups."),
        "social": _("Public posts, comments, and reactions."),
        "contacts": _("Unlocked character contacts."),
        "status": _("Visible notes, work status, and keepsakes."),
    }
    $ shell_title = title_map.get(active_tab, _("Phone"))
    $ shell_subtitle = subtitle_map.get(active_tab, "")
    $ return_home_action = [
        SetScreenVariable("active_tab", "home"),
        SetScreenVariable("selected_thread_id", None),
        SetScreenVariable("selected_mail_id", None),
        SetScreenVariable("selected_status_id", None),
    ]

    add (mm_theme_asset("background_full.png") if mm_loadable(mm_theme_asset("background_full.png")) else Solid("#15120f")) fit "cover"
    add Solid("#0000009a")

    fixed:
        xysize (1920, 1080)

        frame:
            xalign 0.5
            yalign 0.5
            xsize 432
            ysize 768
            background ui_frame_or_solid("gui/library/panel.png", PHONE_BG, 28)
            padding (18, 14)

            frame:
                xfill True
                yfill True
                background Solid(PHONE_SHELL)
                padding (16, 14)

                vbox:
                    spacing 12
                    xfill True
                    yfill True

                    hbox:
                        xfill True

                        text phone_status_bar_time():
                            style "phone_status_text"

                        null xfill True

                        text "▂▃▅  Wi-Fi  85%":
                            style "phone_status_text"
                            color PHONE_MUTED

                    frame:
                        xfill True
                        background Solid("#00000000")
                        padding (0, 4)

                        fixed:
                            xfill True
                            ysize 102

                            if active_tab != "home":
                                textbutton _("‹"):
                                    xpos 0
                                    ypos 8
                                    style "phone_nav_button"
                                    text_style "phone_nav_button_text"
                                    action return_home_action

                            vbox:
                                xalign 0.5
                                spacing 6

                                text shell_title:
                                    xalign 0.5
                                    style "phone_title_text"

                                text "──────── ✦ ────────":
                                    xalign 0.5
                                    style "phone_subtitle_text"
                                    color PHONE_ACCENT

                                text shell_subtitle:
                                    xalign 0.5
                                    style "phone_subtitle_text"
                                    text_align 0.5

                    frame:
                        xfill True
                        ysize 560
                        background Solid("#00000000")
                        padding (0, 0)

                        if active_tab == "home":
                            use phone_app_home(back_action=back_action, back_label=back_label)
                        elif active_tab == "messages":
                            use phone_messages_tab(selected_thread_id)
                        elif active_tab == "mail":
                            use phone_mail_tab(selected_mail_id)
                        elif active_tab == "social":
                            use phone_social_tab()
                        elif active_tab == "contacts":
                            use phone_contacts_tab()
                        else:
                            use phone_status_tab(selected_status_id)

                    if active_tab == "home":
                        vbox:
                            spacing 10
                            xfill True

                            textbutton back_label:
                                style "phone_nav_button"
                                text_style "phone_nav_button_text"
                                xfill True
                                action back_action

                    else:
                        hbox:
                            xfill True
                            spacing 10

                            textbutton _("Home"):
                                style "phone_nav_button"
                                text_style "phone_nav_button_text"
                                xfill True
                                action return_home_action

                            if active_tab == "messages":
                                textbutton _("Threads"):
                                    style "phone_nav_button"
                                    text_style "phone_nav_button_text"
                                    xfill True
                                    action SetScreenVariable("selected_thread_id", None)
                                    sensitive (selected_thread_id is not None)
                            elif active_tab == "mail":
                                textbutton _("Inbox"):
                                    style "phone_nav_button"
                                    text_style "phone_nav_button_text"
                                    xfill True
                                    action SetScreenVariable("selected_mail_id", None)
                                    sensitive (selected_mail_id is not None)
                            elif active_tab == "status":
                                textbutton _("Profiles"):
                                    style "phone_nav_button"
                                    text_style "phone_nav_button_text"
                                    xfill True
                                    action SetScreenVariable("selected_status_id", None)
                                    sensitive (selected_status_id is not None)
                            else:
                                null width 1

screen phone_app_home(back_action, back_label):
    $ unread_threads = len(phone_state.get("unread_threads", []))
    $ unread_mail = max(0, len(phone_state.get("unlocked_mails", [])) - len(phone_state.get("read_mails", [])))
    $ unread_posts = max(0, len(phone_state.get("unlocked_posts", [])) - len(phone_state.get("read_posts", [])))

    vbox:
        spacing 16
        xalign 0.5

        hbox:
            spacing 16
            xalign 0.5
            use phone_home_tile(_("Messages"), "✉", unread_threads, [SetScreenVariable("active_tab", "messages"), SetScreenVariable("selected_thread_id", None)])
            use phone_home_tile(_("Mail"), "✦", unread_mail, [SetScreenVariable("active_tab", "mail"), SetScreenVariable("selected_mail_id", None)])

        hbox:
            spacing 16
            xalign 0.5
            use phone_home_tile(_("Social"), "◎", unread_posts, SetScreenVariable("active_tab", "social"))
            use phone_home_tile(_("Contacts"), "☏", 0, SetScreenVariable("active_tab", "contacts"))

        hbox:
            spacing 16
            xalign 0.5
            use phone_home_tile(_("Status"), "✧", 0, [SetScreenVariable("active_tab", "status"), SetScreenVariable("selected_status_id", None)])
            null width 166

        frame:
            xfill True
            background Solid(PHONE_PANEL)
            padding (14, 12)

            text _("Unread threads: [unread_threads]  •  New mail: [unread_mail]  •  New posts: [unread_posts]"):
                style "phone_card_meta"
                text_align 0.5
                xalign 0.5

screen phone_home_tile(label, icon_text, badge_count, action):
    button:
        style "phone_home_tile_button"
        action action

        fixed:
            xfill True
            yfill True

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 12

                text icon_text:
                    xalign 0.5
                    color PHONE_ACCENT
                    size 42

                text label:
                    xalign 0.5
                    style "phone_home_tile_button_text"

            if badge_count:
                frame:
                    xpos 126
                    ypos 8
                    xminimum 30
                    yminimum 30
                    background Solid(PHONE_UNREAD)
                    padding (8, 4)

                    text str(badge_count):
                        xalign 0.5
                        yalign 0.5
                        style "phone_badge_text"
