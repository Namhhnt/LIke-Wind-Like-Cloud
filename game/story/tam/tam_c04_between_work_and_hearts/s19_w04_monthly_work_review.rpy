# FILE: game/story/tam/tam_c04_between_work_and_hearts/s19_w04_monthly_work_review.rpy
# Week 04 — First monthly performance review for Tâm and Huyền.

label tam_c04_w04_s02_monthly_work_review:
    scene bg_meeting_room_day
    with dissolve

    "Chiều thứ Ba, Quân đặt hai bản đánh giá xuống bàn."

    "Một bản mang tên Tâm. Một bản mang tên Huyền."

    "Huyền nhìn hai tờ giấy như thể việc bị tách riêng đã khiến căn phòng nghiêm trọng hơn."

    quan neutral "Tháng đầu, hai em tiến nhanh. Nhưng theo hai cách khác nhau."

    "Anh đẩy bản của Huyền về phía cô trước."

    quan neutral "Em phản ứng nhanh, bắt vấn đề tốt. Điểm yếu là thường chống lại yêu cầu trước khi kiểm tra xem nó có đúng không."

    huyen neutral "Vâng."

    "Cô không cãi. Quân dừng rất ngắn ở đó."

    quan neutral "Ba tuần gần đây tốt hơn. Giữ phần chủ động. Bỏ phần phản ứng thừa."

    "Sau đó anh nhìn sang Tâm."

    if story_state.get("career_tam", 0) >= 60:
        quan neutral "Em có khả năng dựng cấu trúc và giữ cuộc trao đổi không lệch mục tiêu. Nhưng đôi lúc em dùng việc hỗ trợ người khác để trì hoãn phần mình phải đứng tên."
    else:
        quan neutral "Em quan sát tốt và phối hợp ổn. Nhưng vẫn chờ quá lâu trước khi tự nhận phần việc."

    "Tâm nhìn dòng đánh giá trên giấy. Một vài chữ không dễ chịu. Không chữ nào sai hẳn."

    menu:
        "Nhận một phần việc độc lập trong tháng sau":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_add("tam_observation", 3)
            $ story_add_direction("tam", "tam_career_focus")
            $ story_flag("tam_c04_w04_tam_accepts_independent_assignment")

            tam neutral "Tháng sau em muốn nhận một phần việc riêng. Có người review, nhưng em tự chịu đầu ra."

            quan neutral "Tôi đã chuẩn bị một phần phù hợp."

            "Anh kéo một tờ brief mỏng từ dưới tập tài liệu."

            huyen surprised "Anh chuẩn bị sẵn luôn ạ?"

            quan neutral "Tôi không đưa nhận xét nếu không có bước tiếp theo."

        "Đề nghị Tâm và Huyền tiếp tục đi cùng nhưng chia ownership rõ":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_add_direction("tam", "tam_support_huyen")
            $ story_flag("tam_c04_w04_tam_huyen_split_ownership")

            tam neutral "Bọn em có thể tiếp tục cùng dự án, nhưng mỗi phần có một người chịu trách nhiệm chính."

            huyen neutral "Để khỏi có chuyện hai đứa cùng sửa mà không biết ai quyết định cuối."

            quan neutral "Được. Tự chia trước thứ Sáu."

            "Huyền nhìn sang Tâm. Lần này cái gật đầu giữa hai người giống một thỏa thuận công việc hơn một lời động viên."

        "Để Huyền nhận phần đối ngoại dưới sự review của Quân":
            $ story_add("career_huyen", 5)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w04_huyen_gets_quan_review_track")

            tam neutral "Phần đối ngoại của dự án này Huyền nắm tốt hơn em. Em nghĩ nên để Huyền chịu chính."

            huyen confused "Mày chắc không?"

            tam neutral "Ừ. Nhưng mày tự trình bày với anh Quân."

            quan neutral "Tôi sẽ review hai lần đầu. Sau đó em tự chịu."

            huyen neutral "Vâng."

            "Cô trả lời rất gọn. Khi cúi xuống bản đánh giá, ngón tay lại giữ đúng dòng Quân vừa nói."

    "Cuộc review kết thúc mà không ai thấy nhẹ hẳn."

    "Nhưng lúc ra khỏi phòng, Huyền không vò tờ đánh giá như Tâm đã đoán."

    "Cô gấp nó làm đôi, khá thẳng."

    return
