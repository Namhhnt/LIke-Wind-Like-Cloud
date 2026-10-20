# FILE: game/story/tam/tam_c01_interview_day/s03_success_result.rpy
# Scene file.

label tam_c01_interview_day_s03_success_result:
    scene bg_company_lobby_noon
    with fade

    "Gần trưa, lobby công ty đông hơn lúc sáng."

    "Nhân viên đi ngang qua với thẻ đeo trên cổ, tay cầm cà phê, điện thoại, laptop."

    "Tâm và Huyền ngồi ở hàng ghế gần cửa kính."

    "Cả hai đã thôi nói về câu hỏi phỏng vấn từ mười phút trước."

    "Nói nữa cũng không làm kết quả đến nhanh hơn."

    huyen tired "Tao đói."

    tam neutral "Ừ."

    huyen "Mày không định an ủi tao à?"

    tam smile "Đói thì lát ăn."

    huyen irritated "Đúng là câu trả lời của người cũng đang đói."

    "Điện thoại của Huyền rung trước."

    "Cô cúi nhìn màn hình."

    "Rồi bất động."

    tam neutral "Huyền?"

    huyen surprised "Tâm..."

    "Giọng Huyền nhỏ đến mức gần như không ra tiếng."

    huyen "Tao qua rồi."

    "Tâm chưa kịp đáp, điện thoại của cô cũng rung lên."

    "Một email mới."

    "Tiêu đề ngắn gọn."

    "Interview Result."

    "Tâm mở email."

    "Mắt cô lướt qua những dòng chữ rất nhanh."

    "Rồi chậm lại ở câu cuối."

    tam surprised "..."

    huyen confused "Sao?"

    "Tâm đặt điện thoại xuống đùi."

    "Cô nhìn Huyền."

    "Khóe miệng run lên trước khi kịp thành nụ cười."

    tam happy "Tao cũng qua rồi."

    $ story_flag('tam_interview_passed')
    $ story_flag('huyen_interview_passed')
    $ story_flag('tam_huyen_first_job_offer')

    "Huyền mở to mắt."

    "Một giây."

    "Hai giây."

    scene cg_tam_c01_offer_hug
    with dissolve

    "Rồi cô chồm tới ôm chầm lấy Tâm."

    huyen laughing "Qua rồi! Qua thật rồi!"

    tam laughing "Nhẹ thôi. Người ta nhìn kìa."

    huyen happy "Kệ người ta. Người ta không phỏng vấn thay tao."

    "Tâm cười."

    "Vai cô hơi run."

    "Không biết vì vui, vì nhẹ nhõm, hay vì cuối cùng buổi sáng dài quá mức kia đã chịu kết thúc."

    scene bg_company_lobby_noon
    with dissolve

    menu:
        "How do they react?"

        "Celebrate together":
            $ story_flag('tam_huyen_strong_bond')
            $ story_add('career_huyen', 1)

            huyen happy "Tối nay đi ăn."

            tam smile "Vừa nhận việc đã tiêu tiền à?"

            huyen teasing "Đầu tư tinh thần."

            tam "Nghe giống cái cớ."

            huyen "Cớ tốt."

            "Huyền kéo điện thoại ra, bắt đầu tìm nhà hàng."

            huyen neutral "Không ăn lẩu bình dân. Hôm nay phải tử tế một chút."

            tam confused "Tử tế là sao?"

            huyen grinning "Có khăn ăn gấp hình gì đó. Có ánh đèn vàng. Có menu nhìn vào hơi đau ví."

            tam laughing "Mày gọi đó là tử tế?"

            huyen "Ừ. Để sau này nghèo còn có kỷ niệm sang."

            "Tâm muốn phản bác."

            "Nhưng rồi cô chỉ bật cười."

            tam smile "Được. Tối nay đi ăn."

            huyen happy "Chốt."

        "Call Thiên An first":
            $ story_add('thienan_self_assertion', 1)

            "Tâm cúi nhìn điện thoại."

            huyen neutral "Gọi chị An à?"

            tam surprised "Sao mày biết?"

            huyen teasing "Mặt mày mỗi lần định gọi chị là nghiêm túc hơn hẳn. Như sắp báo cáo tài chính gia đình."

            tam embarrassed "Làm gì đến mức đó."

            "Tâm bấm gọi."

            "Chuông reo ba hồi thì đầu dây bên kia bắt máy."

            thienan "Tâm?"

            tam shy "Chị đang bận không?"

            thienan "Không. Có chuyện gì?"

            "Tâm nhìn email trên màn hình thêm một lần."

            tam smile "Em qua phỏng vấn rồi."

            "Đầu dây bên kia im một nhịp rất ngắn."

            thienan "Tốt."

            "Chỉ một chữ."

            "Nhưng giọng Thiên An mềm hơn bình thường."

            thienan "Chúc mừng em."

            tam happy "Vâng."

            thienan "Tối về nhà ăn cơm không? Chị nói mẹ nấu thêm món em thích."

            "Tâm hơi khựng lại."

            "Một lời chúc mừng rất kiểu Thiên An."

            "Không dài. Không ồn."

            "Nhưng có chỗ để về."

            tam smile "Tối nay chắc em đi ăn với Huyền trước. Mai em về được không?"

            thienan "Được. Đi chơi vui."

            tam "Vâng."

            "Cúp máy xong, Tâm vẫn nhìn màn hình thêm vài giây."

            huyen smile "Chị mày vui đấy."

            tam neutral "Chị ấy nói có một chữ."

            huyen teasing "Với chị mày, một chữ là pháo hoa rồi."

            tam laughing "Ừ. Chắc vậy."

        "Keep the joy quiet":
            $ story_add('tam_self_clarity', 1)

            "Tâm không nhảy lên."

            "Không hét."

            "Không vội gọi cho ai."

            "Cô chỉ cúi xuống đọc lại email một lần nữa."

            huyen confused "Mày bình tĩnh quá đấy."

            tam neutral "Không. Tao đang cố nhớ cảm giác này."

            huyen "Cảm giác gì?"

            tam "Cảm giác tự mình qua được một cửa."

            "Huyền im lại."

            "Rồi cô cười nhỏ."

            huyen smile "Ừ. Cửa đầu tiên."

            tam smile "Ừ. Cửa đầu tiên."

            "Tâm khóa màn hình điện thoại."

            "Lần này, cô không cần đọc lại nữa."

    "Cả hai rời khỏi lobby khi ánh nắng trưa đã hắt mạnh qua lớp kính lớn."

    "Trước cửa xoay, Huyền bỗng dừng lại."

    huyen neutral "Này."

    tam "Sao?"

    huyen smile "Tối nay vẫn phải đi ăn. Dù mày chọn nhánh nào đi nữa."

    tam confused "Nhánh nào?"

    huyen teasing "Không biết. Tao chỉ cảm giác đời mình vừa mở route mới."

    tam laughing "Mày chơi game ít thôi."

    huyen "Không. Từ hôm nay tao là nhân viên tương lai. Tao cần giải trí lành mạnh."

    "Tâm lắc đầu."

    "Nhưng nụ cười trên môi cô không hạ xuống."

    $ unlock_character_section("huyen", "inner_layer")
    return
