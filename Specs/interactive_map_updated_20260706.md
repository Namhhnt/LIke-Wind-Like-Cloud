# Technical Implementation Guide

## Daily Time Management, Payroll, Paybill, Time Skip, and Chapter Migration

Project: **Like Wind, Like Cloud**
Engine: **Ren’Py 8**
Target System: Replace the old free-time session system with a calendar-based daily time management system.

---

# 1. Objective

Replace the current chapter-end free-time model:

```renpy
$ activity_start_free_time_session(40)
```

with a calendar/day-loop system:

```text
Chapter ends
→ Start an inter-chapter period
→ Each day has 24 time points
→ Player chooses daily actions on the interactive map
→ Workdays expect the player to work
→ Salary is paid every 30 days
→ Monthly bills are processed after salary
→ Important interactions may expire
→ Time Skip can automate routine actions
→ Next story event triggers manually or automatically at the deadline
```

The existing Interactive Map system must remain the main interface. Do not replace it. Extend it.

The existing map already supports:

* story chapter selection;
* free-time location interactions;
* location action data via `MAP_LOCATION_ACTIONS`;
* activity state;
* scene router;
* flags and inventory;
* phone/timeline dispatch.

---

# 2. High-Level Design

## 2.1 Core Concepts

### Calendar Day

A calendar day is the base unit of simulation.

Each day has:

```python
time_points = 24
```

The map should display:

```text
Monday, Month 1 Day 12
Next Event: 16 days
```

Do not display too many stats on the map header. Money, stress, bills, and logs should go to the Status/Phone panel.

---

### Inter-Chapter Period

A period is the playable gap between two main story events.

Example:

```python
{
    "id": "after_tam_c02",
    "start_after": "tam_c02_company_party",
    "next_event": "tam_c03_first_salary_week",
    "duration_days": 28,
    "force_trigger": True,
}
```

The player may manually trigger the next event if available, but if they do not, the system automatically triggers it when the period deadline is reached.

---

### Daily Time Points

Default daily time budget:

```python
DAILY_TIME_POINTS = 24
```

Recommended action costs:

| Action                 | Cost |
| ---------------------- | ---: |
| Work at Company        |   10 |
| Sleep 4h               |    4 |
| Sleep 6h               |    6 |
| Sleep 8h               |    8 |
| Sleep 10h              |   10 |
| Sleep 12h              |   12 |
| Visit character        |  2–4 |
| Shopping               |  2–4 |
| Study / Read           |  2–4 |
| Cook / Clean / Journal |  1–3 |
| Weekend OT             |    6 |

Do not use the old concept name `session` for the new system. Use:

```python
time_points
daily_time_points
current_day
period_day
period_days_remaining
```

---

# 3. Files to Add

Add these files:

```text
game/time_management_data.rpy
game/time_management_logic.rpy
game/time_skip_screen.rpy
game/daily_hud_screen.rpy
```

Optional later:

```text
game/payroll_data.rpy
game/payroll_logic.rpy
game/bill_data.rpy
game/bill_logic.rpy
```

For MVP, payroll and bills can live inside `time_management_logic.rpy`.

---

# 4. Files to Modify

Modify these files:

```text
game/map_location_interactions.rpy
game/map_hub_with_interactions.rpy
game/map_screen_with_interactions.rpy
game/progression_logic.rpy
game/progression_data.rpy
game/route_map.rpy
game/story/**/_chapter.rpy
```

Optional:

```text
game/story_state.rpy
game/screens.rpy
game/phone/status screens
```

---

# 5. Activity State Migration

The existing `progress["activity_state"]` must be extended, not replaced.

Add missing keys safely through `ensure_activity_state()`.

## 5.1 Required State Fields

```python
def ensure_activity_state():
    global progress

    if "activity_state" not in progress:
        progress["activity_state"] = {}

    s = progress["activity_state"]

    # Existing core stats.
    s.setdefault("money", 3000000)
    s.setdefault("energy", 70)
    s.setdefault("stress", 20)
    s.setdefault("mood", 50)
    s.setdefault("health", 75)
    s.setdefault("confidence", 0)
    s.setdefault("style", 0)
    s.setdefault("knowledge", 0)
    s.setdefault("work_skill", 0)
    s.setdefault("cooking_skill", 0)
    s.setdefault("life_skill", 0)
    s.setdefault("main_work_focus", 50)

    # Backward compatibility.
    s.setdefault("time_units", 0)

    # New calendar state.
    s.setdefault("current_day", 1)
    s.setdefault("calendar_month", 1)
    s.setdefault("day_of_month", 1)
    s.setdefault("weekday_index", 0)

    # New daily time state.
    s.setdefault("daily_time_points", 24)
    s.setdefault("time_points", 24)
    s.setdefault("last_daily_reset_day", 0)

    # Period state.
    s.setdefault("current_period_id", None)
    s.setdefault("period_day", 1)
    s.setdefault("period_days_total", 0)
    s.setdefault("period_days_remaining", 0)
    s.setdefault("next_event_chapter_id", None)

    # Daily limits.
    s.setdefault("daily_completed_actions", [])
    s.setdefault("daily_character_visits", [])
    s.setdefault("daily_location_visits", [])

    # Workday state.
    s.setdefault("player_is_employed", False)
    s.setdefault("work_expected_today", False)
    s.setdefault("work_completed_today", False)
    s.setdefault("paid_leave_used_this_month", 0)
    s.setdefault("sick_leave_used_this_month", 0)
    s.setdefault("work_attendance_this_month", 0)
    s.setdefault("work_absence_this_month", 0)
    s.setdefault("unexcused_absence_this_month", 0)
    s.setdefault("ot_days_this_month", 0)

    # Payroll.
    s.setdefault("salary_cycle_day", 0)
    s.setdefault("last_salary_day", 0)
    s.setdefault("monthly_salary", 12000000)
    s.setdefault("pending_ot_bonus", 0)
    s.setdefault("pending_salary_penalty", 0)
    s.setdefault("salary_history", [])

    # Bills.
    s.setdefault("auto_pay_bills", True)
    s.setdefault("pending_bills", [])
    s.setdefault("paid_bills", [])
    s.setdefault("unpaid_bill_months", 0)

    # Time Skip.
    s.setdefault("time_skip_plan", [])
    s.setdefault("time_skip_enabled", False)
    s.setdefault("missed_important_interactions", [])
    s.setdefault("auto_triggered_events", [])

    # Existing collection fields.
    s.setdefault("inventory", {})
    s.setdefault("flags", [])
    s.setdefault("completed_actions", [])

    return s
```

---

# 6. Calendar System

## 6.1 Weekday Names

```python
WEEKDAY_NAMES = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
```

## 6.2 Calendar Helpers

```python
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
```

For MVP, every month is exactly 30 days. This keeps payroll and bill logic simple.

---

# 7. Inter-Chapter Period Data

Create:

```text
game/time_management_data.rpy
```

## 7.1 Period Data Structure

```python
init -5 python:

    INTER_CHAPTER_PERIODS = {
        "after_tam_c01": {
            "id": "after_tam_c01",
            "start_after": "tam_c01_interview_day",
            "next_event": "tam_c02_company_party",
            "duration_days": 7,
            "force_trigger": True,
            "warning_days": [3, 1],
            "allowed_main_actions": ["company_work_full_day", "sleep_8h_home"],
            "important_interactions": [
                "visit_huyen_after_first_job",
            ],
        },

        "after_tam_c02": {
            "id": "after_tam_c02",
            "start_after": "tam_c02_company_party",
            "next_event": "tam_c03_first_salary_week",
            "duration_days": 28,
            "force_trigger": True,
            "warning_days": [7, 3, 1],
            "important_interactions": [
                "huyen_party_followup",
                "hoang_house_casual_followup",
            ],
        },
    }


    PERIOD_BY_COMPLETED_CHAPTER = {
        period["start_after"]: period_id
        for period_id, period in INTER_CHAPTER_PERIODS.items()
    }
```

---

# 8. Period Logic

Create:

```text
game/time_management_logic.rpy
```

## 8.1 Start Period

```python
def time_start_period(period_id):
    s = ensure_activity_state()
    period = INTER_CHAPTER_PERIODS.get(period_id)

    if not period:
        return False

    s["current_period_id"] = period_id
    s["period_day"] = 1
    s["period_days_total"] = int(period.get("duration_days", 1))
    s["period_days_remaining"] = int(period.get("duration_days", 1))
    s["next_event_chapter_id"] = period.get("next_event")
    s["daily_time_points"] = 24
    s["time_points"] = 24

    time_reset_day()
    return True
```

## 8.2 Start Period After Chapter

```python
def time_start_period_after_chapter(chapter_id):
    period_id = PERIOD_BY_COMPLETED_CHAPTER.get(chapter_id)

    if not period_id:
        return False

    return time_start_period(period_id)
```

## 8.3 Reset Day

```python
def time_reset_day():
    s = ensure_activity_state()

    s["time_points"] = s.get("daily_time_points", 24)
    s["daily_completed_actions"] = []
    s["daily_character_visits"] = []
    s["daily_location_visits"] = []
    s["work_completed_today"] = False

    setup_day_expectations()
```

## 8.4 Day Expectations

```python
def setup_day_expectations():
    s = ensure_activity_state()

    if s.get("player_is_employed") and time_is_weekday():
        s["work_expected_today"] = True
    else:
        s["work_expected_today"] = False
```

## 8.5 Consume Time

```python
def time_consume(points):
    s = ensure_activity_state()

    points = int(points or 0)

    if points <= 0:
        return True

    if s.get("time_points", 0) < points:
        return False

    s["time_points"] -= points
    return True
```

---

# 9. End Day Logic

## 9.1 End Day Validation

Do not auto-deduct 10 points for work at the beginning of the day.

Instead:

* weekday creates a work expectation;
* player keeps all 24 points;
* player must choose Work, Take Leave, Call Sick, or Skip Work;
* if player tries to end the day without handling work, show warning.

```python
def time_can_end_day():
    s = ensure_activity_state()

    if s.get("work_expected_today") and not s.get("work_completed_today"):
        return False

    return True
```

## 9.2 Work Warning Screen

When player tries to sleep/end day without work:

```text
You have not worked today.
Skipping work may affect attendance, salary, and career progress.

[Go to Work]
[Take Paid Leave]
[Call Sick]
[Skip Work Anyway]
[Cancel]
```

Implement as a Ren’Py screen or label.

## 9.3 Apply Work Absence Options

```python
def time_take_paid_leave():
    s = ensure_activity_state()

    s["paid_leave_used_this_month"] += 1
    s["work_completed_today"] = True
    s["work_expected_today"] = False

    s["stress"] = max(0, s["stress"] - 2)


def time_call_sick():
    s = ensure_activity_state()

    s["sick_leave_used_this_month"] += 1
    s["work_completed_today"] = True
    s["work_expected_today"] = False

    s["health"] = max(0, s["health"] - 1)


def time_skip_work_anyway():
    s = ensure_activity_state()

    s["work_absence_this_month"] += 1
    s["unexcused_absence_this_month"] += 1
    s["pending_salary_penalty"] += 500000

    s["work_completed_today"] = True
    s["work_expected_today"] = False

    s["stress"] = min(100, s["stress"] + 8)

    story_add("career_tam", -1)
    story_flag("skipped_work_without_notice")
```

## 9.4 End Day

```python
def time_end_day(reason="manual"):
    s = ensure_activity_state()

    if not time_can_end_day():
        return "work_warning_required"

    process_daily_missed_interactions()

    if s.get("current_period_id"):
        s["period_day"] += 1
        s["period_days_remaining"] = max(0, s["period_days_remaining"] - 1)

    s["salary_cycle_day"] += 1

    time_process_payroll_if_due()

    should_trigger = time_should_force_next_event()

    time_advance_calendar_day()
    time_reset_day()

    if should_trigger:
        return "force_next_event"

    return "day_ended"
```

---

# 10. Forced Next Event Logic

## 10.1 Rule

Do not trigger the next event in the middle of the day.

Trigger it only after:

* Sleep;
* End Day;
* Time Skip day completion.

## 10.2 Implementation

```python
def time_should_force_next_event():
    s = ensure_activity_state()

    if not s.get("current_period_id"):
        return False

    period = INTER_CHAPTER_PERIODS.get(s["current_period_id"], {})

    if not period.get("force_trigger", True):
        return False

    return s.get("period_days_remaining", 0) <= 0
```

## 10.3 Get Next Event Label

```python
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
```

---

# 11. Payroll System

## 11.1 Important Design Rule

Work action must not directly add monthly salary.

Daily work should affect:

```python
work_attendance_this_month
career_tam
work_skill
energy
stress
```

Salary is paid separately every 30 days.

## 11.2 Work Action Effects

Recommended daily work action:

```python
{
    "id": "company_work_full_day",
    "title": "Work at Company",
    "summary": "Spend a regular workday at the company.",
    "category": "Main",
    "time_cost": 10,
    "money_cost": 0,

    "requires": {
        "time_points": 10,
        "energy_min": 15,
    },

    "effects": {
        "time_points": -10,
        "energy": -18,
        "stress": 8,
        "work_skill": 1,
        "main_work_focus": 2,
    },

    "story_effects": {
        "career_tam": 1,
    },

    "flags": ["worked_company_today"],

    "daily_limit_key": "main_work",
    "daily_limit": 1,

    "marks_work_completed": True,
    "time_skip_allowed": True,
    "time_skip_priority": "main",

    "message": "Tâm spends the day handling office work. Nothing dramatic happens, which is sometimes the best possible outcome."
}
```

## 11.3 Payroll Processing

```python
def time_process_payroll_if_due():
    s = ensure_activity_state()

    if s.get("salary_cycle_day", 0) < 30:
        return False

    time_process_monthly_salary()
    s["salary_cycle_day"] = 0
    return True
```

## 11.4 Monthly Salary Formula

```python
def time_process_monthly_salary():
    s = ensure_activity_state()

    base_salary = int(s.get("monthly_salary", 0))
    ot_bonus = int(s.get("pending_ot_bonus", 0))
    penalty = int(s.get("pending_salary_penalty", 0))

    net_salary = max(0, base_salary + ot_bonus - penalty)

    s["money"] += net_salary

    s["salary_history"].append({
        "day": s.get("current_day"),
        "month": s.get("calendar_month"),
        "base_salary": base_salary,
        "ot_bonus": ot_bonus,
        "penalty": penalty,
        "net_salary": net_salary,
        "attendance": s.get("work_attendance_this_month", 0),
        "absence": s.get("work_absence_this_month", 0),
        "unexcused_absence": s.get("unexcused_absence_this_month", 0),
    })

    story_flag("monthly_salary_received")

    time_process_monthly_bills()

    time_reset_monthly_work_counters()
```

## 11.5 Reset Monthly Work Counters

```python
def time_reset_monthly_work_counters():
    s = ensure_activity_state()

    s["work_attendance_this_month"] = 0
    s["work_absence_this_month"] = 0
    s["unexcused_absence_this_month"] = 0
    s["ot_days_this_month"] = 0
    s["paid_leave_used_this_month"] = 0
    s["sick_leave_used_this_month"] = 0
    s["pending_ot_bonus"] = 0
    s["pending_salary_penalty"] = 0
```

---

# 12. Monthly Paybill System

## 12.1 Bill Data

Add bill profiles.

```python
MONTHLY_BILL_PROFILES = {
    "tam": {
        "rent": 0,
        "utilities": 800000,
        "food": 2500000,
        "travel": 700000,
        "misc": 1000000,
    },

    "huyen": {
        "rent": 3500000,
        "utilities": 700000,
        "food": 2200000,
        "travel": 600000,
        "misc": 800000,
    },

    "quan": {
        "rent": 4200000,
        "utilities": 900000,
        "food": 2600000,
        "travel": 900000,
        "misc": 1200000,
    },
}
```

For MVP, only process the current playable protagonist’s bills.

Default:

```python
current_bill_profile = "tam"
```

Later, support multiple playable characters.

## 12.2 Bill Calculation

```python
def time_get_monthly_bill_total(profile_id="tam"):
    profile = MONTHLY_BILL_PROFILES.get(profile_id, {})
    return sum(int(v or 0) for v in profile.values())
```

## 12.3 Process Monthly Bills

```python
def time_process_monthly_bills(profile_id="tam"):
    s = ensure_activity_state()

    profile = MONTHLY_BILL_PROFILES.get(profile_id, {})
    total_bill = time_get_monthly_bill_total(profile_id)

    bill_record = {
        "day": s.get("current_day"),
        "month": s.get("calendar_month"),
        "profile_id": profile_id,
        "items": dict(profile),
        "total": total_bill,
        "paid": False,
    }

    if s.get("auto_pay_bills", True) and s.get("money", 0) >= total_bill:
        s["money"] -= total_bill
        bill_record["paid"] = True
        s["paid_bills"].append(bill_record)
        s["unpaid_bill_months"] = 0
        story_flag("monthly_bills_paid")
        s["stress"] = max(0, s["stress"] - 3)
    else:
        s["pending_bills"].append(bill_record)
        s["unpaid_bill_months"] += 1
        story_flag("unpaid_monthly_bills")
        s["stress"] = min(100, s["stress"] + 10)
        s["mood"] = max(0, s["mood"] - 5)

        if s["unpaid_bill_months"] >= 2:
            story_flag("financial_pressure_warning")
```

---

# 13. Weekend and OT Logic

## 13.1 Weekend Rule

Weekend actions are available on Saturday and Sunday.

OT should be available:

* on Saturday/Sunday;
* or during special work-pressure periods.

## 13.2 OT Action

```python
{
    "id": "company_ot_weekend",
    "title": "Weekend OT",
    "summary": "Work overtime during the weekend.",
    "category": "Work",
    "location_id": "company",

    "time_cost": 6,
    "money_cost": 0,

    "requires": {
        "time_points": 6,
        "energy_min": 20,
    },

    "conditions": ["is_weekend"],

    "effects": {
        "time_points": -6,
        "energy": -20,
        "stress": 12,
        "work_skill": 1,
        "main_work_focus": 1,
    },

    "story_effects": {
        "career_tam": 1,
    },

    "daily_limit_key": "company_ot",
    "daily_limit": 1,

    "adds_ot_bonus": 500000,
    "time_skip_allowed": True,

    "message": "Tâm spends part of the weekend at the office. The city outside seems softer when viewed from behind glass."
}
```

## 13.3 Apply OT Bonus

Inside `perform_location_action()` or action effect handler:

```python
if action.get("adds_ot_bonus"):
    s["pending_ot_bonus"] += int(action.get("adds_ot_bonus", 0))
    s["ot_days_this_month"] += 1
```

---

# 14. Action Schema Extensions

Extend existing action schema with:

```python
{
    "daily_limit_key": None,
    "daily_limit": 1,

    "marks_work_completed": False,

    "ends_day": False,
    "sleep_hours": 0,

    "time_skip_allowed": False,
    "time_skip_priority": "normal",

    "important": False,
    "missable": False,
    "expires_after_period_day": None,
    "expires_after_current_day": None,
    "missed_flag": None,

    "adds_ot_bonus": 0,
}
```

## 14.1 Daily Limit Check

```python
def activity_daily_limit_key(action):
    return action.get("daily_limit_key") or action.get("id")


def activity_has_daily_limit_been_used(action):
    s = ensure_activity_state()
    key = activity_daily_limit_key(action)
    return key in s.get("daily_completed_actions", [])


def activity_mark_daily_limit_used(action):
    s = ensure_activity_state()
    key = activity_daily_limit_key(action)

    if key not in s["daily_completed_actions"]:
        s["daily_completed_actions"].append(key)
```

## 14.2 Character Visit Limit

For visit actions:

```python
"daily_limit_key": "visit_character:huyen"
```

This prevents farming the same character repeatedly in one day.

---

# 15. Sleep Actions

Sleep should end the day.

Example:

```python
{
    "id": "sleep_8h_home",
    "title": "Sleep 8 Hours",
    "summary": "End the day with a proper sleep.",
    "category": "Sleep",
    "location_id": "tam_apartment",

    "time_cost": 8,
    "requires": {
        "time_points": 8,
    },

    "effects": {
        "time_points": -8,
        "energy": 35,
        "stress": -15,
        "health": 2,
        "mood": 4,
    },

    "ends_day": True,
    "sleep_hours": 8,
    "time_skip_allowed": True,

    "message": "The room grows quiet. Tâm sleeps before her thoughts can organize themselves into trouble."
}
```

If sleep action is performed:

```python
result = time_end_day(reason="sleep")
```

If `result == "force_next_event"`, jump to the next event.

---

# 16. Time Skip System

## 16.1 Time Skip Menu

Add a map button:

```text
Time Skip
```

Options:

```text
Configure Routine
Skip 1 Day
Skip Until Next Event
Cancel
```

Before skipping, show warning:

```text
Time Skip will automate selected routine actions.
Unselected social or important interactions may be missed.
```

If important interactions are available soon, show a stronger warning.

## 16.2 Routine Plan

Routine data:

```python
s["time_skip_plan"] = [
    "company_work_full_day",
    "sleep_8h_home",
]
```

Only actions with:

```python
"time_skip_allowed": True
```

may be selected.

Do not allow important character interactions in Time Skip by default.

## 16.3 Execute Time Skip

```python
def time_skip_days(days):
    s = ensure_activity_state()

    for _i in range(int(days)):
        time_reset_day()

        for action_id in list(s.get("time_skip_plan", [])):
            action = find_location_action_by_id(action_id)

            if not action:
                continue

            if not action.get("time_skip_allowed", False):
                continue

            if can_perform_location_action(action, silent=True):
                perform_location_action_by_id(action_id, silent=True)

            if time_should_force_next_event():
                return "force_next_event"

        result = time_end_day(reason="time_skip")

        if result == "work_warning_required":
            # If routine does not include work on a workday, record unexcused absence.
            time_skip_work_anyway()
            result = time_end_day(reason="time_skip")

        if result == "force_next_event":
            return "force_next_event"

    return "done"
```

## 16.4 Time Skip Work Warning

If the routine does not include work:

```text
Your routine does not include Work at Company.
Weekdays may be counted as absences.
Continue?
```

---

# 17. Important / Missable Interactions

## 17.1 Action Metadata

```python
{
    "id": "visit_huyen_after_company_party",
    "title": "Visit Huyền",
    "category": "Social",
    "location_id": "huyen_apartment",
    "time_cost": 3,

    "daily_limit_key": "visit_character:huyen",
    "daily_limit": 1,

    "use_scene_router": True,
    "scene_key": "huyen_visit_chat",

    "important": True,
    "missable": True,
    "expires_after_period_day": 5,
    "missed_flag": "missed_huyen_party_followup",

    "time_skip_allowed": False,
}
```

## 17.2 Missing Interaction Processing

```python
def process_daily_missed_interactions():
    s = ensure_activity_state()

    period_id = s.get("current_period_id")
    if not period_id:
        return

    period_day = s.get("period_day", 1)

    for location_id, actions in MAP_LOCATION_ACTIONS.items():
        for action in actions:
            if not action.get("important") or not action.get("missable"):
                continue

            expires = action.get("expires_after_period_day")
            if expires is None:
                continue

            if period_day < expires:
                continue

            action_id = action.get("id")
            missed_flag = action.get("missed_flag")

            if action_id in s.get("completed_actions", []):
                continue

            if action_id in s.get("missed_important_interactions", []):
                continue

            s["missed_important_interactions"].append(action_id)

            if missed_flag:
                story_flag(missed_flag)
```

---

# 18. Map UI Changes

## 18.1 Header

Update `interactive_map_screen()` header to show:

```text
Monday, Month 1 Day 12
Next Event: 16 days
```

Optional:

```text
Time Points: 14 / 24
```

Do not show all stats unless a debug flag is enabled.

## 18.2 Main Today Panel

Show pinned expected actions:

```text
Main Today
! Work at Company — 10 TP
```

Only show this on weekdays when `work_expected_today == True`.

## 18.3 Action Disabled Reasons

An action should show disabled if:

* not enough time points;
* not enough money;
* not enough energy;
* already used daily limit;
* locked by weekday/weekend rule;
* locked by story condition.

Example disabled text:

```text
Already visited today.
```

---

# 19. Map Hub Integration

Modify `map_hub_with_interactions.rpy`.

## 19.1 On Story Hub Entry

Before showing the map:

```renpy
$ ensure_activity_state()
$ setup_day_expectations()
```

## 19.2 After End Day

When an end-day action returns `force_next_event`:

```renpy
$ next_chapter = time_get_next_event_chapter_id()
$ time_clear_current_period()
jump expression CHAPTERS[next_chapter]["label"]
```

Use the existing progression label resolution pattern where possible.

---

# 20. Chapter Migration

## 20.1 Old Pattern

Some chapter wrappers may currently end like this:

```renpy
$ story_complete_chapter("tam_c02_company_party")
$ activity_start_free_time_session(40)
if renpy.has_label("route_map"):
    jump route_map
return
```

## 20.2 New Pattern

Replace with:

```renpy
$ story_complete_chapter("tam_c02_company_party")
$ time_start_period_after_chapter("tam_c02_company_party")
if renpy.has_label("route_map"):
    jump route_map
return
```

If no period exists after that chapter, the call safely returns `False` and the game continues normally.

## 20.3 Migration Rule

Search all story files for:

```text
activity_start_free_time_session
```

Replace based on context:

### Case A — Chapter should start a playable period

```renpy
$ time_start_period_after_chapter("<chapter_id>")
```

### Case B — Chapter should directly continue to next chapter

Remove free-time call entirely.

### Case C — Finale / flashback / montage chapter

Do not start daily period unless explicitly intended.

---

# 21. Chapter Data Migration

For each already implemented chapter:

1. Identify its chapter ID.
2. Determine whether it should start an inter-chapter period.
3. Add period data in `INTER_CHAPTER_PERIODS`.
4. Ensure `next_event` points to the correct chapter.
5. Ensure `duration_days` is set.
6. Ensure the next chapter is still controlled by progression prerequisites.
7. Update chapter wrapper to call `time_start_period_after_chapter()`.

Example:

```python
"after_tam_c01": {
    "id": "after_tam_c01",
    "start_after": "tam_c01_interview_day",
    "next_event": "tam_c02_company_party",
    "duration_days": 7,
    "force_trigger": True,
}
```

Wrapper:

```renpy
label tam_c01_interview_day:
    call tam_c01_interview_day_s01_tam_huyen_morning
    call tam_c01_interview_day_s02_interview_room
    call tam_c01_interview_day_s03_success_result
    call tam_c01_interview_day_s04_celebration_dinner

    $ story_complete_chapter("tam_c01_interview_day")
    $ time_start_period_after_chapter("tam_c01_interview_day")

    if renpy.has_label("route_map"):
        jump route_map
    return
```

---

# 22. Progression Compatibility

Do not remove the existing progression system.

The new time system controls **when** the next event is forced.

The progression system still controls:

* whether a chapter is completed;
* whether prerequisites are met;
* whether a chapter is available;
* route unlocks;
* flags;
* relationship directions;
* endings.

When a forced event is triggered, still use the normal chapter label. The chapter itself must still call:

```renpy
$ story_complete_chapter("<chapter_id>")
```

at completion.

---

# 23. Location Action Migration

## 23.1 Convert `time_units` to `time_points`

Existing actions use:

```python
"time_cost": 1
"requires": {"time_units": 1}
"effects": {"time_units": -1}
```

New actions should use:

```python
"time_cost": 2
"requires": {"time_points": 2}
"effects": {"time_points": -2}
```

For backward compatibility, `perform_location_action()` should support both.

Recommended helper:

```python
def action_get_time_cost(action):
    return int(action.get("time_cost", 0))


def action_has_enough_time(action):
    s = ensure_activity_state()
    cost = action_get_time_cost(action)
    return s.get("time_points", 0) >= cost
```

## 23.2 Compatibility Handler

Inside `perform_location_action()`:

```python
effects = dict(action.get("effects", {}))

if "time_units" in effects and "time_points" not in effects:
    effects["time_points"] = effects.pop("time_units")
```

But for new actions, use `time_points` only.

---

# 24. Company Location Actions

Add to `MAP_LOCATION_ACTIONS["company"]`:

```python
MAP_LOCATION_ACTIONS.setdefault("company", []).extend([
    {
        "id": "company_work_full_day",
        "title": "Work at Company",
        "summary": "Spend a regular workday at the company.",
        "category": "Main",
        "time_cost": 10,
        "money_cost": 0,
        "requires": {"time_points": 10, "energy_min": 15},
        "effects": {
            "time_points": -10,
            "energy": -18,
            "stress": 8,
            "work_skill": 1,
            "main_work_focus": 2,
        },
        "story_effects": {"career_tam": 1},
        "flags": ["worked_company_today"],
        "daily_limit_key": "main_work",
        "daily_limit": 1,
        "marks_work_completed": True,
        "conditions": ["is_workday"],
        "time_skip_allowed": True,
        "time_skip_priority": "main",
        "message": "Tâm spends the day at work. The office lights feel less cold when she leaves before sunset.",
    },
    {
        "id": "company_ot_weekend",
        "title": "Weekend OT",
        "summary": "Work overtime during the weekend.",
        "category": "Work",
        "time_cost": 6,
        "money_cost": 0,
        "requires": {"time_points": 6, "energy_min": 20},
        "effects": {
            "time_points": -6,
            "energy": -20,
            "stress": 12,
            "work_skill": 1,
            "main_work_focus": 1,
        },
        "story_effects": {"career_tam": 1},
        "daily_limit_key": "company_ot",
        "daily_limit": 1,
        "conditions": ["is_weekend"],
        "adds_ot_bonus": 500000,
        "time_skip_allowed": True,
        "message": "Tâm works overtime. Outside, the weekend passes with an unreasonable amount of sunlight.",
    },
])
```

---

# 25. Condition System Extension

Extend `map_condition_is_met()` to support:

```text
is_weekday
is_weekend
is_sunday
workday
not_workday
has_active_period
```

Example:

```python
def map_condition_is_met(condition):
    if condition == "is_weekday":
        return time_is_weekday()

    if condition == "is_weekend":
        return time_is_weekend()

    if condition == "is_sunday":
        return time_is_sunday()

    if condition == "has_active_period":
        return bool(ensure_activity_state().get("current_period_id"))

    # existing condition handling continues here
```

---

# 26. Testing Checklist

## 26.1 Calendar

* New game starts at correct day/month/weekday.
* End Day increments day.
* Month rolls over after 30 days.
* Weekday cycles correctly.
* Map displays correct day/month/weekday.

## 26.2 Work

* Weekday shows Work expected.
* Work costs 10 TP.
* Work marks `work_completed_today = True`.
* End Day without work shows warning.
* Paid Leave resolves work expectation.
* Sick Leave resolves work expectation.
* Skip Work adds absence, penalty, and flag.
* Weekend does not require work.
* Weekend OT appears only on weekend.

## 26.3 Payroll

* Salary is not added daily.
* Salary is paid after 30 days.
* OT bonus is included.
* Absence penalty is included.
* Work counters reset after salary.
* Salary history records correctly.

## 26.4 Bills

* Bills are processed after salary.
* Auto-pay subtracts bills if enough money.
* Insufficient money creates pending bill.
* Unpaid bill increases stress/mood penalty.
* Repeated unpaid bills set `financial_pressure_warning`.

## 26.5 Time Skip

* Routine can be configured.
* Only allowed actions appear in Time Skip routine.
* Time Skip performs work on weekdays if selected.
* Time Skip warns if work is not selected.
* Time Skip processes salary and bills.
* Time Skip stops at forced next event.
* Time Skip records missed important interactions.

## 26.6 Chapter Migration

* No remaining `activity_start_free_time_session()` calls.
* Every migrated chapter starts correct period.
* Chapters without period still return to route map safely.
* Forced next event jumps to correct chapter.
* `story_complete_chapter()` still runs normally.

---

# 27. Implementation Order

Implement in this order:

1. Extend `ensure_activity_state()`.
2. Add calendar helpers.
3. Add period data.
4. Add period start/end logic.
5. Add daily reset and End Day logic.
6. Extend action schema and `perform_location_action()`.
7. Add company work and weekend OT actions.
8. Add payroll.
9. Add monthly bills.
10. Add map header day/month/weekday display.
11. Add End Day / Sleep flow.
12. Add Time Skip screen.
13. Add important/missable interaction processing.
14. Migrate chapter wrappers.
15. Remove old free-time session calls.
16. Run full regression on route map, interactive map, phone, and location hubs.

---

# 28. Non-Goals for MVP

Do not implement these yet:

* true real-world calendar;
* variable month length;
* complex rent contracts;
* detailed tax system;
* per-character full economy simulation;
* hunger/thirst micromanagement;
* forced daily commute action;
* minute/hour clock.

Keep the system light.

The purpose is not to simulate office life accurately.
The purpose is to create meaningful pressure between work, rest, relationships, money, and story deadlines.

---

# 29. Design Decision Summary

Use this final rule set:

```text
Each day has 24 time points.
Work costs 10 time points.
Work is expected on weekdays but not auto-deducted.
Player may work, take leave, call sick, or skip work.
Salary is paid every 30 days.
Bills are processed immediately after salary.
Weekend unlocks OT.
Character/home visits are limited to once per day.
Important interactions can expire.
Time Skip automates only selected safe routine actions.
Next event is manually selectable if available, otherwise forced at deadline.
```

This provides player agency without turning the game into a spreadsheet.

---

# 30. Chapter Event-Span System

## 30.1 New Chapter Metadata Fields

Every chapter in `CHAPTERS` (progression_data.rpy) gets two new fields:

```python
"event_span_days": int,     # How many in-story days the chapter's authored scenes cover
"free_duration_days": int,  # How many free-time days the player has after the chapter (default: 14)
"is_flashback": bool,       # If True, duration does NOT count toward total story days
```

Prologue has no period; it is day 0 and jumps directly to Tam C01.

## 30.2 Day Calculation

The story operates on a simple additive calendar:

```python
# Each non-flashback chapter occupies:
chapter_total_days = event_span_days + free_duration_days

# A chapter's start day:
chapter_start_day = sum of all previous non-flashback chapter_total_days + 1

# Flashback chapters start at a separate offset; their days do NOT accumulate.
```

Total story days across all non-flashback, non-prologue chapters must not exceed 500 days.

## 30.3 Chapter Schedule (First Four)

```text
Prologue:   Day 0         — No period (introduction, jumps to C01)
Tam C01:    Day 1         — event_span 1 day, free_duration 7 days
Tam C02:    Day 9         — event_span 21 days, free_duration 7 days
Tam C03:    Day 30–37     — event_span 7 days, free_duration 30 days [skip allowed]
Tam C04+:   Day 58+       — event_span + free_duration per chapter defaults [skip allowed]
```

## 30.4 Skip Rule

| Chapters | Skip Behavior |
|----------|---------------|
| Prologue | No period (direct jump to next chapter) |
| C01–C02  | Time Skip only to next chapter (no day picking) |
| C03+     | Time Skip can pick any day within the free-duration window to start the next event |

## 30.5 Default Placeholder Duration

For any chapter without explicit `free_duration_days`, use a default of **14 days**. This applies to all chapters beyond the first three, including flashbacks and skeleton chapters.

Flashback chapters use their own calendar offset. Their `free_duration_days` IS counted for their own period but does NOT add to the total story day count.

---

# 31. Updated Period Data

Based on the event-span system, the first two period definitions:

```python
INTER_CHAPTER_PERIODS = {
    "after_tam_c01": {
        "id": "after_tam_c01",
        "start_after": "tam_c01_interview_day",
        "next_event": "tam_c02_company_party",
        "duration_days": 7,          # tam_c01 free_duration_days
        "force_trigger": True,
        "allow_skip_to_any_day": False,  # C01–C02: only skip to next chapter
        "warning_days": [3, 1],
        "allowed_main_actions": ["company_work_full_day", "sleep_8h_home"],
        "important_interactions": [
            "visit_huyen_after_first_job",
        ],
    },

    "after_tam_c02": {
        "id": "after_tam_c02",
        "start_after": "tam_c02_company_party",
        "next_event": "tam_c03_thienan_family",
        "duration_days": 7,          # tam_c02 free_duration_days
        "force_trigger": True,
        "allow_skip_to_any_day": False,
        "warning_days": [7, 3, 1],
        "important_interactions": [
            "huyen_party_followup",
            "hoang_house_casual_followup",
        ],
    },
}

DEFAULT_PERIOD_DURATION_DAYS = 14
```

The chapter ID for Tam C03 has been corrected from `tam_c03_first_salary_week` (spec draft) to `tam_c03_thienan_family` (actual codebase ID). The first salary event is already handled inside Chapter 02 scene `s01b_first_salary_and_shopping`.

---

# 32. Chapter Wrapper Migration Template

Every chapter wrapper currently calling `activity_start_free_time_session(40)` gets:

```renpy
# OLD:
# $ activity_start_free_time_session(40)

# NEW:
$ time_start_period_after_chapter("<chapter_id>")
```

Prologue remains unchanged (no period).

Flashback chapters call the same function but the period system uses a separate flashback calendar that does not accumulate toward the 500-day total.

---

# 33. Story Calendar Reference

```text
Story starts in September 2024.
Calendar format: "Monday, Day 12, September, 2024"

Weekdays: Monday–Sunday (7-day week)
Months:   30 days each (MVP simplification)
Total:    ≤ 500 story days across all non-flashback chapters
```


# updates

1. the fist salary pay check happens in chapter_02 in the scene `s01b_first_salary_...`.
2. Use the new specs in the doc, with `time_points` and new range from (0, 100). 
3. Follow the new doc guidelines for formatting and structuring the code.
4. Replace all done chapter exepts the Prologue since it is like an introduction and should remain unchanged. This spec is missing, update it: 
"""
Each chapter should have an `event-span`: 
 + Prolouge is happened in day 0, 
 + Chapter_01 is at day 1, event-span is 1 day, duration is 7 days; [no skip to next chapter]
 + Chapter_02 is at day 9, event-span is 21 days, duration is 7 days; [no skip to next chapter] // 0 (previous chapter end date) + 1 (day start) + 1 (event span) + 7 (duration for free activity) = 9
 + Chapter_03 is at day 30+ and no later than day 37, event-span is 7 days, duration is 30 days; [allow skip to next chapter] // 
 + Chapter_04 is at day 58+ and no later than day 68, etc.  // 28 + 30 = 58, but we want to allow skipping to any day within the chapter's duration
 
 The first Three chapters would only allow playyer to skip time to the next chapter, but the rest of the chapters will allow player to skip time to any day within the chapter's duration to start the next event.
 The duration should be defined in the chapter's metadata and can be used in the code to calculate time points. So, this means that the time points in each chapter should be calculated based on the chapter's duration and the total duration of the story. For example, if the chapter is 1 day => start at day 1; chapter_02 is 20 days => start at day 21+; chapter_03 is 7 days => start at day 28+, etc. The total duration of the story is the sum of all chapter durations and should not exceed 500 days.
"""
5. keep 2 defines in the docs, other chapters should use placeholder/default value: `14` days and can be changed in the future if needed.
6. For Flashbacks chapters, they should also use the same system, but different durations or calendar days and this duration is not counted in the total duration of the story. The total duration of the story is the sum of all chapter durations which happening after prologue which are not flashbacks and should not exceed 500 days.
7. add missing ones
8. Map subtitles should also add Month name, given that the story is happening in September, 2024.: 
"""
- Monday, Day 12, September, 2024
- Next Event: 16 days
- Optional: Time Points: 14 / 24
"""
