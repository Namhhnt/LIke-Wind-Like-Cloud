# FILE: game/story/tam/tam_c01_interview_day/s02_interview_room.rpy
# Scene file.

label tam_c01_interview_day_s02_interview_room:
    scene bg_interview_waiting_room
    with fade

    "Phòng chờ phỏng vấn yên tĩnh hơn Tâm tưởng."

    "Không ai nói lớn. Chỉ có tiếng lật giấy, tiếng bút bấm, và tiếng giày chạm nhẹ lên nền gạch."

    "Huyền ngồi cạnh cô, lưng thẳng hơn bình thường một chút."

    huyen neutral "Tao ghét kiểu im lặng này."

    tam neutral "Vì sao?"

    huyen "Nó làm tao nghe rõ tiếng tim mình."

    tam smile "Ít nhất chứng minh mày còn sống."

    huyen irritated "Cảm ơn. An ủi rất có tâm."

    "Một ứng viên ngồi đối diện khẽ cúi xuống nói với người bên cạnh."

    coworker "Nghe nói team này có anh Quân khó tính lắm."

    coworker "Trưởng phòng ấy. Soi kỹ từng dòng, ít khen, ghét nhất kiểu nói hay mà làm dở."

    "Câu nói rất nhỏ."

    "Nhưng trong căn phòng quá yên, nó vẫn lọt qua."

    huyen confused "Quân?"

    tam neutral "Chắc là trưởng phòng."

    huyen "Mày nghe thấy đoạn 'ít khen' không?"

    tam "Có."

    huyen "Tự nhiên tao thấy không cần được khen nữa."

    tam teasing "Tiết kiệm kỳ vọng. Rất thực tế."

    "Huyền nhìn Tâm."

    "Cô định đáp lại, nhưng tên mình được gọi trước."

    hr "Nguyễn Minh Tâm?"

    "Tâm đứng dậy."

    "Quai túi trượt khỏi vai. Cô giữ lại kịp, nhưng tập hồ sơ bên trong khẽ xô xuống."

    "Một tiếng giấy chạm giấy rất nhỏ."

    "Tâm nghe rõ."

    huyen smile "Đi đi."

    tam neutral "Ừ."

    huyen "Cổ áo ổn."

    tam smile "Tao chưa hỏi."

    huyen teasing "Nhưng mặt mày hỏi rồi."

    "Tâm bật cười rất khẽ."

    scene bg_interview_room
    with dissolve

    "Phòng phỏng vấn sáng và gọn."

    "Một bàn dài. Ba người ngồi phía đối diện. Nước lọc đặt bên tay phải. Bút đặt song song với mép giấy."

    "Tất cả đều ngay ngắn."

    "Tâm thấy hơi buồn cười vì mình lại để ý đến chuyện đó trước tiên."

    hr "Chào em, Tâm. Mời em ngồi."

    tam neutral "Em chào anh chị ạ."

    "Cô đặt túi xuống cạnh ghế, lấy portfolio ra."

    "Lần này chiếc kẹp giấy không lệch."

    interviewer "Bọn chị đã xem CV của em. Hôm nay sẽ trao đổi thêm về kinh nghiệm thực tập, portfolio, và một vài tình huống xử lý công việc."

    manager "Trưởng phòng chuyên môn hôm nay có lịch họp đột xuất nên không trực tiếp tham gia được."

    "Người quản lý dừng lại, lật một trang ghi chú."

    manager "Nhưng anh Quân có gửi lại vài câu hỏi."

    "Tâm nghe thấy tên đó lần thứ hai trong buổi sáng."

    "Lần này nó không còn là lời đồn nữa."

    interviewer "Em cứ thoải mái. Nếu cần thời gian suy nghĩ, có thể nói."

    tam neutral "Vâng. Em hiểu ạ."

    "Tâm đặt hai tay lên đầu gối."

    "Móng tay cái khẽ chạm vào mép vải quần."

    "Một lần."

    "Rồi dừng lại."

    call tam_c01_speech_game

    scene bg_interview_room
    with dissolve

    if tam_salary_tier == "high":
        $ story_flag('tam_perfect_interview')
        $ story_add('career_tam', 2)
        $ story_add('tam_self_clarity', 1)

        "Khi phần trao đổi kết thúc, người phỏng vấn nhìn lại bảng ghi chú thêm vài giây."

        interviewer "Cách em trình bày khá rõ. Không quá dài, nhưng đủ thông tin."

        manager "Và phần đề xuất mức lương của em... có chuẩn bị."

        "Tâm không vội cười."

        "Cô chỉ gật đầu, vừa đủ."

        tam neutral "Em cảm ơn anh chị. Em muốn đưa ra con số phù hợp với năng lực hiện tại và phần việc em tin mình có thể đảm nhận."

        hr "Tốt. Bọn chị sẽ phản hồi sớm."

        "Khi đứng dậy, Tâm mới nhận ra lòng bàn tay mình đã hơi ẩm."

        "Không sao."

        "Ít nhất cô đã không để giọng mình run."

    elif has_player_flag("tam_interview_passed"):
        $ story_add('career_tam', 1)

        "Buổi phỏng vấn kết thúc ở mức ổn."

        "Không có khoảnh khắc nào thật sự rực rỡ, nhưng cũng không có vết trượt nghiêm trọng."

        interviewer "Em có nền tảng tốt. Một vài phần cần thực tế hơn, nhưng chị nghĩ có thể đào tạo được."

        tam smile "Vâng. Em cảm ơn chị."

        manager "Đi làm khác đi học khá nhiều. Nếu vào team, em sẽ cần thích nghi nhanh."

        tam neutral "Em hiểu ạ. Em sẽ cố gắng."

        "Tâm biết câu đó hơi an toàn."

        "Nhưng có những lúc, an toàn vẫn tốt hơn cố tỏ ra sắc sảo rồi tự cắt vào tay mình."

    else:
        $ story_add('doom_score', 1)

        "Có một câu hỏi Tâm trả lời chậm hơn mức cần thiết."

        "Không đến mức tệ."

        "Nhưng cô biết mình đã né quá lâu trước khi đi vào ý chính."

        manager "Em hơi vòng ở phần xử lý mâu thuẫn trong team."

        tam embarrassed "Vâng. Em xin lỗi ạ."

        interviewer "Không sao. Chị hiểu em muốn trả lời cẩn thận. Nhưng trong công việc, đôi khi cần quyết định rõ hơn."

        tam neutral "Vâng. Em sẽ lưu ý."

        "Tâm gật đầu."

        "Câu trả lời vẫn lịch sự."

        "Chỉ có đầu ngón tay cô khẽ bấu vào bìa portfolio."

        "Một vết lõm nhỏ hiện lên trên mép giấy."

    # Unlock minigame for library replay
    $ add_unique(persistent.unlocked_library_content, "minigame_speech_tam_c01")

    scene bg_interview_waiting_room
    with dissolve

    "Khi Tâm quay lại phòng chờ, Huyền đã không còn ngồi yên được nữa."

    huyen surprised "Sao rồi?"

    tam neutral "Chưa biết."

    huyen "Mặt mày là mặt chưa biết thật hay mặt đang giả vờ chưa biết?"

    tam smile "Mày phân biệt được à?"

    huyen "Không. Nên mới hỏi."

    "Tâm ngồi xuống cạnh cô."

    "Hai người im lặng một lúc."

    "Ngoài cửa kính, bóng nhân viên đi ngang qua hành lang. Ai cũng có vẻ biết mình cần đi đâu."

    "Tâm nhìn theo họ."

    "Rồi cô đặt portfolio lên đùi, đưa tay vuốt lại mép giấy vừa bị lõm."

    "Không phẳng hẳn."

    "Nhưng đỡ hơn."

    huyen neutral "Này."

    tam neutral "Ừ?"

    huyen "Nói thật đi. Bên trong thế nào?"

    "Tâm nhìn Huyền."

    "Câu hỏi rất đơn giản."

    "Nhưng cô biết Huyền không chỉ hỏi về căn phòng, hay mấy người phỏng vấn, hay những câu hỏi chuyên môn."

    "Huyền muốn biết liệu bên trong có đáng sợ như lời đồn không."

    "Muốn biết liệu mình sắp bước vào một nơi sẽ nuốt mất toàn bộ sự tự tin còn sót lại không."

    "Tâm cúi nhìn mép portfolio đã được vuốt phẳng hơn một chút."

    "Nói hết thì có thể làm Huyền lo."

    "Giấu đi thì cũng không hẳn là tử tế."

    menu:
        "How should Tâm answer Huyền?"

        "Be honest about the pressure":
            $ story_flag('tam_honest_about_interview_pressure')
            $ story_add('tam_self_clarity', 1)

            tam neutral "Có áp lực."

            huyen tired "Tao biết ngay mà."

            tam "Nhưng không đến mức không thở được."

            "Huyền nhìn cô, chờ tiếp."

            tam neutral "Họ hỏi khá kỹ. Không phải kiểu hỏi cho có. Có vài câu phải nghĩ thật cẩn thận mới trả lời được."

            huyen confused "Có câu nào đánh đố không?"

            tam "Không hẳn. Nhưng có câu nếu mình nói quá đẹp thì nghe sẽ giả."

            huyen embarrassed "Tuyệt. Đúng chuyên môn của tao rồi."

            tam smile "Mày chỉ cần đừng cố tỏ ra hoàn hảo."

            huyen "Khó đấy. Tao vốn hoàn hảo tự nhiên."

            tam teasing "Ừ. Nhất là cổ áo sáng nay."

            huyen irritated "Tâm."

            "Tâm khẽ bật cười."

            tam neutral "Thật đấy. Cứ trả lời rõ ràng. Nếu cần nghĩ thì xin vài giây. Họ không khó chịu đâu."

            huyen neutral "Mày chắc không?"

            tam "Chắc."

            "Huyền thở ra."

            huyen smile "Được. Nghe đáng sợ, nhưng đáng sợ có hình dạng thì đỡ hơn."

            tam smile "Ừ. Ít nhất mình biết nó có mấy cái răng."

            huyen laughing "Ví dụ kinh quá."

        "Keep it vague to avoid worrying her":
            $ story_flag('tam_keeps_interview_vague')
            $ story_add('tam_self_clarity', 1)

            tam neutral "Cũng bình thường."

            huyen confused "Bình thường kiểu nào?"

            tam "Kiểu... phòng phỏng vấn, bàn dài, nước lọc, câu hỏi."

            huyen bored "Cảm ơn. Miêu tả rất giàu giá trị sinh tồn."

            tam smile "Tao nghĩ mày vào rồi sẽ tự bắt nhịp được."

            huyen "Đừng nói kiểu đó. Kiểu đó nghe như câu trước khi nhân vật phụ hy sinh."

            tam teasing "Mày là nhân vật phụ à?"

            huyen "Trong đời tao thì tao là nữ chính."

            tam happy "Vậy nữ chính không chết ở vòng phỏng vấn đâu."

            "Huyền nhìn cô một lúc, nửa nghi ngờ, nửa buồn cười."

            huyen neutral "Mày đang giấu tao gì không?"

            tam neutral "Tao đang giữ lại vài bất ngờ."

            huyen irritated "Đúng là nghe còn đáng sợ hơn."

            tam smile "Không sao đâu. Mày làm được."

            "Lời động viên hơi chung chung."

            "Nhưng ít nhất lúc này, nó giữ cho Huyền không bị kéo sâu thêm vào những hình dung xấu nhất."

        "Be honest with insight" if story_state.get('career_tam', 0) >= 3:
            $ story_flag('tam_honest_with_interview_insight')
            $ story_add('tam_self_clarity', 1)
            $ story_add('career_huyen', 1)

            tam neutral "Có áp lực. Nhưng tao nghĩ họ không tìm người trả lời đẹp nhất."

            huyen confused "Là sao?"

            tam "Họ đang xem mình có hiểu việc thật không."

            "Huyền hơi nghiêng đầu."

            "Tâm hạ giọng, nói chậm hơn một chút."

            tam neutral "Nếu họ hỏi về điểm yếu, đừng biến nó thành một câu khoe khéo. Nếu họ hỏi về teamwork, đừng nói kiểu 'em hòa đồng với tất cả mọi người'. Nghe thì an toàn, nhưng rỗng."

            huyen neutral "Vậy phải nói sao?"

            tam "Nói một tình huống cụ thể. Có vấn đề gì, mày đã làm gì, kết quả ra sao, sau đó mày học được gì."

            "Tâm dừng lại, nhớ đến câu hỏi của Quân được chuyển qua người quản lý."

            tam neutral "Và nếu họ hỏi về mâu thuẫn trong team, đừng né. Cứ thừa nhận là có những lúc làm việc với người khác không dễ. Quan trọng là mình xử lý nó thế nào."

            huyen surprised "Mày vừa được ai nhập à?"

            tam confused "Hả?"

            huyen teasing "Tự nhiên nói nghe như senior đi phỏng vấn fresher."

            tam embarrassed "Tao chỉ vừa bị hỏi xong thôi."

            huyen smile "Ừ. Nhưng hữu ích."

            "Huyền lấy điện thoại ra, gõ nhanh vài chữ vào note."

            huyen neutral "Tình huống cụ thể. Hành động. Kết quả. Bài học."

            tam smile "Ừ."

            huyen "Không giả vờ quá cầu toàn."

            tam "Càng không."

            huyen happy "Được. Tự nhiên tao thấy mình có vẻ sống được."

            tam teasing "Chúc mừng. Thành tựu lớn trước giờ phỏng vấn."

            huyen laughing "Im đi."

            "Huyền cười, nhưng lần này ngón tay cô không còn miết lên mép bìa hồ sơ nữa."

    hr "Lê Thị Thu Huyền?"

    "Tên Huyền vang lên từ phía cửa."

    "Nụ cười trên môi cô lập tức đông lại."

    huyen surprised "Rồi. Tới lượt tao."

    tam neutral "Ừ."

    huyen tired "Nếu tao không quay lại..."

    tam teasing "Tao sẽ ăn phần bánh mừng của mày tối nay."

    huyen irritated "Đồ ác độc."

    "Huyền đứng dậy, chỉnh lại cổ áo theo thói quen."

    "Lần này, cổ áo đã thẳng."

    tam smile "Ổn rồi."

    huyen embarrassed "Tao chưa hỏi."

    tam happy "Nhưng mặt mày hỏi rồi."

    "Huyền khựng lại."

    "Rồi cô bật cười, rất khẽ."

    huyen smile "Được. Tao vào đây."

    "Tâm gật đầu."

    "Cửa phòng phỏng vấn khép lại sau lưng Huyền."

    "Phòng chờ lại yên xuống."

    "Nhưng lần này, sự im lặng không còn nặng như lúc đầu nữa."

    return
