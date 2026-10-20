# FILE: game/story/tam/tam_c02_company_party/s02_party_start.rpy
# Scene file.

label tam_c02_company_party_s02_party_start:
    scene bg_company_year_end_party
    with fade

    "Sáu tuần sau, Tâm đã không còn phải hỏi đường đến máy in."

    "Cô cũng không còn giật mình mỗi lần có email mới từ hệ thống quản lý task."

    "Đó có lẽ là dấu hiệu tốt."

    "Hoặc ít nhất là dấu hiệu con người có khả năng thích nghi đáng kinh ngạc với deadline."

    "Buổi tiệc kỷ niệm thành lập công ty diễn ra tại sảnh lớn tầng sự kiện."

    "Ánh đèn vàng phủ lên bàn tiệc, ly thủy tinh, bảng tên khách mời, và cả những nụ cười hơi xã giao của người vừa tan làm chưa kịp chuyển chế độ."

    "Tâm đứng ở gần cửa vào, một tay cầm clutch nhỏ, tay còn lại giữ nhẹ phần cổ tay áo."

    if story_has_flag('tam_c02_outfit_party_elegant'):
        scene cg_tam_c02_party_premium_dress
        with dissolve
        "Chiếc váy Tâm mặc tối nay không giống những bộ đồ công sở thường ngày của cô."

        "Vải rủ mềm, đường cắt gọn, phần eo vừa vặn đến mức cô đã phải đứng trước gương lâu hơn cần thiết."

        "Không quá phô trương."

        "Nhưng rõ ràng không còn là lựa chọn an toàn."

        huyen smile "Tao nói thật nhé."

        tam neutral "Gì?"

        huyen neutral "Nếu lát nữa có ai hỏi mày bên phòng nào, mày cứ nói bên phòng gây chú ý."

        tam embarrassed "Mày đừng làm tao hối hận."

        huyen teasing "Muộn rồi. Váy đã đẹp thì không trả lại sự khiêm tốn được đâu."

    elif story_has_flag('tam_c02_outfit_office_elegant'):
        scene cg_tam_c02_party_office
        with dissolve

        "Chiếc váy công sở mới khiến Tâm trông gọn gàng hơn thường ngày."

        "Không quá nổi bật."

        "Nhưng phần vai vừa vặn và màu vải dịu làm cô có vẻ bình tĩnh hơn."

        "Ít nhất là từ bên ngoài."

        huyen smile "Ổn đấy."

        tam neutral "Thật không?"

        huyen teasing "Thật. Nhìn như người có thể đọc hết policy công ty mà không khóc."

        tam tired "Mày có thể khen bình thường hơn không?"

        huyen grinning "Không. Đó là giới hạn nghệ thuật của tao."

    else:
        scene cg_tam_c02_party_default
        with dissolve

        "Chiếc váy công sở cô chọn không quá nổi bật."

        "Nhưng vừa đủ gọn gàng."

        "Vừa đủ an toàn."

        "Và vừa đủ khiến Huyền nhìn cô bằng vẻ mặt rất không hài lòng."

        huyen neutral "Mày gọi đây là đi tiệc à?"

        tam neutral "Có vấn đề gì?"

        huyen tired "Không. Rất chuyên nghiệp. Nhìn như sắp lên phát biểu báo cáo quý."

        huyen teasing "Ổn. Ổn kiểu nếu có cháy thì nhân viên cứu hỏa sẽ hỏi mày danh sách khách mời."

        tam tired "Mày bớt đi."

        "Huyền cười, đưa tay kéo nhẹ phần tóc bên vai Tâm ra sau."

        huyen smile "Thôi được. Xinh."

        tam neutral "Vừa nãy mày chê."

        huyen grinning "Chê là quyền bạn thân. Khen là nghĩa vụ công dân."

    "Tâm cúi mắt cười."

    scene bg_company_year_end_party
    with dissolve
    
    "Phía trước sân khấu nhỏ, quản lý các phòng ban đang đứng thành từng cụm."

    "Một nhóm nhân viên trẻ tụ lại cạnh bàn đồ uống."

    "Bên góc phải, vài người đang xem một mô hình dự án đặt trong hộp kính thấp."

    "Tâm nhớ đã thấy hình ảnh mô hình đó trong một tài liệu nội bộ."

    "Dự án thiết kế không gian trải nghiệm mới cho khách hàng."

    "Một số đường nét khá đẹp."

    "Nhưng góc đèn phản chiếu trên mặt kính hơi chói."

    huyen neutral "Mày đang nhìn gì đấy?"

    tam neutral "Cái mô hình kia."

    huyen teasing "À. Tưởng nhìn trai."

    tam embarrassed "Huyền."

    huyen happy "Gì. Tiệc công ty mà. Người ta sinh ra networking là để nhìn người khác hợp pháp hơn."

    "Tâm vừa định đáp lại thì tiếng micro vang lên."

    manager "Mọi người ổn định một chút nhé."

    "Không khí dần dịu xuống."

    "Người đại diện công ty bước lên sân khấu nhỏ, nói vài lời về chặng đường đã qua, những dự án mới, những nỗ lực trong năm."

    "Tâm lắng nghe."

    "Không phải vì bài phát biểu quá cuốn hút."

    "Mà vì cô nhận ra mình đã bắt đầu hiểu một vài cái tên dự án được nhắc đến."

    "Hai tháng trước, chúng chỉ là chữ."

    "Bây giờ, mỗi chữ đều có người, deadline, file sửa, và vài buổi chiều hơi mệt phía sau."

    huyen neutral "Sau bài phát biểu là ăn đúng không?"

    tam smile "Mày có thể chờ thêm ba phút không?"

    huyen tired "Về mặt sinh học thì có. Về mặt tinh thần thì không chắc."

    "Tâm nhìn quanh sảnh."

    "Ở một buổi tiệc như thế này, đứng ở đâu cũng giống một lựa chọn nhỏ."

    "Đứng cạnh Huyền thì an toàn."

    "Đứng gần bàn dự án thì có thể nghe thêm chuyện công việc."

    "Đứng ở góc yên tĩnh thì dễ quan sát hơn."

    "Không có lựa chọn nào sai hẳn."

    "Chỉ là mỗi lựa chọn sẽ kéo cô về một nhịp khác nhau."

    menu:
        "Tâm đứng ở đâu trong buổi tiệc?"

        "Ở gần Huyền":
            $ story_add('career_huyen', 1)
            $ story_add('tam_self_clarity', 1)
            $ story_flag('tam_stays_with_huyen')
            $ story_flag('tam_c02_party_near_huyen')

            "Tâm dịch về phía Huyền thêm nửa bước."

            huyen smile "Biết điều đấy."

            tam neutral "Tao chỉ sợ mày đói quá rồi ăn nhầm hoa trang trí."

            huyen teasing "Hoa trang trí mà ngon thì tao cũng cân nhắc."

            "Hai người đứng cạnh bàn đồ uống."

            "Huyền cầm một ly nước trái cây lên, đưa cho Tâm ly còn lại."

            huyen neutral "Căng không?"

            tam neutral "Ít thôi."

            huyen smile "Tốt. Ít thôi thì uống nước được."

            "Tâm nhận lấy ly."

            "Ly thủy tinh mát lạnh trong tay."

            "Giữa tiếng người nói chuyện xung quanh, cảm giác có một người quen đứng cạnh hóa ra vẫn rất đáng giá."

        "Đứng gần bàn dự án":
            $ story_add('career_tam', 2)
            $ story_add('tam_observation', 1)
            $ story_flag('tam_c02_party_near_project_table')

            "Tâm nhìn sang Huyền."

            tam neutral "Tao qua xem cái mô hình một chút."

            huyen surprised "Tự nhiên chăm chỉ thế?"

            tam smile "Đứng đây nghe mày bàn chuyện đồ ăn thì tao sẽ đói theo."

            huyen grinning "Được. Đi đi. Nhưng đừng yêu cái mô hình."

            tam tired "Tao sẽ cố."

            "Tâm bước về phía bàn dự án."

            "Mô hình được đặt trong hộp kính thấp. Bên trong là một không gian mở, các đường cong màu gỗ nhạt kéo từ khu tiếp khách vào khu trải nghiệm."

            "Có vài người đang bàn về vật liệu."

            "Tâm không chen vào."

            "Cô chỉ đứng cách nửa bước, lắng nghe."

            coworker "Phần này nếu dùng ánh sáng lạnh thì hơi cứng."

            coworker "Bên thiết kế đề xuất đổi sang tone ấm hơn."

            "Tâm nhìn phần trần mô hình."

            "Quả thật, nếu ánh sáng dịu hơn một chút, đường cong sẽ mềm hơn."

            "Cô ghi nhớ điều đó."

        "Đứng ở góc yên tĩnh hơn":
            $ story_add('tam_observation', 2)
            $ story_flag('tam_c02_party_quiet_observer')

            "Tâm chọn một góc gần cửa kính."

            "Từ đó có thể nhìn thấy gần như toàn bộ sảnh."

            "Những nhóm người tự nhiên tách ra theo phòng ban."

            "Người quen đứng gần người quen."

            "Người muốn được chú ý đứng gần ánh đèn."

            "Người không muốn bị hỏi quá nhiều thì chọn chỗ có thể dễ dàng rút lui."

            "Tâm nhận ra điều đó, rồi khựng lại."

            "Vì chính cô cũng đang đứng ở một chỗ như vậy."

            huyen neutral "Trốn à?"

            "Huyền không biết đã đi theo từ lúc nào."

            tam surprised "Tao đâu có trốn."

            huyen teasing "Ừ. Mày chỉ chọn vị trí chiến lược để nếu cần thì biến mất trong ba giây."

            tam embarrassed "Mày nói nhỏ thôi."

            huyen smile "Không sao. Tao cũng thích chỗ này. Nhìn được bàn đồ ăn."

            "Tâm nhìn theo hướng mắt Huyền."

            "Đúng thật."

            "Ngay cả sự quan sát của Huyền cũng rất có mục tiêu."

    "Tiếng nhạc nền chuyển sang một bản nhẹ hơn."

    "Khách mời bên ngoài bắt đầu đến."

    "Một vài người được quản lý ra tận cửa đón."

    "Tâm không chú ý lắm."

    "Cho đến khi cô thấy người đàn ông trẻ vừa bước vào sảnh cúi đầu chào quản lý dự án."

    "Áo sơ mi sáng màu. Vest tối giản. Dáng đứng thoải mái nhưng không xuề xòa."

    "Anh không tạo cảm giác muốn chiếm lấy căn phòng."

    "Nhưng khi anh xuất hiện, căn phòng tự nhiên có thêm một điểm để nhìn."

    huyen neutral "Ê."

    tam neutral "Gì?"

    huyen teasing "Lần này tao chưa nói gì nhé."

    "Tâm rời mắt đi."

    tam embarrassed "Tao cũng chưa nói gì."

    huyen grinning "Ừ. Nhưng mắt mày thì có."

    return
