# FILE: game/story/tam/tam_c03_thienan_family/s05_tam_observes_quang.rpy
# Scene file.

label tam_c03_thienan_family_s05_tam_observes_quang:
    scene bg_tam_family_living_room_evening
    with dissolve

    "Gần mười một giờ, Quang quay lại."

    "Lần này anh không bấm chuông."

    "Anh gọi điện trước cho Thiên An, nhưng người nghe máy là Tâm."

    tam neutral "Chị An ngủ rồi ạ."

    quang "À... vậy thôi. Anh để mai cũng được."

    tam neutral "Anh cần lấy gì sao?"

    quang "Không. Anh thấy trong bản hồ sơ còn thiếu một giấy xác nhận. Anh mang qua để sáng mai An khỏi tìm."

    "Tâm nhìn về phía phòng khách."

    "Thiên An đã ngủ gục trên sofa từ lúc nào."

    "Laptop mở trước mặt cô."

    "Một tay cô vẫn đặt trên tập giấy, như thể ngủ cũng chưa chịu buông công việc ra."

    tam neutral "Anh vào đi. Em mở cửa."

    scene bg_tam_family_entry_evening
    with dissolve

    "Quang bước vào rất khẽ."

    "Anh không hỏi Thiên An đâu."

    "Cũng không nói câu nào dư."

    "Chỉ đi vào phòng khách, đặt tập giấy lên bàn."

    scene bg_tam_family_living_room_evening
    with dissolve

    "Thiên An không tỉnh."

    "Quang đứng yên một lúc."

    "Tâm đứng ở gần cầu thang, bỗng thấy mình không nên lên tiếng."

    "Quang cúi xuống, nhìn màn hình laptop."

    "Anh không đọc nội dung."

    "Chỉ lưu file đang mở, đóng laptop lại, rồi kéo dây sạc ra khỏi mép bàn để nó không vướng vào tay Thiên An."

    "Sau đó anh lấy chiếc áo khoác trên ghế, phủ lên vai cô."

    "Động tác rất nhẹ."

    "Nhẹ đến mức Thiên An chỉ hơi cau mày rồi lại ngủ tiếp."

    "Quang nhìn cô thêm một nhịp."

    "Rồi anh lùi lại."

    tam neutral "Anh không gọi chị ấy dậy à?"

    quang "Không cần."

    tam neutral "Nhỡ chị ấy còn việc?"

    quang "Nếu thật sự gấp, cô ấy sẽ tự tỉnh."

    tam neutral "Còn nếu không?"

    quang "Thì việc đó không đáng để đánh thức cô ấy."

    "Tâm nhìn anh."

    "Quang nói rất bình thường."

    "Như thể đây không phải một câu dịu dàng."

    "Như thể anh chỉ đang đọc một điều khoản trong hợp đồng."

    tam neutral "Anh làm mấy chuyện này thường xuyên à?"

    quang "Chuyện nào?"

    tam neutral "Lưu file. Kéo dây sạc. Đắp áo. Để tài liệu đúng chỗ."

    quang "À."

    "Quang hơi ngẫm nghĩ."

    quang "Chắc vậy."

    tam confused "Chắc vậy?"

    quang "Làm lâu rồi nên anh không đếm."

    "Câu trả lời ấy làm Tâm im mất một lúc."

    "Người ta thường nhớ những lần mình hy sinh."

    "Quang thì không."

    "Hoặc anh đã giả vờ không nhớ quá giỏi."

    menu:
        "Tâm nghĩ gì về Quang lúc này?"

        "Anh ấy xứng đáng có một cơ hội":
            $ story_flag('tam_support_quang')
            $ story_flag('quang_an_route_seed')
            $ story_add_direction('thienan', 'quang')
            $ story_add('thienan_quang_trust', 1)
            $ story_add('tam_observation', 1)

            "Tâm không chắc Thiên An có thể nhìn Quang theo cách khác không."

            "Nhưng cô bỗng thấy nếu không ai thử kéo nhẹ cánh cửa ấy ra, có lẽ Quang sẽ đứng ngoài hiên thêm rất lâu."

            "Mưa không nhất thiết phải rơi."

            "Có người vẫn ướt vì chờ quá lâu."

        "Có lẽ chị An chưa từng nhận ra":
            $ story_flag('tam_noticed_quang_unseen_care')
            $ story_add('tam_observation', 2)
            $ story_add('thienan_quang_trust', 1)

            "Thiên An rất giỏi nhìn vấn đề."

            "Nhưng có lẽ cũng chính vì thế, những điều quá gần lại dễ bị cô xem như một phần của trật tự."

            "Một chiếc áo khoác được phủ lên vai."

            "Một file được lưu kịp."

            "Một người luôn đứng vừa đủ gần."

        "Có lẽ anh ấy nên dừng lại":
            $ story_flag('tam_quang_interest_seed')
            $ story_add('tam_self_clarity', 1)
            $ story_add('thienan_quang_trust', -1)

            "Tâm không biết vì sao mình nghĩ như vậy."

            "Có lẽ vì nhìn một người kiên nhẫn quá lâu cũng hơi đau."

            "Có lẽ vì cô không chắc Thiên An sẽ quay lại."

            "Hoặc có lẽ..."

            "Tâm dừng suy nghĩ đó lại."

            "Cô nhìn Quang."

            "Lần đầu tiên, cô không chỉ nhìn anh như trợ lý của chị mình."

    tam neutral "Anh Quang."

    quang "Ừ?"

    tam neutral "Anh thích chị em à?"

    "Quang khựng lại."

    "Rất nhẹ."

    "Nhưng đủ."

    quang "Câu hỏi này hơi trực tiếp đấy."

    tam embarrassed "Em biết."

    quang "Ai dạy em hỏi vậy?"

    tam neutral "Không ai cả."

    quang "Vậy em nên đổi giáo trình."

    "Tâm không cười."

    "Quang nhìn cô một lúc, rồi ánh mắt dịu xuống."

    quang "Anh không muốn làm cô ấy khó xử."

    tam neutral "Đó không phải câu trả lời."

    quang "Với người lớn, đôi khi đó là câu trả lời an toàn nhất."

    tam neutral "Chị An cũng vừa nói gần giống vậy."

    quang "Vậy chắc anh bị lây."

    "Quang cầm túi tài liệu rỗng lên."

    quang "Anh về đây. Em khóa cửa cẩn thận."

    tam neutral "Vâng."

    "Anh đi ra đến cửa thì dừng lại."

    quang "Tâm."

    tam neutral "Dạ?"

    quang "Đừng nói với An chuyện áo khoác."

    tam confused "Vì sao?"

    quang "Cô ấy sẽ trả lại."

    "Quang cười rất nhẹ."

    quang "Mà tối nay trời lạnh."

    "Cánh cửa khép lại."

    "Tâm đứng yên trong phòng khách."

    "Sau lưng cô, Thiên An vẫn ngủ."

    "Chiếc áo khoác trên vai chị rơi lệch một góc."

    "Tâm bước tới, kéo lại cho ngay."

    "Rồi cô chợt nhận ra mình vừa làm điều Quang đã làm."

    $ story_flag('tam_saw_quang_private_care')

    return