# FILE: game/story/tam/tam_c05_sunday_date/s02_date_or_group.rpy
# The outing begins in the shape already determined by C04/H01.

label tam_c05_sunday_date_s02_date_or_group:
    $ _anniversary_route = story_state.get("hoang_anniversary_route", "friend_group")

    if _anniversary_route == "tam":
        call tam_c05_sunday_date_s02_tam_date

    elif _anniversary_route == "huyen":
        call tam_c05_sunday_date_s02_huyen_date

    else:
        call tam_c05_sunday_date_s02_friend_group

    return


label tam_c05_sunday_date_s02_tam_date:
    scene bg_apartment_lobby_morning
    with fade

    "Cửa thang máy mở ra."

    "Hoàng đang đứng gần lối vào, một tay cầm chìa khóa xe."

    "Anh mặc sơ-mi sáng màu, áo khoác mỏng và đôi giày chỉ xuất hiện trong những dịp cần nghiêm túc hơn bình thường."

    "Nghiêm túc hơn khá nhiều."

    "Tâm bước ra."

    scene cg_tam_c05_tam_pickup
    with dissolve
    "Hoàng nhìn cô."
    scene bg_apartment_lobby_morning
    with dissolve

    "Rất ngắn."

    "Rồi lại nhìn thêm một lần."

    tam teasing "Anh đến sớm à?"

    hoang neutral "Không."

    tam teasing "Em chưa hỏi giờ."

    "Hoàng khựng lại nửa nhịp."

    hoang smile "Ừ. Anh đến sớm."

    "Tâm đi tới gần."

    "Lúc ấy cô mới nhận ra cổ áo bên trái của Hoàng bị gập nhẹ vào trong."

    "Anh đã chuẩn bị gần như mọi thứ."

    "Chỉ quên nhìn lại mình."

    "Tâm không nói."

    "Chưa."

    hoang neutral "Em mặc thế có lạnh không?"

    tam smile "Lát nữa trời ấm lên là ổn."

    "Hoàng nhìn phần tay áo mỏng của cô."

    "Anh không tranh luận."

    "Chỉ mở cửa xe rồi lấy từ ghế sau một chiếc áo khoác khác đặt sang bên cạnh."

    tam teasing "Anh có phương án dự phòng thật à?"

    hoang neutral "Cho thời tiết."

    tam "Chỉ thời tiết thôi?"

    hoang "Em lên xe đi."

    scene bg_c05_breakfast
    with dissolve

    "Quán ăn sáng nằm trên một con phố yên, bàn sát cửa kính đã được đặt trước."

    "Hoàng gọi món mà không cần hỏi lại Tâm có uống lạnh hay không."

    scene cg_tam_c05_tam_breakfast
    with dissolve
    "Cốc nước của cô không có đá."
    scene bg_c05_breakfast
    with dissolve

    "Phần ăn cũng không có hành."

    "Ba tháng trước, Tâm sẽ cảm ơn."

    "Bây giờ cô chỉ kéo đĩa về phía mình như thể mọi chuyện vốn nên như vậy."

    tam neutral "Anh ăn gì?"

    hoang "Như cũ."

    tam "Anh lại bỏ cà phê à?"

    hoang "Anh uống rồi."

    tam irritated "Lúc mấy giờ?"

    hoang "Sáu giờ."

    tam "Thế mà còn hỏi em có lạnh không."

    "Hoàng nhìn cô."

    hoang neutral "Hai chuyện không liên quan."

    tam "Anh cứ nghĩ thế đi."

    scene bg_taxi_interior_day
    with dissolve

    "Sau bữa sáng, xe rời khu trung tâm."

    "Tâm tự mở ngăn trước ghế lấy khăn giấy."

    "Cô chỉnh nhiệt độ lên một nấc."

    "Rồi bỏ qua ba bài hát liên tiếp trong danh sách phát."

    hoang neutral "Bài thứ hai có gì không ổn?"

    tam "Huyền thêm."

    hoang "Sao em biết?"

    tam "Tên bài có ba dấu chấm than."

    "Hoàng không phản bác."

    "Cậu đã biết."

    scene bg_c05_glasshouse
    with dissolve

    "Điểm đến là một công viên lớn ở phía bên kia thành phố."

    "Hoàng định đưa Tâm đến khu vườn kính nằm sâu bên trong."

    "Tấm biển đặt trước lối vào lại viết rất rõ:"

    "TẠM ĐÓNG ĐỂ BẢO TRÌ HỆ THỐNG ĐIỆN."

    scene cg_tam_c05_tam_glasshouse
    with dissolve
    "Hoàng đứng trước tấm biển."
    scene bg_c05_glasshouse
    with dissolve

    "Tâm đứng bên cạnh."

    "Một cơn gió lướt qua."

    "Cổ áo anh vẫn gập."

    if story_state.get("hoang_self_acceptance", 0) >= 55:
        "Hoàng đọc hết dòng thông báo."

        "Sau đó cất điện thoại vào túi."

        hoang neutral "Được."

        tam confused "Được gì?"

        hoang "Phương án hai."

        tam "Anh có thật à?"

        hoang "Không."

        tam smile "Em bắt đầu thích phương án hai rồi đấy."

        "Hoàng nhìn quanh."

        "Cách đó không xa có một xe bán bánh nóng và cà phê giấy."

        hoang "Đi ăn tiếp không?"

        tam laughing "Anh định nuôi em đến chiều à?"

        hoang "Em có thể từ chối."

        tam "Không."

        "Hai người đi về phía xe hàng."

        $ story_flag("hoang_accepts_anniversary_plan_change")
        $ story_add("hoang_self_acceptance", 5)

    elif story_state.get("hoang_self_acceptance", 0) >= 35:
        "Hoàng mở điện thoại."

        "Anh kiểm tra trang của công viên."

        "Rồi kiểm tra lại thư xác nhận."

        "Sau đó tìm một địa điểm khác cách đây mười hai phút lái xe."

        tam neutral "Hoàng."

        hoang "Ừ?"

        tam "Anh đang làm gì thế?"

        hoang "Tìm chỗ khác."

        tam "Em biết."

        tam "Ý em là anh đang cố cứu cái gì?"

        "Ngón tay Hoàng dừng trên màn hình."

        menu:
            "Tâm..."

            "Kéo nhẹ tay áo anh":
                "Tâm nắm phần tay áo gần cổ tay Hoàng."

                tam "Ngồi đâu đó thôi."

                hoang "Em không thất vọng à?"

                tam "Có."

                "Hoàng nhìn cô."

                tam smile "Em đã định chụp ảnh trong vườn kính."

                tam "Nhưng anh đứng đây xin lỗi thêm năm phút thì em sẽ thất vọng hơn."

                "Hoàng tắt màn hình."

                hoang neutral "Có xe bán bánh bên kia."

                tam "Thế đi."

                $ story_add("hoang_tam_trust", 5)
                $ story_add("hoang_insecurity", -5)
                $ story_flag("tam_pulls_hoang_out_of_overplanning")

            "Để anh tìm phương án khác":
                "Tâm đứng đợi."

                "Mười phút sau, Hoàng tìm được một quán trà cách đó gần ba cây số."

                "Quán mở."

                "Có chỗ."

                "Mọi thứ lại đúng kế hoạch."

                "Chỉ có vẻ mặt Hoàng chưa thật sự thả lỏng."

                tam neutral "Lần sau mình không cần chạy nhanh thế đâu."

                hoang "Anh biết."

                "Giọng anh cho thấy cậu chưa biết hẳn."

                $ story_add("hoang_insecurity", 5)
                $ story_flag("hoang_saves_plan_but_not_mood")

            "Trêu anh bị trừ điểm":
                tam teasing "Một điểm trừ."

                hoang confused "Gì?"

                tam "Không kiểm tra lịch bảo trì."

                "Hoàng im một nhịp."

                tam "Nhưng có chuẩn bị áo khoác."

                tam "Cộng lại vẫn dương."

                "Khóe miệng Hoàng nhếch lên."

                hoang "Em chấm dễ thế?"

                tam "Tùy người."

                $ story_add("hoang_tam_trust", 5)
                $ story_add("hoang_self_acceptance", 5)
                $ story_flag("tam_turns_failed_plan_into_joke")

    else:
        "Hoàng đọc tấm biển hai lần."

        "Rồi quay sang nhìn Tâm."

        hoang neutral "Anh xin lỗi."

        tam confused "Vì công viên bảo trì à?"

        hoang "Đáng lẽ anh phải kiểm tra."

        tam "Anh đã kiểm tra rồi."

        hoang "Chưa đủ."

        "Cậu mở điện thoại."

        "Bàn tay kéo màn hình nhanh hơn bình thường."

        "Một địa điểm khác."

        "Một quán khác."

        "Một tuyến đường khác."

        "Tâm nhìn anh thêm vài giây."

        "Sau đó cô đi sang xe hàng gần đó, mua hai chiếc bánh nóng."

        "Cô quay lại, đặt một chiếc lên điện thoại Hoàng."

        tam neutral "Kiểm tra cái này trước."

        hoang confused "Gì?"

        tam "Xem có ăn được không."

        "Hoàng nhìn chiếc bánh."

        "Rồi nhìn cô."

        menu:
            "Hoàng..."

            "Cất điện thoại":
                "Hoàng khóa màn hình."

                "Cậu nhận chiếc bánh."

                hoang neutral "Anh hơi làm quá."

                tam smile "Một chút."

                hoang "Em không cần đồng ý nhanh thế."

                tam "Bánh nguội rồi."

                $ story_add("hoang_self_acceptance", 5)
                $ story_add("hoang_insecurity", -5)
                $ story_flag("hoang_admits_anniversary_overcontrol")

            "Vẫn cố tìm địa điểm khác":
                hoang "Cho anh hai phút."

                "Tâm không cản."

                "Cô ngồi xuống chiếc ghế gần đó, ăn phần của mình."

                "Hai phút thành bảy."

                "Khi Hoàng ngồi xuống, chiếc bánh của cậu đã nguội."

                tam neutral "Em không giận."

                hoang "Anh biết."

                tam "Anh không biết."

                "Cô nói rất nhẹ."

                "Hoàng không mở điện thoại nữa."

                $ story_add("hoang_insecurity", 10)
                $ story_flag("hoang_anniversary_plan_stays_tense")

            "Hỏi Tâm có muốn về không":
                hoang "Nếu em muốn, mình có thể về."

                "Tâm nhìn cậu."

                tam neutral "Anh có muốn về không?"

                hoang "Không."

                tam "Em cũng không."

                tam "Vậy đừng hỏi thay em."

                "Hoàng thở ra."

                hoang neutral "Ừ."

                $ story_add("hoang_self_acceptance", 5)
                $ story_add("hoang_tam_trust", 5)
                $ story_flag("tam_refuses_to_be_decided_for")

    scene bg_c05_park
    with dissolve

    "Cuối cùng, hai người ngồi trên một chiếc ghế đá dưới hàng cây."

    "Không có vườn kính."

    "Không có góc chụp Hoàng đã xem trước."

    scene cg_tam_c05_tam_bench
    with dissolve
    "Chỉ có hai cốc giấy, túi bánh đặt giữa, và vài chiếc lá khô bị gió đẩy ngang lối đi."
    scene bg_c05_park
    with dissolve

    "Tâm nghiêng người lấy khăn giấy."

    "Vai cô chạm vào cánh tay Hoàng."

    "Không ai lùi."

    "Sau một lúc, Tâm nhìn sang."

    tam neutral "Anh nhớ ngày đầu thật à?"

    hoang "Ừ."

    tam "Em tưởng anh chỉ nhớ Huyền gọi quá nhiều món."

    hoang smile "Cái đó khó quên."

    tam "Còn em?"

    "Hoàng nhìn cô."

    hoang neutral "Em ngồi đối diện anh."

    tam "Thế thôi?"

    hoang "Em nhìn anh ba lần rồi giả vờ không nhìn."

    "Tâm quay mặt đi."

    tam irritated "Anh nhớ nhầm rồi."

    hoang "Ừ."

    "Giọng anh không có vẻ tin."

    return


label tam_c05_sunday_date_s02_huyen_date:
    scene bg_apartment_lobby_morning
    with fade

    "Huyền xuống sảnh muộn tám phút."

    "Hoàng đứng cạnh xe, tay cầm hai cốc đồ uống."

    "Cậu nhìn đồng hồ."

    huyen irritated "Đừng nói."

    hoang "Anh chưa nói."

    huyen "Mặt anh nói rồi."

    hoang neutral "Tám phút."

    huyen "Tôi đã giảm từ mười ba xuống tám."

    hoang "Tiến bộ đáng ghi nhận."

    scene cg_tam_c05_huyen_pickup
    with dissolve
    "Huyền nhận cốc từ tay anh."
    scene bg_apartment_lobby_morning
    with dissolve

    "Không lạnh."

    "Ít đường."

    "Cô uống một ngụm."

    huyen neutral "Tâm đâu?"

    hoang "Không đi."

    huyen "Bận à?"

    hoang "Không."

    "Hoàng mở cửa xe."

    hoang neutral "Anh không mời."

    "Huyền nhìn cậu."

    huyen surprised "Ồ."

    hoang "Ồ là sao?"

    huyen "Không sao."

    hoang "Cô vừa nói bằng cái giọng rất có sao."

    huyen "Đứng lâu Tâm đổi ý bây giờ."

    "Cô lên xe trước."

    "Hoàng không sửa câu nói ấy."

    scene bg_c05_market_cafe
    with dissolve

    "Buổi sáng bắt đầu ở một quán nhỏ gần khu chợ cuối tuần."

    "Không có khăn trải bàn trắng."

    "Không có nhân viên kéo ghế."

    "Có một bảng menu viết tay, tiếng máy pha cà phê và mùi bánh mới nướng."

    huyen neutral "Ít nhất anh cũng biết không nên mặc suit."

    hoang confused "Anh từng mặc suit đi ăn với em à?"

    huyen "Chưa."

    huyen "Tôi đang khen khả năng phòng ngừa."

    scene cg_tam_c05_huyen_breakfast
    with dissolve
    "Hoàng đẩy đĩa bánh về phía cô."
    scene bg_c05_market_cafe
    with dissolve

    hoang "Cô chưa ăn sáng."

    huyen "Ai bảo?"

    hoang "Tin nhắn lúc 7:42."

    huyen "Không liên quan."

    hoang "Cô ăn đi."

    "Huyền bẻ một miếng."

    "Sau đó là miếng thứ hai."

    "Cô không tiếp tục tranh luận với bằng chứng."

    scene bg_c05_market_day
    with dissolve

    "Rời quán, họ đi bộ qua khu chợ."

    "Huyền chụp biển hiệu."

    "Chụp một đứa trẻ đang đuổi bong bóng."

    "Chụp con chó nằm dưới chân quầy hoa."

    "Chụp Hoàng đúng lúc cậu quay sang."

    hoang irritated "Xóa đi."

    huyen smile "Không."

    hoang "Mắt anh nhắm."

    huyen "Nghệ thuật."

    "Hoàng chìa tay."

    hoang "Đưa máy đây."

    huyen "Máy tôi hết pin."

    "Màn hình điện thoại trong tay cô sáng lên."

    "Chín mươi tám phần trăm."

    "Hai người cùng nhìn."

    huyen neutral "Nó... hồi pin."

    hoang "Ừ."

    huyen "Công nghệ mới."

    hoang "Đưa đây."

    "Hoàng cầm điện thoại."

    "Lần đầu trong buổi sáng, Huyền đứng ở phía trước ống kính."

    huyen confused "Anh chụp gì?"

    hoang "Đứng yên."

    huyen "Tôi không—"

    scene cg_tam_c05_huyen_photo
    with dissolve
    "Máy ảnh chớp."
    scene bg_c05_market_day
    with dissolve

    huyen irritated "Xấu thì xóa."

    hoang "Để xem đã."

    "Cô bước tới định giật lại."

    "Hoàng giơ tay cao hơn."

    huyen "Trẻ con à?"

    hoang "Ai giật điện thoại người khác trước?"

    "Huyền đứng sát lại."

    "Đúng lúc đó, vài giọt mưa rơi xuống màn hình."

    "Rồi thêm nhiều giọt khác."

    scene bg_c05_rain_awning
    with dissolve

    "Hai người chạy vào dưới mái hiên của một cửa hàng đã đóng."

    "Mưa đổ xuống rất nhanh."

    "Khu chợ trước mặt lập tức co lại dưới những tấm bạt."

    scene cg_tam_c05_huyen_rain
    with dissolve
    "Huyền phủi nước trên tóc."
    scene bg_c05_rain_awning
    with dissolve

    huyen neutral "Kế hoạch đẹp thật."

    "Hoàng nhìn trời."

    if story_state.get("hoang_self_acceptance", 0) >= 55:
        hoang "Ừ."

        huyen confused "Ừ?"

        hoang "Mưa."

        huyen "Tôi thấy."

        hoang "Phía bên kia có arcade."

        huyen "Anh định đưa tôi vào chơi game giữa buổi hẹn à?"

        hoang neutral "Em vừa gọi đây là buổi hẹn."

        "Huyền im."

        "Hoàng nhìn cô."

        huyen irritated "Tôi đang nói theo cách của anh."

        hoang "Anh chưa gọi."

        huyen "Thế thôi."

        "Cô bước ra khỏi mái hiên."

        "Hoàng kéo nhẹ quai túi trên vai cô lại trước khi cô bước hẳn vào mưa."

        hoang "Chạy qua."

        "Huyền không gỡ tay cậu."

        $ story_add("hoang_self_acceptance", 5)
        $ story_flag("hoang_huyen_turn_rain_into_date")

    elif story_state.get("hoang_self_acceptance", 0) >= 35:
        "Hoàng mở bản đồ."

        "Huyền nhìn màn hình từ bên cạnh."

        huyen "Anh lại tìm chỗ khác à?"

        hoang "Có một quán ảnh ở cuối phố."

        huyen "Mưa thế này?"

        hoang "Có mái che."

        menu:
            "Hoàng..."

            "Rủ Huyền sang khu arcade gần đó":
                hoang "Qua bên kia chơi game."

                huyen surprised "Thật à?"

                hoang "Cô sợ thua?"

                huyen "Anh nói lại xem."

                "Huyền kéo tay áo Hoàng."

                huyen "Chạy."

                "Hai người lao qua màn mưa."

                $ story_add("hoang_huyen_interest", 5)
                $ story_add("huyen_hoang_interest", 5)
                $ story_flag("hoang_huyen_arcade_detour")

            "Để Huyền chọn nơi tiếp theo":
                hoang "Em muốn đi đâu?"

                huyen "Anh hỏi tôi à?"

                hoang "Ừ."

                "Huyền nhìn quanh."

                huyen "Có cửa hàng sách cũ phía sau chợ."

                hoang "Đi."

                huyen "Không tiếc kế hoạch à?"

                hoang "Anh đang đi với em."

                "Câu trả lời đến tự nhiên hơn Hoàng dự kiến."

                "Huyền quay mặt nhìn mưa."

                huyen neutral "Ừ. Đi thôi."

                $ story_add("hoang_self_acceptance", 5)
                $ story_add("huyen_hoang_interest", 5)
                $ story_flag("hoang_lets_huyen_shape_date")

            "Cố giữ lịch trình ban đầu":
                hoang "Đợi mưa nhỏ rồi đi tiếp."

                huyen "Chỗ tiếp theo ở ngoài trời đúng không?"

                hoang "Ừ."

                "Huyền nhìn màn mưa."

                "Rồi nhìn Hoàng."

                huyen neutral "Anh cứng đầu thật đấy."

                hoang "Anh đã đặt trước."

                huyen "Tôi biết."

                "Cô không cãi thêm."

                "Sự im lặng của cô khiến Hoàng nhận ra mình đang bảo vệ lịch trình nhiều hơn buổi đi chơi."

                $ story_add("hoang_insecurity", 5)
                $ story_flag("hoang_huyen_date_stays_overplanned")

    else:
        "Hoàng nhìn điện thoại."

        "Rồi nhìn Huyền."

        hoang "Hay anh gọi Tâm?"

        huyen confused "Gọi Tâm làm gì?"

        hoang "Nếu chuyển thành đi ba người—"

        "Câu nói dừng giữa chừng."

        "Huyền không cười."

        "Đây là điều hiếm hơn mưa trái mùa."

        huyen neutral "Anh mời tôi ra đây."

        hoang "Anh biết."

        huyen "Thế thì đừng tìm người thứ ba để làm mọi thứ đỡ giống một buổi hẹn."

        "Hoàng siết điện thoại."

        menu:
            "Hoàng..."

            "Cất điện thoại và xin lỗi":
                hoang "Anh xin lỗi."

                huyen "Đừng xin lỗi kiểu chuẩn bị rút lui."

                hoang "Anh không gọi."

                "Huyền nhìn cậu thêm một lúc."

                huyen "Phía bên kia có arcade."

                hoang "Ừ."

                huyen "Tôi sẽ thắng."

                "Cô bước ra trước."

                "Hoàng đi theo."

                $ story_add("hoang_self_acceptance", 5)
                $ story_add("hoang_insecurity", -5)
                $ story_flag("hoang_stays_in_huyen_date_despite_fear")

            "Đổi thật sang buổi đi ba người":
                hoang "Anh nghĩ đi cả ba sẽ thoải mái hơn."

                "Huyền gật rất nhanh."

                huyen "Ừ."

                "Nhanh đến mức câu trả lời không kịp mang cảm xúc."

                $ story_state["hoang_anniversary_route"] = "friend_group"
                $ story_flag("hoang_huyen_date_collapses_to_group")
                $ story_add("hoang_insecurity", 10)

                return

            "Đánh trống lảng":
                hoang "Anh chỉ hỏi thế thôi."

                huyen "Ừ."

                huyen "Tôi cũng chỉ trả lời thế thôi."

                "Mưa vẫn rơi."

                "Khoảng cách dưới mái hiên bỗng rộng hơn lúc mới chạy vào."

                $ story_add("hoang_insecurity", 10)
                $ story_flag("hoang_huyen_date_avoids_core_question")

    "Khi mưa nhỏ lại, Huyền lấy điện thoại ra."

    "Cô mở tấm ảnh Hoàng vừa chụp."

    "Tóc cô hơi rối."

    "Phía sau là những tấm bạt nhiều màu."

    "Cô không nhìn vào máy."

    "Cô đang nhìn người cầm máy."

    huyen neutral "Cũng được."

    hoang "Anh tưởng xấu thì xóa."

    huyen "Tôi nói mặt tôi."

    hoang "Ừ."

    huyen irritated "Ý gì?"

    hoang smile "Không có gì."

    "Huyền khóa màn hình."

    "Cô không xóa ảnh."

    return


label tam_c05_sunday_date_s02_friend_group:
    scene bg_c05_breakfast
    with fade

    "Hoàng đưa hai người đến một quán ăn nằm không xa nơi họ từng gặp nhau lần đầu."

    "Không phải đúng nhà hàng cũ."

    "Huyền đã phản đối vì giá đắt."

    "Sau đó cô gọi nhiều món nhất bàn."

    tam neutral "Cậu nói chỉ ăn nhẹ thôi mà."

    huyen "Tôi gọi để ba người cùng ăn."

    hoang "Bốn phần món chính?"

    huyen "Anh đang làm tôi mất mặt trước đồ ăn đấy."

    scene cg_tam_c05_group_meal
    with dissolve
    "Tâm bật cười."
    scene bg_c05_breakfast
    with dissolve

    "Một năm trước, cô đã ngồi đối diện Hoàng trong một bữa ăn khác."

    "Khi ấy, họ chưa biết sẽ còn gặp lại."

    "Chưa biết sẽ làm việc cạnh nhau."

    "Chưa biết nhóm trò chuyện kia sẽ sống lâu hơn rất nhiều kế hoạch công việc."

    huyen neutral "Nói thật đi."

    hoang "Gì?"

    huyen "Lúc đầu ông để ý ai hơn?"

    "Tâm đang uống nước."

    "Cô dừng lại."

    hoang neutral "Tâm."

    "Tâm suýt sặc."

    huyen laughing "Biết ngay."

    tam embarrassed "Sao tự nhiên lại hỏi chuyện đó?"

    huyen "Kỷ niệm một năm phải tổng kết."

    hoang "Còn cô thì nói liên tục."

    huyen irritated "Nghĩa là sao?"

    hoang "Không cần để ý cũng nghe thấy."

    huyen "Rồi sau đó?"

    menu:
        "Hoàng trả lời..."

        "“Sau đó thấy cả hai đều phiền.”":
            hoang "Sau đó thấy cả hai đều phiền."

            tam smile "Em bắt đầu thấy buổi kỷ niệm này không đáng đi rồi."

            huyen "Ông ăn một mình đi."

            "Hai người cùng kéo đĩa thức ăn về phía mình."

            "Hoàng nhìn phần bàn trống trước mặt."

            hoang smile "Anh gọi thêm."

            $ story_add("hoang_self_acceptance", 5)
            $ story_flag("hoang_answers_first_impression_honestly")

        "“Tâm dễ nói chuyện hơn, Huyền khó quên hơn.”":
            hoang "Tâm dễ nói chuyện hơn."

            tam surprised "Còn Huyền?"

            hoang "Khó quên hơn."

            "Huyền đang cầm đũa."

            "Cô dừng rất nhẹ."

            huyen teasing "Nghe không giống lời khen."

            hoang "Tùy cô."

            "Tâm nhìn hai người."

            "Rồi cúi xuống lấy thêm thức ăn."

            "Cô không xen vào."

            $ story_flag("hoang_acknowledges_both_friend_dynamics")
            $ story_add("hoang_self_acceptance", 5)

        "Từ chối trả lời":
            hoang "Câu hỏi không có lợi cho anh."

            huyen "Hèn."

            tam "Em thấy hợp lý."

            huyen "Bà đứng về phe nào?"

            tam "Phe được ăn yên."

            "Huyền chuyển sang hỏi ấn tượng đầu tiên của Tâm."

            "Hoàng được tha."

            "Tạm thời."

            $ story_flag("hoang_avoids_first_impression_question")

    scene bg_c05_park
    with dissolve

    "Sau bữa ăn, ba người đi bộ sang công viên."

    "Huyền nhất quyết bắt chụp lại một tấm ảnh gần giống ảnh ở tiệc công ty."

    "Cô đặt điện thoại lên lan can."

    "Hẹn giờ mười giây."

    "Rồi chạy về."

    huyen "Xích vào."

    tam "Tớ đang đứng sát rồi."

    huyen "Hoàng."

    hoang "Gì?"

    huyen "Anh đứng như chụp ảnh thẻ thế?"

    "Hoàng thở ra."

    "Cậu đặt một tay lên vai Tâm."

    "Tay còn lại lên vai Huyền."

    scene cg_tam_c05_group_photo
    with dissolve
    "Máy ảnh chớp đúng lúc Huyền quay sang nhìn cậu."
    scene bg_c05_park
    with dissolve

    "Tấm ảnh không hoàn hảo."

    "Tâm mở mắt."

    "Hoàng không còn lúng túng."

    "Huyền lại nhìn sai hướng."

    huyen irritated "Chụp lại."

    tam laughing "Thôi. Tấm này được mà."

    "Hoàng nhìn ảnh."

    hoang neutral "Ừ. Giữ đi."

    $ story_flag("tam_huyen_hoang_recreate_first_photo")

    return
