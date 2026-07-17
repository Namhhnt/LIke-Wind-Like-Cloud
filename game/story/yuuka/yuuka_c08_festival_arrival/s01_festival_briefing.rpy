# FILE: game/story/yuuka/yuuka_c08_festival_arrival/s01_festival_briefing.rpy
# Scene file.

label yuuka_c08_festival_arrival_s01_festival_briefing:
    scene black
    with fade

    centered "{size=46}CHAPTER 08{/size}\n{size=30}Người ngoài khung hình{/size}"

    scene bg_meeting_room_day
    with dissolve

    "Ba tuần trước Liên hoan phim Châu Á–Thái Bình Dương, Quân gọi cả ban triển khai vào phòng họp."

    "Không có NorthBridge."

    "Dự án kho vận trước đó đã chuyển sang giai đoạn thi công. Phần thiết kế quy trình, phân quyền và kiểm soát hồ sơ gần như hoàn tất."

    "Minh cùng đội cố vấn phía đối tác vẫn theo dự án cũ, nhưng team của Quân không còn phải tham gia vận hành hằng ngày."

    "Thay vào đó, An Thịnh vừa được giao một gói triển khai mới."

    "Không xây rạp. Không sản xuất phim. Càng không có ai trong phòng được phép tự nhận mình hiểu điện ảnh chỉ vì từng xem hết ba mùa một bộ phim truyền hình."

    "Công ty phụ trách điều phối hạ tầng sự kiện, hồ sơ nhà tài trợ, lịch vận chuyển thiết bị, dữ liệu khách mời và một phần quy trình hậu cần của liên hoan phim."

    quan neutral "Nói ngắn gọn: bên tổ chức có nghệ sĩ, có đạo diễn, có truyền thông."

    quan tired "Còn bên mình có bảng tiến độ, thẻ ra vào và trách nhiệm giải thích vì sao một kiện thiết bị đang ở sân bay nhưng trên hệ thống lại ghi đã tới khách sạn."

    huyen grinning "Nghe lãng mạn ghê."

    quan irritated "Anh chưa nói đến đoạn hai mươi bảy đơn vị cùng sửa một file."

    huyen tired "Rút lại. Không còn lãng mạn nữa."

    "Người phụ nữ ngồi cạnh Quân khẽ bật cười. Chị khoảng ngoài ba mươi, tóc buộc thấp, trước mặt là một tập hồ sơ có logo của liên hoan phim."

    quan neutral "Đây là chị Vân, đầu mối vận hành phía ban tổ chức."

    c08_van smile "Chào mọi người. Tôi được cảnh báo trước là team này làm việc tốt nhưng nói chuyện hơi nhiều."

    huyen neutral "Thông tin tương đối chính xác ạ."

    quan irritated "Huyền."

    huyen grinning "Em đang xây dựng niềm tin với đối tác."

    "Vân mở slide tổng quan."

    "Bốn địa điểm tổ chức."

    "Mười ba đoàn phim quốc tế."

    "Ba buổi công chiếu lớn."

    "Một khu vực triển lãm."

    "Hai khách sạn dành cho khách mời."

    "Và một danh sách người tham gia đủ dài để khiến thanh cuộn bên phải trông hơi tuyệt vọng."

    c08_van neutral "Team anh Quân sẽ phụ trách cầu nối giữa ban tổ chức, đơn vị vận hành địa điểm và hệ thống quản lý khách mời."

    c08_van neutral "Việc quan trọng nhất là dữ liệu phải thống nhất. Một người không thể có ba lịch đón sân bay chỉ vì tên được nhập theo ba cách."

    huyen teasing "Chị đánh giá hơi cao khả năng của con người rồi đấy."

    c08_van grinning "Tôi làm sự kiện tám năm. Tôi không còn đánh giá cao con người nữa."

    "Quân chuyển sang slide phân công."

    if c08_tam_leads_festival:
        quan neutral "Tâm sẽ lead nhóm điều phối hồ sơ và vận hành khách mời."

        tam surprised "Em ạ?"

        quan neutral "Job level của em đủ rồi. Dự án trước em xử lý liên phòng ban tốt."

        quan neutral "Nhóm không lớn. Nhưng lịch đón, quyền truy cập, yêu cầu kỹ thuật và thay đổi phút cuối sẽ đi qua em trước."

        huyen teasing "Chúc mừng. Từ giờ mày được tự tay chịu trách nhiệm cho sự đau khổ của mình."

        tam irritated "Cảm ơn lời động viên."

        $ story_add("career_tam", 15)
        $ story_add("tam_self_clarity", 5)
        $ story_flag("tam_leads_festival_workstream")

    else:
        quan neutral "Tâm phụ trách điều phối hồ sơ khách mời dưới team của anh."

        quan neutral "Phần này nhiều dependency. Em theo sát Huyền và chị Vân, đừng tự ôm khi có thay đổi ngoài scope."

        tam neutral "Vâng."

        huyen smile "Yên tâm. Tao sẽ chia đều đau khổ."

        tam teasing "Nghe đáng tin quá."

        $ story_add("career_tam", 5)
        $ story_flag("tam_supports_festival_workstream")

    c08_van neutral "Hôm nay chưa cần nhớ hết tên khách mời. Nhưng có ba nhóm cần ưu tiên."

    c08_van neutral "Đoàn phim khai mạc, khách nhận giải thành tựu, và các đạo diễn có lịch giao lưu chuyên môn."

    "Danh sách hiện lên."

    "Tên người. Quốc gia. Chuyến bay dự kiến. Yêu cầu ngôn ngữ. Người liên hệ."

    "Tâm mở sổ."

    menu:
        "Tâm ưu tiên điều gì trong buổi briefing?"

        "Chốt rõ phạm vi và người chịu trách nhiệm.":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 10)
            $ story_flag("tam_c08_defined_festival_scope")

            tam neutral "Phần thay đổi lịch bay sẽ do bên nào xác nhận cuối cùng ạ? Ban tổ chức hay đơn vị quản lý khách mời?"

            c08_van smile "Câu hỏi đúng."

            c08_van neutral "Ban tổ chức xác nhận nội dung. Team em cập nhật vận hành. Không tự sửa theo tin nhắn riêng của khách."

            quan neutral "Ghi đậm câu cuối."

            huyen teasing "Em sẽ đóng khung treo trước cửa."

        "Vẽ trước các dependency dễ đổ vỡ.":
            $ story_add("career_tam", 10)
            $ story_add("tam_observation", 10)
            $ story_flag("tam_c08_mapped_festival_dependencies")

            tam neutral "Lịch khách mời đang phụ thuộc chuyến bay, khách sạn, phương tiện và quyền ra vào địa điểm."

            tam neutral "Nếu một mục đổi, mình cần cảnh báo tự động cho ba mục còn lại."

            quan smile "Đúng."

            c08_van surprised "Bên tôi đang làm thủ công."

            huyen tired "Thế thì từ hôm nay bên chị được làm thủ công có cấu trúc hơn."

        "Quan sát cách Quân giữ team khỏi bị ôm việc.":
            $ story_add("tam_observation", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_add("career_tam", 5)
            $ story_flag("tam_c08_learned_scope_control")

            "Tâm không ghi tên khách trước."

            "Cô ghi ba dòng Quân vừa nhắc: việc nào thuộc team, ai được quyền đổi, thay đổi nào phải được xác nhận."

            "Ở dự án trước, cô thường nghĩ người làm tốt là người nhận được nhiều việc."

            "Bây giờ cô bắt đầu hiểu người lead tốt còn phải biết việc nào không nên để team mình nhận."

    "Buổi họp kéo dài thêm gần một giờ."

    "Khi mọi người đứng dậy, trên màn hình vẫn còn danh sách khách mời."

    "Ở gần cuối trang có một cái tên Nhật Bản."

    "Nakamura Yuuka."

    "Tâm chỉ kịp nhìn thoáng qua trước khi Vân chuyển slide."

    $ story_flag("festival_project_started")
    $ story_flag("yuuka_name_listed_as_guest_director")

    return