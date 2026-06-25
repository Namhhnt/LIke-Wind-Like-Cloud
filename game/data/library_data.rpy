init -5 python:

    LIBRARY_CATEGORIES = [
        {
            "id": "characters",
            "title": "Character Profiles",
            "subtitle": "Learn about the characters in the story.",
            "icon_text": "◇",
            "screen": "library_characters",
            "requires_unlock": False,
        },
        {
            "id": "stories",
            "title": "Original Stories",
            "subtitle": "Read side stories and original materials.",
            "icon_text": "✦",
            "screen": "library_stories",
            "requires_unlock": False,
        },
        {
            "id": "cg",
            "title": "CG Gallery",
            "subtitle": "Review memorable visual moments.",
            "icon_text": "▣",
            "screen": "library_cg",
            "requires_unlock": False,
        },
        {
            "id": "music",
            "title": "Music Room",
            "subtitle": "Listen to unlocked music tracks.",
            "icon_text": "♪",
            "screen": "library_music",
            "requires_unlock": False,
        },
        {
            "id": "minigames",
            "title": "Minigames",
            "subtitle": "Replay special minigames.",
            "icon_text": "◈",
            "screen": "library_minigames",
            "requires_unlock": False,
        },
        {
            "id": "extras",
            "title": "Extras",
            "subtitle": "Bonus content and special materials.",
            "icon_text": "✧",
            "screen": "library_extras",
            "requires_unlock": False,
        },
    ]

    LIBRARY_PROGRESS_MAP = {
        "characters": "0 / 0",
        "stories": "0 / 0",
        "cg": "0 / 0",
        "music": "0 / 0",
        "minigames": "0 / 0",
        "extras": "0 / 0",
    }

    def library_category_is_unlocked(category_id):
        return True


    def library_get_progress_text(category_id):
        if category_id == "stories" and "get_story_library_progress_text" in globals():
            return get_story_library_progress_text()
        if category_id == "extras":
            unlocked = len(persistent.unlocked_secrets) if hasattr(persistent, "unlocked_secrets") and persistent.unlocked_secrets else 0
            if unlocked:
                return "%d %s" % (unlocked, _("found"))
            return _("None found")
        return LIBRARY_PROGRESS_MAP.get(category_id, "")


    def library_get_category(category_id):
        for category in LIBRARY_CATEGORIES:
            if category["id"] == category_id:
                return category

        return None


    def ui_image_or_solid(path, color):
        if renpy.loadable(path):
            return path

        return Solid(color)


    def ui_frame_or_solid(path, color, border=24):
        if renpy.loadable(path):
            return Frame(path, border, border)

        return Solid(color)


    SECRET_DEFINITIONS = {
        "secret_prologue_seen": {
            "title": "First Dream",
            "description": "Witness the dream in the rain.",
            "icon": "★",
        },
        "secret_tam_interview": {
            "title": "New Beginning",
            "description": "Get through the first job interview.",
            "icon": "★",
        },
        "secret_first_date": {
            "title": "Sunday Date",
            "description": "Experience the Sunday date with Tâm.",
            "icon": "★",
        },
    }

    def ensure_secret_defaults():
        if not hasattr(persistent, "unlocked_secrets") or persistent.unlocked_secrets is None:
            persistent.unlocked_secrets = []
        elif not isinstance(persistent.unlocked_secrets, list):
            persistent.unlocked_secrets = list(persistent.unlocked_secrets)

    ensure_secret_defaults()

    def unlock_secret(secret_id):
        ensure_secret_defaults()
        if secret_id in persistent.unlocked_secrets:
            return False
        persistent.unlocked_secrets.append(secret_id)
        renpy.save_persistent()
        secret = SECRET_DEFINITIONS.get(secret_id)
        if secret:
            renpy.notify(_("Secret found: %s") % secret.get("title", secret_id))
        return True

    def has_unlocked_secret(secret_id):
        ensure_secret_defaults()
        return secret_id in persistent.unlocked_secrets

    def get_unlocked_secrets():
        ensure_secret_defaults()
        results = []
        for secret_id in SECRET_DEFINITIONS:
            if secret_id in persistent.unlocked_secrets:
                results.append((secret_id, SECRET_DEFINITIONS[secret_id]))
        return results

    def get_unlocked_secret_count():
        ensure_secret_defaults()
        return len(persistent.unlocked_secrets)
