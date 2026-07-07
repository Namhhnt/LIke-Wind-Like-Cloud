# FILE: game/story/tam/tam_c01_interview_day/s01_tam_huyen_morning.rpy
# Scene file.

label tam_c01_interview_day_s01_tam_huyen_morning:
    scene bg_tam_room_morning
    with fade

    "Buổi sáng hôm ấy, Tâm thức dậy trước chuông báo thức năm phút."

    "Ngày hôm nay có buổi phỏng vấn quan trọng. Cô không muốn để bản thân bị cuốn vào những giấc mơ mơ hồ, hay những cảm giác khó hiểu."

    "Chiếc điện thoại nằm úp trên bàn, bên cạnh một tập portfolio đã được cô kiểm tra đến mức mép giấy hơi cong lên."

    "Cô cầm điện thoại lên, mở màn hình."

    "Một email mới hiện ra ở đầu hộp thư."

    "{i}Interview Invitation — October 12th (Friday){/i}"

    "Tâm mở email ra đọc lại dù đã biết nội dung từ hôm qua."

    "{i}We are pleased to invite you to an interview for the Junior Staff position...{/i}"

    "{i}Date: Friday, October 12th — 9:00 AM{/i}"

    "Cô đọc đến dòng thứ ba thì dừng, không phải vì có gì mới, mà vì nhìn thấy giờ giấc in đậm ở giữa màn hình."

    "Thứ Sáu, ngày 12 tháng 10."

    "Chín giờ sáng."

    "Cô tắt màn hình, đặt điện thoại ngửa lên bàn."

    "Đây là email đầu tiên cô nhận được từ công ty."

    "Và cũng là thứ duy nhất mở đầu cho một ngày mà cô không thể đoán trước kết thúc."


    tam tired "Mình đúng là rảnh thật..."

    "Cô nói vậy, nhưng vẫn kéo tập hồ sơ lại gần."

    "Ảnh dự án. CV. Thư giới thiệu. Bản in dự phòng."

    "Tất cả đều đủ."

    "Vậy mà ngón tay cô vẫn dừng lại ở chiếc kẹp giấy đầu tiên. Nó hơi lệch."

    tam neutral "..."

    "Tâm tháo ra, kẹp lại."

    "Lần này ngay ngắn hơn một chút."

    "Chuông cửa reo đúng lúc cô vừa bỏ tập hồ sơ vào túi."

    scene bg_tam_living_room_morning
    with dissolve

    huyen happy "Tâm ơi, mở cửa. Tao đến giải cứu mày đây."

    tam confused "Cứu cái gì?"

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

    tam happy "Tao chưa nói gì nhá."

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

    "Huyền ngồi xuống sofa, ôm ly cà phê bằng hai tay."

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

            huyen "Đừng bóc mẽ bạn bè vào buổi sáng. Vô đạo đức lắm."

            tam happy "Ừ. Tao xin lỗi."

            "Tâm ngồi lại gần, mở túi, lấy ra một bản CV của Huyền."

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

            huyen neutral "..."

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

    "Chiếc taxi lăn bánh rời khỏi khu chung cư, nhập vào dòng xe buổi sáng."

    "Ngoài cửa kính, thành phố trôi qua trong những mảng nắng còn nhạt. Tâm đặt tập hồ sơ lên đùi, còn Huyền thì tựa đầu vào ghế, cố tỏ ra bình thản."

    huyen neutral "Còn mười lăm phút nữa. Mày định dùng nó để lo lắng hay để thở?"

    tam smile "Có lựa chọn thứ ba không?"

    huyen teasing "Có. Vừa lo vừa thở. Rất tiết kiệm thời gian."

    menu:
        "What should they do on the way?"

        "Review the portfolios one last time":
            $ story_add('career_tam', 1)
            $ story_add('career_huyen', 1)

            "Tâm mở túi, kiểm tra lại thứ tự hồ sơ lần cuối."

            tam neutral "CV, portfolio, bản in dự phòng. Của mày cũng đủ rồi."

            huyen bored "Nghe như kiểm kê hàng hóa."

            tam teasing "Hàng hóa chất lượng cao."

            huyen laughing "Được. Câu đó lát nữa nhớ nói với nhà tuyển dụng."

        "Lighten up the mood":
            $ story_add('tam_self_clarity', 1)
            $ story_flag('tam_huyen_taxi_bonding')

            tam neutral "Tao nghĩ nếu cả hai cùng trượt, mình vẫn mở được quán cà phê."

            huyen confused "Lại cái quán thất nghiệp đó à?"

            tam smile "Lần này nâng cấp. Có combo CV lỗi và nước mắt rang xay."

            huyen laughing "Mày im đi. Tao mà cười trôi son là mày chịu trách nhiệm."

            "Tâm cũng bật cười."

            "Không khí trong xe nhẹ đi một chút. Vừa đủ để hai bàn tay bớt lạnh."

    "Taxi rẽ vào khu thương mại."
    scene bg_company_lobby_morning
    with dissolve

    "Tòa nhà công ty hiện ra sau bóng dáng của những tòa nhà cao tầng với cửa kính lớn."

    "Hai người trả tiền taxi, rồi bước vào sảnh."

    "Cửa kính xoay mở ra, đón hai cô gái bước vào sảnh."

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