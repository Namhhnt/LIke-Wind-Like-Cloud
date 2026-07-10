# FILE: game/story/tam/tam_c04_between_work_and_hearts/s08_w02_huyen_knows_the_mark.rpy
# Week 02 — Huyền begins anticipating Quân's standards before he says them.

label tam_c04_w02_s03_huyen_knows_the_mark:
    scene bg_company_open_office_day
    with dissolve

    "Sáng thứ Tư, Huyền đặt bản báo cáo mới lên bàn Tâm."

    "Ba dòng được tô vàng. Một thuật ngữ đã được sửa đồng nhất từ đầu đến cuối."

    tam confused "Anh Quân gửi comment mới à?"

    huyen neutral "Chưa."

    tam teasing "Vậy ai nhập vào người mày?"

    huyen irritated "Tao chỉ không muốn nghe lại đúng một câu hai lần."

    "Huyền kéo ghế ngồi xuống, mở trang đối chiếu điều khoản."

    huyen neutral "Chỗ này khách đọc theo nghiệm thu. Nếu để theo luồng người dùng, anh ấy sẽ hỏi vì sao mình bắt người đọc tự nối."

    "Cô nói trọn câu, rồi khựng lại."

    tam smile "Nghe quen ghê."

    huyen irritated "Mày im đi."

    scene bg_meeting_room_day
    with dissolve

    "Buổi review diễn ra vào đầu giờ chiều."

    "Quân lật tới đúng trang Huyền đã đánh dấu."

    quan neutral "Chỗ này—"

    huyen neutral "Em đã tách theo điều khoản nghiệm thu. Phần luồng người dùng để ở phụ lục vì vẫn cần cho đội triển khai."

    "Quân dừng lại."

    "Huyền cũng dừng, như thể chính cô vừa đi trước mình nửa bước."

    quan neutral "Được."

    "Chỉ một chữ."

    "Huyền cúi xuống tài liệu, nhưng khóe bút trong tay cô không còn gõ vào mặt bàn."

    menu:
        "Bổ sung để cả hai cùng được ghi nhận":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ story_add("tam_self_clarity", 3)
            $ story_flag("tam_c04_w02_tam_huyen_shared_review")

            tam neutral "Bọn em cũng thêm bảng liên kết giữa hai phần để lần sau không phải kiểm thủ công."

            quan neutral "Ai đề xuất?"

            tam neutral "Cả hai cùng chỉnh."

            "Huyền nhìn sang Tâm. Lần này cô không phản đối cách chia công."

        "Để khoảnh khắc đó thuộc về Huyền":
            $ story_add("huyen_quan_trust", 5)
            $ story_add("career_huyen", 5)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w02_tam_leaves_huyen_credit")
            $ story_flag("quan_noticed_huyen_learning_his_standard")

            "Tâm khép bút lại."

            "Phần cô định bổ sung không còn cần thiết."

            quan neutral "Giữ cách này cho các báo cáo sau."

            huyen neutral "Vâng."

            "Huyền trả lời nhanh hơn thường lệ. Không chống đối. Cũng chưa mềm đi."

            "Chỉ là cô đã nhận câu nói ấy như một tiêu chuẩn, không còn như một đòn công kích."

        "Chủ động xin phụ trách phần trình bày tiếp theo":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_add("career_huyen", 3)
            $ story_flag("tam_c04_w02_tam_requests_next_presentation")

            tam neutral "Phần trình bày với khách tuần sau để em phụ trách được không?"

            quan neutral "Lý do?"

            tam neutral "Em muốn tự kiểm tra xem mình hiểu yêu cầu đến đâu, thay vì chỉ sửa theo review."

            "Quân nhìn cô, rồi đặt bút xuống."

            quan neutral "Chuẩn bị trước thứ Sáu. Tôi xem rehearsal."

            tam neutral "Vâng."

    scene bg_company_lobby_afternoon
    with dissolve

    "Ra khỏi phòng, Huyền đi cạnh Tâm một đoạn rồi mới lên tiếng."

    huyen neutral "Ổng vừa nói được à?"

    tam teasing "Ừ. Mày muốn tao ghi âm làm nhạc chuông không?"

    huyen irritated "Không. Tao chỉ xác nhận để khỏi nghĩ mình nghe nhầm."

    "Cô chỉnh lại tập tài liệu trong tay. Mép giấy thẳng hơn tuần trước."

    return
