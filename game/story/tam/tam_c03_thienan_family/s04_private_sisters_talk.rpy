# FILE: game/story/tam/tam_c03_thienan_family/s04_private_sisters_talk.rpy
# Scene file.

label tam_c03_thienan_family_s04_private_sisters_talk:
    scene black
    with fade

    $ story_flag('tam_private_talk_with_thienan')
    $ unlock_character_section("thienan", "inner_layer")
    $ unlock_character_section("tam", "inner_layer")

    "Sau bữa tối, Thiên An ra ban công."

    "Tâm đứng trong phòng khách một lúc, tay cầm hai cốc nước ấm."

    "Cô phân vân gần nửa phút."

    "Rồi vẫn bước ra."

    tam neutral "Nước này."

    thienan neutral "Cảm ơn."

    "Thiên An nhận cốc nước."

    "Hai chị em đứng cạnh nhau, nhìn xuống con đường nhỏ trước nhà."

    "Một chiếc xe chạy qua, ánh đèn lướt lên hàng cây rồi mất hút."

    tam melancholic "Chị giận em không?"

    thienan confused "Vì chuyện gì?"

    tam embarrassed "Vì lúc nãy."

    thienan neutral "Em nói đúng."

    tam surprised "Thật ạ?"

    thienan smile "Sao? Em nghĩ chị nhỏ mọn vậy à?"

    tam bashful "Không. Nhưng chị An bình thường rất... khó đoán."

    thienan teasing "Cách nói lịch sự của 'khó gần'?"

    tam embarrassed "Em không nói thế."

    thienan smile "Nhưng nghĩ vậy."

    "Tâm cúi đầu uống một ngụm nước."

    "Nước hơi nóng. Cô suýt nhăn mặt, nhưng kịp giữ lại."

    thienan neutral "Cẩn thận."

    tam neutral "Em biết rồi."

    "Thiên An nhìn cốc nước trong tay mình."

    "Rất lâu sau, cô mới nói tiếp."

    thienan tired "Mẹ không sai."

    tam worried "Vậy chị..."

    thienan neutral "Nhưng mẹ cũng không đúng hẳn."

    "Tâm im lặng."

    "Thiên An nói bằng giọng rất bình thường."

    "Nhưng chính vì bình thường nên Tâm mới thấy câu ấy mệt."

    menu:
        "Tâm hỏi Thiên An điều gì?"

        "Chị có hạnh phúc không?":
            $ story_add('thienan_self_assertion', 1)
            $ story_add('tam_observation', 1)
            $ story_flag('tam_asked_thienan_happiness')
            $ unlock_character_section("thienan", "core_traits")
            $ unlock_character_section("tam", "narrative_function")

            tam melancholic "Chị An."

            thienan neutral "Ừ?"

            tam neutral "Chị có hạnh phúc không?"

            "Thiên An không trả lời ngay."

            "Cô xoay cốc nước trong tay. Hơi nóng phủ một lớp mỏng lên thành cốc."

            thienan smile "Câu hỏi này lớn quá."

            tam worried "Vậy trả lời nhỏ thôi cũng được."

            "Thiên An nhìn em gái."

            "Một lúc sau, cô bật cười rất khẽ."

            thienan melancholic "Có những ngày chị thấy ổn."

            tam neutral "Còn những ngày khác?"

            thienan neutral "Thì chị vẫn làm việc."

            "Câu trả lời không buồn."

            "Nhưng Tâm lại thấy cổ họng mình khô đi."

        "Chị từng thích ai chưa?":
            $ story_add('thienan_minh_residue', 1)
            $ story_add('tam_observation', 1)
            $ story_flag('tam_heard_minh_hint')
            $ unlock_character_section("thienan", "notes")

            tam neutral "Chị từng thích ai chưa?"

            thienan surprised "Sao tự nhiên hỏi vậy?"

            tam embarrassed "Em chỉ... tò mò."

            thienan teasing "Tò mò kiểu em gái, hay tò mò kiểu thám tử nghiệp dư?"

            tam bashful "Hai cái đó khác nhau ạ?"

            "Thiên An cười."

            "Nhưng nụ cười ấy chậm rãi tắt đi khi cô nhìn ra ngoài đường."

            thienan neutral "Từng."

            tam surprised "Thật ạ?"

            thienan smile "Chị cũng là người mà."

            tam neutral "Người đó... như thế nào?"

            "Thiên An im lặng rất lâu."

            thienan melancholic "Rất giỏi."

            tam neutral "Chỉ vậy thôi ạ?"

            thienan neutral "Rất tử tế."

            "Cô dừng lại."

            thienan smile "Và rất không thuộc về chị."

            "Tâm không hỏi tên."

            "Có lẽ vì cô biết, nếu Thiên An muốn nói, chị đã nói rồi."

        "Không hỏi gì, chỉ đứng cạnh chị":
            $ story_add('thienan_quang_trust', 1)
            $ story_add('thienan_self_assertion', 1)
            $ story_flag('tam_sat_with_thienan_in_silence')
            $ unlock_character_section("tam", "core_traits")

            "Tâm định hỏi."

            "Rồi lại thôi."

            "Cô chỉ đứng cạnh Thiên An, hai tay ôm cốc nước."

            "Gió đêm hơi lạnh."

            "Thiên An nhìn em gái, ánh mắt mềm hơn một chút."

            thienan neutral "Em không hỏi gì à?"

            tam smile "Hôm nay chị bị hỏi đủ rồi."

            "Thiên An khựng lại."

            "Rồi cô quay đi."

            thienan smile "Ừ. Đủ thật."

    "Hai cốc nước nguội dần."

    "Không ai nhắc đến chuyện hôn nhân nữa."

    "Nhưng từ đêm đó, Tâm bắt đầu hiểu rằng Thiên An không phải không có điều muốn nói."

    "Chỉ là chị đã quen sống như thể mình không cần nói ra."

    return