# FILE: game/story/work/work_c16_project_crisis/s04_minh_boundary_check.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label work_c16_project_crisis_s04_minh_boundary_check:
    "MVP: Minh's emotional availability is checked against the Yuuka state."
    if story_state['minh_romance_lock']:
        "MVP: Minh stays professionally helpful but romantically unavailable."
        $ story_add('tam_self_clarity', 1)
    else:
        "MVP: Minh may become personally closer to Tâm or Thiên An later."
        $ story_add('tam_minh_drawn', 1)
    menu:
        "What does the crisis leave behind?"

        "Professional respect":
            $ story_add('career_tam', 1)

        "Unspoken tension":
            $ story_add('doom_score', 1)

        "A clearer boundary":
            $ story_add('tam_self_clarity', 1)
    return
