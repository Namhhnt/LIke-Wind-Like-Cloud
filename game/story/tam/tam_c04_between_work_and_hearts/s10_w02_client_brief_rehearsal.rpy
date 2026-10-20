# FILE: game/story/tam/tam_c04_between_work_and_hearts/s10_w02_client_brief_rehearsal.rpy
# Week 02 — Career rehearsal that can strengthen Tâm–Huyền or expose Tâm independently.

label tam_c04_w02_s05_client_brief_rehearsal:
    scene bg_meeting_room_day
    with dissolve

    scene cg_tam_c04_team_review
    with dissolve
    "Chiều thứ Sáu, phòng họp chỉ còn Tâm, Huyền và Quân."
    scene bg_meeting_room_day
    with dissolve

    "Slide đầu tiên nằm yên trên màn hình. Con trỏ chuột chớp ở góc dưới, nhỏ và đều."

    if story_has_flag("tam_c04_w02_tam_requests_next_presentation"):
        "Tâm đứng cạnh màn hình. Đây là phần cô đã chủ động xin."
    elif story_has_flag("tam_c04_w01_first_focus_huyen"):
        "Tâm và Huyền đứng cạnh nhau. Hai người đã chia phần nói từ trước."
    else:
        "Quân bảo cả hai chuẩn bị như thể khách hàng có thể đổi người trình bày vào phút cuối."

    quan neutral "Bắt đầu đi."

    "Tâm trình bày phần bối cảnh. Huyền chuyển sang các điểm thay đổi trong yêu cầu."

    "Đến slide thứ năm, Quân giơ tay."

    quan neutral "Nếu khách hỏi vì sao phương án mới tăng thời gian triển khai, ai trả lời?"

    "Huyền vừa mở miệng. Tâm cũng vừa quay sang."

    menu:
        "Tâm trả lời và tự chịu phần phản biện":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_add("tam_observation", 3)
            $ story_flag("tam_c04_w02_tam_leads_rehearsal")

            tam neutral "Vì phương án mới tách phần nghiệm thu khỏi luồng vận hành. Thời gian triển khai tăng, nhưng giảm rủi ro phải sửa lại toàn bộ khi nghiệm thu."

            quan neutral "Khách không quan tâm rủi ro của đội mình."

            tam neutral "Vậy em sẽ quy đổi thành chi phí thay đổi sau bàn giao. Đó là rủi ro của họ."

            "Quân nhìn slide, rồi nhìn cô."

            quan neutral "Cách đó dùng được. Bổ sung số liệu."

        "Để Huyền trả lời phần cô ấy hiểu rõ nhất":
            $ story_add("career_huyen", 5)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w02_huyen_answers_quan_rehearsal")

            "Tâm lùi nửa bước."

            huyen neutral "Vì nếu giữ phương án cũ, bên khách sẽ phải tự nối điều khoản nghiệm thu với luồng sử dụng. Khi họ đổi một điều khoản, bên mình không biết phần nào bị ảnh hưởng."

            quan neutral "Đó là vấn đề của mình, chưa phải của khách."

            huyen neutral "Chi phí sửa sau bàn giao sẽ là vấn đề của khách. Em sẽ thêm con số ước tính."

            "Quân gật đầu."

            quan neutral "Được."

            "Huyền không nhìn Tâm ngay. Nhưng vai cô hạ xuống rất nhẹ."

        "Hai người phối hợp trả lời":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ story_add("tam_self_clarity", 3)
            $ story_add_direction("tam", "tam_support_huyen")
            $ story_flag("tam_c04_w02_tam_huyen_answer_together")

            tam neutral "Phương án mới tăng thời gian triển khai—"

            huyen neutral "—nhưng giảm phần thay đổi không kiểm soát sau bàn giao."

            tam neutral "Bọn em sẽ bổ sung bảng so sánh chi phí để khách thấy phần chênh lệch."

            "Quân im lặng một nhịp."

            quan neutral "Hai em thống nhất người nói. Nhưng giữ cách chia lập luận này."

            "Huyền nghiêng đầu về phía Tâm."

            huyen teasing "Bản dịch: chưa tệ."

    "Buổi rehearsal kết thúc muộn hơn dự kiến mười lăm phút."

    "Quân rời phòng trước. Huyền thu dây kết nối màn hình, cuộn gọn hơn lần trước."

    huyen neutral "Tao bắt đầu biết ổng sẽ hỏi gì."

    tam teasing "Nguy hiểm rồi."

    huyen irritated "Tao biết. Đừng nói thành tiếng."

    return
