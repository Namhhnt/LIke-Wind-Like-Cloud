# FILE: game/story/tam/tam_c02_company_party/s04_first_branch.rpy
# Scene file.

label tam_c02_company_party_s04_first_branch:
    scene bg_company_year_end_party_late
    with fade

    "Gần cuối buổi tiệc, sảnh sự kiện vơi đi một chút."

    "Nhạc nền nhỏ hơn."

    "Một vài người đã chuyển sang nói chuyện bằng giọng thật, không còn giữ nguyên nụ cười xã giao từ đầu buổi."

    "Trên bàn buffet, vài chiếc đĩa trắng nằm chồng lên nhau."

    "Một chiếc khăn giấy bị ai đó để lệch khỏi khay."

    "Tâm nhìn thấy nó."

    "Rồi không hiểu sao lại đưa tay chỉnh lại."

    huyen neutral "Mày có bệnh nghề nghiệp từ lúc nào thế?"

    tam confused "Gì?"

    huyen teasing "Khăn giấy cũng phải đúng alignment."

    tam embarrassed "Tao tiện tay thôi."

    huyen grinning "Ừ. Người ta thường bắt đầu mọi thói quen kỳ quặc bằng câu đó."

    "Tâm không cãi."

    "Cô nhìn ra phía bàn mô hình."

    "Hoàng vẫn còn ở đó."

    "Anh đang thu lại vài tấm card giới thiệu bị dư, xếp chúng thành một chồng nhỏ, mép giấy thẳng đều."

    "Tâm hơi buồn cười."

    "Có vẻ không chỉ mình cô có vấn đề với những thứ bị lệch."

    "Huyền cũng nhìn theo."

    huyen teasing "Đi chào không?"

    tam neutral "Sắp về rồi."

    huyen neutral "Thì bởi vậy mới nên chào."

    "Tâm nhìn chiếc điện thoại trong tay."

    "Màn hình sáng lên, hiện thông báo lịch làm việc ngày mai."

    "Buổi tối này không hề quyết định gì lớn."

    "Nhưng trước khi rời đi, cô vẫn có thể chọn giữ lại một điều gì đó."

    "Một liên hệ."

    "Một câu trêu."

    "Hoặc đơn giản là sức lực cho ngày làm việc tiếp theo."

    menu:
        "Tâm làm gì trước khi rời tiệc?"

        "Trao đổi liên hệ với Hoàng":
            $ story_add('tam_hoang_interest', 3)
            $ story_add('hoang_tam_trust', 5)
            $ story_add('tam_self_clarity', 1)
            $ story_add_direction('tam', 'tam_hoang_open')
            $ story_add_direction('hoang', 'hoang_tam_open')
            $ story_flag('tam_c02_exchanged_contact_with_hoang')

            "Tâm bước đến gần bàn mô hình."

            "Hoàng vừa đặt chồng card xuống. Anh nhìn lên khi thấy cô."

            hoang smile "Em vẫn còn ở đây à?"

            tam neutral "Dạ. Em chuẩn bị về."

            hoang neutral "Ừ. Cũng muộn rồi."

            "Câu chuyện có thể kết thúc ở đó."

            "Một câu chào lịch sự."

            "Một cái gật đầu."

            "Rồi mỗi người quay về chỗ của mình."

            "Tâm nhìn phần mô hình đã được tắt bớt đèn."

            "Không còn chói như lúc đầu."

            tam neutral "Nếu sau này em có câu hỏi về dự án, em có thể hỏi anh không ạ?"

            "Hoàng nhìn cô."

            "Không ngạc nhiên nhiều."

            "Chỉ như thể anh đã chờ xem cô có thật sự hỏi câu đó không."

            hoang smile "Được."

            "Anh rút một tấm card từ chồng giấy đã xếp gọn, đưa cho cô."

            hoang neutral "Trên này có email. Nhưng nếu hỏi gấp thì nhắn số này nhanh hơn."

            "Tâm nhận lấy."

            "Tấm card khá dày. Mép giấy mịn dưới đầu ngón tay."

            tam smile "Cảm ơn anh."

            hoang neutral "Không có gì."

            "Anh dừng một chút."

            hoang smile "Nhưng nếu là câu hỏi về ánh sáng, anh sẽ kỳ vọng em tự nhìn trước."

            "Tâm bật cười khẽ."

            tam smile "Vậy em sẽ nhìn kỹ rồi mới hỏi."

            hoang smile "Tốt."

            "Câu đó vẫn không phải khen."

            "Nhưng Tâm thấy nó dễ chịu."

            "Cô cất tấm card vào ví, cẩn thận hơn mức cần thiết."

            "Phía sau, Huyền giả vờ nhìn trần nhà."

            huyen teasing "Trần hôm nay đẹp ghê."

            tam embarrassed "Mày thôi ngay."

            huyen grinning "Tao đã nói gì đâu."

        "Để Huyền tiếp tục trêu Hoàng":
            $ story_add('huyen_hoang_interest', 2)
            $ story_add('hoang_huyen_interest', 2)
            $ story_add('career_huyen', 1)
            $ story_flag('tam_c02_huyen_teased_hoang')

            "Tâm chưa kịp quyết thì Huyền đã kéo cô tới bàn mô hình."

            huyen smile "Anh Hoàng."

            hoang neutral "Ừ?"

            huyen teasing "Em có feedback cuối cùng trước khi về."

            hoang smile "Anh nghe."

            huyen neutral "Mô hình rất đẹp. Nhưng nếu để ở tiệc công ty thì nên ghi cảnh báo."

            hoang confused "Cảnh báo gì?"

            huyen grinning "Đừng đứng nhìn quá lâu khi đói. Dễ tưởng mấy khối gỗ này là bánh."

            "Hoàng im lặng đúng một nhịp."

            "Rồi anh cười."

            hoang laughing "Feedback này hơi khó đưa vào bản kỹ thuật."

            huyen teasing "Không sao. Em tin người làm thiết kế phải biết vượt qua giới hạn."

            tam tired "Huyền, mày đừng làm phiền anh ấy nữa."

            hoang smile "Không phiền đâu."

            "Anh nhìn sang Tâm."

            hoang neutral "Bạn em vui thật."

            tam neutral "Dạ. Nhiều lúc hơi quá vui."

            huyen surprised "Ơ?"

            hoang smile "Nhưng trong tiệc công ty thì cần người như vậy."

            "Huyền khoanh tay, vẻ rất hài lòng."

            huyen grinning "Nghe chưa. Người có chuyên môn đã xác nhận giá trị xã hội của tao."

            tam smile "Ừ. Tao ghi nhận."

            "Tâm đứng bên cạnh, nhìn Huyền và Hoàng nói thêm vài câu."

            "Cô không thấy khó chịu."

            "Chỉ hơi lạ."

            "Có những người bắt nhịp với nhau nhanh đến mức người ngoài đứng cạnh cũng thấy nhịp sáng hơn một chút."

            "Tâm không chen vào."

            "Cô chỉ nghe."

            "Và nhớ lại cách Hoàng cười khi bị Huyền trêu."

        "Về sớm để nghỉ cho ngày mai":
            $ story_add('career_tam', 3)
            $ story_add('tam_self_clarity', 1)
            $ story_add_direction('tam', 'tam_career_focus')
            $ story_flag('tam_c02_left_party_early')

            "Tâm nhìn đồng hồ."

            "Không quá muộn."

            "Nhưng cũng đủ để ngày mai trở nên khó chịu nếu cô cố ở lại thêm."

            tam neutral "Tao về trước nhé."

            huyen surprised "Giờ á?"

            tam smile "Ừ. Mai tao còn phải sửa nốt phần tài liệu training."

            huyen neutral "Mày đúng là nhân viên gương mẫu đáng sợ."

            tam tired "Tao chỉ không muốn sáng mai vừa mở mắt đã hối hận."

            huyen smile "Cũng hợp lý."

            "Huyền đưa túi cho cô."

            huyen neutral "Về cẩn thận. Tới nhà nhắn tao."

            tam smile "Biết rồi."

            "Tâm đi ngang qua bàn mô hình."

            "Hoàng đang nói chuyện với quản lý dự án. Anh quay sang đúng lúc cô bước qua."

            hoang smile "Em về à?"

            tam neutral "Dạ. Mai em còn việc."

            hoang neutral "Ừ. Nghỉ sớm cũng tốt."

            "Không có câu nào đặc biệt."

            "Không trao đổi liên hệ."

            "Không hẹn lần sau."

            "Nhưng Hoàng hơi nghiêng đầu chào cô, rất nhẹ."

            "Tâm cũng gật lại."

            "Cô rời khỏi sảnh."

            "Không khí ngoài hành lang lạnh hơn bên trong."

            "Tâm kéo nhẹ tay áo xuống cổ tay."

            "Tối nay cô đã không chọn giữ lại một cuộc trò chuyện."

            "Nhưng cô chọn giữ lại nhịp của mình."

            "Điều đó cũng không tệ."

    "Khi Tâm và Huyền ra đến cửa sảnh, bảng tên sự kiện phía sau vẫn còn sáng."

    "{i}Company Anniversary Party.{/i}"

    "Hai tháng thử việc vẫn chưa kết thúc."

    "Câu chuyện với Quân mới chỉ là tiếng đồn."

    "Câu chuyện với Hoàng mới chỉ là một vài câu nói."

    "Câu chuyện với Huyền thì vẫn tiếp tục bằng việc cô nàng vừa đi vừa than chưa kịp ăn món tráng miệng thứ ba."

    huyen tired "Tao nói thật, đi tiệc công ty mà không ăn đủ đồ ngọt là thất bại chiến lược."

    tam smile "Mày có ăn hai phần bánh rồi."

    huyen neutral "Hai là dữ liệu chưa đủ kết luận."

    tam laughing "Mai tao mua bánh cho."

    huyen happy "Bạn tốt."

    "Tâm cười."

    "Một ngày dài khép lại bằng tiếng giày chạm nhẹ trên nền hành lang."

    "Không có gì bùng nổ."

    "Không có lời hứa hẹn."

    "Chỉ có một vài lựa chọn nhỏ đã được đặt xuống."

    "Nhỏ thôi."

    "Nhưng đủ để ngày mai rẽ đi khác một chút."

    return