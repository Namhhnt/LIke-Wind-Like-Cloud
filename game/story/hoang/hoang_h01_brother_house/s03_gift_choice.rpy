# FILE: game/story/hoang/hoang_h01_brother_house/s03_gift_choice.rpy
# Finalizes the gift or shared anniversary plan.

label hoang_h01_brother_house_s03_gift_choice:
    scene black

    $ _anniversary_route = story_state.get(
        "hoang_anniversary_route",
        "friend_group"
    )

    $ _gift_recommendation = story_state.get(
        "hoang_gift_recommendation",
        "friend_group_shared_day"
    )

    if _anniversary_route == "tam":
        call hoang_h01_brother_house_s03_choose_tam_gift

    elif _anniversary_route == "huyen":
        call hoang_h01_brother_house_s03_choose_huyen_gift

    else:
        call hoang_h01_brother_house_s03_choose_friend_group_plan

    return


label hoang_h01_brother_house_s03_choose_tam_gift:
    "Hoàng mở lại trang cửa hàng trang sức."

    "Hai đôi bông tai vẫn nằm cạnh nhau trên màn hình."

    "Một đôi nhỏ, đá hoàng ngọc màu vàng nhạt, phần viền trắng đơn giản."

    "Đôi còn lại lớn hơn, sáng hơn, đắt hơn gần ba lần."

    if story_state.get("hoang_gift_recommendation") == "tam_topaz_earrings":
        "Cậu xóa đôi lớn khỏi giỏ hàng."

        "Động tác rất nhanh."

        "Nhanh hơn quãng thời gian cậu đã mất để thừa nhận mình vốn không cần nó."

        hoang neutral "Cái này là đủ."

        $ story_flag("hoang_gift_tam_topaz_earrings")
        $ story_add("hoang_tam_trust", 5)

    elif story_state.get("hoang_gift_recommendation") == "tam_expensive_topaz":
        menu:
            "Trước khi thanh toán..."

            "Quay lại đôi nhỏ":
                "Hoàng nhìn mức giá thêm một lúc."

                "Sau đó chuyển sang đôi nhỏ hơn."

                "Không phải vì rẻ."

                "Vì cậu có thể hình dung Tâm đeo nó vào một ngày đi làm bình thường."

                $ story_flag("hoang_gift_tam_topaz_earrings")
                $ story_add("hoang_self_acceptance", 5)
                $ story_add("hoang_insecurity", -5)

            "Giữ đôi nổi bật hơn":
                "Hoàng nhấn thanh toán."

                "Ngay sau đó, cậu đặt điện thoại xuống hơi mạnh."

                "Món quà đã được mua."

                "Cảm giác chắc chắn vẫn chưa đến."

                $ story_flag("hoang_gift_tam_expensive_topaz")
                $ story_flag("tam_may_feel_gift_is_too_much")
                $ story_add("hoang_insecurity", 5)

    else:
        "Hoàng không mở trang trang sức nữa."

        "Cậu chỉ đặt bàn ăn sáng và lưu lại địa chỉ công viên."

        "Món quà vẫn còn để trống."

        "Ngày Chủ Nhật thì không."

        $ story_flag("hoang_tam_date_without_gift")
        $ story_add("hoang_self_acceptance", 5)

    return


label hoang_h01_brother_house_s03_choose_huyen_gift:
    "Hoàng mở thư mục ảnh trong điện thoại."

    "Phần lớn là ảnh chụp linh tinh."

    "Biển hiệu sai chính tả."

    "Một cốc cà phê bị đổ."

    "Tâm ngủ gục trên bàn."

    "Một con mèo béo đến mức Huyền nhất quyết cho rằng nó đang mang thai."

    "Hoàng đã không đủ tàn nhẫn để nói đó là mèo đực."

    "Cậu kéo xuống thêm."

    "Có một tấm Huyền đứng dưới mái hiên, tay cầm túi đồ ăn, tóc bị gió thổi rối."

    "Cô đang cười với người ngoài khung hình."

    "Người đó là Hoàng."

    if story_state.get("hoang_self_acceptance", 0) >= 55:
        "Hoàng gửi tấm ảnh sang máy in."

        "Tờ ảnh nhỏ trượt ra, hơi ấm."

        "Cậu đặt nó vào trang đầu tiên của cuốn album trống."

        "Không viết gì bên dưới."

        "Cậu nghĩ Huyền sẽ tự nói đủ phần còn lại."

        $ story_flag("hoang_gift_huyen_pocket_photo_printer")
        $ story_flag("hoang_includes_first_huyen_photo")
        $ story_add("hoang_huyen_interest", 5)

    elif story_state.get("hoang_self_acceptance", 0) >= 35:
        menu:
            "Tấm ảnh đầu tiên trong album là..."

            "Một tấm chỉ có Huyền":
                "Hoàng đặt tấm ảnh dưới mái hiên vào trang đầu."

                "Cậu nhìn nó thêm một lần."

                "Rồi khép album lại trước khi kịp đổi ý."

                $ story_flag("hoang_gift_huyen_pocket_photo_printer")
                $ story_flag("hoang_openly_centers_huyen")
                $ story_add("hoang_self_acceptance", 5)
                $ story_add("hoang_huyen_interest", 5)

            "Một tấm của cả ba":
                "Hoàng chọn ảnh ba người ở bữa tiệc công ty."

                "An toàn."

                "Vui."

                "Không ai phải hiểu thêm điều gì."

                "Cậu đặt nó vào trang đầu."

                "Tấm ảnh của Huyền vẫn nằm trong điện thoại."

                $ story_flag("hoang_gift_huyen_pocket_photo_printer")
                $ story_flag("hoang_hides_huyen_gift_meaning")
                $ story_add("hoang_insecurity", 5)

            "Để album trống":
                "Hoàng không in tấm nào."

                "Cậu tự nhủ để Huyền chọn sẽ hợp hơn."

                "Lý do nghe rất hợp lý."

                "Hợp lý đến mức cậu biết mình đang né."

                $ story_flag("hoang_gift_huyen_pocket_photo_printer")
                $ story_flag("hoang_leaves_huyen_album_blank")
                $ story_add("hoang_insecurity", 5)

    else:
        "Hoàng nhìn tấm ảnh của Huyền rất lâu."

        "Sau cùng, cậu không đặt hàng."

        "Cậu chuyển sang nhóm trò chuyện ba người."

        hoang neutral "Chủ Nhật này hai người rảnh không?"

        $ story_state["hoang_anniversary_route"] = "friend_group"
        $ story_state["hoang_gift_recommendation"] = "friend_group_shared_day"
        $ story_flag("hoang_huyen_route_paused_by_low_self_acceptance")

        call hoang_h01_brother_house_s03_choose_friend_group_plan

    return


label hoang_h01_brother_house_s03_choose_friend_group_plan:
    "Hoàng bỏ hết quà cá nhân khỏi giỏ hàng."

    "Cậu đặt một bàn cho ba người."

    "Không phải nhà hàng quá sang."

    "Chỉ là một nơi đủ yên để ngồi lâu, món ăn ổn, và không ai phải nhìn giá trước khi gọi thêm."

    "Sau đó cậu chọn một tấm ảnh ba người ở tiệc công ty."

    "Trong ảnh, Tâm đang nhìn sang bên cạnh."

    "Huyền cười quá lớn."

    "Hoàng thì rõ ràng chưa biết phải đặt tay ở đâu."

    hoang smile "Đúng là chẳng ai tử tế."

    "Cậu vẫn gửi ảnh đi in."

    "Ba bản."

    $ story_flag("hoang_friend_group_anniversary_plan")
    $ story_flag("hoang_prints_three_group_photos")
    $ story_add("hoang_self_acceptance", 5)

    return
