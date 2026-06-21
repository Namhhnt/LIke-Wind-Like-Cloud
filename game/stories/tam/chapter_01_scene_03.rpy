# Chapter 01, Scene 03

label tam_c01_scene_03:

    scene bg_company_open_office_day
    with dissolve

    narrator "Tâm học cách phân biệt một email cần trả lời ngay với một email chỉ có vẻ như cần trả lời ngay."

    narrator "Cô học cách đọc biên bản họp mà không ngủ gục."

    narrator "Học cách ghi chú deadline, mã hồ sơ, số hợp đồng, tên nhà thầu, và cả những câu nói nửa đùa nửa thật của cấp trên mà tốt nhất không nên xem là đùa."

    narrator "Phòng triển khai dự án đúng như cô hình dung trong buổi phỏng vấn."

    narrator "Nằm ở giữa rất nhiều thứ."

    narrator "Và cũng bị kéo từ rất nhiều phía."

    scene bg_meeting_room_day
    with dissolve

    manager "Tâm, hồ sơ nghiệm thu lô vật liệu này đang lệch với ghi chú của bên quản lý chất lượng. Kế toán thì cần xác nhận trước cuối ngày để lên thanh toán tạm."

    manager "Em kiểm tra lại giúp anh. Đừng để chiều nay phòng pháp lý phải gọi xuống hỏi vì sao hồ sơ chạy trước biên bản."

    narrator "Một tập tài liệu được đặt xuống trước mặt Tâm."

    narrator "Không dày."

    narrator "Nhưng đủ khiến lòng cô hơi nặng."

    if "tam_work_skill_strong_c01" in progress["player_flags"]:
        narrator "Tâm chợt nhớ lại câu trả lời hôm phỏng vấn."
        narrator "Không chuyển tiếp thông tin khi chưa hiểu bối cảnh."
        narrator "Không để lỗi nhỏ thành vấn đề lớn."

    menu:
        "Tâm nên xử lý hồ sơ lệch thế nào?"

        "Đối chiếu ghi chú QC, hỏi lại vật tư, sau đó gửi một bản tổng hợp ngắn cho kế toán và pháp lý.":
            $ tam_work_skill += 1
            $ tam_confidence += 1
            $ add_unique(progress["player_flags"], "tam_handled_project_issue_well")
            tam serious "Em xin phép kiểm tra lại với QC và vật tư trước. Nếu lệch ở biên bản, em sẽ ghi rõ điểm chưa khớp rồi gửi bản tổng hợp cho các bên liên quan."
            manager "Đúng. Làm như vậy đi."
            narrator "Không ai khen thêm."
            narrator "Nhưng chỉ một câu 'đúng' thôi cũng đủ khiến Tâm thấy sống lưng mình thẳng hơn."

        "Gửi xác nhận tạm cho kế toán trước để kịp deadline, rồi bổ sung sau.":
            $ tam_confidence -= 1
            $ add_unique(progress["player_flags"], "tam_project_issue_rushed")
            tam embarrassed "Em gửi xác nhận tạm trước rồi bổ sung sau được không ạ?"
            manager "Không. Hồ sơ thanh toán mà chạy trước xác nhận chất lượng thì người bị gọi đầu tiên là phòng mình."
            narrator "Tâm im lặng."
            narrator "Cô ghi lại lời nhắc ấy rất kỹ."

        "Chờ trưởng phòng tự quyết vì hồ sơ liên quan nhiều bên.":
            $ tam_confidence -= 1
            tam sad "Vậy phần này em chờ anh quyết định rồi em làm theo ạ?"
            manager "Anh cần em kiểm tra trước khi anh quyết."
            narrator "Câu nói không nặng."
            narrator "Nhưng Tâm vẫn thấy mặt mình nóng lên."

    scene bg_company_year_end_party
    with fade

    narrator "Year End Party của công ty được tổ chức ở một khách sạn lớn vào cuối năm."

    narrator "Sau vài tháng đi làm, Tâm đã bớt giống cô gái cầm hồ sơ ngồi cứng đờ trong phòng chờ phỏng vấn."

    narrator "Cô vẫn cẩn thận. Vẫn hay nghĩ nhiều."

    narrator "Nhưng đã biết lúc nào nên hỏi, lúc nào nên im lặng, và lúc nào phải đứng ra nói một câu rõ ràng trước khi mọi chuyện rối hơn."

    if tam_salary_tier == "high":
        narrator "Mức lương tốt hơn ban đầu cũng cho cô nhiều lựa chọn hơn."
        narrator "Tối nay, Tâm mặc một chiếc váy thanh lịch vừa vặn, phụ kiện nhỏ nhưng sáng, không phô trương mà vẫn đủ khiến người khác ngoái nhìn."
        $ hoang_impression += 2
    else:
        narrator "Tâm chọn một bộ váy đơn giản, gọn gàng, không quá nổi bật nhưng hợp với cô."
        narrator "Cái đẹp của cô vẫn nằm ở sự sạch sẽ, dịu mắt, và một chút lặng lẽ khó gọi tên."

    if tam_confidence >= 2:
        narrator "Cách cô đứng giữa đám đông cũng khác."
        narrator "Không còn là kiểu cố giấu mình ở rìa cuộc vui."
        narrator "Cô nói chuyện vừa đủ, cười vừa đủ, và khi đồng nghiệp nhắc đến một vướng mắc dự án vừa xử lý xong, Tâm trả lời bằng sự bình tĩnh hiếm thấy ở một nhân viên mới."
        $ hoang_impression += 2
    elif tam_confidence >= 1:
        narrator "Tâm chưa thật sự tự tin giữa đám đông, nhưng cô không còn quá lạc lõng."
        $ hoang_impression += 1
    else:
        narrator "Giữa ánh đèn và tiếng nhạc, Tâm vẫn thấy mình hơi nhỏ."
        narrator "Cô đứng cạnh Huyền nhiều hơn, thi thoảng mỉm cười khi có người hỏi chuyện."

    if "huyen_trust_high_c01" in progress["player_flags"]:
        $ hoang_impression += 1
        huyen serious "Đứng thẳng lên. Mày đẹp mà cứ làm như đang xin lỗi xã hội vì mình đẹp ấy."
        tam embarrassed "Mày nói nhỏ thôi."
        huyen serious "Không. Tao đang thực hiện nghĩa vụ bạn thân."

    narrator "Hôm đó công ty có vài khách mời từ đối tác."

    narrator "Tâm không để ý nhiều."

    narrator "Cho đến khi cô nhìn thấy một người đứng gần khu vực cửa kính."

    narrator "Một chàng trai mặc vest tối màu, dáng người cao và gọn. Khuôn mặt không quá xa lạ, nhưng cũng không đủ quen để cô gọi tên cảm giác vừa thoáng qua trong lòng."

    narrator "Anh đang nói chuyện với một người bên ban lãnh đạo công ty."

    narrator "Ánh mắt anh bình tĩnh. Nụ cười vừa đủ lịch sự. Cái kiểu người có thể đứng yên giữa một căn phòng ồn ào mà vẫn khiến không khí quanh mình có trật tự riêng."

    tam thoughtful "..."

    huyen confused "Gì đấy?"

    tam embarrassed "Không có gì."

    huyen smile "Không có gì mà nhìn người ta như đang đọc tài liệu mật?"

    tam embarrassed "Mày im đi."

    narrator "Huyền nhìn theo hướng mắt Tâm, rồi khẽ huých khuỷu tay vào cô."

    huyen smile "À."

    tam surprised "À cái gì?"

    huyen smile "Không có gì. Tao chỉ vừa phát hiện dự án phụ."

    tam embarrassed "Huyền."

    huyen smile "Rồi rồi. Tao im."

    if hoang_impression >= 4:

        $ add_unique(progress["player_flags"], "hoang_first_contact_c01")
        $ add_unique(progress["player_flags"], "hoang_approached_tam_first")
        $ add_unique(progress["player_flags"], "tam_year_end_strong_impression")

        narrator "Tâm định quay đi."

        narrator "Nhưng đúng lúc đó, chàng trai kia nhìn sang."

        narrator "Ánh mắt hai người chạm nhau."

        narrator "Không lâu."

        narrator "Chỉ vừa đủ để Tâm nhận ra anh đang thật sự nhìn mình, không phải nhìn xuyên qua đám đông."

        narrator "Rồi anh bước tới."

        hoang neutral "Chào em."

        tam shy "Dạ... chào anh."

        hoang neutral "Anh là Hoàng. Đi cùng đoàn đối tác hôm nay."

        tam neutral "Em là Tâm. Phòng triển khai dự án."

        hoang smile "Anh biết."

        narrator "Tâm hơi khựng lại."

        hoang serious "Lúc nãy anh có nghe em trao đổi về hồ sơ nghiệm thu với anh bên vật tư. Cách em tóm ý khá gọn."

        tam embarrassed "À... em chỉ nói lại phần em nắm được thôi ạ."

        hoang serious "Nói lại cho người khác hiểu cũng là một kỹ năng."

        narrator "Giọng anh không giống khen xã giao."

        narrator "Và chính vì thế, Tâm bỗng không biết nên đặt tay mình ở đâu cho tự nhiên."

        huyen smile "Tôi đi lấy thêm nước nhé."

        narrator "Huyền nói rất nhanh rồi biến mất."

        narrator "Phản bội rất có kỹ thuật."

        hoang smile "Bạn em thú vị thật."

        tam smile "Dạ. Nó thường xuyên như vậy."

        hoang smile "Vậy chắc em vất vả."

        tam smile "Cũng quen rồi ạ."

        narrator "Hoàng khẽ cười."

        narrator "Một nụ cười rất nhẹ."

        narrator "Nhưng lạ thay, nó làm Tâm nhớ đến chiếc bàn trong góc tối của nhà hàng mấy tháng trước."

        narrator "Một cái ly được nâng lên."

        narrator "Một lời chúc mừng không thành tiếng."

        narrator "Ý nghĩ ấy vụt qua rất nhanh, rồi tan mất giữa tiếng nhạc."

        jump tam_c01_year_end_after_meeting

    elif hoang_impression >= 2:

        $ add_unique(progress["player_flags"], "tam_year_end_can_approach_hoang")

        narrator "Chàng trai kia nhìn sang một lần."

        narrator "Rất nhanh."

        narrator "Không đủ để gọi là bắt chuyện. Nhưng đủ để Tâm biết nếu cô bước tới, điều đó sẽ không quá kỳ lạ."

        menu:
            "Tâm có nên chủ động bắt chuyện không?"

            "Chủ động bắt chuyện với anh" if "tam_year_end_can_approach_hoang" in progress["player_flags"]:
                $ add_unique(progress["player_flags"], "hoang_first_contact_c01")
                $ add_unique(progress["player_flags"], "tam_approached_hoang_first")
                $ hoang_impression += 1

                narrator "Tâm hít một hơi rất khẽ."

                narrator "Không phải vì cô bỗng trở nên can đảm."

                narrator "Chỉ là có những khoảnh khắc nếu bỏ qua, sau này sẽ thấy hơi tiếc."

                tam neutral "Chào anh. Hình như anh là khách mời bên công ty đối tác ạ?"

                hoang neutral "Ừ. Anh là Hoàng."

                tam neutral "Em là Tâm. Phòng triển khai dự án."

                hoang neutral "Anh có nghe giới thiệu lúc nãy."

                tam embarrassed "Vậy chắc anh cũng nghe cả đoạn em nói hơi vấp."

                hoang serious "Có."

                narrator "Tâm ngẩng lên."

                hoang smile "Nhưng đoạn sau em sửa lại tốt."

                narrator "Câu trả lời thẳng đến mức Tâm không biết nên xem là khen hay xác nhận hiện trường."

                tam smile "Anh thường nói chuyện như đang nghiệm thu hồ sơ vậy ạ?"

                narrator "Hoàng thoáng khựng."

                narrator "Rồi anh bật cười."

                hoang smile "Không thường xuyên. Chỉ khi gặp người làm phòng triển khai."

                narrator "Tâm cũng cười."

                narrator "Một cuộc trò chuyện rất ngắn."

                narrator "Nhưng đủ để cả hai có một cái tên dành cho nhau."

                jump tam_c01_year_end_after_meeting

            "Không bắt chuyện, chỉ giữ khoảng cách quan sát":
                $ add_unique(progress["player_flags"], "hoang_no_contact_c01")
                $ add_unique(progress["player_flags"], "hoang_romance_slow_start")
                narrator "Tâm cuối cùng vẫn không bước tới."
                narrator "Cô chỉ nhìn anh thêm một lần nữa, rồi quay sang nghe Huyền nói chuyện."
                narrator "Có những cuộc gặp bắt đầu bằng một lời chào."
                narrator "Cũng có những cuộc gặp bắt đầu bằng việc cả hai đều im lặng."
                jump tam_c01_year_end_no_contact

    else:

        $ add_unique(progress["player_flags"], "hoang_no_contact_c01")
        $ add_unique(progress["player_flags"], "hoang_romance_delayed_start")

        narrator "Chàng trai kia đứng ở phía xa."

        narrator "Tâm nhìn thấy anh."

        narrator "Và có lẽ anh cũng nhìn thấy cô."

        narrator "Nhưng đám đông, ánh đèn, tiếng nhạc, và cả sự thiếu tự tin nhỏ bé trong lòng Tâm đã giữ hai người ở hai phía khác nhau của căn phòng."

        narrator "Không ai bước tới."

        narrator "Không có lời chào."

        narrator "Chỉ có một ánh nhìn rất khẽ, bị buổi tiệc nuốt mất trước khi kịp trở thành điều gì rõ ràng."

        jump tam_c01_year_end_no_contact
