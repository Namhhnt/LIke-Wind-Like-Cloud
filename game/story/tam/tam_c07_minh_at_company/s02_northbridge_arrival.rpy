# FILE: game/story/tam/tam_c07_minh_at_company/s02_northbridge_arrival.rpy
# Scene file.

label tam_c07_minh_at_company_s02_northbridge_arrival:
    scene bg_meeting_room_day
    with dissolve

    "Phòng họp gần kín. IT kéo ghế cạnh ổ cắm. Vật tư ôm một tập catalogue dày. Tài chính mang theo một máy tính bảng và vẻ mặt không muốn tin ai."

    "Tâm ngồi cạnh Huyền, gần cuối bàn."

    "Cửa phòng họp mở ra."

    "Trưởng ban đi vào trước. Sau anh là một phụ nữ mặc vest màu kem. Người còn lại bước sau nửa nhịp."

    "Áo sơ mi trắng. Quần âu tối màu. Không thắt cà vạt."

    "Vai thẳng. Bước chân yên. Gương mặt bình tĩnh đến mức gần như không có biểu cảm thừa."

    if c07_tam_mode == "uncommitted":
        "Tâm quên mất phải thở."

        "Cây bút trong tay cô rơi xuống bàn, nảy một tiếng cạch rõ hơn cô muốn."

        tam shocked "..."

        "Không còn lớp kính mờ của giấc mơ. Không còn mưa, không còn khoảng cách, không còn lý do để tự bảo rằng mình nhớ nhầm."

        "Là anh."

        "Người cô đã nhìn thấy trong giấc mơ. Người vừa xuất hiện trước cửa nhà Hoàng. Và giờ đang đứng dưới ánh đèn trắng của phòng họp như thể chuyện này hoàn toàn bình thường."

        "Một luồng phấn khích chạy từ ngực lên tận đầu ngón tay. Tâm cúi xuống nhặt bút, nhưng phải lần thứ hai mới cầm chắc được."

        $ story_add("tam_minh_drawn", 15)
        $ story_add("tam_observation", 5)
        $ story_flag("tam_dream_man_confirmed")
        $ story_flag("minh_route_unlocked")

    elif c07_tam_mode == "hoang_uncertain":
        "Cây bút trong tay Tâm rơi xuống sổ."

        "Một tiếng cạch rất nhỏ."
        "Không ai để ý. Chỉ có cô nghe thấy."

        "Minh."

        "Người trong giấc mơ. Người cô đã gặp ở cửa nhà Hoàng. Anh trai của Hoàng."

        "Ba sự thật nằm cạnh nhau, không cái nào sai, nhưng ghép lại thì khiến lòng cô lệch đi."

        $ story_add("tam_minh_drawn", 10)
        $ story_add("tam_insecurity", 10)
        $ story_add("tam_observation", 5)
        $ story_flag("tam_dream_man_confirmed")
        $ story_flag("minh_route_unlocked")

    elif c07_tam_mode == "hoang_clear":
        "Tâm nhận ra anh ngay."

        "Có một nhịp bất ngờ, giống như khi ghép được mảnh cuối của một hình ảnh cũ. Nhưng cảm giác ấy dừng ở đó."

        "Người trong giấc mơ là anh trai Hoàng."

        "Kỳ lạ thật. Nhưng không đáng sợ."

        "Bởi lần này, cô biết rõ người mình muốn quay sang kể chuyện đó là ai."

        $ story_add("tam_self_clarity", 5)
        $ story_add("tam_observation", 5)
        $ story_sub("tam_minh_drawn", 5)
        $ story_flag("tam_dream_man_confirmed")

    else:
        "Tâm nhận ra Minh, nhưng chỉ để sự bất ngờ đi qua trong một nhịp."
        $ story_add("tam_observation", 5)

    "Minh chưa nhìn thấy cô ngay. Ánh mắt anh lướt qua căn phòng, lịch sự và đều đặn."

    "Đến khi chạm vào Tâm, nó khựng lại rất nhẹ."

    minh neutral "..."

    "Anh gật đầu. Một cái gật vừa đủ quen, vừa đủ xa."

    tam neutral "..."

    "Tâm gật lại."

    c07_truongban "Giới thiệu với mọi người, đây là anh Huỳnh Nhật Minh, đại diện NorthBridge trong giai đoạn triển khai. Anh Minh sẽ tham gia giám sát tiến độ và cố vấn giải pháp. Bên cạnh anh là chị Mai, phụ trách kiểm soát hồ sơ đầu tư."

    "Huỳnh Nhật Minh."

    if c07_tam_mode == "uncommitted":
        "Tên anh nằm lại trong đầu Tâm rõ đến mức gần như có âm vang."
    elif c07_tam_mode == "hoang_uncertain":
        "Hóa ra người cô từng giữ trong một góc ký ức có một cái tên đầy đủ, một công việc, một đời sống thật — và một người em trai cô đang yêu."
    else:
        "Tâm ghi tên anh vào đầu trang tài liệu, ngay dưới dòng 'NorthBridge'."

    minh neutral "Tôi sẽ không can thiệp vào cách team vận hành nếu mọi thứ đang đi đúng hướng. Nhưng nếu có vấn đề về logic triển khai, phân quyền, nguồn dữ liệu hoặc rủi ro nghiệm thu, tôi sẽ hỏi khá kỹ. Mong mọi người thông cảm trước."

    quan neutral "Hỏi kỹ là kỹ cỡ nào anh?"

    minh neutral "Đủ để sau này khi lỗi xảy ra, không ai phải nói câu 'em tưởng'."

    "Cả phòng im một giây."
    "Rồi vài người bật cười."

    huyen grinning "Em thấy bên IT vừa được cứu rỗi."

    quan irritated "Anh vẫn đang ngồi đây đấy."

    huyen teasing "Em biết. Em nói cho anh nghe mà."

    "Cuộc họp kéo dài gần hai giờ. Minh không chen vào nếu không cần. Nhưng mỗi lần hỏi, người bị hỏi rất khó trả lời qua loa."

    minh neutral "Danh mục thiết bị lấy theo báo giá tháng trước, nhưng tỷ giá lại cập nhật theo tuần này. Hai cách đều được. Đừng trộn."

    minh neutral "Ai có quyền sửa số liệu sau nghiệm thu?"

    minh neutral "Nếu câu trả lời là 'nhiều người', vậy hiện tại chưa có ai chịu trách nhiệm."

    "Khi cuộc họp kết thúc, mọi người rời phòng chậm hơn bình thường. Một phần vì mệt. Phần còn lại vì đang âm thầm kiểm tra lại cuộc đời nghiệp vụ của mình."

    scene bg_company_lobby_noon
    with dissolve

    if c07_tam_mode == "uncommitted":
        if c07_huyen_knows_dream:
            huyen surprised "Đừng nói với tao."
            tam flustered "Gì?"
            huyen teasing "Người trong mơ."
            "Tâm nhìn thẳng phía trước. Tai nóng lên rất nhanh."
            tam flustered "Ừ."
            huyen shocked "Ừ là sao? Mày xác nhận nhẹ như xác nhận lịch họp thế à?"

            if c07_huyen_hoang_commit:
                huyen teasing "May mà lần này mày nhìn đúng người anh. Phần người em... tao không định nhường đâu."
                tam shocked "Mày nói cái gì đấy?"
                huyen grinning "Nói cho cơ cấu gia đình rõ ràng thôi."
            elif c07_huyen_quan_commit:
                huyen teasing "Gu của mày là kiểu người nhìn bảng dữ liệu như sắp bắt nó khai cung à? Tao không phán xét. Gu của tao cũng chẳng hiền hơn."
                "Quân đi phía trước chậm lại nửa bước."
                quan neutral "Anh nghe thấy."
                huyen grinning "Em nói cho anh nghe mà."
            else:
                huyen grinning "Người trong mơ ngoài đời còn biết sửa flow nghiệp vụ. Hơi quá tay rồi đấy."
        else:
            huyen teasing "Mày làm rơi bút hai lần."
            tam neutral "Một lần."
            huyen neutral "Lần thứ hai là suýt. Tao tính luôn."
            huyen teasing "Biết anh ấy à?"
            "Tâm im một nhịp."
            tam flustered "Tao từng mơ thấy anh ấy."
            huyen shocked "...Mày giấu bản đặc biệt này đến giờ?"
            tam irritated "Đừng làm quá."
            huyen grinning "Tao còn chưa bắt đầu làm quá."

    elif c07_tam_mode == "hoang_uncertain":
        if c07_huyen_knows_dream:
            huyen teasing "Anh trai người yêu mày lại là người trong mơ. Đời mày viết tình tiết hơi lười."
            tam irritated "Mày bé mồm thôi."
            huyen neutral "Tao đang bé mà."
            "Huyền nhìn cô thêm một chút, rồi không trêu nữa."
            huyen neutral "Ổn không?"
            tam neutral "Ổn."
            "Câu trả lời nhanh quá. Cả hai đều nghe thấy."
        else:
            huyen teasing "Mày biết anh Minh trước à?"
            tam neutral "Gặp một lần thôi."
            huyen neutral "Một lần mà mặt mày như vừa nhận mail lỗi production."
            tam irritated "Tao không sao."
            huyen neutral "Ừ. Tao chưa hỏi mày có sao không."

    elif c07_tam_mode == "hoang_clear":
        if c07_huyen_knows_dream:
            huyen teasing "Thế là bí ẩn người trong mơ được giải rồi nhé. Có rung rinh không?"
            tam smile "Không."
            huyen surprised "Nhanh thế?"
            tam neutral "Vì tao biết cảm giác muốn về kể chuyện cho ai là gì."
            "Huyền nhìn cô hai giây, rồi bật cười."
            huyen grinning "Được. Câu này đạt chuẩn self-awareness."
        else:
            huyen teasing "Anh trai Hoàng được đấy. Mày có thấy nguy hiểm không?"
            tam smile "Nguy hiểm cho tiến độ dự án thì có."
            huyen grinning "Tỉnh thế. Hơi chán nhưng đáng tin."

    else:
        huyen neutral "Anh Minh khó đọc thật."
        tam neutral "Nhưng hỏi đúng."

    return
