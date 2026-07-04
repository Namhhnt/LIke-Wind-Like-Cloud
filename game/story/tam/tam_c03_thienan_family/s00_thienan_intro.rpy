# FILE: game/story/tam/tam_c03_thienan_family/s00_thienan_intro.rpy
# Scene file.

label tam_c03_thienan_family_s00_thienan_intro:
    scene bg_tam_family_living_room_evening
    with fade

    "Tối hôm ấy, Tâm về nhà muộn hơn thường lệ."

    "Đèn phòng khách vẫn sáng."

    "Trên chiếc sofa dài cạnh cửa sổ, Thiên An đang ngồi tựa lưng, hai mắt nhắm lại. Laptop đặt trên đùi cô vẫn chưa tắt, màn hình còn mở một bảng số liệu dài đến nhức mắt."

    "Một chiếc vali nhỏ để sát chân bàn."

    "Bên cạnh vali là áo khoác, hộ chiếu, vài tập hồ sơ, và một cốc trà đã nguội."

    tam neutral "Chị An?"

    "Thiên An mở mắt."

    "Không phải kiểu tỉnh dậy sau một giấc ngủ. Mà là kiểu một người vừa bị kéo ra khỏi một khoảng nghỉ rất ngắn."

    thienan tired "Em về rồi à?"

    tam neutral "Vâng. Chị ngủ ở đây à?"

    thienan neutral "Không hẳn."

    "Thiên An nhìn xuống laptop, như thể chính cô cũng vừa nhớ ra mình đang làm dở thứ gì."

    thienan tired "Chị chỉ định ngồi một chút."

    "Tâm nhìn chiếc vali."

    tam neutral "Chị lại đi công tác sao?"

    thienan neutral "Miền Nam. Chi nhánh bên đó đang có vài vấn đề."

    tam surprised "Lại nữa ạ?"

    "Thiên An không trả lời ngay."

    "Cô gập laptop lại. Động tác rất gọn, rất sạch, nhưng đầu ngón tay hơi dừng ở mép máy lâu hơn bình thường."

    thienan neutral "Không nghiêm trọng đến mức em phải lo."

    tam confused "Câu đó nghe giống hệt kiểu nói của người đang muốn người khác đừng lo."

    thienan smile "Vậy à?"

    tam neutral "Vâng."

    "Thiên An mỉm cười rất nhạt."

    "Nếu là người ngoài, chắc họ sẽ thấy nụ cười ấy vẫn bình tĩnh. Nhưng Tâm đã nhìn chị mình đủ lâu để nhận ra nó mỏng hơn mọi ngày."

    menu:
        "Tâm làm gì?"

        "Kéo chăn mỏng phủ lên chân Thiên An":
            $ story_flag('tam_supports_thienan')
            $ story_add('thienan_self_assertion', 1)
            $ story_add('tam_observation', 1)

            "Tâm không hỏi thêm."

            "Cô chỉ lấy chiếc chăn mỏng trên ghế bên cạnh, kéo nhẹ phủ qua chân chị."

            thienan surprised "Chị không lạnh."

            tam neutral "Em biết."

            "Tâm chỉnh lại mép chăn."

            tam smile "Nhưng cốc trà kia nguội rồi."

            "Thiên An nhìn cốc trà. Rồi nhìn Tâm."

            "Một lúc sau, cô không đẩy chăn ra."

        "Nhắc chị nên ngủ tử tế":
            $ story_add('thienan_self_assertion', 1)
            $ story_add('tam_observation', 1)

            tam neutral "Chị lên phòng ngủ đi. Ngồi thế này sáng mai đau lưng đấy."

            thienan smile "Em bắt đầu nói chuyện giống mẹ rồi."

            tam teasing "Vậy chị càng nên nghe."

            "Thiên An bật cười rất khẽ."

            "Tiếng cười nhỏ thôi, nhưng ít nhất nó thật hơn nụ cười vừa rồi."

        "Không hỏi thêm, để chị yên":
            $ story_add('tam_insecurity', 1)

            tam neutral "Vậy... chị nghỉ sớm nhé."

            thienan neutral "Ừ."

            "Tâm gật đầu rồi đi về phía cầu thang."

            "Đi được vài bước, cô quay lại."

            "Thiên An đã mở laptop lần nữa."

            "Ánh sáng xanh nhạt hắt lên gương mặt cô, lạnh và mỏng."

    "Trong trí nhớ của Tâm, Thiên An luôn là người đi trước."

    "Đi học trước. Thành công trước. Biết cách nói chuyện với người lớn trước. Biết cách giữ bình tĩnh trước."

    "Còn tối nay, lần đầu tiên Tâm nhận ra một chuyện rất đơn giản."

    "Người đi trước cũng có lúc mỏi chân."

    menu:
        "Tâm thật sự nhìn Thiên An như thế nào?"

        "Là người chị khiến mình muốn cố gắng hơn":
            $ story_flag('tam_sees_thienan_as_role_model')
            $ story_add('career_tam', 1)
            $ story_add('thienan_self_assertion', 1)

            "Tâm từng nghĩ nếu mình cố thêm một chút, có lẽ một ngày nào đó cô cũng có thể đứng vững như chị."

            "Bây giờ cô không còn chắc đứng vững là thứ đáng ngưỡng mộ nhất."

            "Nhưng cô vẫn muốn học cách không bỏ cuộc."

        "Là chị gái mà mình thương nhiều hơn mình nói":
            $ story_flag('tam_loves_thienan_as_sister')
            $ story_flag('tam_supports_thienan')
            $ story_add('thienan_self_assertion', 1)
            $ story_add('tam_observation', 1)

            "Tâm không phải kiểu hay ôm chị rồi nói những câu sến súa."

            "Thiên An cũng không phải."

            "Nhà này vốn tiết kiệm tình cảm bằng lời. Có khi tiết kiệm hơi quá. Kế toán cảm xúc, đại khái vậy."

            "Nhưng Tâm biết mình thương chị."

            "Chỉ là trước đây cô ít khi nghĩ đến việc phải nói ra."

        "Là người trong nhà nhưng đôi khi quá xa":
            $ story_flag('tam_keeps_distance_from_thienan')
            $ story_add('tam_insecurity', 1)
            $ story_add('family_pressure_thienan', 1)

            "Thiên An luôn ở đó."

            "Nhưng cũng luôn ở một vị trí nào đó rất khó chạm tới."

            "Tâm đã quen nhìn chị từ phía sau, đến mức đôi khi quên mất mình cũng có thể gọi chị dừng lại."

    return