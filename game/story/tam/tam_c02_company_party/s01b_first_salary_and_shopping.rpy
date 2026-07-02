# FILE: game/story/tam/tam_c02_company_party/s01b_first_salary_and_shopping.rpy
# Scene file.
# Temporary implementation: Shopping Area click is represented by a selection menu.
# Later, map_hub / interactive_map can call tam_c02_company_party_shopping_area_menu
# when the player clicks location_id == "shopping_area" during this chapter context.
# # hint:
# if current_chapter == "tam_c02_company_party" and location_id == "shopping_area" and story_has_flag("tam_c02_shopping_area_unlocked"):
#     call tam_c02_company_party_shopping_area_menu

label tam_c02_company_party_s01b_first_salary_and_shopping:
    scene bg_company_open_office_day
    with fade

    $ story_flag('tam_c02_first_salary_received')

    "Thứ Năm, một ngày trước buổi tiệc kỷ niệm công ty, Tâm nhận được tháng lương đầu tiên."

    "Không có tiếng pháo hoa."

    "Không có nhạc nền chiến thắng."

    "Chỉ có một thông báo ngân hàng hiện lên trên màn hình điện thoại lúc cô vừa định đứng dậy đi lấy nước."

    tam surprised "..."

    huyen neutral "Sao mặt mày nghiêm trọng thế?"

    "Tâm nhìn lại con số trong tin nhắn."

    "Một con số không lớn đến mức thay đổi đời người."

    "Nhưng đủ để khiến cô ngồi yên thêm vài giây."

    tam neutral "Lương về rồi."

    huyen surprised "Thật á?"

    "Huyền lập tức kéo ghế sang, nhanh đến mức bánh xe ghế kêu lên một tiếng nhỏ trên sàn."

    huyen happy "Cho tao xem. Không phải số tiền. Tao xem cảm xúc thôi."

    tam tired "Cảm xúc cũng cần xem màn hình à?"

    huyen grinning "Có những cảm xúc phải có sao kê mới đáng tin."

    "Tâm tắt màn hình điện thoại, nhưng khóe môi vẫn không giấu được."

    "Tháng lương đầu tiên."

    "Cô đã từng nghĩ mình sẽ bình tĩnh hơn."

    "Nhưng hóa ra có những thứ rất đời thường vẫn đủ làm người ta thấy mình vừa bước qua một cánh cửa nhỏ."

    huyen smile "Ngày mai tiệc công ty rồi."

    tam neutral "Ừ."

    huyen teasing "Và mày định mặc bộ váy công sở an toàn như báo cáo nội bộ?"

    tam embarrassed "Tao chưa quyết."

    huyen neutral "Nghĩa là có."

    tam "..."

    huyen tired "Tâm."

    tam confused "Gì?"

    huyen neutral "Tháng lương đầu tiên không bắt buộc phải tiêu hết. Nhưng ít nhất cũng nên mua cho bản thân một thứ để nhớ."

    "Tâm nhìn xuống tay mình."

    "Ngón tay cô đặt trên cạnh điện thoại, vô thức miết nhẹ phần ốp lưng đã hơi cũ."

    tam neutral "Một thứ để nhớ..."

    huyen smile "Ừ. Không cần đắt. Chỉ cần sau này nhìn lại, mày nhớ: à, hồi đó mình bắt đầu đi làm rồi."

    "Câu đó chạm nhẹ hơn Tâm tưởng."

    "Bên ngoài cửa kính văn phòng, nắng chiều đang trượt dần khỏi những tòa nhà đối diện."

    "Một ngày làm việc sắp kết thúc."

    "Ngày mai là buổi tiệc."

    "Nếu muốn mua gì đó, tối nay là lúc hợp lý nhất."

    menu:
        "Sau giờ làm, Tâm có đi mua sắm không?"

        "Đi Shopping Area với Huyền":
            $ story_flag('tam_c02_shopping_area_unlocked')
            $ story_add('tam_self_clarity', 1)

            tam neutral "Tan làm đi với tao một lát không?"

            huyen happy "Shopping?"

            tam smile "Ừ."

            huyen grinning "Cuối cùng. Công ty này đã tạo ra giá trị xã hội."

            tam tired "Mày bớt nói quá."

            huyen teasing "Không. Khoảnh khắc bạn thân nhận lương đầu và chịu đi mua đồ là sự kiện văn hóa."

            "Tâm cất điện thoại vào túi."

            "Dù chưa biết sẽ mua gì, cô bỗng thấy lòng mình nhẹ hơn một chút."

            call tam_c02_company_party_shopping_area_menu

        "Không mua gì, để dành tiền":
            $ story_add('career_tam', 2)
            $ story_add('tam_self_clarity', 1)
            $ story_flag('tam_c02_saved_first_salary')
            $ story_add_direction('tam', 'tam_career_focus')

            "Tâm nhìn lại tin nhắn ngân hàng."

            "Rồi cô tắt màn hình."

            tam neutral "Thôi. Tao để dành đã."

            huyen confused "Không mua gì thật à?"

            tam smile "Chưa cần."

            huyen neutral "Mai đi tiệc đấy."

            tam neutral "Tao có đồ mặc rồi."

            huyen tired "Câu này nghe như mở đầu của một bi kịch thời trang."

            tam laughing "Không đến mức đó đâu."

            "Huyền nhìn cô thêm một lúc, rồi nhún vai."

            huyen smile "Được. Tiền của mày, mày quyết."

            "Tâm gật đầu."

            "Có một chút tiếc."

            "Nhưng cũng có một chút yên tâm."

            "Tháng lương đầu tiên nằm im trong tài khoản."

            "Như một cái neo nhỏ."

            "Không rực rỡ."

            "Nhưng chắc."

    return