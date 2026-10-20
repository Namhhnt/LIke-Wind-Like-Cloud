# FILE: game/story/tam/tam_c04_between_work_and_hearts/s92_w16_trip_return_delay.rpy

label tam_c04_w16_s02_trip_return_delay:
    scene bg_tam_family_living_room_evening
    with dissolve
    scene cg_tam_c04_quang_thienan_work
    with dissolve
    "Mưa lớn giữ chuyến bay ở lại miền Nam thêm hai ngày."
    scene bg_tam_family_living_room_evening
    with dissolve
    thienan tired "Anh có thể về chuyến sớm hơn. Phần còn lại tôi xử lý được."
    quang "Anh biết."
    thienan neutral "Anh chỉ có một câu đó à?"
    quang "Không. Anh ở lại."
    menu:
        "Thiên An không gạt đi nữa":
            $ story_add("thienan_quang_trust", 7)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 7)
            $ story_flag("tam_c04_w16_thienan_accepts_quang_staying")
            thienan neutral "Vậy đặt thêm một phòng. Đừng ngủ ở ghế."
        "Quang gọi Tâm báo muộn":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 5)
            $ tam_c04_add_extended_score("quang_tam_awareness", 5)
            $ story_flag("tam_c04_w16_quang_calls_tam_delay")
            quang "Anh về muộn hai ngày."
            tam neutral "Em thấy rồi. Nhưng nghe anh nói vẫn khác."
        "Quang gửi một tin chung cho gia đình":
            $ story_add("tam_self_clarity", 3)
            $ story_add("thienan_quang_trust", 3)
            $ story_flag("tam_c04_w16_quang_keeps_family_boundary")
    return
