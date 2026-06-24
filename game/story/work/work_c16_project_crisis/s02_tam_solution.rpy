# FILE: game/story/work/work_c16_project_crisis/s02_tam_solution.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label work_c16_project_crisis_s02_tam_solution:
    "MVP: Tâm has a chance to propose a useful solution."
    menu:
        "How does Tâm act?"

        "Present a practical fix":
            $ story_add('career_tam', 2)
            $ story_add('tam_self_clarity', 1)

        "Ask Minh for guidance":
            if story_state['minh_romance_lock']:
                $ story_add('career_tam', 1)
                $ story_add('tam_self_clarity', 1)
                "MVP: Because Minh is emotionally locked to Yuuka, this remains professional."
            else:
                $ story_add('tam_minh_drawn', 2)

        "Freeze under pressure":
            $ story_add('doom_score', 2)
    return
