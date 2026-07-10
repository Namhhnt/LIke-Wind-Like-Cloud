# FILE: game/story/tam/tam_c04_between_work_and_hearts/s15_w03_huyen_defends_the_standard.rpy
# Week 03 — Huyền starts defending the standard she used to resist.

label tam_c04_w03_s04_huyen_defends_the_standard:
    scene bg_company_open_office_day
    with dissolve

    "Sáng thứ Năm, một thành viên từ đội khác gửi lại tài liệu với lời nhắn: phần này khách vẫn hiểu, không cần sửa thêm."

    "Huyền đọc xong, kéo cửa sổ chat sang bên cạnh rồi gõ một đoạn dài."

    tam confused "Mày đang làm gì vậy?"

    huyen irritated "Giải thích vì sao 'người ta vẫn hiểu' không phải tiêu chuẩn nghiệm thu."

    "Tâm nhìn cô."

    huyen confused "Gì?"

    tam teasing "Không có gì. Chỉ hơi quen tai."

    "Huyền dừng tay. Cô đọc lại dòng mình vừa viết, rồi tựa lưng vào ghế như người vừa phát hiện chữ ký của kẻ khác trên giấy tờ nhà mình."

    huyen frustrated "Tao ghét chuyện này."

    tam smile "Mày ghét tiêu chuẩn hay ghét việc mày đồng ý với nó?"

    huyen irritated "Cả hai. Nhưng cái thứ hai xúc phạm hơn."

    "Quân đi ngang đúng lúc Huyền bấm gửi. Anh nhìn màn hình, đọc phần đầu cuộc trao đổi."

    quan neutral "Bổ sung ví dụ ở dự án tuần trước. Họ sẽ bớt tranh luận."

    huyen neutral "Em đang thêm."

    "Quân gật đầu rồi đi tiếp."

    "Không có lời khen. Cũng không có câu nhắc lại."

    menu:
        "Trêu Huyền rằng cô đã thành học trò của Quân":
            $ story_add("huyen_quan_trust", 3)
            $ story_add("huyen_quan_interest", 1)
            $ story_add("tam_observation", 5)
            $ story_add("career_huyen", 3)
            $ story_flag("tam_c04_w03_tam_teases_huyen_quan_standard")

            tam teasing "Mày học nhanh ghê."

            huyen irritated "Tao đang tự bảo vệ công sức của mình. Đừng gán giáo viên cho tao."

            tam smile "Tao có nói tên ai đâu."

            "Huyền ném cho cô một chiếc kẹp giấy. Nó rơi lệch khỏi bàn phím hai phân."

        "Cùng Huyền bổ sung bằng chứng":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ story_add("tam_self_clarity", 3)
            $ story_add_direction("tam", "tam_support_huyen")
            $ story_flag("tam_c04_w03_tam_helps_huyen_defend_standard")

            tam neutral "Gửi tao link dự án cũ. Tao lấy đoạn phản hồi khách hàng."

            huyen neutral "Tao cần đúng phần họ phải sửa sau bàn giao."

            tam neutral "Biết rồi."

            "Hai người chia việc mà không cần kéo ghế lại. Nhịp làm việc đã quen đến mức khoảng cách giữa hai bàn không còn quan trọng."

        "Để Huyền tự chốt và nhìn phản ứng của Quân":
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 2)
            $ story_add("career_huyen", 5)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w03_tam_leaves_huyen_to_defend_standard")
            $ story_flag("quan_noticed_huyen_defending_standard")

            "Tâm quay lại màn hình của mình."

            "Mười phút sau, Quân gửi vào nhóm đúng một dấu xác nhận dưới phần giải thích của Huyền."

            "Huyền nhìn thông báo, không nói gì. Nhưng cô không tắt nó ngay."

    "Đến trưa, người bên đội kia đồng ý sửa."

    "Huyền đứng dậy lấy nước, đi ngang bàn Quân mà không còn nhìn sang như đang đi qua vùng nguy hiểm."

    "Chưa phải thân thuộc."

    "Chỉ là cô đã biết nơi nào có thể đặt chân."

    return
