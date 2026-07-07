label interactive_map(map_entries=None, context_id="act1_default", allow_back=True, allow_timeline=False, title_override=None):
    while True:
        $ ensure_activity_state()
        $ setup_day_expectations()
        $ resolved_entries = build_map_entries(map_entries, context_id)

        if not resolved_entries:
            "There is nowhere to go right now."
            if allow_timeline and renpy.has_label("route_map_timeline"):
                jump route_map_timeline
            return

        call screen interactive_map_screen(
            resolved_entries,
            context_id=context_id,
            allow_back=allow_back,
            allow_timeline=allow_timeline,
            title_override=title_override,
        )

        $ selected_entry = _return

        if isinstance(selected_entry, dict) and selected_entry.get("_action") == "timeline":
            if renpy.has_label("route_map_timeline"):
                jump route_map_timeline
            return
        elif isinstance(selected_entry, dict) and selected_entry.get("_action") == "time_skip":
            call screen time_skip_screen()
            $ time_skip_request = _return
            if isinstance(time_skip_request, dict):
                $ skip_estimate = time_skip_build_estimate(time_skip_request.get("mode", "next_day"), time_skip_request.get("target_day"), time_skip_request.get("routine_plan", []))
                if skip_estimate.get("can_skip") and skip_estimate.get("loading_seconds", 0.0) > 0.0:
                    call screen time_passage_loading_screen(
                        skip_estimate.get("loading_seconds", 2.0),
                        title=_("Routine In Progress"),
                        body=_("Repeating the selected routine across the skip period..."),
                    )
                $ skip_result = time_skip_execute(time_skip_request.get("mode", "next_day"), time_skip_request.get("target_day"), time_skip_request.get("routine_plan", []))
                if skip_result == "blocked_negative_estimate":
                    "The projected routine would push at least one tracked status below zero, so the skip was cancelled."
                if skip_result == "force_next_event":
                    $ forced_label = time_resolve_next_event_label(clear_period=True)
                    if forced_label:
                        jump expression forced_label
        elif isinstance(selected_entry, dict) and selected_entry.get("_action") == "phone":
            call screen phone_home(back_action=Return(), back_label=_("Back to Map"))
        else:
            if not selected_entry:
                return

            if isinstance(selected_entry, dict) and selected_entry.get("action_type") == "location_hub":
                call location_interaction_hub(selected_entry.get("location_id"))
                $ location_result = _return
                if location_result == "force_next_event":
                    $ forced_label = time_resolve_next_event_label(clear_period=True)
                    if forced_label:
                        jump expression forced_label
            else:
                $ next_label = resolve_map_target_label(selected_entry)

                if not next_label:
                    "This location has no valid story target."
                    return

                jump expression next_label


label story_hub(context_id="act1_default", allow_back=False):
    $ initialize_progression()
    $ ensure_activity_state()
    $ setup_day_expectations()
    $ autosave_progression_at_map(context_id)
    call interactive_map(context_id=context_id, allow_back=allow_back, allow_timeline=True, title_override=_("Interactive Story Map"))
    return
