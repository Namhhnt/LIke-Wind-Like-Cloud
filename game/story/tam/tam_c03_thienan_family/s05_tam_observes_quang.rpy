# FILE: game/story/tam/tam_c03_thienan_family/s05_tam_observes_quang.rpy
# Scene file.

label tam_c03_thienan_family_s05_tam_observes_quang:
    scene bg_tam_family_living_room_evening
    with fade

    $ story_flag('tam_observed_quang_after_trip')
    $ unlock_character_section("quang", "inner_layer")

    "Tối hôm sau, Quang quay lại."

    "Lần này anh không bấm chuông lâu."

    "Chỉ một tiếng rất ngắn."

    "Tâm ra mở cửa, thấy anh đứng bên ngoài với một phong bì hồ sơ trên tay."

    quang neutral "Xin lỗi. Anh để sót bản xác nhận bên chị An."

    tam neutral "Chị An đang ở phòng khách. Nhưng hình như chị ngủ rồi."

    quang confused "Ngủ?"

    "Tâm nghiêng người để Quang nhìn vào."

    "Thiên An đang ngồi trên sofa."

    "Laptop đặt trên đùi. Màn hình đã tối. Đầu cô hơi nghiêng, một tay vẫn đặt trên bàn phím."

    "Quang đứng yên một nhịp."

    "Rồi anh hạ giọng."

    quang neutral "Anh vào một chút được không?"

    tam neutral "Dạ."

    "Quang đi rất khẽ."

    "Anh không gọi Thiên An dậy."

    "Chỉ đặt phong bì lên bàn, rồi cẩn thận rút laptop khỏi tay cô."

    "Động tác của anh chậm đến mức gần như không phát ra tiếng."

    "Anh kiểm tra màn hình, lưu lại file đang mở, rồi gập máy."

    scene cg_tam_c03_quang_jacket
    with dissolve

    "Sau đó, anh lấy chiếc áo khoác treo trên thành ghế, phủ lên vai Thiên An."

    "Thiên An hơi cựa mình."

    thienan tired "Quang...?"

    quang neutral "Ừ. Ngủ tiếp đi."

    thienan confused "Hồ sơ..."

    quang smile "Anh để trên bàn rồi."

    thienan tired "Chuyến bay..."

    quang neutral "Đổi sang chiều mai. Em không cần dậy lúc năm giờ."

    "Thiên An mở mắt."

    "Cô nhìn Quang, vẻ tỉnh táo trở lại một nửa."

    thienan neutral "Ai cho anh đổi?"

    quang embarrassed "Anh."

    thienan irritated "Anh Quang."

    quang neutral "Nếu em muốn mắng thì mai mắng. Bây giờ ngủ."

    "Thiên An nhìn anh."

    "Quang nhìn lại."

    "Không ai nói gì trong vài giây."

    "Cuối cùng, Thiên An kéo áo khoác lại."

    thienan bored "Mai em mắng thật đấy."

    quang smile "Ừ."

    "Thiên An nhắm mắt."

    "Quang đứng thêm một lúc."

    scene bg_tam_family_living_room_evening
    with dissolve

    "Rồi anh quay ra, thấy Tâm vẫn đứng gần cửa."

    tam neutral "Anh hay làm vậy à?"

    quang surprised "Làm gì?"

    tam teasing "Tự ý đổi lịch bay của chị An rồi chờ mai bị mắng."

    quang embarrassed "Không hay lắm."

    tam smile "Nhưng có làm."

    quang neutral "Khi cần."

    "Anh nói rất khẽ."

    "Như thể chuyện đó không đáng nhắc tới."

    menu:
        "Tâm nghĩ gì sau khi nhìn thấy cách Quang chăm sóc Thiên An?"

        "Anh ấy xứng đáng có một cơ hội":
            $ story_add('thienan_quang_trust', 1)
            $ story_add('quang_persistence', 2)
            $ story_flag('tam_support_quang')
            $ story_flag('tam_sees_quang_as_possible_for_thienan')
            $ unlock_character_section("quang", "narrative_function")
            $ unlock_character_section("thienan", "fixed_relationships")

            "Tâm nhìn Quang cúi xuống chỉnh lại đôi dép đi trong nhà cho ngay ngắn trước khi rời đi."

            "Một người nhớ được những điều nhỏ như vậy."

            "Một người ở cạnh lâu như vậy."

            "Nếu nói hoàn toàn không có cơ hội, có lẽ hơi tàn nhẫn."

        "Chị An chưa từng nhìn anh ấy theo cách đó":
            $ story_add('tam_observation', 2)
            $ story_add('family_pressure_thienan', 1)
            $ story_flag('tam_knows_thienan_not_open_to_quang_yet')
            $ unlock_character_section("thienan", "inner_layer")
            $ unlock_character_section("quang", "inner_layer")

            "Tâm thấy rõ sự dịu dàng trong từng động tác của Quang."

            "Cũng thấy rõ sự bình thản trong cách Thiên An nhận lấy nó."

            "Có những việc được làm quá lâu sẽ trở thành hiển nhiên."

            "Mà hiển nhiên thì đôi khi rất khó trở thành tình yêu."

        "Có lẽ anh ấy nên dừng lại":
            $ story_add('tam_quang_interest', 1)
            $ story_add('tam_observation', 1)
            $ story_flag('tam_quang_interest_seed')
            $ story_flag('tam_thinks_quang_should_let_go')
            $ unlock_character_section("quang", "core_traits")
            $ unlock_character_section("tam", "inner_layer")

            "Không hiểu sao, Tâm thấy hơi khó chịu."

            "Không phải với Quang."

            "Cũng không phải với Thiên An."

            "Chỉ là có một người cứ lặng lẽ đứng đó, chuẩn bị mọi thứ, rồi tự xem mình là phần ngoài lề."

            "Tâm bỗng nghĩ, nếu là cô, có lẽ cô sẽ không nỡ để người đó chờ mãi."

    quang neutral "Anh về đây."

    tam neutral "Anh Quang."

    quang confused "Ừ?"

    tam neutral "Anh thích chị em lâu rồi đúng không?"

    "Câu hỏi rơi xuống rất thẳng."

    "Quang hơi khựng lại."

    "Rồi anh cười."

    "Không phủ nhận."

    "Cũng không thừa nhận."

    quang smile "Em còn nhỏ mà hỏi chuyện người lớn ghê."

    tam irritated "Em đi làm rồi."

    quang embarrassed "Ừ. Anh xin lỗi."

    "Anh nhìn về phía phòng khách."

    "Thiên An vẫn ngủ. Chiếc áo khoác trên vai cô hơi trượt xuống một bên."

    quang neutral "Có những chuyện không phải cứ thích là nên nói."

    tam neutral "Vậy cứ im mãi ạ?"

    quang melancholic "Im không tốt."

    quang smile "Nhưng nói sai lúc còn tệ hơn."

    "Tâm không biết đáp gì."

    "Quang cúi đầu chào cô, rồi bước ra ngoài."

    "Cánh cửa khép lại rất nhẹ."

    "Nhẹ đến mức Thiên An không tỉnh."

    return
