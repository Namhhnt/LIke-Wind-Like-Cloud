# FILE: game/patches/tam_c04_extended_route_state.rpy
# Extended Chapter 04 relationship state for Quang/Tam and Quang/Thien An.
#
# These scores separate:
# - Quang's long-established warmth toward Tam,
# - Quang's newer personal awareness of Tam,
# - Quang's route-specific resolve toward Thien An.

init 101 python:

    TAM_C04_EXTENDED_SCORE_DEFAULTS = {
        # Shared work rhythm between Tâm and Huyền.
        "tam_huyen_work_sync": 20,

        # Quang and Tam are already close before Chapter 04. This baseline is
        # familiar care, not romantic commitment.
        "quang_tam_warmth": 35,
        "quang_tam_awareness": 0,

        # Quang already cares about Thien An before this bridge chapter, but he
        # still tends to communicate through Tam instead of acting directly.
        "quang_thienan_resolve": 35,
    }

    def tam_c04_ensure_extended_story_state():
        state = globals().get("story_state")
        if not isinstance(state, dict):
            return False

        for key, default_value in TAM_C04_EXTENDED_SCORE_DEFAULTS.items():
            if key not in state:
                state[key] = default_value

        return True

    def tam_c04_add_extended_score(key, amount=1):
        tam_c04_ensure_extended_story_state()

        state = globals().get("story_state")
        if not isinstance(state, dict):
            raise Exception(
                "tam_c04_add_extended_score(): story_state is unavailable."
            )

        add_fn = globals().get("story_add")
        if callable(add_fn):
            try:
                add_fn(key, amount)
                return state.get(key, 0)
            except (KeyError, ValueError, TypeError):
                # Fall through for projects whose story_add validates keys
                # against a static registry that has not yet been extended.
                pass

        old_value = int(state.get(key, 0) or 0)
        new_value = max(0, min(100, old_value + int(amount)))
        state[key] = new_value

        notify_fn = globals().get("story_notify_state_change")
        if callable(notify_fn):
            try:
                notify_fn(key)
            except TypeError:
                notify_fn()

        return new_value
