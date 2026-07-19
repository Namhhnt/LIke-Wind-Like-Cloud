# FILE: game/story/prologue/prologue_rain_dream/s01_rain_meeting.rpy
# Scene file.

label prologue_rain_dream_s01_rain_meeting:
    scene black
    with fade

    centered "{size=46}PROLOGUE{/size}\n{size=30}Giấc mơ trong mưa{/size}"

    scene black
    with dissolve

    "Mưa rơi rất nhẹ."

    "Không phải kiểu mưa đủ lớn để người ta phải chạy đi tìm chỗ trú."
    "Chỉ là một lớp nước mỏng phủ lên mặt đường, làm ánh đèn bên kia phố nhòe ra thành những vệt dài và lạnh."

    "Tâm đứng dưới mái hiên của một cửa hàng đã đóng cửa."
    "Trong tay cô là một chiếc ô màu xám. Nan ô hơi lệch, mép vải đọng nước thành từng giọt nhỏ."

    "Cô không nhớ mình đến đây bằng cách nào."
    "Cũng không nhớ mình đang chờ ai."

    "Chỉ nhớ là mình đã đứng rất lâu."

    "Một bóng người đi qua màn mưa."

    "Anh ta cao, vai hơi gầy, dáng đi bình tĩnh đến lạ. Không vội. Không nhìn quanh. Như thể con đường ướt lạnh này đã quen thuộc với anh từ lâu."

    "Tâm khẽ siết cán ô."

    tam confused "..."

    "Người đàn ông dừng lại trước mặt cô."
    "Gương mặt anh bị bóng tối và nước mưa làm nhòe đi. Tâm càng cố nhìn rõ, mọi đường nét lại càng tan ra."

    "Nhưng cảm giác ấy thì rất rõ."

    "Rất quen."

    "Quen đến mức vô lý."

    "Anh nhìn chiếc ô trong tay cô, rồi nhìn xuống vai áo đã ướt một mảng của cô."
    "Một lúc sau, anh khẽ thở ra."

    minh_unknown "\"Em cứ đứng như vậy thì cảm mất.\""

    tam surprised "..."

    "Giọng nói đó thấp, khô, nhưng không lạnh."
    "Tâm cảm thấy trong ngực mình có thứ gì đó khựng lại một nhịp."

    tam smile "Em... không sao."

    "Người kia không trả lời ngay."

    "Anh chỉ đưa tay, chỉnh lại nan ô bị lệch cho cô."
    "Đầu ngón tay anh chạm rất nhẹ vào cán ô. Một cái chạm gần như không đáng kể."

    "Nhưng Tâm lại thấy lòng bàn tay mình nóng lên."

    minh_unknown "\"Muộn rồi.\""

    "Anh nói."

    minh_unknown "\"Tôi đưa em về.\""

    "Tâm muốn hỏi về đâu."
    "Muốn hỏi anh là ai."
    "Muốn hỏi tại sao chỉ một câu bình thường như vậy lại khiến cô thấy khó thở."

    "Nhưng cổ họng cô khô lại."

    "Mưa rơi dày hơn."

    "Bóng người trước mặt mờ dần."

    tam shocked "Khoan đã..."

    "Tâm bước lên một bước."
    "Nước mưa bắn nhẹ dưới chân."

    "Người kia quay đầu lại."

    "Trong khoảnh khắc rất ngắn, cô tưởng mình đã nhìn thấy gương mặt anh."

    "Rồi tiếng mưa phủ xuống tất cả."

    menu:
        "Điều gì còn đọng lại sau giấc mơ?"

        "Gương mặt của người đàn ông ấy":
            $ story_add('tam_minh_drawn', 1)
            $ story_add('tam_hoang_interest', 1)
            $ story_flag('dream_remembered_face')

            "Tâm cố níu lại đường nét cuối cùng còn sót trong trí nhớ."
            "Sống mũi. Ánh mắt. Khóe môi hình như từng hơi nhếch lên."
            "Càng cố nhớ, cô càng thấy tim mình đập nhanh hơn."

        "Tiếng mưa":
            $ story_add('tam_self_clarity', 1)
            $ story_flag('dream_remembered_rain')

            "Thứ rõ nhất không phải là người đó."
            "Mà là tiếng mưa rơi trên mép ô."
            "Đều đều. Nhẫn nại. Như một điều gì đó đã chờ cô rất lâu."

        "Không có gì rõ ràng":
            $ story_add('doom_score', 1)
            $ story_flag('dream_ignored')

            "Tất cả vỡ ra rất nhanh."
            "Chỉ còn lại một khoảng trống mờ, lạnh, và cảm giác mình vừa bỏ lỡ điều gì đó quan trọng."

    return
