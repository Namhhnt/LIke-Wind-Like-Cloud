# FILE: game/story/work/work_c10_project_festival_overlap/s04_career_or_relationship_choice.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label work_c10_project_festival_overlap_s04_career_or_relationship_choice:
    "MVP: Work pressure pushes hidden relationships into view."
    menu:
        "Where does the scene push?"

        "Tâm career growth":
            $ story_add('career_tam', 2)

        "Huyền and Quân respect":
            $ story_add('huyen_quan_trust', 2)

        "Hoàng earns credibility":
            $ story_add('hoang_professional_credit', 2)
    return
