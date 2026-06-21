# Chapter 01, Scene 01

label tam_c01:

    scene black
    with fade

    narrator "Chương 01"
    narrator "Ngày Đầu Tiên Gió Đổi Chiều"

    scene bg_tam_room_morning
    with dissolve

    narrator "Buổi sáng hôm ấy, Tâm thức dậy sớm hơn báo thức mười phút."

    narrator "Ngoài cửa sổ, thành phố còn chưa hẳn tỉnh. Một lớp sáng mỏng phủ lên những mái nhà san sát, lặng lẽ như ai đó vừa kéo rèm cho một ngày mới."

    narrator "Trên bàn học của cô là một tập hồ sơ đã được kẹp ngay ngắn. CV. Đơn ứng tuyển. Một bản photo bằng tốt nghiệp. Vài chứng chỉ nhỏ không chắc có giúp ích gì không, nhưng bỏ ra thì lại thấy thiếu."

    narrator "Tâm nhìn chúng rất lâu."

    tam thoughtful "Phòng triển khai dự án..."

    narrator "Tên vị trí nghe không quá xa lạ. Nhưng công ty thì khác."

    narrator "Một công ty đầu tư đa ngành. Có xây dựng. Có vật liệu. Có phòng IT. Có pháp lý. Có kế toán. Có quản lý chất lượng. Có cả những phòng ban mà chỉ đọc tên thôi Tâm đã thấy mình cần thêm một tách cà phê để không bỏ cuộc giữa chừng."

    narrator "Cô không phải kiểu người sợ việc khó."

    narrator "Chỉ là cô hơi sợ những thứ mình chưa nắm rõ."

    play sound "audio/phone_vibrate.ogg"

    narrator "Điện thoại rung lên trên mặt bàn."

    huyen smile "Dậy chưa bà nội?"

    tam dazed "Dậy rồi."

    huyen pouty "Tốt. Tao đang ở dưới nhà mày. Xuống đi. Nếu để tao đi phỏng vấn một mình, tao sẽ trù mày được nhận vào phòng kế toán và phải làm bảng lương đến hết đời."

    tam smile "Mày ác vừa thôi."

    huyen smile "Xuống nhanh. Tao mua bánh mì."

    narrator "Tâm bật cười."

    narrator "Có những người chỉ cần xuất hiện qua một dòng tin nhắn, không khí trong lòng người khác đã bớt nặng đi một chút."

    scene bg_apartment_lobby_morning
    with dissolve

    narrator "Huyền đứng ở sảnh chung cư, một tay cầm hai ổ bánh mì, tay kia ôm túi hồ sơ trước ngực như ôm phao cứu sinh."

    huyen sad "Tao nói thật nhé, tim tao đang đập như chạy deadline cuối quý."

    tam smile "Mày cũng biết sợ cơ à?"

    huyen smile "Tao biết sợ chứ. Tao chỉ giấu giỏi hơn mày thôi."

    narrator "Tâm nhận ổ bánh mì từ tay Huyền. Còn nóng. Giấy gói thấm một chút dầu, mùi pate và rau mùi bốc lên giản dị đến mức làm người ta thấy cuộc đời vẫn còn cứu được."

    huyen neutral "Này, lát nữa nếu người ta hỏi vì sao muốn vào phòng triển khai dự án, mày định nói gì?"

    tam thoughtful "Tao vẫn đang nghĩ."

    huyen pouty "Vậy là chưa nghĩ xong."

    tam embarrassed "Tao nghĩ rồi. Chỉ là chưa sắp xếp được."

    huyen smile "Đấy. Khác gì chưa nghĩ xong đâu."

    narrator "Tâm im lặng một chút. Huyền liếc cô, ánh mắt vừa trêu vừa thật sự quan tâm."

    menu:
        "Tâm nên đáp lại Huyền thế nào?"

        "Thừa nhận mình cũng lo, rồi rủ Huyền cùng rà lại ý chính.":
            $ huyen_trust += 1
            $ add_unique(progress["player_flags"], "tam_huyen_shared_anxiety")
            tam sad "Ừ, tao cũng lo. Hay trên đường đi mình rà lại với nhau một lượt đi. Mày nghe giúp tao xem có chỗ nào ngớ ngẩn không."
            huyen happy "Được đấy. Ít ra hôm nay tao có cảm giác mình là bạn thân chứ không phải NPC phát bánh mì."

        "Tỏ ra tự tin để Huyền bớt lo.":
            tam smile "Không sao đâu. Tao nghĩ vào đó ứng biến được."
            huyen serious "Nghe thì cũng ngầu đấy. Nhưng tao ghét nhất chữ ứng biến trước phỏng vấn."
            narrator "Huyền nói vậy, nhưng cũng không ép thêm."

        "Bảo Huyền đừng làm mình căng thẳng thêm.":
            $ huyen_trust -= 1
            tam sad "Mày đừng hỏi nữa. Tao đang cố không căng thẳng đây."
            huyen sad "Ờ... xin lỗi."
            narrator "Câu trả lời rơi xuống giữa hai người hơi cụt. Không nặng nề. Chỉ là hơi lạnh đi một nhịp."

    scene bg_company_lobby_morning
    with fade

    narrator "Công ty nằm trong một tòa nhà văn phòng lớn, mặt kính sáng đến mức Tâm nhìn thấy bóng mình phản chiếu trên đó."

    narrator "Áo sơ-mi trắng. Chân váy tối màu. Tóc buộc gọn sau gáy. Một vẻ ngoài vừa đủ nghiêm túc, vừa đủ trẻ để người ta không đoán chắc cô đã thật sự sẵn sàng bước vào một guồng máy lớn."

    narrator "Ở quầy lễ tân, Huyền ghé sát tai cô."

    huyen smile "Tao vừa thấy một anh đi qua đeo thẻ phòng pháp lý. Mặt lạnh như văn bản từ chối thanh toán."

    tam smile "Mày đừng làm tao cười."

    huyen happy "Cười cho bớt run. Khoa học chưa chứng minh nhưng tao chứng minh bằng kinh nghiệm cá nhân rồi."

    narrator "Tâm mím môi, nhưng khóe miệng vẫn không nhịn được cong lên."

    scene bg_interview_waiting_room
    with dissolve

    narrator "Phòng chờ phỏng vấn yên tĩnh."

    narrator "Trên tường treo những bức ảnh về công trình, nhà máy vật liệu, một khu văn phòng đang thi công, và vài màn hình dashboard nội bộ hiện những con số mà Tâm chưa kịp hiểu."

    narrator "Có lẽ đây không phải một nơi chỉ cần biết gõ văn bản và gửi email."

    narrator "Càng nhìn, Tâm càng hiểu vị trí mình ứng tuyển nằm ở giữa rất nhiều dòng chảy."

    narrator "Tiến độ. Hồ sơ. Vật tư. Pháp lý. Chi phí. Chất lượng. Con người."

    narrator "Một mắt xích nhỏ, nhưng nếu lệch, rất nhiều thứ phía sau cũng lệch theo."

    play sound "audio/door_open.ogg"

    hr "Bạn Tâm, mời em vào phòng."

    narrator "Tâm đứng dậy."

    narrator "Huyền ngồi bên cạnh khẽ giơ nắm tay."

    huyen happy "Cố lên. Đừng bán đứng tao."

    tam smile "Tao vào phỏng vấn chứ có vào phòng thẩm vấn đâu."

    huyen confused "Khác nhau ở chỗ nào?"

    narrator "Tâm bật cười rất khẽ, rồi bước vào."

    scene bg_interview_room
    with dissolve

    interviewer "Chào em. Em cứ ngồi thoải mái."

    manager "Bọn anh đã xem qua hồ sơ của em. Vị trí triển khai dự án bên anh không chỉ làm giấy tờ. Nó cần phối hợp với nhiều phòng ban. Em hiểu công việc này như thế nào?"

    narrator "Câu hỏi đến sớm hơn Tâm tưởng."

    narrator "Cô đặt hai tay lên đùi, ngón cái khẽ miết vào nhau."

    narrator "Đây không phải lúc để nói lan man."

    narrator "Cô cần sắp xếp ý."

    jump tam_c01_speech_game
