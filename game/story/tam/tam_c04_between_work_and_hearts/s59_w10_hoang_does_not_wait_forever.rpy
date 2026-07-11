label tam_c04_w10_s03_hoang_does_not_wait_forever:
    $ _active = story_state.get("tam_hoang_interest", 0) >= 55
    if not _active:
        $ story_add("career_hoang", 5)
        $ story_add("hoang_self_acceptance", 3)
        $ story_flag("tam_c04_w10_hoang_moves_own_plan")
        return
    scene bg_company_lobby_afternoon
    with dissolve
    "Chiều thứ Tư, Tâm xuống sảnh muộn bốn mươi phút."
    "Hoàng không còn ở đó."
    "Tin nhắn của anh gửi lúc sáu giờ hai mươi: anh về trước. Khi nào em xong thì báo."
    "Không trách móc. Cũng không tiếp tục chờ như một phép thử."
    menu:
        "Gọi Hoàng ngay khi đọc được tin":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_add("tam_self_clarity", 3)
            $ story_flag("tam_c04_w10_tam_calls_hoang_after_missed_time")
            tam neutral "Em xin lỗi. Em đáng ra phải báo."
            hoang neutral "Ừ. Anh không giận vì em bận. Anh chỉ không muốn đoán."
        "Nhắn một giờ hẹn khác cụ thể":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_sub("tam_insecurity", 3)
            $ story_flag("tam_c04_w10_tam_reschedules_hoang_clearly")
            "Tâm gửi: thứ Bảy, bốn giờ. Em sẽ tới."
            "Hoàng trả lời: được."
        "Chỉ xin lỗi và không hứa lịch mới":
            $ story_add("hoang_tam_trust", 3)
            $ story_add("career_tam", 5)
            $ story_add("tam_self_clarity", 3)
            $ story_flag("tam_c04_w10_tam_apologizes_without_reschedule")
            "Tâm xin lỗi. Hoàng trả lời rằng anh hiểu."
            "Khoảng trống sau chữ hiểu dài hơn một tin nhắn bình thường."
    return
