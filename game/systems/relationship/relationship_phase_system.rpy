# FILE: game/systems/relationship/relationship_phase_system.rpy
# Reusable relationship phase and contact-maintenance runtime.
#
# A relationship can move from courtship to dating/confirmed phases. Once the
# pair has entered a committed phase, authored checkpoints may record whether
# meaningful contact was maintained. Missing contact can then reduce trust or
# interest instead of relationships increasing forever without maintenance.

init 120 python:

    RELATIONSHIP_MAINTENANCE_RULES = {
        "tam_hoang": {
            "maintained": {
                "tam_hoang_interest": 1,
                "hoang_tam_trust": 2,
            },
            "missed": {
                "tam_hoang_interest": -2,
                "hoang_tam_trust": -4,
                "tam_insecurity": 2,
            },
        },
    }

    def _relationship_phase_state():
        progress_state = globals().get("progress")
        if isinstance(progress_state, dict):
            return progress_state.setdefault("relationship_phase_state", {})

        runtime_state = globals().get("_relationship_phase_runtime")
        if not isinstance(runtime_state, dict):
            runtime_state = {}
            globals()["_relationship_phase_runtime"] = runtime_state
        return runtime_state

    def relationship_get_record(pair_id):
        state = _relationship_phase_state()
        return state.setdefault(str(pair_id), {
            "phase": "unconfirmed",
            "contacts": {},
            "resolved_periods": {},
        })

    def relationship_set_phase(pair_id, phase):
        pair_id = str(pair_id)
        phase = str(phase)
        record = relationship_get_record(pair_id)
        record["phase"] = phase

        flag_fn = globals().get("story_flag")
        if callable(flag_fn):
            flag_fn("relationship_{}_{}".format(pair_id, phase))
        return phase

    def relationship_get_phase(pair_id, default="unconfirmed"):
        return relationship_get_record(pair_id).get("phase", default)

    def relationship_mark_contact(pair_id, period_id, source="story"):
        pair_id = str(pair_id)
        period_id = str(period_id)
        record = relationship_get_record(pair_id)
        record.setdefault("contacts", {})[period_id] = str(source)

        flag_fn = globals().get("story_flag")
        if callable(flag_fn):
            flag_fn("relationship_{}_contact_{}".format(pair_id, period_id))
        return True

    def relationship_contact_was_maintained(pair_id, period_id):
        record = relationship_get_record(pair_id)
        return str(period_id) in record.setdefault("contacts", {})

    def _relationship_apply_score_delta(score_id, delta):
        delta = int(delta or 0)
        if delta == 0:
            return

        if delta > 0:
            add_fn = globals().get("story_add")
            if callable(add_fn):
                add_fn(score_id, delta)
            return

        sub_fn = globals().get("story_sub")
        if callable(sub_fn):
            sub_fn(score_id, abs(delta))
            return

        add_fn = globals().get("story_add")
        if callable(add_fn):
            add_fn(score_id, delta)

    def relationship_resolve_contact_period(pair_id, period_id):
        pair_id = str(pair_id)
        period_id = str(period_id)
        record = relationship_get_record(pair_id)
        resolved = record.setdefault("resolved_periods", {})
        if period_id in resolved:
            return resolved[period_id]

        maintained = relationship_contact_was_maintained(pair_id, period_id)
        result = "maintained" if maintained else "missed"
        rules = RELATIONSHIP_MAINTENANCE_RULES.get(pair_id, {})

        for score_id, delta in rules.get(result, {}).items():
            _relationship_apply_score_delta(score_id, delta)

        resolved[period_id] = result
        flag_fn = globals().get("story_flag")
        if callable(flag_fn):
            flag_fn("relationship_{}_{}_{}".format(pair_id, period_id, result))
        return result
