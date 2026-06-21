default tam_salary_tier = "standard"
default tam_work_skill = 0
default tam_confidence = 0
default huyen_trust = 0
default hoang_impression = 0

define tam = Character("Tâm")
define huyen = Character("Huyền")
define hr = Character("Chị tuyển dụng")
define interviewer = Character("Người phỏng vấn")
define manager = Character("Trưởng phòng")
define hoang_unknown = Character("Chàng trai kỳ lạ")
define hoang = Character("Hoàng")
define narrator = Character(None)

label tam_c01:

    scene black
    with fade

    narrator "Chương 01"
    narrator "Ngày Đầu Tiên Gió Đổi Chiều"

    scene bg_tam_room_morning
    with dissolve

    narrator "Buổi sáng hôm ấy, Tâm thức dậy sớm hơn báo thức mười phút."

    narrator "Ngoài cửa sổ, thành phố còn chưa hẳn tỉnh. Một lớp sáng mỏng phủ lên những mái nhà san sát, lặng lẽ như ai đó vừa kéo rèm cho một ngày mới."

    narrator "Trên bàn học của cô là một tập hồ sơ đã được kẹp ngay ngắn. CV. Đơn ứng tuyển. Một bản photo bằng tốt nghiệp. Vài chứng chỉ nhỏ không chắc có giúp ích gì không, nhưng bỏ ra thì lại thấy thiếu."

    narrator "Tâm nhìn chúng rất lâu."

    tam "Phòng triển khai dự án..."

    narrator "Tên vị trí nghe không quá xa lạ. Nhưng công ty thì khác."

    narrator "Một công ty đầu tư đa ngành. Có xây dựng. Có vật liệu. Có phòng IT. Có pháp lý. Có kế toán. Có quản lý chất lượng. Có cả những phòng ban mà chỉ đọc tên thôi Tâm đã thấy mình cần thêm một tách cà phê để không bỏ cuộc giữa chừng."

    narrator "Cô không phải kiểu người sợ việc khó."

    narrator "Chỉ là cô hơi sợ những thứ mình chưa nắm rõ."

    play sound "audio/phone_vibrate.ogg"

    narrator "Điện thoại rung lên trên mặt bàn."

    huyen "Dậy chưa bà nội?"

    tam "Dậy rồi."

    huyen "Tốt. Tao đang ở dưới nhà mày. Xuống đi. Nếu để tao đi phỏng vấn một mình, tao sẽ trù mày được nhận vào phòng kế toán và phải làm bảng lương đến hết đời."

    tam "Mày ác vừa thôi."

    huyen "Xuống nhanh. Tao mua bánh mì."

    narrator "Tâm bật cười."

    narrator "Có những người chỉ cần xuất hiện qua một dòng tin nhắn, không khí trong lòng người khác đã bớt nặng đi một chút."

    scene bg_apartment_lobby_morning
    with dissolve

    narrator "Huyền đứng ở sảnh chung cư, một tay cầm hai ổ bánh mì, tay kia ôm túi hồ sơ trước ngực như ôm phao cứu sinh."

    huyen "Tao nói thật nhé, tim tao đang đập như chạy deadline cuối quý."

    tam "Mày cũng biết sợ cơ à?"

    huyen "Tao biết sợ chứ. Tao chỉ giấu giỏi hơn mày thôi."

    narrator "Tâm nhận ổ bánh mì từ tay Huyền. Còn nóng. Giấy gói thấm một chút dầu, mùi pate và rau mùi bốc lên giản dị đến mức làm người ta thấy cuộc đời vẫn còn cứu được."

    huyen "Này, lát nữa nếu người ta hỏi vì sao muốn vào phòng triển khai dự án, mày định nói gì?"

    tam "Tao vẫn đang nghĩ."

    huyen "Vậy là chưa nghĩ xong."

    tam "Tao nghĩ rồi. Chỉ là chưa sắp xếp được."

    huyen "Đấy. Khác gì chưa nghĩ xong đâu."

    narrator "Tâm im lặng một chút. Huyền liếc cô, ánh mắt vừa trêu vừa thật sự quan tâm."

    menu:
        "Tâm nên đáp lại Huyền thế nào?"

        "Thừa nhận mình cũng lo, rồi rủ Huyền cùng rà lại ý chính.":
            $ huyen_trust += 1
            $ add_unique(progress["player_flags"], "tam_huyen_shared_anxiety")
            tam "Ừ, tao cũng lo. Hay trên đường đi mình rà lại với nhau một lượt đi. Mày nghe giúp tao xem có chỗ nào ngớ ngẩn không."
            huyen "Được đấy. Ít ra hôm nay tao có cảm giác mình là bạn thân chứ không phải NPC phát bánh mì."

        "Tỏ ra tự tin để Huyền bớt lo.":
            tam "Không sao đâu. Tao nghĩ vào đó ứng biến được."
            huyen "Nghe thì cũng ngầu đấy. Nhưng tao ghét nhất chữ ứng biến trước phỏng vấn."
            narrator "Huyền nói vậy, nhưng cũng không ép thêm."

        "Bảo Huyền đừng làm mình căng thẳng thêm.":
            $ huyen_trust -= 1
            tam "Mày đừng hỏi nữa. Tao đang cố không căng thẳng đây."
            huyen "Ờ... xin lỗi."
            narrator "Câu trả lời rơi xuống giữa hai người hơi cụt. Không nặng nề. Chỉ là hơi lạnh đi một nhịp."

    scene bg_company_lobby_morning
    with fade

    narrator "Công ty nằm trong một tòa nhà văn phòng lớn, mặt kính sáng đến mức Tâm nhìn thấy bóng mình phản chiếu trên đó."

    narrator "Áo sơ-mi trắng. Chân váy tối màu. Tóc buộc gọn sau gáy. Một vẻ ngoài vừa đủ nghiêm túc, vừa đủ trẻ để người ta không đoán chắc cô đã thật sự sẵn sàng bước vào một guồng máy lớn."

    narrator "Ở quầy lễ tân, Huyền ghé sát tai cô."

    huyen "Tao vừa thấy một anh đi qua đeo thẻ phòng pháp lý. Mặt lạnh như văn bản từ chối thanh toán."

    tam "Mày đừng làm tao cười."

    huyen "Cười cho bớt run. Khoa học chưa chứng minh nhưng tao chứng minh bằng kinh nghiệm cá nhân rồi."

    narrator "Tâm mím môi, nhưng khóe miệng vẫn không nhịn được cong lên."

    scene bg_interview_waiting_room
    with dissolve

    narrator "Phòng chờ phỏng vấn yên tĩnh."

    narrator "Trên tường treo những bức ảnh về công trình, nhà máy vật liệu, một khu văn phòng đang thi công, và vài màn hình dashboard nội bộ hiện những con số mà Tâm chưa kịp hiểu."

    narrator "Có lẽ đây không phải một nơi chỉ cần biết gõ văn bản và gửi email."

    narrator "Càng nhìn, Tâm càng hiểu vị trí mình ứng tuyển nằm ở giữa rất nhiều dòng chảy."

    narrator "Tiến độ. Hồ sơ. Vật tư. Pháp lý. Chi phí. Chất lượng. Con người."

    narrator "Một mắt xích nhỏ, nhưng nếu lệch, rất nhiều thứ phía sau cũng lệch theo."

    play sound "audio/door_open.ogg"

    hr "Bạn Tâm, mời em vào phòng."

    narrator "Tâm đứng dậy."

    narrator "Huyền ngồi bên cạnh khẽ giơ nắm tay."

    huyen "Cố lên. Đừng bán đứng tao."

    tam "Tao vào phỏng vấn chứ có vào phòng thẩm vấn đâu."

    huyen "Khác nhau ở chỗ nào?"

    narrator "Tâm bật cười rất khẽ, rồi bước vào."

    scene bg_interview_room
    with dissolve

    interviewer "Chào em. Em cứ ngồi thoải mái."

    manager "Bọn anh đã xem qua hồ sơ của em. Vị trí triển khai dự án bên anh không chỉ làm giấy tờ. Nó cần phối hợp với nhiều phòng ban. Em hiểu công việc này như thế nào?"

    narrator "Câu hỏi đến sớm hơn Tâm tưởng."

    narrator "Cô đặt hai tay lên đùi, ngón cái khẽ miết vào nhau."

    narrator "Đây không phải lúc để nói lan man."

    narrator "Cô cần sắp xếp ý."

    jump tam_c01_speech_game


label tam_c01_speech_game:

    $ tam_speech_attempts = 0

label tam_c01_speech_retry:

    $ tam_speech_order = []
    $ tam_speech_required = ["context", "coordination", "risk", "commitment"]

    narrator "Mini-game: Sắp xếp các ý chính cho phần trả lời phỏng vấn."
    narrator "Chọn 4 ý cần trình bày. Nếu chọn đủ ý đúng thì pass. Nếu đúng cả ý lẫn thứ tự thì nhận bonus."

    while len(tam_speech_order) < 4:

        menu:
            "Chọn ý tiếp theo trong phần trả lời:"

            "Hiểu đặc thù công ty đa ngành: triển khai dự án là điểm nối giữa xây dựng, vật liệu, IT, pháp lý, kế toán và quản lý chất lượng." if "context" not in tam_speech_order:
                $ tam_speech_order.append("context")

            "Nhấn mạnh năng lực phối hợp: theo dõi tiến độ, tổng hợp thông tin, làm rõ đầu việc và giữ luồng trao đổi giữa các phòng ban." if "coordination" not in tam_speech_order:
                $ tam_speech_order.append("coordination")

            "Nói về tư duy rủi ro: phát hiện vướng mắc sớm, báo cáo minh bạch, không để lỗi nhỏ thành vấn đề lớn." if "risk" not in tam_speech_order:
                $ tam_speech_order.append("risk")

            "Kết lại bằng thái độ làm việc: học nhanh, chịu khó đi hiện trường khi cần, tôn trọng quy trình và chịu trách nhiệm với phần việc của mình." if "commitment" not in tam_speech_order:
                $ tam_speech_order.append("commitment")

            "Nói rằng mức lương là điều em quan tâm nhất vì em muốn được đánh giá đúng giá trị." if "salary_first" not in tam_speech_order:
                $ tam_speech_order.append("salary_first")

            "Khẳng định em có thể tự xử lý mọi việc mà không cần làm phiền phòng ban khác." if "solo" not in tam_speech_order:
                $ tam_speech_order.append("solo")

            "Tập trung kể về điểm mạnh cá nhân và thành tích học tập, không cần đi sâu vào yêu cầu công việc." if "self_only" not in tam_speech_order:
                $ tam_speech_order.append("self_only")

    $ tam_speech_has_required = all(x in tam_speech_order for x in tam_speech_required)
    $ tam_speech_perfect_order = tam_speech_order == tam_speech_required

    if tam_speech_has_required:

        if tam_speech_perfect_order:
            $ tam_salary_tier = "high"
            $ tam_work_skill += 2
            $ tam_confidence += 2
            $ add_unique(progress["player_flags"], "tam_interview_passed")
            $ add_unique(progress["player_flags"], "tam_interview_bonus_order")
            $ add_unique(progress["player_flags"], "tam_salary_high_start")
            $ add_unique(progress["player_flags"], "tam_work_skill_strong_c01")

            narrator "Các ý được đặt đúng thứ tự."
            narrator "Tâm mở đầu bằng việc hiểu bức tranh lớn, sau đó đi vào năng lực phối hợp, tư duy rủi ro, rồi mới kết lại bằng thái độ làm việc."
            narrator "Một câu trả lời không quá hoa mỹ. Nhưng gọn, có trục, và không bị rơi vào kiểu tự quảng cáo non tay."

            jump tam_c01_interview_perfect

        else:
            $ tam_salary_tier = "standard"
            $ tam_work_skill += 1
            $ tam_confidence += 1
            $ add_unique(progress["player_flags"], "tam_interview_passed")
            $ add_unique(progress["player_flags"], "tam_salary_standard_start")

            narrator "Các ý quan trọng đều có mặt, nhưng thứ tự trình bày chưa thật sự sắc."
            narrator "Dù vậy, Tâm vẫn cho thấy cô hiểu công việc và có thái độ nghiêm túc."

            jump tam_c01_interview_pass

    else:

        $ tam_speech_attempts += 1

        if tam_speech_attempts < 3:
            narrator "Câu trả lời bị lệch trọng tâm."
            narrator "Hội đồng không khó chịu, nhưng ánh mắt họ đủ khiến Tâm hiểu mình vừa đi sai hướng."
            narrator "Thử lại."
            jump tam_c01_speech_retry

        else:
            narrator "Tâm đã thất bại 3 lần trong phần sắp xếp ý."
            narrator "Có thể chơi lại để lấy bonus, hoặc skip để pass nhưng không nhận điểm thưởng."

            menu:
                "Chọn cách xử lý:"

                "Chơi lại mini-game":
                    jump tam_c01_speech_retry

                "Skip — pass không bonus":
                    $ tam_salary_tier = "standard"
                    $ add_unique(progress["player_flags"], "tam_interview_pass_skip_no_bonus")
                    $ add_unique(progress["player_flags"], "tam_salary_standard_start")
                    narrator "Tâm hít sâu, bỏ qua sự hoàn hảo mà mình vẫn luôn muốn giữ."
                    narrator "Cô trả lời theo cách an toàn hơn, vừa đủ để không bị loại, nhưng cũng không tạo được điểm sáng đặc biệt."
                    jump tam_c01_interview_skip


label tam_c01_interview_perfect:

    tam "Em nghĩ vị trí triển khai dự án không chỉ là truyền đạt thông tin từ bên này sang bên kia."

    tam "Với một công ty có nhiều mảng như xây dựng, vật liệu, IT, pháp lý, kế toán và quản lý chất lượng, người ở phòng triển khai cần hiểu được việc của mình nằm ở đâu trong toàn bộ dòng chảy dự án."

    tam "Nếu em không hiểu bối cảnh, em sẽ chỉ chuyển tiếp thông tin. Nhưng nếu hiểu bối cảnh, em có thể biết thông tin nào cần làm rõ, phòng ban nào cần được cập nhật, và rủi ro nào nên được báo sớm."

    tam "Em chưa có nhiều kinh nghiệm thực tế, nhưng em có khả năng tổng hợp, theo dõi chi tiết, và em không ngại học quy trình từ đầu."

    tam "Em muốn làm tốt phần việc của mình theo cách đáng tin cậy. Không ồn ào, nhưng rõ ràng và có trách nhiệm."

    manager "Cách em trả lời khá có cấu trúc."

    interviewer "Và thực tế hơn anh chị nghĩ."

    narrator "Tâm thấy vai mình nhẹ đi một chút."

    narrator "Không phải vì cô chắc chắn mình đã thắng."

    narrator "Chỉ là lần đầu tiên trong buổi sáng hôm ấy, cô thấy mình đang đứng đúng chỗ."

    jump tam_c01_after_interview


label tam_c01_interview_pass:

    tam "Em nghĩ công việc triển khai dự án cần khả năng phối hợp và theo dõi chi tiết."

    tam "Công ty mình có nhiều phòng ban liên quan đến từng dự án, nên nếu thông tin không rõ ràng hoặc cập nhật chậm, tiến độ chung có thể bị ảnh hưởng."

    tam "Em muốn học cách nắm quy trình, hỗ trợ các bên làm việc với nhau tốt hơn và báo cáo kịp thời khi có vướng mắc."

    manager "Tốt. Câu trả lời hơi vòng một chút, nhưng ý chính ổn."

    interviewer "Chị đánh giá cao việc em có nhắc đến phối hợp liên phòng ban."

    narrator "Tâm gật đầu."

    narrator "Cô biết mình chưa thật xuất sắc, nhưng ít nhất không bị trôi."

    jump tam_c01_after_interview


label tam_c01_interview_skip:

    tam "Em nghĩ vị trí này cần sự cẩn thận, khả năng phối hợp và tinh thần học hỏi."

    tam "Em chưa có nhiều kinh nghiệm, nhưng em sẵn sàng học quy trình, hỗ trợ công việc và làm theo hướng dẫn của cấp trên."

    manager "Được."

    narrator "Một câu trả lời an toàn."

    narrator "Không sai. Nhưng cũng không để lại nhiều dư âm."

    jump tam_c01_after_interview


label tam_c01_after_interview:

    scene bg_company_lobby_noon
    with dissolve

    narrator "Khi Tâm bước ra khỏi phòng, Huyền đã đứng bật dậy như lò xo."

    huyen "Sao rồi?"

    tam "Chưa biết."

    huyen "Mặt mày nhìn không tệ. Tức là không bị loại ngay tại cửa."

    tam "Cảm ơn vì lời động viên rất có giá trị tinh thần."

    huyen "Không có gì. Tao tính phí theo giờ."

    narrator "Hai người ngồi xuống hàng ghế dài ở sảnh. Bên ngoài lớp kính, nắng trưa bắt đầu rơi thành từng mảng gắt."

    huyen "Tao run quá."

    tam "Đến lượt mày rồi à?"

    huyen "Ừ. Nếu tao chết trong đó, nhớ xóa lịch sử tìm kiếm của tao."

    menu:
        "Tâm nên động viên Huyền thế nào?"

        "Nhắc Huyền bình tĩnh và dùng thế mạnh thật của mình.":
            $ huyen_trust += 1
            $ add_unique(progress["player_flags"], "tam_supported_huyen_interview")
            tam "Mày không cần cố tỏ ra giỏi hơn con người thật của mày đâu. Mày nói chuyện tự nhiên, bắt ý nhanh, lại nhớ chi tiết tốt. Cứ dùng đúng mấy thứ đó."
            huyen "Nghe hơi giống lời thoại trong phim thanh xuân, nhưng... có ích thật."
            tam "Đi đi. Đừng làm xấu mặt bánh mì ban sáng."

        "Trêu Huyền để cô ấy bớt căng.":
            tam "Không sao. Nếu mày trượt, tao sẽ kể chuyện này trong đám cưới mày."
            huyen "Mày đúng là bạn thân kiểu cần cho vào danh sách rủi ro dự án."
            narrator "Huyền bật cười. Căng thẳng trong mắt cô vơi đi một chút."

        "Bảo Huyền tự lo vì ai cũng phải tự vượt qua.":
            $ huyen_trust -= 1
            tam "Tao cũng không biết khuyên gì. Mày tự lo đi. Ai cũng phải tự qua phần của mình mà."
            huyen "Ờ. Tao hiểu."
            narrator "Huyền cười, nhưng nụ cười hơi mỏng."

    narrator "Huyền đi vào phòng phỏng vấn."

    narrator "Tâm ngồi lại một mình."

    narrator "Sảnh công ty bỗng rộng hơn hẳn khi không còn tiếng Huyền nói bên cạnh."

    scene bg_company_lobby_afternoon
    with dissolve

    narrator "Kết quả được thông báo vào cuối buổi chiều."

    narrator "Cả hai cùng trúng tuyển."

    narrator "Tâm đọc email hai lần. Huyền đọc bốn lần. Sau đó hai đứa nhìn nhau vài giây, rồi cùng bật cười như hai kẻ vừa thoát khỏi một vụ tai nạn không nghiêm trọng nhưng đủ làm tim rơi xuống tận đầu gối."

    huyen "Tối nay ăn mừng."

    tam "Ăn gì?"

    huyen "Sang."

    tam "Mày vừa mới được nhận việc đã muốn phá sản à?"

    huyen "Không. Tao gọi đó là đầu tư vào tinh thần trước khi bị doanh nghiệp nghiền nát."

    narrator "Tâm thấy lập luận ấy sai sai."

    narrator "Nhưng cũng khá thuyết phục."

    if tam_salary_tier == "high":
        narrator "Email offer của Tâm có mức lương khởi điểm cao hơn kỳ vọng."
        narrator "Một con số không đến mức khiến cô đổi đời, nhưng đủ để cô nhìn màn hình thêm vài giây, cảm thấy lòng mình sáng lên như vừa có ai mở cửa sổ."

        menu:
            "Tâm nên nói với Huyền về mức lương thế nào?"

            "Chia sẻ thật, nhưng không làm Huyền thấy bị so sánh.":
                $ huyen_trust += 1
                $ add_unique(progress["player_flags"], "tam_shared_salary_with_care")
                tam "Tao được offer cao hơn tao tưởng một chút."
                huyen "Thật á? Bao nhiêu?"
                tam "Tao nói mày nghe, nhưng không phải để khoe đâu nhé. Tao cũng hơi bất ngờ."
                huyen "Con điên. Mày được offer cao thì tao mừng chứ. Sau này nhớ bao tao trà sữa size lớn."
                tam "Đấy mới là mục đích thật của mày đúng không?"
                huyen "Bạn thân là phải biết biến niềm vui của nhau thành đồ uống."

            "Giấu đi để tránh Huyền buồn.":
                $ huyen_trust -= 1
                $ add_unique(progress["player_flags"], "tam_hid_salary_from_huyen")
                tam "Cũng bình thường thôi."
                narrator "Tâm nói vậy. Nhưng cô biết mình vừa giấu Huyền một điều không quá cần phải giấu."
                narrator "Sự im lặng nhỏ ấy nằm lại giữa hai người như một cái ghim lệch."

            "Khoe thẳng vì mình xứng đáng.":
                $ huyen_trust -= 1
                tam "Tao được offer cao hơn. Chắc tại phần phỏng vấn tốt thật."
                huyen "Ờ. Mày giỏi mà."
                narrator "Huyền vẫn cười. Nhưng giọng cô bớt sáng đi một chút."

    else:
        narrator "Mức lương khởi điểm của Tâm ở mức tiêu chuẩn."
        narrator "Không cao đến mức khiến cô reo lên, cũng không thấp đến mức làm cô thất vọng."
        narrator "Vừa đủ. Như một cánh cửa mở ra không quá rộng, nhưng rõ ràng là đã mở."

    if huyen_trust >= 2:
        $ add_unique(progress["player_flags"], "huyen_trust_high_c01")
        $ add_unique(progress["player_flags"], "huyen_advice_work_unlocked")
        $ add_unique(progress["player_flags"], "huyen_advice_relationship_unlocked")
        narrator "Từ hôm đó, Huyền bắt đầu tin Tâm theo một cách khác."
        narrator "Không chỉ là bạn thân để cùng cười, cùng than, cùng ăn những bữa vô nghĩa sau giờ làm."
        narrator "Mà còn là người có thể nói thật, nghe thật, và giữ lại cho nhau vài lời khuyên đúng lúc."

    scene bg_luxury_restaurant_evening
    with fade

    narrator "Tối hôm đó, hai người chọn một nhà hàng sang trọng hơn mức cần thiết."

    narrator "Đèn vàng. Khăn trải bàn trắng. Ly thủy tinh trong suốt đến mức Tâm sợ mình chỉ cần cầm mạnh tay một chút cũng có thể để lộ sự quê mùa vừa kịp giấu đi."

    huyen "Này."

    tam "Gì?"

    huyen "Chúng ta chính thức là người lớn rồi đấy."

    tam "Chỉ vì được nhận việc?"

    huyen "Ừ. Người lớn là những sinh vật vui mừng khi nhận được email bắt đầu chuỗi ngày bán linh hồn cho bảng biểu."

    tam "Nghe bi quan quá."

    huyen "Nhưng tao nói trong nhà hàng sang, nên nó thành triết lý."

    narrator "Tâm cười. Cô nâng ly nước trái cây lên."

    tam "Chúc mừng chúng ta."

    huyen "Chúc mừng chúng ta. Và chúc phòng triển khai dự án sống sót sau khi tuyển hai đứa mình."

    play sound "audio/glass_clink.ogg"

    narrator "Hai chiếc ly chạm nhẹ vào nhau."

    narrator "Tiếng thủy tinh vang lên rất khẽ."

    narrator "Đúng lúc ấy, ở chiếc bàn trong góc khuất, có một người cũng nâng ly."

    narrator "Tâm nhìn thấy điều đó qua khóe mắt."

    narrator "Một chàng trai ngồi một mình. Ánh đèn chỉ rơi đến nửa vai, để khuôn mặt anh chìm trong một khoảng tối vừa đủ xa lạ."

    narrator "Anh không nói gì."

    narrator "Chỉ nâng ly về phía hai cô gái, như một lời chúc mừng lặng lẽ."

    huyen "Gì thế?"

    tam "Không biết."

    huyen "Người quen của mày à?"

    tam "Không."

    narrator "Tâm nhìn lại."

    narrator "Chàng trai trong góc đã đặt ly xuống. Anh hơi nghiêng đầu, như thể vừa vô tình bị bắt gặp trong một hành động không định để ai thấy."

    narrator "Rồi anh quay mặt về phía cửa kính."

    narrator "Thành phố phía sau lưng anh loang loáng ánh đèn."

    narrator "Một khoảnh khắc rất nhỏ."

    narrator "Nhỏ đến mức nếu ngày hôm đó Tâm không vui như thế, có lẽ cô đã quên ngay."

    $ add_unique(progress["player_flags"], "tam_saw_corner_man_at_dinner")
    $ add_unique(progress["player_flags"], "hoang_hidden_first_presence")

    scene black
    with fade

    narrator "Thời gian trôi qua."

    narrator "Một công việc mới không làm đời người lập tức thay đổi."

    narrator "Nó chỉ âm thầm thay đổi nhịp thở của từng ngày."

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
            tam "Em xin phép kiểm tra lại với QC và vật tư trước. Nếu lệch ở biên bản, em sẽ ghi rõ điểm chưa khớp rồi gửi bản tổng hợp cho các bên liên quan."
            manager "Đúng. Làm như vậy đi."
            narrator "Không ai khen thêm."
            narrator "Nhưng chỉ một câu 'đúng' thôi cũng đủ khiến Tâm thấy sống lưng mình thẳng hơn."

        "Gửi xác nhận tạm cho kế toán trước để kịp deadline, rồi bổ sung sau.":
            $ tam_confidence -= 1
            $ add_unique(progress["player_flags"], "tam_project_issue_rushed")
            tam "Em gửi xác nhận tạm trước rồi bổ sung sau được không ạ?"
            manager "Không. Hồ sơ thanh toán mà chạy trước xác nhận chất lượng thì người bị gọi đầu tiên là phòng mình."
            narrator "Tâm im lặng."
            narrator "Cô ghi lại lời nhắc ấy rất kỹ."

        "Chờ trưởng phòng tự quyết vì hồ sơ liên quan nhiều bên.":
            $ tam_confidence -= 1
            tam "Vậy phần này em chờ anh quyết định rồi em làm theo ạ?"
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
        huyen "Đứng thẳng lên. Mày đẹp mà cứ làm như đang xin lỗi xã hội vì mình đẹp ấy."
        tam "Mày nói nhỏ thôi."
        huyen "Không. Tao đang thực hiện nghĩa vụ bạn thân."

    narrator "Hôm đó công ty có vài khách mời từ đối tác."

    narrator "Tâm không để ý nhiều."

    narrator "Cho đến khi cô nhìn thấy một người đứng gần khu vực cửa kính."

    narrator "Một chàng trai mặc vest tối màu, dáng người cao và gọn. Khuôn mặt không quá xa lạ, nhưng cũng không đủ quen để cô gọi tên cảm giác vừa thoáng qua trong lòng."

    narrator "Anh đang nói chuyện với một người bên ban lãnh đạo công ty."

    narrator "Ánh mắt anh bình tĩnh. Nụ cười vừa đủ lịch sự. Cái kiểu người có thể đứng yên giữa một căn phòng ồn ào mà vẫn khiến không khí quanh mình có trật tự riêng."

    tam "..."

    huyen "Gì đấy?"

    tam "Không có gì."

    huyen "Không có gì mà nhìn người ta như đang đọc tài liệu mật?"

    tam "Mày im đi."

    narrator "Huyền nhìn theo hướng mắt Tâm, rồi khẽ huých khuỷu tay vào cô."

    huyen "À."

    tam "À cái gì?"

    huyen "Không có gì. Tao chỉ vừa phát hiện dự án phụ."

    tam "Huyền."

    huyen "Rồi rồi. Tao im."

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

        hoang "Chào em."

        tam "Dạ... chào anh."

        hoang "Anh là Hoàng. Đi cùng đoàn đối tác hôm nay."

        tam "Em là Tâm. Phòng triển khai dự án."

        hoang "Anh biết."

        narrator "Tâm hơi khựng lại."

        hoang "Lúc nãy anh có nghe em trao đổi về hồ sơ nghiệm thu với anh bên vật tư. Cách em tóm ý khá gọn."

        tam "À... em chỉ nói lại phần em nắm được thôi ạ."

        hoang "Nói lại cho người khác hiểu cũng là một kỹ năng."

        narrator "Giọng anh không giống khen xã giao."

        narrator "Và chính vì thế, Tâm bỗng không biết nên đặt tay mình ở đâu cho tự nhiên."

        huyen "Tôi đi lấy thêm nước nhé."

        narrator "Huyền nói rất nhanh rồi biến mất."

        narrator "Phản bội rất có kỹ thuật."

        hoang "Bạn em thú vị thật."

        tam "Dạ. Nó thường xuyên như vậy."

        hoang "Vậy chắc em vất vả."

        tam "Cũng quen rồi ạ."

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

                tam "Chào anh. Hình như anh là khách mời bên công ty đối tác ạ?"

                hoang "Ừ. Anh là Hoàng."

                tam "Em là Tâm. Phòng triển khai dự án."

                hoang "Anh có nghe giới thiệu lúc nãy."

                tam "Vậy chắc anh cũng nghe cả đoạn em nói hơi vấp."

                hoang "Có."

                narrator "Tâm ngẩng lên."

                hoang "Nhưng đoạn sau em sửa lại tốt."

                narrator "Câu trả lời thẳng đến mức Tâm không biết nên xem là khen hay xác nhận hiện trường."

                tam "Anh thường nói chuyện như đang nghiệm thu hồ sơ vậy ạ?"

                narrator "Hoàng thoáng khựng."

                narrator "Rồi anh bật cười."

                hoang "Không thường xuyên. Chỉ khi gặp người làm phòng triển khai."

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


label tam_c01_year_end_after_meeting:

    scene bg_company_year_end_party_late
    with dissolve

    narrator "Đêm ấy, khi buổi tiệc dần trôi về cuối, Tâm đứng cạnh cửa kính nhìn xuống thành phố."

    narrator "Những dòng xe nhỏ như những vệt sáng nối nhau đi qua dưới chân tòa nhà."

    huyen "Sao?"

    tam "Sao gì?"

    huyen "Dự án phụ."

    tam "Mày gọi người ta là dự án phụ thêm lần nữa, tao sẽ nộp mày cho phòng quản lý chất lượng."

    huyen "Tao chỉ đang đánh giá rủi ro."

    tam "Rủi ro gì?"

    huyen "Rủi ro mày thích người ta trước khi kịp hiểu người ta là ai."

    narrator "Tâm quay đi."

    narrator "Má cô hơi nóng. Có lẽ vì rượu trái cây."

    narrator "Có lẽ không."

    if "huyen_trust_high_c01" in progress["player_flags"]:
        huyen "Nhưng nếu có gì thật, nhớ nói tao."
        huyen "Tao không hứa khuyên đúng. Nhưng tao hứa sẽ nghe trước khi phán xét."
        tam "Nghe trưởng thành ghê."
        huyen "Tao diễn đấy. Nhưng cũng có tâm."

    narrator "Tâm khẽ cười."

    narrator "Cô không biết cuộc gặp ngắn ngủi vừa rồi sẽ dẫn mình đến đâu."

    narrator "Cô chỉ biết, trong một ngày cuối năm đầy tiếng người và ánh đèn, có một ánh mắt đã dừng lại nơi cô lâu hơn một nhịp."

    narrator "Và đôi khi, một nhịp thôi cũng đủ làm gió đổi chiều."

    jump tam_c01_end


label tam_c01_year_end_no_contact:

    scene bg_company_year_end_party_late
    with dissolve

    narrator "Cuối buổi tiệc, Tâm đứng bên cửa kính cùng Huyền."

    huyen "Mày đang tiếc à?"

    tam "Tiếc gì?"

    huyen "Không biết. Tao chỉ hỏi vậy thôi."

    narrator "Tâm nhìn xuống thành phố."

    narrator "Ánh đèn dưới kia trôi đi thành từng dòng lặng lẽ."

    tam "Chắc không."

    narrator "Cô nói vậy."

    narrator "Nhưng trong lòng lại có một khoảng rất nhỏ, giống như một chỗ trống vừa bị ai đó khẽ chạm vào rồi bỏ quên."

    narrator "Ở phía xa, chàng trai khách mời cũng rời khỏi buổi tiệc."

    narrator "Hai người không nói với nhau câu nào."

    narrator "Chỉ là sau này, khi nhớ lại, Tâm vẫn sẽ tự hỏi."

    narrator "Nếu hôm đó mình bước tới trước thì sao?"

    jump tam_c01_end


label tam_c01_end:

    scene black
    with fade

    narrator "Chapter 01 complete."

    $ complete_chapter("tam_c01")
    jump route_map

label tam_c02:
    # Cross-route unlock demo: Tam opens Hoang's first POV chapter.
    "The second chapter opens only after the first is complete, using centralized progression data."
    "This chapter now opens Hoang's route before Tam can finish her own line, creating the first interwoven prerequisite."

    $ complete_chapter("tam_c02")
    jump route_map


label tam_c03:
    # Direction-gated core event demo: this chapter depends on Hoang taking one bonus direction.
    "Tam can only reach this moment after Hoang's route has taken one of its two optional emotional directions."
    "That makes the route map prove a real exclusion-driven dependency instead of a simple linear chain."
    "[get_emotional_hint()]"

    if choice_is_available("notice_subtle_reaction"):
        "Because the player has seen Hoang's earlier hesitation, Tam notices a subtle reaction that would otherwise pass unseen."

    menu:
        "How should Tam respond?"

        "Ask gently" if choice_is_available("ask_gently"):
            $ add_unique(progress["player_flags"], "tam_choice_gentle")
            $ progress["emotional_state"]["trust"] += 1
            "Tam softens her words and lets the moment breathe."

        "Choose direct affection" if choice_is_available("choose_direct_affection"):
            $ add_unique(progress["player_flags"], "tam_choice_direct")
            $ progress["emotional_state"]["misunderstanding"] += 1
            "Tam pushes forward directly, even if the timing is dangerous."

        "Say nothing for now":
            $ add_unique(progress["player_flags"], "tam_choice_silence")
            "Tam decides the silence still says enough for now."

    $ complete_chapter("tam_c03")
    jump route_map
