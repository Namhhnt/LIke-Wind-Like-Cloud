# FILE: game/story/tam/tam_c03_thienan_family/s07_career_seed.rpy
# Scene file.

label tam_c03_thienan_family_s07_career_seed:
    scene bg_tam_room_morning
    with fade

    "Sau khi Thiên An đi, Tâm lên phòng."

    "Cô định ngủ tiếp."

    "Ít nhất là cô tự nói với mình như vậy."

    "Nhưng khi đặt lưng xuống giường, cô lại nhìn thấy một tập giấy để trên bàn học."

    "Không phải của cô."

    "Tập giấy được kẹp rất gọn, bên trên dán một tờ note nhỏ."

    "Nét chữ của Thiên An."

    thienan "Nếu em bắt đầu đi làm thật sự, đọc cái này trước."

    "Tâm ngồi dậy."

    "Cô cầm tập giấy lên."

    "Bên trong không phải tài liệu chuyên ngành gì cao siêu."

    "Chỉ là vài trang checklist."

    "Cách chuẩn bị trước cuộc họp."

    "Cách ghi lại việc cần làm."

    "Cách đọc một email mà không bị cuốn theo giọng điệu của người gửi."

    "Cách từ chối việc không thuộc trách nhiệm mà vẫn giữ được quan hệ."

    "Ở trang cuối, Thiên An viết thêm một dòng."

    thienan "Đừng làm việc chăm chỉ chỉ để người khác thấy em chăm chỉ. Làm việc đúng."

    "Tâm đọc đi đọc lại câu đó."

    "Rất Thiên An."

    "Khô."

    "Gọn."

    "Và hơi đáng ghét vì đúng."

    menu:
        "Tâm tiếp nhận lời khuyên của Thiên An thế nào?"

        "Dùng nó nghiêm túc":
            $ story_add('career_tam', 2)
            $ story_add('tam_self_clarity', 1)
            $ story_flag('tam_uses_thienan_career_notes')

            "Tâm lấy một chiếc bút."

            "Cô gạch chân vài dòng."

            "Rồi mở điện thoại, tạo một checklist mới cho ngày làm việc tiếp theo."

            "Cô không chắc mình có thể giống Thiên An."

            "Nhưng có lẽ cô không cần giống."

            "Cô chỉ cần học cách đứng vững bằng nhịp của mình."

        "Cảm thấy mình bị so sánh với chị":
            $ story_add('tam_insecurity', 1)
            $ story_add('career_tam', 1)
            $ story_flag('tam_feels_compared_to_thienan')

            "Tâm đặt tập giấy xuống."

            "Cô biết Thiên An có ý tốt."

            "Chính vì biết nên cảm giác khó chịu ấy mới làm cô thấy mình nhỏ nhen."

            "Chị cô làm gì cũng gọn."

            "Ngay cả quan tâm người khác cũng gọn."

            "Còn Tâm thì chỉ đọc vài trang checklist đã thấy mình như một học sinh vừa nhận bài kiểm tra chưa làm."

            "Cô thở ra."

            "Rồi vẫn cầm bút lên."

            "Khó chịu thì khó chịu."

            "Đúng vẫn là đúng."

        "Nhắn tin cảm ơn chị":
            $ story_add('thienan_self_assertion', 1)
            $ story_add('career_tam', 1)
            $ story_flag('tam_thanked_thienan_honestly')

            "Tâm mở điện thoại."

            "Cô gõ một dòng."

            tam "Em đọc rồi. Cảm ơn chị."

            "Nghĩ một lúc, cô xóa đi."

            "Gõ lại."

            tam "Em đọc rồi. Có vài chỗ hơi khó chịu vì đúng quá. Cảm ơn chị."

            "Cô nhìn màn hình thêm vài giây rồi bấm gửi."

            "Tin nhắn hiện trạng thái đã gửi."

            "Một phút sau, Thiên An trả lời."

            thienan "Khó chịu là dấu hiệu tốt."

            "Tâm nhìn dòng chữ ấy."

            tam bored "Đúng là chị mình."

            "Cô định đặt điện thoại xuống thì lại có tin nhắn thứ hai."

            thienan "Cố lên."

            "Hai chữ rất ngắn."

            "Không hoa mỹ."

            "Không dịu dàng quá mức."

            "Nhưng Tâm nhìn nó lâu hơn cần thiết."

    if story_has_flag('tam_promised_quang_support'):
        "Điện thoại rung thêm một lần."

        "Lần này là tin nhắn từ Quang."

        quang "An ngủ trên xe rồi. Cảm ơn em sáng nay."

        "Tâm nhìn dòng tin nhắn."

        "Cô không biết vì sao anh phải báo với cô chuyện đó."

        "Có lẽ vì cô đã hứa sẽ giúp anh."

        "Có lẽ vì anh cần nói với một người rằng cuối cùng Thiên An cũng ngủ."

        "Tâm gõ lại."

        tam "Anh cũng ngủ đi nếu có thể."

        "Quang trả lời rất nhanh."

        quang "Anh sẽ cố."

        "Nghe không giống một lời hứa."

        "Nhưng ít nhất cũng là một ý định."

    elif story_has_flag('tam_quang_interest_seed'):
        "Tâm mở điện thoại, nhưng không nhắn cho Thiên An ngay."

        "Danh bạ dừng ở tên Quang."

        "Cô nhìn cái tên ấy lâu hơn một chút."

        "Rồi tắt màn hình."

        "Có những cảm giác nếu gọi tên quá sớm sẽ trở nên rất phiền."

        "Tâm hiện tại chưa muốn phiền đến thế."

    elif story_has_flag('tam_encouraged_quang_confession'):
        "Tâm nhớ lại vẻ mặt của Quang lúc cô bảo anh nên nói rõ với Thiên An."

        "Một người tốt chưa chắc sẽ được yêu."

        "Một người kiên nhẫn chưa chắc sẽ được đợi lại."

        "Nhưng nếu không ai nói gì, mọi chuyện sẽ tiếp tục giống như cốc nước để qua đêm."

        "Không hỏng."

        "Chỉ lạnh đi."

    else:
        "Ngoài cửa sổ, trời đã sáng hẳn."

        "Tâm đặt tập giấy vào ngăn bàn."

        "Cô có cảm giác chương này của gia đình mình chưa kết thúc."

        "Chỉ là tạm thời được gấp lại."

    $ story_flag('tam_c03_thienan_family_completed_seed')

    return