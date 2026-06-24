# FILE: game/story/work/work_c16_project_crisis/s01_crisis_setup.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label work_c16_project_crisis_s01_crisis_setup:
    "MVP: The project reaches a real crisis."
    menu:
        "What breaks first?"

        "Timeline":
            $ story_add('career_tam', 1)

        "Team trust":
            $ story_add('doom_score', 1)

        "Client expectation":
            $ story_add('career_huyen', 1)
    return
