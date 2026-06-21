# Chapter 01, Scene 02

label tam_c01_after_interview:

    scene bg_company_lobby_noon
    with dissolve

    narrator "Khi Tâm bước ra khỏi phòng, Huyền đã đứng bật dậy như lò xo."

    huyen sad "Sao rồi?"

    tam dazed "Chưa biết."

    huyen smile "Mặt mày nhìn không tệ. Tức là không bị loại ngay tại cửa."

    tam smile "Cảm ơn vì lời động viên rất có giá trị tinh thần."

    huyen smile "Không có gì. Tao tính phí theo giờ."

    narrator "Hai người ngồi xuống hàng ghế dài ở sảnh. Bên ngoài lớp kính, nắng trưa bắt đầu rơi thành từng mảng gắt."

    huyen sad "Tao run quá."

    tam surprised "Đến lượt mày rồi à?"

    huyen sad "Ừ. Nếu tao chết trong đó, nhớ xóa lịch sử tìm kiếm của tao."

    menu:
        "Tâm nên động viên Huyền thế nào?"

        "Nhắc Huyền bình tĩnh và dùng thế mạnh thật của mình.":
            $ huyen_trust += 1
            $ add_unique(progress["player_flags"], "tam_supported_huyen_interview")
            tam serious "Mày không cần cố tỏ ra giỏi hơn con người thật của mày đâu. Mày nói chuyện tự nhiên, bắt ý nhanh, lại nhớ chi tiết tốt. Cứ dùng đúng mấy thứ đó."
            huyen smile "Nghe hơi giống lời thoại trong phim thanh xuân, nhưng... có ích thật."
            tam smile "Đi đi. Đừng làm xấu mặt bánh mì ban sáng."

        "Trêu Huyền để cô ấy bớt căng.":
            tam smile "Không sao. Nếu mày trượt, tao sẽ kể chuyện này trong đám cưới mày."
            huyen laugh "Mày đúng là bạn thân kiểu cần cho vào danh sách rủi ro dự án."
            narrator "Huyền bật cười. Căng thẳng trong mắt cô vơi đi một chút."

        "Bảo Huyền tự lo vì ai cũng phải tự vượt qua.":
            $ huyen_trust -= 1
            tam neutral "Tao cũng không biết khuyên gì. Mày tự lo đi. Ai cũng phải tự qua phần của mình mà."
            huyen sad "Ờ. Tao hiểu."
            narrator "Huyền cười, nhưng nụ cười hơi mỏng."

    narrator "Huyền đi vào phòng phỏng vấn."

    narrator "Tâm ngồi lại một mình."

    narrator "Sảnh công ty bỗng rộng hơn hẳn khi không còn tiếng Huyền nói bên cạnh."

    scene bg_company_lobby_afternoon
    with dissolve

    narrator "Kết quả được thông báo vào cuối buổi chiều."

    narrator "Cả hai cùng trúng tuyển."

    narrator "Tâm đọc email hai lần. Huyền đọc bốn lần. Sau đó hai đứa nhìn nhau vài giây, rồi cùng bật cười như hai kẻ vừa thoát khỏi một vụ tai nạn không nghiêm trọng nhưng đủ làm tim rơi xuống tận đầu gối."

    huyen happy "Tối nay ăn mừng."

    tam surprised "Ăn gì?"

    huyen serious "Sang."

    tam shocked "Mày vừa mới được nhận việc đã muốn phá sản à?"

    huyen smile "Không. Tao gọi đó là đầu tư vào tinh thần trước khi bị doanh nghiệp nghiền nát."

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
                tam happy "Tao được offer cao hơn tao tưởng một chút."
                huyen surprised "Thật á? Bao nhiêu?"
                tam embarrassed "Tao nói mày nghe, nhưng không phải để khoe đâu nhé. Tao cũng hơi bất ngờ."
                huyen laugh "Con điên. Mày được offer cao thì tao mừng chứ. Sau này nhớ bao tao trà sữa size lớn."
                tam smile "Đấy mới là mục đích thật của mày đúng không?"
                huyen happy "Bạn thân là phải biết biến niềm vui của nhau thành đồ uống."

            "Giấu đi để tránh Huyền buồn.":
                $ huyen_trust -= 1
                $ add_unique(progress["player_flags"], "tam_hid_salary_from_huyen")
                tam sad "Cũng bình thường thôi."
                narrator "Tâm nói vậy. Nhưng cô biết mình vừa giấu Huyền một điều không quá cần phải giấu."
                narrator "Sự im lặng nhỏ ấy nằm lại giữa hai người như một cái ghim lệch."

            "Khoe thẳng vì mình xứng đáng.":
                $ huyen_trust -= 1
                tam happy "Tao được offer cao hơn. Chắc tại phần phỏng vấn tốt thật."
                huyen sad "Ờ. Mày giỏi mà."
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

    huyen neutral "Này."

    tam neutral "Gì?"

    huyen happy "Chúng ta chính thức là người lớn rồi đấy."

    tam surprised "Chỉ vì được nhận việc?"

    huyen smile "Ừ. Người lớn là những sinh vật vui mừng khi nhận được email bắt đầu chuỗi ngày bán linh hồn cho bảng biểu."

    tam smile "Nghe bi quan quá."

    huyen smile "Nhưng tao nói trong nhà hàng sang, nên nó thành triết lý."

    narrator "Tâm cười. Cô nâng ly nước trái cây lên."

    tam happy "Chúc mừng chúng ta."

    huyen happy "Chúc mừng chúng ta. Và chúc phòng triển khai dự án sống sót sau khi tuyển hai đứa mình."

    play sound "audio/glass_clink.ogg"

    narrator "Hai chiếc ly chạm nhẹ vào nhau."

    narrator "Tiếng thủy tinh vang lên rất khẽ."

    narrator "Đúng lúc ấy, ở chiếc bàn trong góc khuất, có một người cũng nâng ly."

    narrator "Tâm nhìn thấy điều đó qua khóe mắt."

    narrator "Một chàng trai ngồi một mình. Ánh đèn chỉ rơi đến nửa vai, để khuôn mặt anh chìm trong một khoảng tối vừa đủ xa lạ."

    narrator "Anh không nói gì."

    narrator "Chỉ nâng ly về phía hai cô gái, như một lời chúc mừng lặng lẽ."

    huyen confused "Gì thế?"

    tam thoughtful "Không biết."

    huyen confused "Người quen của mày à?"

    tam neutral "Không."

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

    jump tam_c01_scene_03
