# FILE: game/story/tam/tam_c07_minh_at_company/s01_monday_morning.rpy
# Scene file.

label tam_c07_minh_at_company_s01_monday_morning:
    scene bg_tam_room_morning
    with fade

    centered "{size=46}CHAPTER 07{/size}\n{size=30}Khoảng cách của một cái bóng{/size}"

    scene bg_tam_room_morning
    with dissolve

    if c07_tam_mode == "hoang_uncertain":
        "Câu hỏi ấy theo Tâm đến tận sáng thứ Hai."

        "Không ồn ào. Không làm cô mất ngủ cả đêm. Nó chỉ nằm ở đó, nhỏ và lì, như một vệt mực đã rửa qua nhưng vẫn còn màu trên đầu ngón tay."

        "Liệu cô có thật sự yêu Hoàng?"

        "Hay trong lần đầu dừng lại trước anh, cô đã nhìn thấy một nét quen thuộc thuộc về người khác?"

        "Điện thoại trên kệ rung lên."

        hoang neutral "Dậy chưa? Hôm nay đi làm nhớ mang áo khoác. Trời đổi gió đấy."

        "Tâm gõ 'Em dậy rồi'."
        "Xóa."
        "Gõ 'Biết rồi. Anh cũng vậy'."
        "Lại xóa."

        tam neutral "Vâng."

        hoang teasing "Ngoan thế. Hơi đáng nghi."

        "Tâm bật cười rất khẽ."
        "Rồi gần như ngay lập tức, cô mím môi lại."

        "Có những lúc người ta không sợ mình buồn."
        "Người ta sợ mình vẫn vui, vì cái vui ấy khiến cảm giác có lỗi trở nên rõ ràng hơn."

    elif c07_tam_mode == "hoang_clear":
        "Sáng thứ Hai, Tâm tỉnh dậy trước chuông báo thức vài phút."

        "Điện thoại trên kệ rung lên."

        hoang neutral "Dậy chưa? Hôm nay đi làm nhớ mang áo khoác. Trời đổi gió đấy."

        tam smile "Em dậy rồi. Anh cũng mặc ấm vào. Đừng chỉ biết nhắc người khác."

        hoang teasing "Rõ. Báo cáo đã tiếp nhận."

        "Tâm đặt điện thoại xuống, khóe môi vẫn còn cong."

        "Cuộc gặp bất ngờ hôm trước vẫn khiến cô tò mò. Nhưng tò mò là tò mò. Nó không làm xê dịch nơi lòng cô đã chọn."

    elif c07_tam_mode == "uncommitted":
        "Sáng thứ Hai, Tâm thức dậy với cảm giác như có một đoạn phim ngắn cứ tự phát lại trong đầu."

        "Cánh cửa mở ra. Một người đàn ông đứng ngoài. Ánh mắt bình tĩnh. Gương mặt quen đến vô lý."

        "Người trong giấc mơ của cô."

        "Ngoài đời thật."

        "Điện thoại rung lên."

        huyen neutral "Dậy chưa? Hôm nay họp đối tác. Mặc đồ cho giống người đáng tin một chút."

        tam irritated "Tao lúc nào chẳng đáng tin."

        huyen teasing "Mày đáng tin. Tủ đồ của mày thì chưa chắc."

        "Tâm bật cười, nhưng khi đặt điện thoại xuống, tim cô lại nảy lên một nhịp không đúng lúc."

        "Cô không biết mình sẽ gặp lại anh hay không."
        "Chính ý nghĩ đó khiến buổi sáng bỗng sáng hơn mức cần thiết."

    else:
        "Sáng thứ Hai bắt đầu bằng một lịch họp dày và ba email gắn cờ đỏ."

        "Tâm chuẩn bị đi làm như thường lệ, cố đặt cuộc gặp bất ngờ hôm trước vào đúng ngăn của nó: một chuyện chưa cần gọi tên."

    scene bg_company_open_office_day
    with dissolve

    "An Thịnh làm phát triển dự án: kho vận, nhà xưởng, thiết bị, vật liệu và những bảng tiến độ đủ dài để khiến người bình thường mất niềm tin vào cuộc sống."

    "Tâm làm ở ban triển khai."

    "Nói cho oai là điều phối nghiệp vụ giữa các phòng ban. Nói thẳng ra là người phải hỏi vì sao cùng một file mà năm phòng hiểu thành sáu kiểu."

    c07_linh tired "Kẹt đời rồi."

    tam confused "Máy in à chị?"

    c07_linh frustrated "Tối qua vừa sửa xong phụ lục hợp đồng. Sáng nay Vật tư đổi danh mục thiết bị. Chị muốn nghỉ việc đi bán bánh mì."

    c07_truong neutral "Bán bánh mì cũng phải quản lý nguyên vật liệu. Không thoát được đâu."

    c07_linh irritated "Im."

    "Trường im thật."

    huyen grinning "Thứ Hai rất công bằng. Nó ghét tất cả mọi người như nhau."

    "Tâm mở laptop. Mười bảy email mới. Ba cái đỏ. Một cái viết hoa toàn bộ tiêu đề."

    tam tired "Công bằng thật."

    quan neutral "Mọi người chuẩn bị vào phòng họp nhé. Bên NorthBridge đến rồi."

    "Tâm cầm laptop, sổ tay và một cây bút."

    if c07_tam_mode == "uncommitted":
        "Cô đứng dậy nhanh hơn bình thường nửa nhịp."

        "Huyền nhìn sang. Không nói gì. Chỉ nhướng một bên mày."

    else:
        "Lúc đứng dậy, cô có cảm giác như bước xuống cầu thang trong bóng tối: biết rõ còn một bậc cuối, nhưng chân vẫn hụt đi nửa nhịp."

    return
