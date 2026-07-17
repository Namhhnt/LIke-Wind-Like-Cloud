# FILE: game/story/yuuka/yuuka_c08_festival_arrival/s03_hoang_introduces_yuuka.rpy
# Scene file.

label yuuka_c08_festival_arrival_s03_hoang_introduces_yuuka:
    scene black
    with fade

    centered "{size=34}Tám ngày trước Liên hoan phim{/size}"

    # New background asset suggested:
    # bg_airport_arrival_day
    scene bg_airport_arrival_day
    with dissolve

    "Máy bay hạ cánh vào gần trưa."

    "Vừa bước khỏi khu kiểm soát, Yuuka đã cảm thấy không khí nơi này khác Nhật Bản."

    "Ấm hơn."

    "Dày hơn."

    "Tiếng bánh xe vali lăn trên nền gạch, tiếng Việt vọng từ các quầy đón khách và mùi cà phê trong sảnh đều quen theo một cách khiến cô hơi khó chịu."

    "Không phải nơi này giống ký ức."

    "Mà là cơ thể cô vẫn nhớ nó."

    "Hoàng đứng gần hàng rào đón khách."

    "Cậu giơ tay lên trước."

    hoang happy "Yuu-san."

    yuuka happy "Ha-kun."

    "Yuuka bước tới, nhìn cậu từ đầu đến chân."

    yuuka teasing "Still sweet as ever."

    yuuka grinning "Good. At least one brother remains lovable."

    hoang laughing "Vừa xuống máy bay đã gây chuyện rồi à?"

    yuuka smile "I had a long flight. I deserve entertainment."

    "Hoàng nhận lấy vali từ tay cô."

    hoang smile "Welcome back."

    "Hai chữ cuối làm Yuuka chớp mắt chậm hơn một nhịp."

    yuuka neutral "Thank you."

    "Cô quay sang nhìn dòng người phía sau như thể chỉ đang kiểm tra xem còn hành lý nào chưa lấy."

    "Hoàng không hỏi."

    "Cậu chỉ kéo vali đi chậm hơn để cô bước kịp."

    scene black
    with dissolve

    "Trên đường về, Yuuka nói nhiều hơn bình thường."

    "Đồ ăn trên máy bay."

    "Thời tiết."

    "Lịch giao lưu."

    "Việc cô ghét thảm đỏ nhưng vẫn phải đi trên đó với vẻ mặt như thể mình sinh ra cho chuyện ấy."

    "Cô hỏi mọi người có khỏe không."

    "Hỏi căn nhà còn cái máy pha cà phê cũ không."

    "Hỏi Minh còn làm việc quá giờ không."

    "Nhưng không hỏi câu mình muốn biết nhất."

    scene black
    with dissolve

    "Cũng vào buổi chiều hôm ấy, Tâm rời công ty sớm."

    "Cô phải ghé đón Thiên An để cùng đến đám cưới Duyên và Kim."

    "Chiếc taxi vừa rẽ vào tuyến đường từ sân bay về trung tâm thì dừng ở một đèn đỏ."

    "Tâm đang nhắn cho chị gái thì nghe tiếng động cơ quen thuộc ở làn bên cạnh."

    "Cô ngẩng lên."

    "Xe của Hoàng."

    "Anh đang lái."

    "Bên ghế phụ là một người phụ nữ có mái tóc dài, gương mặt chỉ nhìn nghiêng cũng đủ khiến người khác phải nhìn lại."

    "Cô ấy đang nói gì đó."

    "Hoàng bật cười."

    "Đèn chuyển xanh."

    "Chiếc xe đi trước."

    if c08_tam_hoang_active:
        "Tâm vẫn cầm điện thoại trong tay."

        "Tin nhắn gửi Thiên An mới gõ được một nửa."

        "Hoàng không nói hôm nay anh ra sân bay."

        "Cũng không nhắc đến một người phụ nữ."

        "Một phần trong Tâm biết chỉ cần gọi điện là có câu trả lời."

        "Phần còn lại đã nhìn theo chiếc xe quá lâu."

        menu:
            "Tâm làm gì?"

            "Nhờ tài xế đi theo xe Hoàng.":
                $ c08_tam_followed_hoang = True
                $ c08_yuuka_intro_source = "house"

                $ story_add("tam_observation", 5)

                if c08_tam_high_clarity:
                    $ story_add("tam_self_clarity", 5)
                else:
                    $ story_add("tam_insecurity", 10)

                $ story_flag("tam_followed_hoang_home")
                $ story_flag("tam_delayed_wedding_pickup")

                tam neutral "Chú đi theo chiếc xe phía trước giúp cháu."

                "Bác tài nhìn vào gương."

                "Không hỏi."

                "Đó là một kiểu chuyên nghiệp Tâm rất biết ơn vào lúc này."

                "Cô nhắn nhanh cho Thiên An."

                tam neutral "Em có chút việc. Chị đợi em thêm mười lăm phút nhé."

                thienan neutral "Việc gì?"

                "Tâm nhìn chiếc xe phía trước rẽ vào con đường quen."

                tam neutral "Em chưa biết."

                thienan irritated "Câu trả lời rất đáng tin."

                scene bg_hoang_house_front_door_day
                with dissolve

                "Khi Tâm đến nơi, xe Hoàng đã nằm trong sân."

                "Cô đứng ngoài cổng vài giây."

                "Rồi bấm chuông."

                "Tiếng bước chân từ bên trong tiến lại gần."

                "Cánh cửa mở ra."

                "Người phụ nữ Tâm vừa nhìn thấy trên xe đang đứng trước mặt cô."

                "Ngoài đời, cô ấy còn nổi bật hơn qua lớp kính ô tô."

                "Gương mặt mềm, sáng. Mái tóc dài mang ánh nâu nhẹ dưới nắng. Dáng người cao và thanh thoát đến mức chiếc áo đơn giản cũng trông như được chọn riêng."

                "Nhưng điều làm Tâm khựng lại không hoàn toàn là vẻ ngoài."

                "Là cách cô ấy mở cửa căn nhà này."

                "Tự nhiên."

                "Không cần hỏi ai."

                yuuka smile "Hi."

                tam shocked "..."

                "Yuuka cũng nhìn cô."

                "Nụ cười vẫn còn đó, nhưng ánh mắt vừa đổi rất nhẹ."

                "Hai người phụ nữ đứng trước nhau, mỗi người đều vừa nghĩ ra một giả thuyết không mấy dễ chịu."

                yuuka neutral "Are you looking for someone?"

                tam flustered "Tôi..."

                "Từ bên trong, giọng Hoàng vọng ra."

                hoang neutral "Ai đấy, Yuu-san?"

                "Tâm nghe thấy cách gọi ấy."

                "Yuuka nghe thấy Hoàng biết người ngoài cửa."

                "Cả hai cùng thả lỏng một phần rất nhỏ."

                hoang surprised "Tâm?"

                "Hoàng bước tới, nhìn cô rồi nhìn chiếc taxi vẫn đợi ngoài cổng."

                hoang confused "Sao em lại ở đây?"

                tam irritated "Em cũng đang định hỏi anh câu đó."

                "Yuuka hơi nghiêng đầu."

                "Khóe môi cô cong lên như vừa hiểu được một phần tình huống."

                hoang neutral "À."

                hoang smile "Đây là Yuuka. Bạn cũ của anh và anh Minh."

                yuuka smile "Yuuka Nakamura."

                "Cái tên khớp vào một dòng credit Tâm đã nhìn thấy hai ngày trước."

                tam surprised "Đạo diễn Yuuka Nakamura?"

                yuuka surprised "Oh."

                yuuka teasing "That sounds much more impressive when someone else says it."

                tam neutral "Công ty tôi đang tham gia phần vận hành Festival."

                if c08_tam_leads_festival:
                    tam neutral "Tôi phụ trách nhóm điều phối hồ sơ và lịch khách mời."

                    yuuka smile "Then I should behave carefully around you."

                else:
                    tam neutral "Tôi đang hỗ trợ phần hồ sơ và lịch khách mời."

                    yuuka smile "Then we may see each other again."

                hoang teasing "Hai người định đứng ngoài cửa họp luôn à?"

                "Yuuka lánh sang một bên."

                yuuka smile "Come in."

                $ c08_tam_met_yuuka = True

                $ story_add("tam_respect_yuuka", 10)
                $ story_add("tam_observation", 5)

                if c08_tam_minh_lean:
                    $ story_add("tam_insecurity", 15)
                    $ story_add("tam_observation", 5)
                    $ story_flag("tam_step_back_choice")
                    $ story_flag("yuuka_rival_not_rival_scene")

                else:
                    $ story_add("tam_insecurity", 5)

                $ story_flag("tam_met_yuuka_at_hoang_house")
                $ story_flag("tam_learns_minh_hoang_are_brothers")

            "Gọi Hoàng và hỏi thẳng.":
                $ c08_yuuka_intro_source = "hoang_phone"

                $ story_add("hoang_tam_trust", 10)
                $ story_add("tam_self_clarity", 10)
                $ story_sub("tam_insecurity", 5)
                $ story_flag("tam_asked_hoang_about_yuuka_directly")

                "Tâm bấm gọi."

                "Hoàng bắt máy sau hai hồi chuông."

                hoang neutral "Anh nghe."

                tam teasing "Em vừa thấy anh đi với một cô gái rất đẹp."

                hoang surprised "Em đang ở đâu?"

                tam neutral "Đường sân bay."

                "Phía bên kia im một nhịp."

                hoang teasing "Theo dõi anh à?"

                tam irritated "Tình cờ."

                hoang smile "Yuu-san. Bạn cũ của anh với anh Minh."

                hoang neutral "Cô ấy là đạo diễn khách mời của Festival. Anh ra sân bay đón."

                "Tâm nhìn về phía chiếc xe đã khuất."

                tam surprised "Yuuka Nakamura?"

                hoang neutral "Ừ. Em biết à?"

                tam neutral "Team em đang chuẩn bị hồ sơ cho Festival."

                hoang teasing "Thế thì sau này gặp nhớ đối xử tốt với người già."

                "Một giọng nữ ở phía xa lập tức vọng vào điện thoại."

                yuuka irritated "I heard that, Ha-kun."

                "Tâm bật cười."

                "Cảm giác khó chịu ban nãy rút xuống, không biến mất hoàn toàn nhưng đã có hình dạng hợp lý hơn."

                $ story_flag("tam_knows_yuuka_as_old_family_friend")
                $ story_flag("tam_learns_minh_hoang_are_brothers")

            "Tiếp tục đi đón Thiên An.":
                $ c08_yuuka_intro_source = "trusted_hoang"

                $ story_add("hoang_tam_trust", 10)
                $ story_add("tam_self_clarity", 5)
                $ story_sub("tam_insecurity", 5)
                $ story_flag("tam_chose_not_to_follow_hoang")

                "Tâm nhìn theo chiếc xe thêm một nhịp."

                "Rồi cúi xuống hoàn thành tin nhắn."

                tam neutral "Em sắp tới rồi."

                thienan neutral "Ừ. Chị đang chờ."

                "Tâm không hỏi Hoàng ngay."

                "Không phải vì cô không tò mò."

                "Mà vì lần đầu tiên, cô muốn cho sự tin tưởng một cơ hội đi trước trí tưởng tượng."

                "Tối đó, Hoàng chủ động nhắn."

                hoang neutral "Hôm nay anh ra sân bay đón một người bạn cũ của anh với anh Minh."

                hoang neutral "Cô ấy sang dự Festival. Khi nào tiện anh giới thiệu."

                tam teasing "Cô ấy đẹp."

                hoang teasing "Anh không phủ nhận sự thật khách quan."

                tam irritated "Anh giỏi."

                hoang grinning "Cảm ơn."

                $ story_flag("tam_knows_yuuka_as_old_family_friend")
                $ story_flag("tam_learns_minh_hoang_are_brothers")

    else:
        "Tâm nhìn chiếc xe đi xa."

        "Cô không có lý do để chạy theo."

        "Chỉ có một chút tò mò rất bình thường trước cảnh Hoàng xuất hiện cùng một người phụ nữ nổi bật đến mức ấy."

        if c08_huyen_hoang_active:
            $ c08_yuuka_intro_source = "huyen"

            "Tâm chụp được một tấm ảnh rất mờ của đuôi xe."

            "Cô gửi cho Huyền."

            tam neutral "Người yêu tin đồn của mày đi với gái đẹp."

            huyen neutral "Gì?"

            "Ba chấm hiện lên."

            "Biến mất."

            "Hiện lại."

            huyen surprised "À."

            tam teasing "À là sao?"

            huyen neutral "Yuu-san. Hoàng có kể hôm nay ra sân bay đón."

            tam neutral "Ai thế?"

            huyen teasing "Bạn cũ của Hoàng và anh Minh."

            huyen grinning "Đạo diễn khách mời của Festival nhà mày đấy."

            tam surprised "Yuuka Nakamura?"

            huyen neutral "Chắc thế."

            huyen teasing "Mày soi giúp tao xem ngoài đời có đẹp quá mức khai báo không."

            tam teasing "Tự soi."

            $ story_add("huyen_hoang_interest", 5)
            $ story_add("hoang_huyen_interest", 5)
            $ story_add("tam_observation", 5)
            $ story_flag("huyen_question_minh")
            $ story_flag("tam_knows_yuuka_as_old_family_friend")
            $ story_flag("tam_learns_minh_hoang_are_brothers")

        else:
            $ c08_yuuka_intro_source = "hoang"

            "Tâm gửi Hoàng một tin nhắn."

            tam teasing "Xe đẹp. Người ngồi bên cạnh còn đẹp hơn."

            "Hoàng trả lời gần như ngay lập tức."

            hoang teasing "Cảm ơn. Xe anh biết rồi."

            tam irritated "Em không khen anh."

            hoang neutral "Yuu-san. Bạn cũ của anh và anh Minh."

            hoang neutral "Cô ấy sang dự Festival. Anh ra sân bay đón."

            tam surprised "Yuuka Nakamura?"

            hoang neutral "Ừ. Em biết cô ấy à?"

            tam neutral "Team em vừa xem trailer phim."

            hoang teasing "Thế thì anh không cần quảng cáo thêm."

            "Tâm nhìn cái tên trong đoạn chat."

            "Một người đã xuất hiện trước bằng tác phẩm."

            "Sau đó mới có một gương mặt chưa kịp nhìn rõ qua cửa kính xe."

            $ story_add("tam_observation", 5)
            $ story_flag("tam_knows_yuuka_as_old_family_friend")
            $ story_flag("tam_learns_minh_hoang_are_brothers")

    $ story_flag("yuuka_arrived_eight_days_before_festival")

    return