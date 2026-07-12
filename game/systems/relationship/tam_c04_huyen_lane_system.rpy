# FILE: game/systems/relationship/tam_c04_huyen_lane_system.rpy
# Chapter 04 monthly resolver for Huyền–Hoàng and Huyền–Quân.
#
# Design rules:
# - Huyền–Hoàng is the default off-screen personal lane when Tâm does not
#   actively create space for Huyền–Quân.
# - Huyền–Quân can still gain professional trust in every route. Personal
#   interest grows mainly when the player repeatedly pushes that lane.
# - Both lanes may coexist. Chapter 04 never commits Huyền–Hoàng romance.
# - Tâm dating Hoàng closes romantic Huyền–Hoàng growth cleanly.

init 132 python:

    TAM_C04_HUYEN_LANE_RULES = {
        "early": {
            0: {"hh": 5, "hq_trust": 2, "hq_interest": 0},
            1: {"hh": 3, "hq_trust": 4, "hq_interest": 2},
            2: {"hh": 1, "hq_trust": 6, "hq_interest": 4},
        },
        "late": {
            0: {"hh": 7, "hq_trust": 2, "hq_interest": 0},
            1: {"hh": 4, "hq_trust": 5, "hq_interest": 3},
            2: {"hh": 2, "hq_trust": 8, "hq_interest": 6},
        },
    }

    # Each tuple is one weekly opportunity. Multiple flags inside one tuple
    # represent variants of the same push and count only once.
    TAM_C04_HUYEN_QUAN_PUSH_EVENTS = {
        "m01": [
            (1, ["tam_c04_w01_first_focus_huyen_quan", "tam_c04_w01_tam_steps_back_from_huyen_quan", "tam_c04_w01_huyen_faces_quan_directly"]),
            (1, ["tam_c04_w02_focus_huyen_quan", "tam_c04_w02_huyen_answers_quan_rehearsal"]),
            (1, ["tam_c04_w03_focus_huyen_quan", "tam_c04_w03_tam_teases_huyen_quan_standard"]),
            (1, ["tam_c04_w04_focus_huyen_quan", "tam_c04_w04_tam_asks_huyen_about_quan_trust"]),
        ],
        "m02": [
            (1, ["tam_c04_w05_focus_huyen_quan"]),
            (1, ["tam_c04_w06_focus_huyen_quan", "tam_c04_w06_tam_says_huyen_knows_quan_review"]),
            (1, ["tam_c04_w07_focus_huyen_quan", "tam_c04_w07_tam_leaves_huyen_quan_agreement", "tam_c04_w07_tam_asks_huyen_quan_listened"]),
            (1, ["tam_c04_w08_focus_huyen_quan", "tam_c04_w08_tam_leaves_huyen_quan_alone"]),
        ],
        "m03": [
            (1, ["tam_c04_w09_focus_huyen_quan", "tam_c04_w09_huyen_sends_without_quan_edit"]),
            (1, ["tam_c04_w10_focus_huyen_quan", "tam_c04_w10_tam_notices_huyen_notices_quan", "tam_c04_w10_huyen_sends_quan_to_eat"]),
            (1, ["tam_c04_w11_focus_huyen_quan", "tam_c04_w11_huyen_quietly_fixes_quan_error"]),
            (1, ["tam_c04_w12_focus_huyen_quan", "tam_c04_w12_tam_leaves_huyen_quan_after_review"]),
        ],
        "m04": [
            (1, ["tam_c04_w13_huyen_accepts_pickup", "tam_c04_w13_tam_asks_quan_trust"]),
            (1, ["tam_c04_w14_huyen_handles_anhni_alone", "tam_c04_w14_tam_learns_quan_home"]),
            (1, ["tam_c04_w15_anhni_stays_huyen_home", "tam_c04_w15_anhni_says_missing_quan"]),
            (1, ["tam_c04_w16_priority_huyen_quan_deep", "tam_c04_w16_huyen_pours_quan_water"]),
        ],
        "m05": [
            (1, ["tam_c04_w17_huyen_keeps_quan_key", "tam_c04_w17_huyen_key_for_trips_only"]),
            (1, ["tam_c04_w19_huyen_builds_bridge_with_anhni", "tam_c04_w19_tam_pushes_quan_home"]),
            (2, ["tam_c04_w20_huyen_accepts_deep_trust"]),
        ],
        "m06": [
            (2, ["tam_c04_w21_huyen_accepts_anhni_ten_days", "tam_c04_w21_huyen_sets_quan_call_rule"]),
            (1, ["tam_c04_w22_huyen_says_quan_reliable"]),
            (1, ["tam_c04_w23_huyen_keeps_quan_lane"]),
            (1, ["tam_c04_final_huyen_quan_home_trust"]),
        ],
    }

    def tam_c04_get_huyen_quan_push_score(month_id):
        month_id = str(month_id)
        score = 0
        for weight, flags in TAM_C04_HUYEN_QUAN_PUSH_EVENTS.get(month_id, []):
            if any(story_has_flag(flag_id) for flag_id in flags):
                score += int(weight)
        return score

    def tam_c04_get_total_huyen_quan_push_score():
        return sum(
            tam_c04_get_huyen_quan_push_score(month_id)
            for month_id in ("m01", "m02", "m03", "m04", "m05", "m06")
        )

    def tam_c04_huyen_quan_active_lane_ready():
        return (
            tam_c04_get_total_huyen_quan_push_score() >= 4
            or story_state.get("huyen_quan_interest", 0) >= 25
        )

    def tam_c04_resolve_huyen_lanes(month_id, phase="early"):
        tam_c04_ensure_extended_story_state()
        month_id = str(month_id)
        phase = str(phase)
        resolved_flag = "tam_c04_{}_huyen_lanes_resolved".format(month_id)

        if story_has_flag(resolved_flag):
            return False

        if phase not in TAM_C04_HUYEN_LANE_RULES:
            raise ValueError("Unknown Huyền lane phase: {}".format(phase))

        push_score = tam_c04_get_huyen_quan_push_score(month_id)
        push_level = min(2, push_score)
        rule = TAM_C04_HUYEN_LANE_RULES[phase][push_level]

        # Professional familiarity may grow in either lane. Personal interest
        # toward Quân requires visible player investment.
        story_add("huyen_quan_trust", rule["hq_trust"])
        story_add("huyen_quan_interest", rule["hq_interest"])

        hh_gain = int(rule["hh"])

        if story_has_flag("tam_c04_tam_hoang_dating"):
            hh_gain = 0
            story_flag("tam_c04_{}_huyen_hoang_closed_by_tam_dating".format(month_id))
        else:
            # Before Tâm answers Hoàng, he keeps an intentional distance from
            # Huyền if the Tâm–Hoàng lane is already strong. The missed growth
            # can catch up after Week 18 if Tâm chooses someone else.
            tam_hoang_pending = (
                not story_has_flag("tam_c04_tam_romance_locked")
                and story_state.get("tam_hoang_interest", 0) >= 70
                and story_state.get("hoang_tam_trust", 0) >= 65
            )
            if tam_hoang_pending and hh_gain > 1:
                hh_gain = 1
                story_flag("tam_c04_huyen_hoang_deferred_by_tam_hoang")

        if hh_gain > 0:
            tam_c04_add_extended_score("huyen_hoang_interest", hh_gain)
            tam_c04_add_extended_score("hoang_huyen_interest", hh_gain)

        if push_level == 0:
            story_flag("tam_c04_{}_huyen_hoang_default_growth".format(month_id))
        elif push_level == 1:
            story_flag("tam_c04_{}_huyen_relationships_mixed".format(month_id))
        else:
            story_flag("tam_c04_{}_huyen_quan_active_growth".format(month_id))

        story_flag(resolved_flag)
        return True

    def tam_c04_resolve_huyen_lane_after_tam_choice():
        if story_has_flag("tam_c04_huyen_lane_post_choice_resolved"):
            return False

        if story_has_flag("tam_c04_tam_hoang_dating"):
            story_flag("tam_c04_huyen_hoang_romance_closed")
        elif story_has_flag("tam_c04_huyen_hoang_deferred_by_tam_hoang"):
            tam_c04_add_extended_score("huyen_hoang_interest", 6)
            tam_c04_add_extended_score("hoang_huyen_interest", 6)
            story_flag("tam_c04_huyen_hoang_catchup_after_tam_choice")

        story_flag("tam_c04_huyen_lane_post_choice_resolved")
        return True

    def tam_c04_finalize_huyen_lane_flags():
        tam_c04_ensure_extended_story_state()

        hh_huyen = int(story_state.get("huyen_hoang_interest", 0) or 0)
        hh_hoang = int(story_state.get("hoang_huyen_interest", 0) or 0)

        if not story_has_flag("tam_c04_tam_hoang_dating"):
            if hh_huyen >= 25 and hh_hoang >= 25:
                story_flag("tam_c04_huyen_hoang_future_open")
                story_flag("tam_c04_huyen_hoang_future_seed")
                story_add_direction("huyen", "huyen_hoang_open")
                story_add_direction("hoang", "hoang_huyen_open")
            elif hh_huyen >= 12 and hh_hoang >= 12:
                story_flag("tam_c04_huyen_hoang_interest_developing")

        if (
            story_state.get("huyen_quan_trust", 0) >= 60
            and tam_c04_huyen_quan_active_lane_ready()
        ):
            story_flag("tam_c04_huyen_quan_deep_trust_available")

        if story_state.get("huyen_quan_interest", 0) >= 25:
            story_flag("tam_c04_huyen_quan_personal_seed")

        return True

    def tam_c04_migrate_huyen_lane_resolution():
        """Backfill monthly lane results for saves made before v2.0."""
        month_map = [
            ("m01", "tam_c04_month_01_completed", "early"),
            ("m02", "tam_c04_month_02_completed", "early"),
            ("m03", "tam_c04_month_03_completed", "early"),
            ("m04", "tam_c04_month_04_completed", "late"),
            ("m05", "tam_c04_month_05_completed", "late"),
            ("m06", "tam_c04_month_06_completed", "late"),
        ]

        for month_id, completed_flag, phase in month_map:
            if (
                story_has_flag(completed_flag)
                and not story_has_flag(
                    "tam_c04_{}_huyen_lanes_resolved".format(month_id)
                )
            ):
                tam_c04_resolve_huyen_lanes(month_id, phase=phase)

        if (
            story_has_flag("tam_c04_w18_completed")
            and story_has_flag("tam_c04_tam_romance_locked")
            and not story_has_flag("tam_c04_huyen_lane_post_choice_resolved")
        ):
            tam_c04_resolve_huyen_lane_after_tam_choice()

        if story_has_flag("tam_c04_w24_completed"):
            tam_c04_finalize_huyen_lane_flags()

        return True

