# FILE: game/story/tam/tam_c03_thienan_family/s02_business_trip_preparation.rpy
# Scene file.

label tam_c03_thienan_family_s02_business_trip_preparation:
    scene bg_hoangminh_villa_living_room_day
    with fade

    $ story_flag('thienan_business_trip_south')
    $ story_flag('family_business_trouble_seed')
    $ unlock_character_section("thienan", "narrative_function")
    $ unlock_character_section("quang", "narrative_function")

    "Sáng hôm sau, phòng khách yên tĩnh hơn thường lệ."

    "Chiếc vali của Thiên An đặt cạnh cửa."

    "Một chiếc túi laptop đặt lên trên, dây đeo được cuộn gọn. Bên cạnh là áo khoác mỏng và một tập hồ sơ đã được bọc bằng túi chống nước."

    "Tâm đứng ở bậc cầu thang, nhìn chị mình kiểm tra lại mọi thứ."

    thienan neutral "Laptop."

    quang neutral "Trong túi. Sạc ở ngăn phải."

    thienan neutral "USB backup."

    quang neutral "Ngăn trước. Cái màu đen."

    thienan neutral "Hợp đồng bản cứng."

    quang neutral "Vali. Lớp trên cùng. Anh để kẹp xanh."

    thienan neutral "Bản sao giấy phép."

    quang neutral "Túi hồ sơ. Phía sau báo cáo tài chính."

    "Hai người nói chuyện như đang đọc một đoạn script đã tập rất nhiều lần."

    "Không ai nhìn ai quá lâu."

    "Không ai cần nhắc lại."

    "Tâm bỗng thấy họ giống một cặp đôi đã sống cùng nhau nhiều năm."

    "Rồi ngay sau đó, cô lại thấy không giống."

    "Vì giữa hai người có sự ăn ý của công việc, nhưng không có sự lơ đãng của thân mật."

    tam neutral "Hai người lúc nào cũng kiểm tra kiểu này ạ?"

    quang smile "Khi đi với chị An thì nên kiểm tra hai lần."

    thienan irritated "Ý anh là em hay quên?"

    quang neutral "Ý anh là em thường nhớ quá nhiều việc cùng lúc."

    "Thiên An khựng lại."

    "Câu nói ấy không giống khen. Cũng không giống trách."

    "Nó giống một người đã nhìn thấy phần mệt của cô từ lâu, nhưng chọn cách nói thật nhẹ."

    thienan neutral "Anh cũng không cần đi cùng lần này."

    quang smile "Anh biết."

    thienan confused "Vậy sao vẫn đi?"

    quang neutral "Vì bên đó có vài người sẽ nói chuyện dễ hơn nếu anh có mặt."

    thienan bored "Anh đang nói giảm."

    quang embarrassed "Ừ. Hơi nhiều người."

    tam confused "Có vấn đề lớn lắm ạ?"

    "Quang nhìn Thiên An."

    "Thiên An kéo khóa vali lại."

    thienan neutral "Chưa lớn. Nhưng nếu để lâu thì sẽ lớn."

    tam worried "Vậy sao chị không nói với bố mẹ?"

    thienan neutral "Bố mẹ biết phần cần biết rồi."

    tam melancholic "Còn phần không cần biết?"

    "Thiên An nhìn Tâm."

    "Ánh mắt ấy rất bình tĩnh."

    "Cũng rất mệt."

    thienan smile "Để chị biết là đủ."

    menu:
        "Tâm nhìn sự ăn ý giữa Thiên An và Quang thế nào?"

        "Họ thật sự tin nhau":
            $ story_add('thienan_quang_trust', 2)
            $ story_add('quang_persistence', 1)
            $ story_flag('tam_noticed_thienan_quang_work_trust')
            $ unlock_character_section("quang", "core_traits")
            $ unlock_character_section("thienan", "fixed_relationships")

            "Tâm nhìn cách Quang cầm túi hồ sơ thay Thiên An."

            "Anh không giành việc."

            "Chỉ cầm đúng thứ cô đang định với tới."

            "Thiên An không cảm ơn."

            "Cũng không từ chối."

            "Sự tin tưởng đôi khi trông giống hệt thói quen."

        "Họ chỉ là đồng nghiệp quá quen việc":
            $ story_add('career_tam', 1)
            $ story_add('tam_observation', 1)
            $ story_flag('tam_reads_quang_thienan_as_professional')
            $ unlock_character_section("thienan", "public_identity")

            "Tâm tự nhắc mình đừng nghĩ quá nhiều."

            "Người làm việc chung lâu năm vốn sẽ ăn ý."

            "Nhất là với người như Thiên An, ai ở cạnh chị đủ lâu mà không học được nhịp của chị thì chắc đã bị loại từ vòng gửi xe rồi."

        "Anh Quang hiểu chị ấy hơn chị muốn thừa nhận":
            $ story_add('thienan_quang_trust', 1)
            $ story_add('tam_observation', 2)
            $ story_add('quang_persistence', 1)
            $ story_flag('tam_noticed_quang_understands_thienan')
            $ unlock_character_section("quang", "inner_layer")
            $ unlock_character_section("thienan", "inner_layer")

            "Quang không hỏi Thiên An có mệt không."

            "Anh chỉ lấy từ túi ra một chai nước nhỏ, vặn nắp trước rồi đặt cạnh tay cô."

            "Thiên An liếc nhìn."

            "Không uống ngay."

            "Nhưng cũng không đẩy ra."

    tam_father "Ra sân bay thì gọi chú một tiếng."

    thienan neutral "Dạ."

    tam_mother "Đừng bỏ bữa."

    thienan smile "Dạ."

    tam_mother "Mẹ nói thật đấy."

    thienan neutral "Con cũng trả lời thật mà."

    "Tâm nhìn mẹ chỉnh lại cổ áo cho Thiên An."

    "Thiên An đứng yên."

    "Rất ngoan."

    "Rất giống một người đã quen để người khác yên tâm bằng dáng vẻ của mình."

    quang neutral "Đến giờ rồi."

    thienan neutral "Ừ."

    "Thiên An kéo vali."

    "Bánh xe lăn qua nền nhà, phát ra một tiếng rất nhỏ."

    "Tâm bỗng thấy căn nhà rộng hơn khi cánh cửa đóng lại."

    return
