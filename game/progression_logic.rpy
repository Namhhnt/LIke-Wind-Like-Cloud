init -1 python:
    def make_progress_state():
        return {
            "initialized": False,
            "completed": [],
            "available": [],
            "excluded": [],
            "hidden": [],
            "play_order": [],
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

    def prerequisites_met(chapter_id):
        chapter = CHAPTERS[chapter_id]
        return all(prerequisite in progress["completed"] for prerequisite in chapter["prerequisites"])

    def initialize_progression():
        if progress["initialized"]:
            recalculate_chapter_availability()
            recalculate_route_status()
            return

        progress["initialized"] = True
        first_chapter = ROUTES[DEFAULT_ROUTE_ID]["entry_chapter"]
        if first_chapter:
            add_unique(progress["available"], first_chapter)

        recalculate_chapter_availability()
        recalculate_route_status()

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

    def recalculate_chapter_availability():
        for chapter_id in CHAPTER_ORDER:
            if chapter_id in progress["completed"]:
                remove_if_present(progress["available"], chapter_id)
                continue

            if chapter_id in progress["excluded"]:
                remove_if_present(progress["available"], chapter_id)
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
        apply_direct_unlocks(chapter)

        recalculate_chapter_availability()
        recalculate_route_status()

    def get_route_status_label(route_id):
        return progress["route_status"].get(route_id, "locked")


default progress = make_progress_state()
