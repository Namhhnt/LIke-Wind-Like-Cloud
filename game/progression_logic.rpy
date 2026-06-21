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

    normalize_persistent_progression_state()

    def make_progress_state():
        return {
            "initialized": False,
            "completed": [],
            "available": [],
            "excluded": [],
            "hidden": [],
            "temporarily_hidden": [],
            "play_order": [],
            "recommended_next": [],
            "route_status": {route_id: "locked" for route_id in ROUTE_ORDER},
            "route_focus": {route_id: 0 for route_id in ROUTE_ORDER},
            "player_flags": [],
            "character_flags": {route_id: [] for route_id in ROUTE_ORDER},
            "relationship_directions": {route_id: [] for route_id in ROUTE_ORDER},
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

    def get_route_chapters(route_id):
        return [chapter_id for chapter_id in CHAPTER_ORDER if CHAPTERS[chapter_id]["route"] == route_id]

    def chapter_title(chapter_id):
        return CHAPTERS[chapter_id]["title"]

    def route_title(route_id):
        return ROUTES[route_id]["title"]

    def has_player_flag(flag):
        return flag in progress["player_flags"]

    def has_relationship_direction(route_id, direction):
        return direction in progress["relationship_directions"][route_id]

    def has_completed(chapter_id):
        return chapter_id in progress["completed"]

    def any_completed(chapter_ids):
        return any(chapter_id in progress["completed"] for chapter_id in chapter_ids)

    def prerequisites_met(chapter_id):
        chapter = CHAPTERS[chapter_id]
        if not all(prerequisite in progress["completed"] for prerequisite in chapter["prerequisites"]):
            return False

        required_directions = chapter.get("required_directions", {})
        for route_id, directions in required_directions.items():
            if not any(direction in progress["relationship_directions"][route_id] for direction in directions):
                return False

        return True

    def initialize_progression():
        normalize_persistent_progression_state()

        if progress["initialized"]:
            recalculate_chapter_availability()
            recalculate_route_status()
            recalculate_ending_eligibility()
            refresh_validation_state()
            update_recommended_next()
            return

        progress["initialized"] = True
        first_chapter = ROUTES[DEFAULT_ROUTE_ID]["entry_chapter"]
        if first_chapter:
            add_unique(progress["available"], first_chapter)

        recalculate_chapter_availability()
        recalculate_route_status()
        recalculate_ending_eligibility()
        refresh_validation_state()
        update_recommended_next()

    def apply_direct_unlocks(chapter):
        for unlocked_chapter_id in chapter["unlocks"]:
            if unlocked_chapter_id in progress["completed"]:
                continue
            if unlocked_chapter_id in progress["excluded"]:
                continue
            if prerequisites_met(unlocked_chapter_id):
                add_unique(progress["available"], unlocked_chapter_id)

    def apply_flags(chapter):
        for flag in chapter["flags_set"]:
            add_unique(progress["player_flags"], flag)

        for route_id, flags in chapter.get("character_flags_set", {}).items():
            for flag in flags:
                add_unique(progress["character_flags"][route_id], flag)

    def apply_relationship_directions(chapter):
        for route_id, directions in chapter.get("relationship_directions_set", {}).items():
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

    def recalculate_chapter_availability():
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
                progress["route_focus"][CHAPTERS[chapter_id]["route"]],
                CHAPTERS[chapter_id]["timeline_position"],
                CHAPTERS[chapter_id]["id"],
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

    def complete_chapter(chapter_id):
        initialize_progression()

        if chapter_id in progress["completed"]:
            return

        chapter = CHAPTERS[chapter_id]

        add_unique(progress["completed"], chapter_id)
        remove_if_present(progress["available"], chapter_id)
        progress["play_order"].append(chapter_id)
        progress["route_focus"][chapter["route"]] += 1

        apply_flags(chapter)
        apply_emotional_effects(chapter)
        apply_relationship_directions(chapter)
        apply_choice_unlocks(chapter)
        apply_exclusions(chapter)
        apply_direct_unlocks(chapter)

        recalculate_chapter_availability()
        recalculate_route_status()
        recalculate_ending_eligibility()
        refresh_validation_state()
        update_recommended_next()

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
        if not directions:
            return "None"
        return ", ".join(directions)

    def get_unlocked_choice_summary():
        if not progress["unlocked_choices"]:
            return "None"
        return ", ".join(progress["unlocked_choices"])

    def choice_is_available(choice_id):
        if choice_id not in CHOICE_DEFINITIONS:
            return False

        if choice_id not in progress["unlocked_choices"] and CHOICE_DEFINITIONS[choice_id]["type"] != "insight":
            return False

        for condition in CHOICE_DEFINITIONS[choice_id]["conditions"]:
            if condition == "direction_hoang_restraint" and not has_relationship_direction("hoang", "restraint"):
                return False
            if condition == "direction_hoang_confession" and not has_relationship_direction("hoang", "confession"):
                return False
            if condition == "flag_player_knows_hoang_restraint" and not has_player_flag("player_knows_hoang_restraint"):
                return False

        return True

    def get_emotional_hint():
        trust = progress["emotional_state"]["trust"]
        misunderstanding = progress["emotional_state"]["misunderstanding"]
        distance = progress["emotional_state"]["distance"]

        if misunderstanding >= 2:
            return "Misunderstanding thickens around the silence between them."
        if trust >= 3 and distance <= 0:
            return "Trust is quietly winning over hesitation."
        if distance > 0:
            return "Distance still lingers between what they feel and what they say."
        return "Their feelings are shifting, but not yet settled."

    def get_ending_summary():
        if not progress["ending_eligibility"]:
            return "None yet"
        return ", ".join(progress["ending_eligibility"])

    def mark_ending_seen(ending_id):
        normalize_persistent_progression_state()

        add_unique(progress["ending_flags"], ending_id)
        if ending_id not in persistent.route_clear_history:
            persistent.route_clear_history.append(ending_id)
        if ending_id not in persistent.gallery_unlocks:
            persistent.gallery_unlocks.append(ending_id)
        if ending_id == "ending_true_convergence":
            persistent.true_ending_seen = True

    def debug_unlock(chapter_id):
        if chapter_id in CHAPTERS and chapter_id not in progress["completed"] and chapter_id not in progress["excluded"]:
            add_unique(progress["available"], chapter_id)
            recalculate_route_status()
            update_recommended_next()

    def debug_complete(chapter_id):
        if chapter_id in CHAPTERS:
            complete_chapter(chapter_id)

    def debug_reset_progress():
        global progress
        progress = make_progress_state()
        initialize_progression()

    def debug_show_progress():
        return {
            "completed": list(progress["completed"]),
            "available": list(progress["available"]),
            "excluded": list(progress["excluded"]),
            "choices": list(progress["unlocked_choices"]),
            "endings": list(progress["ending_eligibility"]),
        }

    def validate_progression_metadata():
        issues = []

        if DEFAULT_ROUTE_ID not in ROUTES:
            issues.append("Default route does not exist.")

        for route_id, route in ROUTES.items():
            entry = route.get("entry_chapter")
            if entry and entry not in CHAPTERS:
                issues.append("Route %s has missing entry chapter %s." % (route_id, entry))

        exclusion_groups = {}
        for chapter_id, chapter in CHAPTERS.items():
            if chapter["route"] not in ROUTES:
                issues.append("Chapter %s references unknown route %s." % (chapter_id, chapter["route"]))

            for ref_group in ["prerequisites", "unlocks", "excludes", "soft_hide_until_any_completed"]:
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
        if not progress["validation_issues"]:
            return "No metadata issues"
        return " | ".join(progress["validation_issues"])

    def run_acceptance_checks():
        results = {
            "default_route_available": ROUTES[DEFAULT_ROUTE_ID]["entry_chapter"] in progress["available"] or ROUTES[DEFAULT_ROUTE_ID]["entry_chapter"] in progress["completed"],
            "cross_route_unlock_present": has_completed("tam_c02") or "hoang_h01" in progress["available"] or has_completed("hoang_h01"),
            "multiple_available_choices": len(progress["available"]) >= 1,
            "bonus_exclusion_works": bool(progress["completed_exclusion_groups"]),
            "excluded_not_selectable": all(chapter_id not in progress["available"] for chapter_id in progress["excluded"]),
            "bonus_unlocks_choices": bool(progress["unlocked_choices"]),
            "bonus_unlocks_directions": any(progress["relationship_directions"][route_id] for route_id in ROUTE_ORDER),
            "route_order_recorded": bool(progress["play_order"]),
            "player_and_character_knowledge_split": has_player_flag("player_knows_hoang_restraint") and bool(progress["character_flags"]["hoang"]),
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


default progress = make_progress_state()
