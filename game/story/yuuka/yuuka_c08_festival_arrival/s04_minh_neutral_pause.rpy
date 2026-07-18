# FILE: game/story/yuuka/yuuka_c08_festival_arrival/s04_minh_neutral_pause.rpy
# Scene file.

label yuuka_c08_festival_arrival_s04_minh_neutral_pause:
    # -------------------------------------------------------------------------
    # Tâm followed Hoàng and is present for the reunion.
    # -------------------------------------------------------------------------

    if c08_tam_met_yuuka:
        scene bg_hoang_house_living_room_day
        with dissolve

        "Vali của Yuuka vẫn dựng cạnh sofa."

        "Chiếc áo khoác mỏng được gấp trên tay vịn ghế, nhưng chiếc khăn quàng lại nằm lệch trên bàn."

        "Một chi tiết nhỏ không hợp với vẻ chỉn chu của cô."

        "Tâm ngồi đối diện Yuuka."

        "Cơn bực ở sân bay đã lắng xuống đủ để cô nhìn người trước mặt rõ hơn."

        "Yuuka không giống một người vừa cố ý chen vào quan hệ của ai."

        "Cô nói chuyện dễ chịu, đôi khi hơi tinh nghịch, có lúc còn cố tình làm Hoàng khó xử."

        yuuka teasing "Ha-kun talked about you."

        tam flustered "Anh ấy kể gì ạ?"

        yuuka grinning "Enough."

        hoang irritated "Yuu-san."

        yuuka smile "Only good things."

        hoang neutral "Câu sau không cứu được câu trước đâu."

        "Tâm bật cười."

        "Không khí ở sân bay rút xuống thêm một chút."

        "Nhưng giữa những câu nói, Tâm nhận ra Yuuka thường liếc về phía cửa."

        "Không nhiều."

        "Chỉ khi có tiếng xe ngoài đường."

        "Hoặc lúc chìa khóa của ai đó va vào nhau ngoài cổng."

        "Hoàng mang thêm nước ra."

        hoang neutral "Anh Minh chắc sắp về."

        "Yuuka cầm cốc lên."

        "Không uống."

        yuuka neutral "I am not waiting."

        hoang teasing "Anh chưa nói em đang đợi."

        yuuka irritated "You implied it."

        hoang grinning "Em tự khai."

        "Yuuka nhìn cậu bằng vẻ mặt rất muốn đuổi người."

        "Đúng lúc ấy, tiếng khóa cửa vang lên."

        "Cốc nước trong tay cô dừng lại."

        "Hoàng quay đầu."

        "Tâm cũng nhìn ra cửa."

        "Minh bước vào."

        "Ánh mắt anh chạm Tâm trước."

        minh neutral "Tâm."

        tam neutral "Chào anh."

        "Sau đó anh nhìn sang sofa."

        "Yuuka đã đứng dậy."

        "Cả hai dừng lại."

        "Không lâu."

        "Chỉ một nhịp nhỏ đến mức nếu trong phòng có thêm tiếng nói, có lẽ chẳng ai nhận ra."

        "Nhưng căn phòng đang yên."

        "Và sự im lặng giữa họ không hề trống."

        minh neutral "..."

        yuuka neutral "..."

        "Yuuka bước về phía anh trước."

        "Minh giơ một tay lên, đặt nhẹ lên đầu cô, giữ cô lại ngoài tầm ôm."

        minh smile "Oh. Akuma-chan."

        minh neutral "Fancy meeting you here."

        "Yuuka nhìn bàn tay trên đầu mình."

        "Rồi nhìn anh."

        yuuka irritated "Put."

        yuuka irritated "Your hand."

        yuuka irritated "Away."

        "Minh buông tay."

        yuuka teasing "Let me hug you, Otou-chan."

        "Cô bước tới ôm anh."

        "Nhanh."

        "Tự nhiên."

        "Nhưng chặt hơn mức một câu đùa cần đến."

        "Minh khựng lại rất nhẹ."

        "Sau đó một tay anh đặt lên lưng cô."

        "Không kéo gần hơn."

        "Cũng không đẩy ra."

        minh neutral "Careful."

        minh teasing "You are acting like you missed me."

        yuuka neutral "Acting, yes."

        "Giọng cô bị vai áo anh chặn mất một phần."

        "Khi Yuuka buông ra, nụ cười đã trở lại trên mặt cô."

        "Sáng."

        "Tròn vai."

        "Chỉ có đầu ngón tay vẫn giữ nhẹ lấy tay áo anh thêm nửa giây."

        if c08_tam_high_clarity:
            "Điều đầu tiên Tâm cảm thấy là nhẹ nhõm."

            "Thẳng thắn mà nói, không đẹp đẽ lắm."

            "Nhưng rõ ràng."

            "Yuuka không đến đây vì Hoàng."

            "Và cách cô nhìn Minh cũng không cho phép ai hiểu nhầm điều đó."

        elif c08_tam_minh_lean:
            "Cảm giác ghen với Hoàng vừa lắng xuống, một điều khó gọi tên khác đã nổi lên."

            "Không mạnh."

            "Chỉ là Tâm chợt nhận ra mình chưa từng thấy Minh để một ai bước vào khoảng cách ấy."

        else:
            "Tâm hiểu vì sao Hoàng chỉ giới thiệu bằng hai chữ 'bạn cũ'."

            "Đó là cách gọi an toàn nhất cho một mối quan hệ rõ ràng không hề đơn giản."

        $ story_add("minh_yuuka_trust", 10)
        $ story_add("minh_yuuka_intimacy", 10)
        $ story_add("minh_yuuka_unresolved", 10)

        $ story_flag("yuuka_route_unlocked")
        $ story_flag("group_notices_minyuu_history")
        $ story_flag("minyuu_reunion_not_yet_defined")

        menu:
            "Điều gì khiến Tâm chú ý nhất?"

            "Nhịp dừng trước khi họ chào nhau.":
                $ story_add("tam_observation", 10)
                $ story_add("minh_yuuka_unresolved", 5)
                $ story_flag("noticed_minyuu_pause")

                "Một người bạn cũ có thể bất ngờ."

                "Nhưng sự im lặng vừa rồi không giống bất ngờ."

                "Nó giống hai người cùng chạm vào một cánh cửa đã đóng rất lâu, rồi đồng thời chưa biết ai nên mở trước."

            "Cái ôm không giống một cuộc tái ngộ xã giao.":
                $ story_add("tam_observation", 10)
                $ story_add("tam_respect_yuuka", 5)
                $ story_flag("noticed_minyuu_familiarity")

                if c08_tam_minh_lean:
                    $ story_add("tam_insecurity", 10)

                    "Tâm không cần biết quá khứ của họ là gì để hiểu một điều."

                    "Yuuka đã từng có một vị trí rất gần."

                    "Có thể vị trí ấy vẫn còn ở đó."

                else:
                    "Tâm nhìn cách Minh đặt tay sau lưng Yuuka."

                    "Một cử chỉ rất nhỏ."

                    "Nhưng nó có độ chính xác của một thói quen chưa mất."

            "Cách Yuuka chỉ mất vai diễn khi Minh bước vào.":
                $ story_add("tam_respect_yuuka", 10)
                $ story_add("tam_observation", 10)
                $ story_flag("tam_noticed_yuuka_emotional_control")

                "Ở cửa, Yuuka có thể cười trước một người lạ."

                "Trong phòng khách, cô có thể trêu Hoàng như không có gì đáng lo."

                "Nhưng khi Minh bước vào, cô đã quên cười đúng một giây."

                "Chỉ một giây ấy thôi cũng đủ thật hơn mọi câu đùa trước đó."

        "Minh đặt chìa khóa lên kệ."

        minh neutral "Em đã ăn gì chưa?"

        yuuka neutral "Airline food."

        minh neutral "Anh hỏi đồ ăn."

        yuuka irritated "That was supposed to be food."

        "Minh nhìn sang Hoàng."

        minh neutral "Trong tủ còn gì?"

        hoang neutral "Còn cá, rau với ít thịt."

        minh neutral "Anh nấu."

        "Yuuka quay mặt đi rất nhẹ."

        "Tâm vẫn nhìn thấy khóe môi cô cong lên."

        "Điện thoại Tâm rung."

        thienan irritated "Em định để chị mang cả vali của em về luôn à?"

        "Tâm nhìn màn hình."

        tam shocked "Chết rồi."

        hoang confused "Sao thế?"

        tam neutral "Chị An đang đợi em ở nhà. Mai bọn em còn đi đám cưới Duyên."

        "Minh đang cởi đồng hồ thì dừng lại."

        minh neutral "Duyên?"

        tam neutral "Vâng. Chị Duyên và anh Kim."

        "Một khoảng lặng khác xuất hiện."

        "Lần này, người khựng lại là Minh."

        "Rất ngắn."

        "Nhưng Yuuka đã nhìn thấy."

        "Cô không hỏi."

        "Hoàng cũng không."

        "Một sợi dây khác của quá khứ vừa được kéo ra, nhưng chưa đến lúc chạm vào."

        $ story_flag("minh_hears_duyen_wedding")
        $ story_flag("duyen_kim_wedding_seeded")

        tam neutral "Em xin phép về trước."

        yuuka smile "See you at the Festival."

        tam smile "Hẹn gặp chị."

        "Tâm đi ra cửa."

        "Lúc cánh cửa khép lại, cô nghe Yuuka hỏi rất nhỏ."

        yuuka neutral "Duyen?"

        "Và giọng Minh đáp lại, đều đến mức gần như không có gì."

        minh neutral "Chuyện cũ thôi."

    # -------------------------------------------------------------------------
    # Tâm did not follow. Reunion is shown from Yuuka's perspective.
    # -------------------------------------------------------------------------

    else:
        scene bg_hoang_house_living_room_day
        with dissolve

        "Căn nhà gần như không thay đổi."

        "Chiếc sofa cũ."

        "Bàn trà."

        "Khung cửa sổ nhìn ra sân."

        "Cả góc bếp vẫn nằm ở nơi Yuuka nhớ."

        "Mọi thứ gọn gàng đến mức có phần bất lịch sự với thời gian."

        "Hoàng mang nước ra rồi vào trong cất hành lý giúp cô."

        "Yuuka ngồi một mình."

        "Cô nhìn cốc nước."

        "Không uống."

        "Tiếng khóa cửa vang lên."

        "Bàn tay cô khép lại quanh thành cốc."

        "Minh bước vào."

        "Anh dừng lại khi nhìn thấy cô."

        "Yuuka đã chuẩn bị rất nhiều câu cho khoảnh khắc này."

        "Không câu nào chịu xuất hiện."

        minh neutral "..."

        yuuka neutral "..."

        "Minh đặt chìa khóa lên kệ."

        "Anh nhìn cô một lúc."

        minh neutral "Chuyến bay ổn chứ?"

        "Một câu rất bình thường."

        "Nhờ vậy Yuuka mới nhớ cách thở."

        menu:
            "Yuuka bước qua khoảng cách đầu tiên thế nào?"

            "Bám vào nhịp cũ và đòi một cái ôm.":
                $ c08_minyuu_greeting_mode = "old_joke"

                $ story_add("minh_yuuka_intimacy", 10)
                $ story_add("minh_yuuka_unresolved", 5)
                $ story_flag("yuuka_used_old_rhythm")

                "Yuuka bước về phía anh."

                "Minh đặt tay lên đầu cô, giữ lại."

                minh smile "Oh. Akuma-chan."

                minh neutral "Fancy meeting you here."

                yuuka irritated "Put your hand away."

                yuuka teasing "Let me hug you, Otou-chan."

                "Minh buông tay."

                "Yuuka ôm anh."

                "Chặt hơn dự tính."

                minh neutral "Careful."

                minh teasing "You are acting like you missed me."

                yuuka neutral "Acting, yes."

                "Không ai sửa lời nói dối ấy."

            "Chào anh như một người bạn lâu ngày gặp lại.":
                $ c08_minyuu_greeting_mode = "formal_friend"

                $ story_add("minh_yuuka_trust", 5)
                $ story_add("boundary_score", 5)
                $ story_flag("yuuka_kept_arrival_formal")

                yuuka smile "Long time no see, Minh."

                minh neutral "Ừ."

                minh neutral "Lâu rồi."

                "Câu trả lời không lạnh."

                "Cũng không gần."

                "Nó đặt giữa hai người một khoảng vừa đủ để không ai phải lùi thêm."

            "Nói điều thật nhất lúc này.":
                $ c08_minyuu_greeting_mode = "returned"

                $ story_add("minh_yuuka_trust", 10)
                $ story_add("minh_yuuka_intimacy", 5)
                $ story_add("minh_yuuka_unresolved", 5)
                $ story_flag("yuuka_said_she_returned")

                yuuka neutral "Em về rồi."

                "Minh nhìn cô."

                "Không hỏi cô đang gọi nơi nào là nơi để về."

                minh neutral "Ừ."

                minh neutral "Chào mừng em trở lại."

                "Yuuka cúi mắt xuống."

                "Mặt nước trong cốc rung rất nhẹ."

        $ story_add("minh_yuuka_trust", 10)
        $ story_add("minh_yuuka_intimacy", 10)
        $ story_add("minh_yuuka_unresolved", 10)

        $ story_flag("yuuka_route_unlocked")
        $ story_flag("minyuu_reunion_not_yet_defined")

        "Hoàng quay lại phòng khách."

        "Cậu nhìn Minh."

        "Rồi nhìn Yuuka."

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