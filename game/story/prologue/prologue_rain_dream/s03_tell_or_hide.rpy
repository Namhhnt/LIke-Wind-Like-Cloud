# FILE: game/story/prologue/prologue_rain_dream/s03_tell_or_hide.rpy
# Scene file.

label prologue_rain_dream_s03_tell_or_hide:
    scene bg_tam_room_morning
    with fade

    "Bảy giờ mười lăm."

    "Tâm đã thay xong áo sơ mi trắng và chân váy công sở màu nhạt."
    "Cô đứng trước gương, cài lại chiếc khuy cổ tay bên trái."

    "Cái khuy nhỏ trượt khỏi đầu ngón tay cô hai lần."

    tam confused "..."

    "Tâm nhìn bàn tay mình."
    "Rồi cô bật cười rất khẽ."

    tam smile "Run gì chứ. Có phải lần đầu đi phỏng vấn đâu."

    "Điện thoại lại rung."

    "Tên Huyền hiện trên màn hình."

    "Tâm bắt máy, kẹp điện thoại giữa vai và tai trong lúc tiếp tục chỉnh tóc."

    huyen happy "Tâm ơi, xuống chưa? Tao sắp đến sảnh rồi đấy."

    tam neutral "Biết rồi. Tao đang chuẩn bị xong."

    huyen teasing "Chuẩn bị xong nghĩa là còn mười phút nữa, đúng không?"

    tam irritated "Mày muốn đi phỏng vấn hay muốn bị tao chặn số từ sáng?"

    huyen laughing "Căng thế. Hôm nay đẹp trời mà."

    "Tâm liếc ra cửa sổ."

    "Nắng đã lên."
    "Mặt kính ngoài ban công khô ráo, sáng trong."

    "Không có dấu vết nào của mưa."

    "Thế mà trong đầu cô vẫn còn tiếng nước rơi trên mép ô."

    huyen confused "Alo? Còn đó không?"

    tam surprised "À... còn."

    huyen teasing "Sao im thế? Hồi hộp à?"

    "Tâm nhìn mình trong gương."
    "Một cô gái công sở bình thường, tóc gọn, son nhạt, cổ áo ngay ngắn."

    "Không giống người vừa mơ thấy một người đàn ông lạ đứng trong mưa."
    "Không giống người vẫn còn nhớ một giọng nói đến mức lòng bàn tay hơi lạnh."

    huyen neutral "Này. Có chuyện gì à?"

    "Huyền hỏi nhẹ hơn."

    "Chỉ một chút thôi."
    "Nhưng Tâm nghe ra."

    menu:
        "Tâm có kể cho Huyền nghe về giấc mơ không?"

        "Kể cho Huyền":
            $ story_flag('huyen_knows_dream')
            $ story_add('career_huyen', 1)

            tam neutral "Tối qua tao mơ hơi lạ."

            huyen confused "Lạ kiểu nào?"

            tam confused "Mưa. Một con phố. Tao đứng dưới mái hiên."

            "Tâm dừng lại, ngón tay vô thức chạm lên cổ tay."

            tam melancholic "Có một người đàn ông tới gần. Tao không nhìn rõ mặt."

            huyen teasing "Ồ."

            tam irritated "Đừng có ồ kiểu đó."

            huyen smile "Tao đã nói gì đâu."

            tam neutral "Nhưng tao có cảm giác... quen."

            "Đầu dây bên kia yên đi một nhịp."

            huyen neutral "Quen như người từng gặp rồi?"

            tam confused "Không biết. Chỉ là quen."

            huyen neutral "Vậy thì cứ nhớ lại từ từ. Đừng ép."

            tam surprised "Mày hôm nay nói chuyện tử tế bất thường đấy."

            huyen teasing "Tại tao đang ở dưới sảnh nhà mày. Chọc quá lát bị bỏ lại thì sao."

            "Tâm bật cười."
            "Cảm giác nặng trong ngực nhẹ đi một chút."

            tam smile "Chờ tao hai phút."

            huyen laughing "Ba phút. Tao thực tế hơn mày."

        "Giữ lại cho riêng mình":
            $ story_flag('tam_keeps_dream_private')
            $ story_add('tam_self_clarity', 1)

            tam neutral "Không có gì. Chắc hơi thiếu ngủ."

            huyen confused "Thật không?"

            tam smile "Thật."

            "Tâm nói rất bình tĩnh."
            "Bình tĩnh đến mức chính cô cũng thấy hơi lạ."

            huyen neutral "Ừ. Vậy xuống đi. Tao mua cà phê cho mày rồi."

            tam surprised "Cà phê?"

            huyen teasing "Không đường. Ít đá. Vì mày sẽ càm ràm nếu tao mua sai."

            "Tâm nhìn vào gương."
            "Khóe môi cô mềm xuống."

            tam smile "Biết điều đấy."

            huyen happy "Tất nhiên. Chị em tốt không phải để trưng."

            "Tâm tắt máy."
            "Một lúc sau, cô mở lại ngăn tủ, đặt quyển sổ nhỏ vào trong cùng."

            "Không phải giấu."
            "Chỉ là chưa đến lúc mở ra."

        "Nói đùa cho qua":
            $ story_flag('huyen_teases_dream')
            $ story_add('tam_hoang_interest', 1)

            tam teasing "Tao vừa mơ thấy một người đàn ông trong mưa."

            huyen shocked "Gì cơ?"

            tam smile "Cao. Trầm tính. Nói ít. Nghe khá đẹp trai nếu không bị mưa che mặt."

            huyen laughing "Trời đất. Mới sáng đã có người trong mộng rồi à?"

            tam embarrassed "Tao đùa thôi."

            huyen teasing "Đùa mà tả kỹ thế?"

            tam flustered "Huyền."

            huyen laughing "Rồi rồi. Tao không chọc nữa. Nhưng nếu lát vào công ty gặp đúng người như thế thì nhớ báo tao."

            "Tâm khựng lại."

            "Chỉ một giây."
            "Rất nhanh."

            tam neutral "Làm gì có chuyện đó."

            huyen teasing "Ai biết được. Đời mà. Nó thích làm màu hơn cả biên kịch phim Hàn."

            "Tâm cười theo."
            "Nhưng lúc cúi xuống lấy túi xách, cô kéo khóa hơi mạnh tay."

            "Tiếng khóa kim loại vang lên khô khốc trong căn phòng yên tĩnh."

    "Tâm kiểm tra lại hồ sơ lần cuối."
    "CV. Bản photo căn cước. Portfolio. Một cây bút."

    "Mọi thứ đều đủ."

    "Cô tắt đèn, bước ra cửa, rồi chợt quay lại nhìn căn phòng thêm một lần."

    "Chiếc giường đã được dọn gọn."
    "Đôi dép đã đặt ngay."
    "Rèm cửa khẽ lay trong gió điều hòa."

    "Không có gì bất thường."

    "Tâm đặt tay lên nắm cửa."

    tam neutral "Đi thôi."

    "Cánh cửa khép lại sau lưng cô."

    $ unlock_library_character("tam")
    $ unlock_character_section("tam", "inner_layer")
    $ unlock_character_section("tam", "core_traits")
    return