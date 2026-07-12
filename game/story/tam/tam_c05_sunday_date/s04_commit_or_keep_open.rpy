# FILE: game/story/tam/tam_c05_sunday_date/s04_commit_or_keep_open.rpy
# Keeps the legacy label name, but no longer chooses the romance.
# It resolves the emotional meaning of the anniversary day.

label tam_c05_sunday_date_s04_commit_or_keep_open:
    $ _anniversary_route = story_state.get("hoang_anniversary_route", "friend_group")

    if _anniversary_route == "tam":
        call tam_c05_sunday_date_s04_tam_return_home

    elif _anniversary_route == "huyen":
        call tam_c05_sunday_date_s04_huyen_return_home

    else:
        call tam_c05_sunday_date_s04_group_afterward

    return


label tam_c05_sunday_date_s04_tam_return_home:
    scene black
    with fade

    "Hoàng đưa Tâm về khi trời đã tối."

    "Xe dừng trước sảnh chung cư."

    "Đèn dưới mái hiên hắt một vệt sáng lên kính chắn gió."

    "Tâm tháo dây an toàn."

    "Cô cầm túi nhưng chưa mở cửa."

    hoang neutral "Hôm nay ổn không?"

    tam teasing "Anh đang xin đánh giá à?"

    hoang "Ừ."

    tam "Bốn sao."

    hoang confused "Trừ ở đâu?"

    tam "Vườn kính đóng."

    hoang "Cái đó không phải lỗi của anh."

    tam "Thế thì bốn sao rưỡi."

    "Hoàng nhìn cô."

    "Tâm bật cười rồi mở cửa xe."

    "Cậu xuống theo."

    "Hai người đứng trước cửa sảnh."

    "Tâm đi được một bước."

    "Rồi quay lại."

    "Cô đưa tay chỉnh cổ áo bên trái của Hoàng."

    "Phần vải bị gập từ sáng cuối cùng cũng nằm đúng chỗ."

    hoang neutral "Cả ngày em mới nói?"

    tam "Em muốn xem bao giờ anh tự nhận ra."

    hoang "Kết quả?"

    tam smile "Không khả quan."

    if story_has_flag("tam_wears_anniversary_earrings") or story_has_flag("hoang_fastens_tam_earring") or story_has_flag("hoang_hesitates_but_fastens_tam_earring"):
        "Đôi bông tai mới khẽ bắt sáng khi Tâm nghiêng đầu."

        "Hoàng nhìn."

        tam teasing "Anh nhìn gì?"

        hoang "Kiểm tra."

        tam "Quà hay người?"

        "Hoàng không trả lời ngay."

        hoang neutral "Cả hai."

        "Tâm giữ tay trên cổ áo anh thêm một nhịp."

        menu:
            "Tâm..."

            "Chạm nhẹ vào tay Hoàng":
                "Tâm hạ tay xuống."

                "Ngón tay cô chạm vào tay Hoàng."

                "Cô không nắm hẳn."

                "Chỉ giữ đủ lâu để cậu hiểu đây không phải vô tình."

                tam neutral "Em vào nhé."

                hoang "Ừ."

                "Không ai rút tay trước câu cuối."

                $ story_add("hoang_tam_trust", 5)
                $ story_add("tam_self_clarity", 5)
                $ story_flag("tam_hoang_anniversary_hand_touch")

            "Hôn nhẹ lên má anh":
                "Tâm nhìn quanh."

                "Sảnh vắng."

                "Cô nhón chân, chạm môi rất nhẹ lên má Hoàng."

                "Nhanh đến mức khi cô lùi lại, Hoàng vẫn đứng yên."

                tam embarrassed "Nửa sao còn lại."

                hoang surprised "Gì?"

                tam "Đừng làm quá."

                "Cô quay vào trong."

                "Cánh cửa kính khép lại trước khi Hoàng kịp trả lời."

                $ story_add("hoang_tam_trust", 10)
                $ story_add("tam_hoang_interest", 5)
                $ story_flag("tam_kisses_hoang_cheek_anniversary")

            "Chỉ chúc ngủ ngon":
                tam smile "Ngủ ngon."

                hoang "Em cũng thế."

                "Tâm đi vào sảnh."

                "Trước khi cửa khép, cô quay lại."

                tam "Em thích quà."

                "Hoàng gật."

                "Cô biết cậu sẽ nhớ câu đó lâu hơn cái hôn nào."

                $ story_add("hoang_tam_trust", 5)
                $ story_flag("tam_confirms_anniversary_gift_at_door")

    elif story_has_flag("tam_expensive_gift_repaired_together"):
        tam neutral "Lần sau đừng chuẩn bị để làm em ấn tượng."

        hoang "Thế chuẩn bị để làm gì?"

        tam "Để hai đứa vui."

        "Hoàng nhìn cô."

        "Cậu gật chậm."

        hoang "Anh biết rồi."

        tam "Lần này em tin."

        "Tâm rút tay khỏi cổ áo."

        "Trước khi đi vào, cô đặt chiếc hộp lại vào tay anh."

        tam smile "Tuần sau đi đổi."

        hoang "Ừ."

        $ story_add("hoang_tam_trust", 5)
        $ story_flag("tam_hoang_anniversary_repairs_overcompensation")

    elif story_has_flag("tam_accepts_expensive_gift_uneasily"):
        "Chiếc hộp vẫn nằm trong túi Tâm."

        "Không ai nhắc tới."

        tam neutral "Cảm ơn anh về hôm nay."

        hoang "Ừ."

        "Câu trả lời quá gọn."

        "Cả hai đều biết còn một việc chưa nói."

        tam "Mai mình nói chuyện nhé."

        "Hoàng nhìn cô."

        hoang "Được."

        "Tâm bước vào sảnh."

        "Cánh cửa khép lại."

        "Ngày hôm nay không hỏng."

        "Chỉ chưa được cất đúng chỗ."

        $ story_add("hoang_insecurity", 5)
        $ story_flag("tam_hoang_anniversary_ends_with_unresolved_gift")

    elif story_has_flag("tam_refuses_gift_without_rejecting_hoang"):
        tam neutral "Anh có giận không?"

        hoang "Không."

        tam "Nói thật."

        "Hoàng nhìn xuống chiếc hộp trong tay."

        hoang "Hơi hụt."

        tam "Em biết."

        hoang "Nhưng không giận."

        "Tâm gật."

        tam smile "Thế được."

        "Cô bước vào trong."

        "Hoàng cất hộp vào túi."

        "Lần này, nó không còn giống một thất bại."

        "Chỉ là một lựa chọn cần làm lại."

        $ story_add("hoang_self_acceptance", 5)
        $ story_add("hoang_tam_trust", 5)
        $ story_flag("tam_hoang_anniversary_honest_boundary")

    else:
        "Tâm lấy tờ giấy gấp trong túi."

        tam neutral "Bản nháp này em giữ."

        hoang "Ừ."

        tam "Bản chính đừng viết cầu kỳ quá."

        hoang "Anh chưa hứa có bản chính."

        tam teasing "Anh vừa hứa rồi."

        "Tâm cất lại tờ giấy."

        "Cô đi vào sảnh với khóe môi vẫn cong."

        $ story_add("hoang_tam_trust", 5)
        $ story_flag("tam_hoang_anniversary_keeps_future_open")

    $ story_flag("tam_hoang_one_year_anniversary_completed")

    # This is reinforcement of an existing route, not a new commitment.
    if story_state.get("hoang_tam_trust", 0) >= 60 and story_state.get("tam_hoang_interest", 0) >= 60 and not story_has_flag("tam_hoang_anniversary_ends_with_unresolved_gift"):
        $ story_add_ending_support("e02_tam_hoang")
        $ story_flag("tam_hoang_anniversary_route_reinforced")

    return


label tam_c05_sunday_date_s04_huyen_return_home:
    scene black
    with fade

    "Hoàng đưa Huyền về muộn hơn dự kiến."

    "Xe dừng trước chung cư."

    "Huyền vẫn cầm túi quà trên đùi."

    "Cô đã mở khóa cửa."

    "Nhưng chưa xuống."

    huyen neutral "Này."

    hoang "Gì?"

    "Huyền nhìn ra ngoài cửa kính."

    huyen "Nếu lúc đầu Tâm thích anh hơn một chút..."

    "Cô xoay dây túi quanh ngón tay."

    huyen "Hôm nay người ngồi trên xe có phải tôi không?"

    "Câu hỏi nghe như một câu đùa đã quên mất phần gây cười."

    if story_state.get("hoang_self_acceptance", 0) >= 55:
        "Hoàng không trả lời ngay."

        hoang neutral "Anh không biết một năm trước sẽ thế nào."

        huyen "Câu trả lời khéo thật."

        hoang "Anh chưa nói xong."

        "Hoàng tắt máy xe."

        "Tiếng động cơ biến mất."

        hoang "Lúc đầu anh để ý Tâm hơn."

        huyen "Ừ."

        hoang "Nhưng ba tháng nay, người anh chờ nhắn khi về nhà là em."

        "Huyền không nhìn cậu ngay."

        huyen neutral "Ba tháng thôi à?"

        hoang "Em muốn tính từ lúc nào?"

        "Khóe miệng Huyền cong lên."

        huyen "Để tôi kiểm tra lại lịch."

        if story_has_flag("hoang_huyen_first_deliberate_photo") or story_has_flag("huyen_places_hoang_in_album") or story_has_flag("hoang_corrects_safe_album_with_couple_photo") or story_has_flag("hoang_huyen_start_album_today"):
            "Huyền mở cửa xe."

            "Trước khi xuống, cô lấy từ túi ra tấm ảnh hai người."

            "Cô đặt nó vào ngăn nhỏ trước mặt Hoàng."

            hoang confused "Em để quên."

            huyen "Không."

            huyen "Bản của anh."

            "Cô xuống xe."

            "Cửa đóng lại."

            "Hoàng nhìn tấm ảnh."

            "Mặt sau có một dòng chữ nhỏ:"

            "Ngày đầu anh nói rõ."

            $ story_add("huyen_hoang_interest", 10)
            $ story_add("hoang_huyen_interest", 5)
            $ story_flag("hoang_huyen_anniversary_clearly_confirmed")
        else:
            "Huyền mở cửa."

            huyen "Hôm nay được."

            hoang "Chỉ hôm nay?"

            huyen "Năm sau làm tốt hơn."

            "Cô bước xuống, ôm chiếc túi sát bên người."

            $ story_add("huyen_hoang_interest", 5)
            $ story_flag("hoang_huyen_anniversary_gently_confirmed")

    elif story_state.get("hoang_self_acceptance", 0) >= 35:
        menu:
            "Hoàng trả lời..."

            "“Không biết lúc đó. Nhưng hôm nay anh chọn em.”":
                hoang "Anh không biết lúc đó."

                "Huyền nhìn sang."

                hoang "Nhưng hôm nay anh chọn em."

                "Cô im vài giây."

                huyen "Câu này tập trước à?"

                hoang "Không."

                huyen "May."

                hoang "Sao?"

                huyen "Tập rồi mà chỉ được thế thì hơi phí."

                "Cô mở cửa xe."

                "Khóe môi vẫn cong."

                $ story_add("hoang_self_acceptance", 5)
                $ story_add("huyen_hoang_interest", 10)
                $ story_flag("hoang_chooses_huyen_in_present")

            "“Hôm nay anh mời em. Thế chưa đủ à?”":
                hoang "Hôm nay anh mời em."

                hoang "Thế chưa đủ à?"

                "Huyền gật nhẹ."

                huyen "Hôm nay thì đủ."

                "Cô cầm túi quà."

                huyen "Mai tính tiếp."

                "Câu trả lời không phải từ chối."

                "Cũng chưa phải nơi để Hoàng nghỉ hẳn."

                $ story_add("huyen_hoang_interest", 5)
                $ story_add("hoang_insecurity", 5)
                $ story_flag("hoang_huyen_anniversary_present_only")

            "“Chuyện đó không xảy ra.”":
                hoang "Chuyện đó không xảy ra."

                huyen "Tôi biết."

                hoang "Thế sao còn hỏi?"

                huyen "Vì tôi hỏi anh."

                "Hoàng không trả lời."

                "Huyền gật như thể đã nhận được một câu."

                huyen neutral "Ngủ ngon."

                "Cô xuống xe."

                "Món quà vẫn được mang theo."

                "Khoảng trống trong câu trả lời cũng vậy."

                $ story_add("hoang_insecurity", 10)
                $ story_flag("hoang_avoids_huyen_second_choice_question")

    else:
        "Hoàng nhìn vô-lăng."

        "Cậu biết câu trả lời mình nên nói."

        "Không chắc đó có phải câu trả lời thật."

        hoang neutral "Anh không biết."

        "Huyền gật."

        "Không giận."

        "Điều đó khiến câu trả lời càng khó chịu."

        huyen "Ừ."

        "Cô đặt túi quà xuống ghế."

        hoang confused "Em không lấy à?"

        huyen "Để hôm khác."

        hoang "Huyền."

        huyen "Không sao."

        "Cô mở cửa."

        huyen neutral "Nhưng đừng tặng tôi thứ anh còn đang dùng để hỏi về người khác."

        "Cửa xe khép lại."

        "Hoàng ngồi yên."

        "Cậu không gọi theo."

        "Ít nhất lần này, cậu hiểu giữ người khác lại khi mình chưa đứng vững không phải là tử tế."

        $ story_state["hoang_anniversary_route"] = "friend_group"
        $ story_add("hoang_self_acceptance", 5)
        $ story_add("hoang_insecurity", 5)
        $ story_flag("hoang_huyen_anniversary_returns_to_friendship")

    $ story_flag("hoang_huyen_one_year_anniversary_completed")

    return


label tam_c05_sunday_date_s04_group_afterward:
    scene black
    with fade

    "Tối hôm đó, ba người đã về nhà."

    "Nhóm trò chuyện sáng lên trước."

    huyen "Ảnh mới đây."

    "Tấm ảnh ở công viên xuất hiện."

    "Tâm mở mắt."

    "Hoàng đứng tự nhiên hơn."

    "Huyền nhìn sai hướng."

    tam "Tấm này em mở mắt rồi."

    hoang "Huyền nhắm."

    huyen "Tôi không nhắm."

    hoang "Cô đang nhìn anh."

    huyen "Thế thì càng không nhắm."

    tam "Giữ tấm này nhé."

    huyen "Có ảnh đẹp là được."

    huyen "Không cần ai cũng hoàn hảo."

    "Hoàng nhìn câu cuối."

    "Cậu lưu ảnh."

    "Không nói."

    "Một lúc sau, Tâm gửi thêm một tin."

    tam "Cảm ơn vì hôm nay."

    huyen "Năm sau vẫn thế nhé."

    "Hoàng gõ một câu."

    "Xóa."

    "Rồi gõ lại."

    hoang "Ừ."

    "Chỉ một chữ."

    "Hai người kia đều thả biểu tượng đồng ý."

    "Sau đúng một năm, không có lời tỏ tình nào được đưa ra."

    "Không ai bị đặt vào vai lựa chọn thứ hai."

    "Chỉ có ba người vẫn tự nguyện dành một ngày cho nhau."

    "Hiện tại, như thế là đủ."

    $ story_flag("tam_huyen_hoang_one_year_close_friends")
    $ story_add_direction("hoang", "hoang_friend_group_stable")
    $ story_add("hoang_self_acceptance", 5)

    return
