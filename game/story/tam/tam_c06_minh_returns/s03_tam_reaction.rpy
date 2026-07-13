# FILE: game/story/tam/tam_c06_minh_returns/s03_tam_reaction.rpy
# Home/stayed: first dinner with Minh.
# Home/fled: recurring dream and Huyền helps set up the canon four-person dinner.
# Company setup: Tâm prepares for next week's official partner meeting.

label tam_c06_minh_returns_s03_tam_reaction:
    if story_state.get("tam_c06_branch", "company_setup") == "home":
        if story_state.get("tam_c06_home_outcome", "fled") == "stayed":
            call tam_c06_minh_returns_s03_three_person_dinner
        else:
            call tam_c06_minh_returns_s03_after_flee
    else:
        call tam_c06_minh_returns_s03_prepare_for_partner_visit

    return


label tam_c06_minh_returns_s03_three_person_dinner:
    scene black
    with fade

    "Minh không để hai người vào bếp lâu."

    "Hoàng vẫn lách qua để lấy bát."

    "Tâm đứng bên cạnh tủ, không biết nên ngồi hay tiếp tục tìm một việc để làm."

    "Minh đưa cô một chồng đĩa."

    minh neutral "Nếu muốn giúp thì đặt lên bàn."

    tam neutral "Vâng."

    "Tâm nhận lấy."

    "Công việc nhỏ khiến tay cô có chỗ để đặt."

    "Bữa tối được dọn ra sau đó không lâu."

    "Ba người ngồi quanh chiếc bàn vốn đủ rộng cho nhiều người hơn."

    "Hoàng nói nhiều nhất."

    "Minh thi thoảng trả lời một câu."

    "Tâm chủ yếu ăn."

    "Và nhìn."

    "Minh biết chính xác mọi thứ nằm ở đâu dù mới trở về."

    "Anh đưa bát cho Hoàng trước khi cậu hỏi."

    "Hoàng tự lấy thêm cơm cho anh như một việc đã làm từ rất lâu."

    "Hai người đốp lại nhau liên tục."

    "Không ai thật sự giận."

    hoang irritated "Lão cho nhiều tiêu thế?"

    minh neutral "Mày vẫn ăn."

    hoang irritated "Em đang góp ý."

    minh teasing "Ăn hết rồi góp."

    "Tâm cúi xuống để giấu nụ cười."

    "Cô gắp một miếng ớt tây sang mép đĩa."

    "Minh nhìn thấy."

    "Anh không nói."

    "Lần sau khi đặt đĩa bò gần Tâm, phần quay về phía cô không còn miếng ớt nào."

    "Tâm nhìn đĩa."

    "Rồi nhìn Minh."

    minh neutral "Không ăn được à?"

    tam neutral "Không hẳn."

    minh neutral "Vậy là không thích."

    tam neutral "Vâng."

    "Hoàng nhìn cả hai."

    hoang teasing "Hôm nay em ít nói thế?"

    tam neutral "Em đang ăn."

    hoang teasing "Bình thường em vừa ăn vừa nói được."

    tam irritated "Anh muốn em nói chuyện hay ăn đồ anh Minh nấu?"

    hoang surprised "À."

    hoang teasing "Thần tượng mới rồi."

    tam embarrassed "Em có nói thế đâu."

    minh neutral "Cứ ăn đi."

    "Minh nói rất bình thường."

    "Tâm càng im hơn."

    "Một lúc sau, Minh hỏi về công việc của cô."

    minh neutral "Em đang làm phần nào của dự án?"

    tam neutral "Phân tích và theo dõi yêu cầu."

    minh neutral "Thích không?"

    tam irritated "Có."

    minh neutral "Phần nào?"

    "Tâm dừng đũa."

    menu:
        "Tâm trả lời..."

        "“Tìm ra chỗ người khác bỏ qua.”":
            tam neutral "Phần tìm ra chỗ người khác bỏ qua."

            "Minh gật."

            minh smile "Vậy công việc hợp em."

            "Một câu công nhận rất ngắn."

            "Tâm lại nhìn anh lâu hơn cần thiết."

            $ story_add("career_tam", 5)
            $ story_add("tam_observation", 5)
            $ story_flag("minh_recognizes_tam_observation_strength")

        "“Biến những thứ rối thành thứ có thể làm được.”":
            tam neutral "Biến những thứ rối thành thứ có thể làm được."

            minh neutral "Khó hơn nghe kể."

            tam neutral "Vâng."

            minh smile "Nhưng đáng làm."

            "Tâm khẽ gật."

            "Cô không biết vì sao câu nói ấy khiến mình nhớ đến giọng trong mưa."

            $ story_add("career_tam", 5)
            $ story_add("tam_minh_drawn", 5)
            $ story_flag("tam_connects_minh_voice_to_old_memory")

        "Trả lời ngắn rồi chuyển sang hỏi Hoàng":
            tam neutral "Em thích phần phân tích."

            "Tâm quay sang."

            tam neutral "Hôm nay anh có về công ty không?"

            hoang neutral "Không."

            "Hoàng nhìn cô."

            "Cậu biết cô vừa đổi hướng câu chuyện."

            "Nhưng không kéo nó quay lại."

            $ story_add("tam_self_clarity", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_flag("tam_grounds_first_minh_dinner_through_hoang")

    "Bữa tối tiếp tục."

    "Tâm vẫn ít nói."

    "Nhưng cô không còn muốn chạy."

    "Khi Minh đứng dậy lấy thêm canh, Tâm tự nhiên đưa bát sang."

    "Anh nhận."

    "Không ai nhắc chuyện ở cửa."

    "Điều đó khiến nó vẫn ở đó."

    "Chỉ không còn quá lớn."

    $ story_flag("tam_stayed_for_first_minh_dinner")
    $ story_flag("minh_notices_tam_observing")
    $ story_flag("tam_completed_first_minh_meeting")

    $ story_add("tam_observation", 10)
    $ story_add("tam_minh_drawn", 5)
    $ story_add("tam_self_clarity", 5)

    return


label tam_c06_minh_returns_s03_after_flee:
    scene black
    with fade

    "Sáng hôm sau, Tâm tỉnh dậy trước báo thức."

    "Cơn mưa trong giấc mơ vẫn còn rất rõ."

    "Cô bé đeo kính ngồi ở trạm xe buýt."

    "Chiếc khăn tay màu trắng."

    "Bàn tay người con trai."

    "Lần này, gương mặt người ấy gần hơn."

    "Không hoàn toàn rõ."

    "Nhưng đủ giống người đàn ông đã mở cửa tối qua."

    "Tâm ngồi bật dậy."

    "Cô đi đến tủ sách."

    "Từ ngăn sâu nhất, cô lấy ra một chiếc hộp giấy cũ."

    "Bên trong là cuốn nhật ký có khóa."

    "Kẹp ở trang đầu tiên là một chiếc khăn tay màu trắng."

    "Ba đường viền xanh đậm chạy song song quanh bốn cạnh."

    "Một họa tiết nhỏ nằm ở góc."

    "Tâm giữ chiếc khăn trong tay."

    "Chuông báo thức vang lên."

    "Cô giật mình."

    "Chiếc khăn được gấp lại quá nhanh."

    "Một góc bị lệch."

    "Tâm nhìn thấy."

    "Cô vẫn đóng sổ."

    "Đến giờ nghỉ trưa, Huyền đã ngồi ở chỗ quen thuộc."

    huyen happy "Thế nào?"

    tam confused "Gì?"

    huyen teasing "Buổi ra mắt."

    tam neutral "Chưa có gì."

    huyen confused "Là sao?"

    tam embarrassed "Tao bỏ về."

    "Huyền đặt cốc cà phê xuống."

    huyen shocked "Mày làm gì?"

    tam flustered "Nhà có việc."

    huyen irritated "Mày nói dối tao cũng đừng nói lười thế."

    "Tâm im."

    huyen confused "Gặp anh trai chưa?"

    "Tâm gật."

    huyen confused "Trông thế nào?"

    tam neutral "Khá giống Hoàng."

    huyen confused "Rồi?"

    tam neutral "Hết."

    huyen teasing "Mày nhìn người ta được bao lâu mà hết nhanh thế?"

    "Tâm cúi xuống."

    "Huyền quan sát bạn."

    "Lần này cô không hỏi tiếp về ngoại hình."

    huyen neutral "Hoàng nói gì?"

    tam neutral "Anh ấy hẹn lại cuối tuần."

    tam embarrassed "Lần này không được viện cớ."

    "Huyền ngồi yên một lúc."

    "Sau đó mắt cô sáng lên."

    huyen happy "Thế tao đi cùng."

    tam surprised "Để làm gì?"

    huyen teasing "Tránh trường hợp mày vừa thấy người ta đã chạy tiếp."

    tam irritated "Tao không chạy."

    huyen neutral "Ừ."

    huyen teasing "Mày dịch chuyển tức thời ra taxi."

    tam embarrassed "..."

    huyen happy "Tiện thể tao xem thử ông anh trai."

    huyen teasing "Biết đâu lại đúng mẫu tao thích."

    tam teasing "Đồ mê trai."

    huyen teasing "Câu này hôm qua mày nói rồi."

    tam teasing "Vẫn đúng."

    "Huyền nắm lấy cổ tay Tâm."

    huyen neutral "Cuối tuần tao đi với mày."

    "Tâm định từ chối."

    "Rồi thôi."

    "Có một người ngồi cạnh có lẽ sẽ dễ hơn."

    $ story_flag("tam_finds_old_handkerchief_after_minh")
    $ story_flag("huyen_joins_four_person_dinner")
    $ story_flag("four_person_weekend_dinner_confirmed")

    $ story_add("tam_minh_drawn", 5)
    $ story_add("tam_observation", 5)

    return


label tam_c06_minh_returns_s03_prepare_for_partner_visit:
    scene black
    with fade

    "Tin đồn không làm khối lượng công việc giảm đi."

    "Ngược lại, đến cuối ngày, Quân gửi một danh sách rà soát dài hơn bình thường."

    "Tâm mở tài liệu dự án."

    "Phần giả định nghiệp vụ có ba mục chưa được xác nhận."

    "Bảng phân quyền có hai dòng để trống."

    "Một quyết định cũ chỉ tồn tại trong lịch sử trò chuyện, chưa được ghi vào tài liệu."

    "Cô nhìn đồng hồ."

    "Vẫn còn đủ thời gian để sửa trước cuối tuần."

    menu:
        "Tâm chuẩn bị cho tuần tới bằng cách..."

        "Rà soát các giả định và quyết định còn thiếu":
            "Tâm tạo một bảng mới."

            "Cột đầu: vấn đề."

            "Cột thứ hai: trạng thái."

            "Cột thứ ba: người có quyền quyết định."

            "Cột cuối: hạn xác nhận."

            "Cô không cố đoán đối tác muốn gì."

            "Chỉ đảm bảo đội mình biết rõ điều gì đã chắc."

            $ story_add("career_tam", 10)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_prepares_decision_register_for_partner")

        "Hỏi Huyền phần thông tin nào đã được xác nhận":
            tam confused "Phần nào cậu biết chắc?"

            huyen teasing "Mày hỏi như kiểm toán ấy."

            tam neutral "Trả lời đi."

            "Huyền tách riêng những gì nghe từ Quân, những gì biết qua Hoàng và những gì chỉ là lời đồn."

            "Tâm ghi chép."

            "Không lấy sự phấn khích của bạn làm dữ liệu."

            "Cũng không bỏ qua những chi tiết có thể kiểm tra."

            $ story_add("career_tam", 5)
            $ story_add("tam_observation", 5)
            $ story_add("career_huyen", 5)
            $ story_flag("tam_verifies_huyen_partner_information")

        "Chờ bản brief chính thức":
            "Tâm đóng nhóm trò chuyện."

            "Cô không có tên."

            "Không có agenda."

            "Không có phạm vi trách nhiệm chính thức."

            "Chuẩn bị dựa trên trí tưởng tượng chỉ khiến cô tạo thêm việc."

            "Tâm hoàn thiện phần đang phụ trách rồi ghi một lời nhắc cho sáng thứ Hai."

            "Đọc brief trước khi kết luận."

            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_waits_for_official_partner_brief")

        "Chuẩn bị cả phương án cho một người cực khó tính":
            "Tâm in thêm tài liệu."

            "Cô đánh dấu mọi điểm có thể bị hỏi."

            "Rồi đánh dấu cả những điểm chỉ có khả năng bị hỏi."

            "Đến trang thứ mười ba, Huyền kéo xấp giấy xuống."

            huyen irritated "Mày chuẩn bị họp hay chuẩn bị ra tòa?"

            tam neutral "Phòng trước."

            huyen neutral "Tin đồn bảo người ta khó tính."

            huyen teasing "Không bảo người ta ăn thịt nhân viên."

            "Tâm nhìn xấp giấy."

            "Cô bỏ bớt bốn trang."

            "Vẫn còn hơi nhiều."

            $ story_add("career_tam", 5)
            $ story_add("tam_insecurity", 5)
            $ story_flag("tam_overprepares_for_unknown_partner")

    "Trước khi tan làm, Quân đi ngang qua bàn."

    quan neutral "Tài liệu rà soát xong trước thứ Sáu."

    tam neutral "Vâng."

    huyen confused "Anh có thể nói trước agenda tuần sau không?"

    "Quân dừng lại."

    quan neutral "Khi nào chốt, tôi sẽ gửi."

    huyen neutral "Một chút thôi cũng được."

    quan neutral "Một chút tin chưa chốt vẫn là tin chưa chốt."

    "Huyền ngồi thẳng lại."

    huyen neutral "Vâng."

    "Quân đi tiếp."

    "Tâm nhìn bạn."

    tam teasing "Trưởng thành rồi?"

    huyen irritated "Tao chỉ kiểm tra quy trình."

    $ story_flag("company_team_prepares_for_partner_visit")

    return
