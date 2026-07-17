# FILE: game/story/yuuka/yuuka_c08_festival_arrival/s02_yuuka_as_director.rpy
# Scene file.

label yuuka_c08_festival_arrival_s02_yuuka_as_director:
    scene bg_meeting_room_day
    with dissolve

    "Hai ngày sau, Vân mang tới bản giới thiệu nội dung dành cho team vận hành."

    "Không phải để mọi người bình luận nghệ thuật."

    "Chị nói điều đó hai lần."

    c08_van neutral "Mọi người cần biết khách nào đi cùng đoàn đông, ai có lịch giao lưu, ai cần kiểm tra thiết bị trình chiếu riêng."

    huyen teasing "Tức là bọn em được xem trailer trong giờ làm nhưng không được giả vờ làm nhà phê bình."

    c08_van smile "Chính xác."

    quan neutral "Ai bình luận dài quá năm phút sẽ được giao nhập dữ liệu passport."

    huyen neutral "Nghệ thuật nên được cảm nhận trong im lặng."

    "Đèn phòng họp tắt bớt."

    "Trailer đầu tiên là một phim tài liệu."

    "Trailer thứ hai có quá nhiều tiếng súng."

    "Đến đoạn phim thứ ba, căn phòng yên xuống theo một cách khác."

    "Không có lời dẫn."

    "Một người phụ nữ lớn tuổi ngồi gấp chiếc áo sơ mi đã cũ."

    "Một chiếc ghế đối diện vẫn trống."

    "Nước trong ấm sôi lên, nhưng bà không rót."

    "Khung hình chuyển sang một ga tàu nhỏ. Một cô gái trẻ đứng sau lớp kính, bàn tay giữ một tấm vé đã nhàu."

    "Không ai khóc."

    "Không ai nói câu nào về chia xa."

    "Nhưng đến lúc cánh cửa tàu đóng lại, Huyền vô thức đặt cây bút xuống."

    huyen neutral "Phim này..."

    quan neutral "Không bình luận nghệ thuật."

    huyen irritated "Em mới nói có hai chữ."

    "Trailer kết thúc bằng cảnh chiếc áo được đặt lên lưng ghế trống."

    "Màn hình tối đi."

    "Dòng credit hiện lên."

    centered "{size=34}Directed by Yuuka Nakamura{/size}"

    "Sau đó là một montage hậu trường rất ngắn."

    "Một người phụ nữ đeo tai nghe đứng sau monitor."

    "Cô quay nghiêng, mái tóc che một phần gương mặt. Khung hình chỉ tồn tại chưa đầy một giây trước khi chuyển sang cảnh khác."

    "Không đủ để nhớ mặt."

    "Chỉ đủ để nhận ra vị đạo diễn ấy còn khá trẻ."

    c08_van neutral "Yuuka Nakamura. Đạo diễn người Nhật."

    c08_van neutral "Phim của cô ấy được chọn vào chương trình trình chiếu trọng điểm và có một buổi giao lưu riêng với sinh viên điện ảnh."

    c08_van neutral "Cô ấy không phải diễn viên, nên truyền thông cá nhân không nhiều bằng một số khách khác."

    c08_van smile "Nhưng bên chuyên môn đánh giá rất cao."

    "Tâm nhìn cái tên trên tài liệu."

    "Nakamura Yuuka."

    "Cô không biết vì sao mình nhớ nó nhanh như vậy."

    if c08_tam_leads_festival:
        c08_van neutral "Nhóm của Tâm sẽ theo lịch đón và quyền truy cập kỹ thuật của đoàn này."

        tam neutral "Em sẽ kiểm tra lại yêu cầu thiết bị."

    else:
        c08_van neutral "Tâm, em theo Huyền kiểm tra lịch đón và danh sách thiết bị của đoàn này nhé."

        tam neutral "Vâng."

    menu:
        "Điều gì trong đoạn phim ở lại với Tâm?"

        "Cách bộ phim dùng những chi tiết rất nhỏ.":
            $ story_add("tam_respect_yuuka", 10)
            $ story_add("tam_observation", 10)
            $ story_flag("tam_respects_yuuka_visual_language")

            "Tâm nhớ chiếc áo cũ."

            "Không phải cảnh ga tàu. Không phải cô gái sau cửa kính."

            "Chỉ là cách người phụ nữ gấp cổ tay áo thêm một lần dù nó đã phẳng."

            "Một động tác nhỏ, nhưng đủ để người xem hiểu bà đang trì hoãn điều gì."

            tam neutral "Đạo diễn này quan sát người khác kỹ thật."

            huyen neutral "Ừ."

            huyen teasing "Kiểu người đáng sợ trong đời thường."

        "Kỷ luật phía sau một đoạn phim tưởng như rất tự nhiên.":
            $ story_add("tam_respect_yuuka", 10)
            $ story_add("career_tam", 10)
            $ story_flag("tam_respects_yuuka_production_discipline")

            "Tâm nhìn lại bảng technical note."

            "Những khung hình mềm và yên ấy đi kèm một danh sách yêu cầu rất chính xác: tỷ lệ màn hình, âm thanh, phụ đề, bản backup, thời gian kiểm tra."

            "Phần cảm xúc có thể nhẹ."

            "Phần vận hành thì không hề mơ hồ."

            tam neutral "Checklist của đoàn này rất sạch."

            quan smile "Người làm tốt thường không bắt hậu trường phải đoán."

        "Cái tên xuất hiện sau cùng trong credit.":
            $ story_add("tam_respect_yuuka", 5)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_remembers_yuuka_name")

            "Tên cô xuất hiện khi tất cả hình ảnh đã kết thúc."

            "Không có gương mặt rõ ràng để bám vào."

            "Chỉ có một cái tên đứng sau những gì người khác vừa nhìn thấy."

            "Tâm khoanh nhẹ dòng ấy trên tài liệu."

    $ story_flag("yuuka_introduced_through_work")
    $ story_flag("yuuka_face_not_clearly_seen")

    return