init python:
    def pd_get_case(case_id=None):
        store = renpy.store
        active_case_id = case_id or store.pd_state.get("case_id")
        return PD_CASES.get(active_case_id, {})


    def pd_make_state(case_id):
        return {
            "case_id": case_id,
            "phase": 1,
            "selected_data_ids": [],
            "generated_insight_ids": [],
            "selected_card_id": None,
            "root_cause_slots": [],
            "impact_slots": [],
            "selected_action_id": None,
            "action_pic_pairs": {},
            "phase_1_score": 0,
            "phase_2_score": 0,
            "total_score": 0,
            "attempts_left": 3,
            "hints_left": 2,
            "feedback_message": "Read the data first, then group only the facts that truly belong together.",
            "created_insight_id": None,
        }


    def pd_prepare_case(case_id):
        store = renpy.store
        if case_id not in PD_CASES:
            raise Exception("Unknown problem diagnosis case: %s" % case_id)

        store.pd_state = pd_make_state(case_id)
        store.pd_last_result = None


    def pd_restart_interaction():
        renpy.restart_interaction()


    def pd_get_card(case_id, card_id):
        case = pd_get_case(case_id)

        for card in case.get("data_cards", []):
            if card["id"] == card_id:
                return card

        return case.get("insight_cards", {}).get(card_id)


    def pd_get_available_organize_cards():
        store = renpy.store
        case = pd_get_case()
        cards = list(case.get("data_cards", []))

        for insight_id in store.pd_state.get("generated_insight_ids", []):
            insight_card = case.get("insight_cards", {}).get(insight_id)
            if insight_card:
                cards.append(insight_card)

        return cards


    def pd_get_card_title(card_id):
        store = renpy.store
        card = pd_get_card(store.pd_state.get("case_id"), card_id)
        return card["title"] if card else card_id


    def pd_get_action_title(action_id):
        case = pd_get_case()
        for action in case.get("actions", []):
            if action["id"] == action_id:
                return action["title"]
        return action_id


    def pd_is_card_assigned(card_id):
        store = renpy.store
        return card_id in store.pd_state.get("root_cause_slots", []) or card_id in store.pd_state.get("impact_slots", [])


    def pd_clear_feedback(created_insight=False):
        store = renpy.store
        if not created_insight:
            store.pd_state["created_insight_id"] = None


    def pd_toggle_data_selection(card_id):
        store = renpy.store
        selected = store.pd_state["selected_data_ids"]
        pd_clear_feedback()

        if card_id in selected:
            selected.remove(card_id)
            store.pd_state["feedback_message"] = "Data point removed from the analysis stack."
            pd_restart_interaction()
            return

        if len(selected) >= PD_MAX_ANALYZE_SELECTION:
            store.pd_state["feedback_message"] = "Too many data points. Narrow the analysis."
            pd_restart_interaction()
            return

        selected.append(card_id)
        store.pd_state["feedback_message"] = "Data point added. Build a set of 2 to 4 related facts."
        pd_restart_interaction()


    def pd_analyze_selected():
        store = renpy.store
        case = pd_get_case()
        selected = set(store.pd_state["selected_data_ids"])
        pd_clear_feedback()

        if len(selected) < PD_MIN_ANALYZE_SELECTION:
            store.pd_state["feedback_message"] = "Select at least 2 related data cards before analyzing."
            pd_restart_interaction()
            return

        for recipe in case.get("analysis_recipes", []):
            if selected == set(recipe.get("requires", [])):
                insight_id = recipe["creates"]

                if insight_id not in store.pd_state["generated_insight_ids"]:
                    store.pd_state["generated_insight_ids"].append(insight_id)
                    store.pd_state["created_insight_id"] = insight_id
                    store.pd_state["feedback_message"] = recipe.get("success_feedback", "A useful insight was generated.")
                    store.pd_state["selected_data_ids"] = []
                else:
                    store.pd_state["feedback_message"] = "You already discovered this insight."

                pd_restart_interaction()
                return

        store.pd_state["feedback_message"] = "These facts are related, but they do not create a clear insight yet."
        pd_restart_interaction()


    def pd_select_organize_card(card_id):
        store = renpy.store
        pd_clear_feedback()

        if store.pd_state.get("selected_card_id") == card_id:
            store.pd_state["selected_card_id"] = None
            store.pd_state["feedback_message"] = "Card selection cleared."
        else:
            store.pd_state["selected_card_id"] = card_id
            store.pd_state["feedback_message"] = "Card ready. Place it into Root Cause or Impact."

        pd_restart_interaction()


    def pd_assign_selected_card(slot_name):
        store = renpy.store
        card_id = store.pd_state.get("selected_card_id")
        pd_clear_feedback()

        if not card_id:
            store.pd_state["feedback_message"] = "Select a raw fact or insight first."
            pd_restart_interaction()
            return

        target = store.pd_state[slot_name]

        if card_id in target:
            store.pd_state["feedback_message"] = "That card is already in this section."
            pd_restart_interaction()
            return

        current_slot_name = None
        for bucket_name in ("root_cause_slots", "impact_slots"):
            if card_id in store.pd_state[bucket_name]:
                current_slot_name = bucket_name
                break

        if len(target) >= PD_SLOT_LIMIT and current_slot_name != slot_name:
            store.pd_state["feedback_message"] = "That section is full. Remove something before assigning another card."
            pd_restart_interaction()
            return

        for bucket_name in ("root_cause_slots", "impact_slots"):
            bucket = store.pd_state[bucket_name]
            if card_id in bucket:
                bucket.remove(card_id)

        target.append(card_id)
        store.pd_state["selected_card_id"] = None
        store.pd_state["feedback_message"] = "Card assigned to %s." % ("Root Cause" if slot_name == "root_cause_slots" else "Impact")
        pd_restart_interaction()


    def pd_remove_from_slot(slot_name, card_id):
        store = renpy.store
        pd_clear_feedback()
        bucket = store.pd_state[slot_name]

        if card_id in bucket:
            bucket.remove(card_id)
            store.pd_state["feedback_message"] = "Card removed from %s." % ("Root Cause" if slot_name == "root_cause_slots" else "Impact")

        pd_restart_interaction()


    def pd_score_phase_1():
        store = renpy.store
        rules = pd_get_case().get("organize_rules", {})
        score = 0

        for card_id in store.pd_state["root_cause_slots"]:
            if card_id in rules.get("root_cause_best", []):
                score += 25
            elif card_id in rules.get("root_cause_accepted", []):
                score += 10
            elif card_id in rules.get("impact_best", []) or card_id in rules.get("impact_accepted", []):
                score -= 5
            elif card_id in rules.get("noise", []):
                score -= 10

        for card_id in store.pd_state["impact_slots"]:
            if card_id in rules.get("impact_best", []):
                score += 20
            elif card_id in rules.get("impact_accepted", []):
                score += 8
            elif card_id in rules.get("root_cause_best", []) or card_id in rules.get("root_cause_accepted", []):
                score -= 5
            elif card_id in rules.get("noise", []):
                score -= 10

        score += len(store.pd_state["generated_insight_ids"]) * 5
        store.pd_state["phase_1_score"] = max(0, min(score, 100))
        return store.pd_state["phase_1_score"]


    def pd_submit_phase_1():
        store = renpy.store
        case = pd_get_case()
        score = pd_score_phase_1()
        required_score = case.get("phase_1_required_score", 60)
        pd_clear_feedback()

        if score >= required_score:
            store.pd_state["phase"] = 2
            store.pd_state["feedback_message"] = "Diagnosis is strong enough. Move to solution ownership."
        elif store.pd_state["attempts_left"] > 1:
            store.pd_state["attempts_left"] -= 1
            store.pd_state["feedback_message"] = "The diagnosis is still weak. Rework the structure and try again."
        else:
            store.pd_state["attempts_left"] = 0
            store.pd_state["phase"] = 2
            store.pd_state["feedback_message"] = "You move forward with an incomplete diagnosis. The project can still be stabilized, but with less margin."

        pd_restart_interaction()


    def pd_reset_phase_1():
        store = renpy.store
        pd_clear_feedback()
        store.pd_state["selected_data_ids"] = []
        store.pd_state["generated_insight_ids"] = []
        store.pd_state["selected_card_id"] = None
        store.pd_state["root_cause_slots"] = []
        store.pd_state["impact_slots"] = []
        store.pd_state["phase_1_score"] = 0
        store.pd_state["feedback_message"] = "Phase 1 selections cleared. Start from the raw facts again."
        pd_restart_interaction()


    def pd_get_actions_for_filter(filter_name):
        actions = []
        for action in pd_get_case().get("actions", []):
            tags = action.get("tags", [])
            if filter_name == "all" or filter_name in tags:
                actions.append(action)
        return actions


    def pd_action_has_insight_bonus(action):
        store = renpy.store
        required = set(action.get("unlocked_if", []))
        return not required or required.issubset(set(store.pd_state.get("generated_insight_ids", [])))


    def pd_select_action(action_id):
        store = renpy.store
        pd_clear_feedback()

        if store.pd_state.get("selected_action_id") == action_id:
            store.pd_state["selected_action_id"] = None
            store.pd_state["feedback_message"] = "Action selection cleared."
        else:
            store.pd_state["selected_action_id"] = action_id
            store.pd_state["feedback_message"] = "Action selected. Now assign the right owner."

        pd_restart_interaction()


    def pd_assign_selected_action(pic_id):
        store = renpy.store
        action_id = store.pd_state.get("selected_action_id")
        pd_clear_feedback()

        if not action_id:
            store.pd_state["feedback_message"] = "Select an action before assigning a PIC."
            pd_restart_interaction()
            return

        store.pd_state["action_pic_pairs"][action_id] = pic_id
        store.pd_state["selected_action_id"] = None
        store.pd_state["feedback_message"] = "Ownership assigned. Keep connecting actions to the people who can move them."
        pd_restart_interaction()


    def pd_clear_action_pair(action_id):
        store = renpy.store
        pd_clear_feedback()

        if action_id in store.pd_state["action_pic_pairs"]:
            del store.pd_state["action_pic_pairs"][action_id]
            store.pd_state["feedback_message"] = "Matched pair removed."

        pd_restart_interaction()


    def pd_score_phase_2():
        store = renpy.store
        case = pd_get_case()
        rules = case.get("pic_rules", {})
        score = 0

        for action_id, pic_id in store.pd_state["action_pic_pairs"].items():
            rule = rules.get(action_id)

            if not rule:
                continue

            if pic_id in rule.get("best", []):
                score += 20
            elif pic_id in rule.get("accepted", []):
                score += 10
            elif pic_id in rule.get("wrong_but_understandable", []):
                score += 3
            else:
                score -= 10

        discovered = set(store.pd_state.get("generated_insight_ids", []))

        for action in case.get("actions", []):
            action_id = action["id"]
            required_insights = set(action.get("unlocked_if", []))

            if action_id in store.pd_state["action_pic_pairs"] and required_insights and required_insights.issubset(discovered):
                score += 5

        store.pd_state["phase_2_score"] = max(0, min(score, 100))
        return store.pd_state["phase_2_score"]


    def pd_finalize_result(aborted=False):
        store = renpy.store
        case = pd_get_case()
        case_id = store.pd_state.get("case_id")
        phase_1 = store.pd_state.get("phase_1_score", 0)
        phase_2 = store.pd_state.get("phase_2_score", 0)
        total = int((phase_1 * 0.55) + (phase_2 * 0.45))

        if aborted:
            tier = "poor"
        elif total >= 85:
            tier = "excellent"
        elif total >= 70:
            tier = "good"
        elif total >= 50:
            tier = "mixed"
        else:
            tier = "poor"

        store.pd_state["total_score"] = total

        tier_effects = minigame_get_variant("problem_diagnosis", case_id, fallback="case_scope_creep_01").get("result_tiers", {}).get(tier, {})

        result = minigame_build_result(
            "problem_diagnosis",
            case_id,
            tier,
            metrics={
                "phase_1_score": phase_1,
                "phase_2_score": phase_2,
                "total_score": total,
            },
            state={
                "generated_insights": list(store.pd_state.get("generated_insight_ids", [])),
                "root_causes": list(store.pd_state.get("root_cause_slots", [])),
                "impacts": list(store.pd_state.get("impact_slots", [])),
                "action_pic_pairs": dict(store.pd_state.get("action_pic_pairs", {})),
            },
            extra={
                "aborted": aborted,
                "case_title": case.get("case_title", ""),
            }
        )
        result["case_id"] = case_id
        result["case_title"] = case.get("case_title", "")
        result["tier"] = tier
        result["phase_1_score"] = phase_1
        result["phase_2_score"] = phase_2
        result["total_score"] = total
        result["generated_insights"] = list(store.pd_state.get("generated_insight_ids", []))
        result["root_causes"] = list(store.pd_state.get("root_cause_slots", []))
        result["impacts"] = list(store.pd_state.get("impact_slots", []))
        result["action_pic_pairs"] = dict(store.pd_state.get("action_pic_pairs", {}))
        result["aborted"] = aborted
        result["effects"] = dict(result.get("effects", {}))

        if tier_effects:
            for effect_key, effect_value in tier_effects.items():
                if isinstance(effect_value, list):
                    result["effects"].setdefault(effect_key, [])
                    result["effects"][effect_key].extend(effect_value)
                elif isinstance(effect_value, dict):
                    result["effects"].setdefault(effect_key, {})
                    result["effects"][effect_key].update(effect_value)
                else:
                    result["effects"][effect_key] = effect_value

        return result


    def pd_submit_phase_2():
        store = renpy.store
        pd_score_phase_2()
        store.pd_last_result = pd_finalize_result()
        minigame_store_result(store.pd_last_result)
        if store.pd_state.get("apply_live_effects", True):
            minigame_apply_effects(store.pd_last_result, source_key=store.pd_state.get("effect_source_key") or ("minigame:problem_diagnosis:%s" % store.pd_last_result.get("variant_id")))


    def pd_exit_current_case():
        store = renpy.store

        if not store.pd_last_result:
            if store.pd_state.get("phase", 1) == 1:
                pd_score_phase_1()
            else:
                pd_score_phase_2()

            store.pd_last_result = pd_finalize_result(aborted=True)
            minigame_store_result(store.pd_last_result)
            if store.pd_state.get("apply_live_effects", True):
                minigame_apply_effects(store.pd_last_result, source_key=store.pd_state.get("effect_source_key") or ("minigame:problem_diagnosis:%s" % store.pd_last_result.get("variant_id")))


    def pd_reset_phase_2():
        store = renpy.store
        pd_clear_feedback()
        store.pd_state["selected_action_id"] = None
        store.pd_state["action_pic_pairs"] = {}
        store.pd_state["phase_2_score"] = 0
        store.pd_state["feedback_message"] = "Phase 2 matches cleared. Reassign the actions from scratch."
        pd_restart_interaction()


    def pd_reset_current_phase():
        store = renpy.store
        if store.pd_state.get("phase", 1) == 1:
            pd_reset_phase_1()
        else:
            pd_reset_phase_2()


    def pd_use_hint():
        store = renpy.store
        case = pd_get_case()

        if store.pd_state.get("hints_left", 0) <= 0:
            store.pd_state["feedback_message"] = "No hints left. Trust your structure."
            pd_restart_interaction()
            return

        store.pd_state["hints_left"] -= 1

        if store.pd_state.get("phase", 1) == 1:
            store.pd_state["feedback_message"] = "In Phase 1, the best root causes usually come from generated insights, not from isolated raw facts."
        else:
            store.pd_state["feedback_message"] = "In Phase 2, favor owners who can authorize or coordinate project-level correction, not only the person who noticed the issue."

        pd_restart_interaction()


    def pd_show_notes():
        case = pd_get_case()
        notes = "\n".join([u"• %s" % note for note in case.get("notes", [])])
        renpy.notify(notes)


    def pd_get_result_tier_label(result):
        if not result:
            return "Pending"

        tier = result.get("tier")
        return {
            "excellent": "Excellent",
            "good": "Good",
            "mixed": "Mixed",
            "poor": "Poor",
        }.get(tier, "Pending")


    def pd_get_pic_name(pic_id):
        case = pd_get_case()
        for pic in case.get("pics", []):
            if pic["id"] == pic_id:
                return pic["name"]
        return pic_id


    def pd_debug_launch_case(case_id):
        store = renpy.store
        store.pd_debug_last_result = renpy.call_in_new_context("problem_diagnosis_debug_run", case_id)
        pd_restart_interaction()


label problem_diagnosis_start(case_id="case_scope_creep_01"):
    $ pd_prepare_case(case_id)
    $ renpy.call_screen("problem_diagnosis_minigame")
    return pd_last_result


label problem_diagnosis_debug_run(case_id="case_scope_creep_01"):
    call problem_diagnosis_start(case_id)
    return pd_last_result
