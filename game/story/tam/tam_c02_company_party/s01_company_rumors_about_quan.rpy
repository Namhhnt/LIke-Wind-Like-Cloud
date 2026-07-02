# FILE: game/story/tam/tam_c02_company_party/s01_company_rumors_about_quan.rpy
# Scene file.

label tam_c02_company_party_s01_company_rumors_about_quan:
    scene bg_company_lobby_noon
    with fade

    $ story_flag('tam_heard_quan_rumors')

    "Đến cuối tuần onboarding đầu tiên, Tâm đã biết đường từ chỗ ngồi ra máy in, từ pantry về phòng họp, và từ phòng họp về lại chỗ ngồi mà không cần nhìn biển chỉ dẫn."

    "Đó là một tiến bộ đáng kể."

    "Ít nhất là theo tiêu chuẩn của Huyền."

    huyen happy "Tuần đầu sống sót. Tối nay nên ăn gì đó mừng đi."

    tam neutral "Mới onboarding thôi. Chưa làm gì thật cả."

    huyen teasing "Chính vì chưa làm gì thật nên mới nên mừng. Sau này muốn mừng có khi không còn sức."

    "Tâm cầm cốc nước giấy lên."

    "Nước hơi nóng. Thành cốc mềm đi dưới đầu ngón tay."

    "Bên cạnh máy pha cà phê, hai nhân viên cũ đang nói chuyện nhỏ."

    coworker "Hai bạn mới vào team dự án bên phòng Quân à?"

    huyen neutral "Dạ, có thể sau onboarding sẽ vào ạ. Em nghe nói vậy."

    coworker "Vậy chuẩn bị tinh thần trước đi."

    "Tâm khựng lại rất nhẹ."

    "Một giọt nước đọng bên miệng cốc trượt xuống ngón tay cô."

    tam neutral "Anh Quân... khó lắm ạ?"

    coworker "Khó thì không hẳn. Anh ấy giỏi thật, làm việc rất chắc. Chỉ là soi kỹ."

    coworker "Sai một dấu chấm trong tài liệu cũng thấy."

    huyen confused "Một dấu chấm luôn ạ?"

    coworker "Ừ. Có lần anh ấy trả lại cả file chỉ vì phần estimate ghi thiếu assumption."

    "Huyền im lặng hai giây."

    huyen teasing "Nghe giống nhân vật boss phải đánh sau khi qua tutorial."

    coworker "Boss này không rơi vật phẩm đâu."

    "Một nhân viên khác đi ngang qua, nghe thấy, bật cười."

    coworker "Nhưng công bằng mà nói, anh Quân không ghét người mới. Anh ấy chỉ ghét người làm màu."

    coworker "Không biết thì nói không biết. Làm sai thì sửa. Đừng cố tỏ ra hiểu."

    "Câu đó khiến Tâm ngẩng lên."

    "Không biết thì nói không biết."

    "Làm sai thì sửa."

    "Đừng cố tỏ ra hiểu."

    "Nghe đáng sợ."

    "Nhưng cũng không hoàn toàn vô lý."

    huyen neutral "Thế anh ấy có khen ai bao giờ không ạ?"

    coworker "Có."

    huyen smile "Vậy cũng được."

    coworker "Nhưng thường là khen bằng cách không bắt sửa nữa."

    huyen tired "À. Kiểu tình yêu im lặng."

    tam smile "Đừng dùng chữ tình yêu ở đây."

    "Cô nhân viên cũ cười thêm một tiếng rồi đi mất."

    "Tâm nhìn xuống cốc nước."

    "Thành cốc giấy đã hơi móp ở chỗ cô vừa siết tay."

    menu:
        "Tâm nên tiếp nhận tin đồn về Quân thế nào?"

        "Ghi nhớ tiêu chuẩn của Quân":
            $ story_add('career_tam', 2)
            $ story_add('tam_observation', 1)
            $ story_flag('tam_c02_quan_standard_noted')

            "Tâm lấy điện thoại ra, mở phần ghi chú."

            "Cô viết rất nhanh."

            "{i}Quân: competent, strict, detail-oriented. Không làm màu. Hỏi sớm. Sửa nhanh.{/i}"

            huyen surprised "Mày ghi thật à?"

            tam neutral "Ừ."

            huyen teasing "Tao tưởng người bình thường nghe tin đồn xong sẽ hoảng."

            tam smile "Tao hoảng có ghi chú."

            huyen laughing "Một hình thức hoảng có tổ chức."

            "Tâm cất điện thoại đi."

            "Trong lòng cô vẫn hơi căng."

            "Nhưng ít nhất, nỗi căng ấy đã có hình dạng cụ thể."

        "Để Huyền đùa cho nhẹ bớt":
            $ story_add('career_huyen', 1)
            $ story_add('tam_self_clarity', 1)
            $ story_flag('tam_c02_huyen_lightens_quan_rumor')

            huyen neutral "Tao nghĩ mình cần chiến thuật."

            tam neutral "Chiến thuật gì?"

            huyen grinning "Mày phụ trách làm đúng. Tao phụ trách xin lỗi dễ thương nếu sai."

            tam tired "Không có chiến thuật nào nghe thiếu trách nhiệm hơn được à?"

            huyen teasing "Có. Cả hai cùng giả vờ chưa nhận email."

            "Tâm bật cười, suýt làm nước trong cốc sóng ra ngoài."

            "Cô đặt cốc xuống bàn."

            "Chiếc cốc hơi lệch khỏi vòng nước cũ. Tâm nhìn nó một giây, rồi đẩy lại đúng chỗ."

            huyen smile "Thấy chưa. Còn chỉnh được cốc là còn sống tốt."

            tam smile "Triết lý văn phòng của mày sâu sắc quá."

            huyen happy "Tao biết. Đáng lẽ nên in thành poster."

        "Bị áp lực hơn":
            $ story_add('tam_insecurity', 2)
            $ story_add('doom_score', 1)
            $ story_flag('tam_c02_quan_pressure')

            "Tâm im lặng lâu hơn thường lệ."

            "Cô muốn hỏi thêm, nhưng câu hỏi mắc lại ở cổ."

            "Nếu hỏi nhiều quá, có giống người không hiểu gì không?"

            "Nếu không hỏi, đến lúc làm sai thì sao?"

            "Chiếc cốc giấy trong tay cô lõm xuống thêm một chút."

            huyen neutral "Tâm."

            tam surprised "Hả?"

            huyen neutral "Cốc sắp bị mày bóp thành origami rồi."

            "Tâm nhìn xuống."

            "Đúng thật."

            tam embarrassed "À..."

            huyen smile "Nghe đồn thôi. Đừng để tin đồn làm mày mệt trước cả người thật."

            tam neutral "Ừ."

            "Tâm đặt cốc xuống."

            "Lần này, cô không chỉnh nó lại."

    scene bg_company_open_office_day
    with dissolve

    "Chiều hôm đó, Tâm nhìn thấy Quân lần đầu tiên."

    "Anh đứng ở cuối dãy bàn làm việc, tay cầm một tập tài liệu mỏng."

    "Không lớn tiếng."

    "Không quát ai."

    "Chỉ gõ đầu bút vào một dòng trên giấy."

    quan neutral "Chỗ này thiếu căn cứ. Sửa lại trước năm giờ."

    coworker "Vâng anh."

    "Quân gật đầu, đặt tập tài liệu xuống bàn người kia, rồi quay đi."

    "Tâm chỉ nhìn thoáng qua."

    "Nhưng không hiểu sao, cô lại nhớ rất rõ tiếng đầu bút chạm vào giấy."

    huyen neutral "Boss xuất hiện."

    tam neutral "Ừ."

    huyen teasing "Không có nhạc nền."

    tam smile "May quá."

    "Tâm mở lại file training."

    "Lần này, trước khi làm tiếp, cô đọc kỹ phần assumption hơn một chút."

    return