# FILE: game/story/tam/tam_c04_between_work_and_hearts/s83_w14_hoang_missed_call.rpy

label tam_c04_w14_s03_hoang_missed_call:
    $ _active = story_state.get("tam_hoang_interest", 0) >= 55
    if not _active:
        return
    scene bg_tam_room_morning
    with dissolve
    "Tối thứ Tư, Tâm nhìn thấy cuộc gọi nhỡ của Hoàng sau gần hai tiếng."
    "Tin nhắn cuối chỉ có: 'Anh về trước.'"
    menu:
        "Gọi lại ngay và xin lỗi rõ ràng":
            $ story_add("tam_hoang_interest", 3)
            $ story_add("hoang_tam_trust", 5)
            $ story_sub("tam_insecurity", 2)
            $ story_flag("tam_c04_w14_tam_calls_hoang_back")
            tam neutral "Em quên nhìn giờ. Không phải em không muốn tới."
            hoang neutral "Anh biết hai việc đó khác nhau. Nhưng người chờ vẫn chỉ có một."
        "Nhắn rằng tuần này quá bận":
            $ story_add("tam_self_clarity", 3)
            $ story_sub("hoang_tam_trust", 2)
            $ story_flag("tam_c04_w14_tam_explains_busy_only")
            "Hoàng trả lời: 'Ừ. Nghỉ đi.'"
        "Để sáng mai mới trả lời":
            $ story_sub("tam_hoang_interest", 2)
            $ story_sub("hoang_tam_trust", 5)
            $ story_add("tam_insecurity", 3)
            $ story_flag("tam_c04_w14_tam_leaves_hoang_overnight")
            "Màn hình tối đi. Chiếc bàn đã đặt không vì thế mà chưa từng tồn tại."
    return
