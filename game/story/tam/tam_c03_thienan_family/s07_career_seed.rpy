# FILE: game/story/tam/tam_c03_thienan_family/s07_career_seed.rpy
# Scene file.

label tam_c03_thienan_family_s07_career_seed:
    scene black
    with fade

    $ story_flag('tam_c03_career_seed_seen')
    $ unlock_character_section("tam", "narrative_function")
    $ unlock_character_section("thienan", "narrative_function")

    "Đêm trước khi Thiên An bay lại vào Nam, Tâm thấy trên bàn học của mình có một cuốn sổ nhỏ."

    "Bìa màu xanh đậm."

    "Không có hoa văn."

    "Chỉ có một tờ giấy nhớ dán ở góc trên."

    "Nét chữ của Thiên An rất gọn."

    thienan neutral "Cho em. Không phải giáo trình. Đừng sợ."

    "Tâm cầm cuốn sổ lên."

    "Bên trong là vài trang ghi chú về cách đọc hợp đồng lao động, cách kiểm tra email công việc, cách ghi lại những trao đổi quan trọng sau cuộc họp."

    "Mỗi mục đều ngắn."

    "Không dạy đời."

    "Không có câu nào kiểu 'em phải cố gắng'."

    "Chỉ toàn những thứ rất thực tế."

    "Ở trang cuối, Thiên An viết một dòng."

    thienan neutral "Đừng làm việc chăm chỉ trước khi em biết mình đang làm đúng việc."

    "Tâm đọc đi đọc lại câu đó."

    "Ngoài hành lang có tiếng bước chân."

    tam neutral "Chị An."

    thienan neutral "Em thấy rồi à?"

    tam smile "Vâng."

    thienan neutral "Cầm lấy mà dùng. Mấy thứ này không ai dạy kỹ đâu."

    tam confused "Sao chị không đưa trực tiếp cho em?"

    thienan bored "Vì đưa trực tiếp thì em sẽ hỏi rất nhiều."

    tam irritated "Em đâu có hỏi nhiều."

    thienan teasing "Câu vừa rồi tính là một câu."

    "Tâm mím môi."

    "Thiên An nhìn cô, ánh mắt dịu hơn thường ngày."

    thienan neutral "Công việc đầu tiên dễ khiến người ta nghĩ rằng chỉ cần ngoan là đủ."

    tam neutral "Không đủ ạ?"

    thienan neutral "Không."

    thienan neutral "Ngoan chỉ giúp em ít bị ghét."

    thienan neutral "Còn muốn đi xa, em phải biết mình đang ký gì, nghe gì, im lặng lúc nào, và lúc nào không được im."

    "Tâm nhìn cuốn sổ trong tay."

    "Bỗng nhiên cô thấy nó không giống một món quà."

    "Nó giống một cái áo khoác được gấp sẵn."

    "Thiên An không nói giữ ấm."

    "Nhưng đã để nó ở đó trước khi trời lạnh."

    menu:
        "Tâm tiếp nhận lời khuyên của Thiên An thế nào?"

        "Nghiêm túc ghi nhớ":
            $ story_add('career_tam', 2)
            $ story_add('tam_self_clarity', 1)
            $ story_flag('tam_took_thienan_career_advice_seriously')
            $ unlock_character_section("tam", "core_traits")
            $ unlock_character_section("thienan", "core_traits")

            tam neutral "Em sẽ đọc kỹ."

            thienan smile "Tốt."

            tam neutral "Và nếu không hiểu, em sẽ hỏi."

            thienan tired "Hỏi vừa thôi."

            tam smile "Chị vừa bảo lúc nào không được im mà."

            "Thiên An nhìn cô."

            "Rồi cô bật cười."

            thienan smile "Ừ. Chị tự chuốc lấy."

        "Cảm thấy mình bị so sánh với chị":
            $ story_add('tam_insecurity', 1)
            $ story_add('career_tam', 1)
            $ story_flag('tam_felt_compared_to_thienan')
            $ unlock_character_section("tam", "inner_layer")

            tam melancholic "Chị lúc nào cũng biết mấy chuyện này nhỉ."

            thienan confused "Không phải lúc nào."

            tam smile "Nhưng trông giống vậy."

            "Thiên An im lặng."

            "Một lúc sau, cô kéo ghế ngồi xuống cạnh Tâm."

            thienan neutral "Chị cũng từng không biết."

            tam surprised "Thật ạ?"

            thienan bored "Em nghĩ chị sinh ra đã biết đọc hợp đồng à?"

            tam embarrassed "Không. Nhưng..."

            thienan neutral "Chị học vì từng ký nhầm một bản phụ lục rất ngu."

            "Tâm chớp mắt."

            thienan teasing "Đừng nhìn chị như thấy thú quý hiếm."

            tam laughing "Em xin lỗi."

            "Lần đầu tiên trong tối đó, khoảng cách giữa hai chị em nhẹ đi một chút."

        "Cảm ơn chị thật lòng":
            $ story_add('thienan_self_assertion', 1)
            $ story_add('tam_self_clarity', 1)
            $ story_flag('tam_thanked_thienan_honestly')
            $ unlock_character_section("thienan", "inner_layer")
            $ unlock_character_section("tam", "fixed_relationships")

            tam neutral "Cảm ơn chị."

            thienan neutral "Ừ."

            tam smile "Em nói thật đấy."

            "Thiên An khựng lại."

            "Tâm ôm cuốn sổ vào ngực, hơi ngại nhưng vẫn nhìn thẳng vào chị."

            tam bashful "Em biết chị bận. Vậy mà vẫn chuẩn bị cái này cho em."

            thienan neutral "Không mất nhiều thời gian."

            tam neutral "Nhưng chị vẫn làm."

            "Thiên An quay mặt đi."

            "Một lúc sau, cô đưa tay chỉnh lại mép giấy nhớ trên bìa sổ."

            thienan smile "Dán hơi lệch."

            tam smile "Không sao. Em thích vậy."

    if story_has_flag('tam_support_quang'):
        $ unlock_character_section("quang", "notes")
        "Tâm định hỏi thêm về Quang."

        "Nhưng nhìn vẻ mệt trên mặt Thiên An, cô lại thôi."

        "Có những chuyện nếu muốn đẩy, cũng phải chọn lúc người kia còn sức để bước."

    elif story_has_flag('tam_quang_interest_seed'):
        $ unlock_character_section("quang", "inner_layer")
        "Tâm nhớ đến túi giấy Quang gửi lúc sáng."

        "Cô bỗng không biết nên đặt nó ở đâu trong câu chuyện của Thiên An."

        "Hay trong câu chuyện của chính mình."

    else:
        "Tâm đặt cuốn sổ vào ngăn bàn."

        "Rất cẩn thận."

    thienan neutral "Tâm."

    tam neutral "Dạ?"

    thienan neutral "Sau này đi làm, nếu có ai khiến em cảm thấy mình phải nhỏ lại mới vừa với chỗ đó..."

    "Thiên An dừng một chút."

    thienan neutral "Thì chỗ đó không đáng."

    "Tâm nhìn chị."

    "Thiên An đã đứng lên, vẻ mặt trở lại bình thường."

    thienan tired "Muộn rồi. Ngủ đi."

    tam smile "Chị cũng vậy."

    thienan smile "Ừ."

    "Thiên An đi ra cửa."

    "Trước khi rời phòng, cô dừng lại, kéo tay nắm cửa khép nhẹ hơn mọi khi."

    "Cánh cửa không đóng hẳn."

    "Để lại một khe sáng mỏng ngoài hành lang."

    $ story_flag('tam_c03_thienan_family_completed_seed')
    $ unlock_character_section("thienan", "notes")
    $ unlock_character_section("tam", "notes")

    return