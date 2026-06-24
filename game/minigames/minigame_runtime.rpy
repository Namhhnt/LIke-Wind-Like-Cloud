default minigame_results = {}
default minigame_applied_effect_sources = []

init -1 python:
    minigame_registry = {}

    def minigame_register(config):
        if not isinstance(config, dict):
            raise Exception("Minigame config must be a dict.")

        minigame_id = config.get("id")
        if not minigame_id:
            raise Exception("Minigame config missing 'id'.")

        minigame_registry[minigame_id] = config
        return config


    def minigame_get_config(minigame_id):
        config = minigame_registry.get(minigame_id)
        if not config:
            raise Exception("Unknown minigame: %s" % minigame_id)
        return config


    def minigame_get_variant(config_or_id, variant_id, fallback=None):
        config = config_or_id if isinstance(config_or_id, dict) else minigame_get_config(config_or_id)
        variants = config.get("variants", {})

        if variant_id in variants:
            return variants[variant_id]

        if fallback and fallback in variants:
            return variants[fallback]

        raise Exception("Unknown minigame variant '%s' for %s." % (variant_id, config.get("id")))


    def minigame_build_result(minigame_id, variant_id, outcome_id, metrics=None, state=None, extra=None):
        config = minigame_get_config(minigame_id)
        variant = minigame_get_variant(config, variant_id, fallback=config.get("default_variant"))
        outcomes = variant.get("outcomes", {})

        if outcome_id not in outcomes:
            raise Exception("Unknown outcome '%s' for %s/%s." % (outcome_id, minigame_id, variant_id))

        outcome = outcomes[outcome_id]

        result = {
            "minigame_id": minigame_id,
            "variant_id": variant_id,
            "outcome_id": outcome_id,
            "title": variant.get("title", config.get("title", minigame_id)),
            "category": config.get("category", "generic"),
            "metrics": dict(metrics or {}),
            "effects": dict(outcome.get("effects", {})),
            "state": dict(state or {}),
            "extra": dict(extra or {}),
        }

        result["summary"] = outcome.get("summary", "")
        result["narrative_key"] = outcome.get("narrative_key", outcome_id)
        result["reward_key"] = outcome.get("reward_key", "%s:%s:%s" % (minigame_id, variant_id, outcome_id))
        return result


    def minigame_store_result(result):
        if not isinstance(result, dict):
            raise Exception("Minigame result must be a dict.")

        minigame_id = result.get("minigame_id")
        if not minigame_id:
            raise Exception("Minigame result missing 'minigame_id'.")

        minigame_results[minigame_id] = result
        return result


    def minigame_get_last_result(minigame_id, default=None):
        return minigame_results.get(minigame_id, default)


    def minigame_effects_already_applied(source_key):
        if not source_key:
            return False
        return source_key in minigame_applied_effect_sources


    def minigame_mark_effects_applied(source_key):
        if source_key:
            add_unique(minigame_applied_effect_sources, source_key)


    def minigame_apply_effects(result, source_key=None):
        if not isinstance(result, dict):
            return False

        if source_key and minigame_effects_already_applied(source_key):
            return False

        effects = result.get("effects", {}) or {}

        for stat_change in effects.get("story_stats_add", []):
            story_add(stat_change.get("key"), stat_change.get("amount", 0))

        for stat_set in effects.get("story_stats_set", []):
            story_set(stat_set.get("key"), stat_set.get("value"))

        for flag in effects.get("story_flags_add", []):
            story_flag(flag)

        for flag in effects.get("story_flags_remove", []):
            story_unflag(flag)

        for progression_flag in effects.get("progress_flags_add", []):
            add_unique(progress["player_flags"], progression_flag)

        for direction in effects.get("relationship_directions_add", []):
            route_id = direction.get("route")
            direction_id = direction.get("direction")
            if route_id and direction_id:
                add_unique(progress["relationship_directions"].setdefault(route_id, []), direction_id)

        for emotional_change in effects.get("emotional_state_add", []):
            key = emotional_change.get("key")
            amount = emotional_change.get("amount", 0)
            if key:
                progress["emotional_state"][key] = progress["emotional_state"].get(key, 0) + amount

        for variable_change in effects.get("store_variables_add", []):
            key = variable_change.get("key")
            amount = variable_change.get("amount", 0)
            if key:
                current = getattr(renpy.store, key, 0)
                setattr(renpy.store, key, current + amount)

        for variable_set in effects.get("store_variables_set", []):
            key = variable_set.get("key")
            if key:
                setattr(renpy.store, key, variable_set.get("value"))

        points = effects.get("investment_points", 0)
        if points > 0:
            award_points = globals().get("award_investment_points", None)
            if callable(award_points):
                reward_source = source_key or ("minigame:%s" % result.get("reward_key", result.get("minigame_id", "unknown")))
                award_points(points, reward_source)

        refresh = globals().get("refresh_validation_state", None)
        if callable(refresh):
            refresh()

        recalculate = globals().get("recalculate_chapter_availability", None)
        if callable(recalculate):
            recalculate()

        route_recalculate = globals().get("recalculate_route_status", None)
        if callable(route_recalculate):
            route_recalculate()

        ending_recalculate = globals().get("recalculate_ending_eligibility", None)
        if callable(ending_recalculate):
            ending_recalculate()

        minigame_mark_effects_applied(source_key)

        return True
