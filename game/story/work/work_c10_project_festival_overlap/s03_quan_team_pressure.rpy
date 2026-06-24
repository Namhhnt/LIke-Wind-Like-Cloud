# FILE: game/story/work/work_c10_project_festival_overlap/s03_quan_team_pressure.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label work_c10_project_festival_overlap_s03_quan_team_pressure:
    "MVP: Quân pressures the team to fix the issue properly."
    menu:
        "Who steps up?"

        "Tâm":
            $ story_add('career_tam', 2)

        "Huyền":
            $ story_add('career_huyen', 2)
            $ story_add('huyen_quan_trust', 1)

        "Hoàng":
            $ story_add('hoang_professional_credit', 2)
    return
