# FILE: game/story/tam/tam_c03_thienan_family/s04_private_sisters_talk.rpy
# Scene file.

label tam_c03_thienan_family_s04_private_sisters_talk:
    scene bg_tam_family_balcony_night
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

    scene cg_tam_c03_sisters_balcony
    with dissolve

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

    scene bg_tam_family_balcony_night
    with dissolve

    # Repeatable sister-talk menu.
    # Tâm can ask up to 4 times.
    # Each question has 2 depth levels.
    # Choosing silence ends the loop immediately.

    $ sister_talk_turns = 0
    $ sister_talk_max_turns = 4
    $ asked_happiness_count = 0
    $ asked_love_count = 0
    $ chose_silence = False

    while sister_talk_turns < sister_talk_max_turns:

        menu:
            "Tâm hỏi Thiên An điều gì?"

            "Chị có hạnh phúc không?" if asked_happiness_count < 2:
                $ sister_talk_turns += 1
                $ asked_happiness_count += 1

                if asked_happiness_count == 1:
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

                else:
                    $ story_add('thienan_self_assertion', 1)
                    $ story_add('tam_observation', 2)
                    $ story_flag('tam_pressed_thienan_happiness_deeper')
                    $ unlock_character_section("thienan", "defense_mechanisms")

                    "Tâm nhìn xuống cốc nước của mình."

                    "Lần này, cô không uống."

                    tam neutral "Nếu không làm việc thì sao?"

                    thienan confused "Gì cơ?"

                    tam melancholic "Những ngày chị không ổn ấy."

                    "Thiên An khựng lại."

                    tam neutral "Nếu hôm đó chị không cố làm việc nữa thì chị muốn làm gì?"

                    "Gió đêm lướt qua ban công."

                    "Thiên An đặt ngón tay lên miệng cốc. Không xoay nữa."

                    thienan neutral "Chị chưa nghĩ tới."

                    tam worried "Chưa từng ạ?"

                    thienan tired "Chưa có thời gian."

                    "Tâm im lặng."

                    "Câu đó nghe giống một câu trả lời."

                    "Nhưng cũng giống một thói quen đã được dùng quá lâu."

                    tam melancholic "Vậy sau này nghĩ thử đi."

                    thienan neutral "Nghĩ để làm gì?"

                    tam smile "Để lúc mệt còn biết mình muốn trốn đi đâu."

                    "Thiên An nhìn Tâm."

                    "Ánh mắt cô hơi mềm xuống, nhưng giọng vẫn tỉnh."

                    thienan smile "Em học nói mấy câu đó từ ai vậy?"

                    tam bashful "Tự nhiên biết thôi."

                    thienan teasing "Ừ. Tự nhiên."

            "Chị từng thích ai chưa?" if asked_love_count < 2:
                $ sister_talk_turns += 1
                $ asked_love_count += 1

                if asked_love_count == 1:
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

                else:
                    $ story_add('thienan_minh_residue', 1)
                    $ story_add('tam_observation', 2)
                    $ story_add('tam_self_clarity', 1)
                    $ story_flag('tam_noticed_thienan_old_feeling')
                    $ unlock_character_section("thienan", "core_wound")

                    "Tâm đưa hai tay ôm cốc nước."

                    "Cô biết mình không nên hỏi quá sâu."

                    "Nhưng nếu hoàn toàn không hỏi, có lẽ Thiên An sẽ lại gấp mọi thứ vào trong như mọi lần."

                    tam neutral "Chị còn nghĩ về người đó không?"

                    thienan neutral "Em hỏi hơi nhiều rồi đấy."

                    tam embarrassed "Em biết."

                    "Tâm cúi mắt."

                    "Một giây sau, cô vẫn nói tiếp."

                    tam melancholic "Nhưng em muốn biết."

                    "Thiên An nhìn em gái."

                    "Lần này cô không cười."

                    thienan neutral "Có."

                    "Câu trả lời ngắn đến mức gần như bị gió cuốn đi."

                    "Nhưng Tâm nghe rất rõ."

                    tam neutral "Vậy sao chị không..."

                    thienan neutral "Vì có những chuyện không phải cứ muốn là được."

                    tam worried "Nhưng nếu cứ không nói thì người ta làm sao biết?"

                    "Thiên An khẽ thở ra."

                    "Hơi thở ấy rất nhẹ."

                    "Nhẹ đến mức nếu không đứng cạnh, Tâm chắc sẽ bỏ qua."

                    thienan melancholic "Có những người biết rồi cũng không thể làm gì."

                    tam neutral "Người đó biết ạ?"

                    "Thiên An nhìn xuống con đường bên dưới."

                    "Một chiếc xe khác chạy qua."

                    "Ánh đèn lần này lướt lên mặt cô rất nhanh, rồi tắt."

                    thienan smile "Em gái ngoan thì không hỏi đến cùng."

                    tam bashful "Vậy em làm em gái hơi hư một chút được không?"

                    "Thiên An bật cười rất khẽ."

                    "Lần này, nụ cười ấy thật hơn một chút."

                    thienan neutral "Hôm nay thôi."

            "Không hỏi gì, chỉ đứng cạnh chị":
                $ story_add('thienan_quang_trust', 1)
                $ story_add('thienan_self_assertion', 1)
                $ story_flag('tam_sat_with_thienan_in_silence')
                $ unlock_character_section("tam", "core_traits")
                $ chose_silence = True
                $ sister_talk_turns = sister_talk_max_turns

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

    # Bonus for asking instead of stopping early.
    # Asking all question types is also care, not interrogation.

    if not chose_silence and asked_happiness_count >= 1 and asked_love_count >= 1:
        $ story_add('tam_observation', 1)
        $ story_add('thienan_self_assertion', 1)
        $ story_flag('tam_asked_all_sister_talk_topics')

        "Tâm nhận ra mình đã hỏi nhiều hơn bình thường."

        "Nhưng Thiên An vẫn chưa bảo cô dừng lại."

        "Điều đó khiến cô can đảm thêm một chút."

    if not chose_silence and asked_happiness_count >= 2 and asked_love_count >= 2:
        $ story_add('tam_observation', 1)
        $ story_add('tam_self_clarity', 1)
        $ story_add('thienan_self_assertion', 1)
        $ story_flag('tam_exhausted_private_sister_talk')
        $ unlock_character_section("tam", "relationship_to_thienan")
        $ unlock_character_section("thienan", "relationship_to_tam")

        "Đến khi không còn câu nào dễ hỏi nữa, Tâm mới nhận ra tay mình đã siết cốc nước hơi chặt."

        "Hỏi nhiều cũng mệt."

        "Nhưng có lẽ im lặng mãi còn mệt hơn."

        thienan neutral "Em hôm nay lạ thật."

        tam embarrassed "Lạ xấu ạ?"

        thienan smile "Không."

        "Thiên An nhìn ra ngoài đường."

        "Một lúc sau, cô nói nhỏ hơn."

        thienan neutral "Lạ giống người lớn hơn."

        "Tâm cúi xuống nhìn cốc nước."

        "Lần này, cô không biết nên vui hay nên buồn."

    "Hai cốc nước nguội dần."

    "Không ai nhắc đến chuyện hôn nhân nữa."

    "Nhưng từ đêm đó, Tâm bắt đầu hiểu rằng Thiên An không phải không có điều muốn nói."

    "Chỉ là chị đã quen sống như thể mình không cần nói ra."

    return
