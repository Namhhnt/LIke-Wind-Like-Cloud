# FILE: game/story/tam/tam_c03_thienan_family/s01_quang_visit_home.rpy
# Scene file.

label tam_c03_thienan_family_s01_quang_visit_home:
    scene bg_tam_family_entry_evening
    with dissolve

    "Chuông cửa vang lên lúc gần chín giờ."

    "Tâm vừa đi xuống cầu thang thì thấy mẹ đã ra mở cửa."

    tam_mother "Quang à, vào đi cháu."

    quang "Dạ, cháu chào cô."

    "Người đàn ông đứng ngoài cửa mặc sơ mi trắng, tay cầm một túi tài liệu màu đen."

    "Anh hơi cúi đầu khi bước vào nhà, rất đúng mực, rất quen đường."

    "Quen đến mức không cần ai nhắc, anh tự đổi dép trong nhà, đặt ô vào góc tủ, rồi kéo nhẹ cánh cửa cho khỏi va vào khung."

    tam_mother "Ăn tối chưa?"

    quang "Dạ cháu ăn rồi ạ."

    tam_mother "Câu này cô nghe chắc ba năm rồi."

    quang "Lần này là thật ạ."

    "Mẹ Tâm nhìn anh."

    "Quang im lặng đúng hai giây."

    quang "Dạ... cháu có ăn một ít bánh mì trên xe."

    tam_mother "Ừ, vậy là chưa ăn."

    "Tâm đứng ở bậc cầu thang, không nhịn được cười."

    tam smile "Anh Quang vẫn thua mẹ em như mọi khi."

    quang "Anh chỉ đang tôn trọng sự thật khách quan."

    tam teasing "Sự thật khách quan là anh chưa ăn tối."

    quang "Ừ. Cũng khá khách quan."

    "Quang cười hiền."

    "Không phải kiểu cười để lấy lòng người lớn. Cũng không phải kiểu cười xã giao. Anh giống một người đã quen bị căn nhà này bắt tại trận trong những chuyện rất nhỏ."

    scene bg_tam_family_living_room_evening
    with dissolve

    "Thiên An từ phòng khách bước ra."

    thienan neutral "Anh đến nhanh vậy?"

    quang "Anh đang ở gần đây. Hợp đồng bản cứng em cần."

    "Quang đưa túi tài liệu cho cô."

    "Thiên An nhận lấy, mở ra kiểm tra ngay."

    thienan neutral "Bản phụ lục đâu?"

    quang "Ngăn trong. Anh đánh dấu bằng kẹp xanh."

    thienan neutral "Báo cáo rủi ro?"

    quang "Sau phụ lục. Có thêm bản tóm tắt một trang."

    thienan neutral "Em chưa yêu cầu bản tóm tắt."

    quang "Anh biết."

    "Thiên An ngẩng lên nhìn anh."

    quang "Nhưng em sẽ đọc trên máy bay. Một trang đỡ mỏi mắt hơn mười sáu trang."

    "Thiên An nhìn anh thêm một nhịp."

    thienan neutral "Cảm ơn."

    quang "Không có gì."

    "Hai người nói chuyện rất bình thường."

    "Bình thường đến mức nếu không để ý, người ta sẽ tưởng họ chỉ là đồng nghiệp lâu năm."

    "Nhưng Tâm để ý."

    "Quang biết Thiên An đọc tài liệu trên máy bay."

    "Biết cô hay đọc đến đau mắt."

    "Biết phần nào cần kẹp màu gì."

    "Còn Thiên An thì nhận tất cả những điều đó như một thói quen công việc."

    "Không tránh. Nhưng cũng không bước gần hơn."

    tam_mother "Quang ở lại ăn chút gì đi. Cô hâm canh cho."

    quang "Dạ thôi, cháu không phiền cô đâu ạ."

    tam_mother "Cháu phiền cô từ năm thứ nhất đại học của con An rồi, giờ mới ngại thì muộn quá."

    tam surprised "Năm nhất đại học?"

    quang "Anh và An học cùng trường kinh tế."

    thienan neutral "Cùng khóa."

    quang "Cùng vài môn."

    thienan neutral "Và cùng khá nhiều bài nhóm."

    quang "Vì có người chọn thành viên nhóm theo tiêu chí ai làm việc được thì giữ."

    thienan smile "Tiêu chí đó rất hợp lý."

    quang "Ừ. Hợp lý đến mức anh bị giữ tới tận bây giờ."

    "Quang nói với giọng rất bình thường."

    "Thiên An cũng chỉ nhìn xuống hồ sơ, khóe môi nhích lên rất nhẹ."

    "Một câu đùa nhỏ rơi xuống giữa phòng khách."

    "Không ai nhặt lên quá lâu."

    menu:
        "Tâm thấy Quang là người như thế nào?"

        "Đáng tin":
            $ story_flag('tam_quang_first_impression_reliable')
            $ story_add('thienan_quang_trust', 1)
            $ story_add('tam_observation', 1)

            "Tâm từng gặp Quang vài lần trước đây."

            "Lần nào anh cũng vừa phải. Không nhiệt tình quá mức, không xa cách khó chịu."

            "Nhưng tối nay, khi nhìn anh đặt tập tài liệu đúng ngay bên tay thuận của Thiên An, cô bỗng thấy anh đáng tin theo một cách rất lặng."

        "Hiền quá":
            $ story_flag('tam_quang_first_impression_gentle')
            $ story_add('family_pressure_thienan', 1)

            "Quang hiền."

            "Có lẽ hơi quá hiền."

            "Ở cạnh Thiên An, sự tử tế của anh đôi khi giống một chiếc áo khoác được đặt sẵn trên ghế."

            "Có cũng tốt. Không ai ghét."

            "Nhưng không chắc người cần nó có nhớ khoác lên hay không."

        "Khó nói rõ":
            $ story_flag('tam_quang_first_impression_uncertain')
            $ story_add('tam_observation', 1)

            "Tâm không chắc nên gọi cảm giác ấy là gì."

            "Quang không nổi bật theo kiểu khiến người khác phải quay đầu."

            "Nhưng anh có mặt ở đó, vừa đủ gần, vừa đủ im, như thể nếu có chuyện gì xảy ra, anh sẽ là người đầu tiên kéo chiếc ghế bị lệch lại đúng chỗ."

    tam_father "Quang."

    quang "Dạ chú."

    tam_father "Công việc trong Nam lần này, cháu đi cùng An?"

    quang "Dạ. Cháu đi trước một ngày để kiểm tra hồ sơ bên chi nhánh."

    tam_father "Ừ. Vất vả cho cháu."

    quang "Việc của cháu mà chú."

    "Bố Tâm gật đầu."

    "Không khen thêm."

    "Nhưng với ông, một cái gật đầu đã là khá nhiều."

    "Tâm nhìn cả nhà."

    "Cô bỗng hiểu vì sao ba mẹ chưa bao giờ nhắc đến chuyện yêu đương giữa Quang và Thiên An."

    "Không phải vì họ không quý anh."

    "Mà có lẽ vì họ đã quý anh quá lâu, chờ quá lâu, rồi tự hiểu rằng có những chuyện nếu bên trong không tự mở cửa, người ngoài đứng mãi ở hiên cũng vô ích."

    $ story_flag('quang_intro_seen')
    $ story_flag('tam_knows_quang_university_history')

    return