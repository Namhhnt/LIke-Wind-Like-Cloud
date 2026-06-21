# ============================================================
# Chapter 01 interview minigame and outcomes
# ============================================================

label tam_c01_speech_game:

    $ tam_speech_attempts = 0

label tam_c01_speech_retry:

    $ tam_speech_order = []
    $ tam_speech_required = list(tam_speech_required_order)

    # Shuffle once per attempt.
    # This keeps the UI stable while the player is selecting 4 answers.
    $ tam_speech_pool = list(tam_speech_items)
    $ renpy.random.shuffle(tam_speech_pool)

    narrator "Mini-game: Sắp xếp các ý chính cho phần trả lời phỏng vấn."
    narrator "Chọn 4 ý cần trình bày. Nếu chọn đủ ý đúng thì pass. Nếu đúng cả ý lẫn thứ tự thì nhận bonus."

    while len(tam_speech_order) < 4:

        # Keep the shuffled order, but hide already selected choices.
        $ tam_speech_available = [
            item for item in tam_speech_pool
            if item["id"] not in tam_speech_order
        ]

        $ tam_speech_choice = renpy.call_screen(
            "tam_speech_choice_screen",
            items=tam_speech_available,
            picked=tam_speech_order
        )

        $ tam_speech_order.append(tam_speech_choice)

    $ tam_speech_has_required = all(x in tam_speech_order for x in tam_speech_required)
    $ tam_speech_perfect_order = tam_speech_order == tam_speech_required

    if tam_speech_has_required:

        if tam_speech_perfect_order:
            $ tam_salary_tier = "high"
            $ tam_work_skill += 2
            $ tam_confidence += 2
            $ add_unique(progress["player_flags"], "tam_interview_passed")
            $ add_unique(progress["player_flags"], "tam_interview_bonus_order")
            $ add_unique(progress["player_flags"], "tam_salary_high_start")
            $ add_unique(progress["player_flags"], "tam_work_skill_strong_c01")

            narrator "Các ý được đặt đúng thứ tự."
            narrator "Tâm mở đầu bằng việc hiểu bức tranh lớn, sau đó đi vào năng lực phối hợp, tư duy rủi ro, rồi mới kết lại bằng thái độ làm việc."
            narrator "Một câu trả lời không quá hoa mỹ. Nhưng gọn, có trục, và không bị rơi vào kiểu tự quảng cáo non tay."

            jump tam_c01_interview_perfect

        else:
            $ tam_salary_tier = "standard"
            $ tam_work_skill += 1
            $ tam_confidence += 1
            $ add_unique(progress["player_flags"], "tam_interview_passed")
            $ add_unique(progress["player_flags"], "tam_salary_standard_start")

            narrator "Các ý quan trọng đều có mặt, nhưng thứ tự trình bày chưa thật sự sắc."
            narrator "Dù vậy, Tâm vẫn cho thấy cô hiểu công việc và có thái độ nghiêm túc."

            jump tam_c01_interview_pass

    else:

        $ tam_speech_attempts += 1

        if tam_speech_attempts < 3:
            narrator "Câu trả lời bị lệch trọng tâm."
            narrator "Hội đồng không khó chịu, nhưng ánh mắt họ đủ khiến Tâm hiểu mình vừa đi sai hướng."
            narrator "Thử lại."

            jump tam_c01_speech_retry

        else:
            narrator "Tâm đã thất bại 3 lần trong phần sắp xếp ý."
            narrator "Có thể chơi lại để lấy bonus, hoặc skip để pass nhưng không nhận điểm thưởng."

            menu:
                "Chọn cách xử lý:"

                "Chơi lại mini-game":
                    jump tam_c01_speech_retry

                "Skip — pass không bonus":
                    $ tam_salary_tier = "standard"
                    $ add_unique(progress["player_flags"], "tam_interview_pass_skip_no_bonus")
                    $ add_unique(progress["player_flags"], "tam_salary_standard_start")

                    narrator "Tâm hít sâu, bỏ qua sự hoàn hảo mà mình vẫn luôn muốn giữ."
                    narrator "Cô trả lời theo cách an toàn hơn, vừa đủ để không bị loại, nhưng cũng không tạo được điểm sáng đặc biệt."

                    jump tam_c01_interview_skip


label tam_c01_interview_perfect:

    tam serious "Em nghĩ vị trí triển khai dự án không chỉ là truyền đạt thông tin từ bên này sang bên kia."

    tam serious "Với một công ty có nhiều mảng như xây dựng, vật liệu, IT, pháp lý, kế toán và quản lý chất lượng, người ở phòng triển khai cần hiểu được việc của mình nằm ở đâu trong toàn bộ dòng chảy dự án."

    tam serious "Nếu em không hiểu bối cảnh, em sẽ chỉ chuyển tiếp thông tin. Nhưng nếu hiểu bối cảnh, em có thể biết thông tin nào cần làm rõ, phòng ban nào cần được cập nhật, và rủi ro nào nên được báo sớm."

    tam neutral "Em chưa có nhiều kinh nghiệm thực tế, nhưng em có khả năng tổng hợp, theo dõi chi tiết, và em không ngại học quy trình từ đầu."

    tam smile "Em muốn làm tốt phần việc của mình theo cách đáng tin cậy. Không ồn ào, nhưng rõ ràng và có trách nhiệm."

    manager "Cách em trả lời khá có cấu trúc."

    interviewer "Và thực tế hơn anh chị nghĩ."

    narrator "Tâm thấy vai mình nhẹ đi một chút."

    narrator "Không phải vì cô chắc chắn mình đã thắng."

    narrator "Chỉ là lần đầu tiên trong buổi sáng hôm ấy, cô thấy mình đang đứng đúng chỗ."

    jump tam_c01_after_interview


label tam_c01_interview_pass:

    tam serious "Em nghĩ công việc triển khai dự án cần khả năng phối hợp và theo dõi chi tiết."

    tam serious "Công ty mình có nhiều phòng ban liên quan đến từng dự án, nên nếu thông tin không rõ ràng hoặc cập nhật chậm, tiến độ chung có thể bị ảnh hưởng."

    tam neutral "Em muốn học cách nắm quy trình, hỗ trợ các bên làm việc với nhau tốt hơn và báo cáo kịp thời khi có vướng mắc."

    manager "Tốt. Câu trả lời hơi vòng một chút, nhưng ý chính ổn."

    interviewer "Chị đánh giá cao việc em có nhắc đến phối hợp liên phòng ban."

    narrator "Tâm gật đầu."

    narrator "Cô biết mình chưa thật xuất sắc, nhưng ít nhất không bị trôi."

    jump tam_c01_after_interview


label tam_c01_interview_skip:

    tam serious "Em nghĩ vị trí này cần sự cẩn thận, khả năng phối hợp và tinh thần học hỏi."

    tam sad "Em chưa có nhiều kinh nghiệm, nhưng em sẵn sàng học quy trình, hỗ trợ công việc và làm theo hướng dẫn của cấp trên."

    manager "Được."

    narrator "Một câu trả lời an toàn."

    narrator "Không sai. Nhưng cũng không để lại nhiều dư âm."

    jump tam_c01_after_interview