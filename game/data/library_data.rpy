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
        if category_id == "characters":
            unlocked = get_unlocked_character_count()
            total = len(CHARACTER_PROFILES)
            return "%d / %d" % (unlocked, total)
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


    CHARACTER_PROFILES = [
        {
            "id": "tam",
            "name": "Tâm",
            "route": "tam",
            "sprite": "side tam neutral",
            "description": "The protagonist. A young woman navigating her career, relationships, and self-discovery in the city.",
            "tags": ["protagonist", "main"],
        },
        {
            "id": "hoang",
            "name": "Hoàng",
            "route": "hoang",
            "sprite": "side hoang neutral",
            "description": "A calm and observant man, connected to Minh by family. His quiet presence leaves a strong impression.",
            "tags": ["route", "main"],
        },
        {
            "id": "yuuka",
            "name": "Yuuka",
            "route": "yuuka",
            "sprite": "side yuuka neutral",
            "description": "A young Japanese film director whose arrival stirs old memories and new connections.",
            "tags": ["route", "main"],
        },
        {
            "id": "minh",
            "name": "Minh",
            "route": "minh",
            "sprite": "side minh neutral",
            "description": "A figure from the past whose return reopens questions of love, friendship, and closure.",
            "tags": ["route", "main"],
        },
        {
            "id": "thienan",
            "name": "Thiên An",
            "route": "thienan",
            "sprite": "side thienan neutral",
            "description": "A grounded presence with her own struggles. Her story weaves through family pressure and self-assertion.",
            "tags": ["route", "main"],
        },
        {
            "id": "huyen",
            "name": "Huyền",
            "route": "huyen",
            "sprite": "side huyen neutral",
            "description": "Tâm's close friend. She balances her own ambitions and relationships while staying by Tâm's side.",
            "tags": ["route", "main"],
        },
        {
            "id": "quan",
            "name": "Quân",
            "route": None,
            "sprite": "side quan neutral",
            "description": "A colleague and friend. His warmth and reliability make him a steady presence at work and beyond.",
            "tags": ["supporting"],
        },
    ]


    def is_character_unlocked(profile):
        if profile.get("route") is None:
            return True

        route_id = profile["route"]
        if not hasattr(persistent, "unlocked_chapters") or not isinstance(persistent.unlocked_chapters, list):
            return False

        for chapter_id in persistent.unlocked_chapters:
            chapter = globals().get("CHAPTERS", {}).get(chapter_id)
            if chapter and chapter.get("route") == route_id:
                return True

        return False


    def get_unlocked_character_count():
        count = 0
        for profile in CHARACTER_PROFILES:
            if is_character_unlocked(profile):
                count += 1
        return count
