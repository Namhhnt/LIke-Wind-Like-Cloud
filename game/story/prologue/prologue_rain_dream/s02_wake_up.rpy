# FILE: game/story/prologue/prologue_rain_dream/s02_wake_up.rpy
# Scene file.

label prologue_rain_dream_s02_wake_up:
    scene bg_tam_room_morning
    with fade

    "Tâm mở mắt."

    "Trần phòng quen thuộc hiện ra trước mắt cô."
    "Không có mái hiên. Không có con phố ướt. Không có người đàn ông đứng trong mưa."

    "Chỉ có tiếng điều hòa chạy rất khẽ, chiếc rèm cửa màu kem, và ánh sáng buổi sáng đang trườn qua một khe hở nhỏ."

    tam tired "..."

    "Cô nằm yên thêm vài giây."
    "Một tay vẫn đặt trên ngực, như thể vừa tỉnh dậy sau khi chạy một quãng rất dài."

    "Điện thoại trên tủ đầu giường rung lên."

    "06:30."

    "Phỏng vấn lúc chín giờ."

    "Tâm nhắm mắt lại, thở ra một hơi."

    tam confused "Mơ thôi mà..."

    "Câu đó đáng lẽ phải làm cô nhẹ lòng hơn."
    "Nhưng nó không làm được."

    scene cg_prologue_tam_wakes
    with dissolve

    "Cô ngồi dậy, kéo chăn sang một bên."
    scene bg_tam_room_morning
    with dissolve

    "Dưới chân giường, đôi dép trong nhà nằm lệch nhau. Một chiếc quay ngang, một chiếc quay về phía cửa."

    "Tâm nhìn chúng vài giây."

    "Rồi cô cúi xuống, đặt lại cho ngay."

    "Việc nhỏ thôi."
    "Nhưng không hiểu sao sau khi làm xong, lòng cô vẫn chưa yên."

    "Cô bước vào phòng tắm, rửa mặt bằng nước lạnh."
    "Nước chảy qua cổ tay, lạnh đến mức làm cô tỉnh hẳn."

    "Trong gương, khuôn mặt cô vẫn bình thường."
    "Chỉ có đôi mắt là hơi thiếu ngủ."

    tam neutral "Hôm nay là ngày phỏng vấn. Tập trung đi."

    "Cô nói với chính mình."
    "Giọng nghe rất có lý."

    "Nhưng khi đưa tay lấy khăn mặt, Tâm lại khựng lại."
    "Trên cổ tay cô vẫn còn cảm giác ai đó đã từng chạm rất nhẹ."

    menu:
        "Tâm xử lý giấc mơ đó thế nào?"

        "Xem nó là một dấu hiệu đáng chú ý":
            $ story_add('tam_observation', 1)

            "Tâm quay lại bàn, kéo ngăn tủ lấy một quyển sổ nhỏ."
            "Cô không viết dài. Chỉ ghi vài chữ."

            "\"Mưa. Mái hiên. Lại là người đó. Giọng nói vẫn vậy.\""

            "Ngòi bút dừng lại rất lâu sau chữ cuối cùng."
            "Cuối cùng, cô gấp mép trang lại."

            tam neutral "Để sau tính."

        "Gạt đi như áp lực trước phỏng vấn":
            $ story_add('career_tam', 1)

            "Tâm đóng vòi nước, lau mặt thật nhanh."
            "Một giấc mơ kỳ lạ vào buổi sáng ngày phỏng vấn không phải chuyện hiếm."

            "Cô có đủ thứ cần lo: hồ sơ, portfolio, câu trả lời, đường đi, thời gian đến nơi."

            "Một người đàn ông không rõ mặt trong mưa rõ ràng không nằm trong danh sách ưu tiên."

            tam neutral "Đi phỏng vấn trước đã."

        "Thấy bất an nhưng không gọi tên":
            $ story_add('doom_score', 1)

            "Tâm không ghi lại."
            "Cũng không tự thuyết phục mình quên đi."

            "Cô chỉ đứng yên trước gương lâu hơn bình thường một chút."
            "Khăn mặt trong tay bị cô vặn lệch đi."

            tam melancholic "..."

            "Đến khi nhận ra, cô mới chậm rãi gấp nó lại cho ngay ngắn."

    "Ngoài cửa sổ, trời sáng hẳn."
    "Một ngày bình thường bắt đầu theo đúng cách bình thường của nó."

    "Chỉ có Tâm biết có gì đó vừa lệch đi một chút."

    return
