label tam_c04_w12_s03_hoang_asks_for_clear_no:
    $ _active = story_state.get("tam_hoang_interest", 0) >= 55
    if not _active:
        $ story_add("career_hoang", 5)
        $ story_add("hoang_self_acceptance", 5)
        $ story_flag("tam_c04_w12_hoang_no_longer_waiting_route")
        return
    scene black
    with dissolve
    "Sau buổi review, Hoàng đi cạnh Tâm một đoạn."
    hoang neutral "Anh muốn đề nghị một việc."
    tam neutral "Nghe nghiêm túc vậy."
    hoang neutral "Khi em không muốn gặp, nói không. Đừng nói để xem đã rồi biến mất trong công việc."
    menu:
        "Đồng ý và hỏi Hoàng cũng làm như vậy":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_sub("tam_insecurity", 3)
            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_c04_w12_tam_hoang_clear_yes_no")
            tam neutral "Được. Nhưng anh cũng vậy. Không tự lùi rồi bảo là cho em không gian."
            hoang neutral "Công bằng."
        "Nói Tâm vẫn cần thời gian để biết mình muốn gì":
            $ story_add("hoang_tam_trust", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_c04_w12_tam_needs_time_with_hoang")
            tam neutral "Có lúc em thật sự chưa biết."
            hoang neutral "Vậy nói chưa biết. Cũng rõ hơn im lặng."
        "Hỏi Hoàng có đang yêu cầu một lời hứa không":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_self_acceptance", 5)
            $ story_add("tam_observation", 3)
            $ story_flag("tam_c04_w12_tam_asks_hoang_promise")
            tam neutral "Anh đang muốn em hứa à?"
            hoang neutral "Không. Anh muốn em đừng để anh tự viết phần còn thiếu."
    "Họ dừng ở ngã rẽ."
    "Không có lời hứa. Chỉ có một quy tắc nhỏ để không làm nhau mỏi vì đoán."
    return
