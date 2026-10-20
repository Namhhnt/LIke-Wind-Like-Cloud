label tam_c04_w12_s02_three_month_work_review:
    scene bg_meeting_room_day
    with dissolve
    scene cg_tam_c04_team_review
    with dissolve
    "Chiều thứ Ba, Quân đặt ba tập giấy lên bàn: đánh giá của Tâm, của Huyền, và bản tổng hợp dự án."
    scene bg_meeting_room_day
    with dissolve
    quan neutral "Ba tháng đầu không đủ để kết luận em sẽ đi được bao xa. Đủ để biết em chịu trách nhiệm theo cách nào."
    "Anh nhìn Tâm."
    if story_has_flag("tam_c04_w11_tam_owns_scope_mistake"):
        quan neutral "Em mắc lỗi trong phạm vi mình quyết định và không đẩy nó sang người khác. Giữ cách xử lý đó. Giảm số lần phải dùng đến nó."
    elif story_state.get("career_tam", 0) >= 70:
        quan neutral "Em nhận việc nhanh. Cần phân biệt tốc độ với việc ôm quá nhiều quyền quyết định."
    else:
        quan neutral "Em quan sát tốt. Nhưng quyền quyết định chỉ có giá trị khi em dùng nó."
    "Anh chuyển sang Huyền."
    if story_has_flag("tam_c04_w11_huyen_quietly_fixes_quan_error"):
        quan neutral "Em sửa lỗi mà không biến nó thành cuộc tranh thắng. Đó là tiến bộ."
    elif story_state.get("huyen_quan_trust", 0) >= 65:
        quan neutral "Em đã ổn định hơn. Vẫn nói nhiều hơn mức cần thiết."
        huyen neutral "Phần sau không cần ghi vào quyết định đâu ạ."
    else:
        quan neutral "Em làm tốt khi có áp lực. Cần làm tốt cả khi không có ai nhìn."

    menu:
        "Nhận một đầu việc có quyền ký duyệt nội bộ":
            $ story_add("career_tam", 15)
            $ story_add("tam_self_clarity", 5)
            $ story_add("tam_observation", 3)
            $ story_add_direction("tam", "tam_career_focus")
            $ story_flag("tam_c04_w12_tam_accepts_internal_approval")
            tam neutral "Em nhận phần cần ký duyệt nội bộ."
            quan neutral "Quyền đó đi cùng log quyết định."
        "Đề nghị Tâm và Huyền sở hữu hai luồng ngang nhau":
            $ story_add("career_tam", 10)
            $ story_add("career_huyen", 10)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 5)
            $ story_flag("tam_c04_w12_tam_huyen_parallel_owners")
            tam neutral "Bọn em có thể sở hữu hai luồng riêng, review chéo ở checkpoint."
            huyen neutral "Không cứu nhau. Biết rồi."
            quan neutral "Làm trong tháng tới."
        "Đề xuất Huyền dẫn buổi review khách hàng tiếp theo":
            $ story_add("career_huyen", 15)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 3)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w12_huyen_leads_next_review")
            tam neutral "Buổi review tiếp theo để Huyền dẫn."
            huyen neutral "Em nhận."
            quan neutral "Tôi sẽ ngồi cuối phòng."
    "Quân ký bản tổng hợp cuối cùng."
    "Nét bút vẫn như cũ. Phần trách nhiệm dưới mỗi cái tên thì không."
    return
