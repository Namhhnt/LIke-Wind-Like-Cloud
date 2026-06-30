# The script of the game goes in this file.

define e = Character("Eileen")


default progression_autosave_slot = "_progression_auto"
default next_story_map_context_id = None


init -1 python:
    def has_progression_autosave():
        return renpy.can_load(progression_autosave_slot)


    def autosave_progression_at_map(context_id="act1_default"):
        initialize_progression()
        save_title = "Map Hub"

        context = globals().get("MAP_CONTEXTS", {}).get(context_id, None)
        if isinstance(context, dict):
            save_title = context.get("title", save_title)

        renpy.save(
            progression_autosave_slot,
            extra_info=save_title,
            include_screenshot=False,
        )


    def clear_progression_autosave():
        if renpy.can_load(progression_autosave_slot):
            renpy.unlink_save(progression_autosave_slot)


    def reset_progression_for_new_game():
        global progress, next_story_map_context_id

        clear_progression_autosave()

        if callable(globals().get("normalize_persistent_progression_state", None)):
            normalize_persistent_progression_state()

        persistent.unlocked_chapters = []
        persistent.timeline_bookmarks = []

        if callable(globals().get("make_progress_state", None)):
            progress = make_progress_state()

        next_story_map_context_id = None

        renpy.block_rollback()

label start:
    $ initialize_progression()
    jump route_map


label new_game_overwrite:
    $ reset_progression_for_new_game()
    jump start


label after_load:
    $ initialize_progression()
    $ refresh_validation_state()
    return
