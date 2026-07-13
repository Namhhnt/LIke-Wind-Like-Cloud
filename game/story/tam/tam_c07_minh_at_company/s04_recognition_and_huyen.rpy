# FILE: game/story/tam/tam_c07_minh_at_company/s04_recognition_and_huyen.rpy
# Scene file.

label tam_c07_minh_at_company_s04_recognition_and_huyen:
    scene bg_meeting_room_day
    with dissolve

    "Cuối tháng, ban triển khai được khen trong cuộc họp tổng kết giai đoạn một."

    c07_truongban "Phần mapping giữa mua sắm, nhập khẩu và nghiệm thu đã giúp NorthBridge duyệt hồ sơ nhanh hơn dự kiến. Tâm tiến bộ rõ ở phần liên phòng ban. Em giữ nhịp này nhé."

    "Mọi người vỗ tay."

    quan teasing "Có thưởng nhớ mời trà sữa."

    tam irritated "Anh mơ đi."

    huyen grinning "Không mời cũng được. Gửi tao file mẫu trước là tao thương."

    "Tâm cúi đầu cười, tai hơi nóng."

    scene bg_company_lobby_afternoon
    with dissolve

    "Sau cuộc họp, cô ra hành lang lấy nước. Minh vừa kết thúc một cuộc gọi gần cửa sổ."

    minh neutral "Chúc mừng."

    tam confused "Dạ?"

    minh neutral "Hôm nay em được khen."

    tam neutral "Cũng nhờ mọi người giúp nhiều ạ."

    minh neutral "Câu đó dùng trong email tổng kết thì được. Ngoài hành lang không cần."

    tam smile "Vâng. Vậy... em cảm ơn."

    minh neutral "Em làm tốt thật."

    if c07_tam_mode == "uncommitted":
        "Bốn chữ rất ngắn. Vậy mà niềm vui trong Tâm sáng lên rõ đến mức cô phải cúi xuống nhìn cốc nước."

        "Không phải chỉ vì được khen."
        "Mà vì người nói là anh."

        if c07_work_choice == "follow_pull":
            "Cô không còn đủ thành thật để gọi cảm giác ấy là ngưỡng mộ đơn thuần."
        else:
            "Cô vẫn chưa biết phải gọi cảm giác ấy là gì. Nhưng nó có thật, và đang lớn nhanh hơn dự tính."

    elif c07_tam_mode == "hoang_uncertain":
        "Tâm thấy vui. Nhưng vẫn là cái vui ngay ngắn của một người được công nhận đúng chỗ."

        "Không có cảm giác tim đập lệch như khi Hoàng nhìn cô rồi nói một câu rất bình thường: 'Hôm nay em xinh đấy.'"

        "Chính sự khác nhau ấy đáng lẽ phải làm mọi thứ đơn giản."
        "Nhưng Tâm lại bắt đầu sợ câu hỏi khác: nếu cô không rung động với Minh, tại sao cô vẫn hoang mang?"

    elif c07_tam_mode == "hoang_clear":
        "Tâm nhận lời khen với một niềm vui rõ ràng, không cần né tránh."

        "Minh là người cô ngưỡng mộ. Hoàng là người cô muốn kể chuyện này đầu tiên. Hai điều không hề tranh chỗ của nhau."

    else:
        "Tâm gật đầu, giữ lời khen ở đúng tầng của nó."

    "Minh cầm tập hồ sơ lên."

    minh neutral "Chiều nay xem lại phần phân quyền dữ liệu lần cuối. Quân sửa đúng hướng rồi, nhưng còn một chỗ dễ bị hiểu sai."

    tam neutral "Vâng."

    "Anh đi vào phòng họp nhỏ. Cửa kính khép lại."

    if c07_tam_mode == "hoang_clear":
        "Tâm lấy điện thoại ra ngay."

        tam happy "Em được sếp khen."

        hoang happy "Thế à? Tối nay phải thưởng rồi."

        tam teasing "Thưởng gì?"

        hoang teasing "Anh cho phép em chọn món. Nhưng anh giữ quyền ăn ké."

        "Tâm bật cười, không úp điện thoại xuống."

    elif c07_tam_mode == "hoang_uncertain":
        "Tâm mở khung chat với Hoàng."

        "Cô gõ: 'Em được sếp khen.'"

        "Lần này cô không xóa."

        hoang happy "Thế à? Tối nay phải thưởng rồi."

        tam neutral "Thưởng gì?"

        hoang teasing "Anh cho phép em chọn món. Nhưng anh giữ quyền ăn ké."

        "Tâm cúi đầu cười. Lòng mềm xuống, rồi lại nặng lên gần như cùng lúc."

    scene bg_company_open_office_day
    with dissolve

    "Giờ nghỉ trưa, Huyền xuất hiện bên bàn Tâm với một hộp sữa chua."

    huyen grinning "Người thành công."

    tam neutral "Gì?"

    huyen teasing "Đừng giả vờ. Tao nghe rồi. Thưởng nóng. Không cần cảm ơn."

    tam neutral "Hết hạn chưa?"

    huyen irritated "Mày xúc phạm tình bạn hơi đều đấy."

    if c07_tam_mode == "uncommitted":
        huyen teasing "Nào. Báo cáo thật đi. Được người trong mơ khen có khác được sếp khen không?"

        tam flustered "Mày đừng gọi thế ở công ty."

        if c07_huyen_hoang_commit:
            huyen teasing "Được. Tao sẽ gọi là anh trai người yêu tao. Nghe còn nguy hiểm hơn."
            tam shocked "Huyền."
            huyen grinning "Tao nói nhỏ mà."
        elif c07_huyen_quan_commit:
            huyen neutral "Tao hiểu cảm giác ngưỡng mộ người giỏi. Nhưng mày đang cười kiểu không hoàn toàn nghề nghiệp đâu."
            tam flustered "Tao có cười gì đâu."
            huyen teasing "Ừ. Chắc cơ mặt tự triển khai độc lập."
        else:
            huyen grinning "Không sao. Nếu là tao, tao cũng rung. Đẹp trai đã phiền, còn sửa được cả dự án thì quá phạm quy."

        if c07_work_choice == "follow_pull":
            tam neutral "Tao muốn biết thêm về anh ấy."
            "Huyền thôi cười một nhịp."
            huyen neutral "Thì biết. Nhưng nhớ nhìn người thật, đừng yêu bản dựng trong đầu."
            tam neutral "Tao biết."
        else:
            tam neutral "Tao chỉ... thấy anh ấy đặc biệt."
            huyen neutral "Ừ. Cái đó tao nhìn ra. Phần còn lại từ từ."

    elif c07_tam_mode == "hoang_uncertain":
        huyen neutral "Dạo này mày hơi lạ."

        tam neutral "Lạ gì?"

        huyen neutral "Cứ như bị ai nhấn mute một nửa."

        tam irritated "Tao bận thôi."

        huyen teasing "Bận thì mày vẫn cãi được. Dạo này bận mà hiền quá."

        "Tâm bật cười, nhưng tay vẫn kéo xuống một đoạn trong checklist."

        huyen neutral "Tối nay đi ăn mừng không?"

        tam neutral "Hoàng hẹn tao rồi."

        huyen grinning "À. Thế thì tha."

        "Huyền đi được hai bước rồi quay lại."

        huyen neutral "Ăn hết hộp sữa chua. Đừng để đấy rồi quên."

        tam smile "Biết rồi."

        "Huyền không kéo ghế ngồi xuống. Không gặng hỏi. Cũng không thay Tâm gọi tên điều gì."

    elif c07_tam_mode == "hoang_clear":
        huyen teasing "Thế nào? Được anh trai người yêu khen, có thấy cánh cửa nguy hiểm nào mở ra không?"

        tam smile "Không. Tao ngưỡng mộ anh ấy thật."

        huyen surprised "Thẳng thắn thế?"

        tam neutral "Ngưỡng mộ thì có gì phải giấu. Còn người tao muốn nhắn đầu tiên vẫn là Hoàng."

        huyen grinning "Được. Tỉnh táo một cách hơi gây khó chịu."

        if c07_huyen_quan_commit:
            huyen neutral "Tao mà rõ được nửa thế này thì đỡ phải cãi nhau với một người nào đó mỗi tuần."
            quan neutral "Anh nghe thấy."
            huyen grinning "Tốt. Em nói cho anh nghe."

    else:
        huyen neutral "Dự án này xem ra giúp mày lên tay thật."
        tam smile "Ừ. Ít nhất cũng đáng với số email đỏ."

    return
