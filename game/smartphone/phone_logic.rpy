init python:
    PHONE_CHARACTER_IDS = ["tam", "hoang", "huyen", "minh", "yuuka", "thienan"]
    _career_promotion_guard = False

    def phone_default_state_template():
        return {
            "unlocked_contacts": [],
            "unlocked_threads": [],
            "read_threads": [],
            "unread_threads": [],
            "read_messages": [],
            "sent_replies": {},
            "unlocked_mails": [],
            "read_mails": [],
            "unlocked_posts": [],
            "read_posts": [],
            "liked_posts": [],
            "notification_log": [],
        }

    def phone_default_character_status_template():
        return {
            "job_title": None,
            "job_level": 0,
            "salary": None,
            "income_monthly": None,
            "inventory": [],
            "known_info": [],
            "public_stats": {},
        }

    def phone_ensure_state():
        global phone_state
        global character_status

        if phone_state is None or not isinstance(phone_state, dict):
            phone_state = {}

        for key, value in phone_default_state_template().items():
            if isinstance(value, list):
                phone_state.setdefault(key, [])
            elif isinstance(value, dict):
                phone_state.setdefault(key, {})
            else:
                phone_state.setdefault(key, value)

        if character_status is None or not isinstance(character_status, dict):
            character_status = {}

        for character_id in PHONE_CHARACTER_IDS:
            character_status.setdefault(character_id, phone_default_character_status_template().copy())

    def phone_list_get(key):
        phone_ensure_state()
        return phone_state.setdefault(key, [])

    def phone_dict_get(key):
        phone_ensure_state()
        return phone_state.setdefault(key, {})

    def phone_find_profile(character_id):
        for profile in globals().get("CHARACTER_PROFILES", []):
            if profile.get("id") == character_id:
                return profile
        return None

    def phone_contact_data(contact_id):
        return globals().get("PHONE_CONTACTS", {}).get(contact_id, {})

    def phone_get_contact_display_name(contact_id):
        contact = phone_contact_data(contact_id)
        if contact.get("display_name"):
            return contact.get("display_name")
        profile = phone_find_profile(contact_id)
        if profile and profile.get("name"):
            return profile.get("name")
        return contact_id.replace("_", " ").title()

    def phone_get_contact_status(contact_id):
        contact = phone_contact_data(contact_id)
        return contact.get("default_status", "Available")

    def phone_has_completed(chapter_id):
        if callable(globals().get("story_chapter_done", None)):
            if story_chapter_done(chapter_id):
                return True
        try:
            return chapter_id in story_completed_chapters
        except Exception:
            pass

        progress = globals().get("progress", None)
        if isinstance(progress, dict):
            return chapter_id in progress.get("completed", [])
        return False

    def phone_has_flag(flag_name):
        try:
            if story_has_flag(flag_name):
                return True
        except Exception:
            pass

        try:
            if flag_name in story_flags:
                return True
        except Exception:
            pass

        progress = globals().get("progress", None)
        if isinstance(progress, dict):
            if flag_name in progress.get("player_flags", []):
                return True
            for flags in progress.get("character_flags", {}).values():
                if flag_name in flags:
                    return True

        return False

    def phone_has_direction(character_id, direction):
        return phone_has_flag("direction_%s_%s" % (character_id, direction))

    def phone_get_score(score_key):
        try:
            return story_state.get(score_key, 0)
        except Exception:
            return 0

    def phone_eval_condition(condition):
        if not condition:
            return True

        parts = condition.split(":")

        if parts[0] == "completed" and len(parts) == 2:
            return phone_has_completed(parts[1])
        if parts[0] == "flag" and len(parts) == 2:
            return phone_has_flag(parts[1])
        if parts[0] == "not_flag" and len(parts) == 2:
            return not phone_has_flag(parts[1])
        if parts[0] == "contact" and len(parts) == 2:
            return phone_has_contact(parts[1])
        if parts[0] == "thread_read" and len(parts) == 2:
            return parts[1] in phone_state.get("read_threads", [])
        if parts[0] == "mail_read" and len(parts) == 2:
            return parts[1] in phone_state.get("read_mails", [])
        if parts[0] == "post_read" and len(parts) == 2:
            return parts[1] in phone_state.get("read_posts", [])
        if parts[0] == "direction" and len(parts) == 3:
            return phone_has_direction(parts[1], parts[2])
        if parts[0] == "score_gte" and len(parts) == 3:
            return phone_get_score(parts[1]) >= int(parts[2])
        if parts[0] == "score_lte" and len(parts) == 3:
            return phone_get_score(parts[1]) <= int(parts[2])

        return False

    def phone_conditions_met(conditions):
        if not conditions:
            return True
        return all(phone_eval_condition(condition) for condition in conditions)

    def phone_add_notification(kind, entry_id):
        phone_ensure_state()
        entry = "%s:%s" % (kind, entry_id)
        log = phone_list_get("notification_log")
        if entry not in log:
            log.append(entry)

    def phone_unlock_contact(contact_id):
        if contact_id not in globals().get("PHONE_CONTACTS", {}):
            return False

        contacts = phone_list_get("unlocked_contacts")
        if contact_id not in contacts:
            contacts.append(contact_id)
            phone_add_notification("contact", contact_id)
        return True

    def phone_has_contact(contact_id):
        return contact_id in phone_state.get("unlocked_contacts", [])

    def phone_refresh_contacts():
        for contact_id, data in globals().get("PHONE_CONTACTS", {}).items():
            if phone_conditions_met(data.get("unlock_conditions", [])):
                phone_unlock_contact(contact_id)

    def phone_unlock_thread(thread_id, mark_unread=True):
        if thread_id not in globals().get("PHONE_THREADS", {}):
            return False

        unlocked = phone_list_get("unlocked_threads")
        unread = phone_list_get("unread_threads")

        if thread_id not in unlocked:
            unlocked.append(thread_id)
            phone_add_notification("thread", thread_id)

        if mark_unread and thread_id not in phone_state.get("read_threads", []):
            if thread_id not in unread:
                unread.append(thread_id)

        return True

    def phone_mark_thread_read(thread_id):
        unread = phone_list_get("unread_threads")
        read = phone_list_get("read_threads")
        first_read = thread_id not in read

        if thread_id in unread:
            unread.remove(thread_id)
        if first_read:
            read.append(thread_id)

        data = globals().get("PHONE_THREADS", {}).get(thread_id)
        if first_read and data:
            phone_apply_effects(data.get("effects_on_read", {}))

    def phone_refresh_threads():
        for thread_id, data in globals().get("PHONE_THREADS", {}).items():
            if phone_conditions_met(data.get("unlock_conditions", [])):
                phone_unlock_thread(thread_id)

    def phone_unlock_mail(mail_id, mark_unread=True):
        if mail_id not in globals().get("PHONE_MAILS", {}):
            return False

        unlocked = phone_list_get("unlocked_mails")
        if mail_id not in unlocked:
            unlocked.append(mail_id)
            phone_add_notification("mail", mail_id)
        return True

    def phone_mark_mail_read(mail_id):
        read = phone_list_get("read_mails")
        first_read = mail_id not in read
        if first_read:
            read.append(mail_id)

        data = globals().get("PHONE_MAILS", {}).get(mail_id)
        if first_read and data:
            phone_apply_effects(data.get("effects_on_read", {}))

    def phone_refresh_mails():
        for mail_id, data in globals().get("PHONE_MAILS", {}).items():
            if phone_conditions_met(data.get("unlock_conditions", [])):
                phone_unlock_mail(mail_id)

    def phone_unlock_post(post_id):
        if post_id not in globals().get("PHONE_SOCIAL_POSTS", {}):
            return False

        unlocked = phone_list_get("unlocked_posts")
        if post_id not in unlocked:
            unlocked.append(post_id)
            phone_add_notification("post", post_id)
        return True

    def phone_mark_post_read(post_id):
        read = phone_list_get("read_posts")
        first_read = post_id not in read
        if first_read:
            read.append(post_id)

        data = globals().get("PHONE_SOCIAL_POSTS", {}).get(post_id)
        if first_read and data:
            phone_apply_effects(data.get("effects_on_read", {}))

    def phone_like_post(post_id):
        liked = phone_list_get("liked_posts")
        if post_id not in liked:
            liked.append(post_id)
            data = globals().get("PHONE_SOCIAL_POSTS", {}).get(post_id)
            if data:
                phone_apply_effects(data.get("effects_on_like", {}))

    def phone_refresh_posts():
        for post_id, data in globals().get("PHONE_SOCIAL_POSTS", {}).items():
            if phone_conditions_met(data.get("unlock_conditions", [])):
                phone_unlock_post(post_id)

    def phone_refresh_all():
        phone_ensure_state()
        phone_refresh_contacts()
        phone_refresh_threads()
        phone_refresh_mails()
        phone_refresh_posts()

    def phone_get_character_status(character_id):
        global character_status

        if character_status is None or not isinstance(character_status, dict):
            character_status = {}

        return character_status.setdefault(character_id, phone_default_character_status_template().copy())

    def phone_update_character_status(character_id, **kwargs):
        status = phone_get_character_status(character_id)
        for key, value in kwargs.items():
            if key == "public_stats":
                status.setdefault("public_stats", {}).update(value)
            elif key == "known_info":
                for note in value:
                    char_add_known_info(character_id, note)
            elif key == "inventory":
                for item_id in value:
                    char_add_item(character_id, item_id)
            else:
                status[key] = value

    def career_get_track(character_id):
        return globals().get("CHARACTER_CAREER_TRACKS", {}).get(character_id)

    def career_get_score_key(character_id):
        track = career_get_track(character_id)
        if not track:
            return None
        return track.get("score_key")

    def career_get_character_for_score(score_key):
        return globals().get("CAREER_SCORE_TO_CHARACTER", {}).get(score_key)

    def career_get_level_data(character_id, level):
        track = career_get_track(character_id)
        if not track:
            return None
        for level_data in track.get("levels", []):
            if int(level_data.get("level", 0)) == int(level or 0):
                return level_data
        return None

    def career_get_salary_for_level(character_id, level_data):
        if not level_data:
            return None

        salary_amount = int(level_data.get("salary", 0) or 0)
        track = career_get_track(character_id) or {}
        for flag_name, salary_overrides in track.get("salary_flag_overrides", {}).items():
            if story_has_flag(flag_name):
                salary_amount = int(salary_overrides.get(level_data.get("level"), salary_amount) or salary_amount)
        return salary_amount

    def career_sync_level_status(character_id, level=None, known_info=None):
        status = phone_get_character_status(character_id)
        target_level = int(level if level is not None else status.get("job_level", 0) or 0)
        if target_level <= 0:
            return None

        level_data = career_get_level_data(character_id, target_level)
        if not level_data:
            return None

        salary_amount = career_get_salary_for_level(character_id, level_data)
        status_patch = {
            "job_title": level_data.get("title"),
            "job_level": target_level,
            "income_monthly": salary_amount,
        }
        if known_info:
            status_patch["known_info"] = known_info
        phone_update_character_status(character_id, **status_patch)

        track = career_get_track(character_id) or {}
        if track.get("sync_activity_salary"):
            activity_state = ensure_activity_state()
            activity_state["monthly_salary"] = salary_amount

        return level_data

    def career_assign_level(character_id, level, known_info=None):
        status = phone_get_character_status(character_id)
        current_level = int(status.get("job_level", 0) or 0)
        target_level = max(current_level, int(level or 0))
        level_data = career_sync_level_status(character_id, level=target_level, known_info=known_info)
        career_check_character_promotion(character_id)
        return level_data

    def career_requirements_met(level_data):
        if not level_data:
            return False

        for flag_name in level_data.get("required_flags", []):
            if not phone_has_flag(flag_name):
                return False

        for score_key, minimum_value in level_data.get("required_scores", {}).items():
            if story_get_score(score_key) < int(minimum_value or 0):
                return False

        for score_key, maximum_value in level_data.get("required_max_scores", {}).items():
            if story_get_score(score_key) > int(maximum_value or 0):
                return False

        for chapter_id in level_data.get("required_completed_chapters", []):
            if not phone_has_completed(chapter_id):
                return False

        return True

    def career_get_pending_level(character_id):
        status = phone_get_character_status(character_id)
        current_level = int(status.get("job_level", 0) or 0)
        return career_get_level_data(character_id, current_level + 1)

    def career_consume_score(character_id):
        score_key = career_get_score_key(character_id)
        if not score_key:
            return
        story_state[score_key] = max(0, int(story_state.get(score_key, 0) or 0) - 100)

    def career_apply_promotion(character_id, level_data):
        if not level_data:
            return False

        career_consume_score(character_id)
        career_sync_level_status(
            character_id,
            level=int(level_data.get("level", 0)),
            known_info=["Promoted to %s." % level_data.get("title", "the next role")],
        )
        story_flag("career_%s_level_%s" % (character_id, level_data.get("level")))
        return True

    def career_check_character_promotion(character_id):
        track = career_get_track(character_id)
        if not track:
            return False

        status = phone_get_character_status(character_id)
        if int(status.get("job_level", 0) or 0) <= 0:
            return False

        promoted_any = False
        score_key = track.get("score_key")
        if not score_key:
            return False

        while story_get_score(score_key) >= 100:
            next_level_data = career_get_pending_level(character_id)
            if not next_level_data or not career_requirements_met(next_level_data):
                break
            if not career_apply_promotion(character_id, next_level_data):
                break
            promoted_any = True

        return promoted_any

    def career_refresh_all_statuses():
        for character_id in globals().get("CHARACTER_CAREER_TRACKS", {}).keys():
            status = phone_get_character_status(character_id)
            if int(status.get("job_level", 0) or 0) > 0:
                career_sync_level_status(character_id)

    def career_check_all_promotions():
        promoted_any = False
        for character_id in globals().get("CHARACTER_CAREER_TRACKS", {}).keys():
            if career_check_character_promotion(character_id):
                promoted_any = True
        return promoted_any

    def career_handle_story_state_change(changed_key=None):
        global _career_promotion_guard

        if _career_promotion_guard:
            return

        try:
            _career_promotion_guard = True

            if changed_key and changed_key not in globals().get("CAREER_SCORE_TO_CHARACTER", {}) and changed_key not in globals().get("STORY_SCORE_KEYS", set()):
                return

            if changed_key and changed_key in globals().get("CAREER_SCORE_TO_CHARACTER", {}):
                career_check_character_promotion(career_get_character_for_score(changed_key))
            else:
                career_check_all_promotions()
        finally:
            _career_promotion_guard = False

    def char_add_item(character_id, item_id):
        status = phone_get_character_status(character_id)
        inventory = status.setdefault("inventory", [])
        if item_id not in inventory:
            inventory.append(item_id)

    def char_add_known_info(character_id, note):
        status = phone_get_character_status(character_id)
        known_info = status.setdefault("known_info", [])
        if note not in known_info:
            known_info.append(note)

    def phone_apply_effects(effects):
        if not effects:
            return

        for flag_name in effects.get("flags", []):
            try:
                story_flag(flag_name)
            except Exception:
                if flag_name not in story_flags:
                    story_flags.append(flag_name)

        for score_key, amount in effects.get("story_add", {}).items():
            try:
                story_add(score_key, amount)
            except Exception:
                story_state[score_key] = story_state.get(score_key, 0) + amount

        for character_id, directions in effects.get("directions", {}).items():
            for direction in directions:
                try:
                    story_add_direction(character_id, direction)
                except Exception:
                    fallback_flag = "direction_%s_%s" % (character_id, direction)
                    if fallback_flag not in story_flags:
                        story_flags.append(fallback_flag)

        for character_id, status_patch in effects.get("character_status", {}).items():
            phone_update_character_status(character_id, **status_patch)

        for character_id, item_ids in effects.get("inventory_add", {}).items():
            for item_id in item_ids:
                char_add_item(character_id, item_id)

        for character_id, notes in effects.get("known_info_add", {}).items():
            for note in notes:
                char_add_known_info(character_id, note)


        for chapter_id in effects.get("chapter_unlocks", []):
            if chapter_id in CHAPTERS:
                _prog = globals().get("progress", None)
                if isinstance(_prog, dict):
                    _avail = _prog.get("available", [])
                    if chapter_id not in _avail and chapter_id not in _prog.get("completed", []):
                        _avail.append(chapter_id)
                        _recalc = globals().get("recalculate_chapter_availability", None)
                        if callable(_recalc):
                            _recalc()
                        _update = globals().get("update_recommended_next", None)
                        if callable(_update):
                            _update()

    def phone_reply_was_sent(thread_id, reply_id):
        sent_replies = phone_dict_get("sent_replies")
        return reply_id in sent_replies.get(thread_id, [])

    def phone_send_reply(thread_id, reply_id):
        reply_choices = globals().get("PHONE_REPLY_CHOICES", {}).get(thread_id, [])
        selected = None
        for reply in reply_choices:
            if reply.get("id") == reply_id:
                selected = reply
                break

        if selected is None:
            return False
        if phone_reply_was_sent(thread_id, reply_id):
            return False

        sent_replies = phone_dict_get("sent_replies")
        sent_replies.setdefault(thread_id, []).append(reply_id)

        thread = globals().get("PHONE_THREADS", {}).get(thread_id)
        if thread is None:
            return False

        player_message = {
            "id": "reply_%s" % reply_id,
            "sender": "player",
            "text": selected.get("text", "..."),
            "time": selected.get("time", "now"),
        }
        thread.setdefault("messages", []).append(player_message)

        for response in selected.get("response_messages", []):
            thread.setdefault("messages", []).append(response)

        phone_apply_effects(selected.get("effects", {}))
        phone_unlock_thread(thread_id, mark_unread=False)
        phone_mark_thread_read(thread_id)
        return True

    def phone_get_profile_title(character_id):
        profile = phone_find_profile(character_id)
        if not profile:
            return ""
        profile_data = profile.get("profile", {})
        return profile_data.get("role") or profile.get("description", "")

    def phone_character_status_visible(character_id):
        base = globals().get("CHARACTER_STATUS_BASE", {}).get(character_id)
        if not base:
            return False
        return phone_conditions_met(base.get("hidden_until", []))

    def phone_status_display(character_id):
        base = globals().get("CHARACTER_STATUS_BASE", {}).get(character_id, {})
        status = phone_get_character_status(character_id)
        profile = phone_find_profile(character_id) or {}
        profile_data = profile.get("profile", {})
        return {
            "id": character_id,
            "name": base.get("name") or phone_get_contact_display_name(character_id),
            "public_title": status.get("job_title") or base.get("public_title") or profile_data.get("role") or "",
            "subtitle": profile.get("description", ""),
            "notes": list(base.get("default_notes", [])) + list(status.get("known_info", [])),
            "inventory": list(status.get("inventory", [])),
            "income_monthly": status.get("income_monthly"),
            "job_level": status.get("job_level", 0),
            "public_stats": dict(status.get("public_stats", {})),
            "profile_id": base.get("profile_id") or character_id,
            "contact_status": phone_get_contact_status(character_id),
        }

    def phone_get_sorted_contact_ids():
        contacts = list(phone_state.get("unlocked_contacts", []))
        contacts.sort(key=lambda contact_id: phone_get_contact_display_name(contact_id).lower())
        return contacts

    def phone_get_sorted_thread_ids():
        threads = list(phone_state.get("unlocked_threads", []))
        threads.sort(key=lambda thread_id: globals().get("PHONE_THREADS", {}).get(thread_id, {}).get("sort_order", 0), reverse=True)
        return threads

    def phone_get_sorted_mail_ids():
        mails = list(phone_state.get("unlocked_mails", []))
        mails.sort(key=lambda mail_id: globals().get("PHONE_MAILS", {}).get(mail_id, {}).get("sort_order", 0), reverse=True)
        return mails

    def phone_get_sorted_post_ids():
        posts = list(phone_state.get("unlocked_posts", []))
        posts.sort(key=lambda post_id: globals().get("PHONE_SOCIAL_POSTS", {}).get(post_id, {}).get("sort_order", 0), reverse=True)
        return posts

    def phone_get_visible_status_ids():
        result = []
        for character_id in PHONE_CHARACTER_IDS:
            if phone_character_status_visible(character_id):
                result.append(character_id)
        return result

    def phone_format_currency(value):
        if value is None:
            return "Unknown"
        return "$%s / month" % value

    def phone_get_item(item_id):
        return globals().get("STORY_ITEMS", {}).get(item_id, {"name": item_id, "description": item_id})

    def phone_total_unread_count():
        return len(phone_state.get("unread_threads", []))

    def phone_status_bar_time():
        import datetime
        return datetime.datetime.now().strftime("%I:%M %p").lstrip("0")
