# FILE: game/story/tam/tam_c04_between_work_and_hearts/s130_w23_group_dinner_new_balance.rpy

label tam_c04_w23_s02_group_dinner_new_balance:
    scene bg_luxury_restaurant_evening
    with dissolve
    scene cg_tam_c04_group_dinner
    with dissolve
    "Bữa tối có Tâm, Huyền, Hoàng và Ánh Nhi. Quân gọi video từ khách sạn đúng lúc món ăn được mang ra."
    scene bg_luxury_restaurant_evening
    with dissolve
    anhni "Bố, chú Hoàng gắp hết hành cho con."
    hoang neutral "Cháu nói như chú vừa phạm tội."
    huyen neutral "Anh ấy đang mua chuộc nhân chứng."
    menu:
        "Ngồi cạnh Hoàng như một điều đã được xác nhận" if story_has_flag("tam_c04_tam_hoang_dating"):
            $ relationship_mark_contact("tam_hoang", "tam_c04_w23", source="story")
            $ story_add("hoang_tam_trust", 3)
            $ story_flag("tam_c04_w23_tam_sits_by_hoang")
            "Hoàng đẩy cốc nước ấm về phía Tâm mà không hỏi. Huyền nhìn thấy nhưng không trêu."
        "Kể với Huyền rằng Tâm và Quang đã nói rõ" if story_has_flag("tam_c04_tam_quang_confirmed"):
            $ story_add("tam_quang_interest", 3)
            $ story_add("tam_self_clarity", 3)
            $ story_flag("tam_c04_w23_tam_tells_huyen_quang")
            huyen surprised "Cuối cùng hai người cũng chịu dùng từ đúng nghĩa à?"
        "Giữ bữa tối ở đúng nghĩa nhóm bạn" if story_has_flag("tam_c04_tam_independent"):
            $ story_add("tam_self_clarity", 5)
            $ story_add("career_tam", 3)
            $ story_flag("tam_c04_w23_tam_keeps_friend_group")
    return
