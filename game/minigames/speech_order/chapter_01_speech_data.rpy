# Tam Route - Chapter 01 Speech Mini-game Data
# ============================================================

default tam_speech_attempts = 0
default tam_speech_order = []

init python:

    tam_speech_required_order = [
        "context",
        "coordination",
        "risk",
        "commitment",
    ]

    tam_speech_short_labels = {
        "self_only": _("Self-introduction"),
        "context": _("Understand the company context"),
        "coordination": _("Cross-team coordination"),
        "solo": _("Independent work"),
        "risk": _("Risk awareness"),
        "commitment": _("Work attitude"),
        "salary_first": _("Salary-focused"),
    }

    tam_speech_items = [
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
    ]


    def tam_speech_toggle_choice(picked, item_id):
        if item_id in picked:
            picked.remove(item_id)
        elif len(picked) < 4:
            picked.append(item_id)

        renpy.restart_interaction()


    def tam_speech_order_is_perfect(order):
        return order == tam_speech_required_order


    def tam_speech_order_has_required(order):
        return all(item_id in order for item_id in tam_speech_required_order)
