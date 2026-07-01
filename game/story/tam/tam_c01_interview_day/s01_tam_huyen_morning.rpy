# FILE: game/story/tam/tam_c01_interview_day/s01_tam_huyen_morning.rpy
# Scene file.

label tam_c01_interview_day_s01_tam_huyen_morning:
    scene bg_tam_room_morning
    with fade

    "Buổi sáng hôm ấy, Tâm thức dậy trước chuông báo thức năm phút."

    "Chiếc điện thoại nằm úp trên bàn, bên cạnh một tập portfolio đã được cô kiểm tra đến mức mép giấy hơi cong lên."

    tam tired "Mình đúng là rảnh thật..."

    "Cô nói vậy, nhưng vẫn kéo tập hồ sơ lại gần."

    "Ảnh dự án. CV. Thư giới thiệu. Bản in dự phòng."

    "Tất cả đều đủ."

    "Vậy mà ngón tay cô vẫn dừng lại ở chiếc kẹp giấy đầu tiên. Nó hơi lệch."

    tam neutral "..."

    "Tâm tháo ra, kẹp lại."

    "Lần này ngay hơn một chút."

    "Chuông cửa reo đúng lúc cô vừa bỏ tập hồ sơ vào túi."

    huyen happy "Tâm ơi, mở cửa. Tao đến cứu đời mày đây."

    tam confused "Cứu gì?"

    huyen teasing "Cứu khỏi việc mày tự soi CV đến mức nhà tuyển dụng chưa kịp đánh giá thì giấy đã mòn trước."

    "Tâm mở cửa."

    "Huyền đứng ngoài hành lang, tay cầm hai ly cà phê giấy. Mái tóc buộc vội, cổ áo sơ mi lệch một bên."

    "Trông cô giống người vừa chạy khỏi một trận chiến nhỏ với chính cái tủ quần áo của mình."

    tam smile "Cổ áo."

    huyen surprised "Hả?"

    "Tâm đưa tay chỉnh lại cổ áo cho Huyền."

    huyen embarrassed "À... biết rồi. Đừng nhìn tao kiểu đó."

    tam teasing "Kiểu nào?"

    huyen "Kiểu 'người này lát nữa đi phỏng vấn thật à'."

    tam happy "Tao chưa nói gì mà."

    huyen irritated "Nhưng mặt mày nói rồi."

    "Huyền đặt một ly cà phê lên bàn, rồi đảo mắt nhìn căn phòng."

    huyen neutral "Hồ sơ đâu?"

    tam neutral "Trong túi."

    huyen "Portfolio?"

    tam "Trong túi."

    huyen "Bản in dự phòng?"

    tam "Cũng trong túi."

    huyen "Tinh thần?"

    tam "Chắc... để quên đâu đó."

    "Huyền im một nhịp."

    "Rồi cô bật cười."

    huyen laughing "Ổn. Ít nhất vẫn còn biết đùa. Chưa chết."

    tam shy "Mày mới là người cổ áo còn lệch đấy."

    huyen teasing "Đó là phong cách. Người thường không hiểu được."

    "Tâm cười khẽ."

    "Cô cầm ly cà phê lên, nhưng không uống ngay. Hơi nóng chạm vào đầu ngón tay, làm cô tỉnh hơn một chút."

    huyen neutral "Mày có lo không?"

    tam neutral "Có."

    huyen "Nhiều không?"

    tam "Vừa đủ để không làm mất mặt bản thân."

    huyen smile "Câu trả lời nghe như đi phỏng vấn rồi."

    tam smile "Tập trước."

    "Huyền ngồi xuống mép giường, ôm ly cà phê bằng hai tay."

    "Lần này đến lượt Tâm nhìn ra chỗ lệch."

    "Không phải cổ áo."

    "Là ngón cái Huyền đang miết liên tục lên mép nắp ly."

    menu:
        "What does Tâm prioritize before the interview?"

        "Calm Huyền down":
            $ story_add('career_huyen', 1)
            $ story_flag('tam_supports_huyen')

            tam neutral "Mày cũng lo đúng không?"

            huyen surprised "Ai? Tao á?"

            tam smile "Ừ. Người có phong cách cổ áo lệch."

            huyen embarrassed "..."

            "Huyền cúi nhìn ly cà phê trên tay."

            huyen tired "Một chút."

            tam neutral "Một chút của mày thường là khá nhiều."

            huyen "Đừng vạch trần bạn bè vào buổi sáng. Vô đạo đức lắm."

            tam happy "Ừ. Tao xin lỗi."

            "Tâm kéo ghế lại gần, mở túi, lấy ra một bản CV của Huyền."

            tam neutral "Tao xem qua rồi. Phần kinh nghiệm thực tập của mày ổn. Phần teamwork cũng ổn. Nếu họ hỏi về điểm yếu, đừng nói 'quá cầu toàn'."

            huyen confused "Sao?"

            tam teasing "Nghe giả."

            huyen laughing "Khó tính thế."

            tam smile "Nói thật hơn đi. Ví dụ mày hay ôm việc, nhưng đang học cách chia task rõ hơn."

            huyen neutral "Nghe cũng giống tao."

            tam "Vì đúng là mày."

            "Huyền im vài giây, rồi thở ra."

            huyen smile "Rồi. Tự nhiên thấy đỡ hơn một chút."

            tam "Ừ. Vậy uống cà phê đi. Tay mày sắp bóp nát cái nắp rồi."

            huyen embarrassed "..."

        "Review the portfolio again":
            $ story_add('career_tam', 2)

            "Tâm kéo túi về phía mình, lấy tập portfolio ra lần nữa."

            huyen bored "Lại nữa à?"

            tam neutral "Một lần cuối."

            huyen teasing "Mày nói câu đó từ tối qua."

            tam "Lần cuối của sáng nay."

            "Huyền nhìn cô vài giây rồi chịu thua, ngồi xích lại."

            huyen neutral "Được. Cho tao xem."

            "Hai cô gái cúi đầu bên tập giấy."

            "Tâm không đọc lại từng dòng. Cô chỉ kiểm tra thứ tự trang, chỗ dán ảnh, phần ghi chú ngắn dưới mỗi dự án."

            "Đến trang cuối, cô dừng lại."

            "Một dấu mực nhỏ nằm ở góc dưới."

            huyen confused "Cái đó ai nhìn thấy được?"

            tam neutral "Tao."

            huyen "Nhà tuyển dụng đâu phải mày."

            tam "Nhưng người đi phỏng vấn là tao."

            "Huyền há miệng định phản bác, rồi lại ngậm vào."

            "Cũng có lý. Hơi phiền, nhưng có lý."

            huyen smile "Thôi được. Lau đi, nữ hoàng chi tiết."

            tam shy "Đừng gọi tao thế."

            huyen teasing "Vâng, nữ hoàng."

        "Hide her nervousness with a joke":
            $ story_add('tam_self_clarity', 1)

            tam neutral "Tao nghĩ nếu phỏng vấn hỏng, mình vẫn có thể mở quán cà phê."

            huyen confused "Gì cơ?"

            tam smile "Tên quán là 'Hai người trượt phỏng vấn'. Slogan: thất nghiệp nhưng thơm mùi rang xay."

            huyen "..."

            huyen laughing "Ý tưởng tệ đến mức tao thấy tỉnh hẳn."

            tam teasing "Hiệu quả là được."

            huyen smile "Mày đang run à?"

            tam neutral "Không."

            "Tâm nhấc ly cà phê lên."

            "Nắp ly chạm nhẹ vào răng."

            "Cạch."

            huyen teasing "Ừ. Không run. Ly tự run."

            tam embarrassed "Do cà phê nóng."

            huyen "Tao chưa hỏi nguyên nhân."

            "Hai người nhìn nhau."

            "Rồi cùng bật cười."

    scene bg_apartment_lobby_morning
    with dissolve

    "Bảy giờ bốn mươi."

    "Hai cô gái đứng trong sảnh chung cư, mỗi người ôm một tập hồ sơ."

    "Gương thang máy phản chiếu hai gương mặt đã cố tỏ ra bình tĩnh."

    huyen neutral "Mày thấy tao ổn chưa?"

    tam smile "Ổn."

    huyen "Không nói dối?"

    tam "Có trang điểm nhẹ nên nếu nói dối cũng khó phát hiện."

    huyen irritated "Tâm."

    tam laughing "Ổn thật."

    "Cửa thang máy mở ra."

    "Tâm bước vào trước, rồi giữ cửa cho Huyền."

    "Một buổi sáng bình thường."

    "Chỉ có quai túi trên vai cô hơi siết vào lòng bàn tay."

    scene bg_company_lobby_morning
    with dissolve

    "Tòa nhà công ty hiện ra sau lớp kính lớn của sảnh chính."

    "Máy lạnh trong lobby thổi ra một luồng khí khô và lạnh. Mùi nước lau sàn mới còn vương rất nhẹ."

    "Huyền dừng lại trước quầy lễ tân, hít một hơi sâu."

    huyen neutral "Tới rồi."

    tam neutral "Ừ."

    huyen "Không chạy nữa nhé?"

    tam smile "Mày nói mày hay tao?"

    huyen "Cả hai."

    "Tâm nhìn cửa kính trước mặt."

    "Bên trong, vài ứng viên khác đã ngồi chờ. Ai cũng ăn mặc chỉnh tề, tay đặt trên hồ sơ như sợ chỉ cần buông ra thì sự tự tin cũng rơi theo."

    tam neutral "Vào thôi."

    huyen smile "Ừ. Vào thôi."

    $ unlock_library_character("huyen")
    $ unlock_character_section("huyen", "core_traits")
    $ unlock_character_section("tam", "narrative_function")
    return