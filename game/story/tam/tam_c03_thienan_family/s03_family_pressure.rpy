# FILE: game/story/tam/tam_c03_thienan_family/s03_family_pressure.rpy
# Scene file.

label tam_c03_thienan_family_s03_family_pressure:
    scene bg_tam_family_dining_room_evening
    with dissolve

    "Bữa tối muộn diễn ra trong một nhịp hơi lạ."

    "Mẹ Tâm hâm lại canh."

    "Bố Tâm ngồi ở đầu bàn, thỉnh thoảng hỏi Thiên An vài câu về chi nhánh miền Nam."

    "Quang đã ra về."

    "Chiếc bát anh dùng được úp riêng trên giá, nước vẫn còn đọng ở vành."

    tam_mother "Lần này con đi mấy ngày?"

    thienan neutral "Chưa chắc. Nếu thuận lợi thì ba ngày."

    tam_father "Không thuận lợi?"

    thienan neutral "Năm ngày."

    "Bố Tâm đặt đũa xuống."

    tam_father "Con đừng ôm hết mọi việc. Bên dưới có quản lý chi nhánh, có phòng vận hành, có pháp chế."

    thienan neutral "Con biết."

    tam_father "Biết là một chuyện. Làm được lại là chuyện khác."

    "Thiên An không phản bác."

    "Cô chỉ gắp một miếng rau vào bát, nhưng không ăn ngay."

    tam_mother "Ba con nói đúng. Công việc quan trọng, nhưng sức khỏe cũng quan trọng."

    thienan neutral "Con sẽ chú ý."

    tam_mother "Và chuyện riêng của con cũng quan trọng."

    "Đũa của Tâm khựng lại."

    "Thiên An thì không."

    "Cô vẫn giữ nguyên vẻ mặt bình tĩnh đến mức gần như đã đoán trước câu nói này từ trước khi mẹ mở miệng."

    thienan neutral "Mẹ."

    tam_mother "Mẹ chỉ nhắc thôi."

    thienan neutral "Mẹ nhắc ba lần trong tháng này rồi."

    tam_mother "Vì con nghe như không nghe."

    "Không khí trên bàn ăn hơi chùng xuống."

    "Tâm nhìn sang bố."

    "Ông không nói gì, nhưng cũng không ngăn lại."

    tam_mother "Con không còn nhỏ nữa. Nhà mình không ép con phải kết hôn ngay, nhưng ít nhất con cũng nên nghiêm túc nghĩ đến chuyện gặp gỡ ai đó."

    thienan neutral "Hiện tại con không có thời gian."

    tam_mother "Con lúc nào cũng không có thời gian."

    thienan neutral "Vì công ty lúc nào cũng có việc."

    tam_mother "Quang làm với con bao nhiêu năm như vậy còn không được, thì mẹ cũng không biết con định đợi đến lúc nào."

    "Câu nói ấy rơi xuống bàn ăn rất nhẹ."

    "Nhẹ đến mức chính vì thế mà khó tránh."

    "Thiên An đặt đũa xuống."

    thienan neutral "Chuyện của anh Quang không liên quan."

    tam_mother "Mẹ biết. Mẹ có nói gì Quang đâu."

    "Mẹ Tâm thở ra."

    tam_mother "Chỉ là mẹ tiếc. Thằng bé tốt. Lại hiểu con. Nhưng nếu con không có ý gì, thì thôi."

    thienan neutral "Vậy thì thôi."

    "Không phải câu nói giận."

    "Cũng không phải lạnh."

    "Chỉ là một cánh cửa được đóng lại bằng tay rất sạch."

    "Tâm nhìn chị."

    "Rồi nhìn chiếc bát trước mặt mình."

    "Miếng rau cô vừa gắp rơi lệch khỏi bát, nằm im trên mặt bàn."

    menu:
        "Tâm phản ứng thế nào?"

        "Hỏi nhẹ mẹ về áp lực này":
            $ story_add('thienan_self_assertion', 2)
            $ story_add('tam_observation', 1)
            $ story_flag('tam_questioned_family_pressure')

            tam neutral "Mẹ."

            tam_mother "Sao con?"

            tam neutral "Nếu chị An đang phải xử lý nhiều việc như vậy... có thể để chuyện này sau được không ạ?"

            "Mẹ Tâm nhìn cô."

            "Thiên An cũng nhìn cô."

            "Tâm hơi siết tay quanh đôi đũa, nhưng vẫn nói tiếp."

            tam neutral "Con nghĩ chị ấy không phải không nghe. Chỉ là... bây giờ hỏi thêm chuyện đó, chị ấy cũng không có chỗ để trả lời."

            "Một khoảng im lặng ngắn."

            tam_father "Ăn cơm đi."

            "Giọng bố Tâm không nặng."

            "Nhưng câu nói ấy đủ để đẩy bữa ăn trở lại mặt bàn."

            "Thiên An không nói cảm ơn."

            "Chỉ gắp lại miếng rau bị rơi lệch vào bát Tâm."

            thienan neutral "Ăn đi. Đừng diễn thuyết lúc đói."

            tam embarrassed "Em nói có hai câu."

            thienan smile "Hai câu dài."

        "Im lặng":
            $ story_add('family_pressure_thienan', 2)
            $ story_add('tam_insecurity', 1)
            $ story_flag('tam_stayed_silent_family_pressure')

            "Tâm cúi xuống ăn tiếp."

            "Cô không biết nên nói gì."

            "Cũng không chắc mình có quyền xen vào chuyện của chị."

            "Thiên An vẫn ngồi thẳng lưng."

            "Rất đẹp."

            "Rất đúng mực."

            "Và một mình."

        "Đánh trống lảng sang công việc":
            $ story_add('career_tam', 1)
            $ story_add('family_pressure_thienan', 1)
            $ story_flag('tam_deflected_family_pressure_with_work')

            tam neutral "Chị An, chi nhánh trong Nam là mảng phân phối đúng không ạ?"

            "Mẹ Tâm nhìn Tâm."

            "Thiên An cũng nhìn cô."

            "Tâm giả vờ không nhận ra mình vừa đổi chủ đề hơi vụng."

            thienan neutral "Ừ. Phân phối và một phần vận hành kho."

            tam neutral "Vậy nếu có sai lệch số liệu thì phát hiện khó không?"

            "Thiên An nhìn cô thêm một nhịp."

            thienan neutral "Tùy sai lệch nằm ở đâu."

            tam_mother "Hai chị em con đúng là..."

            "Mẹ Tâm lắc đầu."

            "Nhưng ít nhất bà không nhắc tiếp chuyện kết hôn."

    "Bữa tối kết thúc muộn."

    "Không có ai cãi nhau."

    "Nhưng khi Thiên An đứng dậy dọn bát, Tâm thấy chị rửa một chiếc thìa lâu hơn cần thiết."

    "Nước chảy qua mu bàn tay cô."

    "Lạnh."

    "Trong một căn bếp rất sáng."

    return