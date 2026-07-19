# FILE: game/story/tam/tam_c03_thienan_family/s06_support_choice.rpy
# Scene file.

label tam_c03_thienan_family_s06_support_choice:
    scene bg_hoangminh_villa_day
    with fade

    $ story_flag('tam_quang_support_choice_seen')
    $ unlock_character_section("quang", "notes")

    "Sáng hôm sau, Tâm gặp Quang ở cổng."

    "Anh đến sớm hơn giờ hẹn."

    "Trong tay là một túi giấy nhỏ, bên trong có vài hộp thuốc bổ, một gói cà phê không đường và một hộp kẹo bạc hà."

    tam confused "Anh mang gì nhiều vậy?"

    quang neutral "Không nhiều đâu."

    tam neutral "Nếu anh nói vậy thì chắc là nhiều."

    quang embarrassed "Một chút đồ cho chị An. Với cô chú."

    tam teasing "Anh có chắc là anh không định mở cửa hàng tiện lợi trước cổng nhà em không?"

    quang bashful "Nếu mở thì chắc lỗ."

    tam smile "Vì toàn đem cho không?"

    quang embarrassed "Ừm..."

    "Tâm bật cười."

    "Quang cũng cười theo, hơi ngượng."

    "Một người đàn ông trưởng thành, làm việc chắc chắn, vậy mà khi bị trêu lại có vẻ thật thà đến tội."

    "Nhưng có lẽ chính vì vậy nên bố mẹ cô mới quý anh."

    quang neutral "Tâm."

    tam neutral "Dạ?"

    quang neutral "Mấy ngày tới chị An có thể sẽ hơi căng. Nếu em thấy chị ấy bỏ bữa, nhờ em nhắc giúp anh."

    tam confused "Sao anh không tự nhắc?"

    quang smile "Anh nhắc thì chị ấy sẽ bảo anh lắm chuyện."

    tam teasing "Em nhắc thì chị ấy cũng bảo vậy thôi."

    quang neutral "Nhưng em là em gái. Được quyền hơn anh."

    "Câu nói ấy rất bình thường."

    "Nhưng Tâm lại thấy nó hơi buồn."

    "Quang biết rõ vị trí của mình."

    "Biết rõ đến mức chưa từng bước quá nửa bước."

    if story_has_flag('tam_sees_quang_as_possible_for_thienan'):
        "Tâm nhớ lại chiếc áo khoác trên vai Thiên An tối qua."

    elif story_has_flag('tam_quang_interest_seed'):
        "Tâm nhớ lại cách Quang đứng ngoài cửa, như thể đã quen với việc rời đi trước khi người khác kịp giữ."

    else:
        "Tâm nhìn túi giấy trong tay Quang, không hiểu vì sao mình lại thấy câu chuyện này đáng tiếc."

    menu:
        "Tâm trả lời Quang thế nào?"

        "Em sẽ giúp anh":
            $ story_add('thienan_quang_trust', 1)
            $ story_add('quang_persistence', 2)
            $ story_flag('tam_agrees_to_help_quang')
            $ story_flag('tam_support_quang')
            $ unlock_character_section("quang", "narrative_function")
            $ unlock_character_section("thienan", "notes")

            tam neutral "Em sẽ giúp anh."

            quang surprised "Giúp anh?"

            tam smile "Nhắc chị An ăn. Nhắc chị ấy nghỉ. Và nếu có cơ hội..."

            quang confused "Nếu có cơ hội?"

            tam teasing "Em chưa nghĩ ra. Nhưng chắc sẽ có."

            "Quang nhìn Tâm."

            "Ánh mắt anh thoáng rối, rồi dịu xuống."

            quang smile "Cảm ơn em."

            tam neutral "Nhưng anh cũng phải tự cố."

            quang embarrassed "Anh biết."

            tam irritated "Không. Anh không biết."

            "Quang khựng lại."

            tam neutral "Nếu biết thì anh đã không chờ lâu như vậy."

            "Quang im lặng."

            "Lần này, anh không cười để né."

        "Em sẽ giúp chị em":
            $ story_add('thienan_self_assertion', 1)
            $ story_add('tam_observation', 1)
            $ story_flag('tam_prioritizes_thienan_choice')
            $ unlock_character_section("tam", "narrative_function")
            $ unlock_character_section("thienan", "core_traits")

            tam neutral "Em sẽ giúp chị em."

            "Quang nhìn cô."

            "Rồi anh gật đầu."

            quang smile "Ừ. Như vậy là đúng."

            tam melancholic "Anh không buồn à?"

            quang neutral "Buồn thì cũng không được làm sai."

            "Tâm hơi khựng lại."

            quang smile "Anh thích chị An. Nhưng người cần được đặt ở giữa chuyện này là chị ấy, không phải anh."

            "Câu đó khiến Tâm không trêu tiếp được."

            "Vì nó quá đàng hoàng."

        "Anh nên nói với chị ấy một ngày nào đó":
            $ story_add('quang_persistence', 2)
            $ story_add('thienan_quang_trust', 1)
            $ story_flag('tam_encouraged_quang_confession')
            $ unlock_character_section("quang", "inner_layer")
            $ unlock_character_section("quang", "notes")

            tam neutral "Anh nên nói với chị ấy một ngày nào đó."

            quang surprised "Nói gì?"

            tam bored "Anh Quang."

            quang embarrassed "Ừ."

            "Anh đưa mắt nhìn sang chỗ khác."

            "Rất vụng."

            "Vụng đến mức Tâm thấy hơi buồn cười, nhưng cô không cười."

            tam neutral "Nếu không nói, chị em có thể sẽ không bao giờ biết."

            quang melancholic "Chị em không phải người không biết."

            tam confused "Vậy?"

            quang neutral "Biết và muốn nghe là hai chuyện khác nhau."

            "Tâm im lặng."

            "Quang cầm túi giấy bằng cả hai tay, như thể nó nặng hơn thực tế rất nhiều."

            quang smile "Nhưng anh sẽ nghĩ về chuyện đó."

        "Anh nên nghĩ cho mình nhiều hơn":
            $ story_add('tam_quang_interest', 2)
            $ story_add('quang_persistence', -1)
            $ story_flag('tam_tells_quang_to_choose_himself')
            $ story_flag('tam_quang_interest_seed')
            $ unlock_character_section("tam", "inner_layer")
            $ unlock_character_section("quang", "core_traits")

            tam melancholic "Anh cũng nên nghĩ cho mình nhiều hơn."

            quang confused "Anh?"

            tam neutral "Vâng."

            "Tâm nhìn túi giấy trong tay anh."

            tam neutral "Anh cứ chuẩn bị mọi thứ cho chị ấy. Nhưng nếu một ngày chị ấy vẫn không quay lại nhìn anh thì sao?"

            "Quang không trả lời."

            "Một lúc lâu sau, anh mới cười."

            quang melancholic "Thì ít nhất mấy thứ đó vẫn có ích."

            tam hurt "Anh đừng nói như vậy."

            "Câu đó bật ra nhanh hơn Tâm nghĩ."

            "Quang nhìn cô."

            "Tâm cũng hơi bất ngờ với chính mình."

            tam embarrassed "Ý em là... nghe không công bằng lắm."

            quang smile "Ừ. Có lẽ vậy."

    "Quang đặt túi giấy vào tay Tâm."

    quang neutral "Nhờ em."

    tam neutral "Dạ."

    "Tâm ôm túi giấy."

    "Nó không nặng."

    "Nhưng lúc quay vào nhà, cô vẫn phải dùng cả hai tay."

    return
