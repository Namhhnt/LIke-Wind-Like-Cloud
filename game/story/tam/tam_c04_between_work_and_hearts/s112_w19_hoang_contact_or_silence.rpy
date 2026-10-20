# FILE: game/story/tam/tam_c04_between_work_and_hearts/s112_w19_hoang_contact_or_silence.rpy

label tam_c04_w19_s05_hoang_contact_or_silence:
    if not story_has_flag("tam_c04_tam_hoang_dating"):
        return
    scene bg_tam_room_morning
    with dissolve
    scene cg_tam_c04_phone_night
    with dissolve
    "Tối thứ Năm, công việc kéo dài hơn dự kiến. Lịch với Hoàng còn ba mươi phút."
    scene bg_asset_0007
    with dissolve
    menu:
        "Nhắn trước rằng Tâm sẽ muộn":
            $ relationship_mark_contact("tam_hoang", "tam_c04_w19", source="story")
            $ story_add("hoang_tam_trust", 3)
            $ story_flag("tam_c04_w19_tam_warns_hoang_late")
            "Hoàng trả lời: 'Anh đợi thêm bốn mươi phút. Sau đó mình đổi ngày.'"
        "Hủy lịch và đề xuất ngày khác":
            $ relationship_mark_contact("tam_hoang", "tam_c04_w19", source="story")
            $ story_add("tam_self_clarity", 3)
            $ story_flag("tam_c04_w19_tam_reschedules_hoang")
            "Không vui, nhưng rõ. Hoàng gửi lại hai khung giờ."
        "Đợi xong việc mới nhắn":
            $ story_add("career_tam", 5)
            $ story_flag("tam_c04_w19_tam_silences_hoang")
            "Khi Tâm mở điện thoại, Hoàng đã về."
    return
