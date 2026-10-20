# FILE: game/story/tam/tam_c02_company_party/s03_hoang_intro.rpy
# Scene file.

label tam_c02_company_party_s03_hoang_intro:
    scene bg_company_year_end_party
    with fade

    "Người đàn ông trẻ kia nhanh chóng được quản lý dự án dẫn đến gần bàn mô hình."

    manager "Mọi người, giới thiệu một chút. Đây là Hoàng, bên đối tác thiết kế. Cậu ấy hỗ trợ concept không gian cho dự án trải nghiệm khách hàng mới."

    hoang smile "Chào mọi người. Em chỉ hỗ trợ một phần thôi, còn team chính vẫn là bên mình."

    "Giọng Hoàng không lớn."

    "Anh nói vừa đủ, cười vừa đủ, và lùi lại nửa bước ngay sau câu giới thiệu."

    "Một kiểu lịch sự rất biết giữ khoảng cách."

    "Tâm nhận ra điều đó trước khi kịp nhận ra mình đang nhìn anh hơi lâu."

    huyen neutral "Đối tác thiết kế trẻ, đẹp trai, nói chuyện khiêm tốn."

    tam neutral "Mày đang đọc mô tả sản phẩm à?"

    huyen teasing "Không. Đang đánh giá nguy cơ."

    tam confused "Nguy cơ gì?"

    huyen grinning "Nguy cơ trong vòng mười phút nữa có ít nhất ba chị phòng marketing hỏi xin danh thiếp."

    "Như để chứng minh Huyền không hẳn bịa, một nhân viên nữ bước tới hỏi Hoàng về mô hình."

    "Hoàng trả lời lịch sự."

    "Nhưng mỗi khi câu hỏi chuyển sang chuyện cá nhân, anh lại đưa nó về dự án bằng một câu rất mềm."

    coworker "Em trẻ vậy mà đã làm concept chính rồi à?"

    hoang neutral "Dạ, em chỉ hỗ trợ phần hướng trải nghiệm thôi. Phần kỹ thuật vẫn cần các anh chị kiểm tra nhiều."

    coworker "Thế bình thường em làm ở đâu?"

    hoang smile "Bên em hay làm theo dự án. Nếu chị quan tâm phần layout, em có thể gửi profile studio sau."

    "Huyền nhướng mày."

    huyen teasing "Phòng thủ đẹp."

    tam neutral "Ừ."

    huyen surprised "Mày cũng thấy à?"

    tam neutral "Anh ấy không khó gần. Chỉ là không muốn bị kéo khỏi việc mình đến đây để làm."

    "Huyền nhìn Tâm thêm một giây."

    huyen smile "Ồ."

    tam confused "Sao?"

    huyen teasing "Không có gì. Tự nhiên thấy mày cũng có mắt."

    tam embarrassed "Mày im đi."

    scene cg_tam_c02_hoang_model
    with dissolve

    "Ở bàn mô hình, Hoàng cúi xuống chỉnh lại tấm name card nhỏ bị lệch."

    "Một động tác rất nhanh."

    "Nếu không nhìn đúng lúc, chắc chẳng ai để ý."

    "Tâm nhìn tấm name card đã thẳng lại."

    "Rồi nhìn phần ánh sáng hắt lên mặt kính."

    "Góc phản chiếu vẫn hơi chói."

    "Một điều rất nhỏ."

    "Nhưng có vẻ Hoàng cũng đã nhận ra. Anh nhìn nó hai giây, rồi hơi nghiêng đầu."

    scene bg_company_year_end_party
    with dissolve

    "Tâm bỗng thấy mình muốn hỏi."

    "Không phải vì Huyền đang đứng cạnh."

    "Cũng không phải vì Hoàng đẹp trai."

    "Chỉ là cô thật sự muốn biết anh sẽ xử lý góc sáng đó thế nào."

    if story_has_flag('tam_c02_hoang_approaches_due_to_dress'):
        jump tam_c02_company_party_s03_hoang_approaches_due_to_dress

    menu:
        "Ai mở cuộc trò chuyện với Hoàng?"

        "Tâm chủ động bắt chuyện với Hoàng":
            $ story_add('tam_hoang_interest', 5)
            $ story_add('hoang_tam_trust', 4)
            $ story_add('tam_self_clarity', 2)
            $ story_add('tam_observation', 1)
            $ story_add_direction('tam', 'tam_hoang_open')
            $ story_add_direction('hoang', 'hoang_tam_open')
            $ story_flag('tam_c02_hoang_first_talk')
            $ story_flag('tam_c02_hoang_project_question')

            "Tâm đặt ly nước xuống bàn."

            huyen neutral "Đi đâu?"

            tam neutral "Hỏi một câu."

            huyen teasing "Một câu thôi nhé. Đừng hỏi luôn tình trạng hôn nhân."

            tam embarrassed "Tao không có."

            "Tâm bước đến gần bàn mô hình."

            "Hoàng vừa kết thúc câu trả lời với một nhân viên khác. Anh quay sang, thấy cô đứng cách mình một khoảng vừa phải."

            tam neutral "Em hỏi hơi ngoài lề một chút được không ạ?"

            hoang smile "Được chứ."

            "Tâm chỉ vào phần mặt kính phía trên mô hình."

            tam neutral "Góc đèn này nếu đặt ngoài thực tế thì có bị chói ở khu ngồi chờ không anh?"

            "Hoàng khựng lại rất nhẹ."

            "Không phải vì câu hỏi khó."

            "Mà vì có lẽ nó không phải kiểu câu anh đang chờ trong một buổi tiệc."

            hoang neutral "Có thể bị."

            tam embarrassed "Em nhìn mô hình thấy hơi vậy. Nếu hỏi sai thì anh bỏ qua."

            hoang smile "Không sai đâu."

            "Anh cúi xuống gần mô hình hơn, dùng ngón tay chỉ một đường rất nhỏ dọc theo phần trần."

            hoang neutral "Bản ban đầu dùng ánh sáng trực tiếp. Nhưng sau đó bên anh đề xuất chuyển sang gián tiếp ở đoạn này."

            tam neutral "Để mềm hơn?"

            hoang smile "Và để người ngồi ở đây không có cảm giác đang bị thẩm vấn."

            "Tâm bật cười."

            tam smile "Vậy tốt. Khu chờ mà giống phòng thẩm vấn thì hơi đáng sợ."

            hoang neutral "Anh cũng nghĩ vậy."

            "Hoàng nhìn cô thêm một chút."

            "Ánh mắt anh không quá lộ."

            "Nhưng lớp phòng thủ ban nãy có vẻ đã hạ xuống một nửa."

            hoang smile "Em bên team nào?"

            tam neutral "Em mới vào. Đang trong giai đoạn thử việc. Có thể sẽ được phân vào team liên quan đến dự án này."

            hoang neutral "Vậy em hỏi đúng chỗ rồi."

            tam confused "Dạ?"

            hoang smile "Người mới thường nhìn thấy vài lỗi mà người đã nhìn quá lâu không còn thấy."

            "Tâm không biết nên đáp sao."

            "Câu đó không hẳn là khen."

            "Nhưng cũng không phải xã giao."

            tam smile "Vậy em sẽ cố nhìn cho đàng hoàng."

            hoang smile "Ừ. Nhìn kỹ một chút cũng tốt."

            "Phía sau, Huyền nâng ly nước lên che nửa mặt."

            huyen teasing "..."

            "Tâm không cần quay lại cũng biết cô nàng đang cười."

        "Hoàng bắt chuyện với Tâm trước":
            $ story_add('tam_hoang_interest', 3)
            $ story_add('hoang_tam_trust', 3)
            $ story_add('tam_observation', 1)
            $ story_add_direction('hoang', 'hoang_tam_open')
            $ story_flag('tam_c02_hoang_noticed_tam_first')

            "Tâm còn đang phân vân thì Hoàng đã nhìn sang."

            "Có lẽ anh nhận ra cô đã nhìn mô hình khá lâu."

            hoang smile "Em thấy chỗ nào hơi lạ à?"

            tam surprised "Dạ?"

            hoang neutral "Mô hình ấy. Em nhìn phần kính phía trên từ nãy."

            "Tâm hơi ngượng."

            "Bị bắt gặp đang quan sát người khác thì lúng túng."

            "Bị bắt gặp đang quan sát một mô hình trong tiệc công ty còn lúng túng theo kiểu hơi... khó giải thích."

            tam embarrassed "Em chỉ thấy góc sáng hơi chói."

            hoang smile "Anh cũng thấy."

            tam confused "Vậy sao vẫn để thế ạ?"

            hoang neutral "Vì đây là bản trưng bày. Bản kỹ thuật đã sửa rồi."

            tam neutral "À."

            hoang smile "Nhưng em nhìn ra nhanh đấy."

            "Tâm cúi mắt."

            tam neutral "Chắc do em đứng ở góc dễ thấy."

            hoang neutral "Không hẳn. Nhiều người đứng ở góc đó nhưng không nhìn."

            "Câu nói ấy khiến Tâm ngẩng lên."

            "Hoàng vẫn cười nhẹ."

            "Không quá gần."

            "Không quá xa."

            huyen teasing "Tâm."

            "Huyền từ phía sau chen vào bằng giọng rất tỉnh."

            huyen smile "Nước của mày sắp hết lạnh rồi."

            tam tired "Nước cũng có deadline à?"

            huyen grinning "Ở công ty này thì cái gì cũng có."

            "Hoàng bật cười khẽ."

            hoang smile "Nghe hợp lý."

        "Huyền nói chuyện với Hoàng trước":
            $ story_add('huyen_hoang_interest', 4)
            $ story_add('hoang_huyen_interest', 2)
            $ story_add('career_huyen', 1)
            $ story_add_direction('huyen', 'huyen_hoang_open')
            $ story_add_direction('hoang', 'hoang_huyen_open')
            $ story_flag('tam_c02_huyen_hoang_first_talk')

            "Tâm còn đang nhìn mô hình thì Huyền đã bước tới trước."

            huyen smile "Em chào anh. Em hỏi thật nhé, mô hình này có chống được nhân viên đói không ạ?"

            "Hoàng chớp mắt."

            "Rồi anh cười."

            hoang smile "Nếu nhân viên đói quá thì chắc không."

            huyen teasing "Vậy là thiết kế còn thiếu tính nhân đạo."

            hoang neutral "Anh sẽ ghi nhận feedback."

            huyen grinning "Tốt quá. Em tên Huyền. Nhân viên mới, chuyên đưa feedback ngoài phạm vi."

            hoang smile "Hoàng. Đối tác thiết kế, chuyên tiếp nhận feedback bất ngờ."

            "Tâm đứng cạnh, nhìn hai người bắt nhịp nhanh đến mức gần như không cần khởi động."

            "Huyền có tài làm người khác phải phản ứng."

            "Còn Hoàng, dù ban đầu hơi phòng thủ, rõ ràng không ghét kiểu trêu đúng nhịp."

            huyen neutral "Tâm, mày cũng hỏi đi. Nãy mày nhìn cái gì đó mà."

            tam embarrassed "Không có gì."

            huyen teasing "Không có gì là câu trả lời đáng nghi nhất trong mọi nền văn minh."

            hoang smile "Em cứ hỏi. Nếu anh trả lời được."

            "Tâm nhìn phần kính phía trên mô hình."

            "Rồi lại lắc đầu."

            tam neutral "Thôi ạ. Chắc để lúc khác."

            "Hoàng gật nhẹ."

            "Không ép."

            "Điều đó khiến Tâm dễ chịu hơn một chút."

        "Không có cuộc trò chuyện đáng kể":
            $ story_add('career_tam', 2)
            $ story_add('tam_insecurity', 1)
            $ story_flag('tam_c02_no_hoang_contact')

            "Tâm cuối cùng không bước tới."

            "Không phải vì cô không muốn hỏi."

            "Chỉ là quanh bàn mô hình mỗi lúc một đông hơn."

            "Một câu hỏi nhỏ nếu chen vào sai lúc có thể biến thành làm phiền."

            "Ít nhất Tâm tự giải thích với mình như vậy."

            huyen neutral "Không qua à?"

            tam neutral "Thôi. Anh ấy đang bận."

            huyen teasing "Ừ. Bận được ba chị hỏi chuyện."

            tam tired "Huyền."

            huyen smile "Rồi rồi. Không trêu nữa."

            "Tâm đứng lại ở mép sảnh."

            "Cô chuyển sự chú ý sang phần bảng thông tin dự án đặt gần đó."

            "Nếu không nói chuyện được với người thiết kế, ít nhất cô vẫn có thể đọc kỹ phần tài liệu."

            "Dòng chữ trên bảng khá nhỏ."

            "Tâm phải cúi gần hơn một chút mới đọc rõ."

            "Không có gì sai trong việc chọn công việc."

            "Chỉ là khi tiếng cười từ bàn mô hình vang lên, cô vẫn vô thức nhìn sang."

    jump tam_c02_company_party_s03_after_intro_common

label tam_c02_company_party_s03_hoang_approaches_due_to_dress:
    $ story_add('tam_hoang_interest', 5)
    $ story_add('hoang_tam_trust', 5)
    $ story_add('tam_self_clarity', 1)
    $ story_add('tam_observation', 1)
    $ story_add_direction('tam', 'tam_hoang_open')
    $ story_add_direction('hoang', 'hoang_tam_open')
    $ story_flag('tam_c02_hoang_noticed_tam_first')
    $ story_flag('tam_c02_hoang_approached_tam_first')
    $ story_flag('tam_c02_dress_impressed_hoang')

    "Tâm còn chưa kịp quyết định có nên bước đến bàn mô hình hay không thì Hoàng đã nhìn sang."

    "Ánh mắt anh dừng lại trên cô lâu hơn một nhịp."

    "Không lộ liễu."

    "Không suồng sã."

    "Chỉ là một khoảng dừng rất nhỏ, đủ để người tinh ý nhận ra."

    "Tâm nhận ra."

    "Và vì nhận ra, cô bỗng thấy phần cổ tay mình hơi nóng."

    huyen teasing "Ồ."

    tam embarrassed "Gì?"

    huyen smile "Không có gì. Người ta đang đi về phía này thôi."

    tam confused "Ai?"

    "Tâm chưa kịp quay hẳn lại thì Hoàng đã dừng cách hai người một khoảng vừa lịch sự."

    hoang smile "Chào em."

    tam surprised "Dạ... chào anh."

    hoang neutral "Anh thấy em nhìn mô hình từ nãy."

    huyen teasing "Anh chắc là nhìn mô hình chứ?"

    tam flustered "Huyền."

    "Hoàng khựng lại nửa giây."

    "Rồi anh cười."

    hoang smile "Cả mô hình nữa."

    "Câu đáp rất nhẹ."

    "Nhưng đủ khiến Huyền im được đúng hai giây, một thành tích không nhỏ."

    tam embarrassed "Em chỉ thấy phần ánh sáng ở góc kia hơi chói."

    hoang neutral "Đúng rồi. Bản trưng bày vẫn dùng đèn trực tiếp."

    "Anh bước sang bên cạnh bàn mô hình, chỉ vào một đường nhỏ ở phần trần."

    hoang neutral "Bản kỹ thuật đã đổi sang ánh sáng gián tiếp ở đoạn này."

    tam neutral "Để khu chờ mềm hơn ạ?"

    hoang smile "Và để khách không có cảm giác mình đang ngồi chờ bị thẩm vấn."

    "Tâm bật cười khẽ."

    tam smile "Vậy tốt. Chờ đã mệt rồi, bị thẩm vấn nữa thì hơi quá."

    hoang smile "Anh cũng nghĩ vậy."

    "Hoàng nhìn cô thêm một chút."

    "Lần này Tâm không biết anh đang nhìn vì câu hỏi của cô, hay vì chiếc váy."

    "Có lẽ cả hai."

    "Cô không hỏi."

    "Có những câu hỏi nếu hỏi ra sẽ làm mọi thứ vụng đi ngay lập tức."

    huyen neutral "Em là Huyền. Bạn thân kiêm cố vấn thời trang tối nay."

    hoang smile "Vậy chắc anh nên cảm ơn em."

    huyen grinning "Nên ạ."

    tam flustered "Mày đừng nhận công trắng trợn thế."

    huyen teasing "Tao nhận công có cơ sở."

    "Hoàng cười nhẹ."

    "Không khí quanh họ tự nhiên hơn một chút."

    "Không phải gần gũi."

    "Chỉ là khoảng cách ban đầu đã bớt cứng."

    jump tam_c02_company_party_s03_after_intro_common


label tam_c02_company_party_s03_after_intro_common:

    "Buổi tiệc tiếp tục trôi."

    "Người ta cụng ly, hỏi thăm, giới thiệu người này với người kia."

    "Những câu chuyện ngắn nối nhau như ánh đèn phản chiếu trên thành ly."

    "Có câu đọng lại."

    "Có câu vừa nói xong đã tan."

    "Tâm không biết cuộc trò chuyện với Hoàng, hoặc việc không trò chuyện với anh, sau này có nghĩa gì không."

    "Hiện tại, nó chỉ là một khoảnh khắc nhỏ trong một buổi tối nhiều tiếng người."

    "Nhưng đôi khi, một route dài cũng chỉ bắt đầu bằng một câu hỏi rất bình thường."

    "Và một người chịu dừng lại để trả lời."

    return

