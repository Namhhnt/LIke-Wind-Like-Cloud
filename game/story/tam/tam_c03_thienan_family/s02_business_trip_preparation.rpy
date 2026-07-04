# FILE: game/story/tam/tam_c03_thienan_family/s02_business_trip_preparation.rpy
# Scene file.

label tam_c03_thienan_family_s02_business_trip_preparation:
    scene bg_tam_family_living_room_evening
    with dissolve

    "Sau khi ăn tạm bát canh nóng dưới sự giám sát không khoan nhượng của mẹ Tâm, Quang ở lại thêm một lúc để cùng Thiên An rà soát hồ sơ."

    "Hai người ngồi ở hai đầu bàn trà."

    "Giữa họ là laptop, hợp đồng, bút ký, kẹp giấy, và một danh sách công việc được in ra trên giấy A4."

    thienan neutral "Báo cáo tồn kho?"

    quang "Đã gửi vào mail. Bản in ở tập thứ hai."

    thienan neutral "Số liệu quý trước?"

    quang "Có chênh lệch giữa bản chi nhánh gửi và bản kế toán tổng hợp."

    thienan neutral "Bao nhiêu?"

    quang "Không lớn. Nhưng đủ khó chịu."

    thienan neutral "Đánh dấu lại."

    quang "Anh đánh rồi."

    "Thiên An dừng tay."

    "Cô lật thêm hai trang. Đúng là có một tờ giấy nhỏ dán ở mép phải."

    thienan neutral "Màu vàng?"

    quang "Màu xanh em dùng cho việc đã xử lý. Màu vàng cho việc cần nhìn lại."

    thienan neutral "Em đổi màu từ khi nào?"

    quang "Từ tháng Ba."

    "Thiên An nhìn anh."

    quang "Em quên à?"

    thienan neutral "Không. Em chỉ không nghĩ anh nhớ."

    quang "Có vài thứ nhớ dễ hơn quên."

    "Tâm ngồi ở bàn ăn, giả vờ uống nước."

    "Cô không cố nghe lén."

    "Nhưng phòng khách không rộng đến thế."

    "Sự ăn ý giữa hai người khiến cô hơi ngạc nhiên. Không phải kiểu ngọt ngào. Không có ánh mắt kéo dài, không có câu nói dư."

    "Chỉ là người này vừa dừng, người kia đã biết cần đưa thứ gì tiếp theo."

    "Giống như một chiếc máy đã chạy chung quá lâu."

    "Tốt. Chính xác."

    "Và hơi buồn."

    menu:
        "Tâm nghĩ gì khi nhìn Thiên An và Quang làm việc?"

        "Hai người thật sự tin nhau":
            $ story_add('thienan_quang_trust', 2)
            $ story_add('tam_observation', 1)
            $ story_flag('tam_noticed_thienan_quang_work_trust')

            "Tin nhau không nhất thiết phải nói bằng lời."

            "Đôi khi nó nằm ở việc một người có thể đưa tài liệu mà không cần giải thích, và người kia nhận lấy mà không nghi ngờ."

            "Tâm không biết giữa họ có tình cảm hay không."

            "Nhưng cô biết có một loại gắn bó ở đó."

        "Có lẽ họ chỉ là đồng nghiệp quá lâu":
            $ story_flag('tam_reads_quang_as_colleague')
            $ story_add('family_pressure_thienan', 1)

            "Có những người làm việc cùng nhau lâu đến mức trở nên quen thuộc."

            "Quen thuộc không hẳn là thân mật."

            "Nhiều khi nó chỉ là một dạng hiệu suất được luyện quá kỹ."

            "Tâm tự nhắc mình đừng suy diễn."

        "Họ hiểu nhau đến mức hơi đáng sợ":
            $ story_flag('tam_noticed_quang_silent_care')
            $ story_add('tam_observation', 2)
            $ story_add('thienan_quang_trust', 1)

            "Tâm nhìn chiếc kẹp giấy màu vàng."

            "Một chi tiết quá nhỏ."

            "Nhỏ đến mức chính Thiên An cũng không chắc mình đã từng nói với Quang."

            "Vậy mà anh nhớ."

            "Không phải nhớ kiểu cố tình gây ấn tượng."

            "Là nhớ vì đã để ý quá lâu."

    thienan neutral "Chuyến bay sáng mai mấy giờ?"

    quang "Bảy giờ mười."

    thienan tired "Sớm vậy?"

    quang "Em còn lịch họp lúc mười một giờ."

    thienan neutral "Đổi sang họp online."

    quang "Anh thử rồi. Bên đó nói cần gặp trực tiếp."

    thienan neutral "Ai nói?"

    quang "Anh Bình."

    "Thiên An khựng lại rất nhẹ."

    thienan neutral "Anh Bình thường không thích họp trực tiếp."

    quang "Ừ."

    "Quang đẩy một tập giấy mỏng về phía cô."

    quang "Nên anh in thêm phần lịch sử trao đổi với bên đó. Em xem trên xe cũng được."

    "Thiên An không nói gì."

    "Cô nhận tập giấy."

    "Mép giấy hơi cong lên vì được đọc qua trước đó."

    "Tâm nhìn thấy điều đó."

    $ story_flag('business_irregularity_seeded')

    return