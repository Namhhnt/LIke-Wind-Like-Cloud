# FILE: game/story/tam/tam_c05_sunday_date/s01_route_check.rpy
# Opens the anniversary morning from the correct POV.
# Route selection has already happened in C04/H01.

label tam_c05_sunday_date_s01_route_check:
    $ _anniversary_route = story_state.get("hoang_anniversary_route", "friend_group")

    scene black
    with fade

    centered "{size=46}CHAPTER 05{/size}\n{size=30}Buổi hẹn Chủ Nhật{/size}"

    scene black
    with dissolve

    # Compatibility fallback for old/debug saves that enter C05 directly.
    if _anniversary_route not in ("tam", "huyen", "friend_group"):
        if story_has_flag("romance_hoang_tam_confirmed"):
            $ _anniversary_route = "tam"
        elif story_has_flag("romance_hoang_huyen_confirmed"):
            $ _anniversary_route = "huyen"
        else:
            $ _anniversary_route = "friend_group"

        $ story_state["hoang_anniversary_route"] = _anniversary_route

    if _anniversary_route == "tam":
        call tam_c05_sunday_date_s01_tam_morning

    elif _anniversary_route == "huyen":
        call tam_c05_sunday_date_s01_huyen_morning

    else:
        call tam_c05_sunday_date_s01_group_morning

    return


label tam_c05_sunday_date_s01_tam_morning:
    scene bg_tam_room_morning
    with fade

    "Sáu giờ mười hai phút sáng Chủ Nhật."

    scene cg_tam_c05_tam_morning
    with dissolve
    "Tâm đứng trước tủ quần áo, tay giữ một chiếc váy màu cam hồng nhạt."
    scene bg_tam_room_morning
    with dissolve

    "Trên giường đã có ba bộ khác."

    "Một chiếc áo nằm dưới sàn."

    "Cánh tủ bên phải còn mở."

    "Nếu nhìn riêng từng thứ thì chẳng có gì đáng nói."

    "Đặt tất cả vào căn phòng vốn luôn gọn gàng của Tâm, chúng bắt đầu giống bằng chứng."

    "Hoàng sẽ đến lúc bảy giờ bốn mươi lăm."

    "Cô đã chọn xong từ mười phút trước."

    "Vẫn chưa thay."

    if story_state.get("tam_insecurity", 0) >= 45:
        "Tâm ướm chiếc váy lên người thêm lần nữa."

        "Nó không có gì sai."

        "Chỉ là trong đầu cô lần lượt xuất hiện những cô gái từng đứng cạnh Hoàng ở các buổi tiệc."

        "Cao hơn."

        "Ăn mặc đẹp hơn."

        "Tự nhiên hơn khi khoác tay anh."

        "Tâm nhìn mình trong gương."

        "Rồi nhìn đống quần áo sau lưng."

        tam irritated "Đừng làm quá."

        "Câu nói nghe khá giống Huyền."

        "Tác dụng cũng tương đương."

    elif story_state.get("tam_insecurity", 0) >= 25:
        "Tâm xoay sang trái."

        "Rồi sang phải."

        "Cô biết bộ này hợp."

        "Điều cô chưa biết là hôm nay Hoàng định làm gì để phải nhắn một câu bí mật đến thế."

        "Ba tháng hẹn hò chưa đủ khiến anh trở thành người dễ đoán."

        "Chỉ đủ khiến cô biết khi nào anh đang cố tỏ ra mình không hồi hộp."

    else:
        "Tâm đặt chiếc váy lên thành ghế."

        "Cô không cần thử thêm."

        "Hoàng đã nhìn thấy cô trong váy công sở, áo thun cũ, tóc rối và cả những buổi chiều mắt mệt đến mức chẳng muốn nói."

        "Một ngày đặc biệt không cần một phiên bản khác của cô."

        "Chỉ cần cô đến."

    menu:
        "Tâm quyết định..."

        "Mặc bộ khiến mình thấy thoải mái nhất":
            "Tâm lấy lại bộ đầu tiên."

            "Màu nhẹ."

            "Vừa đủ đẹp."

            "Và quan trọng nhất, cô không phải kéo vạt áo xuống mỗi khi ngồi."

            $ story_add("tam_self_clarity", 5)
            $ story_add("tam_insecurity", -5)
            $ story_flag("tam_anniversary_dresses_for_herself")

        "Giữ chiếc váy nổi bật hơn":
            "Tâm chọn chiếc váy cam hồng."

            "Không phải vì cần Hoàng bất ngờ."

            "Nhưng nếu anh có bất ngờ một chút, cô cũng không phản đối."

            $ story_add("tam_hoang_interest", 5)
            $ story_flag("tam_anniversary_dresses_for_hoang")

        "Nhắn Huyền hỏi ý kiến":
            "Tâm chụp hai tấm ảnh trước gương."

            "Cô gửi sang cho Huyền."

            tam "Bộ nào ổn hơn?"

            "Tin nhắn được xem gần như ngay lập tức."

            huyen "Bên trái."

            "Ba giây sau."

            huyen "Không. Bên phải."

            "Thêm năm giây."

            huyen "Thôi mặc bộ đầu tiên đi."

            tam "Sao lại bộ đầu tiên?"

            huyen "Đằng nào ông ấy cũng chỉ nhìn mặt bà."

            "Tâm nhìn câu trả lời."

            "Tai cô nóng lên hơi vô lý."

            tam "Cậu dậy từ bao giờ thế?"

            huyen "Tôi chưa ngủ."

            "Dòng trạng thái của Huyền chuyển sang offline."

            $ story_flag("tam_asks_huyen_before_anniversary")
            $ story_add("tam_insecurity", -5)

    "Bảy giờ ba mươi tám."

    "Tâm vừa cài xong khuy tay áo thì điện thoại sáng lên."

    if story_has_flag("hoang_invitation_tam_direct"):
        hoang "Anh đang dưới nhà."

        "Không có dấu chấm."

        "Không có câu hỏi."

        "Rất Hoàng."

    elif story_has_flag("hoang_invitation_tam_overplanned"):
        hoang "Anh đến rồi. Trời không mưa. Lịch vẫn như cũ."

        "Tâm đọc lại câu cuối."

        tam smile "Anh đúng là đã lập lịch thật."

    elif story_has_flag("hoang_invitation_tam_fragile_honest"):
        hoang "Anh đến rồi."

        "Chỉ ba chữ."

        "Tâm nhớ câu anh đã nhắn mấy hôm trước."

        "Ừ. Anh muốn gặp em."

        "Cô đặt điện thoại lên bàn, nhìn mình lần cuối trong gương."

        "Lần này không sửa gì nữa."

    else:
        hoang "Anh đang đợi dưới sảnh."

    "Tâm cầm túi, đi được hai bước rồi quay lại."

    "Cô nhét nhanh một thỏi son vào ngăn nhỏ."

    "Sau đó khép cánh tủ."

    "Một tay áo vẫn mắc ngoài khe."

    "Tâm nhìn thấy."

    "Cô quyết định để tối về xử lý."

    return


label tam_c05_sunday_date_s01_huyen_morning:
    scene bg_bed_room_01_morning
    with fade

    "Bảy giờ ba mươi tám."

    scene cg_tam_c05_huyen_morning
    with dissolve
    "Huyền mở mắt vì điện thoại rung lần thứ hai."
    scene bg_bed_room_01_morning
    with dissolve

    "Tin nhắn của Hoàng nằm ngay trên màn hình."

    hoang "Bảy giờ bốn mươi lăm."

    "Cô nhìn đồng hồ."

    "Rồi nhìn bộ quần áo đã được đặt sẵn trên ghế từ tối qua."

    huyen neutral "Tiện tay lấy ra thôi."

    "Không ai ở trong phòng để nghe."

    "Đỡ phải giải thích."

    "Tóc cô chưa chải."

    "Điện thoại đã đầy pin."

    "Pin dự phòng cũng đầy."

    "Một người hoàn toàn không chuẩn bị cho buổi hẹn thường vẫn làm vậy."

    if story_has_flag("hoang_invitation_huyen_direct"):
        "Tin nhắn trước đó của Hoàng vẫn còn ở phía trên."

        hoang "Chủ Nhật đi với anh."

        "Không nói đi đâu."

        "Không nói Tâm có đi không."

        "Cũng không để lại nhiều chỗ cho Huyền giả vờ rằng đây chỉ là một buổi tụ tập bình thường."

    elif story_has_flag("hoang_invitation_huyen_personal"):
        "Hoàng đã nói tìm được một chỗ cô sẽ thích."

        "Câu đó nguy hiểm ở chỗ nó cho thấy anh đã nghĩ đến cô trước khi nghĩ đến địa điểm."

        "Huyền không định phân tích."

        "Cô đã phân tích xong từ tối qua."

    elif story_has_flag("hoang_invitation_huyen_corrected_honestly"):
        "Cô nhớ mình từng hỏi Tâm có đi không."

        "Hoàng trả lời: Không. Anh đang mời em."

        "Một câu đơn giản."

        "Đủ khiến cô mất gần mười phút để chọn một đôi giày."

    menu:
        "Huyền..."

        "Mặc đúng bộ đã chuẩn bị":
            "Huyền thay đồ rất nhanh."

            "Chiếc áo không quá cầu kỳ."

            "Nhưng là chiếc Hoàng từng nhìn lâu hơn bình thường rồi nói màu này hợp cô."

            "Cô nhớ."

            "Tất nhiên chỉ vì trí nhớ tốt."

            $ story_add("huyen_hoang_interest", 5)
            $ story_flag("huyen_anniversary_keeps_prepared_outfit")

        "Đổi sang bộ casual an toàn hơn":
            "Huyền cầm chiếc áo đã chuẩn bị."

            "Rồi cất lại."

            "Cô thay áo phông, khoác sơ-mi mỏng bên ngoài."

            "Đủ đẹp để ra ngoài."

            "Không đủ để ai kết luận cô đã coi hôm nay là một buổi hẹn."

            $ story_flag("huyen_anniversary_plays_it_safe")

        "Nhắn Tâm hỏi vòng":
            huyen "Này. Hôm nay bà có lịch gì không?"

            "Tâm trả lời sau vài giây."

            tam "Có việc riêng."

            huyen "Với ai?"

            tam "Không phải Hoàng."

            "Huyền nhìn ba chữ cuối."

            huyen "Tôi có hỏi đâu."

            tam "Ừ."

            tam "Cậu cũng chưa hỏi vì sao mình hỏi."

            "Huyền tắt màn hình."

            huyen irritated "Bạn bè kiểu gì."

            "Khóe môi cô vẫn cong lên."

            $ story_flag("huyen_confirms_private_date_through_tam")
            $ story_add("huyen_hoang_interest", 5)

    "Bảy giờ bốn mươi bốn."

    "Chuông cửa dưới sảnh vang lên."

    hoang "Anh đến rồi."

    "Huyền nhìn mái tóc còn hơi rối trong gương."

    "Cô lấy dây buộc tóc."

    "Rồi đặt lại xuống bàn."

    "Có vài thứ chuẩn bị quá kỹ sẽ mất vui."

    "Cô xỏ giày, cầm điện thoại và đi ra."

    "Pin dự phòng vẫn nằm trong túi."

    return


label tam_c05_sunday_date_s01_group_morning:
    scene bg_tam_room_morning
    with fade

    "Bảy giờ bốn mươi ba."

    "Nhóm trò chuyện “Ba người trưởng thành có việc làm” sáng lên."

    hoang "Anh đang dưới nhà Tâm."

    tam "Em xuống ngay."

    huyen "Tôi mới dậy."

    hoang "Anh biết."

    huyen "Ông theo dõi tôi à?"

    hoang "Cô vừa gửi sticker chào buổi sáng lúc 7:42."

    tam "Bây giờ là 7:43."

    huyen "Hai người bắt nạt hội đồng à?"

    hoang "Mười phút."

    huyen "Mười lăm."

    hoang "Mười."

    huyen "Mười hai. Giá cuối."

    tam "Em xuống trước nhé."

    "Tâm cất điện thoại vào túi."

    "Hôm nay cô không mất nhiều thời gian chọn đồ."

    "Không phải vì ngày này không quan trọng."

    "Chỉ vì khi một buổi đi chơi có Huyền, mọi kế hoạch ăn mặc đều có nguy cơ kết thúc bằng việc ngồi xổm bên vỉa hè ăn thứ gì đó dính sốt."

    scene bg_taxi_interior_day
    with dissolve

    "Mười một phút sau, Tâm đã ngồi trong xe Hoàng."

    "Huyền gửi thêm một tin."

    huyen "Xuống rồi."

    "Hoàng nhìn đồng hồ."

    hoang neutral "Mười ba phút."

    tam smile "Ít hơn dự đoán."

    "Hai người nhìn về phía cửa chung cư."

    "Huyền chạy ra, một tay giữ túi, tay kia buộc tóc."

    "Cô mở cửa sau."

    huyen irritated "Sao bà ngồi ghế trước?"

    tam confused "Tớ xuống trước."

    huyen "Lý do yếu."

    hoang "Cô muốn lái không?"

    huyen "Không."

    hoang "Thế lên xe."

    "Huyền ngồi xuống."

    "Cửa xe đóng lại."

    scene cg_tam_c05_group_morning
    with dissolve
    "Ba người nhìn nhau qua gương chiếu hậu."
    scene bg_taxi_interior_day
    with dissolve

    huyen smile "Rồi. Kỷ niệm một năm bắt đầu ở đâu?"

    hoang "Ăn sáng."

    huyen "Tốt."

    tam "Cậu chưa ăn à?"

    huyen "Tôi đã hy sinh bữa sáng ở nhà vì tình bạn."

    hoang "Cô mới dậy."

    huyen "Đừng phá ý nghĩa câu chuyện."

    $ story_flag("tam_huyen_hoang_anniversary_morning_started")

    return
