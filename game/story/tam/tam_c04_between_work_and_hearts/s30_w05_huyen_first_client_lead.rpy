# FILE: game/story/tam/tam_c04_between_work_and_hearts/s30_w05_huyen_first_client_lead.rpy
# Week 05 — Huyền leads her first client call while Quân reviews from the back.

label tam_c04_w05_s05_huyen_first_client_lead:
    scene bg_meeting_room_day
    with dissolve

    scene cg_tam_c04_huyen_presentation
    with dissolve
    "Sáng thứ Sáu, Huyền đứng ở đầu bàn họp."
    scene bg_meeting_room_day
    with dissolve

    "Quân ngồi phía cuối, laptop đóng lại."

    "Việc anh không mở máy khiến Huyền nhìn về phía đó nhiều hơn cả khi anh ghi chú."

    huyen neutral "Phần này em sẽ trình bày. Tâm phụ trách dữ liệu hỗ trợ."

    "Khách hàng hỏi một câu ngoài phạm vi."

    "Huyền dừng nửa nhịp."

    menu:
        "Đưa dữ liệu, nhưng để Huyền tự kết luận":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 10)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 5)
            $ story_add("huyen_quan_trust", 3)
            $ story_flag("tam_c04_w05_tam_supports_huyen_without_taking_over")

            tam neutral "Số liệu quý trước ở trang mười hai."

            "Tâm mở đúng trang rồi xoay màn hình về phía Huyền."

            "Huyền nhìn một lần, tự trả lời phần còn lại."

            "Quân không can thiệp."

        "Lùi lại để Huyền tự xử lý hoàn toàn":
            $ story_add("career_huyen", 10)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 3)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w05_tam_leaves_huyen_full_lead")

            "Tâm giữ tay trên bàn phím."

            "Huyền hít vào, hỏi lại khách hàng một câu để thu hẹp phạm vi."

            "Sau cuộc họp, Quân chỉ nói một chữ."

            quan neutral "Được."

            "Huyền không cười. Cô chỉ đóng nắp bút chậm hơn bình thường."

        "Can thiệp để giữ cuộc họp an toàn":
            $ story_add("career_tam", 10)
            $ story_add("career_huyen", 3)
            $ story_add("tam_observation", 3)
            $ story_flag("tam_c04_w05_tam_takes_client_question")

            tam neutral "Phần đó hiện chưa nằm trong phạm vi cam kết. Em có thể gửi phân tích riêng sau."

            "Cuộc họp tiếp tục trơn tru."

            "Huyền không phản ứng ngay. Đến khi ra ngoài, cô mới kéo Tâm lại."

            huyen neutral "Lần sau cho tao thêm một nhịp."

            tam neutral "Ừ."

    "Quân đi qua hai người trước khi rời phòng."

    quan neutral "Chiều gửi biên bản. Huyền chịu bản cuối."

    huyen neutral "Vâng."

    "Lần này cô không nhìn Tâm trước khi nhận việc."

    return
