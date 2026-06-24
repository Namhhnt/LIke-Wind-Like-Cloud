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
