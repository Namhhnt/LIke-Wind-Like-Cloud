default pd_state = {}
default pd_last_result = None
default pd_debug_last_result = None


init python:
    PD_MIN_ANALYZE_SELECTION = 2
    PD_MAX_ANALYZE_SELECTION = 4
    PD_SLOT_LIMIT = 4

    minigame_register({
        "id": "problem_diagnosis",
        "category": "analysis",
        "title": _("Problem Diagnosis"),
        "default_variant": "case_scope_creep_01",
        "variants": {
            "case_scope_creep_01": {
                "title": _("Project Diagnosis"),
                "outcomes": {
                    "excellent": {
                        "summary": _("The diagnosis is sharp, actionable, and well owned."),
                        "effects": {},
                    },
                    "good": {
                        "summary": _("The diagnosis is solid and keeps the project on track."),
                        "effects": {},
                    },
                    "mixed": {
                        "summary": _("The diagnosis works, but leaves avoidable risk behind."),
                        "effects": {},
                    },
                    "poor": {
                        "summary": _("The diagnosis is weak and the team moves forward with limited clarity."),
                        "effects": {},
                    },
                },
                "result_tiers": {
                    "excellent": {"investment_points": 3, "story_flags_add": ["pd_scope_creep_excellent"]},
                    "good": {"investment_points": 2, "story_flags_add": ["pd_scope_creep_good"]},
                    "mixed": {"investment_points": 1, "story_flags_add": ["pd_scope_creep_mixed"]},
                    "poor": {"investment_points": 0, "story_flags_add": ["pd_scope_creep_poor"]},
                },
            },
        },
    })

    PD_CASES = {
        "case_scope_creep_01": {
            "title": "Project Diagnosis",
            "subtitle_phase_1": "Phase 1 — Data / Analyze / Organize",
            "subtitle_phase_2": "Phase 2 — Solution / Actions / PIC",
            "debug_title": "Problem Diagnosis Debug",
            "case_title": "Demo Mismatch",
            "description": "The project demo does not match the client's expectation.",
            "phase_1_required_score": 60,
            "guide_name": "Minh",
            "guide_quote_phase_1": "Raw facts are only useful after you organize them into something the team can act on.",
            "guide_quote_phase_2": "A good solution becomes real only when the right person owns it.",
            "notes": [
                "Confirm what is fact, what is interpretation, and what is only noise.",
                "A root cause explains why the problem exists. An impact shows what it is already hurting.",
                "Choose owners who can actually move the project, not just people closest to the issue.",
            ],
            "data_cards": [
                {
                    "id": "D01",
                    "type": "raw",
                    "title": "Client changed requirement 3 times",
                    "description": "The expected output changed three times within two weeks.",
                    "tags": ["requirement", "client", "scope"],
                },
                {
                    "id": "D02",
                    "type": "raw",
                    "title": "Team said they understood the scope",
                    "description": "The team verbally confirmed the scope after the meeting.",
                    "tags": ["team", "communication"],
                },
                {
                    "id": "D03",
                    "type": "raw",
                    "title": "Demo output mismatched expectation",
                    "description": "The demo did not match what the client expected.",
                    "tags": ["demo", "impact"],
                },
                {
                    "id": "D04",
                    "type": "raw",
                    "title": "No meeting note after discussion",
                    "description": "No written confirmation was created after the requirement discussion.",
                    "tags": ["process", "requirement", "communication"],
                },
                {
                    "id": "D05",
                    "type": "raw",
                    "title": "Deadline unchanged despite scope increase",
                    "description": "Timeline remained unchanged even after new requests were added.",
                    "tags": ["timeline", "scope", "impact"],
                },
                {
                    "id": "D06",
                    "type": "raw",
                    "title": "Tâm did not escalate risk",
                    "description": "Tâm noticed the timeline risk but hesitated to escalate.",
                    "tags": ["risk", "owner", "communication"],
                },
            ],
            "insight_cards": {
                "I01": {
                    "id": "I01",
                    "type": "insight",
                    "title": "Requirement baseline was never confirmed",
                    "description": "There is no single source of truth for the agreed requirement.",
                    "tags": ["requirement", "baseline", "root_cause"],
                },
                "I02": {
                    "id": "I02",
                    "type": "insight",
                    "title": "Scope creep was not controlled",
                    "description": "New requests were accepted without timeline or scope adjustment.",
                    "tags": ["scope", "root_cause"],
                },
                "I03": {
                    "id": "I03",
                    "type": "insight",
                    "title": "Timeline risk was not escalated",
                    "description": "The risk was visible but not raised early enough.",
                    "tags": ["timeline", "impact", "risk"],
                },
            },
            "analysis_recipes": [
                {
                    "id": "R01",
                    "requires": ["D01", "D03", "D04"],
                    "creates": "I01",
                    "success_feedback": "The requirement baseline was unclear.",
                    "fail_feedback": "These facts are related, but they do not create a clear insight yet.",
                },
                {
                    "id": "R02",
                    "requires": ["D01", "D05"],
                    "creates": "I02",
                    "success_feedback": "Scope increased without control.",
                    "fail_feedback": "This points to pressure, but not to the source of the project drift.",
                },
                {
                    "id": "R03",
                    "requires": ["D05", "D06"],
                    "creates": "I03",
                    "success_feedback": "Timeline risk was not escalated early enough.",
                    "fail_feedback": "You noticed the tension, but not the ownership gap behind it.",
                },
            ],
            "organize_rules": {
                "root_cause_best": ["I01", "I02"],
                "root_cause_accepted": ["D01", "D04"],
                "impact_best": ["D03", "D05", "I03"],
                "impact_accepted": ["D06"],
                "noise": ["D02"],
            },
            "actions": [
                {
                    "id": "A01",
                    "title": "Confirm requirement baseline with client",
                    "description": "Run a confirmation meeting and document the agreed requirement.",
                    "tags": ["priority", "communication"],
                    "unlocked_if": ["I01"],
                },
                {
                    "id": "A02",
                    "title": "Create a formal change request",
                    "description": "Document scope additions and obtain approval.",
                    "tags": ["priority", "scope"],
                    "unlocked_if": ["I02"],
                },
                {
                    "id": "A03",
                    "title": "Split demo into must-have and optional items",
                    "description": "Separate required demo items from optional improvements.",
                    "tags": ["planning", "timeline"],
                    "unlocked_if": [],
                },
                {
                    "id": "A04",
                    "title": "Escalate timeline risk before end of day",
                    "description": "Raise the timeline risk formally before the next reporting cycle.",
                    "tags": ["timeline", "risk"],
                    "unlocked_if": [],
                },
                {
                    "id": "A05",
                    "title": "Centralize feedback into one official channel",
                    "description": "Stop scattered feedback from chat, calls, and informal comments.",
                    "tags": ["communication"],
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
                    "accepted": ["P_CLIENT_PM"],
                    "wrong_but_understandable": ["P_TAM"],
                },
                "A02": {
                    "best": ["P_QUAN"],
                    "accepted": ["P_MINH"],
                },
                "A03": {
                    "best": ["P_TAM"],
                    "accepted": ["P_QUAN"],
                },
                "A04": {
                    "best": ["P_TAM"],
                    "accepted": ["P_QUAN"],
                },
                "A05": {
                    "best": ["P_HUYEN"],
                    "accepted": ["P_TAM"],
                },
            },
        },
    }
