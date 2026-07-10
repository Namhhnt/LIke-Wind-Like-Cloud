# FILE: game/story/tam/tam_c04_between_work_and_hearts/s23_w04_month_one_priority.rpy
# Week 04 — Final priority choice of Month 01. Still no route lock.

label tam_c04_w04_s06_month_one_priority:
    scene bg_company_open_office_day
    with dissolve

    "Thứ Sáu, sáu giờ hai phút."

    "Tháng đầu tiên không kết thúc bằng một sự kiện lớn."

    "Chỉ có bản brief mới của Tâm, outline mới của Huyền, lịch cuối tuần Hoàng gửi từ đầu tuần và tin nhắn Quang báo Thiên An đã về nhà an toàn."

    "Những thứ nhỏ nằm cạnh nhau trên màn hình."

    "Tâm biết mình vẫn có thể chọn nhiều hơn một điều trong những tháng tới."

    "Nhưng tối nay, như mọi lần, cô vẫn phải mở một thứ trước."

    menu:
        "Xác nhận kế hoạch cuối tuần với Hoàng":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_sub("tam_insecurity", 3)
            $ story_add("huyen_quan_trust", 3)
            $ story_add("career_huyen", 3)
            $ story_add("thienan_quang_trust", 3)
            $ story_add_direction("tam", "tam_hoang_open")
            $ story_flag("tam_c04_w04_focus_hoang")

            tam "Giờ cũ nhé. Lần này em sẽ không để anh đợi bốn mươi phút."

            hoang "Anh sẽ chỉ tính từ phút bốn mươi mốt."

            "Tâm cười, đặt điện thoại xuống bên cạnh tập brief."

        "Cùng Huyền chia ownership cho tháng sau":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_add("huyen_quan_trust", 3)
            $ story_add("hoang_self_acceptance", 3)
            $ story_add_direction("tam", "tam_support_huyen")
            $ story_flag("tam_c04_w04_focus_huyen")

            tam neutral "Mở file phân công đi. Chia xong rồi về."

            huyen neutral "Tao lấy phần đối ngoại. Mày đừng giành."

            tam teasing "Mới một tháng đã biết tranh việc rồi."

            huyen smile "Tiến bộ có định hướng."

        "Để Huyền tự gửi outline cho Quân":
            $ story_add("career_huyen", 5)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("tam_observation", 5)
            $ story_add("hoang_self_acceptance", 3)
            $ story_flag("tam_c04_w04_focus_huyen_quan")

            tam neutral "Outline của mày thì mày tự gửi. Đừng thêm tao vào chỉ để đỡ run."

            huyen irritated "Tao không run."

            tam smile "Ừ. Gửi đi."

            "Huyền nhìn nút gửi thêm hai giây rồi bấm."

        "Nhắn Quang rằng anh đã có chỗ ở bàn ăn, đừng chỉ đứng ngoài cửa":
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_add_direction("tam", "tam_support_quang_thienan")
            $ story_flag("tam_c04_w04_focus_quang_thienan")

            tam "Lần sau anh vào nhà luôn đi. Đứng ngoài cổng không làm chị An bớt khó xử đâu."

            quang "Anh biết."

            tam teasing "Câu này tháng này anh dùng hơi nhiều."

            quang "Tháng sau anh sửa."

        "Hỏi Quang khi nào anh định trả lời câu hỏi về chiếc ô":
            $ story_add("tam_quang_interest", 5)
            $ story_add("tam_observation", 5)
            $ story_add("quang_persistence", 3)
            $ story_add("career_huyen", 3)
            $ story_flag("tam_c04_w04_focus_quang_personal")

            tam "Anh nghĩ xong cách trả lời chưa?"

            quang "Câu nào?"

            tam "Câu thật."

            "Tin nhắn im gần một phút."

            quang "Chưa. Nhưng anh không quên."

            "Tâm không hỏi tiếp. Lần đầu tiên, sự trì hoãn ấy không giống né tránh hoàn toàn."

        "Mở brief độc lập của mình":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_add("tam_observation", 3)
            $ story_add("huyen_quan_trust", 3)
            $ story_add("career_huyen", 3)
            $ story_add("hoang_self_acceptance", 3)
            $ story_add("thienan_quang_trust", 3)
            $ story_add_direction("tam", "tam_career_focus")
            $ story_flag("tam_c04_w04_focus_career")

            "Tâm mở brief mới."

            "Tên cô nằm một mình ở dòng phụ trách."

            "Cảm giác hơi trống. Cũng hơi nhẹ."

            "Cô tạo file đầu tiên, đặt tên rõ ràng rồi mới trả lời các tin nhắn còn lại."

    "Ngoài cửa kính, ánh sáng cuối ngày rút khỏi các tòa nhà từng tầng một."

    "Một tháng đã trôi qua mà không ai nói thành lời."

    "Chỉ có vài cách xưng hô bớt cứng. Vài tin nhắn đến sớm hơn. Vài chiếc ghế không còn bị kéo ra quá xa."

    return
