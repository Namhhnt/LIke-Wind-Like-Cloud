# FILE: game/story/work/work_c10_project_festival_overlap/s01_project_problem.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label work_c10_project_festival_overlap_s01_project_problem:
    "MVP: The company project overlaps with Festival requirements and begins to strain."
    menu:
        "What is the main pressure?"

        "Schedule":
            $ story_add('career_tam', 1)

        "Communication":
            $ story_add('career_huyen', 1)

        "Creative mismatch":
            $ story_add('hoang_professional_credit', 1)
    return
