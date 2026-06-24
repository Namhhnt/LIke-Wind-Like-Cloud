# FILE: game/story_state.rpy
# Purpose: MVP-only route state, score helpers, relationship locks, and ending support helpers.
# This file is intentionally generic and safe to expand later.

# Core relation state.
default story_state = {
    "minh_yuuka_relation": "unknown",        # unknown | old_close_friends | ex_lovers_long_separated | still_lovers
    "minh_romance_lock": False,
    "yuuka_romance_lock": False,

    "doom_score": 0,

    # Tâm
    "tam_hoang_interest": 0,
    "tam_minh_drawn": 0,
    "tam_self_clarity": 0,
    "tam_respect_yuuka": 0,
    "tam_insecurity": 0,
    "tam_observation": 0,
    "career_tam": 0,

    # Hoàng
    "hoang_tam_trust": 0,
    "hoang_huyen_interest": 0,
    "hoang_insecurity": 0,
    "hoang_self_acceptance": 0,
    "hoang_professional_credit": 0,

    # Huyền
    "huyen_quan_trust": 0,
    "huyen_hoang_interest": 0,
    "career_huyen": 0,

    # Thiên An
    "thienan_quang_trust": 0,
    "thienan_minh_residue": 0,
    "family_pressure_thienan": 0,
    "thienan_self_assertion": 0,

    # Minh-Yuuka
    "minh_yuuka_trust": 0,
    "minh_yuuka_intimacy": 0,
    "minh_yuuka_unresolved": 0,
    "old_friend_score": 0,
    "ex_lover_score": 0,
    "still_lover_score": 0,
    "romantic_score": 0,
    "boundary_score": 0,

    # Ending nudges selected in late-game chapters.
    "ending_support": [],
}

default story_flags = []
default story_completed_chapters = []

init python:
    def add_unique(target_list, value):
        if value not in target_list:
            target_list.append(value)

    def remove_value(target_list, value):
        if value in target_list:
            target_list.remove(value)

    def story_add(key, amount=1):
        story_state[key] = story_state.get(key, 0) + amount

    def story_set(key, value):
        story_state[key] = value

    def story_flag(flag):
        add_unique(story_flags, flag)

    def story_unflag(flag):
        remove_value(story_flags, flag)

    def story_has_flag(flag):
        return flag in story_flags

    def story_add_direction(character, direction):
        story_flag("direction_%s_%s" % (character, direction))

    def story_has_direction(character, direction):
        return story_has_flag("direction_%s_%s" % (character, direction))

    def story_add_ending_support(ending_id):
        add_unique(story_state["ending_support"], ending_id)

    def story_has_ending_support(ending_id):
        return ending_id in story_state.get("ending_support", [])

    def story_relation_is(value):
        return story_state.get("minh_yuuka_relation") == value

    def lock_minh_romance_except_yuuka():
        story_state["minh_romance_lock"] = True
        story_flag("lock_minh_romance_except_yuuka")
        story_flag("blocked_tam_minh_commit")
        story_flag("blocked_thienan_minh_commit")

    def lock_yuuka_romance_except_minh():
        story_state["yuuka_romance_lock"] = True
        story_flag("lock_yuuka_romance_except_minh")
        story_flag("blocked_yuuka_single_true")

    def story_set_minyuu_relation(relation):
        story_state["minh_yuuka_relation"] = relation

        if relation == "old_close_friends":
            story_state["minh_romance_lock"] = False
            story_state["yuuka_romance_lock"] = False
            story_add_direction("minh", "minh_yuuka_old_friends")
            story_add_direction("yuuka", "yuuka_minh_old_friends")

        elif relation == "ex_lovers_long_separated":
            lock_minh_romance_except_yuuka()
            story_add_direction("minh", "minh_yuuka_ex_lovers")
            story_add_direction("yuuka", "yuuka_minh_ex_lovers")

        elif relation == "still_lovers":
            lock_minh_romance_except_yuuka()
            lock_yuuka_romance_except_minh()
            story_add_direction("minh", "minh_yuuka_still_lovers")
            story_add_direction("yuuka", "yuuka_minh_still_lovers")

    def story_complete_chapter(chapter_id):
        # Adapter: use the project's real complete_chapter() if it exists.
        real_complete = globals().get("complete_chapter", None)
        if callable(real_complete):
            real_complete(chapter_id)
        else:
            add_unique(story_completed_chapters, chapter_id)

    def story_chapter_done(chapter_id):
        # Adapter: support both this MVP fallback and the existing progression data if available.
        if chapter_id in story_completed_chapters:
            return True
        progress = globals().get("progress", None)
        if isinstance(progress, dict):
            completed = progress.get("completed_chapters", [])
            return chapter_id in completed
        return False

