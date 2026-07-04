label interactive_map(map_entries=None, context_id="act1_default", allow_back=True, allow_timeline=False, title_override=None):
    while True:
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
        elif isinstance(selected_entry, dict) and selected_entry.get("_action") == "phone":
            call screen phone_home(back_action=Return(), back_label=_("Back to Map"))
        else:
            if not selected_entry:
                return

            if isinstance(selected_entry, dict) and selected_entry.get("action_type") == "location_hub":
                call location_interaction_hub(selected_entry.get("location_id"))
            else:
                $ next_label = resolve_map_target_label(selected_entry)

                if not next_label:
                    "This location has no valid story target."
                    return

                jump expression next_label


label story_hub(context_id="act1_default", allow_back=False):
    $ initialize_progression()
    $ autosave_progression_at_map(context_id)
    call interactive_map(context_id=context_id, allow_back=allow_back, allow_timeline=True, title_override=_("Interactive Story Map"))
    return
