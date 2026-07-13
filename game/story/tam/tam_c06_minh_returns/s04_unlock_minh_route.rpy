# FILE: game/story/tam/tam_c06_minh_returns/s04_unlock_minh_route.rpy
# Legacy label name retained.
#
# Home branch:
# - Stayed: Hoàng drives Tâm home; she may disclose the old connection.
# - Fled: canon four-person weekend dinner completes the first meeting.
#   Minh character/content visibility is unlocked, not an automatic romance.
#
# Company branch:
# - Only the official meeting setup is revealed.
# - Minh remains unseen until C07; minh_route_unlocked is NOT set here.

label tam_c06_minh_returns_s04_unlock_minh_route:
    if story_state.get("tam_c06_branch", "company_setup") == "home":
        if story_state.get("tam_c06_home_outcome", "fled") == "stayed":
            call tam_c06_minh_returns_s04_drive_home
        else:
            call tam_c06_minh_returns_s04_four_person_dinner
    else:
        call tam_c06_minh_returns_s04_company_meeting_pending

    return


label tam_c06_minh_returns_s04_drive_home:
    scene black
    with fade

    "Hoàng đưa Tâm về khi trời đã tối."

    "Mưa chỉ còn lất phất."

    "Hai người đi gần hết quãng đường mà không nhắc đến Minh."

    "Đến trước chung cư, Hoàng tắt máy."

    "Tâm tháo dây an toàn."

    "Cô vẫn chưa mở cửa."

    hoang neutral "Em biết anh Minh à?"

    tam neutral "Không."

    hoang neutral "Em nhìn lão như người quen."

    "Tâm nhìn ra cửa kính."

    tam confused "Em cũng đang nghĩ thế."

    "Hoàng chờ."

    "Cậu không hỏi dồn."

    menu:
        "Tâm..."

        "Kể về giấc mơ và cảm giác duyên phận":
            tam confused "Em thấy hình như mình từng gặp anh ấy."

            hoang confused "Ở đâu?"

            tam confused "Em không biết."

            tam flustered "Có thể trong một giấc mơ."

            "Hoàng quay sang."

            tam irritated "Anh nhìn đường đi."

            hoang smile "Xe đang đỗ."

            tam irritated "Thì nhìn phía trước."

            hoang smile "Anh chỉ hơi bất ngờ."

            tam confused "Vì sao?"

            hoang teasing "Lần đầu nghe em nói chuyện duyên phận."

            tam embarrassed "Em không nói là duyên phận."

            hoang teasing "Em vừa nói giấc mơ."

            tam irritated "Hai chuyện khác nhau."

            hoang neutral "Ừ."

            hoang teasing "Duyên phận có căn cứ."

            "Tâm huých nhẹ vào vai anh."

            tam irritated "Em đang nói nghiêm túc."

            "Hoàng thôi cười."

            hoang neutral "Nếu em nhớ ra thì nói anh."

            tam confused "Anh không thấy kỳ à?"

            hoang neutral "Có."

            "Tâm nhìn sang."

            hoang smile "Nhưng em đã kể anh nghe rồi."

            hoang smile "Thế là được."

            "Tâm đặt tay lên tay nắm cửa."

            "Cảm giác trong lòng vẫn chưa có tên."

            "Ít nhất nó không còn là một bí mật."

            $ story_add("hoang_tam_trust", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_add("tam_minh_drawn", 5)
            $ story_flag("tam_tells_hoang_about_minh_connection")
            $ story_flag("hoang_knows_tam_minh_recognition")

        "Chỉ nói Minh trông rất quen":
            tam confused "Em chỉ thấy anh ấy rất quen."

            hoang neutral "Ừ."

            tam confused "Anh không hỏi nữa à?"

            hoang neutral "Khi nào chắc thì em nói."

            "Tâm nhìn anh."

            "Sự bình thản ấy làm cô nhẹ đi."

            tam neutral "Vâng."

            $ story_add("hoang_tam_trust", 5)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_tells_hoang_minh_feels_familiar")

        "Giữ lại vì chưa chắc":
            tam neutral "Chắc em nhìn nhầm."

            "Hoàng không phản bác."

            "Anh chỉ gật."

            hoang neutral "Về đến nhà nhắn anh."

            tam neutral "Vâng."

            "Tâm mở cửa xe."

            "Trước khi bước xuống, cô nhìn anh thêm một lần."

            "Cậu không hoàn toàn tin."

            "Nhưng vẫn để cô có chỗ chưa cần nói."

            $ story_add("tam_minh_drawn", 5)
            $ story_flag("tam_hides_minh_recognition_from_hoang")

    $ story_flag("minh_character_profile_unlocked")
    $ story_flag("minh_first_seen_at_hoang_house")
    $ story_flag("minh_present_timeline_active")
    $ story_flag("minh_route_unlocked")
    $ story_flag("tam_minh_romance_observation_only")

    return


label tam_c06_minh_returns_s04_four_person_dinner:
    scene black
    with fade

    "Chiều tối thứ Bảy."

    "Huyền đến nhà Tâm sớm hơn gần một giờ."

    "Cô mở tủ quần áo trước khi kịp ngồi xuống."

    tam irritated "Chỉ ăn tối ở nhà thôi."

    huyen teasing "Ra mắt lại."

    tam irritated "Không phải ra mắt."

    huyen teasing "Mày chạy khỏi lần đầu."

    huyen grinning "Lần này tính là lần đầu hợp lệ."

    "Huyền lấy ra một chiếc váy màu trắng ngà."

    "Hàng hoa văn tím chạy ngang phần ngực và chân váy."

    tam irritated "Cầu kỳ quá."

    huyen teasing "Không."

    tam irritated "Có."

    huyen teasing "Anh chồng người ta nấu ăn."

    huyen teasing "Mày ít nhất nên trông như người có ý định ở lại đến hết bữa."

    tam irritated "Đừng gọi thế."

    "Huyền ướm chiếc váy lên người bạn."

    huyen happy "Bộ này."

    tam confused "Tao mặc quần được không?"

    huyen teasing "Không."

    tam confused "Tại sao?"

    huyen grinning "Tao đã chọn xong."

    "Tâm nhìn cô."

    tam teasing "Lý do rất thuyết phục."

    "Cuối cùng, Tâm vẫn thay váy."

    "Huyền khoác thêm cho cô một chiếc khăn voan mỏng."

    "Tiếng chuông cửa vang lên đúng lúc hai người đang tranh luận về đôi giày."

    "Hoàng đứng ngoài."

    "Cậu nhìn Tâm."

    "Rồi nhìn Huyền."

    hoang teasing "Có người giám sát nên hôm nay anh yên tâm hơn."

    tam irritated "Em không trốn."

    huyen teasing "Anh đừng tin."

    "Hoàng cười."

    "Hai mươi phút sau, xe dừng trước cổng nhà."

    "Tâm và Huyền xuống trước."

    "Hoàng tiếp tục lái xe vào gara."

    "Huyền nắm tay Tâm."

    tam irritated "Tao tự đi được."

    huyen neutral "Tao biết."

    "Cô vẫn không buông."

    "Hai người bấm chuông."

    "Minh ra mở cửa."

    "Huyền đứng yên."

    "Hai mắt mở to."

    "Phản ứng gần giống Tâm lần trước."

    "Chỉ thiếu chiếc taxi bên kia đường."

    "Minh nhìn hai cô gái."

    "Ánh mắt dừng ở Tâm trước."

    "Rồi chuyển sang Huyền."

    minh smile "Hai người vào đi."

    minh neutral "Ngoài này lạnh."

    "Huyền khẽ dạ."

    "Tâm cũng dạ."

    "Hai người đi vào nhà."

    "Minh để cửa mở cho Hoàng rồi quay vào bếp."

    minh neutral "Hai người cứ ngồi."

    minh neutral "Một lát nữa đồ ăn xong."

    "Huyền nhổm người."

    huyen neutral "Anh có cần bọn em giúp gì không?"

    minh neutral "Không cần."

    minh neutral "Hai người là khách."

    huyen smile "Vậy phiền anh."

    "Cô ngồi xuống cạnh Tâm."

    "Đợi Minh khuất vào bếp, Huyền nghiêng sang."

    huyen teasing "Ổn."

    tam irritated "Im."

    huyen teasing "Rất ổn."

    tam irritated "Tao về bây giờ."

    "Huyền lập tức kéo tay cô."

    huyen irritated "Không được."

    "Cô nhìn về phía bếp."

    huyen teasing "Vào giúp đi."

    tam neutral "Anh ấy bảo không cần."

    huyen teasing "Kiếm điểm với anh chồng."

    tam irritated "Huyền."

    "Huyền đứng dậy."

    "Cô kéo Tâm lên rồi đẩy nhẹ về phía bếp."

    huyen teasing "Cẩn thận không tối nay không có gì ăn."

    "Tâm đi được vài bước rồi quay lại."

    "Huyền khoát tay đuổi."

    "Tâm đành bước vào bếp."

    tam neutral "Anh có cần em giúp gì không?"

    "Minh đang đảo nồi canh."

    "Anh quay đầu nhìn."

    minh neutral "Không cần."

    minh neutral "Cũng sắp xong rồi."

    "Tâm đứng đó."

    "Rời đi ngay thì quá rõ."

    "Ở lại không làm gì cũng ngại."

    "Cô nhìn những động tác nhanh và gọn của Minh."

    "Anh không phải tìm dao."

    "Không phải nhìn lại gia vị."

    "Mọi thứ diễn ra như thể căn bếp luôn ở trong trí nhớ bàn tay."

    "Tâm mở tủ."

    "Cô lấy bát đĩa ra đặt lên bàn."

    "Một lúc sau, Hoàng đi vào."

    hoang neutral "Anh giúp."

    minh irritated "Mày tránh ra."

    hoang teasing "Nhà em."

    minh teasing "Bếp anh."

    "Tâm cúi mặt cười."

    "Hoàng nhìn cô."

    "Cậu không nhắc chuyện lần trước."

    "Chỉ đứng cạnh và nhận những chiếc bát cô đưa."

    "Mười phút sau, bốn người ngồi vào bàn."

    "Thịt viên."

    "Bò xào ớt tây."

    "Tôm rim đã bóc vỏ."

    "Canh chua đậu bắp."

    "Huyền nhìn bàn ăn."

    "Mắt sáng lên."

    huyen surprised "Em hỏi hơi vô duyên."

    huyen confused "Anh Minh từng làm đầu bếp à?"

    minh teasing "Từng chạy bàn."

    hoang teasing "Lão xoay sở nhanh hơn chút là mở nhà hàng được."

    "Huyền gắp một miếng."

    "Cô vừa nhai vừa định nói."

    tam irritated "Nuốt xong rồi nói."

    "Huyền nuốt."

    huyen happy "Ngon thật."

    huyen happy "Nếu không tận mắt nhìn thấy anh đứng bếp thì em không tin."

    minh neutral "Hoàng cũng nấu được."

    hoang neutral "Không ngon bằng lão."

    minh smile "Nhưng nó bày đẹp hơn."

    "Minh nhìn hai cô gái."

    minh teasing "Chẳng lẽ Hoàng chưa từng nấu cho hai người ăn?"

    "Bàn ăn im một nhịp."

    "Tâm và Huyền cùng nhìn Hoàng."

    "Hoàng nhìn anh trai."

    hoang irritated "Lão ăn đi."

    minh smile "Hiểu rồi."

    "Tâm nhớ đến nồi cháo trứng Hoàng từng nấu khi cô ốm."

    "Cô không nói."

    "Huyền tiếp tục ăn."

    huyen neutral "Em cứ nghĩ cha mẹ hai anh cũng ở trong thành phố."

    huyen confused "Sao anh Minh không về ở với hai bác?"

    minh neutral "Không thích."

    hoang neutral "Vì đây là nhà của lão."

    minh neutral "Chỉ đứng tên thôi."

    minh neutral "Mày sống ở đây nhiều hơn anh."

    "Hai cô gái dừng đũa."

    hoang neutral "Cả xe ngoài kia cũng của lão gửi về."

    minh neutral "Anh gửi cho mày."

    hoang neutral "Em thích motor hơn."

    minh irritated "Chở người yêu đi trời mưa bằng motor à?"

    hoang neutral "Mặc quần bò."

    minh confused "Khói bụi?"

    hoang neutral "Khẩu trang."

    minh confused "Trời lạnh?"

    hoang neutral "Áo khoác."

    minh teasing "Mưa?"

    "Hoàng im."

    "Huyền ghé sát Tâm."

    huyen teasing "Lần đầu tao thấy Hoàng cãi như trẻ con."

    "Tâm cười khúc khích."

    "Hoàng nghe thấy."

    hoang irritated "Hai người nói nhỏ hơn được không?"

    huyen teasing "Không."

    "Minh nghiêng sang em trai."

    minh teasing "Anh biết để người yêu ngồi sau ôm eo thì thích hơn."

    minh neutral "Nhưng yêu thì nghĩ cho người ta một chút."

    "Hoàng lườm anh."

    "Tâm cúi xuống bát."

    "Tai cô nóng lên."

    "Buổi tối tiếp tục trong tiếng nói chuyện."

    "Hoàng vẫn nói nhiều nhất."

    "Huyền cười rất tự nhiên."

    "Minh thi thoảng thêm một câu."

    "Tâm chủ yếu ăn."

    "Và thi thoảng nhìn người đàn ông đối diện."

    "Mỗi lần Minh nhìn lại, cô chuyển mắt sang món ăn."

    "Huyền nhận ra."

    "Cô chưa nói."

    "Sau bữa tối, bốn người ngồi thêm một lúc ở phòng khách."

    "Hoàng lái xe đưa hai cô gái về."

    "Huyền nói sẽ ngủ lại nhà Tâm."

    "Khi cửa căn hộ khép lại, cô ôm chầm lấy bạn."

    huyen happy "Đúng là hai anh em quái vật."

    tam confused "Gì nữa?"

    huyen grinning "Cái người như thế thì ai cưa cho nổi."

    tam teasing "Mày kết luận nhanh hơn hồi gặp Hoàng đấy."

    huyen neutral "Hoàng khó."

    huyen neutral "Minh là không có cửa."

    tam neutral "Mới gặp một tối."

    huyen neutral "Chính vì gặp một tối."

    "Huyền nằm dài trên sofa."

    huyen surprised "Anh ấy nhìn một cái là biết tao đang dò xét."

    huyen neutral "Nói chuyện thì nhẹ."

    huyen neutral "Nhưng không có chỗ chen."

    tam teasing "Thế mà vẫn mê."

    huyen irritated "Tao đang đánh giá."

    tam teasing "Ừ."

    huyen teasing "Còn mày."

    tam confused "Tao làm sao?"

    huyen teasing "Cứ len lén nhìn anh chồng."

    tam embarrassed "Đừng gọi thế."

    huyen teasing "Bị nhìn lại thì né."

    tam irritated "Tao đi tắm."

    "Tâm đứng dậy."

    "Huyền gọi theo."

    huyen surprised "Ơ. Ngồi nói thêm đã."

    "Cửa phòng tắm đóng lại."

    "Tâm tựa lưng lên cửa."

    "Cô không biết mình đang tránh Huyền."

    "Hay tránh câu hỏi mà Huyền chưa kịp hỏi."

    "Cùng lúc đó, ở nhà Hoàng, Minh đang đọc sách."

    hoang neutral "Lão thấy Tâm thế nào?"

    "Minh dời mắt khỏi trang giấy."

    minh neutral "Được."

    "Hoàng cười."

    "Một chữ ấy, từ Minh, đã đủ dài."

    minh neutral "Nhưng hơi khác anh nghĩ."

    hoang confused "Khác sao?"

    minh teasing "Anh tưởng người chịu được tính trẻ con của mày phải nhiệt tình hơn."

    minh neutral "Cô bé ít nói quá."

    hoang neutral "Ngại lão thôi."

    minh neutral "Có lẽ."

    "Minh lật trang."

    minh neutral "Cô bạn của Tâm."

    hoang confused "Huyền?"

    minh neutral "Ừ."

    minh neutral "Cô bé hay phán đoán người khác từ lần đầu."

    hoang confused "Sao lão biết?"

    minh neutral "Ánh mắt."

    "Hoàng im."

    minh neutral "Phán đoán không hẳn xấu."

    minh neutral "Nhưng tin vào nhận định của mình quá sớm thì dễ bỏ qua thứ tốt."

    "Hoàng nhìn về phía căn bếp đã tắt đèn."

    "Cậu không biết câu đó nói về Huyền."

    "Hay còn nói về ai khác."

    $ story_flag("four_person_weekend_dinner_completed")
    $ story_flag("tam_completed_first_minh_meeting")
    $ story_flag("huyen_first_meets_minh_at_family_dinner")
    $ story_flag("minh_character_profile_unlocked")
    $ story_flag("minh_first_seen_at_hoang_house")
    $ story_flag("minh_present_timeline_active")
    $ story_flag("minh_route_unlocked")
    $ story_flag("tam_minh_romance_observation_only")

    $ story_add("tam_observation", 10)
    $ story_add("tam_self_clarity", 5)
    $ story_add("tam_minh_drawn", 5)

    return


label tam_c06_minh_returns_s04_company_meeting_pending:
    scene black
    with fade

    "Chiều thứ Sáu, một lịch họp mới xuất hiện trong hộp thư của Tâm."

    "Thứ Hai."

    "Chín giờ sáng."

    "Project Partner Alignment."

    "Phòng họp lớn."

    "Danh sách người tham dự phía công ty đã có Quân, Tâm, Huyền và các đầu mối dự án."

    "Danh sách phía đối tác vẫn để trống."

    "Tâm mở phần mô tả."

    "Chỉ có ba dòng."

    "Thống nhất phạm vi."

    "Rà soát rủi ro."

    "Chốt cơ chế phối hợp trực tiếp."

    "Không có tên Minh."

    "Không có ảnh."

    "Không có gì để cô nhận ra."

    "Ở bàn bên cạnh, Huyền cũng vừa đọc xong."

    huyen neutral "Sắp biết rồi."

    tam confused "Biết gì?"

    if story_has_flag("huyen_fangirls_over_minh"):
        if not story_state.get("tam_c06_tam_other_romance_committed", False):
            huyen teasing "Đứa nào mê trai."
        else:
            huyen teasing "Đứa nào đứng hình."
    else:
        huyen neutral "Tin đồn nào đúng."

    tam irritated "Làm việc đi."

    "Huyền quay lại màn hình."

    "Nụ cười vẫn còn."

    "Tâm lưu lịch họp."

    "Cô kéo tài liệu chuẩn bị sang một bên."

    "Tuần sau, người của phía đối tác sẽ bước vào phòng họp."

    "Còn hiện tại, họ vẫn chỉ là hai ô trống trong danh sách khách mời."

    $ story_flag("major_partner_visit_announced")
    $ story_flag("minh_company_arrival_pending")
    $ story_flag("partner_alignment_meeting_scheduled")
    $ story_flag("minh_company_first_meeting_reserved_for_c07")

    # Intentionally do not set:
    # $ story_flag("minh_route_unlocked")
    #
    # Minh has not appeared to Tâm in this branch yet.

    return
