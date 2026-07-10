# FILE: game/systems/career/career_bonus_scene_system.rpy
# Reusable authored career promotion scene bridge.
#
# This module is chapter-agnostic. Any chapter, map event, phone event, or
# authored work segment can watch Tâm/Huyền career levels by calling:
#
#     $ career_bonus_begin_checkpoint("unique_source_id", ["tam", "huyen"])
#     ... story choices that may add career XP ...
#     call career_bonus_process_checkpoint("unique_source_id", ["tam", "huyen"])
#
# The existing career runtime remains authoritative for requirements, XP,
# promotion application, and salary. This module adds authored presentation,
# one-time flags, salary synchronization for the player, and reusable scenes.

# Save-persistent runtime state.
default career_bonus_queue = []
default career_bonus_seen = []
default career_bonus_current = None
default career_bonus_checkpoint_baselines = {}
default career_bonus_chapter_baselines = {}
default career_bonus_acknowledged_levels = {}

init 102 python:

    # Authored presentation for the first four levels.
    # Keep these titles aligned with CHARACTER_CAREER_TRACKS.
    CAREER_BONUS_LEVEL_PRESENTATIONS = {
        1: {
            "title": "Nhân viên mới",
            "decision_type": "appointment",
            "completion_flag_suffix": "new_employee_confirmed",
        },
        2: {
            "title": "Nhân viên chính thức — Rank 1",
            "decision_type": "promotion",
            "completion_flag_suffix": "official_rank_1_confirmed",
        },
        3: {
            "title": "Nhân viên chính thức — Rank 2",
            "decision_type": "promotion",
            "completion_flag_suffix": "official_rank_2_confirmed",
        },
        4: {
            "title": "Nhân viên chính thức — Rank 3",
            "decision_type": "promotion",
            "completion_flag_suffix": "official_rank_3_confirmed",
        },
    }

    CAREER_BONUS_SCENE_LABELS = {
        "tam": {
            1: "career_bonus_tam_level_01_new_employee",
            2: "career_bonus_tam_level_02_official_rank_1",
            3: "career_bonus_tam_level_03_official_rank_2",
            4: "career_bonus_tam_level_04_official_rank_3",
        },
        "huyen": {
            1: "career_bonus_huyen_level_01_new_employee",
            2: "career_bonus_huyen_level_02_official_rank_1",
            3: "career_bonus_huyen_level_03_official_rank_2",
            4: "career_bonus_huyen_level_04_official_rank_3",
        },
    }

    CAREER_BONUS_FALLBACK_LABELS = {
        "tam": "career_bonus_tam_promotion",
        "huyen": "career_bonus_huyen_promotion",
    }

    def career_bonus_normalize_character_ids(character_ids=None):
        if character_ids is None:
            return ("tam", "huyen")
        if isinstance(character_ids, str):
            return (character_ids,)
        return tuple(character_ids)

    def career_bonus_value(source, key, default=None):
        if isinstance(source, dict):
            return source.get(key, default)
        return getattr(source, key, default)

    def career_bonus_get_character_status(character_id):
        statuses = globals().get("character_status")
        if not isinstance(statuses, dict):
            return {}
        value = statuses.get(character_id, {})
        return value if isinstance(value, dict) else {}

    def career_bonus_get_level(character_id):
        status = career_bonus_get_character_status(character_id)
        raw_level = status.get("job_level", status.get("level", 0))
        try:
            return int(raw_level or 0)
        except (TypeError, ValueError):
            return 0

    def career_bonus_get_salary(character_id):
        status = career_bonus_get_character_status(character_id)
        for key in ("salary", "income_monthly", "monthly_salary"):
            value = status.get(key)
            if value is not None:
                try:
                    return int(value)
                except (TypeError, ValueError):
                    pass
        return 0

    def career_bonus_get_title(character_id):
        status = career_bonus_get_character_status(character_id)
        return status.get("job_title") or status.get("title") or "vị trí mới"

    def career_bonus_get_presentation(target_level):
        try:
            target_level = int(target_level)
        except (TypeError, ValueError):
            return {}
        value = CAREER_BONUS_LEVEL_PRESENTATIONS.get(target_level, {})
        return value if isinstance(value, dict) else {}

    def career_bonus_format_salary(value):
        try:
            value = int(value)
        except (TypeError, ValueError):
            value = 0
        if value <= 0:
            return "mức lương mới"
        return "{:,.0f}".format(value).replace(",", ".") + " đ/tháng"

    def career_bonus_extract_pending_level(pending):
        if pending is None or pending is False:
            return None

        if isinstance(pending, dict):
            for key in ("level", "job_level", "target_level", "level_number"):
                if key in pending:
                    try:
                        return int(pending[key])
                    except (TypeError, ValueError):
                        pass
            return None

        for key in ("level", "job_level", "target_level", "level_number"):
            value = getattr(pending, key, None)
            if value is not None:
                try:
                    return int(value)
                except (TypeError, ValueError):
                    pass

        try:
            return int(pending)
        except (TypeError, ValueError):
            return None

    def career_bonus_get_pending(character_id):
        pending_fn = globals().get("career_get_pending_level")
        if not callable(pending_fn):
            return None

        try:
            return pending_fn(character_id)
        except TypeError:
            return None

    def career_bonus_get_track(character_id):
        track_fn = globals().get("career_get_track")
        if callable(track_fn):
            try:
                return track_fn(character_id)
            except TypeError:
                pass

        tracks = globals().get("CHARACTER_CAREER_TRACKS")
        if isinstance(tracks, dict):
            return tracks.get(character_id)
        return None

    def career_bonus_iter_level_definitions(track):
        if track is None:
            return []

        candidate = track
        if isinstance(track, dict):
            for key in ("levels", "career_levels", "ranks", "track"):
                value = track.get(key)
                if value is not None:
                    candidate = value
                    break

        if isinstance(candidate, dict):
            return list(candidate.values())
        if isinstance(candidate, (list, tuple)):
            return list(candidate)
        return []

    def career_bonus_get_level_definition(character_id, target_level):
        try:
            target_level = int(target_level)
        except (TypeError, ValueError):
            return None

        for level_data in career_bonus_iter_level_definitions(career_bonus_get_track(character_id)):
            raw_level = None
            for key in ("level", "job_level", "number", "level_number", "rank"):
                value = career_bonus_value(level_data, key)
                if value is not None:
                    raw_level = value
                    break
            try:
                if int(raw_level) == target_level:
                    return level_data
            except (TypeError, ValueError):
                continue
        return None

    def career_bonus_resolve_title(character_id, target_level, pending_data=None):
        presentation = career_bonus_get_presentation(target_level)
        if presentation.get("title"):
            return presentation.get("title")

        for source in (pending_data, career_bonus_get_level_definition(character_id, target_level)):
            for key in ("title", "job_title", "name"):
                value = career_bonus_value(source, key)
                if value:
                    return value
        return career_bonus_get_title(character_id)

    def career_bonus_resolve_salary(character_id, target_level, pending_data=None):
        for source in (pending_data, career_bonus_get_level_definition(character_id, target_level)):
            for key in ("salary", "income_monthly", "monthly_salary"):
                value = career_bonus_value(source, key)
                if value is not None:
                    try:
                        return int(value)
                    except (TypeError, ValueError):
                        pass
        return career_bonus_get_salary(character_id)

    def career_bonus_get_scene_label(character_id, target_level):
        level_map = CAREER_BONUS_SCENE_LABELS.get(character_id, {})
        return level_map.get(target_level) or CAREER_BONUS_FALLBACK_LABELS.get(character_id)

    def career_bonus_seed_acknowledged_level(character_id):
        acknowledged = globals().get("career_bonus_acknowledged_levels")
        if not isinstance(acknowledged, dict):
            return
        if character_id not in acknowledged:
            acknowledged[character_id] = career_bonus_get_level(character_id)

    def career_bonus_capture_chapter_start(chapter_id, character_ids):
        character_ids = career_bonus_normalize_character_ids(character_ids)
        baselines = globals().get("career_bonus_chapter_baselines")
        if not isinstance(baselines, dict):
            return

        for character_id in character_ids:
            career_bonus_seed_acknowledged_level(character_id)
            key = "{}:{}".format(chapter_id, character_id)
            if key in baselines:
                continue

            score_key = "career_{}".format(character_id)
            state = globals().get("story_state", {})
            score = int(state.get(score_key, 0) or 0) if isinstance(state, dict) else 0

            baselines[key] = {
                "level": career_bonus_get_level(character_id),
                "score": score,
            }

    def career_bonus_get_progress_since_chapter_start(chapter_id, character_id):
        baselines = globals().get("career_bonus_chapter_baselines")
        if not isinstance(baselines, dict):
            return 0

        key = "{}:{}".format(chapter_id, character_id)
        baseline = baselines.get(key)
        if not isinstance(baseline, dict):
            career_bonus_capture_chapter_start(chapter_id, [character_id])
            baseline = baselines.get(key, {"level": 0, "score": 0})

        current_level = career_bonus_get_level(character_id)
        state = globals().get("story_state", {})
        score_key = "career_{}".format(character_id)
        current_score = int(state.get(score_key, 0) or 0) if isinstance(state, dict) else 0

        level_delta = max(0, current_level - int(baseline.get("level", 0) or 0))
        score_delta = current_score - int(baseline.get("score", 0) or 0)
        return max(0, level_delta * 100 + score_delta)

    def career_bonus_begin_checkpoint(checkpoint_id, character_ids=None):
        character_ids = career_bonus_normalize_character_ids(character_ids)
        baselines = globals().get("career_bonus_checkpoint_baselines")
        if not isinstance(baselines, dict):
            return

        checkpoint_data = {}
        for character_id in character_ids:
            career_bonus_seed_acknowledged_level(character_id)
            checkpoint_data[character_id] = career_bonus_get_level(character_id)
        baselines[checkpoint_id] = checkpoint_data

    def career_bonus_queue_item(character_id, target_level, source, checkpoint_id, pending_data=None):
        queue = globals().get("career_bonus_queue")
        seen = globals().get("career_bonus_seen")
        if not isinstance(queue, list) or not isinstance(seen, list):
            return False

        try:
            target_level = int(target_level)
        except (TypeError, ValueError):
            return False

        event_key = "{}:level:{}".format(character_id, target_level)
        if event_key in seen:
            return False
        if any(item.get("event_key") == event_key for item in queue if isinstance(item, dict)):
            return False

        presentation = career_bonus_get_presentation(target_level)
        queue.append({
            "event_key": event_key,
            "character_id": character_id,
            "target_level": target_level,
            "source": source,
            "checkpoint_id": checkpoint_id,
            "label": career_bonus_get_scene_label(character_id, target_level),
            "title": career_bonus_resolve_title(character_id, target_level, pending_data),
            "salary": career_bonus_resolve_salary(character_id, target_level, pending_data),
            "decision_type": presentation.get("decision_type", "promotion"),
            "completion_flag_suffix": presentation.get("completion_flag_suffix"),
            "pending_data": pending_data,
        })
        return True

    def career_bonus_scan_checkpoint(checkpoint_id, character_ids=None):
        character_ids = career_bonus_normalize_character_ids(character_ids)

        refresh_fn = globals().get("career_refresh_all_statuses")
        if callable(refresh_fn):
            try:
                refresh_fn()
            except TypeError:
                pass

        check_fn = globals().get("career_check_all_promotions")
        if callable(check_fn):
            try:
                check_fn()
            except TypeError:
                pass

        baselines = globals().get("career_bonus_checkpoint_baselines")
        checkpoint_data = baselines.get(checkpoint_id, {}) if isinstance(baselines, dict) else {}
        acknowledged = globals().get("career_bonus_acknowledged_levels")

        for character_id in character_ids:
            career_bonus_seed_acknowledged_level(character_id)
            current_level = career_bonus_get_level(character_id)
            before_level = int(checkpoint_data.get(character_id, current_level) or 0)
            acknowledged_level = int(acknowledged.get(character_id, before_level) or 0) if isinstance(acknowledged, dict) else before_level
            queue_from_level = max(before_level, acknowledged_level)

            if current_level > queue_from_level:
                for level in range(queue_from_level + 1, current_level + 1):
                    career_bonus_queue_item(character_id, level, "applied", checkpoint_id)
                continue

            pending = career_bonus_get_pending(character_id)
            pending_level = career_bonus_extract_pending_level(pending)
            if pending_level is not None and pending_level > max(current_level, acknowledged_level):
                career_bonus_queue_item(
                    character_id,
                    pending_level,
                    "pending",
                    checkpoint_id,
                    pending_data=pending,
                )

    def career_bonus_apply_pending_item(item):
        if not isinstance(item, dict) or item.get("source") != "pending":
            return False

        character_id = item.get("character_id")
        target_level = item.get("target_level")
        apply_fn = globals().get("career_apply_promotion")
        if not callable(apply_fn):
            return False

        try:
            import inspect
            parameters = list(inspect.signature(apply_fn).parameters.values())
            positional = [
                p for p in parameters
                if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)
            ]

            if len(positional) <= 1:
                apply_fn(character_id)
            else:
                second_name = positional[1].name.lower()
                if "level" in second_name:
                    apply_fn(character_id, target_level)
                else:
                    apply_fn(
                        character_id,
                        item.get("pending_data") or career_bonus_get_pending(character_id),
                    )
        except (TypeError, ValueError):
            apply_fn(character_id)

        return True

    def career_bonus_sync_player_salary():
        salary = career_bonus_get_salary("tam")
        if salary <= 0:
            return False

        ensure_fn = globals().get("ensure_activity_state")
        state = ensure_fn() if callable(ensure_fn) else None
        if not isinstance(state, dict):
            progress_state = globals().get("progress")
            if isinstance(progress_state, dict):
                state = progress_state.get("activity_state")

        if not isinstance(state, dict):
            return False

        old_salary = int(state.get("monthly_salary", 0) or 0)
        state["monthly_salary"] = salary
        if "salary" in state:
            state["salary"] = salary

        history = state.get("salary_history")
        if isinstance(history, list) and old_salary != salary:
            history.append({
                "old_salary": old_salary,
                "new_salary": salary,
                "reason": "career_promotion",
            })
        return True

    def career_bonus_finalize_current():
        item = globals().get("career_bonus_current")
        if not isinstance(item, dict):
            return False

        career_bonus_apply_pending_item(item)

        refresh_fn = globals().get("career_refresh_all_statuses")
        if callable(refresh_fn):
            try:
                refresh_fn()
            except TypeError:
                pass

        character_id = item.get("character_id")
        target_level = int(item.get("target_level", 0) or 0)

        if character_id == "tam":
            career_bonus_sync_player_salary()

        acknowledged = globals().get("career_bonus_acknowledged_levels")
        if isinstance(acknowledged, dict):
            acknowledged[character_id] = max(
                int(acknowledged.get(character_id, 0) or 0),
                target_level,
            )

        seen = globals().get("career_bonus_seen")
        if isinstance(seen, list) and item.get("event_key") not in seen:
            seen.append(item.get("event_key"))

        flag_fn = globals().get("story_flag")
        if callable(flag_fn):
            flag_fn("career_bonus_{}_level_{}_seen".format(character_id, target_level))
            flag_fn("career_{}_level_{}_decision_signed_by_quan".format(character_id, target_level))

            suffix = item.get("completion_flag_suffix")
            if suffix:
                flag_fn("career_{}_{}".format(character_id, suffix))

        return True
