# FILE: game/story_state.rpy
# Purpose: Route state, 0-100 score helpers, relationship locks, and ending support helpers.
# Scores are normalized to 0-100. Higher is better unless the score name explicitly means pressure, insecurity, unresolved tension, or boundary distance.

# Core relation state.
default story_state = {
    "minh_yuuka_relation": "unknown",        # unknown | old_close_friends | ex_lovers_long_separated | still_lovers
    "minh_romance_lock": False,
    "yuuka_romance_lock": False,

    # 0 = safe / stable, 100 = tragedy pressure is overwhelming.
    "doom_score": 0,

    # Tâm — baseline reflects early-route emotional position, not final eligibility.
    "tam_hoang_interest": 35,
    "tam_quang_interest": 0,
    "tam_quan_interest": 0,
    "tam_minh_drawn": 5,
    "tam_self_clarity": 20,
    "tam_respect_yuuka": 0,
    "tam_insecurity": 35,
    "tam_observation": 20,
    "career_tam": 15,

    # Hoàng
    "hoang_tam_trust": 35,
    "hoang_huyen_interest": 5,
    "hoang_insecurity": 30,
    "hoang_self_acceptance": 35,
    "hoang_professional_credit": 30,

    # Huyền
    "huyen_quan_trust": 10,
    "huyen_quan_interest": 5,
    "huyen_hoang_interest": 10,
    "career_huyen": 15,

    # Thiên An — family pressure and Minh residue start high, then can decrease through choices.
    "thienan_quang_trust": 35,
    "thienan_minh_residue": 65,
    "family_pressure_thienan": 70,
    "thienan_self_assertion": 35,
    "quang_persistence": 60,

    # Minh-Yuuka shared flashback arc.
    # Trust / intimacy / branch scores grow upward; unresolved and boundary should be reduced.
    "minh_yuuka_trust": 0,
    "minh_yuuka_intimacy": 0,
    "minh_yuuka_unresolved": 55,
    "old_friend_score": 0,
    "ex_lover_score": 0,
    "still_lover_score": 0,
    "romantic_score": 0,
    "boundary_score": 50,

    # Ending nudges selected in late-game chapters.
    "ending_support": [],
}

default story_flags = []
default story_completed_chapters = []

init python:
    STORY_SCORE_MIN = 0
    STORY_SCORE_MAX = 100

    STORY_SCORE_KEYS = set([
        "doom_score",
        "tam_hoang_interest", "tam_quang_interest", "tam_quan_interest", "tam_minh_drawn",
        "tam_self_clarity", "tam_respect_yuuka", "tam_insecurity", "tam_observation", "career_tam",
        "hoang_tam_trust", "hoang_huyen_interest", "hoang_insecurity", "hoang_self_acceptance", "hoang_professional_credit",
        "huyen_quan_trust", "huyen_quan_interest", "huyen_hoang_interest", "career_huyen",
        "thienan_quang_trust", "thienan_minh_residue", "family_pressure_thienan", "thienan_self_assertion",
        "quang_persistance", "quang_persistence",
        "minh_yuuka_trust", "minh_yuuka_intimacy", "minh_yuuka_unresolved",
        "old_friend_score", "ex_lover_score", "still_lover_score", "romantic_score", "boundary_score",
    ])

    def clamp_story_score(value):
        try:
            numeric_value = int(value)
        except Exception:
            numeric_value = STORY_SCORE_MIN
        return max(STORY_SCORE_MIN, min(STORY_SCORE_MAX, numeric_value))

    def add_unique(target_list, value):
        if value not in target_list:
            target_list.append(value)

    def remove_value(target_list, value):
        if value in target_list:
            target_list.remove(value)

    def story_get_score(key, default=0):
        return clamp_story_score(story_state.get(key, default))

    def story_add(key, amount=1):
        if key in STORY_SCORE_KEYS:
            story_state[key] = clamp_story_score(story_state.get(key, 0) + amount)
        else:
            story_state[key] = story_state.get(key, 0) + amount

    def story_sub(key, amount=1):
        story_add(key, -amount)

    def story_set(key, value):
        if key in STORY_SCORE_KEYS:
            story_state[key] = clamp_story_score(value)
        else:
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

    def unlock_minh_romance_after_yuuka():
        story_state["minh_romance_lock"] = False
        story_unflag("lock_minh_romance_except_yuuka")
        story_unflag("blocked_tam_minh_commit")
        story_unflag("blocked_thienan_minh_commit")
        story_flag("minh_romance_open_after_yuuka")

    def lock_yuuka_romance_except_minh():
        story_state["yuuka_romance_lock"] = True
        story_flag("lock_yuuka_romance_except_minh")
        story_flag("blocked_yuuka_single_true")

    def unlock_yuuka_romance_after_minh():
        story_state["yuuka_romance_lock"] = False
        story_unflag("lock_yuuka_romance_except_minh")
        story_unflag("blocked_yuuka_single_true")

    def story_set_minyuu_relation(relation):
        story_state["minh_yuuka_relation"] = relation

        if relation == "old_close_friends":
            unlock_minh_romance_after_yuuka()
            unlock_yuuka_romance_after_minh()
            story_add_direction("minh", "minh_yuuka_old_friends")
            story_add_direction("yuuka", "yuuka_minh_old_friends")

        elif relation == "ex_lovers_long_separated":
            lock_minh_romance_except_yuuka()
            unlock_yuuka_romance_after_minh()
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
