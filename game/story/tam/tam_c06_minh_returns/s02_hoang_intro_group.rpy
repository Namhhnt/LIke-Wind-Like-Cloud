# FILE: game/story/tam/tam_c06_minh_returns/s02_hoang_intro_group.rpy
# Home branch: canon door encounter.
# Company branch: Huyền provides side information depending on her maturity/routes.

label tam_c06_minh_returns_s02_hoang_intro_group:
    if story_state.get("tam_c06_branch", "company_setup") == "home":
        call tam_c06_minh_returns_s02_home_door
    else:
        call tam_c06_minh_returns_s02_company_side_information

    return


label tam_c06_minh_returns_s02_home_door:
    scene bg_hoang_house_front_door_day
    with fade

    "Tâm đổi hai túi đồ sang tay trái."

    "Cô bấm chuông cửa."

    "Không có động tĩnh."

    "Cô đợi một lúc rồi bấm lần thứ hai."

    "Tiếng chân từ trong nhà tiến lại gần."

    "Khóa cửa bật mở."

    "Người đứng sau cánh cửa không phải Hoàng."

    "Tâm khựng lại."

    "Người đàn ông trước mặt cũng dừng một nhịp."

    "Anh cao hơn Hoàng một chút."

    "Tóc dài hơn."

    "Khuôn mặt có những đường nét rất giống, nhưng vẻ trưởng thành khiến sự giống nhau trở nên khó gọi tên."

    "Tâm nhìn anh."

    "Không chớp."

    "Quai túi trên tay siết sâu thêm vào da."

    "Người đàn ông nhìn qua gương mặt cô, rồi nhìn hai túi thực phẩm."

    minh smile "Tâm phải không?"

    minh neutral "Vào đi."

    minh neutral "Hoàng nó đang tắm."

    "Tâm không trả lời."

    "Minh hơi nghiêng người, gỡ hai túi đồ khỏi tay cô."

    minh neutral "Đưa anh."

    "Anh quay vào trong."

    "Tâm nhìn theo bóng lưng ấy khuất sau cánh cửa."

    "Một dáng người."

    "Một giọng nói."

    "Và cảm giác rất rõ rằng cô đã biết người này trước khi được giới thiệu."

    "Cổ họng Tâm khô lại."

    "Cô quay đầu nhìn ra ngoài."

    "Chiếc taxi ban nãy vẫn đang đỗ bên kia đường."

    $ _tam_clarity_high = story_state.get("tam_self_clarity", 0) > 80

    if _tam_clarity_high:
        menu:
            "Chiếc taxi vẫn chưa rời đi."

            "Chạy về":
                call tam_c06_minh_returns_s02_flee_from_door

            "Dừng lại và quay vào nhà":
                call tam_c06_minh_returns_s02_stay_after_door
    else:
        call tam_c06_minh_returns_s02_flee_from_door

    return


label tam_c06_minh_returns_s02_flee_from_door:
    "Quyết định đến trước cả suy nghĩ."

    "Tâm quay người chạy khỏi cổng."

    "Cô gần như lao qua đường."

    "Người tài xế vừa khởi động xe thì cửa sau bị kéo mở."

    tam shocked "Anh cho em về chỗ cũ."

    "Người tài xế nhìn cô qua gương."

    "Không hỏi."

    "Chiếc taxi lăn bánh."

    "Tâm ép hai tay lên đầu gối."

    "Hai lòng bàn tay vẫn còn vết đỏ của quai túi."

    "Cô không mang theo đồ ăn."

    "Cũng chưa kịp gặp Hoàng."

    "Xe đi chưa được bao xa thì điện thoại rung."

    "Hoàng gọi."

    "Tâm nhìn tên anh hồi lâu."

    "Rồi mới bắt máy."

    hoang confused "Sao em đến nơi rồi lại bỏ về thế?"

    "Giọng anh vừa khó hiểu vừa lo."

    "Tâm dừng một giây."

    tam neutral "Em chợt nhớ ra nhà có chuyện nên phải về gấp."

    hoang confused "Thật không?"

    tam flustered "Thật mà anh."

    "Cô cười rất nhẹ."

    "Một nụ cười không ai nhìn thấy."

    tam flustered "Hẹn hai người hôm khác được không?"

    "Đầu dây bên kia im lặng."

    hoang neutral "Ừ."

    hoang neutral "Cuối tuần nhé?"

    hoang teasing "Em đừng viện cớ nữa đấy."

    tam neutral "Vâng."

    "Cuộc gọi kết thúc."

    "Tâm đặt điện thoại xuống ghế bên cạnh."

    "Màn hình vẫn sáng thêm vài giây."

    "Cô nhìn ra cửa kính."

    "Thành phố chạy lùi về phía sau."

    "Trong đầu cô, người đàn ông ở cửa vẫn đứng yên."

    $ story_state["tam_c06_home_outcome"] = "fled"
    $ story_flag("tam_fled_first_minh_meeting")
    $ story_flag("tam_left_before_meeting_hoang")
    $ story_flag("tam_used_family_emergency_excuse")
    $ story_flag("tam_minh_recognition_unspoken")
    $ story_flag("setup_four_person_weekend_dinner")

    $ story_add("tam_minh_drawn", 10)
    $ story_add("tam_insecurity", 5)
    $ story_add("doom_score", 5)

    call tam_c06_minh_returns_s02_brothers_after_flee

    return


label tam_c06_minh_returns_s02_brothers_after_flee:
    scene black
    with fade

    "Trong nhà, Hoàng đặt điện thoại xuống bàn."

    "Cậu nhìn về phía cửa."

    "Rồi quay sang bếp."

    hoang irritated "Này lão."

    minh neutral "Gì?"

    hoang confused "Anh làm gì khiến cô ấy sợ mà bỏ chạy thế?"

    "Minh đang lấy thực phẩm ra khỏi túi."

    "Anh ngẩng lên."

    minh laughing "Anh mới là người nên sợ."

    hoang confused "Sợ gì?"

    minh teasing "Cô ấy đứng nhìn anh như muốn nhớ lại kiếp trước."

    hoang irritated "Về đây thì nói tiếng Việt đi."

    minh neutral "Anh đang nói tiếng Việt."

    hoang irritated "Ý em là đừng nói nhảm."

    "Minh đặt mớ rau lên bàn."

    minh neutral "Anh mới nói được hai câu."

    hoang confused "Hai câu gì?"

    minh neutral "Tâm phải không."

    minh neutral "Vào đi."

    hoang confused "Thế mà cô ấy chạy?"

    minh neutral "Ừ."

    "Hoàng dựa lưng vào ghế."

    "Cậu nghĩ một lúc."

    hoang neutral "Sáng nay cô ấy còn rất hào hứng."

    minh neutral "Gọi lại hỏi đi."

    hoang neutral "Cô ấy nói nhà có việc."

    "Minh nhìn em trai."

    hoang irritated "Em biết."

    minh smile "Anh chưa nói gì."

    hoang irritated "Mặt lão nói rồi."

    "Minh quay lại bếp."

    "Tiếng dao chạm thớt vang lên đều."

    "Hơn một giờ sau, bàn ăn có nhiều món hơn hai người cần."

    "Hoàng ngồi xuống."

    hoang surprised "Nhiều thế?"

    minh teasing "Cảm ơn người yêu mày."

    minh neutral "Toàn chọn đồ tươi."

    minh neutral "Cô bé có vẻ biết nấu."

    hoang irritated "Có vẻ thôi à?"

    hoang teasing "Món Việt chưa chắc thua lão."

    minh teasing "Chưa cưới đã biết bênh."

    hoang teasing "Dù gì lão cũng không nấu cho em ăn cả đời."

    minh irritated "Vô ơn."

    "Hoàng cười."

    "Nhưng khi nhìn chiếc ghế trống đối diện, nụ cười dịu xuống."

    hoang neutral "Lão thấy cô ấy thế nào?"

    minh neutral "Chưa đủ lâu để thấy gì."

    "Minh gắp thức ăn."

    minh neutral "Nhìn được."

    hoang irritated "Khó tính."

    minh teasing "Có điều thú vị."

    hoang confused "Gì?"

    minh teasing "Thấy anh trai người yêu mà nhìn chằm chằm như thế."

    "Hoàng lườm anh."

    minh smile "Anh đùa."

    "Minh nói vậy."

    "Giọng không giống đùa hoàn toàn."

    $ story_flag("minh_cooks_tam_groceries_after_flee")
    $ story_flag("hoang_knows_tam_excuse_was_false")

    return


label tam_c06_minh_returns_s02_stay_after_door:
    "Tâm đã bước được hai bước ra phía cổng."

    "Cô dừng lại."

    "Theo thói quen, bàn tay cô khép lại để giữ quai túi."

    "Chỉ chạm vào khoảng không."

    "Hai túi thực phẩm đã ở trong nhà."

    "Chi tiết nhỏ ấy kéo cô trở lại."

    "Tâm nhìn chiếc taxi."

    "Rồi nhìn cánh cửa vẫn chưa khép hẳn."

    "Cô đứng giữa lối đi."

    "Cuối cùng, chiếc taxi rời đi trước."

    "Tâm quay lại."

    "Minh đang đặt thực phẩm lên bàn bếp."

    "Anh nhìn cô bước vào."

    "Không hỏi vì sao cô vừa biến mất."

    minh neutral "Hoàng còn ở trên tầng."

    tam neutral "Vâng."

    "Tâm đứng gần bàn."

    tam neutral "Em giúp anh."

    minh neutral "Không cần."

    tam neutral "Em đã mua đồ."

    minh neutral "Vậy càng không cần làm thêm."

    "Tâm vẫn chưa ngồi."

    "Minh nhìn cô."

    minh neutral "Em chắc mình ổn chứ?"

    tam flustered "Em ổn."

    "Câu trả lời nhanh hơn bình thường."

    minh neutral "Ừ."

    "Anh không hỏi tiếp."

    "Tâm không biết mình thấy nhẹ nhõm hay hụt vì điều đó."

    "Tiếng chân từ cầu thang vang xuống."

    "Hoàng xuất hiện, tóc còn ướt."

    hoang neutral "Em đến lâu chưa?"

    tam flustered "Chưa."

    "Hoàng đi tới."

    "Cậu nhìn Minh rồi nhìn Tâm."

    hoang smile "Anh Minh."

    hoang smile "Đây là Tâm."

    hoang smile "Người yêu em."

    "Tâm nhìn Hoàng."

    "Anh nói ba chữ ấy rất tự nhiên."

    "Như thể chúng vốn đã có một chỗ trong căn nhà."

    minh smile "Anh biết."

    hoang confused "Hai người nói chuyện rồi à?"

    minh neutral "Một chút."

    "Tâm không sửa."

    "Hoàng kéo chiếc ghế cạnh bàn."

    hoang neutral "Em ngồi đi."

    tam neutral "Em giúp nấu."

    hoang neutral "Anh giúp."

    minh irritated "Hai người ra ngoài cả đi."

    hoang teasing "Nhà em."

    minh teasing "Bếp anh."

    "Hoàng nhìn Tâm."

    hoang neutral "Em thấy chưa."

    tam smile "Em thấy rồi."

    "Giọng cô nhỏ."

    "Nhưng lần này đã trở lại là giọng của cô."

    $ story_state["tam_c06_home_outcome"] = "stayed"
    $ story_flag("tam_stayed_after_first_minh_door_shock")
    $ story_flag("hoang_introduces_tam_as_girlfriend")
    $ story_flag("minh_first_meeting_at_hoang_house")

    return


label tam_c06_minh_returns_s02_company_side_information:
    scene bg_company_open_office_day
    with fade

    $ _huyen_quan_mature = story_state.get("tam_c06_huyen_quan_mature", False)
    $ _huyen_met_minh = story_state.get("tam_c06_huyen_met_minh", False)

    if _huyen_met_minh:
        call tam_c06_minh_returns_s02_huyen_fangirl_report

        if _huyen_quan_mature:
            call tam_c06_minh_returns_s02_huyen_accurate_partner_info

    elif _huyen_quan_mature:
        call tam_c06_minh_returns_s02_huyen_accurate_partner_info

    else:
        call tam_c06_minh_returns_s02_generic_company_rumor

    return


label tam_c06_minh_returns_s02_huyen_fangirl_report:
    "Huyền nhìn quanh."

    "Cô kéo ghế sát hơn."

    huyen happy "Tao gặp anh Minh rồi."

    tam confused "Anh của Hoàng?"

    huyen neutral "Ừ."

    tam confused "Và?"

    "Huyền đặt hai tay lên bàn."

    huyen grinning "Và cái người đó hơi quá đáng."

    tam confused "Anh ấy làm gì cậu?"

    huyen teasing "Không làm gì cả."

    huyen grinning "Thế mới quá đáng."

    "Tâm nhìn cốc cà phê của bạn."

    tam teasing "Cậu uống mấy cốc rồi?"

    huyen irritated "Nghe tao kể đã."

    "Huyền gặp Minh khi sang chỗ Hoàng."

    "Cuộc trò chuyện bắt đầu từ một câu than vãn rất bình thường."

    "Dự án của cô bị sửa đến lần thứ ba."

    "Mỗi người duyệt đưa một ý."

    "Đội vừa sửa xong theo người này thì người khác lại yêu cầu quay về bản cũ."

    huyen happy "Tao mới kể đến lần sửa thứ ba."

    huyen happy "Anh ấy hỏi đúng một câu."

    huyen neutral "Ai là người có quyền chốt bản cuối?"

    tam confused "Cậu trả lời sao?"

    huyen surprised "Tao đứng hình."

    tam confused "Vì không biết?"

    huyen frustrated "Vì đúng là chẳng có ai chốt cả."

    "Huyền bắt chước giọng Minh, thấp hơn bình thường một cách rất vụng."

    huyen neutral "Đừng coi mọi phản hồi là yêu cầu."

    huyen neutral "Tách chúng ra."

    huyen neutral "Cái nào đã xác nhận."

    huyen neutral "Cái nào chỉ là giả định."

    huyen neutral "Cái nào còn đang tranh luận."

    huyen neutral "Mỗi dòng phải có tên người chịu trách nhiệm quyết định."

    tam confused "Rồi sao?"

    huyen neutral "Rồi mang sang hỏi anh Quân."

    huyen neutral "Khóa ba tiêu chí quan trọng nhất trước vòng sửa tiếp theo."

    huyen neutral "Không được sửa tiếp chỉ để làm hài lòng tất cả nếu các phản hồi tự mâu thuẫn."

    "Tâm ngừng gõ bàn phím."

    tam neutral "Nghe hợp lý."

    huyen surprised "Không chỉ hợp lý."

    huyen happy "Tao làm thử rồi."

    huyen happy "Buổi họp chiều qua giảm gần nửa thời gian."

    tam teasing "Mày thổi phồng vừa thôi."

    huyen irritated "Thề! Tao chỉ đang nói chuyện công việc."

    tam teasing "Đồ mê trai."

    huyen irritated "Tao mới kể đúng sự thật."

    tam teasing "Ừ."

    tam teasing "Sự thật cao khoảng mét tám, giọng trầm, nhìn một cái là biết vấn đề?"

    "Huyền dựa lưng vào ghế."

    huyen teasing "Mày cứ cười đi."

    if not story_state.get("tam_c06_tam_other_romance_committed", False):
        huyen teasing "Cứ đợi sang tuần đi rồi biết đứa nào mê trai."
    else:
        huyen teasing "Cứ đợi sang tuần đi rồi biết đứa nào đứng hình."

    tam irritated "Không có chuyện đó."

    huyen neutral "Ừ."

    huyen teasing "Tao cũng từng nghĩ tao chỉ sang uống nước."

    "Tâm lắc đầu."

    "Cô quay lại màn hình."

    "Sau vài giây, cô mở một tài liệu mới."

    "Các cột đầu tiên được đặt tên:"

    "Đã xác nhận."

    "Giả định."

    "Còn tranh luận."

    "Huyền nhìn thấy."

    huyen smile "Không mê trai."

    tam irritated "Im."

    $ story_flag("huyen_met_minh_before_tam")
    $ story_flag("huyen_fangirls_over_minh")
    $ story_flag("huyen_shared_minh_work_advice")
    $ story_flag("tam_curious_about_minh_from_huyen")
    $ story_add("career_huyen", 5)

    return


label tam_c06_minh_returns_s02_huyen_accurate_partner_info:
    "Huyền hạ giọng."

    "Sự phấn khích, nếu có, được cất sang một bên."

    huyen neutral "Phần tao biết chắc là thế này."

    huyen neutral "Sang tuần có hai người từ phía đối tác sang."

    tam surprised "Hai?"

    huyen neutral "Một nam, một nữ."

    huyen neutral "Người nam là người Việt."

    huyen neutral "Làm ở nước ngoài lâu rồi, nhưng không lạ dự án trong nước."

    tam confused "Tên?"

    huyen neutral "Chưa có trong thông báo chính thức."

    tam confused "Cậu lấy thông tin từ đâu?"

    huyen teasing "Nguồn đáng tin."

    tam teasing "Anh Quân?"

    huyen irritated "Tao không nói."

    tam teasing "Cậu vừa xác nhận."

    "Huyền kéo một tập tài liệu che nửa mặt."

    huyen neutral "Hai người là thật."

    huyen neutral "Còn chuyện người nam làm việc áp lực hơn anh Quân thì tao chưa kiểm chứng."

    tam teasing "Hiếm khi thấy cậu có trách nhiệm với tin đồn thế."

    huyen grinning "Trưởng thành rồi."

    tam teasing "Từ bao giờ?"

    huyen tired "Từ lúc phải sửa cùng một bản ba lần."

    "Tâm cười."

    "Cô ghi lại hai dòng vào sổ."

    "Hai đại diện."

    "Một nam, một nữ."

    "Không thêm phần chưa được xác nhận."

    $ story_flag("huyen_shares_accurate_partner_information")
    $ story_flag("partner_team_one_man_one_woman")
    $ story_add("career_huyen", 5)
    $ story_add("tam_observation", 5)

    return


label tam_c06_minh_returns_s02_generic_company_rumor:
    huyen neutral "Nghe nói phía đối tác cử người sang."

    tam confused "Bao nhiêu người?"

    huyen neutral "Không biết."

    tam confused "Ai?"

    huyen neutral "Không biết."

    tam confused "Làm gì?"

    huyen tired "Làm đội mình khổ."

    "Tâm nhìn cô."

    tam confused "Thế cậu biết được gì?"

    huyen teasing "Biết tuần sau không nên xin nghỉ."

    tam teasing "Thông tin rất có giá trị."

    huyen grinning "Không cần cảm ơn."

    "Hai người quay lại làm việc."

    "Ngoài hành lang, câu chuyện về đối tác vẫn tiếp tục tự lớn lên."

    $ story_flag("company_partner_information_still_vague")

    return
