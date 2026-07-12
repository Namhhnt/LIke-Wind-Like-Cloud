# FILE: game/story/hoang/hoang_h01_brother_house/s02_minh_remote_presence.rpy
# Hoàng POV — three months after the route-development chapter.
# Uses the route resolved in s01 and lets Hoàng ask Minh for advice.

label hoang_h01_brother_house_s02_minh_remote_presence:
    scene black
    with fade

    $ _hoang_self = story_state.get("hoang_self_acceptance", 0)
    $ _hoang_insecurity = story_state.get("hoang_insecurity", 0)
    $ _anniversary_route = story_state.get(
        "hoang_anniversary_route",
        "friend_group"
    )

    "Căn nhà yên đến mức Hoàng nghe rõ tiếng đồng hồ đổi phút."

    "Trên bàn trước mặt cậu là một cốc nước đã nguội, chiếc điện thoại và ba cửa sổ trình duyệt mở dở."

    "Một trang bán trang sức."

    "Một trang thiết bị chụp ảnh."

    "Trang còn lại là danh sách những nơi mở cửa vào Chủ Nhật."

    "Hoàng nhìn qua cả ba."

    "Rồi úp điện thoại xuống."

    "Nửa phút sau, cậu lại cầm lên."

    hoang irritated "Có mỗi chuyện chọn quà thôi mà."

    "Cậu nói với căn phòng."

    "Căn phòng không thấy có nghĩa vụ phải trả lời."

    "Hoàng kéo danh bạ xuống, dừng ở một cái tên."

    "Ngón tay đặt trên nút gọi lâu hơn bình thường."

    if _hoang_self < 35:
        "Cậu đã định tắt màn hình."

        "Đúng lúc đó, đồng hồ trên tường lại nhích thêm một phút."

        hoang neutral "Thôi được."

    "Cuộc gọi đổ chuông bốn lần."

    minh neutral "Nói đi."

    hoang irritated "Anh nghe máy như trực tổng đài thế?"

    minh neutral "Em gọi vào giờ này. Chắc không phải để chúc ngủ ngon."

    hoang neutral "Em hỏi chuyện này."

    minh neutral "Ừ."

    hoang neutral "Tặng quà cho một người thì nên tặng gì?"

    "Đầu dây bên kia im hai giây."

    minh neutral "Người nào?"

    hoang irritated "Anh cứ trả lời chung trước được không?"

    minh neutral "Không."

    hoang confused "Tại sao?"

    minh neutral "Vì quà chung chung thường chỉ phù hợp với người mình không hiểu rõ."

    "Hoàng dựa lưng vào sofa."

    hoang neutral "Đúng là gọi anh để tự làm khó mình."

    if story_state["hoang_anniversary_route"] == "tam":
        call hoang_h01_brother_house_s02_call_minh_tam

    elif story_state["hoang_anniversary_route"] == "huyen":
        call hoang_h01_brother_house_s02_call_minh_huyen

    else:
        call hoang_h01_brother_house_s02_call_minh_friend_group

    return


label hoang_h01_brother_house_s02_call_minh_tam:
    hoang neutral "Tâm."

    minh neutral "Dịp gì?"

    hoang neutral "Chủ Nhật này tròn một năm từ hôm bọn em gặp nhau."

    minh neutral "Một năm quen nhau hay một năm yêu nhau?"

    hoang confused "Khác nhau à?"

    minh neutral "Em đang mua quà cho dịp nào?"

    "Hoàng im."

    "Câu hỏi nghe không khó."

    "Có điều cậu chưa từng nghĩ phải tách hai việc ấy ra."

    hoang neutral "Ngày quen nhau."

    hoang smile "Còn chuyện sau đó thì... tiện thể tính luôn."

    minh neutral "Tâm biết em nhớ ngày này không?"

    hoang neutral "Chưa."

    minh neutral "Thế em nhớ cô ấy thích gì?"

    hoang neutral "Cô ấy không thích thứ quá nổi."

    hoang neutral "Trang sức thì chỉ đeo loại nhỏ. Đi làm cũng không thay nhiều."

    minh neutral "Màu gì?"

    hoang neutral "Vàng nhạt. Hoặc trắng."

    minh neutral "Em hỏi anh làm gì nữa?"

    hoang irritated "Để xác nhận là em không chọn sai."

    minh neutral "Anh chưa nhìn thấy món em định mua."

    hoang neutral "Có một đôi bông tai hoàng ngọc."

    hoang neutral "Đá nhỏ. Viền trắng. Không quá cầu kỳ."

    minh neutral "Cô ấy từng nhìn nó à?"

    hoang neutral "Không đúng đôi đó."

    hoang neutral "Nhưng có lần đi ngang một cửa hàng, cô ấy đứng lại trước một đôi gần giống."

    minh neutral "Bao lâu?"

    hoang confused "Gì?"

    minh neutral "Cô ấy nhìn bao lâu?"

    hoang neutral "Chắc... năm, sáu giây."

    minh neutral "Nhìn đôi bông tai hay nhìn giá?"

    "Hoàng khựng lại."

    hoang neutral "Cả hai."

    minh neutral "Vậy đừng mua loại khiến cô ấy phải lo xem nên nhận hay nên trả."

    if story_state.get("hoang_self_acceptance", 0) >= 55:
        hoang smile "Em cũng nghĩ thế."

        minh neutral "Không. Em đã nghĩ đến loại đắt hơn."

        hoang surprised "Sao anh biết?"

        minh neutral "Nếu không thì em đã mua rồi, không gọi anh."

        "Hoàng nhìn sang cửa sổ trình duyệt đầu tiên."

        "Món đang mở không phải đôi nhỏ cậu vừa miêu tả."

        "Viên đá lớn hơn."

        "Giá cũng lớn hơn khá nhiều."

        hoang irritated "Thỉnh thoảng anh có thể giả vờ không biết được không?"

        minh neutral "Không cần thiết."

        $ story_state["hoang_gift_recommendation"] = "tam_topaz_earrings"
        $ story_flag("hoang_understands_tam_gift")

    elif story_state.get("hoang_self_acceptance", 0) >= 35:
        minh neutral "Em đang muốn tặng cô ấy một món quà."

        minh neutral "Hay muốn chứng minh em làm được một buổi hẹn đủ đặc biệt?"

        hoang neutral "Có gì khác nhau?"

        minh neutral "Một cái nghĩ về người nhận."

        minh neutral "Cái còn lại nghĩ về việc em trông thế nào trong mắt cô ấy."

        "Hoàng đưa tay kéo cổ áo."

        "Cậu không mặc áo sơ-mi."

        "Động tác ấy vì thế hơi thừa."

        menu:
            "Hoàng trả lời..."

            "“Em muốn cô ấy dùng được.”":
                hoang neutral "Em muốn cô ấy dùng được."

                minh neutral "Vậy chọn đôi nhỏ."

                hoang neutral "Ừ."

                $ story_add("hoang_self_acceptance", 5)
                $ story_add("hoang_insecurity", -5)
                $ story_state["hoang_gift_recommendation"] = "tam_topaz_earrings"
                $ story_flag("hoang_chose_tam_over_performance")

            "“Em chỉ không muốn làm sơ sài.”":
                hoang neutral "Em chỉ không muốn làm sơ sài."

                minh neutral "Đắt không đồng nghĩa với kỹ."

                hoang irritated "Anh nói câu đó nghe hơi thuận miệng nhỉ."

                minh neutral "Vì nó đúng."

                $ story_add("hoang_insecurity", 5)
                $ story_state["hoang_gift_recommendation"] = "tam_expensive_topaz"
                $ story_flag("hoang_overcompensates_tam_gift")

            "“Hay để dịp khác.”":
                hoang neutral "Hay để dịp khác."

                minh neutral "Em đang sợ cô ấy không thích món quà..."

                minh neutral "Hay sợ cô ấy hiểu món quà có ý nghĩa gì?"

                "Hoàng không trả lời."

                $ story_add("hoang_self_acceptance", -5)
                $ story_add("hoang_insecurity", 5)
                $ story_state["hoang_gift_recommendation"] = "tam_no_gift_yet"
                $ story_flag("hoang_avoids_anniversary_gift")

    else:
        hoang neutral "Hay anh chọn hộ em đi."

        minh neutral "Không."

        hoang irritated "Anh từ chối nhanh thế?"

        minh neutral "Vì em không hỏi anh cô ấy thích gì."

        minh neutral "Em đang hỏi anh em nên trở thành người thế nào khi đứng trước cô ấy."

        hoang neutral "..."

        minh neutral "Cái đó anh chọn hộ thì không còn là em nữa."

        "Hoàng nhìn lại ba cửa sổ đang mở."

        "Món nào cũng đẹp."

        "Không món nào khiến cậu thấy chắc tay."

        menu:
            "Hoàng..."

            "Đóng trang món đắt nhất":
                "Hoàng nhấn dấu đóng ở cửa sổ đầu tiên."

                hoang neutral "Đôi nhỏ."

                minh neutral "Ừ."

                hoang confused "Anh không định khen em tiến bộ à?"

                minh neutral "Em vừa đóng một cửa sổ trình duyệt."

                minh neutral "Đừng làm quá."

                $ story_add("hoang_self_acceptance", 5)
                $ story_add("hoang_insecurity", -5)
                $ story_state["hoang_gift_recommendation"] = "tam_topaz_earrings"
                $ story_flag("hoang_fragile_but_honest_tam")

            "Giữ món đắt hơn":
                hoang neutral "Em vẫn nghĩ loại tốt hơn sẽ hợp."

                minh neutral "Tùy em."

                "Giọng Minh không phản đối."

                "Chính vì thế, Hoàng càng biết anh không đồng ý."

                $ story_add("hoang_insecurity", 10)
                $ story_state["hoang_gift_recommendation"] = "tam_expensive_topaz"
                $ story_flag("hoang_uses_gift_to_prove_himself")

            "Không mua gì":
                hoang neutral "Thôi."

                hoang neutral "Em sẽ đưa cô ấy đi chơi trước."

                minh neutral "Cũng được."

                minh neutral "Miễn là em không giả vờ quên ngày này chỉ vì chưa chọn được quà."

                $ story_state["hoang_gift_recommendation"] = "tam_no_gift_yet"
                $ story_flag("hoang_tam_anniversary_without_gift")

    minh neutral "Còn một việc."

    hoang neutral "Gì?"

    minh neutral "Đừng nhờ nhân viên cửa hàng viết lời nhắn hộ."

    hoang irritated "Em chưa tệ đến thế."

    minh neutral "Anh đang phòng xa."

    return


label hoang_h01_brother_house_s02_call_minh_huyen:
    hoang neutral "Huyền."

    "Lần này, đầu dây bên kia im lâu hơn."

    minh neutral "Anh tưởng lúc đầu em để ý Tâm."

    hoang neutral "Đúng."

    hoang neutral "Lúc đầu là Tâm."

    "Hoàng xoay cốc nước một vòng trên mặt bàn."

    hoang neutral "Tâm khiến người ta để ý ngay."

    hoang neutral "Cô ấy nhẹ. Dễ nói chuyện. Ở cạnh cũng không phải đề phòng gì."

    minh neutral "Còn Huyền?"

    hoang irritated "Ồn."

    minh neutral "Anh hỏi nghiêm túc."

    hoang neutral "Em cũng đang nói nghiêm túc."

    "Hoàng cười khẽ."

    hoang neutral "Ban đầu em chỉ thấy cô ấy ồn."

    hoang neutral "Sau đó lại thành quen."

    hoang neutral "Cô ấy cứ chen vào câu chuyện, giật điện thoại của em, tự đổi nhạc trên xe."

    hoang neutral "Đi ăn thì bảo không đói, xong gắp gần hết phần của người khác."

    minh neutral "Nghe có vẻ nhiều khuyết điểm."

    hoang neutral "Ừ."

    "Hoàng dừng một nhịp."

    hoang neutral "Nhưng những hôm cô ấy im thì em lại nhận ra trước."

    "Ở đầu dây bên kia không có tiếng động."

    "Minh không thúc."

    hoang neutral "Chắc là từ lúc đó."

    minh neutral "Em nghiêng về Huyền vì thích cô ấy..."

    minh neutral "Hay vì Tâm không nghiêng về em đủ nhiều?"

    "Câu hỏi rơi xuống rất gọn."

    "Không nặng."

    "Nhưng đúng chỗ."

    if story_state.get("hoang_self_acceptance", 0) >= 55:
        hoang neutral "Nếu chỉ vì Tâm, em đã không gọi anh để hỏi quà cho Huyền."

        minh neutral "Chưa chắc."

        hoang irritated "Anh có thể để em nói một câu nghe được một lần không?"

        minh neutral "Nói tiếp đi."

        hoang neutral "Em không biết Huyền sẽ đi với em đến đâu."

        hoang neutral "Nhưng em biết lúc cô ấy không có ở đó, em vẫn tìm."

        minh neutral "Vậy được."

        hoang confused "Được là sao?"

        minh neutral "Ít nhất em đang chọn một người."

        minh neutral "Không phải chọn cảm giác được một người chọn."

        $ story_add("hoang_self_acceptance", 5)
        $ story_flag("hoang_names_huyen_feelings_clearly")

    elif story_state.get("hoang_self_acceptance", 0) >= 35:
        minh neutral "Anh hỏi cách khác."

        minh neutral "Nếu tối nay Tâm gọi và nói cô ấy muốn bắt đầu lại..."

        minh neutral "Em có đổi món quà không?"

        "Hoàng nhìn màn hình điện thoại."

        "Tên Tâm nằm trong nhóm trò chuyện gần nhất."

        "Tên Huyền nằm ngay phía trên."

        menu:
            "Hoàng nghĩ rằng..."

            "“Không.”":
                hoang neutral "Không."

                minh neutral "Em trả lời hơi nhanh."

                hoang neutral "Vì em đã nghĩ chậm đủ lâu rồi."

                "Minh không nói gì thêm."

                "Lần này, sự im lặng nghe giống một cái gật đầu."

                $ story_add("hoang_self_acceptance", 5)
                $ story_add("hoang_insecurity", -5)
                $ story_flag("hoang_chooses_huyen_without_comparison")

            "“Em không biết.”":
                hoang neutral "Em không biết."

                minh neutral "Vậy đừng tặng Huyền một món quà khiến cô ấy tưởng em đã biết."

                "Hoàng cúi mắt."

                "Cậu không thích câu đó."

                "Có điều không tìm được chỗ nào để phản đối."

                $ story_add("hoang_insecurity", 5)
                $ story_add("hoang_self_acceptance", -5)
                $ story_state["hoang_anniversary_route"] = "friend_group"
                $ story_flag("hoang_huyen_not_ready_to_commit")

                call hoang_h01_brother_house_s02_shift_to_friend_group

                return

            "“Tâm sẽ không gọi.”":
                hoang neutral "Tâm sẽ không gọi."

                minh neutral "Anh không hỏi Tâm có gọi không."

                minh neutral "Anh hỏi em sẽ làm gì."

                "Hoàng dựa đầu ra sau ghế."

                "Trần nhà không giúp cậu né câu hỏi."

                $ story_add("hoang_insecurity", 5)
                $ story_flag("hoang_answers_about_tam_not_huyen")

                menu:
                    "Nghĩ thêm một lúc..."

                    "Vẫn chọn Huyền":
                        hoang neutral "Không đổi."

                        hoang neutral "Dù Tâm có gọi."

                        minh neutral "Ừ."

                        $ story_add("hoang_self_acceptance", 5)
                        $ story_flag("hoang_reaches_huyen_answer_late")

                    "Không thể trả lời chắc":
                        hoang neutral "Em chưa trả lời chắc được."

                        minh neutral "Vậy giữ mọi chuyện nhẹ thôi."

                        $ story_state["hoang_anniversary_route"] = "friend_group"
                        $ story_flag("hoang_steps_back_before_hurting_huyen")

                        call hoang_h01_brother_house_s02_shift_to_friend_group

                        return

    else:
        minh neutral "Nếu Tâm đồng ý với em từ đầu, em còn nhìn Huyền như bây giờ không?"

        "Hoàng mở miệng."

        "Rồi lại thôi."

        "Một câu trả lời quá nhanh sẽ là nói dối."

        "Một khoảng im lặng quá lâu cũng đã gần thành câu trả lời."

        menu:
            "Hoàng..."

            "Thừa nhận mình chưa chắc":
                hoang neutral "Em chưa chắc."

                minh neutral "Vậy đừng kéo cô ấy vào chỗ em còn chưa đứng vững."

                "Hoàng nhìn sang khung trò chuyện của ba người."

                "Tin nhắn cuối cùng là một tấm ảnh Huyền gửi."

                "Tâm đang nhắm mắt."

                "Hoàng nhìn lệch khỏi máy."

                "Còn Huyền cười đến mức ảnh bị rung."

                hoang neutral "Chủ Nhật vẫn gặp cả ba."

                minh neutral "Ừ."

                $ story_add("hoang_self_acceptance", 5)
                $ story_state["hoang_anniversary_route"] = "friend_group"
                $ story_flag("hoang_protects_huyen_from_uncertainty")

                call hoang_h01_brother_house_s02_shift_to_friend_group

                return

            "Khẳng định mình chọn Huyền":
                hoang neutral "Có."

                minh neutral "Có gì?"

                hoang neutral "Em vẫn sẽ nhìn cô ấy."

                hoang neutral "Có thể muộn hơn."

                hoang neutral "Nhưng vẫn sẽ nhìn."

                "Minh im một lúc."

                minh neutral "Thế thì nhớ câu đó."

                minh neutral "Đừng để sau này chính em biến Huyền thành lựa chọn thứ hai."

                $ story_add("hoang_self_acceptance", 5)
                $ story_add("hoang_insecurity", 5)
                $ story_flag("hoang_huyen_choice_under_pressure")

    minh neutral "Cô ấy thích gì?"

    hoang neutral "Chụp ảnh."

    minh neutral "Anh nhớ Huyền không phải nhiếp ảnh gia."

    hoang neutral "Không phải kiểu đó."

    hoang neutral "Thấy ánh sáng đẹp là giật điện thoại của người khác."

    hoang neutral "Chụp xong để cả trăm tấm trong máy em mà không gửi."

    minh neutral "Có ảnh của cô ấy không?"

    hoang neutral "Ít."

    minh neutral "Vậy đừng mua thứ chỉ để cô ấy tiếp tục đứng sau máy."

    "Hoàng nhìn sang cửa sổ trình duyệt thứ hai."

    "Một chiếc máy in ảnh bỏ túi nằm trong giỏ hàng."

    "Bên cạnh là cuốn album nhỏ, bìa trơn."

    hoang neutral "Máy in ảnh mini thì sao?"

    minh neutral "Được."

    hoang surprised "Nhanh thế?"

    minh neutral "Vì em đã chọn trước khi gọi."

    hoang smile "Em chỉ cần người xác nhận."

    minh neutral "Không."

    minh neutral "Em cần người bắt em nói ra vì sao."

    $ story_state["hoang_gift_recommendation"] = "huyen_pocket_photo_printer"
    $ story_flag("hoang_gift_puts_huyen_in_frame")

    return


label hoang_h01_brother_house_s02_call_minh_friend_group:
    hoang neutral "Không phải một người."

    minh neutral "Hai?"

    hoang neutral "Tâm với Huyền."

    minh neutral "Em định làm gì?"

    hoang neutral "Mua mỗi người một món."

    minh neutral "Giống nhau?"

    hoang neutral "Chắc vậy."

    minh neutral "Quà công ty."

    hoang irritated "Thế mua khác nhau."

    minh neutral "Rồi em sẽ phải giải thích vì sao khác."

    hoang neutral "Anh có đề xuất nào không mang tính phá hoại không?"

    minh neutral "Đừng mua."

    hoang irritated "Cảm ơn. Hữu ích thật."

    minh neutral "Tặng họ một ngày."

    "Hoàng ngừng xoay cốc nước."

    minh neutral "Ba người quen nhau cùng một lúc."

    minh neutral "Nếu sau một năm vẫn còn ở cạnh nhau, thứ đáng giữ là chuyện đó."

    hoang neutral "Anh nói nghe như bọn em sắp giải tán."

    minh neutral "Vậy càng không cần quà chia tay."

    hoang smile "..."

    hoang neutral "Em đặt một chỗ ăn."

    minh neutral "Ừ."

    hoang neutral "Rồi đi đâu đó sau."

    minh neutral "Ừ."

    hoang neutral "In một tấm ảnh ba người."

    minh neutral "Nếu có tấm nào cả ba đều mở mắt."

    hoang irritated "Anh không cần hạ thấp tiêu chuẩn đến thế."

    $ story_state["hoang_gift_recommendation"] = "friend_group_shared_day"
    $ story_flag("hoang_chooses_shared_anniversary_memory")
    $ story_add("hoang_self_acceptance", 5)

    return


label hoang_h01_brother_house_s02_shift_to_friend_group:
    hoang neutral "Nếu đi cả ba thì sao?"

    minh neutral "Thì em không cần giả vờ một câu trả lời chưa có."

    hoang neutral "Nghe hơi hèn."

    minh neutral "Không."

    minh neutral "Hèn là biết mình chưa rõ nhưng vẫn để người khác đặt cược."

    "Hoàng nhìn ba cửa sổ trình duyệt."

    "Cậu đóng trang trang sức trước."

    "Sau đó đóng cả trang quà cá nhân."

    "Chỉ giữ lại danh sách địa điểm mở cửa vào Chủ Nhật."

    $ story_state["hoang_gift_recommendation"] = "friend_group_shared_day"
    $ story_flag("hoang_anniversary_route_soft_reset")

    return
