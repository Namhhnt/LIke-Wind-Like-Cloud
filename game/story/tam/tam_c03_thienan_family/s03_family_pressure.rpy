# FILE: game/story/tam/tam_c03_thienan_family/s03_family_pressure.rpy
# Scene file.

label tam_c03_thienan_family_s03_family_pressure:
    scene black
    with fade

    $ story_flag('thienan_family_pressure_introduced')
    $ unlock_character_section("thienan", "core_traits")

    "Ba ngày sau, Thiên An về nhà."

    "Cô mang theo một chiếc vali nhỏ hơn lúc đi, nhưng vẻ mệt mỏi thì nhiều hơn."

    "Bữa cơm tối hôm ấy có đủ người."

    "Mẹ Tâm nấu canh bí, món Thiên An thường ăn được nhiều nhất sau mỗi chuyến công tác."

    "Nhưng tối nay, bát cơm của Thiên An vơi rất chậm."

    tam_mother "Bên đó ổn hơn chưa con?"

    thienan neutral "Tạm ổn rồi ạ."

    tam_father "Tạm ổn nghĩa là vẫn còn vấn đề."

    thienan neutral "Dạ. Nhưng đã kiểm soát được phần lớn."

    tam_father "Ừ."

    "Bố Tâm gật đầu."

    "Ông không khen."

    "Nhưng Tâm biết với bố, chữ 'ừ' ở nhịp này đã gần giống một lời công nhận."

    tam_mother "Con cũng nên giữ sức. Công ty quan trọng, nhưng không thể cứ một mình con chạy qua chạy lại mãi."

    thienan smile "Con biết."

    tam_mother "Biết thì tốt."

    "Mẹ Tâm múc thêm canh vào bát Thiên An."

    "Rồi như thể tiện miệng, bà nói tiếp."

    tam_mother "Quang lần này cũng đi cùng con đúng không?"

    thienan neutral "Dạ."

    tam_mother "Thằng bé vẫn cẩn thận như mọi khi."

    thienan neutral "Anh Quang làm việc rất chắc."

    tam_mother "Mẹ biết."

    "Một khoảng lặng nhỏ rơi xuống bàn ăn."

    "Thiên An đặt đũa xuống, rất nhẹ."

    tam_father "Mẹ con không có ý gì đâu."

    thienan neutral "Con cũng chưa nói gì mà bố."

    tam_mother "Thật ra nếu có thể thì Quang rất tốt."

    "Tâm nhìn lên."

    "Thiên An không đổi sắc mặt."

    "Chỉ có bàn tay đặt bên cạnh bát cơm hơi khựng lại."

    thienan neutral "Mẹ."

    tam_mother "Mẹ biết. Mẹ không ép con với Quang."

    tam_mother "Hai đứa làm việc với nhau bao nhiêu năm rồi. Nếu có gì thì chắc cũng không cần đợi mẹ nhắc."

    "Câu nói ấy đáng lẽ nên làm không khí nhẹ đi."

    "Nhưng không."

    "Nó chỉ khiến sự im lặng trên bàn ăn có hình dạng rõ hơn."

    tam_father "Ý mẹ con là, nếu không phải Quang thì cũng nên nghĩ đến người khác."

    thienan neutral "Con hiện tại không có thời gian nghĩ đến chuyện đó."

    tam_mother "Chính vì lúc nào con cũng nói không có thời gian nên mẹ mới lo."

    thienan tired "Con đang xử lý việc công ty."

    tam_mother "Và sau đó thì sao?"

    "Thiên An không trả lời ngay."

    "Tâm nhìn bát canh trước mặt chị."

    "Một miếng bí bị chiếc thìa cắt lệch, nằm chìm một nửa trong nước."

    "Chị cô rất ít khi làm thứ gì lệch."

    menu:
        "Tâm phản ứng thế nào?"

        "Nhẹ nhàng hỏi mẹ có thể để chị nghỉ tối nay không":
            $ story_add('thienan_self_assertion', 2)
            $ story_add('tam_observation', 1)
            $ story_flag('tam_softly_defended_thienan')
            $ story_flag('tam_supports_thienan')
            $ unlock_character_section("tam", "narrative_function")
            $ unlock_character_section("thienan", "inner_layer")

            tam neutral "Mẹ."

            tam_mother "Sao con?"

            tam melancholic "Chị An mới về. Hay để chị ăn xong đã ạ."

            "Mẹ Tâm khựng lại."

            "Bố Tâm nhìn Tâm một thoáng."

            "Thiên An không nhìn em gái."

            "Nhưng bàn tay cô buông chiếc thìa ra."

            thienan neutral "Không sao."

            tam neutral "Có sao đấy."

            "Tâm nói nhỏ."

            "Nhỏ đến mức gần như chỉ Thiên An nghe được."

            "Thiên An nhìn cô."

            "Lần này, cô không nói 'chị xử lý được'."

        "Im lặng vì sợ làm không khí nặng hơn":
            $ story_add('family_pressure_thienan', 2)
            $ story_add('tam_insecurity', 1)
            $ story_flag('tam_silent_during_thienan_pressure')
            $ unlock_character_section("tam", "inner_layer")

            "Tâm cúi xuống bát cơm."

            "Cô biết mình nên nói gì đó."

            "Nhưng lời vừa lên tới cổ lại bị nuốt xuống."

            "Ở bàn ăn nhà mình, có những lúc im lặng còn dễ hơn cả yêu thương."

            thienan neutral "Con hiểu rồi."

            "Thiên An cầm đũa lên."

            "Miếng bí trong bát vẫn nằm lệch."

        "Đánh trống lảng sang chuyện công việc":
            $ story_add('career_tam', 1)
            $ story_add('tam_observation', 1)
            $ story_add('family_pressure_thienan', 1)
            $ story_flag('tam_deflected_thienan_pressure_with_work')
            $ unlock_character_section("tam", "core_traits")

            tam smile "À, chị An, bên chi nhánh phía Nam có phải dùng hệ thống quản lý khác bên này không ạ?"

            "Câu hỏi hơi vụng."

            "Nhưng đủ để kéo ánh mắt mọi người khỏi chuyện kết hôn."

            thienan confused "Sao em hỏi vậy?"

            tam embarrassed "Em tò mò thôi. Công ty em cũng đang nói về quy trình."

            "Thiên An nhìn Tâm thêm một giây."

            "Rồi cô hiểu."

            thienan neutral "Ừ. Có khác. Và chính vì khác nên mới phiền."

            tam_mother "Hai chị em nhà này đúng là..."

            "Mẹ Tâm lắc đầu, nhưng cuối cùng không nói tiếp chuyện vừa rồi."

    "Bữa cơm kết thúc muộn hơn bình thường."

    "Không ai lớn tiếng."

    "Không ai thật sự giận."

    "Nhưng có những thứ trong nhà không cần vỡ ra mới khiến người ta nghe thấy tiếng nứt."

    return