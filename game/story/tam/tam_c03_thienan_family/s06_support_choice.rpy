# FILE: game/story/tam/tam_c03_thienan_family/s06_support_choice.rpy
# Scene file.

label tam_c03_thienan_family_s06_support_choice:
    scene bg_tam_family_entry_evening
    with dissolve

    "Sáng hôm sau, trời chưa sáng hẳn thì Thiên An đã chuẩn bị ra sân bay."

    "Tâm xuống dưới nhà khi nghe tiếng vali kéo qua nền gạch."

    scene bg_tam_family_living_room_evening
    with dissolve

    "Thiên An mặc áo khoác mỏng, tóc buộc gọn sau gáy."

    "Trên cổ tay cô là chiếc đồng hồ thường dùng khi đi công tác."

    "Quang đứng cạnh cửa, tay cầm điện thoại, vẻ mặt tỉnh táo đến mức khiến người khác nghi ngờ anh có thật sự ngủ hay không."

    tam tired "Hai người đi sớm vậy ạ?"

    thienan neutral "Em ngủ tiếp đi."

    tam neutral "Em dậy rồi."

    thienan neutral "Mặt em nói khác."

    quang "Anh đồng ý với An."

    tam embarrassed "Hai người đi công tác mà cũng hợp tác bắt nạt em à?"

    quang "Không. Đây là đánh giá độc lập."

    thienan smile "Khá khách quan."

    "Tâm lườm cả hai."

    "Quang mỉm cười."

    "Thiên An kéo vali ra cửa."

    tam neutral "Chị."

    thienan neutral "Ừ?"

    tam neutral "Đi cẩn thận."

    "Thiên An nhìn cô."

    "Rồi cô đưa tay kéo lại cổ áo ngủ bị lệch của Tâm."

    thienan neutral "Em cũng vậy. Ở nhà đừng để mẹ hỏi dồn quá thì lại khai hết chuyện riêng."

    tam embarrassed "Em có chuyện riêng gì đâu."

    thienan smile "Vậy càng đáng nghi."

    "Thiên An nói xong thì đi ra trước."

    scene bg_tam_family_entry_evening
    with dissolve

    "Quang chậm hơn một nhịp."

    "Anh kiểm tra lại khóa vali cho Thiên An, rồi mới quay sang Tâm."

    quang "Nhờ em để ý cô chú giúp anh."

    tam neutral "Bố mẹ em á?"

    quang "Ừ. Và An nữa."

    tam neutral "Chị An đi với anh mà."

    quang "Không phải lúc nào người ở cạnh cũng nhìn được hết."

    "Tâm im lặng."

    "Câu đó không giống lời nhờ vả thông thường."

    "Nó giống một người đã hiểu rõ giới hạn của chính mình."

    menu:
        "Tâm trả lời Quang thế nào?"

        "\"Em sẽ giúp anh.\"":
            $ story_flag('tam_promised_quang_support')
            $ story_flag('tam_support_quang')
            $ story_flag('quang_an_route_seed')
            $ story_add_direction('thienan', 'quang')
            $ story_add('thienan_quang_trust', 2)

            tam neutral "Em sẽ giúp anh."

            "Quang hơi khựng lại."

            quang "Giúp anh?"

            tam neutral "Vâng."

            "Tâm nhìn ra ngoài cửa."

            "Thiên An đang đứng cạnh xe, cúi xuống kiểm tra tin nhắn."

            tam neutral "Nếu có lúc chị ấy không nhìn thấy, em sẽ thử nhắc."

            quang "Tâm..."

            tam neutral "Nhưng em không hứa thành công đâu."

            quang "Anh biết."

            "Quang cười."

            "Nụ cười ấy nhẹ hơn thường ngày."

            quang "Chỉ cần em đừng làm cô ấy khó chịu là được."

            tam teasing "Nghe như anh có kinh nghiệm thất bại rồi."

            quang "Rất nhiều."

            "Anh nói bình thản."

            "Bình thản đến mức Tâm không trêu tiếp được."

        "\"Em sẽ giúp chị em.\"":
            $ story_flag('tam_supports_thienan')
            $ story_add('thienan_self_assertion', 2)
            $ story_add('tam_observation', 1)

            tam neutral "Em sẽ giúp chị em."

            "Quang nhìn cô."

            "Rồi anh gật đầu."

            quang "Vậy là đủ rồi."

            tam neutral "Anh không thấy hụt hẫng à?"

            quang "Không."

            "Quang nhìn về phía Thiên An."

            quang "Nếu cô ấy ổn hơn, thì ai giúp không quan trọng."

            "Tâm không biết nên gọi đó là cao thượng hay cứng đầu."

            "Có khi là cả hai."

        "\"Một ngày nào đó, anh nên nói rõ với chị ấy.\"":
            $ story_flag('tam_encouraged_quang_confession')
            $ story_flag('quang_an_route_seed')
            $ story_add_direction('thienan', 'quang')
            $ story_add('thienan_quang_trust', 1)
            $ story_add('thienan_self_assertion', 1)

            tam neutral "Một ngày nào đó, anh nên nói rõ với chị ấy."

            "Quang im lặng."

            "Ngoài cửa, tiếng động cơ xe khẽ rung trong buổi sáng sớm."

            quang "Anh từng nghĩ vậy."

            tam neutral "Rồi sao ạ?"

            quang "Rồi anh nhận ra có những câu nói ra chỉ để người nói nhẹ lòng hơn."

            tam neutral "Nhưng nếu không nói thì người kia không biết."

            quang "Có thể."

            "Quang nhìn Tâm."

            quang "Nhưng An không phải người không biết."

            tam confused "Vậy chị ấy biết?"

            quang "Anh không chắc."

            "Anh cười nhẹ."

            quang "Và anh cũng không đủ can đảm để chắc."

            "Tâm nhìn anh."

            "Người đàn ông này không yếu."

            "Chỉ là có những người càng nghiêm túc, càng không dám dùng tình cảm của mình để ép người khác phải trả lời."

        "\"Anh cũng nên nghĩ cho mình.\"":
            $ story_flag('tam_quang_interest_seed')
            $ story_add('tam_self_clarity', 1)
            $ story_add('tam_observation', 1)

            tam neutral "Anh cũng nên nghĩ cho mình."

            "Quang hơi ngạc nhiên."

            quang "Anh?"

            tam neutral "Vâng. Anh."

            "Tâm siết nhẹ tay vào tay áo."

            tam neutral "Em không biết chuyện giữa anh và chị An là gì. Nhưng nếu một người cứ đứng mãi một chỗ..."

            "Cô dừng lại."

            "Không biết nên nói tiếp thế nào cho đúng."

            quang "Sẽ mỏi chân?"

            tam embarrassed "Đại khái vậy."

            "Quang bật cười rất khẽ."

            quang "Ừ. Cũng có lúc mỏi."

            "Tâm ngẩng lên."

            "Lần đầu tiên, trong mắt Quang có một chút mệt mỏi không kịp giấu."

            "Rất nhanh thôi."

            "Nhưng cô đã thấy."

    thienan "Anh Quang."

    "Giọng Thiên An gọi từ ngoài cửa."

    quang "Anh ra ngay."

    "Quang quay lại với Tâm."

    quang "Cảm ơn em."

    tam neutral "Vì chuyện gì ạ?"

    quang "Vì đã dậy sớm."

    tam confused "Chỉ vậy thôi?"

    quang "Ừ."

    "Quang đi ra ngoài."

    "Tâm đứng trong cửa, nhìn hai người bước tới xe."

    "Thiên An ngồi vào ghế sau, đã mở laptop."

    "Quang cúi xuống nói gì đó với tài xế, rồi vòng sang phía còn lại."

    "Trước khi đóng cửa xe, anh nhìn về phía Tâm, gật nhẹ."

    "Tâm gật lại."

    "Chiếc xe rời khỏi cổng."

    "Buổi sáng còn rất mỏng."

    "Trong phòng khách, chiếc cốc nước Thiên An uống dở tối qua vẫn đặt trên bàn."

    "Tâm cầm lên."

    "Nước đã lạnh."

    return