label tam_c04_w10_s01_monday_phone_pulse:
    scene bg_tam_room_morning
    with fade
    $ story_flag("tam_c04_w10_started")
    $ phone_refresh_all()
    scene cg_tam_c04_phone_morning
    with dissolve
    "Sáng thứ Hai, nhóm dự án nhận một mail có tiêu đề: URGENT — thay đổi nội dung trước bản demo."
    scene bg_tam_room_morning
    with dissolve
    "Tin của Huyền đến trước cả chuông báo thứ hai."
    huyen neutral "Tao ghét chữ urgent viết hoa."
    if story_has_flag("tam_c04_w09_focus_hoang"):
        "Hoàng nhắn rằng anh sẽ không giữ lịch nếu Tâm chưa biết mình tan làm lúc nào."
    elif story_state.get("tam_hoang_interest", 0) >= 55:
        "Hoàng chỉ gửi: tuần này em lo việc trước đi."
    if story_has_flag("tam_c04_w09_focus_quang_thienan"):
        "Quang báo Thiên An đã đóng lịch hai ngày để xử lý việc gia đình."
    elif story_has_flag("tam_c04_w09_focus_quang_personal"):
        "Quang hỏi Tâm có cần anh mang bữa sáng tới công ty không."
    "Một tuần mới bắt đầu bằng việc không ai có thể đứng thay hoàn toàn cho ai."
    return
