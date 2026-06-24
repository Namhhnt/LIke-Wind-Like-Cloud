default persistent.investment_points = 0
default persistent.spent_investment_points = 0
default persistent.unlocked_library_content = []
default persistent.read_library_content = []
default persistent.claimed_rewards = []

define STORY_LIBRARY_STORY_REWARD = 1
define STORY_LIBRARY_DEFAULT_SMALL_COST = 1
define STORY_LIBRARY_DEFAULT_MEDIUM_COST = 3
define STORY_LIBRARY_DEFAULT_LARGE_COST = 5
define STORY_LIBRARY_DEFAULT_SPECIAL_COST = 10

init -1 python:
    import json
    import os

    library_items = {}
    story_library_loaded = False
    story_library_last_error = None

    def ensure_story_library_defaults():
        if not hasattr(persistent, "investment_points") or persistent.investment_points is None:
            persistent.investment_points = 0

        if not hasattr(persistent, "spent_investment_points") or persistent.spent_investment_points is None:
            persistent.spent_investment_points = 0

        if not hasattr(persistent, "unlocked_library_content") or persistent.unlocked_library_content is None:
            persistent.unlocked_library_content = []
        elif not isinstance(persistent.unlocked_library_content, list):
            persistent.unlocked_library_content = list(persistent.unlocked_library_content)

        if not hasattr(persistent, "read_library_content") or persistent.read_library_content is None:
            persistent.read_library_content = []
        elif not isinstance(persistent.read_library_content, list):
            persistent.read_library_content = list(persistent.read_library_content)

        if not hasattr(persistent, "claimed_rewards") or persistent.claimed_rewards is None:
            persistent.claimed_rewards = []
        elif not isinstance(persistent.claimed_rewards, list):
            persistent.claimed_rewards = list(persistent.claimed_rewards)

    def safe_story_library_int(value, default=0):
        try:
            return int(value)
        except Exception:
            return default

    def chapter_point_cost(size, explicit_cost=None):
        if explicit_cost not in [None, ""]:
            explicit = safe_story_library_int(explicit_cost, 0)
            return explicit

        size = (size or "").strip().lower()
        if size == "small":
            return STORY_LIBRARY_DEFAULT_SMALL_COST
        if size == "medium":
            return STORY_LIBRARY_DEFAULT_MEDIUM_COST
        if size == "large":
            return STORY_LIBRARY_DEFAULT_LARGE_COST
        if size == "special":
            return STORY_LIBRARY_DEFAULT_SPECIAL_COST
        return 0

    def story_library_game_path(path):
        normalized = (path or "").replace("\\", "/").lstrip("/")
        if not normalized:
            return None

        game_dir = getattr(config, "gamedir", None)
        if not game_dir:
            return None

        return os.path.join(game_dir, normalized)

    def story_library_read_text(path):
        filesystem_path = story_library_game_path(path)

        if filesystem_path and os.path.isfile(filesystem_path):
            try:
                with open(filesystem_path, "r", encoding="utf-8") as handle:
                    return handle.read()
            except Exception as exc:
                renpy.log("Story library: failed to read filesystem path %s (%s)" % (filesystem_path, exc))

        try:
            raw_data = renpy.file(path).read()
            if isinstance(raw_data, bytes):
                return raw_data.decode("utf-8")
            return raw_data
        except Exception as exc:
            renpy.log("Story library: failed to read %s (%s)" % (path, exc))
            return None

    def story_library_list_text_files():
        files = set()

        stories_dir = story_library_game_path("stories")
        if stories_dir and os.path.isdir(stories_dir):
            for root, _dirs, filenames in os.walk(stories_dir):
                for filename in filenames:
                    if not (filename.endswith(".md") or filename.endswith(".txt")):
                        continue

                    absolute_path = os.path.join(root, filename)
                    relative_path = os.path.relpath(absolute_path, getattr(config, "gamedir", stories_dir))
                    normalized = relative_path.replace("\\", "/")
                    if normalized.startswith("stories/"):
                        files.add(normalized)

        for path in renpy.list_files():
            normalized = path.replace("\\", "/")
            if not normalized.startswith("stories/"):
                continue
            if normalized.endswith("manifest.json"):
                continue
            if normalized.endswith(".md") or normalized.endswith(".txt"):
                files.add(normalized)
        return sorted(files)

    def story_library_slug_from_path(path):
        base_name = os.path.splitext(os.path.basename(path))[0]
        slug = base_name.strip().lower().replace(" ", "_")
        return slug or "story"

    def normalize_library_item(item):
        if not isinstance(item, dict):
            return None

        item_id = (item.get("id") or "").strip()
        file_path = (item.get("file") or item.get("local_file") or "").strip()
        if not item_id or not file_path:
            return None

        normalized = dict(item)
        normalized["id"] = item_id
        normalized["file"] = file_path.replace("\\", "/")
        normalized["title"] = (item.get("title") or item_id.replace("_", " ").title()).strip()
        normalized["series"] = (item.get("series") or _("Original Stories")).strip()
        normalized["type"] = (item.get("type") or "original_story").strip().lower()
        normalized["size"] = (item.get("size") or "small").strip().lower()
        normalized["source"] = (item.get("source") or "local").strip().lower()
        normalized["order"] = safe_story_library_int(item.get("order"), 0)
        normalized["category"] = (item.get("category") or "stories").strip().lower()
        normalized["is_read_only"] = bool(item.get("is_read_only", True))
        normalized["cover"] = (item.get("cover") or "").strip()
        normalized["unlock_mode"] = (item.get("unlock_mode") or "").strip().lower() or None

        prerequisites = item.get("prerequisites") or []
        if isinstance(prerequisites, str):
            prerequisites = [prerequisites]
        normalized["prerequisites"] = [value for value in prerequisites if value]

        tags = item.get("tags") or []
        if isinstance(tags, str):
            tags = [tags]
        normalized["tags"] = [value for value in tags if value]

        point_cost = chapter_point_cost(normalized["size"], item.get("point_cost"))
        normalized["point_cost"] = point_cost
        if normalized["unlock_mode"] is None:
            normalized["unlock_mode"] = "points" if point_cost > 0 else "free"

        return normalized

    def register_library_item(item):
        normalized = normalize_library_item(item)
        if not normalized:
            return False
        library_items[normalized["id"]] = normalized
        return True

    def load_story_library_manifest_items():
        raw_manifest = story_library_read_text("stories/manifest.json")
        if not raw_manifest:
            return []

        try:
            manifest = json.loads(raw_manifest)
        except Exception as exc:
            renpy.log("Story library: invalid manifest.json (%s)" % exc)
            return []

        stories = manifest.get("stories", [])
        items = []
        for entry in stories:
            normalized = normalize_library_item(entry)
            if normalized:
                items.append(normalized)
        return items

    def build_library_item_from_story_file(path):
        raw_text = story_library_read_text(path)
        if not raw_text:
            return None

        parsed_story = parse_story_text(raw_text)
        metadata = parsed_story.get("metadata", {})
        item_id = (metadata.get("id") or story_library_slug_from_path(path)).strip()
        return normalize_library_item({
            "id": item_id,
            "title": metadata.get("title") or item_id.replace("_", " ").title(),
            "series": metadata.get("series") or _("Original Stories"),
            "type": metadata.get("type") or "original_story",
            "size": metadata.get("size") or "small",
            "file": path,
            "order": metadata.get("order") or 0,
            "point_cost": metadata.get("point_cost") or 0,
            "unlock_mode": metadata.get("unlock_mode") or None,
            "prerequisites": metadata.get("prerequisites") or [],
            "tags": metadata.get("tags") or [],
            "cover": metadata.get("cover") or "",
            "source": "local",
            "category": "stories",
            "is_read_only": True,
        })

    def load_story_library_local_items():
        manifest_items = load_story_library_manifest_items()
        if manifest_items:
            return manifest_items

        scanned_items = []
        for path in story_library_list_text_files():
            item = build_library_item_from_story_file(path)
            if item:
                scanned_items.append(item)
        return scanned_items

    def refresh_story_library_registry():
        global story_library_loaded, story_library_last_error

        ensure_story_library_defaults()
        # Preserve non-story items (minigames, extras, etc.) registered outside the manifest.
        preserved = {k: v for k, v in library_items.items() if v.get("category") != "stories"}
        library_items.clear()
        library_items.update(preserved)
        story_library_last_error = None

        try:
            for item in load_story_library_local_items():
                register_library_item(item)
            story_library_loaded = True
        except Exception as exc:
            story_library_loaded = False
            story_library_last_error = str(exc)
            renpy.log("Story library: registry refresh failed (%s)" % exc)

    def ensure_story_library_loaded():
        if not story_library_loaded:
            refresh_story_library_registry()

    def get_library_item(content_id):
        ensure_story_library_loaded()
        return library_items.get(content_id)

    def get_library_story_items():
        ensure_story_library_loaded()
        items = [item for item in library_items.values() if item.get("category") == "stories"]
        return sorted(items, key=lambda item: (item.get("series", ""), item.get("order", 0), item.get("title", "")))

    def get_library_story_counts():
        items = get_library_story_items()
        unlocked = [item for item in items if is_library_content_unlocked(item["id"])]
        read_items = [item for item in items if item["id"] in persistent.read_library_content]
        return {
            "total": len(items),
            "unlocked": len(unlocked),
            "read": len(read_items),
        }

    def get_story_library_progress_text():
        counts = get_library_story_counts()
        if counts["total"] <= 0:
            return "0 / 0"
        return "%d / %d" % (counts["unlocked"], counts["total"])

    def is_chapter_completed_for_library(chapter_id):
        progress_state = globals().get("progress", None)
        if isinstance(progress_state, dict) and chapter_id in progress_state.get("completed", []):
            return True

        fallback_completed = globals().get("story_completed_chapters", [])
        return chapter_id in fallback_completed

    def library_prerequisites_met(item):
        for chapter_id in item.get("prerequisites", []):
            if not is_chapter_completed_for_library(chapter_id):
                return False
        return True

    def get_library_prerequisite_labels(item):
        labels = []
        chapter_lookup = globals().get("CHAPTERS", {})
        chapter_title_fn = globals().get("chapter_title", None)

        for chapter_id in item.get("prerequisites", []):
            if callable(chapter_title_fn) and chapter_id in chapter_lookup:
                labels.append(chapter_title_fn(chapter_id))
            else:
                labels.append(chapter_id)

        return labels

    def get_library_prerequisite_text(item):
        labels = get_library_prerequisite_labels(item)
        if not labels:
            return _("No story requirement.")
        return _("Requires: %(requirements)s") % {"requirements": ", ".join(labels)}

    def has_investment_points(cost):
        ensure_story_library_defaults()
        return persistent.investment_points >= max(0, safe_story_library_int(cost, 0))

    def spend_investment_points(cost):
        ensure_story_library_defaults()
        amount = max(0, safe_story_library_int(cost, 0))
        if persistent.investment_points < amount:
            return False

        persistent.investment_points -= amount
        persistent.spent_investment_points += amount
        renpy.save_persistent()
        return True

    def award_investment_points(amount, source_key=None):
        ensure_story_library_defaults()
        points = max(0, safe_story_library_int(amount, 0))
        if points <= 0:
            return False

        if source_key and source_key in persistent.claimed_rewards:
            return False

        persistent.investment_points += points
        if source_key:
            persistent.claimed_rewards.append(source_key)

        renpy.save_persistent()
        return True

    def award_investment_points_for_story_chapter(chapter_id):
        reward_key = "chapter_reward:%s" % chapter_id
        return award_investment_points(STORY_LIBRARY_STORY_REWARD, reward_key)

    def is_library_content_unlocked(content_id):
        ensure_story_library_defaults()

        item = get_library_item(content_id)
        if not item:
            return False

        if item.get("unlock_mode") in [None, "free"]:
            return library_prerequisites_met(item)

        return content_id in persistent.unlocked_library_content

    def can_unlock_library_content(content_id):
        item = get_library_item(content_id)
        if not item:
            return False, "not_found"

        if is_library_content_unlocked(content_id):
            return True, "already_unlocked"

        if not library_prerequisites_met(item):
            return False, "missing_prerequisites"

        cost = safe_story_library_int(item.get("point_cost"), 0)
        if cost <= 0:
            return True, "free"

        if not has_investment_points(cost):
            return False, "not_enough_points"

        return True, "can_unlock"

    def unlock_library_content(content_id):
        ensure_story_library_defaults()

        item = get_library_item(content_id)
        if not item:
            return False, "not_found"

        ok, reason = can_unlock_library_content(content_id)
        if not ok:
            return False, reason

        if content_id in persistent.unlocked_library_content:
            return True, "already_unlocked"

        cost = safe_story_library_int(item.get("point_cost"), 0)
        if cost > 0 and not spend_investment_points(cost):
            return False, "not_enough_points"

        persistent.unlocked_library_content.append(content_id)
        renpy.save_persistent()
        return True, "unlocked"

    def mark_library_content_read(content_id):
        ensure_story_library_defaults()
        if content_id not in persistent.read_library_content:
            persistent.read_library_content.append(content_id)
            renpy.save_persistent()

    def get_library_story_state(item):
        content_id = item["id"]
        is_unlocked = is_library_content_unlocked(content_id)
        is_read = content_id in persistent.read_library_content
        prerequisites_ready = library_prerequisites_met(item)
        cost = safe_story_library_int(item.get("point_cost"), 0)

        if is_read:
            return "read"
        if is_unlocked:
            return "available"
        if not prerequisites_ready:
            return "locked_prerequisites"
        if cost > 0 and not has_investment_points(cost):
            return "not_enough_points"
        if cost > 0:
            return "unlockable"
        return "available"

    def get_library_story_action_text(item):
        state = get_library_story_state(item)
        cost = safe_story_library_int(item.get("point_cost"), 0)

        if state == "read":
            return _("Read Again")
        if state == "available":
            return _("Read")
        if state == "locked_prerequisites":
            return _("Locked")
        if state == "not_enough_points":
            return _("Need %(points)s Point(s)") % {"points": cost}
        if state == "unlockable":
            return _("Unlock — %(points)s Point(s)") % {"points": cost}
        return _("Unavailable")

    def get_library_story_status_text(item):
        state = get_library_story_state(item)
        if state == "read":
            return _("Read")
        if state == "available":
            return _("Unlocked")
        if state == "locked_prerequisites":
            return _("Locked by story progression")
        if state == "not_enough_points":
            return _("Missing Investment Points")
        if state == "unlockable":
            return _("Ready to unlock")
        return _("Unavailable")

    def attempt_unlock_library_content(content_id):
        item = get_library_item(content_id)
        if not item:
            renpy.notify(_("This story could not be found."))
            return False

        ok, reason = unlock_library_content(content_id)
        if ok and reason in ["unlocked", "already_unlocked"]:
            renpy.notify(_("Unlocked %(title)s.") % {"title": item.get("title", content_id)})
            return True

        if reason == "missing_prerequisites":
            renpy.notify(_("Story requirements are not met yet."))
        elif reason == "not_enough_points":
            renpy.notify(_("Not enough Investment Points."))
        else:
            renpy.notify(_("This story could not be unlocked."))
        return False

    def story_library_debug_grant_points(amount=3):
        award_investment_points(amount)

    refresh_story_library_registry()
