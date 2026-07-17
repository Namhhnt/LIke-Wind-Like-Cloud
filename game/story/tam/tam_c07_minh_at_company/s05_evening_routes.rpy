# FILE: game/story/tam/tam_c07_minh_at_company/s05_evening_routes.rpy
# Scene file.

label tam_c07_minh_at_company_s05_evening_routes:
    if c07_tam_mode == "hoang_clear":
        scene bg_luxury_restaurant_evening
        with dissolve

        "Tối đó, Hoàng đưa Tâm đi ăn. Hơi nóng từ nồi lẩu bốc lên giữa hai người, làm kính cửa phía sau mờ đi một lớp."

        hoang teasing "Người được khen có quyền gọi món."

        tam teasing "Vậy em gọi phần đặc biệt nhé?"

        hoang neutral "Gọi đi. Cùng lắm cuối tháng ăn mì gói."

        "Tâm kể chuyện dự án. Kể chị Linh muốn bỏ nghề bán bánh mì. Kể Trường cuối cùng cũng tìm được người chịu nói hộ nỗi oan của IT."

        "Rồi cô kể về Minh."

        tam neutral "Anh Minh nhìn flow một lúc là thấy ngay bọn em đang ép hai loại yêu cầu vào cùng một mẫu. Công nhận anh ấy giỏi thật."

        hoang teasing "Ây chà. Thần tượng anh Minh rồi đúng không?"

        tam smile "Ừ. Có một chút."

        "Hoàng chớp mắt. Có vẻ câu trả lời thẳng quá làm anh mất sẵn một câu đùa."

        tam neutral "Nhưng người em muốn kể đầu tiên vẫn là anh."

        hoang neutral "Hai việc đó không giống nhau à?"

        tam smile "Không giống."

        "Hoàng nhìn cô vài giây. Rồi gắp miếng đậu phụ vừa chín đặt vào bát cô."

        hoang teasing "Vậy anh giữ vị trí người nghe báo cáo. Còn anh Minh phụ trách sửa quy trình."

        tam teasing "Phân quyền rõ ràng."

        hoang happy "Anh học từ chuyên gia."

        $ story_add("hoang_tam_trust", 10)
        $ story_add("tam_self_clarity", 10)
        $ story_sub("tam_minh_drawn", 10)
        $ story_sub("hoang_insecurity", -5)
        $ story_flag("tam_hoang_stable_path")
        $ story_flag("tam_c07_admiration_only")

        "Tâm cúi xuống ăn."

        "Minh vẫn là một người đáng để ngưỡng mộ."

        "Nhưng khi Hoàng gắp thêm thức ăn vào bát cô, Tâm không cần hỏi lòng mình đang ở đâu nữa."

    elif c07_tam_mode == "hoang_uncertain":
        scene bg_luxury_restaurant_evening
        with dissolve

        "Tối đó, Hoàng đưa Tâm đi ăn mừng."

        hoang teasing "Người được khen có quyền gọi món."

        tam teasing "Vậy em gọi phần đặc biệt nhé?"

        hoang neutral "Gọi đi. Hôm nay anh chuẩn bị tinh thần rồi."

        "Bữa ăn bắt đầu rất nhẹ. Nhẹ đến mức Tâm suýt quên cảm giác nặng trong lòng mấy ngày vừa qua."

        "Cô kể chuyện chị Linh dọa học thêm ngoại ngữ chỉ để chửi bên Vật tư cho chính xác. Kể chuyện Trường đặt tên folder dài đến mức chính anh cũng quên."

        "Rồi câu chuyện trượt sang dự án."

        tam neutral "Lúc đầu bên em định để cả Vật tư lẫn Thiết bị sửa thông tin sau nghiệm thu. Anh Minh hỏi đúng một câu là ai chịu trách nhiệm, cả phòng im luôn."

        hoang neutral "Nghe hợp lý."

        tam neutral "Còn phần nhập khẩu nữa. Em cứ nghĩ chỉ cần link chứng từ là được, nhưng anh Minh nói phải gắn với tiến độ thanh toán."

        hoang neutral "Ừ."

        tam neutral "Với cả flow phê duyệt. Bọn em cứ cố ép thiết bị và vật liệu vào cùng một mẫu. Anh Minh nhìn một lúc là thấy ngay—"

        "Tâm dừng lại."

        "Không phải vì Hoàng cắt lời. Mà vì chính cô vừa nghe thấy mình nhắc tên Minh quá nhiều."

        hoang teasing "Ây chà."

        tam confused "Gì?"

        hoang teasing "Dạo này anh thấy em nhắc anh Minh hơi nhiều nhé. Thần tượng ổng rồi đúng không?"

        if c07_work_choice == "keep_distance":
            "Tâm khựng một nhịp, nhưng lần này cô không né."

            tam neutral "Em có ngưỡng mộ anh ấy. Nhưng mấy hôm nay em sợ mình hiểu sai cảm xúc nên mới giữ khoảng cách."

            hoang neutral "Với anh Minh?"

            tam neutral "Với cả anh."

            "Hoàng đặt đũa xuống. Không cười nữa, nhưng cũng không đóng lại."

            hoang neutral "Thế giờ em hiểu chưa?"

            tam melancholic "Chưa hết. Nhưng em biết em không muốn làm anh phải đoán một mình."

            "Hoàng nhìn cô lâu hơn bình thường. Rồi chậm rãi đổ thêm nước dùng vào nồi."

            hoang neutral "Ừ. Thế thì nói từ từ."

            $ story_add("hoang_tam_trust", 10)
            $ story_add("tam_self_clarity", 10)
            $ story_sub("tam_insecurity", 10)
            $ story_sub("hoang_insecurity", -5)
            $ story_flag("tam_c07_early_honesty")

            "Hơi nóng bốc lên giữa hai người. Lần này nó không dùng để che mặt ai cả."

        else:
            "Nếu là ngày khác, Tâm có lẽ đã lườm anh. Hoặc hỏi lại: 'Anh ghen à?'"

            "Nhưng lần này, cô không đáp."

            "Đũa trong tay dừng giữa chừng. Miếng đậu phụ trượt xuống bát nước chấm."

            hoang neutral "Này. Anh đùa thôi mà."

            tam neutral "Em biết."

            hoang teasing "Chuyện đó bình thường thôi. Ai tiếp xúc với ổng mà chẳng thế. Anh cho phép."

            "Tâm không cười."

            hoang neutral "Miễn vẫn thích anh hơn là được."

            "Tiếng ồn trong quán bỗng lùi ra xa."

            "Nếu cô nói 'em vẫn thích anh hơn', câu ấy nghe như một cuộc xếp hạng. Nếu không nói, sự im lặng lại giống một lời thú nhận."

            hoang neutral "Tâm?"

            tam neutral "Nước cạn rồi kìa."

            "Một câu đánh trống lảng vụng về đến mức cả hai đều nhận ra."

            "Hoàng nhìn cô thêm một lúc. Nhưng anh không hỏi tiếp. Chỉ cầm bình nước dùng, chậm rãi đổ thêm vào nồi."

            "Phần còn lại của bữa ăn vẫn có tiếng nói chuyện. Nhưng ít hơn trước."

            $ story_add("tam_insecurity", 10)
            $ story_add("hoang_insecurity", 10)
            $ story_add("tam_minh_drawn", 5)
            $ story_sub("hoang_tam_trust", 5)
            $ story_flag("tam_hoang_shadow_doubt")

            scene black
            with dissolve

            "Sau hôm đó, Tâm bắt đầu né Hoàng."

            "Không rõ ràng đến mức có thể gọi là tránh mặt. Cô vẫn trả lời tin nhắn. Vẫn hỏi anh đã ăn chưa, đã về nhà chưa."

            "Nhưng mọi thứ ngắn hơn một chút. Chậm hơn vài phút. Ít trêu lại hơn."

            hoang neutral "Tối nay qua anh ăn cơm không? Anh nấu."

            tam neutral "Hôm nay em hơi mệt. Để hôm khác nhé."

            hoang neutral "Ừ. Nghỉ sớm đi."

            "Không trách. Không hỏi thêm. Chính vì thế mà lòng cô lại đau hơn."

            "Đến cuối tuần, Hoàng nhắn lần nữa."

            hoang neutral "Cuối tuần này em rảnh không?"

            "Tâm gõ: 'Em rảnh.'"
            "Rồi xóa."

            tam neutral "Chắc em phải xem lại lịch dự án đã."

            hoang neutral "Ừ. Có gì báo anh."

            "Tâm nhìn màn hình rất lâu."

            "Trong đầu cô hiện lên Minh ở phòng họp, tay cầm bút chỉ vào một điểm sai trong flow. Rồi hình ảnh ấy bị thay bằng Hoàng phía bên kia nồi lẩu, nụ cười chậm rãi nhạt đi."

            "Cô không nhớ Minh."
            "Cô nhớ Hoàng."

            "Và điều ấy đáng lẽ phải là câu trả lời."

            "Nhưng cô vẫn chưa đủ can đảm để tin vào nó."

            $ story_flag("tam_c07_avoids_hoang")
            $ story_flag("tam_explain_later")

    elif c07_tam_mode == "uncommitted":
        scene bg_company_lobby_afternoon
        with dissolve

        "Tan làm, Huyền đứng cạnh cửa thang máy, kiểm tra điện thoại."

        if c07_huyen_hoang_commit:
            huyen neutral "Tao phải đi trước. Hoàng đang đợi."

            huyen teasing "Mày đừng nhìn tao như thế. Người có lịch hẹn cũng có quyền sống."

            tam neutral "Tao có nhìn gì đâu."

            huyen grinning "Tốt. Dành ánh mắt cho người trong mơ đi."

        elif c07_huyen_quan_commit:
            quan neutral "Huyền, xuống chưa?"

            huyen neutral "Đấy. Cai ngục gọi."

            quan irritated "Anh nghe thấy."

            huyen grinning "Em biết."

        else:
            huyen neutral "Đi ăn không?"

            tam neutral "Mày không bận à?"

            huyen teasing "Tình bạn đang mở bán khuyến mãi. Chốt nhanh."

        "Điện thoại Tâm rung lên. Một tin nhắn công việc mới."

        minh neutral "Bản flow mới đúng hướng. Mai kiểm tra lại quyền sửa sau nghiệm thu. Đừng để phần đúng bị sửa vì người duyệt hỏi bằng giọng tự tin."

        "Tâm đọc lại hai lần."

        if c07_work_choice == "follow_pull":
            "Khóe môi cô cong lên trước khi kịp giữ."

            if not story_has_direction("tam", "tam_minh_open"):
                $ story_add_direction("tam", "tam_minh_open")

            $ story_add("tam_minh_drawn", 10)
            $ story_flag("tam_minh_possible")
            $ story_flag("tam_c07_minh_route_opened")

            if c07_huyen_hoang_commit or c07_huyen_quan_commit:
                huyen teasing "Mặt đó không phải mặt đọc checklist."

            else:
                huyen teasing "Mày có muốn tao đi trước để tiện cười một mình không?"

            tam flustered "Anh ấy chỉ nhắn công việc."

            huyen neutral "Ừ. Tao có bảo không đâu."

            "Tâm tắt màn hình, nhưng tên Minh vẫn ở lại trong đầu."

            "Lần này, cô không tự ép mình phải gọi nó là định mệnh. Cô chỉ cho phép mình tò mò thêm một chút về con người thật."

        else:
            "Tâm mỉm cười, rồi khóa màn hình."

            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_c07_career_over_projection")

            tam neutral "Đi ăn. Tao đói rồi."

            huyen surprised "Không ngồi ngắm tin nhắn à?"

            tam teasing "Mai còn phải sửa flow. Người trong mơ không làm hộ tao đâu."

            huyen grinning "Tốt. Ít nhất mày còn dùng được não."

            "Hai người bước vào thang máy."

            "Tâm vẫn phấn khích. Vẫn rung động. Nhưng lần đầu tiên, cô giữ được hai điều cùng lúc: một cảm giác đẹp và một đời sống không cần chạy theo nó ngay lập tức."

    else:
        scene bg_company_lobby_afternoon
        with dissolve

        "Ngày làm việc kết thúc. Tâm đóng laptop, cất lời khen và sự tò mò vào đúng ngăn của chúng."

        "Một chương mới đã mở trong dự án. Còn những câu chuyện khác, cô chưa cần vội."

    scene black
    with fade

    return
