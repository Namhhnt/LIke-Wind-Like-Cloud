# FILE: game/story/tam/tam_c07_minh_at_company/s03_working_logic.rpy
# Scene file.

label tam_c07_minh_at_company_s03_working_logic:
    scene bg_company_open_office_day
    with dissolve

    "Những ngày sau đó, cái tên 'anh Minh bên NorthBridge' xuất hiện ở khắp nơi."

    "Anh Minh bảo file thiếu mapping với mã vật tư."
    "Anh Minh hỏi lại điều kiện thanh toán của lô thiết bị nhập khẩu."
    "Anh Minh nói dữ liệu nghiệm thu phải khóa quyền sửa sau khi duyệt."
    "Anh Minh bảo đừng để IT ôm hết lỗi nghiệp vụ."

    c07_truong happy "Cuối cùng cũng có người nói tiếng người."

    huyen teasing "Anh nói như thể trước giờ anh làm việc với động vật."

    c07_truong irritated "Anh không nói thế."

    huyen grinning "Nhưng mặt anh có."

    "Tâm biết Minh giỏi. Nhưng biết và tận mắt chứng kiến là hai chuyện khác nhau."

    "Cái giỏi của anh không nằm ở những câu lớn. Nó nằm ở cách anh nghe hai phòng ban tranh luận mười phút, rồi tóm lại bằng ba câu khiến cả hai bên đều không cãi được."

    "Anh không làm thay. Chỉ đẩy người khác tự nhìn ra chỗ sai."

    scene bg_meeting_room_day
    with dissolve

    "Chiều thứ Năm, phòng họp nhỏ chỉ còn Tâm, Minh và Trường."

    "Trường đeo tai nghe xử lý lỗi phân quyền trên hệ thống demo, gần như tách khỏi thế giới."

    tam neutral "Em sửa lại flow phê duyệt vật tư theo góp ý hôm trước. Nhưng đoạn này vẫn hơi vướng."

    minh neutral "Vướng chỗ nào?"

    tam neutral "Nếu để Vật tư tạo yêu cầu, Thiết bị xác nhận thông số rồi Tài chính duyệt ngân sách thì hợp lý."

    tam neutral "Nhưng phần vật liệu lại cần đội kỹ thuật kiểm tra tiêu chuẩn trước. Nếu thêm một bước nữa thì flow dài quá."

    "Minh kéo ghế lại gần vừa đủ để nhìn màn hình, không gần hơn."

    minh neutral "Em đang cố dùng một flow cho hai loại việc khác nhau."

    tam confused "Dạ?"

    minh neutral "Mua thiết bị cần thông số. Duyệt vật liệu cần tiêu chuẩn nghiệm thu."

    minh neutral "Nếu ép chung, người dùng phải điền nhiều trường không liên quan. Sau đó họ sẽ bỏ qua."

    "Anh chỉ vào điểm giao giữa hai nhánh."

    minh neutral "Tách ra. Chỉ giữ phần chung ở ngân sách và hợp đồng."

    tam neutral "Nhưng như vậy phải làm hai mẫu yêu cầu."

    minh neutral "Làm hai mẫu đúng còn hơn một mẫu sai."

    "Tâm nhìn sơ đồ. Một điểm cô đã mắc ở đó gần hai ngày bỗng trở nên đơn giản đến khó chịu."

    minh neutral "Phần em sửa ở bước nghiệm thu tốt hơn bản cũ."

    tam surprised "Thật ạ?"

    minh neutral "Ừ. Ít nhất bây giờ người đọc biết ai chịu trách nhiệm nếu số liệu lệch."

    if c07_tam_mode == "uncommitted":
        "Niềm vui đến nhanh hơn Tâm kịp giữ. Cô cúi xuống ghi chú để giấu nụ cười, nhưng đầu bút chạy nhanh đến mức chữ hơi nghiêng."

    elif c07_tam_mode == "hoang_uncertain":
        "Tâm thấy vui theo một cách ngay ngắn, giống như được người nghiêm khắc gật đầu công nhận. Nhưng chính vì vui, cô lại thấy mình cần cẩn thận hơn."

    elif c07_tam_mode == "hoang_clear":
        "Tâm mỉm cười. Một lời công nhận nghề nghiệp, rõ ràng và vừa đủ. Cô nhận nó đúng như thế."

    # Core chapter choice: professional growth, emotional boundary, or active pull.
    menu:
        "Giữ khoảng cách. Chỉ trao đổi đúng phần việc cần thiết." if c07_tam_hoang_commit:
            $ c07_work_choice = "keep_distance"
            $ story_add("hoang_tam_trust", 10)
            $ story_add("tam_self_clarity", 10)
            $ story_sub("tam_minh_drawn", 10)
            $ story_add_direction("tam", "tam_hoang_open")
            $ story_flag("tam_c07_kept_professional_distance")

            tam neutral "Em hiểu rồi. Em sẽ tách flow và gửi lại bản mới trước thứ Hai."

            minh neutral "Được. Nếu còn vướng thì hỏi Trường trước. Phần phân quyền anh ấy nắm rõ hơn."

            c07_truong neutral "Cuối cùng anh cũng được nhớ tới."

            minh neutral "Anh vẫn ở đây mà."

            "Tâm khép laptop lại. Cô không ở thêm để tìm một câu hỏi khác."

        "Chủ động hỏi thêm về phần logic công việc.":
            $ c07_work_choice = "ask_work"
            $ story_add("career_tam", 15)
            $ story_add("tam_observation", 10)
            $ story_flag("tam_minh_professional_bond")

            if c07_tam_mode != "hoang_clear":
                $ story_add("tam_minh_drawn", 5)

            tam neutral "Nếu tách hai mẫu, phần ngân sách chung nên dùng một record gốc hay hai record liên kết ạ?"

            minh neutral "Một record gốc. Hai loại yêu cầu chỉ là hai cách đi vào cùng một cam kết chi phí."

            tam neutral "Vậy nếu hợp đồng thay đổi, chỉ cần cập nhật ở record gốc."

            minh smile "Đúng."

            "Tâm ghi lại. Lần này cô không chỉ chép lời anh. Cô tự vẽ tiếp phần còn lại của flow."

        "Ở lại thêm một chút. Hỏi cả điều mình chưa thật sự cần biết." if c07_tam_mode == "uncommitted" or c07_tam_mode == "hoang_uncertain":
            $ c07_work_choice = "follow_pull"
            $ story_add("tam_minh_drawn", 15)
            $ story_add("tam_insecurity", 10)
            $ story_add_direction("tam", "tam_minh_open")
            $ story_flag("tam_minh_possible")
            $ story_flag("tam_c07_followed_minh_pull")

            if c07_tam_hoang_commit:
                $ story_add("hoang_insecurity", 10)

            tam neutral "Anh làm cố vấn cho NorthBridge lâu chưa ạ?"

            minh neutral "Câu đó liên quan đến flow vừa rồi à?"

            tam flustered "Không hẳn."

            "Minh nhìn cô một nhịp. Không làm cô khó xử, nhưng cũng không giả vờ không nhận ra."

            minh neutral "Đủ lâu để biết vấn đề hiếm khi nằm đúng chỗ người ta đang chỉ tay vào."

            tam neutral "Anh lúc nào cũng nhìn mọi thứ như thế sao?"

            minh neutral "Không. Có những thứ nhìn kỹ quá chỉ làm chúng phức tạp hơn."

            "Câu nói dừng lại ở đó."

            if c07_tam_mode == "uncommitted":
                "Tâm biết mình nên quay về bàn. Nhưng cô vẫn đứng thêm một nhịp, chỉ để ghi nhớ giọng anh ngoài căn phòng của giấc mơ."

            else:
                "Tâm nghe thấy tên Hoàng trong phần im lặng của chính mình. Cô khép laptop hơi nhanh."

    # The small work correction is a chapter-wide career gain.
    $ story_add("career_tam", 10)
    $ story_add("tam_observation", 10)

    if c07_tam_mode != "hoang_clear" and c07_work_choice != "keep_distance":
        $ story_add("tam_minh_drawn", 5)

    $ story_flag("minh_helped_tam_work_error")

    "Trước khi Tâm rời phòng, Minh gọi lại."

    minh neutral "Tâm."

    tam neutral "Dạ?"

    minh neutral "Đừng sửa phần em đã làm đúng chỉ vì người khác hỏi bằng giọng tự tin."

    "Tâm nhìn bản flow trong tay."

    tam smile "Vâng."

    return
