# FILE: game/story/tam/tam_c04_between_work_and_hearts/s13_w03_client_meeting_pressure.rpy
# Week 03 — The rehearsal becomes a real client meeting.

label tam_c04_w03_s02_client_meeting_pressure:
    scene bg_meeting_room_day
    with dissolve

    scene cg_tam_c04_tam_presentation
    with dissolve
    "Chiều thứ Ba, bản trình bày thử trở thành một cuộc họp thật."
    scene bg_meeting_room_day
    with dissolve

    "Phía khách hàng có thêm một người chưa từng xuất hiện trong danh sách. Ông ta ngồi cuối bàn, lật tài liệu nhanh hơn lời giới thiệu."

    "Tâm đứng bên màn hình. Huyền ngồi gần laptop, tay đặt trên chuột. Quân ở phía đối diện, không chen vào phần mở đầu."

    "Đến slide về thời gian triển khai, người khách mới ngẩng lên."

    "Khách hàng" "Tôi không thấy lý do phải trả thêm thời gian cho việc đội các bạn tự làm phức tạp quy trình."

    "Huyền khựng tay. Con trỏ trên màn hình lệch khỏi dòng cần chỉ."

    "Tâm nhận ra trước khi bất kỳ ai lên tiếng."

    menu:
        "Tâm nhận phần phản biện":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w03_tam_handles_client_pressure")

            tam neutral "Phần thời gian tăng thêm nằm ở giai đoạn kiểm chứng. Nếu bỏ nó, chi phí không biến mất. Nó chỉ chuyển sang sau bàn giao, lúc việc sửa đổi đắt hơn."

            "Khách hàng" "Đó là giả định của cô."

            tam neutral "Vâng. Vì vậy bọn em đã chuẩn bị số liệu của ba dự án có phạm vi tương đương."

            "Tâm chuyển sang phụ lục. Huyền bắt đúng nhịp, mở bảng so sánh trước khi cô phải quay lại."

            "Quân không nói gì. Nhưng cây bút trong tay anh được đặt xuống."

        "Để Huyền trả lời phần cô ấy đã chuẩn bị":
            $ story_add("career_huyen", 5)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w03_huyen_handles_client_pressure")

            "Tâm lùi khỏi màn hình nửa bước."

            huyen neutral "Nếu giữ quy trình cũ, khách hàng vẫn trả thời gian. Nhưng trả sau bàn giao, khi một thay đổi kéo theo nhiều phần đã nghiệm thu."

            "Khách hàng" "Cô có số liệu không?"

            huyen neutral "Có. Phụ lục ba, trang mười bốn."

            "Huyền mở đúng trang. Giọng cô nhanh hơn Quân, mềm hơn Quân, nhưng cách đặt vấn đề đã không còn xa anh nhiều như trước."

            "Quân nhìn cô một lần rồi quay lại phía khách."

        "Tâm và Huyền phối hợp như lúc rehearsal":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ story_add("tam_self_clarity", 3)
            $ story_add("huyen_quan_trust", 3)
            $ story_add_direction("tam", "tam_support_huyen")
            $ story_flag("tam_c04_w03_tam_huyen_handle_pressure_together")

            tam neutral "Thời gian không tăng ở toàn bộ quy trình. Chỉ tăng ở phần kiểm chứng—"

            huyen neutral "—để giảm thay đổi dây chuyền sau bàn giao. Bọn em có bảng so sánh ở phụ lục ba."

            "Huyền mở dữ liệu. Tâm giữ phần giải thích."

            "Không ai phải nhìn sang người kia để hỏi lượt."

    "Cuộc họp kết thúc muộn mười hai phút."

    "Khi cánh cửa đóng lại, Huyền thở ra rồi nhìn Quân."

    huyen neutral "Em tưởng anh sẽ cắt lời."

    quan neutral "Hai em chưa cần."

    "Huyền đứng im một nhịp."

    huyen neutral "Vâng."

    "Câu trả lời không còn mang âm chống đối. Chỉ còn phần mệt và một chút nhẹ đi mà cô chưa định gọi tên."

    return
