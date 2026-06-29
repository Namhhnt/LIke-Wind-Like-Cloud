# FILE: game/data/library_music_data.rpy
# Purpose: Library Music Room tracks scanned from game/audio/music with chapter unlock gates.

default persistent.library_music_playing_id = None

init -1 python:
    import os
    import re

    MUSIC_FOLDER = "audio/music"

    # Map each filename in game/audio/music to the chapter that unlocks it on first completion.
    MUSIC_CHAPTER_BY_FILENAME = {
        "108 Nights The Sky Remembers.mp3": "yuuka_c18c_long_distance_interlude",
        "Between the Frames.mp3": "fb_minyuu_01_first_frame",
        "Calling For My Hand.mp3": "hoang_h01_brother_house",
        "Con Vẫn Đang Lớn.mp3": "tam_c03_thienan_family",
        "Couldnt Say Aloud.mp3": "fb_minyuu_04a_old_friends",
        "Finally Be Family.mp3": "group_c11_social_dinner",
        "I Refuse Your Sacrifice.mp3": "hoang_h05_shadow_of_minh",
        "Keep Going On.mp3": "tam_c01_interview_day",
        "Not a Glitch but a Feature.mp3": "work_c10_project_festival_overlap",
        "Only Exception.mp3": "tam_c20b_admiration_vs_love",
        "Seal on My Throat.mp3": "c19b_city_after_festival_ex_lovers",
        "Still Holding Hands.mp3": "tam_c05_sunday_date",
        "THE WORLD IS WEIRD But Im Awake.mp3": "yuuka_c08_festival_arrival",
        "The Habit of You.mp3": "yuuka_c18b_habit_of_you",
        "The Loop We Are.mp3": "fb_minyuu_02_working_rhythm",
        "Unsent Letter JP Full ver.mp3": "fb_minyuu_03_door_left_open",
        "When Nothing Happens.mp3": "prologue_rain_dream",
        "夜が朝にほどけるまで.mp3": "yuuka_c09_yuukas_work",
    }

    def music_slug_from_filename(filename):
        base_name = os.path.splitext(filename)[0]
        slug = re.sub(r"[^a-z0-9]+", "_", base_name.strip().lower())
        slug = slug.strip("_")
        return slug or "track"

    def music_title_from_filename(filename):
        return os.path.splitext(filename)[0].strip()

    def music_chapter_order(chapter_id):
        chapter_order = globals().get("CHAPTER_ORDER", [])
        try:
            return chapter_order.index(chapter_id)
        except ValueError:
            return 9999

    def list_music_folder_files():
        files = set()
        music_dir = story_library_game_path(MUSIC_FOLDER)
        if music_dir and os.path.isdir(music_dir):
            for filename in os.listdir(music_dir):
                if filename.lower().endswith(".mp3"):
                    files.add(filename)

        prefix = MUSIC_FOLDER.rstrip("/") + "/"
        for path in renpy.list_files():
            normalized = path.replace("\\", "/")
            if normalized.startswith(prefix) and normalized.lower().endswith(".mp3"):
                files.add(os.path.basename(normalized))

        return sorted(files, key=lambda name: (music_chapter_order(MUSIC_CHAPTER_BY_FILENAME.get(name, "")), name.lower()))

    def build_music_library_item(filename):
        chapter_id = MUSIC_CHAPTER_BY_FILENAME.get(filename)
        if not chapter_id:
            return None

        track_path = "%s/%s" % (MUSIC_FOLDER, filename)
        if not renpy.loadable(track_path):
            return None

        slug = music_slug_from_filename(filename)
        return {
            "id": "music_%s" % slug,
            "title": music_title_from_filename(filename),
            "category": "music",
            "series": _("Original Soundtrack"),
            "type": "music_track",
            "size": "small",
            "point_cost": 0,
            "unlock_mode": "free",
            "prerequisites": [chapter_id],
            "tags": ["music", "ost", chapter_id],
            "cover": "",
            "file": track_path,
            "order": music_chapter_order(chapter_id),
        }

    def refresh_music_library_registry():
        ensure_story_library_defaults()
        for key in list(library_items.keys()):
            if library_items[key].get("category") == "music":
                del library_items[key]

        for filename in list_music_folder_files():
            item = build_music_library_item(filename)
            if item:
                register_library_item(item)

    def ensure_music_library_registered(force=False):
        ensure_story_library_loaded()

        has_music_items = False
        for item in library_items.values():
            if item.get("category") == "music":
                has_music_items = True
                break

        if force or not has_music_items:
            refresh_music_library_registry()

    def get_music_library_items():
        ensure_music_library_registered()
        items = [item for item in library_items.values() if item.get("category") == "music"]
        items.sort(key=lambda item: (item.get("order", 9999), item.get("title", "")))
        return items

    def get_music_library_progress_text():
        items = get_music_library_items()
        if not items:
            return "0 / 0"

        unlocked = 0
        for item in items:
            if is_library_content_unlocked(item["id"]):
                unlocked += 1

        return "%d / %d" % (unlocked, len(items))

    def play_library_music_track(content_id):
        ensure_music_library_registered()
        item = get_library_item(content_id)
        if not item or item.get("category") != "music":
            return

        if not is_library_content_unlocked(content_id):
            return

        track_path = item.get("file")
        if not track_path or not renpy.loadable(track_path):
            return

        renpy.music.play(track_path, channel="music", loop=True)
        persistent.library_music_playing_id = content_id
        renpy.save_persistent()

    def stop_library_music_preview():
        renpy.music.stop(channel="music", fadeout=0.5)
        persistent.library_music_playing_id = None
        renpy.save_persistent()

        if renpy.loadable("audio/bgm.mp3"):
            renpy.music.play("audio/bgm.mp3", channel="music", loop=True, fadein=0.5)

    def is_library_music_playing(content_id):
        if persistent.library_music_playing_id != content_id:
            return False
        return renpy.music.get_playing(channel="music") is not None

    def resume_game_bgm():
        if renpy.music.get_playing(channel="music"):
            return

        if renpy.loadable("audio/bgm.mp3"):
            renpy.music.play("audio/bgm.mp3", channel="music", loop=True, fadein=0.5)


init 1 python:
    refresh_music_library_registry()
