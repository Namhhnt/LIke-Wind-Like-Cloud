# FILE: game/patches/time_story_calendar_bridge.rpy
# Story-to-time-management calendar bridge.
#
# Story checkpoints can cover several authored weekdays without entering the
# interactive map. The normal map loop therefore has no opportunity to advance
# current_day / weekday_index / day_of_month / calendar_month.
#
# This bridge advances calendar dates for authored story time while deliberately
# leaving period_day / period_days_remaining untouched. It also avoids
# time_end_day(), because that function belongs to the free-time loop and may
# apply attendance or missed-work consequences to story-controlled workdays.

init 110 python:

    def _story_time_log(message):
        try:
            renpy.log("[story-time] {}".format(message))
        except Exception:
            pass


    def _story_time_get(key, default=None):
        getter = globals().get("activity_get")
        if callable(getter):
            return getter(key, default)

        ensure = globals().get("ensure_activity_state")
        state = None
        if callable(ensure):
            try:
                state = ensure()
            except TypeError:
                state = None

        if not isinstance(state, dict):
            progress_state = globals().get("progress")
            if isinstance(progress_state, dict):
                state = progress_state.setdefault("activity_state", {})

        if isinstance(state, dict):
            return state.get(key, default)

        return default


    def _story_time_set(key, value):
        setter = globals().get("activity_set")
        if callable(setter):
            setter(key, value)
            return value

        ensure = globals().get("ensure_activity_state")
        state = None
        if callable(ensure):
            try:
                state = ensure()
            except TypeError:
                state = None

        if not isinstance(state, dict):
            progress_state = globals().get("progress")
            if isinstance(progress_state, dict):
                state = progress_state.setdefault("activity_state", {})

        if not isinstance(state, dict):
            raise Exception(
                "time_story_calendar_bridge.rpy: activity state is unavailable."
            )

        state[key] = value
        return value


    def _story_time_int(value, default):
        try:
            return int(value)
        except (TypeError, ValueError):
            return int(default)


    def _story_time_call_optional(function_name):
        function = globals().get(function_name)
        if not callable(function):
            return False

        try:
            function()
            return True
        except TypeError as exc:
            # Do not break the story if a future implementation changes an
            # optional hook signature. The core calendar state is still valid.
            _story_time_log(
                "Skipped optional hook {}: {}".format(function_name, exc)
            )
            return False


    def time_story_set_weekday(weekday_index):
        """Align only the weekday label; do not consume a calendar day."""
        weekday_index = _story_time_int(weekday_index, 0) % 7
        _story_time_set("weekday_index", weekday_index)
        return weekday_index


    def time_story_advance_days(days, process_monthly_hooks=True):
        """
        Advance authored story days without consuming an inter-chapter period.

        Updated fields:
        - current_day
        - weekday_index
        - day_of_month
        - calendar_month
        - calendar_year, only when that field already exists

        Deliberately untouched:
        - current_period_id
        - period_day
        - period_days_total
        - period_days_remaining
        - next_event_chapter_id
        """
        days = max(0, _story_time_int(days, 0))
        if days == 0:
            return 0

        for _unused in range(days):
            current_day = _story_time_int(_story_time_get("current_day", 1), 1)
            weekday_index = _story_time_int(
                _story_time_get("weekday_index", 0), 0
            ) % 7
            day_of_month = _story_time_int(
                _story_time_get("day_of_month", 1), 1
            )
            calendar_month = _story_time_int(
                _story_time_get("calendar_month", 1), 1
            )

            current_day += 1
            weekday_index = (weekday_index + 1) % 7
            day_of_month += 1
            month_rolled = False

            # The live design uses a 30-day salary/billing cycle. Keeping the
            # authored calendar on the same 30-day model prevents chapter time
            # from drifting away from payroll and bill milestones.
            if day_of_month > 30:
                day_of_month = 1
                calendar_month += 1
                month_rolled = True

                if calendar_month > 12:
                    calendar_month = 1
                    existing_year = _story_time_get("calendar_year", None)
                    if existing_year is not None:
                        _story_time_set(
                            "calendar_year",
                            _story_time_int(existing_year, 1) + 1,
                        )

            _story_time_set("current_day", current_day)
            _story_time_set("weekday_index", weekday_index)
            _story_time_set("day_of_month", day_of_month)
            _story_time_set("calendar_month", calendar_month)

            if process_monthly_hooks:
                _story_time_call_optional("time_process_payroll_if_due")
                if month_rolled:
                    _story_time_call_optional("time_prepare_monthly_bills")

        # The following free-time period will reset the new day's time points.
        # We intentionally do not reset them here, because this helper may also
        # be called while migrating an older save before the next checkpoint.
        return days


    def time_story_advance_days_once(flag_id, days, process_monthly_hooks=True):
        """Idempotent calendar advancement guarded by a normal story flag."""
        has_flag = globals().get("story_has_flag")
        add_flag = globals().get("story_flag")

        if flag_id and callable(has_flag) and has_flag(flag_id):
            return 0

        advanced = time_story_advance_days(days, process_monthly_hooks)

        if flag_id and callable(add_flag):
            add_flag(flag_id)

        return advanced


    def time_story_begin_workweek(flag_id=None):
        """Mark an authored checkpoint as Monday without consuming a day."""
        has_flag = globals().get("story_has_flag")
        add_flag = globals().get("story_flag")

        if flag_id and callable(has_flag) and has_flag(flag_id):
            return False

        time_story_set_weekday(0)

        if flag_id and callable(add_flag):
            add_flag(flag_id)

        return True
