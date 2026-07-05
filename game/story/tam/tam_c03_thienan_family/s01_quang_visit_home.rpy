# FILE: game/story/tam/tam_c03_thienan_family/s01_quang_visit_home.rpy
# Scene file.

label tam_c03_thienan_family_s01_quang_visit_home:
    scene black
    with fade

    $ story_flag('quang_introduced')
    $ story_flag('quang_familiar_with_tam_family')
    $ unlock_library_character("quang")
    $ unlock_character_section("quang", "role")
    $ unlock_character_section("quang", "public_identity")
    $ unlock_character_section("quang", "fixed_relationships")
    $ unlock_character_section("thienan", "fixed_relationships")

    "Hơn tám giờ tối, chuông cửa vang lên."

    "Tâm vừa đi ra hành lang thì mẹ cô đã từ bếp nói vọng ra."

    tam_mother "Tâm, ra mở cửa giúp mẹ. Chắc Quang đấy."

    tam surprised "Anh Quang ạ?"

    tam_mother "Ừ. Chị con bảo cậu ấy ghé lấy ít hồ sơ."

    "Cách mẹ nói rất tự nhiên."

    "Tự nhiên như thể người tên Quang ấy vốn đã nằm trong danh sách những người có thể xuất hiện ở nhà vào buổi tối mà không cần giải thích nhiều."

    "Tâm mở cửa."

    quang neutral "Chào Tâm."

    tam smile "Em chào anh."

    "Quang đứng ngoài cửa, tay cầm một túi tài liệu màu xám. Áo sơ mi của anh phẳng phiu, nhưng cổ tay áo có một nếp gấp nhỏ, giống như vừa bị kéo vội xuống sau một cuộc họp dài."

    quang smile "Anh làm phiền giờ này không?"

    tam teasing "Nếu anh nói không thì mẹ em vẫn sẽ hỏi anh ăn tối chưa."

    quang embarrassed "Anh đoán vậy."

    tam_mother "Quang à, ăn tối chưa cháu?"

    "Từ trong bếp, giọng mẹ Tâm vang ra gần như ngay lập tức."

    "Tâm nhướng mày."

    quang embarrassed "Dạ cháu ăn rồi ạ."

    tam_mother "Câu này cháu nói ba năm rồi."

    quang bashful "Dạ... lần này là thật ạ."

    "Tâm bật cười."

    tam laughing "Anh vào đi."

    "Quang thay dép rất gọn."

    "Anh không cần Tâm chỉ. Đôi dép dành cho khách nằm ở kệ thứ hai, anh lấy đúng đôi màu nâu sẫm như mọi lần."

    "Khi đi ngang qua phòng khách, anh hơi cúi người chào bố Tâm."

    quang neutral "Cháu chào chú."

    tam_father "Ừ, Quang đấy à. Lại việc công ty?"

    quang neutral "Dạ. Có vài hồ sơ chị An cần mang đi sáng mai."

    tam_father "Ngồi đi. Uống trà không?"

    quang smile "Dạ thôi ạ. Cháu lấy tài liệu rồi về ngay, không làm phiền nhà mình."

    tam_mother "Cứ nói chuyện khách sáo mãi."

    "Quang chỉ cười."

    "Một nụ cười hiền, hơi ngại, nhưng không hề lúng túng."

    "Anh quen với căn nhà này vừa đủ để không xa lạ."

    "Nhưng cũng giữ khoảng cách vừa đủ để không ai có thể gọi anh là người nhà."

    thienan neutral "Anh đến rồi à?"

    "Thiên An từ cầu thang đi xuống."

    "Cô đã thay sang một bộ đồ ở nhà đơn giản, tóc buộc thấp sau gáy. Trên tay vẫn cầm điện thoại."

    quang neutral "Ừ. Anh mang bản hợp đồng bổ sung và báo cáo kiểm kê."

    thienan neutral "Cảm ơn anh."

    "Cách Thiên An nhận tập hồ sơ rất tự nhiên."

    "Cách Quang đưa nó cho cô cũng vậy."

    "Không dư một cử chỉ."

    "Không thiếu một nhịp hiểu nhau."

    tam neutral "Hai người hẹn nhau từ trước ạ?"

    thienan neutral "Không hẳn. Chị nhờ anh ấy ghé qua sau cuộc họp."

    quang smile "Anh tiện đường."

    thienan bored "Nhà anh ngược hướng."

    quang embarrassed "Thì... cũng không ngược lắm."

    "Thiên An nhìn anh."

    "Quang ho khẽ."

    quang neutral "Ngược. Nhưng không xa."

    tam teasing "Anh Quang thật thà ghê."

    thienan smile "Từ hồi đại học đã vậy rồi."

    tam surprised "Hai người học chung đại học ạ?"

    quang neutral "Ừ. Bọn anh học cùng trường kinh tế. Khác lớp, nhưng có vài môn chung."

    thienan neutral "Sau đó làm cùng công ty."

    tam smile "Lâu thật."

    thienan neutral "Ừ. Cũng lâu rồi."

    "Thiên An nói vậy, rồi cúi xuống lật hồ sơ."

    "Giọng cô bình thường."

    "Bình thường đến mức Tâm không biết nên hiểu chữ 'lâu' kia là thân thiết, hay chỉ đơn giản là nhiều năm."

    menu:
        "Tâm ấn tượng thế nào về Quang?"

        "Anh ấy đáng tin":
            $ story_add('thienan_quang_trust', 1)
            $ story_add('tam_observation', 1)
            $ story_flag('tam_sees_quang_as_reliable')
            $ unlock_character_section("quang", "core_traits")

            "Tâm nhìn Quang đặt từng tập hồ sơ xuống bàn theo thứ tự Thiên An cần."

            "Anh không hỏi lại."

            "Thiên An cũng không giải thích."

            "Có lẽ sự ăn ý lâu năm chính là như vậy. Không gây chú ý, nhưng khi thiếu đi sẽ lập tức lệch nhịp."

        "Anh ấy hiền quá":
            $ story_add('quang_persistence', 1)
            $ story_add('tam_quang_interest', 1)
            $ story_flag('tam_notices_quang_gentleness')
            $ unlock_character_section("quang", "inner_layer")

            "Quang nói chuyện rất nhỏ nhẹ."

            "Không phải kiểu yếu đuối."

            "Chỉ là anh giống người luôn chừa cho người khác một khoảng để thở."

            "Tâm bỗng nghĩ, với một người như Thiên An, điều đó có lẽ vừa tốt... vừa rất khó."

        "Chị An vẫn giữ khoảng cách":
            $ story_add('tam_observation', 2)
            $ story_add('family_pressure_thienan', 1)
            $ story_flag('tam_noticed_thienan_distance_from_quang')
            $ unlock_character_section("thienan", "inner_layer")

            "Thiên An cảm ơn Quang."

            "Lịch sự. Tự nhiên. Đúng mực."

            "Nhưng cũng chỉ đến thế."

            "Tâm không hiểu vì sao mình lại thấy hơi tiếc."

    quang neutral "Vậy anh về trước. Sáng mai anh sẽ ra sân bay sớm."

    thienan neutral "Không cần. Em tự đi được."

    quang smile "Anh biết. Nhưng anh cũng phải đi."

    thienan confused "Anh cũng đi?"

    quang neutral "Anh gửi mail rồi. Chắc em chưa đọc."

    "Thiên An im lặng một nhịp."

    thienan tired "Ừ. Chắc vậy."

    quang smile "Không sao. Anh in lịch trình rồi."

    "Anh đặt một tờ giấy gấp đôi lên mặt bàn."

    "Thiên An nhìn tờ giấy."

    "Không nói gì."

    "Nhưng cô không trả lại."

    return