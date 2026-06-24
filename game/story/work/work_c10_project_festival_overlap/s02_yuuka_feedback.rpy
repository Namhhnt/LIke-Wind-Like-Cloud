# FILE: game/story/work/work_c10_project_festival_overlap/s02_yuuka_feedback.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label work_c10_project_festival_overlap_s02_yuuka_feedback:
    "MVP: Yuuka gives feedback from the perspective of a filmmaker and audience experience."
    menu:
        "How does the team receive Yuuka's feedback?"

        "Tâm applies it carefully":
            $ story_add('career_tam', 2)
            $ story_add('tam_respect_yuuka', 1)

        "Hoàng translates it into design":
            $ story_add('hoang_professional_credit', 2)

        "The team resists it":
            $ story_add('doom_score', 1)
    return
