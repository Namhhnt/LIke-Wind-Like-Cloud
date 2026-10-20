# FILE: game/story/tam/tam_c01_interview_day/s04_celebration_dinner.rpy
# Scene file.

label tam_c01_interview_day_s04_celebration_dinner:
    scene bg_luxury_restaurant_evening
    with fade

    "Buổi tối, Huyền kéo Tâm đến một nhà hàng mà theo lời cô là 'vừa đủ sang để nhớ, chưa đủ sang để khóc'."

    "Ánh đèn vàng rơi nhẹ trên mặt bàn. Khăn ăn được gấp ngay ngắn bên cạnh ly nước trong suốt."

    "Đúng kiểu nơi khiến người ta tự nhiên ngồi thẳng lưng hơn một chút."

    huyen happy "Thấy chưa? Tử tế."

    tam neutral "Tao thấy giá nước lọc ở đây cũng tử tế với chủ nhà hàng lắm."

    huyen laughing "Đừng phá mood."

    tam smile "Tao đang bảo vệ ví tiền."

    huyen teasing "Ví tiền hôm nay được phép hy sinh vì sự nghiệp."

    "Người phục vụ đặt menu xuống bàn."

    "Tâm mở ra."

    "Rồi đóng lại."

    huyen confused "Sao?"

    tam neutral "Tao cần chuẩn bị tinh thần."

    huyen "Để gọi món?"

    tam "Để đọc giá."

    huyen laughing "Trời ơi, mày làm như tao dẫn mày đi bán thận."

    tam smile "Chưa chắc."

    "Hai người cười khẽ."

    "Không khí từ sáng đến giờ cuối cùng cũng mềm xuống."

    "Không còn phòng chờ, không còn email kết quả, không còn những câu hỏi phải trả lời thật gọn."

    "Chỉ còn một chiếc bàn nhỏ, hai ly nước, và một tương lai vừa mở ra vừa khiến người ta hơi sợ."

    huyen neutral "Mày nghĩ đi làm rồi sẽ thế nào?"

    tam neutral "Chắc mệt."

    huyen bored "Thực tế quá."

    tam "Cũng vui."

    huyen "Thêm đi."

    tam "Có tiền."

    huyen happy "Đúng. Đây mới là trọng tâm."

    "Tâm bật cười, cầm ly nước lên."

    tam smile "Chúc mừng chúng ta?"

    huyen smile "Chúc mừng chúng ta."

    scene cg_tam_c01_celebration_toast
    with dissolve

    "Hai chiếc ly chạm nhẹ vào nhau."

    "Một âm thanh rất nhỏ."

    "Nhưng đủ làm buổi tối này có hình dạng riêng."

    scene cg_tam_c01_hoang_window
    with dissolve

    "Ở phía bên kia nhà hàng, một chàng trai trẻ ngồi một mình ở chiếc bàn gần khung cửa sổ."

    "Ánh đèn không chiếu thẳng vào mặt anh."

    "Từ vị trí của Tâm và Huyền, người ta chỉ thấy một dáng ngồi khá thẳng, bàn tay đặt hờ bên ly rượu, và ánh mắt thỉnh thoảng dừng lại ở khoảng không ngoài cửa kính."

    "Trước mặt anh là một phần ăn gần như chưa động đến."

    "Người phục vụ đi qua, khẽ hỏi gì đó."

    hoang_unknown neutral "Không sao. Cứ để thêm một lúc."

    "Giọng anh thấp, lịch sự, không gây chú ý."

    scene bg_luxury_restaurant_evening
    with dissolve

    "Nhưng khi Tâm và Huyền cụng ly lần nữa, anh hơi nghiêng đầu nhìn sang."

    "Có lẽ vì tiếng cười của Huyền."

    "Cũng có thể vì nụ cười của Tâm dưới ánh đèn vàng trông sáng hơn phần còn lại của căn phòng."

    menu:
        "Who notices Hoàng first?"

        "Tâm":
            $ story_add('tam_hoang_interest', 1)
            $ story_flag('tam_notices_hoang_first')

            "Tâm là người nhìn thấy anh trước."

            "Không phải vì cô cố ý quan sát."

            "Chỉ là khi đặt ly xuống, mắt cô vô tình đi qua khung cửa sổ bên kia."

            "Người đàn ông trẻ kia cũng vừa nhìn sang."

            "Hai ánh mắt chạm nhau trong một thoáng rất ngắn."

            "Tâm hơi khựng lại."

            "Anh không cười hẳn."

            "Chỉ nâng ly lên rất nhẹ, như một lời chúc mừng gửi nhầm nhưng vẫn đủ lịch sự để nhận."

            tam surprised "..."

            huyen confused "Gì đấy?"

            tam embarrassed "Không có gì."

            huyen teasing "Không có gì mà mặt hơi đỏ à?"

            tam "Đèn vàng."

            huyen "Ừ. Đèn vàng biết chọn người ghê."

            "Tâm cúi xuống nhìn đĩa ăn."

            "Một người xa lạ."

            "Chỉ vậy thôi."

            "Nhưng không hiểu sao, cái cách anh nâng ly vừa đủ kia khiến cô nhớ lâu hơn mức cần thiết."

        "Huyền":
            $ story_add('huyen_hoang_interest', 1)
            $ story_flag('huyen_notices_hoang_first')

            "Huyền là người phát hiện ra anh trước."

            "Cô đang định gọi thêm món tráng miệng thì bỗng dừng lại, mắt liếc qua vai Tâm."

            huyen neutral "Ê."

            tam confused "Sao?"

            huyen teasing "Bàn bên kia có trai đẹp."

            tam embarrassed "Mày nhỏ tiếng thôi."

            huyen "Tao nói sự thật bằng âm lượng rất văn minh."

            tam "Huyền."

            "Huyền chống cằm, nhìn như đang đánh giá một món trang trí nội thất đắt tiền."

            huyen neutral "Ngồi một mình. Ăn ít. Uống rượu. Nhìn cửa sổ. Chín mươi phần trăm là thất tình."

            tam confused "Mười phần trăm còn lại?"

            huyen grinning "Nhân vật nam bí ẩn trong truyện ngôn tình."

            tam laughing "Mày đúng là hết cứu."

            huyen "Cảm ơn."

            "Như cảm nhận được ánh nhìn quá lâu, người đàn ông kia nghiêng mắt sang."

            "Huyền lập tức quay lại, tỉnh bơ cầm ly nước."

            huyen neutral "Không tệ."

            tam "Mày vừa bị bắt gặp đấy."

            huyen "Không. Tao đang nghiên cứu thị trường."

            tam teasing "Thị trường gì?"

            huyen smile "Thị trường trai đẹp thành phố."

            "Tâm lắc đầu."

            "Cô không nhìn sang."

            "Nhưng cái tên chưa biết mặt ấy đã kịp bước vào câu chuyện tối nay theo cách rất Huyền: ồn ào, vô tội, và hơi đáng ngờ."

        "Neither of them pays much attention":
            $ story_add('career_tam', 1)

            "Không ai trong hai người thật sự để ý đến anh."

            "Tâm đang bận nghe Huyền kể lại khoảnh khắc cô suýt trả lời sai câu hỏi về teamwork."

            "Huyền kể đến đâu tự diễn đến đó."

            huyen frustrated "Lúc đó tao thật sự muốn nói là 'em teamwork tốt trừ khi teammate quá báo'. Nhưng may quá, tao còn chút lý trí."

            tam laughing "Chút đó cứu mày."

            huyen happy "Đúng. Hôm nay phải cảm ơn chút lý trí."

            "Tâm cười đến mức phải đặt đũa xuống."

            "Ở bàn bên kia, người đàn ông trẻ lặng lẽ nhìn sang."

            "Anh nghe không rõ họ nói gì."

            "Chỉ thấy hai cô gái vừa được một tin vui nào đó, vừa cố tỏ ra người lớn, vừa thất bại khá đáng yêu."

            "Anh nâng ly lên một chút."

            "Không ai nhìn thấy."

            "Cũng không sao."

            "Có những lời chúc vốn chỉ cần người gửi biết là đủ."

    "Bữa tối kéo dài hơn dự định."

    "Họ gọi thêm món tráng miệng."

    "Huyền chụp ảnh hai ly nước, một đĩa bánh, rồi bắt Tâm giơ tay tạo dáng với email trúng tuyển trên màn hình điện thoại."

    tam embarrassed "Xấu hổ quá."

    huyen happy "Sau này già rồi nhìn lại mới vui."

    tam "Mới nhận việc đã nói chuyện già."

    huyen "Đời công sở làm người ta trưởng thành nhanh lắm."

    tam teasing "Mày chưa đi làm ngày nào."

    huyen "Nên tao mới tranh thủ nói trước."

    "Tâm chịu thua."

    "Cô nhìn tấm ảnh vừa chụp."

    "Trong ảnh, nụ cười của cô hơi ngượng. Vai Huyền nghiêng sát vào cô. Phía sau, ánh đèn nhà hàng mờ thành từng vệt vàng nhỏ."

    "Một buổi tối bình thường."

    "Một bàn ăn nhỏ."

    "Một người xa lạ ở phía bên kia căn phòng."

    "Và một cánh cửa vừa mở ra, nhẹ đến mức lúc ấy chẳng ai biết nó sẽ dẫn mình đi xa đến đâu."

    scene bg_company_lobby_afternoon
    with fade

    "Ngày hôm sau, khi Tâm đi ngang qua công ty để nộp bổ sung giấy tờ, lobby đã khác hẳn."

    "Không còn cảm giác phỏng vấn."

    "Không còn hàng ghế chờ."

    "Chỉ còn một tòa nhà rộng, sáng, và hơi xa lạ."

    "Tâm đứng trước cửa kính vài giây."

    tam neutral "Từ tuần sau..."

    "Cô không nói hết câu."

    "Một nhân viên đi ngang qua, thẻ đeo khẽ va vào cúc áo."

    "Tâm kéo quai túi lên vai."

    "Rồi bước vào."

    $ unlock_character_section("huyen", "narrative_function")
    $ unlock_character_section("huyen", "notes")
    return
