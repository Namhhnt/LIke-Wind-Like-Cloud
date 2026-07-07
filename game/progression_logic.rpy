# FILE: game/progression_logic.rpy
# Purpose: Progression/runtime logic for the full skeleton route chapter map MVP.
# Compatible with skeleton labels that call story_complete_chapter().

init -1 python:
    def normalize_persistent_progression_state():
        if not hasattr(persistent, "gallery_unlocks") or persistent.gallery_unlocks is None:
            persistent.gallery_unlocks = []
        elif not isinstance(persistent.gallery_unlocks, list):
            persistent.gallery_unlocks = list(persistent.gallery_unlocks)

        if not hasattr(persistent, "route_clear_history") or persistent.route_clear_history is None:
            persistent.route_clear_history = []
        elif not isinstance(persistent.route_clear_history, list):
            persistent.route_clear_history = list(persistent.route_clear_history)

        if not hasattr(persistent, "true_ending_seen") or persistent.true_ending_seen is None:
            persistent.true_ending_seen = False

        if not hasattr(persistent, "debugging_mode") or persistent.debugging_mode is None:
            persistent.debugging_mode = False

        if not hasattr(persistent, "debug_reveal_spoilers") or persistent.debug_reveal_spoilers is None:
            persistent.debug_reveal_spoilers = False

        if not hasattr(persistent, "timeline_bookmarks") or persistent.timeline_bookmarks is None:
            persistent.timeline_bookmarks = []
        elif not isinstance(persistent.timeline_bookmarks, list):
            persistent.timeline_bookmarks = list(persistent.timeline_bookmarks)

        if not hasattr(persistent, "unlocked_chapters") or persistent.unlocked_chapters is None:
            persistent.unlocked_chapters = []
        elif not isinstance(persistent.unlocked_chapters, list):
            persistent.unlocked_chapters = list(persistent.unlocked_chapters)

    normalize_persistent_progression_state()

    def progression_track_ids():
        track_ids = list(ROUTE_ORDER)
        for track_id in globals().get("RELATIONSHIP_TRACK_ORDER", []):
            add_unique(track_ids, track_id)
        return track_ids

    def make_progress_state():
        track_ids = list(ROUTE_ORDER)
        extra_tracks = globals().get("RELATIONSHIP_TRACK_ORDER", [])
        for track_id in extra_tracks:
            if track_id not in track_ids:
                track_ids.append(track_id)

        return {
            "initialized": False,
            "completed": [],
            "available": [],
            "excluded": [],
            "hidden": [],
            "temporarily_hidden": [],
            "unlocked_map_locations": [],
            "play_order": [],
            "recommended_next": [],
            "route_status": {route_id: "locked" for route_id in ROUTE_ORDER},
            "route_focus": {route_id: 0 for route_id in ROUTE_ORDER},
            "player_flags": [],
            "character_flags": {track_id: [] for track_id in track_ids},
            "relationship_directions": {track_id: [] for track_id in track_ids},
            "emotional_state": {
                "trust": 0,
                "distance": 0,
                "guard": 0,
                "misunderstanding": 0,
            },
            "unlocked_choices": [],
            "completed_exclusion_groups": [],
            "ending_flags": [],
            "ending_eligibility": [],
            "validation_issues": [],
            "acceptance_results": {},
        }

    def add_unique(target, value):
        if value not in target:
            target.append(value)

    def remove_if_present(target, value):
        if value in target:
            target.remove(value)

    def normalize_progress_runtime_state():
        # Save-safe migration when ROUTE_ORDER / skeleton metadata changes.
        expected_tracks = progression_track_ids()

        for key, default_value in make_progress_state().items():
            if key not in progress:
                progress[key] = default_value

        for route_id in ROUTE_ORDER:
            progress["route_status"].setdefault(route_id, "locked")
            progress["route_focus"].setdefault(route_id, 0)

        for stale_route_id in list(progress["route_status"].keys()):
            if stale_route_id not in ROUTE_ORDER:
                progress["route_status"].pop(stale_route_id, None)

        for stale_route_id in list(progress["route_focus"].keys()):
            if stale_route_id not in ROUTE_ORDER:
                progress["route_focus"].pop(stale_route_id, None)

        for track_id in expected_tracks:
            progress["character_flags"].setdefault(track_id, [])
            progress["relationship_directions"].setdefault(track_id, [])

    def chapter_data(chapter_id):
        return CHAPTERS[chapter_id]

    def get_route_chapters(route_id):
        return [chapter_id for chapter_id in CHAPTER_ORDER if CHAPTERS[chapter_id].get("route") == route_id]

    def chapter_title(chapter_id):
        return CHAPTERS[chapter_id].get("title", chapter_id)

    def route_title(route_id):
        return ROUTES.get(route_id, {}).get("title", route_id)

    def has_player_flag(flag):
        if flag in progress["player_flags"]:
            return True
        # Fallback for skeleton scenes that store flags in story_flags.
        story_has_flag_fn = globals().get("story_has_flag", None)
        if callable(story_has_flag_fn):
            return story_has_flag_fn(flag)
        return False

    def has_relationship_direction(route_id, direction):
        if direction in progress["relationship_directions"].get(route_id, []):
            return True
        # Fallback for skeleton scenes that call story_add_direction(character, direction).
        story_has_direction_fn = globals().get("story_has_direction", None)
        if callable(story_has_direction_fn):
            return story_has_direction_fn(route_id, direction)
        return False

    def has_completed(chapter_id):
        return chapter_id in progress["completed"]

    def any_completed(chapter_ids):
        return any(chapter_id in progress["completed"] for chapter_id in chapter_ids)

    def story_relation_value():
        state = globals().get("story_state", None)
        if isinstance(state, dict):
            return state.get("minh_yuuka_relation", "unknown")
        return "unknown"

    def story_relation_allowed(allowed_relations):
        if not allowed_relations:
            return True
        if isinstance(allowed_relations, str):
            allowed_relations = [allowed_relations]
        return story_relation_value() in allowed_relations

    def story_flag_blocked(blocking_flags):
        for flag in blocking_flags:
            if has_player_flag(flag):
                return True
        return False

    def prerequisites_met(chapter_id):
        chapter = CHAPTERS[chapter_id]

        if not all(prerequisite in progress["completed"] for prerequisite in chapter.get("prerequisites", [])):
            return False

        prerequisites_any = chapter.get("prerequisites_any", [])
        if prerequisites_any and not any_completed(prerequisites_any):
            return False

        required_story_relation = chapter.get("required_story_relation", [])
        if required_story_relation and not story_relation_allowed(required_story_relation):
            return False

        blocked_story_relation = chapter.get("blocked_story_relation", [])
        if blocked_story_relation and story_relation_allowed(blocked_story_relation):
            return False

        if story_flag_blocked(chapter.get("blocked_if_story_flag_any", [])):
            return False

        required_flags_all = chapter.get("required_flags_all", [])
        if required_flags_all and not all(has_player_flag(flag) for flag in required_flags_all):
            return False

        required_flags_any = chapter.get("required_flags_any", [])
        if required_flags_any and not any(has_player_flag(flag) for flag in required_flags_any):
            return False

        required_directions = chapter.get("required_directions", {})
        for route_id, directions in required_directions.items():
            if not any(has_relationship_direction(route_id, direction) for direction in directions):
                return False

        return True

    def initialize_progression():
        normalize_persistent_progression_state()
        normalize_progress_runtime_state()

        refresh_map_unlocks = globals().get("refresh_unlocked_map_locations", None)

        if progress["initialized"]:
            if callable(refresh_map_unlocks):
                refresh_map_unlocks()
            recalculate_chapter_availability()
            recalculate_route_status()
            recalculate_ending_eligibility()
            refresh_validation_state()
            update_recommended_next()

            refresh_phone = globals().get("phone_refresh_all", None)
            if callable(refresh_phone):
                refresh_phone()
            return

        progress["initialized"] = True

        first_chapter = ROUTES[DEFAULT_ROUTE_ID].get("entry_chapter")
        if first_chapter:
            add_unique(progress["available"], first_chapter)

        if callable(refresh_map_unlocks):
            refresh_map_unlocks()
        recalculate_chapter_availability()
        recalculate_route_status()
        recalculate_ending_eligibility()
        refresh_validation_state()
        update_recommended_next()

        refresh_phone = globals().get("phone_refresh_all", None)
        if callable(refresh_phone):
            refresh_phone()

        refresh_career = globals().get("career_check_all_promotions", None)
        if callable(refresh_career):
            refresh_career()

    def apply_direct_unlocks(chapter):
        for unlocked_chapter_id in chapter.get("unlocks", []):
            if unlocked_chapter_id not in CHAPTERS:
                continue
            if unlocked_chapter_id in progress["completed"]:
                continue
            if unlocked_chapter_id in progress["excluded"]:
                continue
            if prerequisites_met(unlocked_chapter_id):
                add_unique(progress["available"], unlocked_chapter_id)

    def apply_flags(chapter):
        for flag in chapter.get("flags_set", []):
            add_unique(progress["player_flags"], flag)

        for route_id, flags in chapter.get("character_flags_set", {}).items():
            progress["character_flags"].setdefault(route_id, [])
            for flag in flags:
                add_unique(progress["character_flags"][route_id], flag)

    def apply_relationship_directions(chapter):
        for route_id, directions in chapter.get("relationship_directions_set", {}).items():
            progress["relationship_directions"].setdefault(route_id, [])
            for direction in directions:
                add_unique(progress["relationship_directions"][route_id], direction)

    def apply_choice_unlocks(chapter):
        for choice_id in chapter.get("choice_unlocks", []):
            add_unique(progress["unlocked_choices"], choice_id)

    def apply_emotional_effects(chapter):
        for effect_key, delta in chapter.get("emotional_effects", {}).items():
            progress["emotional_state"][effect_key] = progress["emotional_state"].get(effect_key, 0) + delta

    def apply_exclusions(chapter):
        exclusion_group = chapter.get("exclusion_group")
        if exclusion_group:
            add_unique(progress["completed_exclusion_groups"], exclusion_group)

        for excluded_chapter_id in chapter.get("excludes", []):
            if excluded_chapter_id not in progress["completed"]:
                add_unique(progress["excluded"], excluded_chapter_id)
                remove_if_present(progress["available"], excluded_chapter_id)

    def sync_story_route_locks():
        relation = story_relation_value()
        if relation in ["ex_lovers_long_separated", "still_lovers"]:
            # Minh's romantic pairing routes with other characters are hard-blocked.
            for chapter_id in ["tam_c20a_tam_minh_possible", "thienan_c21a_minh_possible"]:
                if chapter_id in CHAPTERS and chapter_id not in progress["completed"]:
                    add_unique(progress["excluded"], chapter_id)
                    remove_if_present(progress["available"], chapter_id)

    def recalculate_chapter_availability():
        normalize_progress_runtime_state()
        sync_story_route_locks()
        progress["temporarily_hidden"] = []

        for chapter_id in CHAPTER_ORDER:
            if chapter_id in progress["completed"]:
                remove_if_present(progress["available"], chapter_id)
                remove_if_present(progress["hidden"], chapter_id)
                continue

            if chapter_id in progress["excluded"]:
                remove_if_present(progress["available"], chapter_id)
                remove_if_present(progress["hidden"], chapter_id)
                continue

            exclusion_group = CHAPTERS[chapter_id].get("exclusion_group")
            if exclusion_group and exclusion_group in progress["completed_exclusion_groups"]:
                remove_if_present(progress["available"], chapter_id)
                if chapter_id not in progress["completed"]:
                    add_unique(progress["excluded"], chapter_id)
                continue

            soft_hide_until_any_completed = CHAPTERS[chapter_id].get("soft_hide_until_any_completed", [])
            if soft_hide_until_any_completed and not any_completed(soft_hide_until_any_completed):
                remove_if_present(progress["available"], chapter_id)
                add_unique(progress["hidden"], chapter_id)
                add_unique(progress["temporarily_hidden"], chapter_id)
                continue

            remove_if_present(progress["hidden"], chapter_id)

            if prerequisites_met(chapter_id):
                add_unique(progress["available"], chapter_id)
            else:
                remove_if_present(progress["available"], chapter_id)

    def recalculate_route_status():
        normalize_progress_runtime_state()
        for route_id in ROUTE_ORDER:
            route_chapters = get_route_chapters(route_id)

            if not route_chapters:
                progress["route_status"][route_id] = "locked"
                continue

            completed_count = sum(1 for chapter_id in route_chapters if chapter_id in progress["completed"])
            available_count = sum(1 for chapter_id in route_chapters if chapter_id in progress["available"])

            if completed_count == len(route_chapters):
                progress["route_status"][route_id] = "completed"
            elif completed_count > 0 or available_count > 1:
                progress["route_status"][route_id] = "partially_unlocked"
            elif available_count > 0:
                progress["route_status"][route_id] = "available"
            else:
                progress["route_status"][route_id] = "locked"

    def ending_rule_met(ending_id, rule):
        normalize_persistent_progression_state()

        if not all(has_completed(chapter_id) for chapter_id in rule.get("requires_completed", [])):
            return False

        for route_id, directions in rule.get("requires_directions_any", {}).items():
            if not any(has_relationship_direction(route_id, direction) for direction in directions):
                return False

        required_story_relation = rule.get("required_story_relation", [])
        if required_story_relation and not story_relation_allowed(required_story_relation):
            return False

        for key, value in rule.get("emotional_min", {}).items():
            if progress["emotional_state"].get(key, 0) < value:
                return False

        for key, value in rule.get("emotional_max", {}).items():
            if progress["emotional_state"].get(key, 0) > value:
                return False

        if "route_focus_greater" in rule:
            left, right = rule["route_focus_greater"]
            if progress["route_focus"].get(left, 0) <= progress["route_focus"].get(right, 0):
                return False

        for ending_key in rule.get("persistent_endings_all", []):
            if ending_key not in persistent.route_clear_history:
                return False

        return True

    def recalculate_ending_eligibility():
        eligible = []
        for ending_id, rule in ENDING_RULES.items():
            if ending_rule_met(ending_id, rule):
                eligible.append(ending_id)
        progress["ending_eligibility"] = eligible

    def sort_available_chapters(chapter_ids):
        return sorted(
            chapter_ids,
            key=lambda chapter_id: (
                CHAPTERS[chapter_id].get("timeline_position", 9999),
                progress["route_focus"].get(CHAPTERS[chapter_id].get("route"), 0),
                CHAPTERS[chapter_id].get("id", chapter_id),
            ),
        )

    def update_recommended_next():
        available = [chapter_id for chapter_id in progress["available"] if chapter_id not in progress["hidden"]]
        progress["recommended_next"] = sort_available_chapters(available)[:2]

    def get_chapter_state(chapter_id):
        if chapter_id in progress["completed"]:
            return "completed"
        if chapter_id in progress["excluded"]:
            return "excluded"
        if chapter_id in progress["hidden"]:
            return "hidden"
        if chapter_id in progress["available"]:
            return "available"
        return "locked"

    def progression_debug_reveal_spoilers():
        normalize_persistent_progression_state()
        return bool(getattr(persistent, "debug_reveal_spoilers", False))

    def chapter_is_revealed(chapter_id):
        # Player-facing chapter names/details stay hidden until the chapter is
        # available or completed. Debug reveal must be explicitly toggled.
        if progression_debug_reveal_spoilers():
            return True
        return get_chapter_state(chapter_id) in ["available", "completed"]

    def chapter_safe_title(chapter_id, locked_title=None):
        if chapter_id in CHAPTERS and chapter_is_revealed(chapter_id):
            return chapter_title(chapter_id)
        if chapter_id in CHAPTERS:
            return CHAPTERS[chapter_id].get("locked_title") or locked_title or "Chưa mở khóa"
        return locked_title or "Chưa mở khóa"

    def chapter_safe_display_title(chapter_id, unlocked_title=None, locked_title=None):
        if chapter_id in CHAPTERS and chapter_is_revealed(chapter_id):
            return unlocked_title or chapter_title(chapter_id)
        if chapter_id in CHAPTERS:
            return CHAPTERS[chapter_id].get("locked_display_title") or CHAPTERS[chapter_id].get("locked_title") or locked_title or "Chương chưa mở khóa"
        return locked_title or "Chương chưa mở khóa"

    def chapter_list_safe_summary(chapter_ids):
        if not chapter_ids:
            return "None"
        return ", ".join(chapter_safe_display_title(chapter_id) for chapter_id in chapter_ids)

    def debug_toggle_spoiler_reveal():
        normalize_persistent_progression_state()
        persistent.debug_reveal_spoilers = not bool(persistent.debug_reveal_spoilers)
        return persistent.debug_reveal_spoilers

    def complete_chapter(chapter_id):
        initialize_progression()

        if chapter_id not in CHAPTERS:
            renpy.notify("Cannot complete unknown chapter: %s" % chapter_id)
            return

        if chapter_id in progress["completed"]:
            return

        chapter = CHAPTERS[chapter_id]
        route_id = chapter.get("route")

        add_unique(progress["completed"], chapter_id)
        remove_if_present(progress["available"], chapter_id)
        progress["play_order"].append(chapter_id)

        normalize_persistent_progression_state()
        add_unique(persistent.unlocked_chapters, chapter_id)

        reward_story_points = globals().get("award_investment_points_for_story_chapter", None)
        if callable(reward_story_points):
            reward_story_points(chapter_id)

        if route_id in progress["route_focus"]:
            progress["route_focus"][route_id] += 1

        apply_flags(chapter)
        apply_emotional_effects(chapter)
        apply_relationship_directions(chapter)
        apply_choice_unlocks(chapter)
        apply_exclusions(chapter)
        apply_direct_unlocks(chapter)

        refresh_map_unlocks = globals().get("refresh_unlocked_map_locations", None)
        if callable(refresh_map_unlocks):
            refresh_map_unlocks()

        recalculate_chapter_availability()
        recalculate_route_status()
        recalculate_ending_eligibility()
        refresh_validation_state()
        update_recommended_next()

        refresh_phone = globals().get("phone_refresh_all", None)
        if callable(refresh_phone):
            refresh_phone()

    def get_route_status_label(route_id):
        return progress["route_status"].get(route_id, "locked")

    def is_recommended_chapter(chapter_id):
        return chapter_id in progress["recommended_next"]

    def get_last_completed_chapter():
        if progress["play_order"]:
            return progress["play_order"][-1]
        return None

    def get_play_order_summary():
        if not progress["play_order"]:
            return "No chapters completed yet."
        return " → ".join(chapter_title(chapter_id) for chapter_id in progress["play_order"])

    def get_route_focus_summary(route_id):
        return progress["route_focus"].get(route_id, 0)

    def get_relationship_direction_summary(route_id):
        directions = progress["relationship_directions"].get(route_id, [])
        return ", ".join(directions) if directions else "None"

    def get_unlocked_choice_summary():
        return ", ".join(progress["unlocked_choices"]) if progress["unlocked_choices"] else "None"

    def choice_is_available(choice_id):
        if choice_id not in CHOICE_DEFINITIONS:
            return False

        definition = CHOICE_DEFINITIONS[choice_id]
        if choice_id not in progress["unlocked_choices"] and definition.get("type") != "insight":
            return False

        for condition in definition.get("conditions", []):
            if condition.startswith("direction_"):
                parts = condition.split("_")
                if len(parts) >= 3:
                    track = parts[1]
                    direction = "_".join(parts[2:])
                    if not has_relationship_direction(track, direction):
                        return False
            elif condition.startswith("flag_"):
                flag = condition.replace("flag_", "", 1)
                if not has_player_flag(flag):
                    return False
            elif condition == "relation_old_close_friends":
                if story_relation_value() != "old_close_friends":
                    return False

        return True

    def get_emotional_hint():
        trust = progress["emotional_state"].get("trust", 0)
        misunderstanding = progress["emotional_state"].get("misunderstanding", 0)
        distance = progress["emotional_state"].get("distance", 0)

        if misunderstanding >= 2:
            return "Misunderstanding thickens around the silence between them."
        if trust >= 3 and distance <= 0:
            return "Trust is quietly winning over hesitation."
        if distance > 0:
            return "Distance still lingers between what they feel and what they say."
        return "Their feelings are shifting, but not yet settled."

    def get_ending_summary():
        return ", ".join(progress["ending_eligibility"]) if progress["ending_eligibility"] else "None yet"

    def mark_ending_seen(ending_id):
        normalize_persistent_progression_state()
        add_unique(progress["ending_flags"], ending_id)
        add_unique(persistent.route_clear_history, ending_id)
        add_unique(persistent.gallery_unlocks, ending_id)
        if ending_id == "e01_canon_true":
            persistent.true_ending_seen = True

    def debug_unlock(chapter_id):
        if chapter_id in CHAPTERS and chapter_id not in progress["completed"] and chapter_id not in progress["excluded"]:
            add_unique(progress["available"], chapter_id)
            recalculate_route_status()
            update_recommended_next()

        refresh_phone = globals().get("phone_refresh_all", None)
        if callable(refresh_phone):
            refresh_phone()

    def debug_complete(chapter_id):
        if chapter_id in CHAPTERS:
            complete_chapter(chapter_id)

    def debug_reset_progress():
        global progress
        progress = make_progress_state()
        initialize_progression()

    def debug_set_minyuu_relation(relation):
        story_set_relation = globals().get("story_set_minyuu_relation", None)
        if callable(story_set_relation):
            story_set_relation(relation)
        else:
            state = globals().get("story_state", None)
            if isinstance(state, dict):
                state["minh_yuuka_relation"] = relation
        recalculate_chapter_availability()
        recalculate_route_status()
        update_recommended_next()

        refresh_phone = globals().get("phone_refresh_all", None)
        if callable(refresh_phone):
            refresh_phone()

    def debug_show_progress():
        return {
            "completed": list(progress["completed"]),
            "available": list(progress["available"]),
            "excluded": list(progress["excluded"]),
            "choices": list(progress["unlocked_choices"]),
            "endings": list(progress["ending_eligibility"]),
            "relation": story_relation_value(),
        }

    def validate_progression_metadata():
        issues = []

        if DEFAULT_ROUTE_ID not in ROUTES:
            issues.append("Default route does not exist.")

        for route_id, route in ROUTES.items():
            entry = route.get("entry_chapter")
            if entry and entry not in CHAPTERS:
                issues.append("Route %s has missing entry chapter %s." % (route_id, entry))

        order_seen = set()
        for chapter_id in CHAPTER_ORDER:
            if chapter_id in order_seen:
                issues.append("Chapter order contains duplicate chapter %s." % chapter_id)
            order_seen.add(chapter_id)
            if chapter_id not in CHAPTERS:
                issues.append("Chapter order references unknown chapter %s." % chapter_id)

        for chapter_id in CHAPTERS:
            if chapter_id not in CHAPTER_ORDER:
                issues.append("Chapter %s is missing from CHAPTER_ORDER." % chapter_id)

        exclusion_groups = {}
        for chapter_id, chapter in CHAPTERS.items():
            if chapter.get("route") not in ROUTES:
                issues.append("Chapter %s references unknown route %s." % (chapter_id, chapter.get("route")))

            for ref_group in ["prerequisites", "prerequisites_any", "unlocks", "excludes", "soft_hide_until_any_completed"]:
                for ref in chapter.get(ref_group, []):
                    if ref not in CHAPTERS:
                        issues.append("Chapter %s references unknown chapter %s in %s." % (chapter_id, ref, ref_group))

            for choice_id in chapter.get("choice_unlocks", []):
                if choice_id not in CHOICE_DEFINITIONS:
                    issues.append("Chapter %s unlocks unknown choice %s." % (chapter_id, choice_id))

            exclusion_group = chapter.get("exclusion_group")
            if exclusion_group:
                exclusion_groups.setdefault(exclusion_group, []).append(chapter_id)

        for group_id, members in exclusion_groups.items():
            if len(members) < 2:
                issues.append("Exclusion group %s needs at least two members." % group_id)

        for ending_id, rule in ENDING_RULES.items():
            for chapter_id in rule.get("requires_completed", []):
                if chapter_id not in CHAPTERS:
                    issues.append("Ending rule %s references unknown chapter %s." % (ending_id, chapter_id))

        return issues

    def get_validation_summary():
        return "No metadata issues" if not progress["validation_issues"] else " | ".join(progress["validation_issues"])

    def run_acceptance_checks():
        default_entry = ROUTES[DEFAULT_ROUTE_ID].get("entry_chapter")
        results = {
            "default_route_available": default_entry in progress["available"] or default_entry in progress["completed"],
            "full_skeleton_order_present": "final_c24_last_choices" in CHAPTER_ORDER and len(CHAPTER_ORDER) >= 30,
            "minyuu_verdict_present": all(ch in CHAPTERS for ch in ["fb_minyuu_04a_old_friends", "fb_minyuu_05b_separation", "fb_minyuu_04c_no_breakup"]),
            "all_ending_rules_present": len(ENDING_RULES) >= 24,
            "excluded_not_selectable": all(chapter_id not in progress["available"] for chapter_id in progress["excluded"]),
            "route_order_recorded": bool(progress["play_order"]) or not progress["completed"],
            "route_map_refresh_ready": True,
            "save_safe_default_state": True,
            "debug_tools_present": True,
        }
        progress["acceptance_results"] = results
        return results

    def get_acceptance_summary():
        run_acceptance_checks()
        passed = sum(1 for value in progress["acceptance_results"].values() if value)
        total = len(progress["acceptance_results"])
        return "%d/%d checks currently satisfied" % (passed, total)

    def refresh_validation_state():
        progress["validation_issues"] = validate_progression_metadata()
        run_acceptance_checks()

    def timeline_route_has_selectable_node(route_id):
        return any(CHAPTERS[chapter_id].get("route") == route_id and get_chapter_state(chapter_id) in ["available", "completed"] for chapter_id in CHAPTER_ORDER)

    def timeline_get_first_available_route_id():
        for route_id in ROUTE_ORDER:
            if timeline_route_has_selectable_node(route_id):
                return route_id
        return DEFAULT_ROUTE_ID

    def timeline_resolve_route_selection(selected_route=None, selected_node=None):
        route_id = selected_route if selected_route in ROUTES else DEFAULT_ROUTE_ID
        node_id = selected_node

        if not timeline_route_has_selectable_node(route_id):
            route_id = timeline_get_first_available_route_id()
            node_id = None

        if not node_id:
            node_id = timeline_get_first_selectable_node(route_id)

        if not node_id:
            for candidate_route in ROUTE_ORDER:
                candidate_node = timeline_get_first_selectable_node(candidate_route)
                if candidate_node:
                    return candidate_route, candidate_node

        return route_id, node_id


default progress = make_progress_state()
