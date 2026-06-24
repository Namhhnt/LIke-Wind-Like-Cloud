# FILE: game/story/huyen/huyen_c22_quan_or_hoang/s02_quan_professional_respect.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label huyen_c22_quan_or_hoang_s02_quan_professional_respect:
    "MVP: Huyền and Quân either gain respect or remain only workplace friction."
    menu:
        "How does Huyền answer Quân?"

        "With competence":
            $ story_add('huyen_quan_trust', 2)
            $ story_add_ending_support('e05_huyen_quan')

        "With jokes only":
            $ story_add('career_huyen', 1)

        "With avoidance":
            $ story_add('doom_score', 1)
    return
