# FILE: game/story/work/work_c16_project_crisis/s03_huyen_quan_interaction.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label work_c16_project_crisis_s03_huyen_quan_interaction:
    "MVP: Huyền and Quân clash, then recognize each other's competence."
    menu:
        "How does Huyền handle Quân?"

        "Argue with evidence":
            $ story_add('huyen_quan_trust', 2)
            $ story_add('career_huyen', 1)

        "Deflect with sarcasm":
            $ story_add('career_huyen', 1)

        "Back down too fast":
            $ story_add('doom_score', 1)
    return
