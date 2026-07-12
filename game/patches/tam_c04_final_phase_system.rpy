# FILE: game/patches/tam_c04_final_phase_system.rpy
# Route-breakthrough helpers for the final three months of Chapter 04.

init -10 python:
    if not globals().get("anhni"):
        anhni = Character("Ánh Nhi")

init 130 python:

    def tam_c04_hoang_breakthrough_ready():
        return (
            story_state.get("tam_hoang_interest", 0) >= 70
            and story_state.get("hoang_tam_trust", 0) >= 65
            and (
                story_has_flag("tam_c04_m03_hoang_mutual_habit")
                or story_has_flag("tam_c04_m03_hoang_needs_clarity")
                or story_has_flag("tam_c04_m04_hoang_ready")
            )
        )

    def tam_c04_quang_tam_breakthrough_ready():
        tam_c04_ensure_extended_story_state()
        return (
            story_state.get("tam_quang_interest", 0) >= 35
            and story_state.get("quang_tam_warmth", 0) >= 60
            and story_state.get("quang_tam_awareness", 0) >= 30
            and not story_has_flag("tam_c04_quang_thienan_committed")
        )

    def tam_c04_quang_thienan_breakthrough_ready():
        tam_c04_ensure_extended_story_state()
        return (
            story_state.get("thienan_quang_trust", 0) >= 70
            and story_state.get("quang_thienan_resolve", 0) >= 70
            and not story_has_flag("tam_c04_tam_quang_confirmed")
        )

    def tam_c04_huyen_quan_deep_trust_ready():
        active_lane_fn = globals().get("tam_c04_huyen_quan_active_lane_ready")
        active_lane = active_lane_fn() if callable(active_lane_fn) else (
            story_state.get("huyen_quan_interest", 0) >= 25
        )
        return (
            story_state.get("huyen_quan_trust", 0) >= 60
            and active_lane
        )

    def tam_c04_lock_tam_romance(route_id):
        route_id = str(route_id)
        if story_has_flag("tam_c04_tam_romance_locked"):
            if route_id == "hoang" and story_has_flag("tam_c04_tam_hoang_dating"):
                return True
            if route_id == "quang" and story_has_flag("tam_c04_tam_quang_confirmed"):
                return True
            if route_id == "independent" and story_has_flag("tam_c04_tam_independent"):
                return True
            return False

        story_flag("tam_c04_tam_romance_locked")
        story_flag("tam_c04_tam_route_{}".format(route_id))

        if route_id == "hoang":
            story_flag("tam_c04_tam_hoang_dating")
            story_flag("tam_hoang_romance_confirmed")
            story_add_direction("tam", "tam_hoang_commit")
            story_add_direction("hoang", "hoang_tam_pursue")
            relationship_set_phase("tam_hoang", "dating")
        elif route_id == "quang":
            story_flag("tam_c04_tam_quang_confirmed")
            story_flag("tam_quang_romance_confirmed")
            story_add_direction("tam", "tam_quang_commit")
            story_add_direction("quang", "quang_tam_commit")
            relationship_set_phase("tam_quang", "feelings_confirmed")
        else:
            story_flag("tam_c04_tam_independent")
            story_add_direction("tam", "tam_career_focus")
            relationship_set_phase("tam_independent", "chosen")
        return True

    def tam_c04_commit_quang_thienan():
        if story_has_flag("tam_c04_tam_quang_confirmed"):
            return False
        story_flag("tam_c04_quang_thienan_committed")
        story_flag("quang_thienan_romance_confirmed")
        story_add_direction("quang", "quang_thienan_commit")
        story_add_direction("thienan", "thienan_quang_commit")
        relationship_set_phase("quang_thienan", "closer")
        return True

    def tam_c04_commit_huyen_quan_deep_trust():
        story_flag("tam_c04_huyen_quan_deep_trust")
        story_add_direction("huyen", "huyen_quan_deep_trust")
        story_add_direction("quan", "quan_huyen_family_trust")
        relationship_set_phase("huyen_quan", "deep_trust")
        return True

    def tam_c04_seed_huyen_hoang_if_eligible():
        # Compatibility helper for older scene calls. The monthly resolver now
        # owns growth; this helper only records final availability.
        if story_has_flag("tam_c04_tam_hoang_dating"):
            return False

        finalize_fn = globals().get("tam_c04_finalize_huyen_lane_flags")
        if callable(finalize_fn):
            finalize_fn()
            return story_has_flag("tam_c04_huyen_hoang_future_open")

        return False
