# FILE: game/story/tam/tam_c05_sunday_date/s03_intimacy_choice.rpy
# Route-specific intimacy payoff:
# - Tâm: topaz earrings / gift repair
# - Huyền: pocket photo printer and album
# - Group: three copies of one shared photograph

label tam_c05_sunday_date_s03_intimacy_choice:
    $ _anniversary_route = story_state.get("hoang_anniversary_route", "friend_group")

    if _anniversary_route == "tam":
        call tam_c05_sunday_date_s03_tam_gift

    elif _anniversary_route == "huyen":
        call tam_c05_sunday_date_s03_huyen_gift

    else:
        call tam_c05_sunday_date_s03_group_gift

    return


label tam_c05_sunday_date_s03_tam_gift:
    scene black
    with fade

    "Buổi chiều, công viên bớt đông."

    "Hoàng và Tâm vẫn ngồi trên chiếc ghế cũ."

    "Túi bánh đã trống."

    "Cốc giấy chỉ còn một lớp nước mỏng dưới đáy."

    "Hoàng đưa tay vào túi áo."

    "Động tác ấy đủ chậm để Tâm nhận ra trước khi chiếc hộp xuất hiện."

    tam confused "Gì thế?"

    hoang neutral "Cho em."

    tam "Em biết là cho em."

    tam teasing "Ý em là dịp gì?"

    hoang "Một năm."

    tam "Một năm quen nhau?"

    hoang "Ừ."

    tam "Không phải một năm yêu nhau à?"

    "Hoàng nhìn cô."

    "Câu hỏi giống hệt câu Minh từng hỏi cậu."

    hoang neutral "Ngày đó chưa tới."

    tam smile "Thế thì tiện thể tính trước."

    if story_has_flag("hoang_gift_tam_topaz_earrings"):
        "Tâm mở hộp."

        "Bên trong là một đôi bông tai nhỏ."

        "Viên hoàng ngọc màu vàng nhạt, được giữ bằng phần viền trắng rất mảnh."

        "Không quá sáng."

        "Không quá lớn."

        "Là kiểu cô có thể đeo đi làm mà không phải nghĩ xem nó có hợp với ngày hôm đó không."

        "Tâm im vài giây."

        hoang neutral "Không thích à?"

        tam "Không."

        "Hoàng hơi khựng."

        tam smile "Ý em là không phải không thích."

        hoang irritated "Em có thể chọn cách trả lời ít nguy hiểm hơn không?"

        "Tâm chạm nhẹ vào viên đá."

        tam neutral "Anh nhớ à?"

        hoang "Em đứng trước cửa kính gần mười giây."

        tam "Sáu giây."

        hoang "Em đếm à?"

        tam "Không."

        "Cả hai đều bỏ qua sự vô lý rất rõ trong câu trả lời ấy."

        menu:
            "Tâm..."

            "Đeo ngay":
                "Tâm tháo đôi bông tai đang đeo."

                "Cô cài đôi mới trước màn hình điện thoại."

                "Chiếc bên phải hơi lệch."

                "Hoàng đưa tay lên."

                "Rồi dừng lại trước khi chạm."

                hoang neutral "Lệch."

                tam "Anh sửa đi."

                "Hoàng chỉnh nhẹ phần khóa."

                "Đầu ngón tay chạm vào vành tai cô chưa đến một giây."

                "Tâm vẫn thấy rõ."

                tam teasing "Khóa nhỏ à?"

                hoang "Ừ."

                "Cô nhìn anh qua màn hình điện thoại."

                tam "Vâng. Tại khóa."

                $ story_add("hoang_tam_trust", 10)
                $ story_add("tam_hoang_interest", 5)
                $ story_flag("tam_wears_anniversary_earrings")

            "Nhờ Hoàng giúp cài":
                "Tâm đưa một chiếc bông tai cho Hoàng."

                tam neutral "Anh giúp em."

                hoang confused "Ở đây?"

                tam "Không thì em đưa anh làm gì?"

                "Hoàng nhận lấy."

                "Tâm vén tóc sang một bên."

                "Khoảng cách giữa hai người thu lại rất chậm."

                if story_state.get("hoang_self_acceptance", 0) >= 55:
                    "Tay Hoàng giữ rất chắc."

                    "Chỉ đến lúc phần khóa khép lại, đầu ngón tay cậu mới chạm nhẹ vào da cô."

                    tam teasing "Anh run à?"

                    hoang "Khóa nhỏ."

                    tam "Em vừa nghe câu này đâu đó."

                    hoang "Em tự cài chiếc còn lại đi."

                    "Tâm bật cười."

                    "Cô không lùi ngay."

                    $ story_add("hoang_tam_trust", 10)
                    $ story_add("tam_self_clarity", 5)
                    $ story_flag("hoang_fastens_tam_earring")

                else:
                    "Hoàng làm rơi phần khóa xuống lòng bàn tay."

                    "Cậu giữ lại được trước khi nó rơi hẳn."

                    tam smile "Từ từ thôi."

                    hoang neutral "Anh biết."

                    tam "Anh nói câu đó khi chưa biết."

                    "Tâm giữ cổ tay cậu một nhịp."

                    "Lần thứ hai, phần khóa vào đúng chỗ."

                    $ story_add("hoang_self_acceptance", 5)
                    $ story_add("hoang_insecurity", -5)
                    $ story_flag("hoang_hesitates_but_fastens_tam_earring")

            "Cất lại để dùng vào một ngày khác":
                "Tâm khép hộp."

                "Cô giữ nó trong hai tay."

                hoang neutral "Em không đeo à?"

                tam "Có."

                tam "Nhưng không phải hôm nay."

                "Hoàng nhìn chiếc hộp."

                tam smile "Em muốn lần đầu đeo là một ngày bình thường."

                tam "Để xem anh có nhận ra không."

                hoang "Anh sẽ nhận ra."

                tam "Tự tin thế?"

                hoang "Em vừa báo trước."

                "Tâm bật cười rồi cất hộp vào ngăn nhỏ trong túi."

                "Không giấu sâu."

                $ story_add("tam_self_clarity", 5)
                $ story_add("hoang_tam_trust", 5)
                $ story_flag("tam_saves_anniversary_earrings_for_ordinary_day")

    elif story_has_flag("hoang_gift_tam_expensive_topaz"):
        "Tâm mở hộp."

        "Viên đá bên trong sáng hơn cô dự kiến."

        "Đẹp."

        "Rất đẹp."

        "Cũng lớn hơn mọi món trang sức cô thường đeo."

        "Nụ cười của Tâm chậm lại."

        tam neutral "Đẹp lắm."

        "Hoàng nhìn cô."

        "Cậu biết đó chưa phải câu trả lời."

        hoang neutral "Nhưng?"

        tam "Em không biết có nên nhận không."

        hoang "Chỉ là quà thôi."

        "Câu nói ra hơi nhanh."

        "Tâm khép hộp lại."

        menu:
            "Tâm..."

            "Nói thật rằng món quà quá lớn":
                tam neutral "Không chỉ là quà."

                tam "Ít nhất với em thì không."

                hoang "Anh không muốn em nghĩ nhiều."

                tam "Thế anh mua thứ khiến em phải nghĩ nhiều làm gì?"

                "Hoàng nhìn chiếc hộp."

                "Cậu thở ra."

                hoang neutral "Anh hơi làm quá."

                tam "Hơi thôi à?"

                hoang "Khá nhiều."

                "Tâm đẩy hộp lại về phía cậu."

                tam smile "Mình đổi cùng nhau."

                hoang "Em vẫn nhận à?"

                tam "Em nhận việc anh nhớ."

                tam "Còn viên đá thì chọn lại."

                $ story_add("hoang_self_acceptance", 10)
                $ story_add("hoang_insecurity", -10)
                $ story_add("hoang_tam_trust", 5)
                $ story_flag("tam_expensive_gift_repaired_together")

            "Nhận để Hoàng không mất vui":
                "Tâm giữ hộp trong tay."

                tam smile "Em thích."

                "Nụ cười đủ đẹp."

                "Không đủ tự nhiên."

                "Hoàng nhìn thấy."

                "Cậu không hỏi."

                "Tâm cất hộp vào túi."

                "Nó nằm nặng hơn kích thước thật."

                $ story_add("tam_insecurity", 5)
                $ story_add("hoang_insecurity", 5)
                $ story_flag("tam_accepts_expensive_gift_uneasily")

            "Từ chối nhưng giữ ngày hôm nay":
                "Tâm đặt hộp lại vào tay Hoàng."

                tam neutral "Em không nhận món này."

                "Hoàng không khép tay lại."

                tam "Nhưng không có nghĩa em không thích hôm nay."

                hoang "Anh hiểu."

                tam "Anh đang nói khi chưa hiểu."

                "Hoàng nhìn cô."

                "Sau một lúc, cậu gật."

                hoang neutral "Ừ. Anh sẽ nghĩ lại."

                "Tâm đặt tay lên chiếc hộp, đẩy nhẹ về phía cậu."

                tam "Mình vẫn đi ăn tối."

                hoang "Ừ."

                $ story_add("tam_self_clarity", 5)
                $ story_add("hoang_self_acceptance", 5)
                $ story_flag("tam_refuses_gift_without_rejecting_hoang")

    else:
        "Hoàng không lấy ra một chiếc hộp."

        "Cậu lấy ra một tấm vé gấp đôi."

        "Là hóa đơn bữa sáng."

        "Mặt sau có vài dòng viết tay."

        tam confused "Đây là gì?"

        hoang "Bản nháp."

        tam "Bản nháp gì?"

        hoang "Anh chưa chọn được món quà đủ đúng."

        hoang "Nên hôm nay là bản nháp."

        "Tâm lật tờ giấy."

        "Mặt sau chỉ ghi ngày hôm nay và một dòng ngắn:"

        "Lần đầu anh chủ động."

        "Tâm đọc xong, gấp lại."

        menu:
            "Tâm..."

            "Bảo rằng bản nháp cũng được":
                tam smile "Cũng được."

                hoang "Gì?"

                tam "Bản nháp."

                tam "Nhưng lần sau nhớ sửa lỗi chính tả."

                hoang confused "Anh viết sai à?"

                tam "Không."

                tam "Em đang để anh có lý do đưa bản sau."

                "Hoàng nhìn cô."

                "Rồi cười."

                $ story_add("hoang_tam_trust", 5)
                $ story_add("hoang_self_acceptance", 5)
                $ story_flag("tam_accepts_anniversary_draft")

            "Đề nghị lần sau chọn cùng nhau":
                tam neutral "Lần sau mình chọn cùng."

                hoang "Thế còn là quà à?"

                tam "Anh trả tiền."

                hoang "Rõ rồi."

                "Tâm gấp tờ giấy cẩn thận rồi cất vào ví."

                $ story_add("tam_self_clarity", 5)
                $ story_flag("tam_and_hoang_will_choose_gift_together")

            "Trêu anh nợ một món":
                tam teasing "Vậy anh đang nợ em."

                hoang "Anh biết."

                tam "Có lãi."

                hoang "Bao nhiêu?"

                tam "Tùy thái độ."

                "Hoàng dựa lưng vào ghế."

                hoang smile "Nguy hiểm thật."

                $ story_add("tam_hoang_interest", 5)
                $ story_flag("tam_teases_hoang_about_future_gift")

    return


label tam_c05_sunday_date_s03_huyen_gift:
    scene black
    with fade

    "Buổi chiều, mưa đã tạnh."

    "Hoàng và Huyền ngồi ở một quán có cửa kính nhìn ra phố."

    "Trên bàn là một chiếc hộp chữ nhật bọc giấy đơn giản."

    "Huyền nhìn nó."

    "Rồi nhìn Hoàng."

    huyen teasing "Anh đừng bảo trong đó là báo cáo tổng kết một năm nhé."

    hoang "Không."

    huyen "Thế mở được không?"

    hoang "Anh đưa em để ngắm à?"

    "Huyền mở giấy bọc."

    "Bên trong là một máy in ảnh bỏ túi và một cuốn album nhỏ."

    huyen surprised "Anh nghĩ tôi chụp chưa đủ nhiều à?"

    hoang neutral "Anh nghĩ em nên có nhiều ảnh của mình hơn."

    "Huyền cầm cuốn album."

    "Nụ cười trên môi cô nhỏ đi."

    if story_has_flag("hoang_includes_first_huyen_photo") or story_has_flag("hoang_openly_centers_huyen"):
        "Trang đầu tiên có một tấm ảnh."

        "Huyền đứng dưới mái hiên, tóc bị gió thổi rối, tay cầm một túi đồ ăn."

        "Cô không nhìn vào máy."

        "Cô đang cười với người ngoài khung hình."

        "Người đó là Hoàng."

        huyen neutral "Anh giữ tấm này à?"

        hoang "Em chụp bằng máy anh."

        huyen "Không có nghĩa anh được giữ."

        hoang "Giờ em có bản rồi."

        "Dưới ảnh không có lời nhắn."

        "Chỉ có ngày."

        menu:
            "Huyền..."

            "Viết tên Hoàng dưới ngày":
                "Huyền lấy cây bút đặt cạnh quầy."

                "Cô viết thêm một chữ nhỏ dưới ngày."

                "Hoàng."

                "Cậu nhìn."

                hoang confused "Để làm gì?"

                huyen "Ghi nguồn ảnh."

                hoang "Anh đâu chụp."

                huyen "Nguồn gây cười."

                "Huyền khép album lại trước khi Hoàng kịp nói thêm."

                $ story_add("huyen_hoang_interest", 10)
                $ story_add("hoang_self_acceptance", 5)
                $ story_flag("huyen_places_hoang_in_album")

            "Chụp một tấm mới có cả hai":
                "Huyền lấy điện thoại, mở camera trước."

                huyen "Lại đây."

                hoang "Làm gì?"

                huyen "Anh mua máy mà đứng xa thế à?"

                "Hoàng dịch ghế lại."

                "Huyền giơ điện thoại."

                "Tấm đầu tiên bị rung vì cô bật cười đúng lúc chụp."

                hoang "Chụp lại."

                huyen "Không."

                "Cô gửi ảnh sang máy in."

                "Tờ ảnh nhỏ trượt ra."

                "Huyền đặt nó vào trang thứ hai."

                "Không xóa tấm đầu."

                $ story_add("huyen_hoang_interest", 5)
                $ story_add("hoang_huyen_interest", 5)
                $ story_flag("hoang_huyen_first_deliberate_photo")

            "Trêu rồi cất album đi":
                huyen teasing "Món này nguy hiểm đấy."

                hoang "Vì sao?"

                huyen "Tôi sẽ in hết ảnh xấu của anh."

                hoang "Anh có thể lấy lại."

                "Huyền ôm chiếc hộp sát hơn."

                huyen "Đã tặng rồi."

                hoang "Ừ."

                "Cô cất nó vào túi."

                "Rất nhanh."

                "Như thể sợ cậu đổi ý thật."

                $ story_add("huyen_hoang_interest", 5)
                $ story_flag("huyen_accepts_gift_behind_joke")

    elif story_has_flag("hoang_hides_huyen_gift_meaning"):
        "Trang đầu là ảnh ba người ở buổi tiệc công ty."

        "An toàn."

        "Vui."

        "Không ai phải hiểu thêm điều gì."

        "Huyền nhìn nó khá lâu."

        huyen neutral "An toàn ghê."

        hoang "Ảnh đầu tiên của bọn mình."

        huyen "Ừ."

        huyen "Của bọn mình."

        "Hai chữ ấy có thể là ba người."

        "Cũng có thể là hai."

        "Không ai hỏi."

        menu:
            "Hoàng..."

            "Nói rõ món quà là cho riêng Huyền":
                hoang neutral "Nhưng máy là cho em."

                "Huyền ngẩng lên."

                hoang "Không phải quà chung."

                huyen "Tôi biết."

                hoang "Em vừa nói như không biết."

                huyen "Tôi muốn nghe anh nói."

                "Hoàng im một nhịp."

                huyen smile "Giờ nghe rồi."

                $ story_add("hoang_self_acceptance", 5)
                $ story_add("huyen_hoang_interest", 5)
                $ story_flag("hoang_clarifies_huyen_is_not_group_gift")

            "Để nghĩa của ảnh ở trạng thái mở":
                hoang "Cô không thích à?"

                huyen "Thích."

                huyen "Ảnh đẹp."

                "Cô khép album."

                "Câu trả lời thật."

                "Chỉ chưa đầy đủ."

                $ story_flag("hoang_huyen_gift_remains_safe")
                $ story_add("hoang_insecurity", 5)

            "Đề nghị chụp thêm một tấm hai người":
                hoang "Mình chụp thêm."

                huyen surprised "Hai người?"

                hoang "Ở đây còn ai?"

                "Huyền nhìn quanh rất khoa trương."

                huyen "Đúng là không có Tâm."

                "Cô kéo ghế lại."

                $ story_add("hoang_huyen_interest", 5)
                $ story_add("huyen_hoang_interest", 5)
                $ story_flag("hoang_corrects_safe_album_with_couple_photo")

    elif story_has_flag("hoang_leaves_huyen_album_blank"):
        "Album trống."

        "Trang đầu sạch đến mức gần như phản chiếu ánh đèn."

        huyen neutral "Không có ảnh à?"

        hoang "Để em tự chọn."

        huyen "Hay anh không biết nên chọn tấm nào?"

        "Hoàng nhìn cuốn album."

        menu:
            "Hoàng trả lời..."

            "“Anh sợ chọn sai.”":
                hoang "Anh sợ chọn sai."

                "Huyền không cười."

                "Cô mở thư mục ảnh."

                "Lướt qua vài tấm."

                "Rồi chọn tấm Hoàng vừa chụp cô dưới mái hiên sáng nay."

                huyen "Vậy bắt đầu bằng tấm này."

                hoang "Em bảo xấu."

                huyen "Tôi đổi ý."

                $ story_add("hoang_self_acceptance", 5)
                $ story_add("huyen_hoang_interest", 5)
                $ story_flag("huyen_fills_blank_album_after_honesty")

            "“Tấm nào cũng như nhau.”":
                hoang "Tấm nào cũng như nhau."

                "Huyền khép album hơi nhanh."

                huyen smile "Ừ. Thế để tôi tự chọn."

                "Nụ cười vẫn ở đó."

                "Chỉ không còn chạm tới mắt."

                $ story_add("hoang_insecurity", 10)
                $ story_flag("hoang_hurts_huyen_with_indifference")

            "“Anh muốn ảnh đầu tiên là hôm nay.”":
                hoang "Anh muốn ảnh đầu tiên là hôm nay."

                "Huyền nhìn cậu."

                huyen "Sao không nói từ đầu?"

                hoang "Giờ nói rồi."

                "Cô lấy điện thoại."

                huyen "Lại đây."

                $ story_add("hoang_self_acceptance", 5)
                $ story_add("huyen_hoang_interest", 5)
                $ story_flag("hoang_huyen_start_album_today")

    else:
        "Huyền mở hộp."

        "Bên trong vẫn là máy in ảnh."

        "Không có album."

        "Không có tấm ảnh đầu tiên."

        "Có vẻ đơn hàng đã đến thiếu một phần."

        huyen "Anh kiểm tra hàng chưa?"

        hoang "Rồi."

        huyen "Thế album đâu?"

        hoang "Anh chưa chọn."

        "Huyền nhìn cậu một lúc."

        huyen "Được."

        "Cô cầm máy lên."

        huyen "Vậy hôm nay mua cùng."

        "Hoàng gật."

        $ story_add("hoang_self_acceptance", 5)
        $ story_flag("hoang_huyen_choose_album_together")

    return


label tam_c05_sunday_date_s03_group_gift:
    scene black
    with fade

    "Trước khi rời công viên, Hoàng lấy từ túi ra ba phong bì mỏng."

    huyen confused "Cái gì thế?"

    hoang "Quà."

    huyen "Ba cái giống nhau à?"

    hoang "Ừ."

    huyen "Quà công ty."

    "Hoàng nhìn cô."

    "Câu đó nghe quen một cách đáng ngờ."

    tam smile "Mở đi."

    "Mỗi phong bì có một tấm ảnh."

    "Ảnh ba người ở buổi tiệc công ty."

    "Tâm nhìn sai hướng."

    "Huyền cười quá lớn."

    "Hoàng chưa biết đặt tay ở đâu."

    huyen laughing "Ai chọn tấm này thế?"

    hoang "Anh."

    huyen "Thù gì nhau à?"

    tam neutral "Em thích."

    "Tâm lật mặt sau."

    "Trống."

    huyen "Phải viết gì đó."

    hoang "Không cần."

    huyen "Cần."

    menu:
        "Ba người quyết định..."

        "Viết ấn tượng đầu tiên về nhau":
            "Huyền chia ba cây bút."

            huyen "Không được cho người khác xem trước."

            tam "Viết hết ba người à?"

            huyen "Mỗi người viết một câu."

            "Tâm viết rất lâu."

            "Hoàng viết nhanh nhất."

            "Huyền che tờ ảnh bằng cả cánh tay."

            "Khi đổi ảnh cho nhau, mặt sau tấm của Hoàng có hai dòng."

            tam "Trông lạnh hơn thực tế."

            huyen "Trông hiền hơn thực tế."

            "Hoàng đọc."

            hoang "Hai người thống nhất trước à?"

            tam "Không."

            huyen "Đáng lẽ nên."

            "Mặt sau ảnh của Huyền:"

            tam "Nhiều năng lượng."

            hoang "Ồn."

            huyen irritated "Tôi giữ quà để làm bằng chứng bạo lực tinh thần."

            $ story_add("hoang_self_acceptance", 5)
            $ story_flag("group_writes_first_impressions")

        "Viết một điều muốn làm cùng nhau trong năm tới":
            "Tâm viết trước."

            tam "Đi du lịch một chuyến."

            huyen "Xa không?"

            tam "Đủ xa để cậu không quay về lấy đồ quên."

            huyen "Không thể."

            "Huyền viết:"

            huyen "Một ngày không nói chuyện công việc."

            "Hoàng nhìn cô."

            huyen "Đừng nhìn. Đấy là mục tiêu dài hạn."

            "Hoàng viết cuối cùng."

            hoang "Vẫn gặp nhau vào ngày này."

            "Hai người kia im một nhịp."

            huyen neutral "Câu này được."

            tam smile "Ừ."

            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ story_flag("group_writes_next_year_plan")

        "Không viết, chụp thêm một tấm mới":
            huyen "Ảnh cũ xấu."

            hoang "Cô vừa nói phải viết."

            huyen "Tôi đổi ý."

            "Cô dựng điện thoại lên thành ghế."

            "Ba người ngồi sát lại."

            "Lần đầu, Tâm mở mắt."

            "Lần thứ hai, Hoàng nhìn nhầm máy."

            "Lần thứ ba, Huyền cười trước khi bộ đếm kết thúc."

            "Họ giữ tấm thứ ba."

            "Không ai hoàn hảo."

            "Nhìn lại đúng là họ."

            $ story_flag("group_recreates_first_photo_again")

    "Ba tấm ảnh được cất vào ba nơi khác nhau."

    "Không món nào riêng hơn món nào."

    "Cũng không món nào thừa."

    return
