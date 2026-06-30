init -1 python:

    def map_condition_is_met(condition):
        if not condition or condition == "always":
            return True

        parts = condition.split(":")
        if not parts:
            return False

        kind = parts[0]

        if kind == "completed" and len(parts) >= 2:
            return parts[1] in progress.get("completed", [])

        if kind == "not_completed" and len(parts) >= 2:
            return parts[1] not in progress.get("completed", [])

        if kind == "flag" and len(parts) >= 2:
            checker = globals().get("has_player_flag", None)
            return checker(parts[1]) if callable(checker) else parts[1] in progress.get("player_flags", [])

        if kind == "not_flag" and len(parts) >= 2:
            checker = globals().get("has_player_flag", None)
            return (not checker(parts[1])) if callable(checker) else parts[1] not in progress.get("player_flags", [])

        if kind == "direction" and len(parts) >= 3:
            checker = globals().get("has_relationship_direction", None)
            if callable(checker):
                return checker(parts[1], parts[2])
            directions = progress.get("relationship_directions", {}).get(parts[1], [])
            return parts[2] in directions

        return False


    def map_conditions_are_met(conditions):
        if not conditions:
            return True

        for condition in conditions:
            if not map_condition_is_met(condition):
                return False

        return True


    def fixed_location_is_unlocked(location_id):
        loc = FIXED_MAP_LOCATIONS.get(location_id)
        if not loc:
            return False
        if loc.get("default_unlocked", False):
            return True

        unlocked_locations = progress.get("unlocked_map_locations", [])
        if unlocked_locations is None:
            unlocked_locations = []
        elif not isinstance(unlocked_locations, list):
            unlocked_locations = list(unlocked_locations)
            progress["unlocked_map_locations"] = unlocked_locations

        if location_id in unlocked_locations:
            return True

        return map_conditions_are_met(loc.get("unlock_conditions", []))


    def refresh_unlocked_map_locations():
        unlocked_locations = progress.setdefault("unlocked_map_locations", [])
        if unlocked_locations is None:
            unlocked_locations = []
            progress["unlocked_map_locations"] = unlocked_locations
        elif not isinstance(unlocked_locations, list):
            unlocked_locations = list(unlocked_locations)
            progress["unlocked_map_locations"] = unlocked_locations

        opening_locations_ready = (
            map_condition_is_met("flag:opening_map_locations_unlocked")
            or map_condition_is_met("completed:tam_c01_interview_day")
        )

        if not opening_locations_ready:
            for location_id in ["tam_apartment", "huyen_apartment", "company"]:
                remove_if_present(unlocked_locations, location_id)

        for location_id, location in FIXED_MAP_LOCATIONS.items():
            if location.get("default_unlocked", False):
                add_unique(unlocked_locations, location_id)
                continue

            if map_conditions_are_met(location.get("unlock_conditions", [])):
                add_unique(unlocked_locations, location_id)


    def unlock_map_location(location_id):
        initialize_progression()

        if location_id not in FIXED_MAP_LOCATIONS:
            return

        unlocked_locations = progress.setdefault("unlocked_map_locations", [])
        if unlocked_locations is None:
            unlocked_locations = []
            progress["unlocked_map_locations"] = unlocked_locations
        elif not isinstance(unlocked_locations, list):
            unlocked_locations = list(unlocked_locations)
            progress["unlocked_map_locations"] = unlocked_locations

        add_unique(unlocked_locations, location_id)


    def unlock_map_locations(location_ids):
        initialize_progression()

        for location_id in location_ids or []:
            unlock_map_location(location_id)


    def map_context_for_story_target(chapter_id=None, scene_id=None):
        if scene_id:
            context_id = MAP_CONTEXT_BY_SCENE.get(scene_id)
            if context_id in MAP_CONTEXTS:
                return context_id

        if chapter_id:
            context_id = MAP_CONTEXT_BY_CHAPTER.get(chapter_id)
            if context_id in MAP_CONTEXTS:
                return context_id

        return None


    def queue_story_map_context(context_id=None, chapter_id=None, scene_id=None):
        global next_story_map_context_id

        resolved_context_id = context_id or map_context_for_story_target(chapter_id=chapter_id, scene_id=scene_id)
        next_story_map_context_id = resolved_context_id if resolved_context_id in MAP_CONTEXTS else None
        return next_story_map_context_id


    def resolve_story_map_context(default_context_id="act1_default"):
        global next_story_map_context_id

        resolved_context_id = next_story_map_context_id
        next_story_map_context_id = None

        if resolved_context_id in MAP_CONTEXTS:
            return resolved_context_id

        last_completed_chapter = globals().get("get_last_completed_chapter", None)
        chapter_id = last_completed_chapter() if callable(last_completed_chapter) else None
        resolved_context_id = map_context_for_story_target(chapter_id=chapter_id)

        if resolved_context_id in MAP_CONTEXTS:
            return resolved_context_id

        return default_context_id if default_context_id in MAP_CONTEXTS else "act1_default"


    def chapter_is_available_for_map(chapter_id):
        initialize_progression()

        if chapter_id not in CHAPTERS:
            return False

        state_fn = globals().get("get_chapter_state", None)
        if callable(state_fn):
            return state_fn(chapter_id) == "available"

        if chapter_id in progress.get("completed", []):
            return False
        if chapter_id in progress.get("excluded", []):
            return False
        return chapter_id in progress.get("available", [])


    def map_kind_for_chapter(chapter):
        chapter_type = chapter.get("type", "extra")
        if chapter_type == "core":
            return "main"
        if chapter_type == "pov":
            return "character"
        if chapter_type == "bonus":
            return "bonus"
        return "extra"


    def map_location_for_chapter(chapter_id):
        chapter = CHAPTERS.get(chapter_id, {})
        return MAP_CHAPTER_LOCATION_OVERRIDES.get(chapter_id, MAP_ROUTE_DEFAULT_LOCATIONS.get(chapter.get("route")))


    def map_make_entry_description(chapter_id):
        chapter = CHAPTERS.get(chapter_id, {})
        route_label = route_title(chapter.get("route")) if chapter.get("route") else chapter_id
        chapter_type = chapter.get("type", "extra").replace("_", " ").title()
        return "%s • %s" % (route_label, chapter_type)


    def map_route_fallback_coordinates(route_id, slot_index):
        base_locations = {
            "tam": (280, 218),
            "hoang": (302, 782),
            "yuuka": (1546, 170),
            "minh": (366, 486),
            "thienan": (700, 500),
            "huyen": (520, 290),
            "work": (1158, 548),
            "final": (1048, 456),
        }
        base_x, base_y = base_locations.get(route_id, (960, 540))
        offset_x, offset_y = MAP_MARKER_OFFSETS[slot_index % len(MAP_MARKER_OFFSETS)]
        return base_x + offset_x, base_y + offset_y


    def resolve_map_entry(raw_entry):
        entry = dict(raw_entry)
        location_id = entry.get("location_id")

        if location_id:
            fixed = FIXED_MAP_LOCATIONS.get(location_id, {})
            entry.setdefault("name", fixed.get("name", "Unknown Location"))
            entry.setdefault("x", fixed.get("x", 0))
            entry.setdefault("y", fixed.get("y", 0))
            entry.setdefault("category", fixed.get("category", "unknown"))
            entry.setdefault("icon", fixed.get("icon", "default"))
            entry.setdefault("description", fixed.get("description", ""))
        else:
            entry.setdefault("name", entry.get("title", "Temporary Location"))
            entry.setdefault("category", "temporary")
            entry.setdefault("icon", "temporary")

        entry.setdefault("kind", "extra")
        entry.setdefault("conditions", [])
        entry.setdefault("required", False)
        entry.setdefault("enabled", True)
        entry.setdefault("lock_reason", "")
        entry.setdefault("state", "available")
        return entry


    def map_entry_is_available(entry, context=None):
        location_id = entry.get("location_id")
        target_chapter_id = entry.get("target_chapter_id")
        target_label = entry.get("target_label")

        if target_chapter_id:
            if not chapter_is_available_for_map(target_chapter_id):
                entry["lock_reason"] = "Story event is not available yet."
                return "locked"

        elif location_id and not fixed_location_is_unlocked(location_id):
            return "hidden"

        if target_label and not renpy.has_label(target_label):
            entry["lock_reason"] = "This story event is not ready yet."
            return "locked"

        if not map_conditions_are_met(entry.get("conditions", [])):
            return "hidden"

        if not entry.get("enabled", True):
            entry["lock_reason"] = entry.get("lock_reason") or "This location is not available right now."
            return "locked"

        if context:
            temp_locks = context.get("temporarily_locked_locations", {})
            if location_id in temp_locks:
                entry["lock_reason"] = temp_locks[location_id]
                return "locked"

            force_only = context.get("force_only_locations", [])
            if force_only and location_id and location_id not in force_only:
                entry["lock_reason"] = "Not available right now."
                return "locked"

        return "available"


    def build_story_hub_raw_entries():
        initialize_progression()

        available_chapters = [
            chapter_id
            for chapter_id in progress.get("available", [])
            if chapter_id not in progress.get("hidden", []) and chapter_id not in progress.get("excluded", [])
        ]

        sorter = globals().get("sort_available_chapters", None)
        if callable(sorter):
            available_chapters = sorter(available_chapters)
        else:
            available_chapters = sorted(available_chapters)

        location_counts = {}
        route_counts = {}
        raw_entries = []

        for chapter_id in available_chapters:
            chapter = CHAPTERS.get(chapter_id, {})
            route_id = chapter.get("route")
            location_id = map_location_for_chapter(chapter_id)

            raw_entry = {
                "id": "chapter_%s" % chapter_id,
                "title": chapter_title(chapter_id),
                "target_chapter_id": chapter_id,
                "kind": map_kind_for_chapter(chapter),
                "description": map_make_entry_description(chapter_id),
                "route_id": route_id,
                "chapter_id": chapter_id,
            }

            if location_id:
                raw_entry["location_id"] = location_id
                slot_index = location_counts.get(location_id, 0)
                location_counts[location_id] = slot_index + 1
                offset_x, offset_y = MAP_MARKER_OFFSETS[slot_index % len(MAP_MARKER_OFFSETS)]
                fixed = FIXED_MAP_LOCATIONS.get(location_id, {})
                raw_entry["x"] = fixed.get("x", 960) + offset_x
                raw_entry["y"] = fixed.get("y", 540) + offset_y
            else:
                slot_index = route_counts.get(route_id, 0)
                route_counts[route_id] = slot_index + 1
                raw_entry["x"], raw_entry["y"] = map_route_fallback_coordinates(route_id, slot_index)

            raw_entries.append(raw_entry)

        return raw_entries


    def build_context_location_markers(context, used_location_ids):
        if not context.get("show_locked_fixed_locations", False):
            return []

        temp_locks = context.get("temporarily_locked_locations", {})
        force_only = context.get("force_only_locations", [])
        entries = []

        for location_id, location in FIXED_MAP_LOCATIONS.items():
            if location_id in used_location_ids:
                continue

            visible = fixed_location_is_unlocked(location_id) or location_id in temp_locks or location_id in force_only
            if not visible:
                continue

            lock_reason = temp_locks.get(location_id, "No story event is available here right now.")
            if force_only and location_id not in force_only and location_id not in temp_locks:
                lock_reason = "Not available right now."

            entries.append({
                "id": "fixed_%s" % location_id,
                "location_id": location_id,
                "title": location.get("name", location_id),
                "name": location.get("name", location_id),
                "description": location.get("description", ""),
                "kind": "locked",
                "enabled": False,
                "lock_reason": lock_reason,
                "state": "locked",
            })

        return entries


    def build_map_entries(raw_entries=None, context_id="act1_default"):
        initialize_progression()

        source_entries = raw_entries if raw_entries is not None else build_story_hub_raw_entries()
        context = MAP_CONTEXTS.get(context_id, MAP_CONTEXTS["act1_default"])

        final_entries = []
        used_location_ids = set()

        for raw_entry in source_entries:
            entry = resolve_map_entry(raw_entry)
            state = map_entry_is_available(entry, context)
            if state == "hidden":
                continue

            entry["state"] = state
            final_entries.append(entry)

            if entry.get("location_id"):
                used_location_ids.add(entry["location_id"])

        for extra_entry in build_context_location_markers(context, used_location_ids):
            final_entries.append(resolve_map_entry(extra_entry))

        priority = {
            "main": 0,
            "character": 1,
            "bonus": 2,
            "extra": 3,
            "temporary": 4,
            "locked": 5,
        }
        final_entries.sort(key=lambda entry: (priority.get(entry.get("kind"), 99), entry.get("title", entry.get("name", ""))))
        return final_entries


    def resolve_map_target_label(entry):
        if not entry:
            return None

        if entry.get("target_label"):
            target_label = entry.get("target_label")
            return target_label if renpy.has_label(target_label) else None

        chapter_id = entry.get("target_chapter_id")
        if chapter_id and chapter_id in CHAPTERS:
            target_label = CHAPTERS[chapter_id].get("label", chapter_id)
            return target_label if renpy.has_label(target_label) else None

        return None
