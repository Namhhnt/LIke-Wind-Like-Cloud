# FILE: game/story/hoang/hoang_h01_brother_house/s04_send_invitation.rpy
# Hoàng sends the invitation after choosing the gift/plan.
# Low self-acceptance changes how directly he communicates, but does not
# fabricate a new romance route at the last moment.

label hoang_h01_brother_house_s04_send_invitation:
    scene black

    $ _anniversary_route = story_state.get(
        "hoang_anniversary_route",
        "friend_group"
    )
    $ _hoang_self = story_state.get("hoang_self_acceptance", 0)

    "Mọi thứ cần chuẩn bị đã nằm trước mặt Hoàng."

    "Hoặc trong giỏ hàng."

    "Hoặc trong một đoạn tin nhắn chưa gửi."

    if _anniversary_route == "tam":
        call hoang_h01_brother_house_s04_invite_tam

    elif _anniversary_route == "huyen":
        call hoang_h01_brother_house_s04_invite_huyen

    else:
        call hoang_h01_brother_house_s04_invite_friend_group

    return


label hoang_h01_brother_house_s04_invite_tam:
    "Khung trò chuyện với Tâm mở sẵn."

    if story_state.get("hoang_self_acceptance", 0) >= 55:
        "Hoàng gõ một dòng."

        hoang "Chủ Nhật để anh đón. Đừng lên kế hoạch gì."

        "Cậu đọc lại."

        "Không sửa."

        "Tin nhắn được gửi đi."

        "Tâm trả lời chưa đầy một phút sau."

        tam "Mấy giờ?"

        hoang "Bảy rưỡi."

        tam "Sớm thế?"

        hoang "Anh mời em ăn sáng."

        tam "Vậy cho em tám giờ."

        hoang "Bảy rưỡi."

        tam "Bảy giờ bốn mươi lăm."

        "Hoàng nhìn con số một lúc."

        hoang smile "Được."

        $ story_flag("hoang_invitation_tam_direct")
        $ story_add("hoang_tam_trust", 5)

    elif story_state.get("hoang_self_acceptance", 0) >= 35:
        menu:
            "Hoàng nhắn..."

            "“Chủ Nhật để anh đón. Đừng lên kế hoạch gì.”":
                hoang "Chủ Nhật để anh đón. Đừng lên kế hoạch gì."

                "Câu chữ trông quyết đoán hơn cảm giác trong lòng cậu."

                "Hoàng vẫn nhấn gửi."

                tam "Vâng."

                tam "Nhưng ít nhất cũng phải cho em biết nên mặc gì chứ?"

                hoang "Thứ em thấy thoải mái."

                tam "Câu trả lời nguy hiểm thật đấy."

                $ story_flag("hoang_invitation_tam_direct")
                $ story_add("hoang_self_acceptance", 5)
                $ story_add("hoang_tam_trust", 5)

            "“Chủ Nhật em rảnh không? Anh có chỗ muốn đưa em đến.”":
                hoang "Chủ Nhật em rảnh không? Anh có chỗ muốn đưa em đến."

                "Hoàng gửi xong mới nhận ra mình đã biết rõ lịch của Tâm."

                "Cậu vẫn chờ."

                tam "Em rảnh."

                tam "Anh đang hỏi thật hay chỉ xác nhận?"

                hoang "Xác nhận cho lịch sự."

                tam "Thế thì em lịch sự đồng ý."

                $ story_flag("hoang_invitation_tam_gentle")
                $ story_add("hoang_tam_trust", 5)

            "Viết rõ toàn bộ kế hoạch":
                "Hoàng gõ giờ đón."

                "Địa điểm ăn sáng."

                "Khoảng thời gian dự kiến ở công viên."

                "Cả phương án dự phòng nếu trời mưa."

                "Tin nhắn dài gần bằng một lịch công tác."

                "Cậu nhìn nó."

                "Rồi xóa bớt một nửa."

                hoang "Chủ Nhật em rảnh không? Anh đã đặt chỗ ăn sáng."

                tam "Anh đang hồi hộp à?"

                "Ngón tay Hoàng dừng trên màn hình."

                hoang "Không."

                tam "Vâng. Em sẽ giả vờ tin."

                $ story_flag("hoang_invitation_tam_overplanned")
                $ story_add("hoang_insecurity", 5)

    else:
        "Hoàng viết ba phiên bản."

        "Bản đầu nghe như một lời mời công việc."

        "Bản thứ hai giải thích quá nhiều."

        "Bản cuối cùng chỉ còn sáu chữ."

        hoang "Chủ Nhật này em rảnh không?"

        "Cậu nhấn gửi trước khi kịp xóa lần nữa."

        "Ba dấu chấm hiện lên."

        "Biến mất."

        "Rồi hiện lại."

        tam "Có."

        tam "Anh muốn gặp em à?"

        "Một câu hỏi rất thẳng."

        "Hoàng nhìn lâu đến mức màn hình tự tối."

        menu:
            "Hoàng trả lời..."

            "“Ừ. Anh muốn gặp em.”":
                hoang "Ừ. Anh muốn gặp em."

                "Câu trả lời không làm căn phòng thay đổi."

                "Chỉ khiến vai cậu bớt căng đi một chút."

                tam "Vậy Chủ Nhật gặp."

                $ story_flag("hoang_invitation_tam_fragile_honest")
                $ story_add("hoang_self_acceptance", 5)
                $ story_add("hoang_insecurity", -5)

            "“Anh có chuyện muốn đưa em đi xem.”":
                hoang "Anh có chỗ muốn đưa em đến."

                tam "Được."

                "Tâm không hỏi thêm."

                "Sự dịu dàng đó khiến Hoàng thấy nhẹ đi."

                "Cũng khiến cậu biết mình vừa né."

                $ story_flag("hoang_invitation_tam_avoids_direct_answer")
                $ story_add("hoang_insecurity", 5)

            "Trêu để lảng đi":
                hoang "Không. Anh đang làm khảo sát lịch rảnh."

                tam "Thế à."

                tam "Vậy kết quả khảo sát là em rảnh."

                tam "Còn anh có muốn gặp hay không thì tự điền."

                "Hoàng thở ra qua mũi."

                hoang "Có."

                tam "Em biết rồi."

                $ story_flag("hoang_invitation_tam_teasing_recovery")
                $ story_add("hoang_self_acceptance", 5)

    return


label hoang_h01_brother_house_s04_invite_huyen:
    "Hoàng mở khung trò chuyện với Huyền."

    "Tin nhắn cuối cùng của cô là ảnh một biển hiệu viết sai chính tả."

    if story_state.get("hoang_self_acceptance", 0) >= 55:
        hoang "Chủ Nhật đi với anh."

        "Phản hồi đến gần như ngay lập tức."

        huyen "Đi đâu?"

        hoang "Chưa nói."

        huyen "Bắt cóc à?"

        hoang "Cô có thể từ chối."

        "Ba dấu chấm chạy một lúc."

        huyen "Ai bảo tôi từ chối?"

        huyen "Nhưng đồ ăn phải ngon."

        hoang "Biết rồi."

        huyen "Và không được bắt tôi dậy lúc sáu giờ."

        hoang "Bảy giờ."

        huyen "Ông bị gì vậy?"

        hoang smile "Bảy rưỡi."

        huyen "Tám giờ. Giá cuối."

        $ story_flag("hoang_invitation_huyen_direct")
        $ story_add("hoang_huyen_interest", 5)

    elif story_state.get("hoang_self_acceptance", 0) >= 35:
        menu:
            "Hoàng nhắn..."

            "“Chủ Nhật đi với anh.”":
                hoang "Chủ Nhật đi với anh."

                huyen "Ô."

                huyen "Hôm nay biết dùng câu khẳng định rồi cơ à?"

                hoang "Cô đi không?"

                huyen "Đi."

                huyen "Trước khi ông kịp đổi lại thành câu hỏi."

                $ story_flag("hoang_invitation_huyen_direct")
                $ story_add("hoang_self_acceptance", 5)
                $ story_add("hoang_huyen_interest", 5)

            "“Anh tìm được chỗ chắc em sẽ thích.”":
                hoang "Anh tìm được chỗ chắc em sẽ thích."

                huyen "Nghe đáng ngờ."

                hoang "Vậy thôi."

                huyen "Ơ?"

                huyen "Ai cho thôi?"

                huyen "Gửi giờ đây."

                "Hoàng khẽ cười."

                "Cô luôn tự bước nốt nửa bước còn lại."

                "Điều đó dễ chịu."

                "Đôi khi cũng khiến cậu phải nhớ mình không nên để cô làm mãi."

                $ story_flag("hoang_invitation_huyen_personal")
                $ story_add("hoang_huyen_interest", 5)

            "Giả vờ hỏi về buổi đi chơi chung":
                hoang "Chủ Nhật cô có rảnh không?"

                huyen "Tâm có đi không?"

                "Hoàng nhìn câu hỏi."

                "Huyền đã nhận ra sự thiếu rõ ràng trước cả khi cậu nhận."

                menu:
                    "Nói thật":
                        hoang "Không. Anh đang mời em."

                        "Lần này Huyền trả lời chậm hơn."

                        huyen "Ừ."

                        huyen "Thế thì tôi đi."

                        $ story_flag("hoang_invitation_huyen_corrected_honestly")
                        $ story_add("hoang_self_acceptance", 5)
                        $ story_add("hoang_insecurity", -5)

                    "Đổi thành buổi đi ba người":
                        hoang "Anh định rủ cả Tâm."

                        huyen "Được thôi."

                        "Câu trả lời vẫn nhanh."

                        "Chỉ không còn dấu hỏi nào phía sau."

                        $ story_state["hoang_anniversary_route"] = "friend_group"
                        $ story_state["hoang_gift_recommendation"] = "friend_group_shared_day"
                        $ story_flag("hoang_huyen_invitation_retreats_to_group")
                        $ story_add("hoang_insecurity", 5)

                        call hoang_h01_brother_house_s04_invite_friend_group

                        return

    else:
        # Normally s03 already soft-resets low-self-acceptance Huyền paths.
        # This fallback keeps the scene safe for altered or older saves.
        "Hoàng gõ tên Huyền."

        "Rồi dừng lại."

        "Món quà đặt riêng trước mặt cậu."

        "Câu trả lời trong lòng thì chưa."

        "Cậu thoát khỏi khung trò chuyện riêng và mở nhóm ba người."

        $ story_state["hoang_anniversary_route"] = "friend_group"
        $ story_state["hoang_gift_recommendation"] = "friend_group_shared_day"
        $ story_flag("hoang_huyen_low_self_acceptance_group_fallback")

        call hoang_h01_brother_house_s04_invite_friend_group

    return


label hoang_h01_brother_house_s04_invite_friend_group:
    "Nhóm “Ba người trưởng thành có việc làm” hiện lên."

    hoang "Chủ Nhật này hai người rảnh không?"

    huyen "Có âm mưu gì?"

    tam "Em rảnh buổi sáng."

    hoang "Tròn một năm rồi."

    "Nhóm trò chuyện im gần nửa phút."

    huyen "Ông nhớ thật à?"

    hoang "Cô vừa nhắc."

    huyen "Ý tôi là trước khi tôi nhắc."

    "Hoàng nhìn tấm ảnh đã chọn để in."

    hoang "Có."

    tam "Em không nhớ chính xác ngày."

    huyen "Phản bội."

    tam "Nhưng em nhớ bữa ăn hôm đó."

    tam "Huyền đã gọi quá nhiều món."

    huyen "Đấy là vì hai người ăn ít."

    hoang "Chủ Nhật anh đặt bàn."

    huyen "Ở đâu?"

    hoang "Chỗ đủ yên."

    huyen "Nghe chán."

    tam "Em đi."

    huyen "Tôi có bảo không đi đâu."

    "Hoàng đặt điện thoại xuống."

    "Không có câu trả lời lớn nào được đưa ra."

    "Chỉ có ba người vẫn chọn dành một ngày cho nhau sau đúng một năm."

    "Hiện tại, như thế là đủ."

    $ story_flag("hoang_friend_group_invitation_sent")
    $ story_add("hoang_self_acceptance", 5)

    return
