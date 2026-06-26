# FILE: game/minigames/library_minigame_data.rpy
# Purpose: Library-accessible minigame variants + replay labels.
# Each minigame variant is registered in the minigame engine, then
# exposed as a library item so players can replay it from Library -> Minigames.
#
# Replay flow:
#   - Prerequisite chapter completion makes the library item available (free unlock mode).
#   - Replay calls a dedicated label that runs the minigame screens without story effects.

init python:
    # ------------------------------------------------------------------
    # HOÀNG — Gift Choice (speech_order variant)
    # Hoàng is choosing a gift for his brother Minh.
    # The right order is: thoughtfulness > practicality > personal attachment > convenience.
    # ------------------------------------------------------------------
    minigame_register({
        "id": "speech_order",
        "category": "ordering",
        "title": _("Speech Order"),
        "default_variant": "tam_c01_interview",
        "variants": {
            "hoang_h01_gift_choice": {
                "title": _("Hoàng's Gift Choice"),
                "max_choices": 4,
                "max_attempts": 3,
                "required_order": [
                    "thoughtfulness",
                    "practicality",
                    "personal",
                    "convenience",
                ],
                "short_labels": {
                    "thoughtfulness": _("Thoughtfulness"),
                    "practicality": _("Practicality"),
                    "time_together": _("Time together"),
                    "personal": _("Personal sentiment"),
                    "convenience": _("Ease of purchase"),
                    "appearance": _("Looks impressive"),
                },
                "items": [
                    {
                        "id": "thoughtfulness",
                        "label": _("Choose something that shows you understand what he values, not just what looks expensive on the surface."),
                    },
                    {
                        "id": "practicality",
                        "label": _("Something useful he would actually need day to day, even if it is not flashy."),
                    },
                    {
                        "id": "time_together",
                        "label": _("Just spend time with him — a meal, a walk, or a quiet afternoon. The gift itself does not matter that much."),
                    },
                    {
                        "id": "personal",
                        "label": _("A gift tied to a shared memory, something only the two of you would understand."),
                    },
                    {
                        "id": "convenience",
                        "label": _("Buy whatever is easiest to get — last minute is fine as long as there is something to give."),
                    },
                    {
                        "id": "appearance",
                        "label": _("Pick something that looks impressive when others see it, even if it has little personal meaning."),
                    },
                ],
                "outcomes": {
                    "perfect": {
                        "summary": _("Hoàng picks a gift with genuine thought — it shows he is learning to care beyond himself."),
                        "effects": {},
                    },
                    "pass": {
                        "summary": _("Hoàng chooses reasonably well, though the reasoning is still a little scattered."),
                        "effects": {},
                    },
                    "skip": {
                        "summary": _("Hoàng picks something safe and convenient. Minh will not complain, but he will notice."),
                        "effects": {},
                    },
                },
            },
            # ------------------------------------------------------------------
            # YUUKA — Director Speech (speech_order variant)
            # Yuuka is presenting her festival directorship plan.
            # Right order: vision > structure > execution > connection.
            # ------------------------------------------------------------------
            "yuuka_c08_director_speech": {
                "title": _("Yuuka's Director Speech"),
                "max_choices": 4,
                "max_attempts": 3,
                "required_order": [
                    "vision",
                    "structure",
                    "execution",
                    "connection",
                ],
                "short_labels": {
                    "vision": _("Festival vision"),
                    "structure": _("Event structure"),
                    "team": _("Team roles"),
                    "execution": _("Execution plan"),
                    "connection": _("Community connection"),
                    "budget": _("Budget constraints"),
                },
                "items": [
                    {
                        "id": "vision",
                        "label": _("Start with the why: what the festival means for the community and why people should care."),
                    },
                    {
                        "id": "structure",
                        "label": _("Lay out the event framework: schedule, venue layout, key activities, and participant flow."),
                    },
                    {
                        "id": "team",
                        "label": _("Introduce the team: who is responsible for each area and how they will coordinate."),
                    },
                    {
                        "id": "execution",
                        "label": _("Explain how the plan gets done: timelines, milestones, fallback options for bad weather or low turnout."),
                    },
                    {
                        "id": "connection",
                        "label": _("Close with the human side: how this festival brings people together and what success looks like in their eyes."),
                    },
                    {
                        "id": "budget",
                        "label": _("Lead with the numbers: budget breakdown and fundraising targets before anything else."),
                    },
                ],
                "outcomes": {
                    "perfect": {
                        "summary": _("Yuuka delivers a compelling, well-structured pitch that earns real buy-in from the room."),
                        "effects": {},
                    },
                    "pass": {
                        "summary": _("Yuuka covers the essentials. The presentation works, though it lacks some polish."),
                        "effects": {},
                    },
                    "skip": {
                        "summary": _("Yuuka sticks to safe talking points. The presentation does not leave a strong impression."),
                        "effects": {},
                    },
                },
            },
        },
    })

    # ------------------------------------------------------------------
    # Problem diagnosis — Team Communication Breakdown
    # A case about a cross-team miscommunication that caused rework.
    # The variant is registered to the minigame engine. The case data
    # is stored in a local variable and added to PD_CASES at init 1
    # (after problem_diagnosis_data.rpy defines the PD_CASES dict).
    # ------------------------------------------------------------------
    _team_conflict_variant_config = {
        "title": _("Team Conflict Diagnosis"),
        "outcomes": {
            "excellent": {
                "summary": _("The diagnosis cuts to the real cause — process failure, not people failure."),
                "effects": {},
            },
            "good": {
                "summary": _("Solid diagnosis with concrete next steps. The team can recover."),
                "effects": {},
            },
            "mixed": {
                "summary": _("The analysis identifies some issues but misses the deeper communication breakdown."),
                "effects": {},
            },
            "poor": {
                "summary": _("The diagnosis stays surface level. The same conflict is likely to resurface."),
                "effects": {},
            },
        },
        "result_tiers": {
            "excellent": {"investment_points": 3, "story_flags_add": ["pd_team_conflict_excellent"]},
            "good": {"investment_points": 2, "story_flags_add": ["pd_team_conflict_good"]},
            "mixed": {"investment_points": 1, "story_flags_add": ["pd_team_conflict_mixed"]},
            "poor": {"investment_points": 0, "story_flags_add": ["pd_team_conflict_poor"]},
        },
    }

    minigame_register({
        "id": "problem_diagnosis",
        "category": "analysis",
        "title": _("Problem Diagnosis"),
        "default_variant": "case_scope_creep_01",
        "variants": {
            "case_team_conflict_01": _team_conflict_variant_config,
        },
    })

    _team_conflict_case_data = {
        "title": "Conflict Diagnosis",
        "subtitle_phase_1": "Phase 1 — Gather / Analyze / Organize",
        "subtitle_phase_2": "Phase 2 — Resolution / Actions / PIC",
        "debug_title": "Team Conflict Debug",
        "case_title": "Cross-Team Miscommunication",
        "description": "Two teams delivered overlapping work with conflicting specifications, causing a week of rework.",
        "phase_1_required_score": 60,
        "guide_name": "Minh",
        "guide_quote_phase_1": "Facts first. Blame later. Separate what happened from who you think is at fault.",
        "guide_quote_phase_2": "A good resolution fixes the process, not just the symptom.",
        "notes": [
            "Distinguish between miscommunication, assumption, and negligence.",
            "A root cause explains why the process broke. An impact shows what it already damaged.",
            "Choose owners who can change the process, not just patch the current issue.",
        ],
        "data_cards": [
            {
                "id": "D01",
                "type": "raw",
                "title": "Two teams received different specs",
                "description": "Team A and Team B each received a different version of the requirement document.",
                "tags": ["requirement", "process", "communication"],
            },
            {
                "id": "D02",
                "type": "raw",
                "title": "Spec version was not tracked",
                "description": "No one noticed the versions diverged because there was no central revision log.",
                "tags": ["process", "documentation"],
            },
            {
                "id": "D03",
                "type": "raw",
                "title": "Rework cost 5 engineering days",
                "description": "Integration testing failed and both teams had to realign their work.",
                "tags": ["impact", "timeline"],
            },
            {
                "id": "D04",
                "type": "raw",
                "title": "Blame was directed at one junior member",
                "description": "A junior engineer was singled out for the mismatch, though they followed the spec they received.",
                "tags": ["team", "culture", "people"],
            },
            {
                "id": "D05",
                "type": "raw",
                "title": "No cross-team sync was scheduled",
                "description": "Both teams worked independently for two weeks without a checkpoint meeting.",
                "tags": ["communication", "process"],
            },
            {
                "id": "D06",
                "type": "raw",
                "title": "Deadline was not adjusted after rework",
                "description": "The original delivery date stayed unchanged despite the lost week.",
                "tags": ["timeline", "risk"],
            },
        ],
        "insight_cards": {
            "I01": {
                "id": "I01",
                "type": "insight",
                "title": "No single source of truth for specs",
                "description": "Without a central requirement repository, version drift was inevitable.",
                "tags": ["process", "root_cause"],
            },
            "I02": {
                "id": "I02",
                "type": "insight",
                "title": "Cross-team communication gap",
                "description": "No structured sync between teams created silos that hid the misalignment.",
                "tags": ["communication", "root_cause"],
            },
            "I03": {
                "id": "I03",
                "type": "insight",
                "title": "Blame culture undermines process improvement",
                "description": "Pointing fingers at individuals discourages honest reporting and prevents systemic fixes.",
                "tags": ["culture", "impact"],
            },
        },
        "analysis_recipes": [
            {
                "id": "R01",
                "requires": ["D01", "D02"],
                "creates": "I01",
                "success_feedback": "The spec version gap is a process failure, not a people failure.",
                "fail_feedback": "These facts touch the spec issue but don't point to the root yet.",
            },
            {
                "id": "R02",
                "requires": ["D01", "D05"],
                "creates": "I02",
                "success_feedback": "The real gap was not between specs, but between teams who never synced.",
                "fail_feedback": "You see the communication problem, but not the structural gap behind it.",
            },
            {
                "id": "R03",
                "requires": ["D04", "D03"],
                "creates": "I03",
                "success_feedback": "Blaming individuals hides the system flaw. This insight reframes the issue.",
                "fail_feedback": "These facts are related, but they don't yet reveal the cultural pattern.",
            },
        ],
        "organize_rules": {
            "root_cause_best": ["I01", "I02"],
            "root_cause_accepted": ["D01", "D05"],
            "impact_best": ["D03", "D06", "I03"],
            "impact_accepted": ["D04"],
            "noise": ["D02"],
        },
        "actions": [
            {
                "id": "A01",
                "title": "Establish a single spec repository",
                "description": "Create a central version-controlled requirement document accessible to both teams.",
                "tags": ["priority", "process"],
                "unlocked_if": ["I01"],
            },
            {
                "id": "A02",
                "title": "Implement cross-team sync meetings",
                "description": "Schedule a biweekly checkpoint between teams to catch alignment issues early.",
                "tags": ["priority", "communication"],
                "unlocked_if": ["I02"],
            },
            {
                "id": "A03",
                "title": "Conduct a blameless post-mortem",
                "description": "Review what happened without assigning fault — focus on process gaps.",
                "tags": ["culture", "process"],
                "unlocked_if": [],
            },
            {
                "id": "A04",
                "title": "Revise the deadline with stakeholder buy-in",
                "description": "Negotiate a realistic timeline that accounts for the rework already done.",
                "tags": ["timeline", "risk"],
                "unlocked_if": [],
            },
            {
                "id": "A05",
                "title": "Create a shared glossary for requirements",
                "description": "Define key terms and acceptance criteria so both teams interpret specs the same way.",
                "tags": ["communication", "process"],
                "unlocked_if": [],
            },
        ],
        "pics": [
            {"id": "P_TAM", "name": "Tâm", "role": "Project coordinator"},
            {"id": "P_MINH", "name": "Minh", "role": "Mentor / senior lead"},
            {"id": "P_QUAN", "name": "Quân", "role": "Project manager"},
            {"id": "P_HUYEN", "name": "Huyền", "role": "Cross-team coordinator"},
            {"id": "P_CLIENT_PM", "name": "Client PM", "role": "Client-side owner"},
        ],
        "pic_rules": {
            "A01": {
                "best": ["P_QUAN"],
                "accepted": ["P_TAM"],
                "wrong_but_understandable": ["P_MINH"],
            },
            "A02": {
                "best": ["P_HUYEN"],
                "accepted": ["P_TAM"],
            },
            "A03": {
                "best": ["P_MINH"],
                "accepted": ["P_HUYEN"],
            },
            "A04": {
                "best": ["P_QUAN"],
                "accepted": ["P_CLIENT_PM"],
            },
            "A05": {
                "best": ["P_TAM"],
                "accepted": ["P_HUYEN"],
            },
        },
    }

init 1 python:
    # Add team conflict case to PD_CASES after problem_diagnosis_data.rpy has defined the dict.
    PD_CASES["case_team_conflict_01"] = _team_conflict_case_data

    # ------------------------------------------------------------------
    # Library item registrations for each minigame variant.
    # These register into library_items so the Library -> Minigames screen
    # can display them with prerequisites and unlock state.
    # ------------------------------------------------------------------
    ensure_story_library_defaults()

    # Tam's Speech (tam_c01_interview) — already exists in story, add library entry
    register_library_item({
        "id": "minigame_speech_tam_c01",
        "title": _("Tam's Interview Speech"),
        "category": "minigames",
        "series": _("Speech Order"),
        "type": "minigame_speech_order",
        "size": "small",
        "point_cost": 0,
        "unlock_mode": "free",
        "prerequisites": ["tam_c01_interview_day"],
        "tags": ["minigame", "speech_order", "tam", "chapter_01"],
        "cover": "",
    })

    # Hoàng's Gift Choice (hoang_h01_gift_choice)
    register_library_item({
        "id": "minigame_speech_hoang_h01",
        "title": _("Hoàng's Gift Choice"),
        "category": "minigames",
        "series": _("Speech Order"),
        "type": "minigame_speech_order",
        "size": "small",
        "point_cost": 0,
        "unlock_mode": "free",
        "prerequisites": ["hoang_h01_brother_house"],
        "tags": ["minigame", "speech_order", "hoang", "chapter_01"],
        "cover": "",
    })

    # Yuuka's Director Speech (yuuka_c08_director_speech)
    register_library_item({
        "id": "minigame_speech_yuuka_c08",
        "title": _("Yuuka's Director Speech"),
        "category": "minigames",
        "series": _("Speech Order"),
        "type": "minigame_speech_order",
        "size": "small",
        "point_cost": 0,
        "unlock_mode": "free",
        "prerequisites": ["yuuka_c08_festival_arrival"],
        "tags": ["minigame", "speech_order", "yuuka", "chapter_08"],
        "cover": "",
    })

    # Problem Diagnosis — Scope Creep (case_scope_creep_01) — existing case, add library entry
    register_library_item({
        "id": "minigame_pd_scope_creep",
        "title": _("Project Diagnosis: Scope Creep"),
        "category": "minigames",
        "series": _("Problem Diagnosis"),
        "type": "minigame_problem_diagnosis",
        "size": "medium",
        "point_cost": 0,
        "unlock_mode": "free",
        "prerequisites": ["work_c10_project_festival_overlap"],
        "tags": ["minigame", "problem_diagnosis", "work", "project"],
        "cover": "",
    })

    # Problem Diagnosis — Team Conflict (case_team_conflict_01)
    register_library_item({
        "id": "minigame_pd_team_conflict",
        "title": _("Conflict Diagnosis: Communication Breakdown"),
        "category": "minigames",
        "series": _("Problem Diagnosis"),
        "type": "minigame_problem_diagnosis",
        "size": "medium",
        "point_cost": 0,
        "unlock_mode": "free",
        "prerequisites": ["work_c16_project_crisis"],
        "tags": ["minigame", "problem_diagnosis", "work", "conflict"],
        "cover": "",
    })


# ------------------------------------------------------------------
# Helper: map library content ID to minigame replay parameters.
# Each library minigame entry points to a replay label with specific args.
# ------------------------------------------------------------------
init python:
    MINIGAME_LIBRARY_REPLAY_MAP = {
        "minigame_speech_tam_c01": {
            "minigame_id": "speech_order",
            "variant_id": "tam_c01_interview",
            "replay_label": "library_replay_speech_order",
        },
        "minigame_speech_hoang_h01": {
            "minigame_id": "speech_order",
            "variant_id": "hoang_h01_gift_choice",
            "replay_label": "library_replay_speech_order",
        },
        "minigame_speech_yuuka_c08": {
            "minigame_id": "speech_order",
            "variant_id": "yuuka_c08_director_speech",
            "replay_label": "library_replay_speech_order",
        },
        "minigame_pd_scope_creep": {
            "minigame_id": "problem_diagnosis",
            "variant_id": "case_scope_creep_01",
            "replay_label": "library_replay_problem_diagnosis",
        },
        "minigame_pd_team_conflict": {
            "minigame_id": "problem_diagnosis",
            "variant_id": "case_team_conflict_01",
            "replay_label": "library_replay_problem_diagnosis",
        },
    }

    def get_minigame_library_replay_info(content_id):
        return MINIGAME_LIBRARY_REPLAY_MAP.get(content_id)


# ------------------------------------------------------------------
# Replay labels — these launch the minigame screens without applying
# story effects or mutating progression state.
#
# Each label:
#   1. Looks up the variant config
#   2. Runs the minigame screen(s) in display-only mode
#   3. Shows a result summary
#   4. Returns to the library menu
# ------------------------------------------------------------------

label library_replay_speech_order(content_id="minigame_speech_tam_c01"):
    $ replay_info = get_minigame_library_replay_info(content_id)
    if not replay_info:
        "Minigame info not found."
        return

    $ config = minigame_get_config(replay_info["minigame_id"])
    $ variant = minigame_get_variant(config, replay_info["variant_id"])
    $ speech_pool = list(variant.get("items", []))
    $ renpy.random.shuffle(speech_pool)

    $ _library_replay_result = renpy.call_screen(
        "lib_speech_minigame",
        items=speech_pool,
        variant=variant,
        attempt=1,
        can_skip=True,
    )

    if _library_replay_result.get("action") == "skip":
        "You chose to skip this minigame."
        return

    $ _selected = list(_library_replay_result.get("picked", []))
    $ _required_order = variant.get("required_order", [])
    $ _has_required = tam_speech_order_has_required_for_list(_selected, _required_order)
    $ _is_perfect = tam_speech_order_is_perfect_for_list(_selected, _required_order)

    if _is_perfect:
        "Perfect order! You structured the response in the ideal sequence."
    elif _has_required:
        "Good effort — you covered the essential points, though the order could be improved."
    else:
        "You missed some key points this time. Try again for a stronger outcome."
    return


label library_replay_problem_diagnosis(content_id="minigame_pd_scope_creep"):
    $ replay_info = get_minigame_library_replay_info(content_id)
    if not replay_info:
        "Minigame info not found."
        return

    $ _pd_case_id = replay_info["variant_id"]
    $ pd_prepare_case(_pd_case_id)
    $ renpy.call_screen("problem_diagnosis_minigame")

    if pd_last_result:
        $ _summary = pd_last_result.get("summary", "Diagnosis complete.")
        "[_summary]"
    else:
        "Diagnosis complete."
    return
