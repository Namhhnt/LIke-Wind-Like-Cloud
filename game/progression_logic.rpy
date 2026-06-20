init -1 python:
    def make_progress_state():
        return {
            "initialized": False,
            "completed": [],
            "available": [],
            "excluded": [],
            "hidden": [],
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
        if progress["initialized"]:
            recalculate_chapter_availability()
            recalculate_route_status()
            recalculate_ending_eligibility()
            update_recommended_next()
            return

        progress["initialized"] = True
        first_chapter = ROUTES[DEFAULT_ROUTE_ID]["entry_chapter"]
        if first_chapter:
            add_unique(progress["available"], first_chapter)

        recalculate_chapter_availability()
        recalculate_route_status()
        recalculate_ending_eligibility()
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
        for chapter_id in CHAPTER_ORDER:
            if chapter_id in progress["completed"]:
                remove_if_present(progress["available"], chapter_id)
                continue

            if chapter_id in progress["excluded"]:
                remove_if_present(progress["available"], chapter_id)
                continue

            exclusion_group = CHAPTERS[chapter_id].get("exclusion_group")
            if exclusion_group and exclusion_group in progress["completed_exclusion_groups"]:
                remove_if_present(progress["available"], chapter_id)
                if chapter_id not in progress["completed"]:
                    add_unique(progress["excluded"], chapter_id)
                continue

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

    def recalculate_ending_eligibility():
        eligible = []

        if "hoang_h02" not in progress["completed"]:
            progress["ending_eligibility"] = eligible
            return

        if has_relationship_direction("hoang", "restraint") and progress["emotional_state"]["misunderstanding"] <= 1:
            eligible.append("ending_restraint")

        if has_relationship_direction("hoang", "confession"):
            eligible.append("ending_confession")

        if progress["emotional_state"]["trust"] >= 3 and progress["emotional_state"]["distance"] <= 0:
            eligible.append("ending_shared_silence")

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
        add_unique(progress["ending_flags"], ending_id)

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


default progress = make_progress_state()
