screen phone_messages_tab(selected_thread_id=None):
    $ compact = ui_is_compact()
    if selected_thread_id is None:
        $ sorted_thread_ids = phone_get_sorted_thread_ids()

        viewport:
            yfill True
            mousewheel True
            draggable True
            scrollbars "vertical"

            vbox:
                spacing 10

                if not sorted_thread_ids:
                    text _("No conversations unlocked yet.") style ("phone_compact_card_body" if compact else "phone_card_body")

                for thread_id in sorted_thread_ids:
                    $ thread = PHONE_THREADS.get(thread_id, {})
                    $ title = thread.get("title", thread_id)
                    $ unread = thread_id in phone_state.get("unread_threads", [])
                    $ last_message = thread.get("messages", [])[-1] if thread.get("messages") else {}
                    $ preview = last_message.get("text", _("No messages yet."))

                    button:
                        style ("phone_compact_card_button" if compact else "phone_card_button")
                        ysize (174 if compact else 126)
                        action [SetScreenVariable("selected_thread_id", thread_id), Function(phone_mark_thread_read, thread_id)]

                        fixed:
                            xfill True
                            ysize (146 if compact else 98)

                            frame:
                                pos (0, 8)
                                xysize (52, 52)
                                padding (0, 0)
                                background ui_panel(PHONE_PANEL_ALT)
                                text title[:1]:
                                    align (0.5, 0.5)
                                    size (40 if compact else 26)
                                    color PHONE_ACCENT

                            text (title[:24] + "…" if len(title) > 24 else title):
                                pos (92 if compact else 68, 0)
                                style ("phone_compact_card_title" if compact else "phone_card_title")
                                color (PHONE_ACCENT if unread else PHONE_TEXT)
                                xmaximum (1250 if compact else 300)

                            text last_message.get("time", ""):
                                xpos (1640 if compact else 470)
                                xanchor 1.0
                                style ("phone_compact_card_meta" if compact else "phone_card_meta")

                            text ((preview[:100] + "…" if len(preview) > 100 else preview) if compact else (preview[:62] + "…" if len(preview) > 62 else preview)):
                                pos (92 if compact else 68, 68 if compact else 34)
                                style ("phone_compact_card_body" if compact else "phone_card_body")
                                size (40 if compact else 22)
                                color PHONE_MUTED
                                xmaximum (1480 if compact else 398)
                                ymaximum (64 if compact else 56)

                            if unread:
                                text "•":
                                    pos (18, 66)
                                    size (40 if compact else 24)
                                    color PHONE_ACCENT

    else:
        use phone_thread_view(selected_thread_id)


screen phone_thread_view(thread_id):
    $ compact = ui_is_compact()
    $ thread = PHONE_THREADS.get(thread_id, {})
    $ reply_data = PHONE_REPLY_CHOICES.get(thread_id, []) if "PHONE_REPLY_CHOICES" in globals() else []
    $ pending_replies = [reply for reply in reply_data if not phone_reply_was_sent(thread_id, reply.get("id"))]

    vbox:
        spacing 16
        xfill True

        viewport:
            ysize ((352 if pending_replies else 650) if compact else (350 if pending_replies else 650))
            xfill True
            yinitial 1.0
            mousewheel True
            draggable True
            scrollbars "vertical"

            vbox:
                xfill True
                spacing 18

                for message in thread.get("messages", []):
                    use phone_message_bubble(message)

        if pending_replies:
            viewport:
                ysize (282 if compact else 284)
                mousewheel True
                draggable True
                scrollbars "vertical"
                frame:
                    xfill True
                    background ui_panel(PHONE_BG, PHONE_BORDER, radius=22)
                    padding (14, 12)

                    vbox:
                        spacing 8

                        add GoldDivider() xsize (1640 if compact else 490)

                        text _("Reply once"):
                            style ("phone_compact_card_meta" if compact else "phone_card_meta")
                            color PHONE_ACCENT
                            size (40 if compact else 24)
                            xalign 0.5

                        for reply in pending_replies:
                            button:
                                style ("phone_compact_nav_button" if compact else "phone_nav_button")
                                xfill True
                                yminimum 112
                                alt reply.get("text", "...")
                                action Function(phone_send_reply, thread_id, reply.get("id"))
                                hbox:
                                    spacing 24
                                    xfill True
                                    text reply.get("text", "..."):
                                        style ("phone_compact_nav_button_text" if compact else "phone_nav_button_text")
                                        xmaximum (1500 if compact else 460)
                                        yalign 0.5
                                    if compact:
                                        null xfill True
                                        add Transform(ui_icon("back", medallion=False), xzoom=-1) xysize (72, 72) yalign 0.5


screen phone_message_bubble(message):
    $ compact = ui_is_compact()
    $ sender = message.get("sender", "")
    $ sender_label = _("You") if sender == "player" else phone_get_contact_display_name(sender)
    $ text_value = message.get("text", "")
    $ time_value = message.get("time", "")

    vbox:
        xfill True
        spacing 5

        frame:
            xalign (1.0 if sender == "player" else 0.0)
            xmaximum (1320 if compact else 480)
            background ui_panel(PHONE_PANEL if sender != "player" else PHONE_PANEL_ALT, "#c39860cc", radius=16)
            padding (16, 14)

            vbox:
                spacing 6

                text text_value:
                    style ("phone_compact_card_body" if compact else "phone_card_body")
                    xmaximum (1288 if compact else 448)

        if time_value:
            text (renpy.translate_string(sender_label) + "  ·  " + time_value):
                style ("phone_compact_card_meta" if compact else "phone_card_meta")
                xalign (1.0 if sender == "player" else 0.0)


screen phone_mail_tab(selected_mail_id=None):
    $ compact = ui_is_compact()
    if selected_mail_id is None:
        $ sorted_mail_ids = phone_get_sorted_mail_ids()

        viewport:
            yfill True
            mousewheel True
            draggable True
            scrollbars "vertical"

            vbox:
                spacing 10

                if not sorted_mail_ids:
                    text _("No mail unlocked yet.") style ("phone_compact_card_body" if compact else "phone_card_body")

                for mail_id in sorted_mail_ids:
                    $ mail = PHONE_MAILS.get(mail_id, {})
                    $ unread = mail_id not in phone_state.get("read_mails", [])

                    button:
                        style ("phone_compact_card_button" if compact else "phone_card_button")
                        action [SetScreenVariable("selected_mail_id", mail_id), Function(phone_mark_mail_read, mail_id)]

                        vbox:
                            spacing 6
                            xfill True

                            hbox:
                                xfill True

                                text mail.get("subject", mail_id):
                                    style ("phone_compact_card_title" if compact else "phone_card_title")
                                    color (PHONE_ACCENT if unread else PHONE_TEXT)

                                null xfill True

                                if unread:
                                    text _("new"):
                                        style ("phone_compact_card_meta" if compact else "phone_card_meta")
                                        color PHONE_UNREAD

                            text (mail.get("from", "") + "  •  " + mail.get("preview", "")):
                                style ("phone_compact_card_meta" if compact else "phone_card_meta")

    else:
        use phone_mail_view(selected_mail_id)


screen phone_mail_view(mail_id):
    $ compact = ui_is_compact()
    $ mail = PHONE_MAILS.get(mail_id, {})

    viewport:
        yfill True
        mousewheel True
        draggable True
        scrollbars "vertical"

        frame:
            xfill True
            background Solid(PHONE_PANEL)
            padding (16, 14)

            vbox:
                spacing 10

                text mail.get("subject", mail_id):
                    style ("phone_compact_card_title" if compact else "phone_card_title")
                    size (40 if compact else 26)
                text ("From: " + mail.get("from", "")):
                    style ("phone_compact_card_meta" if compact else "phone_card_meta")
                    color PHONE_ACCENT

                text mail.get("body", ""):
                    style ("phone_compact_card_body" if compact else "phone_card_body")


screen phone_social_tab():
    $ compact = ui_is_compact()
    $ sorted_post_ids = phone_get_sorted_post_ids()

    viewport:
        yfill True
        mousewheel True
        draggable True
        scrollbars "vertical"

        vbox:
            spacing 10

            if not sorted_post_ids:
                text _("No public posts yet.") style ("phone_compact_card_body" if compact else "phone_card_body")

            for post_id in sorted_post_ids:
                $ post = PHONE_SOCIAL_POSTS.get(post_id, {})
                $ author_id = post.get("author", "")
                $ is_read = post_id in phone_state.get("read_posts", [])
                $ liked = post_id in phone_state.get("liked_posts", [])

                frame:
                    xfill True
                    background Solid(PHONE_PANEL)
                    padding (16, 14)

                    vbox:
                        spacing 8

                        hbox:
                            xfill True

                            text phone_get_contact_display_name(author_id):
                                style ("phone_compact_card_title" if compact else "phone_card_title")

                            null xfill True

                            if not is_read:
                                text _("new"):
                                    style ("phone_compact_card_meta" if compact else "phone_card_meta")
                                    color PHONE_UNREAD

                        text post.get("content", ""):
                            style ("phone_compact_card_body" if compact else "phone_card_body")

                        if post.get("comments"):
                            frame:
                                xfill True
                                background Solid(PHONE_PANEL_ALT)
                                padding (12, 10)

                                vbox:
                                    spacing 6

                                    for comment in post.get("comments", []):
                                        $ comment_author = phone_get_contact_display_name(comment.get("author", ""))
                                        text (comment_author + ": " + comment.get("text", "")):
                                            style ("phone_compact_card_meta" if compact else "phone_card_meta")

                        hbox:
                            spacing 10

                            textbutton (_("Read") if not is_read else _("Viewed")):
                                style ("phone_compact_nav_button" if compact else "phone_nav_button")
                                text_style ("phone_compact_nav_button_text" if compact else "phone_nav_button_text")
                                action Function(phone_mark_post_read, post_id)
                                sensitive (not is_read)

                            textbutton (_("Like") if not liked else _("Liked")):
                                style ("phone_compact_nav_button" if compact else "phone_nav_button")
                                text_style ("phone_compact_nav_button_text" if compact else "phone_nav_button_text")
                                action Function(phone_like_post, post_id)
                                sensitive (not liked)


screen phone_contacts_tab():
    $ compact = ui_is_compact()
    $ sorted_contact_ids = phone_get_sorted_contact_ids()

    viewport:
        yfill True
        mousewheel True
        draggable True
        scrollbars "vertical"

        vbox:
            spacing 10

            if not sorted_contact_ids:
                text _("No contacts unlocked yet.") style ("phone_compact_card_body" if compact else "phone_card_body")

            for contact_id in sorted_contact_ids:
                $ contact = PHONE_CONTACTS.get(contact_id, {})
                $ profile = phone_find_profile(contact_id)

                frame:
                    xfill True
                    background Solid(PHONE_PANEL)
                    padding (16, 14)

                    hbox:
                        spacing 12
                        xfill True

                        frame:
                            xsize 54
                            ysize 54
                            background Solid(PHONE_PANEL_ALT)
                            padding (0, 0)

                            text phone_get_contact_display_name(contact_id)[:1]:
                                xalign 0.5
                                yalign 0.5
                                size (40 if compact else 28)
                                color PHONE_ACCENT

                        vbox:
                            spacing 4
                            xfill True

                            text phone_get_contact_display_name(contact_id):
                                style ("phone_compact_card_title" if compact else "phone_card_title")

                            text phone_get_contact_status(contact_id):
                                style ("phone_compact_card_meta" if compact else "phone_card_meta")
                                color PHONE_ACCENT

                            if profile:
                                text profile.get("description", ""):
                                    style ("phone_compact_card_meta" if compact else "phone_card_meta")

                            if contact.get("tags"):
                                text ", ".join(contact.get("tags", [])):
                                    style ("phone_compact_card_meta" if compact else "phone_card_meta")


screen phone_status_tab(selected_status_id=None):
    $ compact = ui_is_compact()
    if selected_status_id is None:
        $ visible_status_ids = phone_get_visible_status_ids()

        viewport:
            yfill True
            mousewheel True
            draggable True
            scrollbars "vertical"

            vbox:
                spacing 10

                # ── Financial summary ──────────────────────────────────
                $ fin = time_get_financial_summary()
                $ money_str = activity_format_money(fin["money"])
                frame:
                    xfill True
                    background Solid(PHONE_PANEL)
                    padding (16, 12)

                    vbox:
                        spacing 6

                        text _("Finance"):
                            style ("phone_compact_card_title" if compact else "phone_card_title")
                            color PHONE_ACCENT

                        # Money balance
                        text "[money_str]":
                            style ("phone_compact_card_title" if compact else "phone_card_title")
                            size (40 if compact else 26)
                        null height 4

                        # Employment & salary line
                        if fin["is_employed"]:
                            $ salary_str = activity_format_money(fin["monthly_salary"])
                            hbox:
                                xfill True
                                text _("Monthly Salary:") style ("phone_compact_card_meta" if compact else "phone_card_meta")
                                text "[salary_str]/mo":
                                    style ("phone_compact_card_meta" if compact else "phone_card_meta")
                                    color PHONE_ACCENT
                                    xalign 1.0
                        else:
                            text _("Status: Unemployed") style ("phone_compact_card_meta" if compact else "phone_card_meta")

                        # Paycheck progress
                        if fin["is_employed"]:
                            $ progress = fin["next_salary_progress"]
                            $ pct = int(float(progress) / 30.0 * 100.0)
                            $ attend_str = str(fin["work_attendance_this_month"])
                            $ absent_str = str(fin["work_absence_this_month"])
                            hbox:
                                xfill True
                                text _("Paycheck in [progress]/30 days") style ("phone_compact_card_meta" if compact else "phone_card_meta")
                                text "[pct]%":
                                    style ("phone_compact_card_meta" if compact else "phone_card_meta")
                                    color PHONE_ACCENT
                                    xalign 1.0

                            text _("Attendance this month: [attend_str] work · [absent_str] absences"):
                                style ("phone_compact_card_meta" if compact else "phone_card_meta")

                        null height 4

                        # Pending bills warning
                        if fin["pending_bills_total"] > 0:
                            $ bills_total_str = activity_format_money(fin["pending_bills_total"])
                            text _("Pending bills: [bills_total_str]"):
                                style ("phone_compact_card_meta" if compact else "phone_card_meta")
                                color PHONE_UNREAD

                            for bill in fin["pending_bills"]:
                                $ bill_label = bill.get("label", "")
                                $ bill_amount_str = activity_format_money(bill.get("amount", 0))
                                hbox:
                                    xfill True
                                    text "[bill_label]" style ("phone_compact_card_meta" if compact else "phone_card_meta")
                                    text "[bill_amount_str]":
                                        style ("phone_compact_card_meta" if compact else "phone_card_meta")
                                        xalign 1.0
                        elif fin["is_employed"]:
                            text _("No pending bills") style ("phone_compact_card_meta" if compact else "phone_card_meta")

                        if fin["unpaid_bill_months"] > 0:
                            $ overdue_str = str(fin["unpaid_bill_months"])
                            text _("⚠ Overdue: [overdue_str] month(s) unpaid"):
                                style ("phone_compact_card_meta" if compact else "phone_card_meta")
                                color PHONE_UNREAD

                        # Last paycheck
                        $ last_pay = fin["last_salary"]
                        if last_pay:
                            $ last_amount_str = activity_format_money(last_pay.get("amount", 0))
                            $ last_day_str = str(last_pay.get("day", ""))
                            null height 4
                            text _("Last Paycheck: +[last_amount_str] (Day [last_day_str])"):
                                style ("phone_compact_card_meta" if compact else "phone_card_meta")

                null height 4

                # ── Character status entries ───────────────────────────
                if not visible_status_ids:
                    text _("No public status entries yet.") style ("phone_compact_card_body" if compact else "phone_card_body")

                for character_id in visible_status_ids:
                    $ data = phone_status_display(character_id)

                    button:
                        style ("phone_compact_card_button" if compact else "phone_card_button")
                        action SetScreenVariable("selected_status_id", character_id)

                        vbox:
                            spacing 6

                            text data.get("name", character_id):
                                style ("phone_compact_card_title" if compact else "phone_card_title")

                            if data.get("public_title"):
                                text data.get("public_title", ""):
                                    style ("phone_compact_card_meta" if compact else "phone_card_meta")
                                    color PHONE_ACCENT

                            if data.get("notes"):
                                text data.get("notes", [""])[0]:
                                    style ("phone_compact_card_meta" if compact else "phone_card_meta")

    else:
        use phone_status_detail(selected_status_id)


screen phone_status_detail(character_id):
    $ compact = ui_is_compact()
    $ data = phone_status_display(character_id)

    viewport:
        yfill True
        mousewheel True
        draggable True
        scrollbars "vertical"

        vbox:
            spacing 10

            frame:
                xfill True
                background Solid(PHONE_PANEL)
                padding (16, 14)

                vbox:
                    spacing 8

                    text data.get("name", character_id):
                        style ("phone_compact_card_title" if compact else "phone_card_title")
                        size (40 if compact else 28)
                    if data.get("public_title"):
                        text data.get("public_title", ""):
                            style ("phone_compact_card_meta" if compact else "phone_card_meta")
                            color PHONE_ACCENT

                    if data.get("subtitle"):
                        text data.get("subtitle", ""):
                            style ("phone_compact_card_meta" if compact else "phone_card_meta")

            frame:
                xfill True
                background Solid(PHONE_PANEL)
                padding (16, 14)

                vbox:
                    spacing 6

                    text _("Contact Note"):
                        style ("phone_compact_card_meta" if compact else "phone_card_meta")
                        color PHONE_ACCENT

                    text data.get("contact_status", ""):
                        style ("phone_compact_card_body" if compact else "phone_card_body")

            if data.get("income_monthly") is not None or data.get("job_level"):
                frame:
                    xfill True
                    background Solid(PHONE_PANEL)
                    padding (16, 14)

                    vbox:
                        spacing 6

                        text _("Public Status"):
                            style ("phone_compact_card_meta" if compact else "phone_card_meta")
                            color PHONE_ACCENT

                        if data.get("job_level"):
                            text ("Job level: " + str(data.get("job_level", 0))):
                                style ("phone_compact_card_body" if compact else "phone_card_body")

                        if data.get("income_monthly") is not None:
                            text phone_format_currency(data.get("income_monthly")):
                                style ("phone_compact_card_body" if compact else "phone_card_body")

            if data.get("notes"):
                frame:
                    xfill True
                    background Solid(PHONE_PANEL)
                    padding (16, 14)

                    vbox:
                        spacing 6

                        text _("Known Notes"):
                            style ("phone_compact_card_meta" if compact else "phone_card_meta")
                            color PHONE_ACCENT

                        for note in data.get("notes", []):
                            text ("- " + note):
                                style ("phone_compact_card_body" if compact else "phone_card_body")

            if data.get("inventory"):
                frame:
                    xfill True
                    background Solid(PHONE_PANEL)
                    padding (16, 14)

                    vbox:
                        spacing 6

                        text _("Inventory"):
                            style ("phone_compact_card_meta" if compact else "phone_card_meta")
                            color PHONE_ACCENT

                        for item_id in data.get("inventory", []):
                            $ item = phone_get_item(item_id)
                            text item.get("name", item_id):
                                style ("phone_compact_card_body" if compact else "phone_card_body")
                            text item.get("description", ""):
                                style ("phone_compact_card_meta" if compact else "phone_card_meta")
