# FILE: game/story/tam/tam_c02_company_party/s00_onboarding.rpy
# Scene file.

label tam_c02_company_party_s00_onboarding:
    $ tam_monthly_salary = 15000000 if story_has_flag("tam_perfect_interview") else 12000000
    $ phone_update_character_status("tam", job_title="Junior Staff", job_level=1, income_monthly=tam_monthly_salary)
    $ phone_update_character_status("huyen", job_title="Junior Staff", job_level=1, income_monthly=12000000)
    python:
        activity_state = ensure_activity_state()
        activity_state["player_is_employed"] = True
        activity_state["monthly_salary"] = tam_monthly_salary
    if not story_has_flag("tam_c02_party_invitation_sent"):
        $ story_flag("tam_c02_party_invitation_sent")
        $ phone_unlock_mail("company_party_invitation")
        $ phone_refresh_all()

    scene bg_company_open_office_day
    with fade

    "Ngày đầu tiên đi làm không có tiếng trống khai giảng, cũng chẳng có ai đứng ở cửa rắc hoa giấy."

    "Chỉ có thẻ nhân viên mới, một chiếc laptop còn nguyên mùi nhựa, và bản lịch onboarding được gửi vào email lúc tám giờ mười hai phút."

    "Tâm nhìn dòng tiêu đề email thêm một lần."

    "{i}Onboarding Plan — 2-week training and 6-week trial preparation.{/i}"

    "Hai tuần làm quen quy trình."

    "Sáu tuần chuẩn bị cho giai đoạn thử việc đầu tiên."

    "Và cuối dòng lịch, được tô màu vàng nhạt như thể không quan trọng lắm, là một mục nhỏ."

    "{i}Company Anniversary Party — Friday evening.{/i}"

    tam neutral "Hai tháng..."

    huyen smile "Ừ. Nghe cũng không dài lắm."

    "Huyền kéo ghế ngồi xuống bên cạnh Tâm. Trên bàn cô là một cuốn sổ mới tinh, bút còn chưa bóc tem."

    huyen teasing "Nếu không tính chuyện trong hai tháng đó mình có thể bị đánh giá, bị soi, bị giao việc, bị hỏi vì sao commit sai format..."

    tam tired "Mày đang động viên tao đấy à?"

    huyen grinning "Đang giúp mày làm quen với thực tế. Dịch vụ bạn thân cao cấp."

    "Tâm bật cười rất khẽ."

    "Một tiếng cười nhỏ thôi, đủ để phần vai đang hơi căng của cô hạ xuống."

    "Phía bên kia văn phòng, vài nhân viên đi ngang qua với cốc cà phê trên tay. Tiếng bàn phím, tiếng máy in, tiếng ai đó gọi nhau qua vách kính."

    "Mọi thứ vận hành đều, nhanh, và có vẻ đã quen với việc không chờ người mới."

    "Tâm mở file onboarding."

    "Dòng đầu tiên là danh sách những công cụ cần setup. Dòng thứ hai là quy trình báo cáo. Dòng thứ ba là lịch training."

    "Cô kéo xuống thêm một chút."

    "Một ô checklist nhỏ hiện ra ở cuối trang."

    "Chưa có gì khó."

    "Vậy mà ngón tay cô vẫn dừng ở touchpad lâu hơn cần thiết."

    huyen neutral "Sao?"

    tam neutral "Không có gì."

    huyen teasing "Không có gì mà mặt như vừa thấy bảng KPI biết nói."

    tam embarrassed "Mặt tao bình thường."

    huyen smile "Ừ. Bình thường kiểu chuẩn bị tự lập bảng Excel quản lý nỗi lo."

    "Tâm liếc sang Huyền."

    "Huyền tỉnh bơ mở nắp bút. Cái tem nhỏ trên thân bút vẫn còn dính một góc."

    "Tâm đưa tay bóc nó ra giúp."

    huyen surprised "Ơ?"

    tam neutral "Vướng mắt."

    huyen teasing "Đấy. Người vừa vào công ty ngày đầu đã bắt đầu tối ưu vật tư văn phòng."

    "Tâm không cãi."

    "Cô chỉ đặt mảnh tem nhỏ vào góc bàn, ngay ngắn đến mức chính cô cũng thấy hơi buồn cười."

    menu:
        "Tâm nên chuẩn bị cho hai tháng thử việc thế nào?"

        "Chuẩn bị nghiêm túc":
            $ story_add('career_tam', 3)
            $ story_add('tam_self_clarity', 1)
            $ story_flag('tam_c02_serious_onboarding')

            "Tâm kéo cuốn sổ của mình lại gần."

            "Cô viết xuống ba dòng ngắn."

            "{i}Setup xong trong hôm nay.{/i}"

            "{i}Hỏi rõ quy trình trước khi làm.{/i}"

            "{i}Không để Huyền bị lạc một mình.{/i}"

            huyen neutral "Mới ngày đầu mà mày đã lập kế hoạch tác chiến rồi à?"

            tam smile "Không. Kế hoạch sống sót thôi."

            huyen laughing "Nghe chuyên nghiệp hẳn."

            "Tâm đóng nắp bút lại."

            "Tiếng cạch rất nhỏ, nhưng lòng cô yên hơn một chút."

        "Đi chậm lại cùng Huyền":
            $ story_add('career_tam', 1)
            $ story_add('career_huyen', 2)
            $ story_add('tam_self_clarity', 1)
            $ story_flag('tam_c02_huyen_shared_pace')

            "Tâm nhìn sang màn hình của Huyền."

            "Cửa sổ cài đặt phần mềm của cô nàng đã đứng yên ở mức bốn mươi bảy phần trăm được gần năm phút."

            tam neutral "Đưa đây tao xem."

            huyen surprised "Mày chưa setup xong máy mày mà."

            tam smile "Tao làm sau cũng được."

            huyen teasing "Nghe cảm động ghê."

            tam neutral "Đừng làm quá. Máy mày mà lỗi thì mày lại ngồi chửi hệ điều hành cả buổi."

            huyen grinning "Bạn thân hiểu mình đến đau lòng."

            "Tâm kéo ghế sát lại."

            "Hai chiếc laptop đặt cạnh nhau, hai màn hình sáng lên trong cùng một màu xanh nhạt."

            "Không nhanh hơn bao nhiêu."

            "Nhưng ít nhất, cảm giác lạc lõng cũng giảm đi một nửa."

        "Thấy hơi bị ngợp":
            $ story_add('tam_insecurity', 2)
            $ story_add('doom_score', 1)
            $ story_flag('tam_c02_onboarding_intimidated')

            "Tâm nhìn những dòng checklist thêm một lúc."

            "Mỗi dòng đều ngắn."

            "Nhưng khi xếp cạnh nhau, chúng biến thành một bức tường khá cao."

            tam confused "Tao thấy... hơi nhiều."

            huyen neutral "Ừ. Nhiều thật."

            "Câu trả lời quá thật của Huyền khiến Tâm ngẩng lên."

            huyen smile "Nhưng nhiều thì chia ra làm. Mày xử lý phần của mày, tao xử lý phần của tao. Cùng lắm thì hai đứa cùng bị mắng, đỡ cô đơn."

            tam tired "An ủi kiểu gì thế?"

            huyen teasing "Kiểu thực tế."

            "Tâm cười theo."

            "Nhưng khi cúi xuống, cô nhận ra mình đã bấm đầu bút quá mạnh."

            "Một chấm mực nhỏ lem ra trên trang giấy đầu tiên."

    scene bg_meeting_room_day
    with dissolve

    "Buổi orientation đầu tiên diễn ra trong phòng họp nhỏ."

    "Người phụ trách nhân sự nói về quy trình, văn hóa, lịch training, và những thứ mà người mới thường chỉ nhớ được một nửa."

    manager "Trong hai tuần đầu, các bạn cứ hỏi nhiều vào. Hỏi sớm luôn tốt hơn sửa muộn."

    "Tâm ghi câu đó vào sổ."

    "Nét chữ của cô hơi nhỏ hơn bình thường."

    manager "Sau onboarding, các bạn sẽ có sáu tuần để làm quen với team, nhận task thật, và chuẩn bị cho buổi đánh giá thử việc."

    huyen neutral "Sáu tuần..."

    tam neutral "Ừ."

    manager "À, tháng sau công ty có tiệc kỷ niệm thành lập. Người mới cũng tham gia nhé. Không bắt buộc phải quá nghiêm túc, nhưng cũng đừng xem nó là một buổi ăn miễn phí đơn thuần."

    huyen teasing "Vậy là vẫn có ăn miễn phí."

    tam neutral "Mày nhỏ tiếng thôi."

    "Tâm cúi xuống nhìn dòng chữ cuối cùng mình vừa ghi."

    "{i}Đừng xem mọi thứ là chuyện nhỏ.{/i}"

    "Cô dừng bút."

    "Rồi gạch nhẹ dưới chữ {i}mọi thứ{/i}."

    return
