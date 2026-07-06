init -1 python:

    TIME_NUMERIC_DEFAULTS = {
        "money": 3000000,
        "energy": 70,
        "stress": 20,
        "mood": 50,
        "health": 75,
        "confidence": 0,
        "style": 0,
        "knowledge": 0,
        "work_skill": 0,
        "cooking_skill": 0,
        "life_skill": 0,
        "main_work_focus": 50,
        "time_units": 24,
        "daily_time_points": 24,
        "time_points": 24,
        "last_daily_reset_day": 0,
        "current_day": 1,
        "calendar_month": 1,
        "day_of_month": 1,
        "weekday_index": 0,
        "period_day": 1,
        "period_days_total": 0,
        "period_days_remaining": 0,
        "paid_leave_used_this_month": 0,
        "sick_leave_used_this_month": 0,
        "work_attendance_this_month": 0,
        "work_absence_this_month": 0,
        "unexcused_absence_this_month": 0,
        "ot_days_this_month": 0,
        "salary_cycle_day": 0,
        "last_salary_day": 0,
        "monthly_salary": 12000000,
        "pending_ot_bonus": 0,
        "pending_salary_penalty": 0,
        "unpaid_bill_months": 0,
        "part_time_count_this_period": 0,
    }

    TIME_LIST_DEFAULTS = {
        "daily_completed_actions": [],
        "daily_character_visits": [],
        "daily_location_visits": [],
        "salary_history": [],
        "pending_bills": [],
        "paid_bills": [],
        "time_skip_plan": [],
        "missed_important_interactions": [],
        "auto_triggered_events": [],
        "flags": [],
        "completed_actions": [],
    }

    TIME_BOOL_DEFAULTS = {
        "player_is_employed": False,
        "work_expected_today": False,
        "work_completed_today": False,
        "auto_pay_bills": True,
        "time_skip_enabled": False,
    }

    DEFAULT_MONTHLY_BILLS = [
        {"id": "rent", "label": "Rent", "amount": 4500000},
        {"id": "utilities", "label": "Utilities", "amount": 750000},
        {"id": "food", "label": "Food", "amount": 1500000},
    ]


    def _time_copy_default(value):
        if isinstance(value, list):
            return list(value)
        if isinstance(value, dict):
            return dict(value)
        return value


    def _time_clamp_state_value(key, value):
        clamps = globals().get("ACTIVITY_CLAMPS", {})
        bounds = clamps.get(key)
        if not bounds:
            return value
        if isinstance(value, (int, float)):
            low, high = bounds
            return min(max(int(value), low), high)
        return value


    def time_management_extend_activity_state(state):
        if state is None or not isinstance(state, dict):
            state = {}

        for key, value in TIME_NUMERIC_DEFAULTS.items():
            state.setdefault(key, value)

        for key, value in TIME_LIST_DEFAULTS.items():
            current_value = state.setdefault(key, _time_copy_default(value))
            if current_value is None or not isinstance(current_value, list):
                state[key] = list(current_value) if current_value else []

        for key, value in TIME_BOOL_DEFAULTS.items():
            state.setdefault(key, value)

        state.setdefault("inventory", {})
        if state["inventory"] is None or not isinstance(state["inventory"], dict):
            state["inventory"] = dict(state["inventory"]) if state["inventory"] else {}

        state.setdefault("current_period_id", None)
        state.setdefault("next_event_chapter_id", None)

        for key in list(TIME_NUMERIC_DEFAULTS.keys()):
            state[key] = _time_clamp_state_value(key, state.get(key))

        legacy_time_units = state.get("time_units")
        time_points = state.get("time_points")
        if isinstance(legacy_time_units, (int, float)) and legacy_time_units > 100 and not state.get("current_period_id"):
            legacy_time_units = 24
        if isinstance(time_points, (int, float)) and time_points > 100 and not state.get("current_period_id"):
            time_points = 24

        if isinstance(time_points, (int, float)):
            synchronized_points = int(time_points)
        elif isinstance(legacy_time_units, (int, float)):
            synchronized_points = int(legacy_time_units)
        else:
            synchronized_points = int(state.get("daily_time_points", 24))

        synchronized_points = min(max(synchronized_points, 0), 100)
        state["time_points"] = synchronized_points
        state["time_units"] = synchronized_points

        daily_points = state.get("daily_time_points", 24)
        if not isinstance(daily_points, (int, float)) or daily_points <= 0:
            daily_points = 24
        state["daily_time_points"] = min(max(int(daily_points), 1), 24)

        return state


    def time_sync_time_keys(value):
        if value is None:
            return 0
        try:
            value = int(value)
        except Exception:
            value = 0
        value = min(max(value, 0), 100)
        return value


    def time_get_weekday_name():
        s = ensure_activity_state()
        return WEEKDAY_NAMES[s.get("weekday_index", 0) % 7]


    def time_is_weekday():
        s = ensure_activity_state()
        return s.get("weekday_index", 0) % 7 <= 4


    def time_is_weekend():
        return not time_is_weekday()


    def time_is_sunday():
        s = ensure_activity_state()
        return s.get("weekday_index", 0) % 7 == 6


    def time_advance_calendar_day():
        s = ensure_activity_state()
        s["current_day"] += 1
        s["day_of_month"] += 1
        s["weekday_index"] = (s["weekday_index"] + 1) % 7
        if s["day_of_month"] > 30:
            s["day_of_month"] = 1
            s["calendar_month"] += 1


    def time_get_next_event_days_remaining():
        s = ensure_activity_state()
        remaining = s.get("period_days_remaining", 0)
        if not s.get("current_period_id"):
            return None
        return max(0, int(remaining))


    def time_get_header_line():
        s = ensure_activity_state()
        return "%s, Month %s Day %s" % (
            time_get_weekday_name(),
            s.get("calendar_month", 1),
            s.get("day_of_month", 1),
        )


    def time_get_secondary_header_line():
        days_remaining = time_get_next_event_days_remaining()
        if days_remaining is None:
            return "No active inter-chapter period"
        label = "day" if days_remaining == 1 else "days"
        return "Next Event: %s %s" % (days_remaining, label)


    def time_get_points_header_line():
        s = ensure_activity_state()
        return "Time Points: %s / %s" % (s.get("time_points", 0), s.get("daily_time_points", 24))


    def time_get_main_today_summary():
        s = ensure_activity_state()
        if not s.get("work_expected_today"):
            return None
        if s.get("work_completed_today"):
            return "Work at Company ✓"
        return "! Work at Company — 10 TP"


    def time_get_chapter_start_day(chapter_id):
        if chapter_id == "prologue_rain_dream":
            return 0
        chapters = globals().get("CHAPTER_ORDER", [])
        total = 0
        for ordered_chapter_id in chapters:
            if ordered_chapter_id == chapter_id:
                return total + 1
            metadata = chapter_time_metadata(ordered_chapter_id)
            if ordered_chapter_id == "prologue_rain_dream" or metadata.get("is_flashback"):
                continue
            total += int(metadata.get("event_span_days", DEFAULT_EVENT_SPAN_DAYS))
            total += int(metadata.get("free_duration_days", DEFAULT_PERIOD_DURATION_DAYS))
        return total + 1


    def time_get_period_start_day(chapter_id):
        metadata = chapter_time_metadata(chapter_id)
        return time_get_chapter_start_day(chapter_id) + int(metadata.get("event_span_days", 0))


    def time_align_calendar_to_chapter(chapter_id):
        start_day = max(1, int(time_get_period_start_day(chapter_id)))
        s = ensure_activity_state()
        s["current_day"] = start_day
        s["calendar_month"] = ((start_day - 1) // 30) + 1
        s["day_of_month"] = ((start_day - 1) % 30) + 1
        s["weekday_index"] = (start_day - 1) % 7
        return start_day


    def time_reset_day(reset_time_points=True):
        s = ensure_activity_state()
        if reset_time_points:
            synchronized_points = time_sync_time_keys(s.get("daily_time_points", 24))
            s["time_points"] = synchronized_points
            s["time_units"] = synchronized_points
        s["daily_completed_actions"] = []
        s["daily_character_visits"] = []
        s["daily_location_visits"] = []
        s["work_completed_today"] = False
        s["last_daily_reset_day"] = s.get("current_day", 1)
        setup_day_expectations()


    def setup_day_expectations():
        s = ensure_activity_state()
        employed = bool(s.get("player_is_employed"))
        s["work_expected_today"] = employed and time_is_weekday()
        return s["work_expected_today"]


    def time_start_period(period_id):
        s = ensure_activity_state()
        period = INTER_CHAPTER_PERIODS.get(period_id)
        if not period:
            return False

        chapter_id = period.get("start_after")
        time_align_calendar_to_chapter(chapter_id)
        s["current_period_id"] = period_id
        s["period_day"] = 1
        s["period_days_total"] = int(period.get("duration_days", 1))
        s["period_days_remaining"] = int(period.get("duration_days", 1))
        s["next_event_chapter_id"] = period.get("next_event")
        s["player_is_employed"] = bool(period.get("player_is_employed", s.get("player_is_employed", False)))
        s["part_time_count_this_period"] = 0
        time_reset_day(reset_time_points=True)
        return True


    def time_start_period_after_chapter(chapter_id):
        period_id = PERIOD_BY_COMPLETED_CHAPTER.get(chapter_id)
        if not period_id:
            return False
        return time_start_period(period_id)


    def time_should_force_next_event():
        s = ensure_activity_state()
        if not s.get("current_period_id"):
            return False
        period = INTER_CHAPTER_PERIODS.get(s["current_period_id"], {})
        if not period.get("force_trigger", True):
            return False
        return s.get("period_days_remaining", 0) <= 0


    def time_get_next_event_chapter_id():
        s = ensure_activity_state()
        return s.get("next_event_chapter_id")


    def time_clear_current_period():
        s = ensure_activity_state()
        s["current_period_id"] = None
        s["period_day"] = 1
        s["period_days_total"] = 0
        s["period_days_remaining"] = 0
        s["next_event_chapter_id"] = None


    def time_resolve_next_event_label(clear_period=True):
        chapter_id = time_get_next_event_chapter_id()
        if not chapter_id:
            return None
        chapter = globals().get("CHAPTERS", {}).get(chapter_id, {})
        label_name = chapter.get("label", chapter_id)
        if clear_period:
            time_clear_current_period()
        return label_name if renpy.has_label(label_name) else None


    def time_prepare_monthly_bills():
        s = ensure_activity_state()
        pending_bills = []
        for bill in DEFAULT_MONTHLY_BILLS:
            pending_bills.append(dict(bill))
        s["pending_bills"] = pending_bills


    def time_pay_pending_bills():
        s = ensure_activity_state()
        total = sum(int(bill.get("amount", 0)) for bill in s.get("pending_bills", []))
        if total <= 0:
            return True
        if s.get("money", 0) >= total:
            s["money"] -= total
            s["paid_bills"].append({"day": s.get("current_day", 1), "amount": total})
            s["pending_bills"] = []
            s["unpaid_bill_months"] = 0
            story_flag("monthly_bills_paid")
            return True
        s["unpaid_bill_months"] += 1
        story_flag("unpaid_monthly_bills")
        story_flag("financial_pressure_warning")
        return False


    def time_process_payroll_if_due():
        s = ensure_activity_state()
        if s.get("salary_cycle_day", 0) < 30:
            return False

        attendance = max(0, int(s.get("work_attendance_this_month", 0)))
        absences = max(0, int(s.get("unexcused_absence_this_month", 0)))
        salary = int(s.get("monthly_salary", 12000000))
        salary += int(s.get("pending_ot_bonus", 0))
        salary -= int(s.get("pending_salary_penalty", 0))
        salary -= absences * 250000
        if attendance == 0 and s.get("player_is_employed"):
            salary = max(0, salary - 1000000)

        s["money"] += max(0, salary)
        s["last_salary_day"] = s.get("current_day", 1)
        s["salary_history"].append({
            "day": s.get("current_day", 1),
            "amount": max(0, salary),
            "attendance": attendance,
            "absences": absences,
        })
        s["salary_cycle_day"] = 0
        s["pending_ot_bonus"] = 0
        s["pending_salary_penalty"] = 0
        s["work_attendance_this_month"] = 0
        s["work_absence_this_month"] = 0
        s["unexcused_absence_this_month"] = 0
        s["ot_days_this_month"] = 0
        story_flag("monthly_salary_received")
        time_prepare_monthly_bills()
        if s.get("auto_pay_bills", True):
            time_pay_pending_bills()
        return True


    def activity_daily_limit_key(action):
        return action.get("daily_limit_key") or action.get("id")


    def activity_has_daily_limit_been_used(action):
        s = ensure_activity_state()
        key = activity_daily_limit_key(action)
        return key in s.get("daily_completed_actions", [])


    def activity_mark_daily_limit_used(action):
        s = ensure_activity_state()
        key = activity_daily_limit_key(action)
        if key and key not in s.get("daily_completed_actions", []):
            s["daily_completed_actions"].append(key)


    def time_action_requirement_failure(action):
        s = ensure_activity_state()
        required_period_ids = action.get("required_period_ids", []) or []
        current_period_id = s.get("current_period_id")
        if required_period_ids and current_period_id not in required_period_ids:
            return "This interaction is not available in the current period."

        if action.get("weekday_only") and not time_is_weekday():
            return "Only available on weekdays."
        if action.get("weekend_only") and not time_is_weekend():
            return "Only available on weekends."

        if activity_has_daily_limit_been_used(action):
            return action.get("daily_limit_message", "Already visited today.")

        return None


    def time_mark_action_visit(action):
        s = ensure_activity_state()
        location_id = action.get("location_id")
        if location_id and location_id not in s.get("daily_location_visits", []):
            s["daily_location_visits"].append(location_id)

        key = activity_daily_limit_key(action)
        if isinstance(key, str) and key.startswith("visit_character:"):
            character_id = key.split(":", 1)[1]
            if character_id and character_id not in s.get("daily_character_visits", []):
                s["daily_character_visits"].append(character_id)


    def process_daily_missed_interactions():
        s = ensure_activity_state()
        current_period_id = s.get("current_period_id")
        if not current_period_id:
            return

        current_period = INTER_CHAPTER_PERIODS.get(current_period_id, {})
        period_day = s.get("period_day", 1)
        important_ids = set(current_period.get("important_interactions", []))

        for actions in globals().get("MAP_LOCATION_ACTIONS", {}).values():
            for action in actions:
                action_id = action.get("id")
                if action_id not in important_ids:
                    continue
                if not action.get("important") or not action.get("missable"):
                    continue
                expires = action.get("expires_after_period_day")
                if expires is None or period_day < expires:
                    continue
                if action_id in s.get("completed_actions", []):
                    continue
                if action_id in s.get("missed_important_interactions", []):
                    continue
                s["missed_important_interactions"].append(action_id)
                missed_flag = action.get("missed_flag")
                if missed_flag:
                    story_flag(missed_flag)


    def time_can_end_day():
        s = ensure_activity_state()
        if s.get("work_expected_today") and not s.get("work_completed_today"):
            s["work_absence_this_month"] += 1
            s["unexcused_absence_this_month"] += 1
            s["pending_salary_penalty"] += 250000
            s["stress"] = min(100, s.get("stress", 0) + 8)
            story_add("career_tam", -1)
            story_flag("skipped_work_without_notice")
        return True


    def time_end_day(reason="manual"):
        s = ensure_activity_state()
        if not time_can_end_day():
            return "work_warning_required"

        process_daily_missed_interactions()

        if s.get("current_period_id"):
            s["period_day"] += 1
            s["period_days_remaining"] = max(0, s.get("period_days_remaining", 0) - 1)

        s["salary_cycle_day"] += 1
        time_process_payroll_if_due()

        should_trigger = time_should_force_next_event()

        time_advance_calendar_day()
        time_reset_day(reset_time_points=True)

        if should_trigger:
            s["auto_triggered_events"].append({
                "day": s.get("current_day", 1),
                "reason": reason,
                "chapter_id": time_get_next_event_chapter_id(),
            })
            return "force_next_event"

        return "day_ended"


    def time_skip_is_available():
        s = ensure_activity_state()
        return bool(s.get("current_period_id"))


    def time_skip_can_choose_any_day():
        s = ensure_activity_state()
        current_period = INTER_CHAPTER_PERIODS.get(s.get("current_period_id"), {})
        return bool(current_period.get("allow_skip_to_any_day"))


    def time_skip_target_day_choices():
        s = ensure_activity_state()
        total_days = max(1, int(s.get("period_days_total", 1)))
        current_day = max(1, int(s.get("period_day", 1)))
        return [day for day in range(current_day, total_days + 1)]


    def time_skip_apply_default_day_plan():
        s = ensure_activity_state()
        if s.get("work_expected_today"):
            s["work_completed_today"] = True
            s["work_attendance_this_month"] += 1
            s["energy"] = max(0, s.get("energy", 0) - 15)
            s["stress"] = min(100, s.get("stress", 0) + 6)
            s["work_skill"] = min(100, s.get("work_skill", 0) + 2)
            story_add("career_tam", 1)


    def time_skip_execute(mode="next_day", target_day=None):
        if not time_skip_is_available():
            return "unavailable"

        if mode == "next_day":
            time_skip_apply_default_day_plan()
            return time_end_day(reason="time_skip")

        if mode == "to_target_day":
            target_day = int(target_day or 1)
            while ensure_activity_state().get("period_day", 1) < target_day:
                time_skip_apply_default_day_plan()
                result = time_end_day(reason="time_skip")
                if result == "force_next_event":
                    return result
            return "day_ended"

        if mode == "to_next_event":
            while True:
                time_skip_apply_default_day_plan()
                result = time_end_day(reason="time_skip")
                if result == "force_next_event":
                    return result
                if ensure_activity_state().get("current_period_id") is None:
                    return result

        return "unavailable"


    def time_get_financial_summary():
        s = ensure_activity_state()
        pending_bills = list(s.get("pending_bills", []))
        return {
            "money": s.get("money", 0),
            "monthly_salary": s.get("monthly_salary", 0),
            "is_employed": s.get("player_is_employed", False),
            "next_salary_progress": max(0, min(30, s.get("salary_cycle_day", 0))),
            "pending_bills": pending_bills,
            "pending_bills_total": sum(b.get("amount", 0) for b in pending_bills),
            "unpaid_bill_months": s.get("unpaid_bill_months", 0),
            "last_salary": s.get("salary_history", [])[-1] if s.get("salary_history") else None,
            "salary_history_count": len(s.get("salary_history", [])),
            "work_attendance_this_month": s.get("work_attendance_this_month", 0),
            "work_absence_this_month": s.get("work_absence_this_month", 0),
            "pending_ot_bonus": s.get("pending_ot_bonus", 0),
            "pending_salary_penalty": s.get("pending_salary_penalty", 0),
        }
