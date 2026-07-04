# FILE: game/story/tam/tam_c03_thienan_family/s04_private_sisters_talk.rpy
# Scene file.

label tam_c03_thienan_family_s04_private_sisters_talk:
    scene bg_tam_family_balcony_night
    with dissolve

    "Sau bữa tối, Thiên An ra ban công."

    "Tâm đi theo sau vài phút."

    "Không phải vì đã quyết định sẽ nói chuyện gì đó sâu sắc."

    "Chỉ là cô thấy chị cầm theo cốc nước nhưng để quên không uống."

    tam neutral "Chị."

    thienan neutral "Ừ?"

    tam neutral "Nước của chị."

    "Thiên An nhìn xuống tay mình."

    "Cốc nước vẫn đầy."

    thienan smile "À."

    "Cô uống một ngụm nhỏ."

    "Gió đêm thổi qua ban công, kéo một lọn tóc của Thiên An lệch khỏi vai."

    "Cô không vén lại ngay."

    "Điều đó khiến Tâm thấy lạ hơn cả những câu mẹ vừa nói trong bữa cơm."

    tam neutral "Chị có mệt không?"

    thienan neutral "Có."

    "Tâm hơi bất ngờ."

    "Thiên An ít khi trả lời thẳng như vậy."

    thienan neutral "Nhưng mệt không có nghĩa là không làm được."

    tam neutral "Em không hỏi chuyện làm được."

    "Thiên An quay sang."

    thienan neutral "Vậy em hỏi chuyện gì?"

    "Tâm nhìn cốc nước trong tay chị."

    "Trên thành cốc có một vệt nước nhỏ trượt xuống rất chậm."

    menu:
        "Tâm hỏi gì?"

        "Chị có hạnh phúc không?":
            $ story_flag('tam_asked_thienan_happiness')
            $ story_add('thienan_self_assertion', 1)
            $ story_add('tam_observation', 1)

            tam neutral "Chị có hạnh phúc không?"

            "Thiên An im lặng."

            "Không phải kiểu im vì khó chịu."

            "Là kiểu im vì câu hỏi đi thẳng hơn dự kiến."

            thienan neutral "Em học câu đó ở đâu vậy?"

            tam embarrassed "Không học ở đâu cả."

            thienan smile "Nghe giống câu trong phim."

            tam neutral "Vậy chị trả lời như ngoài đời đi."

            "Thiên An nhìn ra ngoài."

            "Đèn đường dưới xa xếp thành những đốm vàng nhỏ."

            thienan neutral "Chị không bất hạnh."

            tam neutral "Đó không phải câu trả lời."

            thienan neutral "Với người lớn, đôi khi đó đã là một câu trả lời khá tốt rồi."

            tam sad "Nghe không tốt lắm."

            "Thiên An bật cười khẽ."

            thienan neutral "Ừ. Chắc là không."

        "Chị có từng thích ai thật lòng chưa?":
            $ story_add('thienan_minh_residue', 1)
            $ story_flag('tam_heard_minh_hint')
            $ story_flag('tam_asked_thienan_past_love')

            tam neutral "Chị có từng thích ai thật lòng chưa?"

            "Thiên An không quay lại ngay."

            "Gió đêm làm mặt nước trong cốc khẽ rung."

            thienan neutral "Sao tự nhiên hỏi vậy?"

            tam neutral "Không tự nhiên lắm. Mẹ vừa nhắc chuyện kết hôn mà."

            thienan neutral "Vậy đáng lẽ em nên hỏi chị có muốn kết hôn không."

            tam neutral "Câu đó dễ né hơn."

            "Thiên An nhìn Tâm."

            "Một lúc sau, cô cười."

            thienan smile "Em lớn hơn chị nghĩ rồi đấy."

            tam embarrassed "Đừng nói như em mới học xong cấp hai."

            thienan neutral "Từng có."

            "Tâm khựng lại."

            tam surprised "Thật ạ?"

            thienan neutral "Ừ."

            tam neutral "Người đó..."

            thienan neutral "Qua rồi."

            "Thiên An nói rất nhẹ."

            "Nhẹ đến mức nếu Tâm không đứng gần, có lẽ cô sẽ tưởng đó là tiếng gió."

            tam neutral "Vậy sao chị vẫn nhớ?"

            "Thiên An nhìn cốc nước."

            thienan neutral "Có những chuyện qua rồi nhưng không biến mất. Chỉ là mình không sống dựa vào nó nữa."

            "Tâm không hỏi tiếp."

            "Cô bỗng cảm thấy cái tên mình chưa được nghe cũng có trọng lượng."

        "Chị thấy anh Quang thế nào?":
            $ story_add('thienan_quang_trust', 1)
            $ story_flag('tam_asked_about_quang')
            $ story_flag('quang_an_route_seed')

            tam neutral "Chị thấy anh Quang thế nào?"

            thienan neutral "Là sao?"

            tam neutral "Thì... anh ấy làm với chị lâu như vậy."

            thienan neutral "Anh Quang rất đáng tin."

            tam neutral "Chỉ vậy thôi ạ?"

            thienan neutral "Với công việc, đó là đánh giá rất cao."

            tam neutral "Còn ngoài công việc?"

            "Thiên An nhìn Tâm."

            "Tâm hơi rụt cổ."

            tam embarrassed "Em hỏi hơi nhiều à?"

            thienan neutral "Hơi."

            tam neutral "Vậy chị có thể trả lời hơi ít cũng được."

            "Khóe môi Thiên An nhích lên rất nhẹ."

            thienan neutral "Anh ấy là người tốt."

            tam neutral "Câu đó nghe nguy hiểm lắm."

            thienan confused "Nguy hiểm?"

            tam teasing "Thường trong chuyện tình cảm, ai bị gọi là người tốt thì hơi đáng lo."

            "Thiên An bật cười."

            "Lần này là cười thật."

            thienan smile "Em đọc linh tinh ít thôi."

            tam smile "Nhưng em nói đúng không?"

            "Thiên An không trả lời."

            "Cô uống thêm một ngụm nước."

            "Cốc nước lần này vơi đi thật."

        "Không hỏi gì, chỉ đứng cạnh chị":
            $ story_add('thienan_quang_trust', 1)
            $ story_add('tam_observation', 1)
            $ story_flag('tam_sat_with_thienan_silently')

            "Tâm không hỏi nữa."

            "Cô chỉ đứng cạnh Thiên An, cùng nhìn xuống khoảng sân tối dưới nhà."

            "Hai chị em im lặng một lúc lâu."

            "Cái im lặng ấy không thoải mái hẳn."

            "Nhưng cũng không khó chịu."

            "Thiên An uống nước."

            "Tâm tựa tay lên lan can."

            "Một lúc sau, Thiên An kéo nhẹ tay cô ra khỏi mép sắt lạnh."

            thienan neutral "Lạnh."

            tam neutral "À."

            "Tâm rút tay lại."

            "Cô không nói cảm ơn."

            "Thiên An cũng không cần."

    thienan neutral "Tâm."

    tam neutral "Vâng?"

    thienan neutral "Chuyện của chị, em không cần gánh."

    tam neutral "Em biết."

    thienan neutral "Biết thật không?"

    tam smile "Không chắc."

    "Thiên An nhìn cô."

    "Rồi cô thở ra rất nhẹ."

    thienan neutral "Vậy ít nhất đừng gánh một mình."

    "Tâm chớp mắt."

    "Câu đó vốn nên là câu em gái nói với chị."

    "Nhưng Thiên An nói trước."

    "Đúng là chị cô."

    "Có mệt đến đâu cũng phải thắng trước nửa câu."

    return