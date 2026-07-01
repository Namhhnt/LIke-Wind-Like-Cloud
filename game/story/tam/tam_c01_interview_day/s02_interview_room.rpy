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

    coworker "Nghe nói team này có anh Quân khó lắm."

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

    if tam_salary_tier == "high":
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

    return