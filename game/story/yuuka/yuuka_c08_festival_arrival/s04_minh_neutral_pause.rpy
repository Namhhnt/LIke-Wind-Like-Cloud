# FILE: game/story/yuuka/yuuka_c08_festival_arrival/s04_minh_neutral_pause.rpy
# Scene file.

label yuuka_c08_festival_arrival_s04_minh_neutral_pause:
    # The reunion always happens at Minh / Hoàng's house.
    # Tâm only witnesses it if she followed Hoàng in scene 03.

    scene bg_hoang_house_living_room_day
    with dissolve

    if c08_tam_met_yuuka:
        "Trong phòng khách, vali của Yuuka vẫn dựng cạnh sofa."

        "Một chiếc áo khoác mỏng đặt trên tay vịn."

        "Cô ngồi rất tự nhiên, nhưng hai bàn tay lại giữ cốc nước lâu hơn mức cần thiết."

        "Hoàng giải thích ngắn gọn rằng Yuuka từng học cùng Minh ở nước ngoài."

        "Không nói thêm."

        "Tâm cũng không hỏi."

        yuuka teasing "So."

        yuuka smile "You are Tâm."

        tam confused "Chị biết em ạ?"

        "Yuuka liếc sang Hoàng."

        yuuka teasing "Ha-kun is not very subtle."

        hoang irritated "Anh kể chuyện bình thường."

        yuuka grinning "Yes. Repeatedly."

        tam flustered "..."

        hoang neutral "Yuu-san."

        yuuka smile "What? I am helping."

        "Tâm không biết Yuuka đang giúp ai."

        "Nhưng vẻ căng thẳng ở cửa đã nhẹ đi."

        "Yuuka không giống hình dung ban đầu của cô."

        "Không xa cách. Không kiểu cách."

        "Cô hoạt bát hơn, thậm chí hơi trẻ con."

        "Chỉ có đôi lúc, giữa hai câu đùa, ánh mắt cô lại vô thức dừng ở phía cửa."

        "Rất nhanh."

        "Như thể chính cô cũng không muốn ai phát hiện mình đang đợi."

        "Tiếng khóa cửa vang lên."

        "Yuuka im giữa một câu nói."

        "Hoàng quay đầu."

        hoang neutral "Anh Minh về."

        "Cửa mở."

        "Minh bước vào, tay vẫn cầm chìa khóa."

        "Anh nhìn thấy Tâm trước."

        minh neutral "Tâm."

        tam neutral "Chào anh."

        "Sau đó ánh mắt anh chuyển sang người đang ngồi cạnh sofa."

        "Yuuka đã đứng dậy."

        "Không ai nói gì trong một nhịp."

        "Một nhịp rất nhỏ."

        "Nhưng căn phòng đủ yên để nó có trọng lượng."

        minh neutral "..."

        yuuka neutral "..."

        "Minh đặt chìa khóa lên kệ."

        minh neutral "Chuyến bay ổn chứ?"

        yuuka smile "Barely survivable."

        yuuka teasing "The food was an international crime."

        minh neutral "Vậy là vẫn bình thường."

        "Yuuka bật cười."

        "Minh cũng hơi cong khóe môi."

        "Không có cái ôm."

        "Không có lời nào đủ để xác nhận hai người từng là gì."

        "Chỉ có một sự thân thuộc không cần được giới thiệu lại."

        $ story_add("minh_yuuka_trust", 10)
        $ story_add("minh_yuuka_intimacy", 10)
        $ story_add("minh_yuuka_unresolved", 10)
        $ story_flag("yuuka_route_unlocked")
        $ story_flag("group_notices_past")

        menu:
            "Tâm chú ý đến điều gì?"

            "Nhịp dừng trước câu chào.":
                $ story_add("tam_observation", 10)
                $ story_add("minh_yuuka_unresolved", 5)
                $ story_flag("noticed_minyuu_pause")

                "Tâm không biết bên trong một giây im lặng ấy có gì."

                "Nhưng nó không giống sự ngượng ngùng của hai người lâu ngày chưa gặp."

                "Nó giống một cánh cửa cả hai đều biết nằm ở đó, nhưng chưa ai đặt tay lên."

            "Cách Yuuka giấu căng thẳng bằng một câu đùa.":
                $ story_add("tam_respect_yuuka", 10)
                $ story_add("tam_observation", 5)
                $ story_flag("tam_noticed_yuuka_emotional_control")

                "Từ lúc Minh bước vào, giọng Yuuka sáng hơn một chút."

                "Không run."

                "Không yếu."

                "Chỉ sáng hơn mức tự nhiên."

                "Tâm từng làm điều tương tự: nói nhanh hơn để không ai hỏi vì sao mình im."

            "Giữ cách hiểu đơn giản: họ là bạn cũ.":
                $ story_add("tam_self_clarity", 10)
                $ story_add("tam_respect_yuuka", 5)
                $ story_flag("tam_does_not_project_onto_minyuu")

                "Có thể giữa họ từng có chuyện."

                "Cũng có thể không."

                "Tâm không lấy vài giây quan sát được để viết thay cả quá khứ của hai người."

                "Ít nhất, lần này cô không cần biến điều mình chưa biết thành điều đáng sợ."

        "Điện thoại Tâm rung lên."

        thienan irritated "Mười lăm phút của em dài hơn giờ hành chính à?"

        "Tâm nhìn đồng hồ."

        tam shocked "Chết rồi."

        hoang confused "Sao thế?"

        tam neutral "Em phải đi đón chị An tới đám cưới Duyên."

        hoang neutral "Anh đưa em đi."

        "Tâm nhìn vali cạnh sofa, rồi nhìn Yuuka."

        tam neutral "Anh ở lại đi. Em gọi xe được."

        yuuka smile "Please go. I have already stolen enough of your afternoon."

        tam smile "Hẹn gặp chị ở Festival."

        yuuka smile "I will try not to create extra paperwork."

        tam teasing "Em không tin đạo diễn."

        yuuka grinning "Smart girl."

        "Tâm bước ra cửa."

        "Trước khi cánh cửa khép lại, cô nghe Hoàng hỏi Yuuka có đói không."

        "Rồi tiếng Minh từ phía bếp vọng ra, bình tĩnh như thể bốn năm hay bốn ngày đều có thể được đặt vào cùng một câu."

        minh neutral "Trong tủ còn đồ. Anh nấu."

        "Tâm không quay lại."

    else:
        # Yuuka POV branch when Tâm did not follow Hoàng home.
        "Căn nhà gần như không thay đổi."

        "Chiếc sofa cũ."

        "Bàn trà."

        "Khung cửa sổ nhìn ra khoảng sân."

        "Cả góc bếp nằm ở nơi Yuuka vẫn nhớ."

        "Mọi thứ gọn gàng đến mức có phần bất lịch sự với thời gian."

        "Hoàng mang nước ra rồi vào phòng cất hành lý giúp cô."

        "Yuuka ngồi một mình trong phòng khách."

        "Cô nhìn cốc nước."

        "Không uống."

        "Tiếng khóa cửa vang lên."

        "Bàn tay cô giữ cốc chặt hơn một chút."

        "Minh bước vào."

        "Anh dừng lại khi nhìn thấy cô."

        "Yuuka đã chuẩn bị rất nhiều câu cho khoảnh khắc này."

        "Không câu nào chịu xuất hiện."

        minh neutral "..."

        yuuka neutral "..."

        "Minh đặt chìa khóa lên kệ."

        minh neutral "Chuyến bay ổn chứ?"

        "Một câu rất bình thường."

        "Nhờ thế, Yuuka mới nhớ cách thở."

        menu:
            "Yuuka trả lời thế nào?"

            "Dùng một câu đùa để phá khoảng im.":
                $ c08_minyuu_greeting_mode = "old_joke"

                $ story_add("minh_yuuka_intimacy", 5)
                $ story_add("minh_yuuka_unresolved", 5)
                $ story_flag("yuuka_used_old_rhythm")

                yuuka teasing "No."

                yuuka irritated "The airline tried to kill me with steamed vegetables."

                minh neutral "Em vẫn còn đủ sức phàn nàn."

                yuuka smile "A professional survives."

                "Khóe môi Minh cong lên rất nhẹ."

                "Chỉ một chút."

                "Nhưng đủ để Yuuka biết anh vẫn nhận ra nhịp cũ."

            "Chào anh như một người bạn lâu ngày gặp lại.":
                $ c08_minyuu_greeting_mode = "formal_friend"

                $ story_add("minh_yuuka_trust", 5)
                $ story_add("boundary_score", 5)
                $ story_flag("yuuka_kept_arrival_formal")

                yuuka smile "Long time no see, Minh."

                minh neutral "Ừ. Lâu rồi."

                "Câu trả lời không lạnh."

                "Cũng không gần."

                "Nó đặt giữa hai người một khoảng vừa đủ để không ai phải lùi thêm."

            "Chỉ nói điều thật nhất lúc này.":
                $ c08_minyuu_greeting_mode = "returned"

                $ story_add("minh_yuuka_trust", 5)
                $ story_add("minh_yuuka_intimacy", 5)
                $ story_add("minh_yuuka_unresolved", 5)
                $ story_flag("yuuka_said_she_returned")

                yuuka neutral "Em về rồi."

                "Minh nhìn cô."

                "Không hỏi cô gọi nơi nào là nơi để về."

                minh neutral "Ừ."

                minh neutral "Chào mừng em trở lại."

                "Yuuka cúi mắt xuống cốc nước."

                "Mặt nước rung rất nhẹ."

        # Core arrival state. This does not resolve the past relationship.
        $ story_add("minh_yuuka_trust", 10)
        $ story_add("minh_yuuka_intimacy", 10)
        $ story_add("minh_yuuka_unresolved", 10)
        $ story_flag("yuuka_route_unlocked")
        $ story_flag("minyuu_reunion_not_yet_defined")

        "Hoàng quay lại phòng khách, nhìn hai người."

        hoang neutral "Hai người nói chuyện xong chưa?"

        yuuka teasing "No."

        yuuka grinning "Your brother has become even worse at welcoming guests."

        minh neutral "Em vẫn chưa uống nước."

        "Yuuka nhìn cốc trong tay."

        "Cô uống một ngụm."

        yuuka neutral "Happy?"

        minh neutral "Tạm được."

        "Hoàng thở ra."

        hoang teasing "Tốt. Hai người vẫn nói chuyện được."

        "Không ai hỏi cậu đang so với điều gì."

    scene black
    with fade

    return