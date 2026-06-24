# FILE: game/story/tam/tam_c02_company_party/s02_party_start.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label tam_c02_company_party_s02_party_start:
    "MVP: The company party begins after onboarding."
    menu:
        "Where does Tâm stand during the party?"

        "Near Huyền":
            $ story_flag('tam_stays_with_huyen')

        "Near the project table":
            $ story_add('career_tam', 1)

        "Near the quieter side of the room":
            $ story_add('tam_observation', 1)
    return
