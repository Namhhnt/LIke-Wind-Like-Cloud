# Tam Route - Chapter 01 Speech Mini-game Data
# ============================================================

default tam_speech_attempts = 0
default tam_speech_order = []

init python:

    minigame_register({
        "id": "speech_order",
        "category": "ordering",
        "title": _("Speech Order"),
        "default_variant": "tam_c01_interview",
        "variants": {
            "tam_c01_interview": {
                "title": _("Tam's Speech"),
                "max_choices": 4,
                "max_attempts": 3,
                "required_order": [
                    "context",
                    "coordination",
                    "risk",
                    "commitment",
                ],
                "short_labels": {
                    "self_only": _("Self-introduction"),
                    "context": _("Understand the company context"),
                    "coordination": _("Cross-team coordination"),
                    "solo": _("Independent work"),
                    "risk": _("Risk awareness"),
                    "commitment": _("Work attitude"),
                    "salary_first": _("Salary-focused"),
                },
                "items": [
                    {
                        "id": "self_only",
                        "label": _("Self-introduction: focus on personal strengths, academic achievements, observation, and willingness to learn."),
                    },
                    {
                        "id": "context",
                        "label": _("Project implementation connects construction, materials, IT, legal, accounting, and quality management."),
                    },
                    {
                        "id": "coordination",
                        "label": _("Emphasize coordination skills: track progress, synthesize information, clarify tasks, and keep communication flowing across departments."),
                    },
                    {
                        "id": "solo",
                        "label": _("Independent work ability: I can handle everything on my own without bothering other departments."),
                    },
                    {
                        "id": "risk",
                        "label": _("Talk about risk awareness: spot issues early, report transparently, and keep small mistakes from becoming major problems."),
                    },
                    {
                        "id": "commitment",
                        "label": _("Work attitude: learn quickly, visit the site when needed, respect process, and take responsibility for my part of the work."),
                    },
                    {
                        "id": "salary_first",
                        "label": _("Say that salary matters most because I want to be evaluated for my true worth."),
                    },
                ],
                "outcomes": {
                    "skip": {
                        "summary": _("Tam gives a safe answer without a bonus reward."),
                        "effects": {
                            "progress_flags_add": ["tam_interview_pass_skip_no_bonus", "tam_salary_standard_start"],
                            "store_variables_set": [{"key": "tam_salary_tier", "value": "standard"}],
                        },
                    },
                    "pass": {
                        "summary": _("Tam covers the important points and passes the interview."),
                        "effects": {
                            "progress_flags_add": ["tam_interview_passed", "tam_salary_standard_start"],
                            "store_variables_set": [{"key": "tam_salary_tier", "value": "standard"}],
                            "store_variables_add": [{"key": "tam_work_skill", "amount": 1}, {"key": "tam_confidence", "amount": 1}],
                            "investment_points": 1,
                        },
                    },
                    "perfect": {
                        "summary": _("Tam structures the answer perfectly and earns the stronger outcome."),
                        "effects": {
                            "progress_flags_add": ["tam_interview_passed", "tam_interview_bonus_order", "tam_salary_high_start", "tam_work_skill_strong_c01"],
                            "store_variables_set": [{"key": "tam_salary_tier", "value": "high"}],
                            "store_variables_add": [{"key": "tam_work_skill", "amount": 2}, {"key": "tam_confidence", "amount": 2}],
                            "investment_points": 2,
                        },
                    },
                },
            },
        },
    })

    def tam_speech_variant():
        return minigame_get_variant("speech_order", "tam_c01_interview")


    def tam_speech_required_order():
        return list(tam_speech_variant().get("required_order", []))


    def tam_speech_short_labels():
        return dict(tam_speech_variant().get("short_labels", {}))


    def tam_speech_items():
        return list(tam_speech_variant().get("items", []))


    def tam_speech_toggle_choice(picked, item_id):
        max_choices = tam_speech_variant().get("max_choices", 4)
        if item_id in picked:
            picked.remove(item_id)
        elif len(picked) < max_choices:
            picked.append(item_id)

        renpy.restart_interaction()


    def tam_speech_order_is_perfect(order):
        return order == tam_speech_required_order()


    def tam_speech_order_has_required(order):
        return all(item_id in order for item_id in tam_speech_required_order())


    # ------------------------------------------------------------------
    # Generic helpers for speech-order variants used by library replay.
    # These work with any variant's required_order list.
    # ------------------------------------------------------------------
    def tam_speech_order_is_perfect_for_list(order, required_order):
        if not required_order:
            return False
        if len(order) < len(required_order):
            return False
        return list(order)[:len(required_order)] == list(required_order)


    def tam_speech_order_has_required_for_list(order, required_order):
        return all(item_id in order for item_id in required_order)


    def tam_speech_short_labels_for_variant(variant):
        return dict(variant.get("short_labels", {}))


    def tam_speech_toggle_choice_generic(picked, item_id, max_choices):
        if item_id in picked:
            picked.remove(item_id)
        elif len(picked) < max_choices:
            picked.append(item_id)
        renpy.restart_interaction()
