# FILE: game/story/yuuka/yuuka_c08_festival_arrival/s03_hoang_introduces_yuuka.rpy
# Scene file.

label yuuka_c08_festival_arrival_s03_hoang_introduces_yuuka:
    scene bg_airport_arrival_day
    with fade

    centered "{size=34}Tám ngày trước Liên hoan phim{/size}"

    scene bg_airport_arrival_day
    with dissolve

    "Máy bay từ Nhật hạ cánh vào gần trưa."

    "Khi bước ra khỏi khu kiểm soát, Yuuka chậm lại một nhịp."

    "Không khí nơi này ấm hơn Tokyo."

    "Dày hơn."

    "Tiếng Việt vang giữa sảnh, tiếng bánh xe vali kéo trên nền gạch, mùi cà phê lẫn trong hơi điều hòa — tất cả đều quen theo một cách không nên còn quen nữa."

    "Hoàng đứng phía ngoài hàng rào đón khách."

    "Yuuka nhận ra cậu gần như ngay lập tức."

    hoang happy "Yuu-san."

    yuuka happy "Ha-kun."

    "Cô giơ tay lên, bước nhanh hơn."

    "Hoàng nhận lấy vali. Yuuka thuận thế khoác tay cậu, tự nhiên như thể bốn năm vừa rồi chỉ là một chuyến đi hơi dài."

    yuuka teasing "Still sweet as ever."

    yuuka grinning "Good. At least one brother remains lovable."

    hoang laughing "Vừa xuống máy bay đã gây chuyện rồi à?"

    yuuka smile "I had a long flight. I deserve entertainment."

    hoang smile "Welcome back to Vietnam."

    "Nụ cười trên môi Yuuka dừng lại rất khẽ."

    "Cô quay sang nhìn qua lớp cửa kính, như thể phía ngoài kia có thứ gì đáng chú ý hơn."

    yuuka neutral "Thank you."

    "Hoàng không hỏi."

    "Cậu chỉ kéo vali đi chậm lại để cô vẫn có thể khoác tay mình mà không phải bước vội."

    # -------------------------------------------------------------------------
    # Tâm's perspective.
    # -------------------------------------------------------------------------

    "Ở phía bên kia sảnh đến, Tâm đang đứng gần một cột chỉ dẫn."

    "Cô tới đón Thiên An sau chuyến công tác."

    "Mấy hôm sau, hai chị em còn phải đến dự đám cưới của Duyên và Kim — những người bạn học cũ của Thiên An."

    "Tâm vừa kiểm tra lại số hiệu chuyến bay thì nghe một giọng cười quen."

    "Cô ngẩng lên."

    "Hoàng."

    "Anh đang kéo một chiếc vali lớn."

    "Bên cạnh anh là một cô gái cao, nổi bật, mái tóc dài ánh nâu nhẹ dưới nắng từ cửa kính."

    "Cô ấy khoác tay Hoàng."

    "Không phải cái khoác tay xã giao ngập ngừng của hai người lâu ngày không gặp."

    "Nó thân thuộc đến mức Hoàng chẳng hề nhìn xuống."

    if c08_tam_hoang_active:
        "Tâm đứng yên."

        "Điện thoại đã nằm trong tay cô trước khi cô kịp quyết định mình muốn làm gì."

        "Cô gọi cho Hoàng."

        "Ở phía xa, tiếng chuông vang lên."

        "Hoàng đưa tay vào túi áo."

        "Anh nhìn màn hình."

        "Nụ cười trên môi chậm lại rất nhẹ."

        "Một hồi chuông."

        "Hai hồi."

        "Cuối cùng anh cũng nhận cuộc gọi."

        hoang neutral "A lô?"

        "Giọng nói vang trong điện thoại và từ phía bên kia sảnh gần như cùng lúc."

        "Đúng là anh."

        tam neutral "..."

        "Tâm ngắt máy."

        "Hoàng nhìn màn hình thêm một giây, rồi ngẩng lên quan sát dòng người."

        "Nhưng một nhóm khách vừa bước ra chắn giữa hai người."

        "Yuuka nói gì đó."

        "Cô lại kéo tay Hoàng đi."

        "Tâm nhìn theo cho đến khi hai bóng người khuất sau cửa ra."

    else:
        "Tâm chậm bước."

        "Cô không có lý do để khó chịu."

        "Nhưng cảnh tượng ấy vẫn đủ khiến cô tò mò."

        "Hoàng chưa bao giờ nhắc đến một cô gái nào thân thiết đến mức có thể khoác tay anh giữa sân bay như vậy."

    "Một bàn tay chạm nhẹ vào vai Tâm."

    thienan neutral "Tâm."

    tam surprised "Ơ?"

    thienan confused "Em đứng đây làm gì mà như mất hồn thế?"

    "Thiên An đứng phía sau cô với một chiếc vali nhỏ."

    "Áo khoác màu ngà phủ ngoài bộ đồ công sở, tóc búi gọn sau đầu. Chuyến bay vừa rồi dường như chỉ khiến chị mệt, không làm chị bớt chỉn chu."

    "Tâm nhận lấy chiếc vali."

    tam neutral "Không có gì. Mình về thôi chị."

    "Thiên An nhìn cô một giây."

    "Không hỏi ngay."

    # -------------------------------------------------------------------------
    # Existing Tâm–Hoàng route.
    # -------------------------------------------------------------------------

    if c08_tam_hoang_active:
        scene bg_taxi_interior_day
        with dissolve

        "Taxi rời sân bay."

        "Thiên An mở điện thoại xem lại tin nhắn công việc. Tâm ngồi bên cạnh, mắt vẫn nhìn qua cửa kính."

        "Cô biết nhà Hoàng ở đâu."

        "Cũng biết anh sống cùng Minh."

        "Điều duy nhất cô không biết là người phụ nữ vừa khoác tay anh là ai."

        menu:
            "Tâm làm gì?"

            "Ghé qua nhà Hoàng trước.":
                $ c08_tam_followed_hoang = True
                $ c08_yuuka_intro_source = "house"

                $ story_add("tam_observation", 5)
                $ story_add("tam_insecurity", 10)
                $ story_sub("hoang_tam_trust", 5)

                $ story_flag("tam_followed_hoang_home")
                $ story_flag("tam_delayed_thienan_trip")

                tam neutral "Chú lái xe, cho cháu ghé qua một chỗ trước được không ạ?"

                thienan confused "Đi đâu vậy em?"

                tam neutral "Em cần gặp Hoàng một chút."

                "Thiên An khóa màn hình."

                thienan neutral "Có chuyện gì?"

                tam irritated "Em chưa biết."

                thienan neutral "Em vừa nói một câu rất đáng lo."

                tam neutral "Em chỉ muốn hỏi cho rõ thôi."

                "Tâm đọc địa chỉ cho tài xế."

                "Thiên An không hỏi thêm. Nhưng khi chiếc taxi rẽ vào con phố yên tĩnh, chị bắt đầu nhìn ra ngoài lâu hơn."

                "Đến lúc xe dừng trước cổng, Thiên An khựng lại."

                thienan surprised "Là nhà này sao?"

                tam confused "Chị biết chỗ này à?"

                "Thiên An nhìn cánh cổng."

                "Màu sơn đã khác đôi chút. Cây trong sân cũng cao hơn trước."

                "Nhưng chị vẫn nhận ra."

                thienan neutral "Đây là nhà Minh."

                tam neutral "Vâng."

                tam neutral "Anh Hoàng là em trai anh ấy. Hai người đang ở cùng nhau."

                "Thiên An quay sang nhìn Tâm."

                "Trong ánh mắt chị có một khoảnh khắc hiếm hoi hoàn toàn không che giấu được sự sửng sốt."

                thienan confused "Bạn trai em là em trai Minh?"

                tam neutral "Em tưởng em đã kể rồi."

                thienan neutral "Em chỉ nói tên anh ta là Hoàng."

                tam neutral "..."

                thienan irritated "Một thông tin hơi thiếu cấu trúc."

                "Tâm mở cửa xe."

                tam neutral "Chị cứ về trước nhé. Chìa khóa của em đây."

                thienan neutral "Tâm."

                "Tâm dừng lại."

                thienan neutral "Hỏi cho rõ. Đừng tự viết phần còn lại trong đầu rồi giận thay cho sự thật."

                tam neutral "Em biết."

                "Cô đóng cửa xe."

                "Chiếc taxi bắt đầu lăn bánh."

                "Thiên An nhìn qua cửa kính, thấy Tâm đẩy cổng bước vào."

                "Chị tựa lưng vào ghế."

                thienan melancholic "Oan gia ngõ hẹp."

                $ story_flag("thienan_discovers_hoang_is_minhs_brother")
                $ story_flag("thienan_recognizes_minh_house")
                $ story_flag("thienan_oa_gia_ngo_hep")

                scene bg_hoang_house_front_door_day
                with dissolve

                "Xe Hoàng đã nằm trong gara."

                "Tâm đi thẳng đến cửa."

                "Lúc ở sân bay, cô đã nghĩ ra khá nhiều câu để hỏi."

                "Đến khi bấm chuông, chúng lại chen nhau đến mức không câu nào còn rõ."

                "Có tiếng bước chân bên trong."

                "Cánh cửa mở ra."

                "Người đứng sau cửa không phải Hoàng."

                "Là cô gái ở sân bay."

                "Nhìn gần, Tâm mới hiểu vì sao chỉ một bóng nghiêng cũng đủ khiến người khác chú ý."

                "Gương mặt cô mềm và sáng. Mái tóc dài phủ qua vai. Không cần trang điểm cầu kỳ, từng đường nét vẫn rõ đến mức có phần thiếu công bằng."

                "Cô đang cười khi mở cửa."

                "Nhưng lúc nhận ra người ngoài cửa không phải người mình chờ, nụ cười ấy khựng lại rất nhẹ."

                yuuka smile "Hi."

                tam shocked "..."

                "Hai người nhìn nhau."

                "Tâm nghĩ đến bàn tay cô đang khoác trên tay Hoàng."

                "Yuuka nhìn một cô gái trẻ biết chính xác phải tìm đến căn nhà này."

                "Mỗi người đều vừa dựng lên một giả thuyết không mấy dễ chịu."

                yuuka neutral "Are you looking for someone?"

                tam flustered "Tôi..."

                "Từ trong nhà, giọng Hoàng vọng ra."

                hoang neutral "Ai đấy, Yuu-san? Không phải anh Minh à?"

                "Ánh mắt Yuuka đổi nhẹ."

                "Không phải anh Minh."

                "Vậy cô gái này rất có thể không đến tìm Minh."

                "Tâm cũng nghe rõ cách Hoàng gọi người trước mặt."

                "Yuu-san."

                "Không giống cách một người đàn ông gọi cô gái đang giấu bạn gái mình."

                "Ít nhất là không hoàn toàn."

                Yuuka teasing "No."

                yuuka grinning "Just a strange lady. She keeps staring at me."

                tam irritated "Tôi không—"

                "Hoàng bước ra."

                "Khi nhìn thấy Tâm, anh dừng hẳn lại."

                hoang shocked "Tâm?"

                tam irritated "Em cũng đang định hỏi anh đây."

                "Hoàng nhìn khuôn mặt cô."

                "Rồi nhìn Yuuka."

                "Mọi thứ nối lại trong đầu anh nhanh đến mức đáng ghét."

                hoang neutral "À."

                hoang smile "Yuu-san, đây là Tâm."

                hoang neutral "Bạn gái anh."

                "Sự cảnh giác trong mắt Yuuka biến mất gần như ngay lập tức."

                yuuka surprised "Oh."

                yuuka smile "So you are Tâm."

                tam confused "Chị biết em?"

                yuuka teasing "Ha-kun is not very subtle."

                hoang irritated "Anh chỉ kể chuyện bình thường."

                yuuka grinning "Repeatedly."

                tam flustered "..."

                hoang neutral "Tâm, đây là Yuuka."

                hoang neutral "Bạn cũ của anh và anh Minh."

                "Tâm không bất ngờ vì mối liên hệ với Minh."

                "Cô đã biết hai anh em từ chương trước."

                "Điều khiến cô khựng lại là cái tên."

                tam surprised "Yuuka Nakamura?"

                yuuka surprised "You know me?"

                tam neutral "Công ty em đang tham gia phần vận hành Liên hoan phim."

                tam neutral "Team em vừa xem trailer phim của chị."

                if c08_tam_leads_festival:
                    tam neutral "Em phụ trách nhóm điều phối hồ sơ và lịch khách mời."

                    yuuka smile "Then I should be very careful around you."

                else:
                    tam neutral "Em đang hỗ trợ hồ sơ và lịch khách mời."

                    yuuka smile "Then we will probably meet again."

                "Hoàng chống một tay lên khung cửa."

                hoang teasing "Hai người định đứng đây tổ chức buổi giao lưu trước Festival à?"

                "Yuuka lánh sang bên."

                yuuka smile "Come in."

                $ c08_tam_met_yuuka = True

                $ story_add("tam_respect_yuuka", 10)
                $ story_add("tam_observation", 5)

                if c08_tam_high_clarity:
                    $ story_sub("tam_insecurity", 5)
                    $ story_add("hoang_tam_trust", 5)
                    $ story_flag("tam_c08_airport_misunderstanding_cleared")
                else:
                    $ story_add("tam_insecurity", 5)
                    $ story_flag("tam_c08_yuuka_first_impression_unsettled")

                $ story_flag("tam_met_yuuka_at_hoang_house")

            "Gọi lại và hỏi Hoàng ngay.":
                $ c08_tam_followed_hoang = False
                $ c08_yuuka_intro_source = "hoang_phone"

                $ story_add("hoang_tam_trust", 10)
                $ story_add("tam_self_clarity", 10)
                $ story_sub("tam_insecurity", 5)

                $ story_flag("tam_asked_hoang_about_yuuka_directly")

                "Tâm gọi lại."

                "Lần này Hoàng nhận máy gần như ngay lập tức."

                hoang neutral "Tâm?"

                tam neutral "Anh vừa ở sân bay đúng không?"

                "Hoàng im một nhịp."

                hoang neutral "Ừ."

                tam teasing "Cô gái đẹp khoác tay anh là ai thế?"

                hoang teasing "Câu hỏi có vẻ rất bình tĩnh."

                tam irritated "Anh trả lời đi."

                hoang smile "Yuu-san. Bạn cũ của anh với anh Minh."

                hoang neutral "Cô ấy là đạo diễn khách mời của Festival. Anh ra đón."

                tam surprised "Yuuka Nakamura?"

                hoang neutral "Em biết à?"

                tam neutral "Team em đang chuẩn bị phần vận hành."

                "Một giọng nữ vọng vào từ phía bên kia."

                yuuka teasing "Is that your girlfriend?"

                hoang neutral "Ừ."

                yuuka grinning "Tell her you are innocent. Mostly."

                tam irritated "Em nghe thấy đấy."

                hoang laughing "Thế thì anh đỡ phải dịch."

                "Tâm nhìn ra cửa kính."

                "Cục nghẹn trong lòng rút xuống, để lại một chút ngượng không mấy dễ chịu."

                $ story_flag("tam_knows_yuuka_as_old_family_friend")

            "Không đuổi theo. Đợi Hoàng tự giải thích.":
                $ c08_tam_followed_hoang = False
                $ c08_yuuka_intro_source = "trusted_hoang"

                $ story_add("hoang_tam_trust", 10)
                $ story_add("tam_self_clarity", 5)
                $ story_sub("tam_insecurity", 5)

                $ story_flag("tam_chose_not_to_follow_hoang")

                "Tâm đặt điện thoại úp xuống đùi."

                "Cô vẫn khó chịu."

                "Nhưng khó chịu không có nghĩa là phải lập tức kết tội một người."

                thienan neutral "Không định hỏi à?"

                tam neutral "Có."

                tam neutral "Nhưng không phải lúc này."

                "Thiên An nhìn cô, rồi khẽ gật."

                "Tối hôm ấy, Hoàng chủ động nhắn."

                hoang neutral "Hôm nay anh ra sân bay đón Yuu-san."

                hoang neutral "Bạn cũ của anh với anh Minh. Cô ấy sang dự Festival."

                tam teasing "Em thấy rồi."

                hoang surprised "Thấy?"

                tam neutral "Cả đoạn khoác tay."

                hoang neutral "..."

                tam teasing "Giải thích đi."

                hoang teasing "Anh đang cân nhắc thuê luật sư."

                "Tâm bật cười dù không định."

                $ story_flag("tam_knows_yuuka_as_old_family_friend")

    # -------------------------------------------------------------------------
    # No active Tâm–Hoàng route.
    # -------------------------------------------------------------------------

    else:
        scene bg_taxi_interior_day
        with dissolve

        "Taxi rời sân bay."

        "Tâm vẫn nhớ cảnh Hoàng kéo vali cho cô gái kia."

        "Không phải vì ghen."

        "Chỉ vì sự thân thuộc giữa họ quá rõ để xem như một cuộc gặp xã giao."

        if c08_huyen_hoang_active:
            $ c08_yuuka_intro_source = "huyen"

            "Tâm gửi Huyền một tin nhắn."

            tam teasing "Người yêu tin đồn của mày vừa đón một cô gái rất đẹp ở sân bay."

            huyen neutral "Cô gái Nhật?"

            tam surprised "Mày biết?"

            huyen neutral "Hoàng có kể."

            huyen teasing "Bạn cũ của hai anh em."

            tam neutral "Tên gì?"

            huyen neutral "Yuuka."

            "Tâm nhìn lại tài liệu Festival trong điện thoại."

            tam surprised "Yuuka Nakamura?"

            huyen neutral "Chắc thế."

            huyen teasing "Mày gặp ngoài đời rồi thì báo cáo giúp tao xem ảnh có khai gian không."

            tam teasing "Tự đi mà hỏi."

            $ story_add("tam_observation", 5)
            $ story_add("huyen_hoang_interest", 5)
            $ story_flag("tam_knows_yuuka_as_old_family_friend")

        else:
            $ c08_yuuka_intro_source = "hoang"

            "Tâm gửi Hoàng một tin nhắn."

            tam teasing "Vừa thấy anh ở sân bay."

            hoang neutral "Thế à?"

            tam teasing "Xe đẹp. Cô gái đi cùng còn đẹp hơn."

            hoang teasing "Anh sẽ chuyển lời khen."

            tam irritated "Ai thế?"

            hoang neutral "Yuu-san. Bạn cũ của anh với anh Minh."

            hoang neutral "Cô ấy sang dự Festival."

            tam surprised "Yuuka Nakamura?"

            hoang neutral "Ừ. Team em phụ trách cô ấy à?"

            tam neutral "Một phần hồ sơ."

            hoang teasing "Thế thì nhớ đối xử tử tế với người nhà."

            tam irritated "Bạn cũ mà thành người nhà nhanh thế?"

            hoang grinning "Bạn rất cũ."

            $ story_add("tam_observation", 5)
            $ story_flag("tam_knows_yuuka_as_old_family_friend")

    $ story_flag("yuuka_arrived_eight_days_before_festival")

    return
