# FILE: game/story/hoang/hoang_h01_brother_house/s02_minh_remote_presence.rpy
# MVP scene file. Replace placeholder text later; keep label name stable.

label hoang_h01_brother_house_s02_minh_remote_presence:
    "MVP: Minh appears through a call/message, giving Hoàng practical advice."
    menu:
        "What does Hoàng ask Minh about?"

        "A gift for Tâm":
            $ story_add('hoang_tam_trust', 1)
            $ story_add_direction('hoang', 'hoang_tam_open')

        "A gift for Huyền":
            $ story_add('hoang_huyen_interest', 1)
            $ story_add_direction('hoang', 'hoang_huyen_open')

        "A work-related design issue":
            $ story_add('hoang_professional_credit', 2)
    return
