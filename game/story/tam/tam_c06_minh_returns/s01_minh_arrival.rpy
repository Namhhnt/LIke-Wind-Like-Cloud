# FILE: game/story/tam/tam_c06_minh_returns/s01_minh_arrival.rpy
# Resolves the two large C06 structures:
# - Home/canon branch when Tâm–Hoàng are committed.
# - Company-rumor branch when Tâm has not committed to Hoàng.

label tam_c06_minh_returns_s01_minh_arrival:
    scene black
    with fade

    centered "{size=46}CHAPTER 06{/size}\n{size=30}Minh về nước{/size}"

    scene black
    with dissolve

    $ _tam_hoang_committed = (
        story_has_flag("romance_hoang_tam_confirmed")
        or story_has_flag("tam_hoang_anniversary_route_reinforced")
        or (
            story_has_flag("tam_hoang_one_year_anniversary_completed")
            and story_state.get("hoang_anniversary_route", "") == "tam"
        )
        or story_has_direction("tam", "tam_hoang_commit")
        or (
            story_state.get("hoang_tam_trust", 0) >= 75
            and story_state.get("tam_hoang_interest", 0) >= 75
        )
    )

    $ story_state["tam_c06_branch"] = "home" if _tam_hoang_committed else "company_setup"
    $ story_flag("minh_returned_to_vietnam")

    if story_state["tam_c06_branch"] == "home":
        call tam_c06_minh_returns_s01_home_invitation
    else:
        call tam_c06_minh_returns_s01_company_rumor_begins

    return


label tam_c06_minh_returns_s01_home_invitation:
    scene bg_tam_room_morning
    with fade

    "Trời mưa rả rích."

    "Trong giấc mơ, một cô bé đeo kính ngồi một mình ở trạm xe buýt."

    "Tóc cô bé ướt."

    "Hai bàn tay giữ chặt mép váy."

    "Một chiếc khăn tay màu trắng được đưa sang."

    "Giọng một người con trai vang lên giữa tiếng mưa."

    "Cô bé có muốn nói chuyện không?"

    "Tâm mở mắt."

    "Tiếng báo thức trên bàn vừa bắt đầu rung."

    "Căn phòng tối hơn một buổi sáng bình thường."

    "Ngoài cửa sổ, nước mưa chạy thành những vệt dài trên kính."

    "Tâm nằm yên thêm vài giây."

    "Giấc mơ đã trở lại nhiều lần trong tuần."

    "Lần nào cũng dừng trước khi cô nhìn rõ gương mặt người đưa khăn."

    "Điện thoại rung lần nữa."

    hoang neutral "Anh đang dưới nhà."

    "Tâm ngồi dậy."

    "Cô gấp chăn, sửa lại gối rồi đi vào phòng tắm."

    "Những việc nhỏ quen thuộc nhanh chóng đẩy giấc mơ trở về một nơi chưa cần giải thích."

    "Hai mươi phút sau, Tâm bước vào xe Hoàng."

    "Cô nghiêng người, chạm môi nhẹ lên má anh."

    tam neutral "Chào buổi sáng."

    hoang neutral "Ừ."

    "Hoàng cho xe lăn bánh."

    "Cần gạt nước đều đặn quét màn mưa sang hai bên."

    hoang confused "Sáng nay ăn gì?"

    tam neutral "Phở."

    hoang neutral "Được."

    "Xe đi qua một ngã tư."

    "Hoàng giảm tốc."

    hoang confused "Chiều nay em được nghỉ sớm đúng không?"

    tam neutral "Vâng."

    tam confused "Có chuyện gì à?"

    "Hoàng nhìn đường."

    "Khóe miệng hơi cong."

    hoang neutral "Anh Minh mới về được mấy hôm."

    hoang neutral "Chiều anh đưa em về gặp lão."

    "Tâm xoay sang."

    tam surprised "Hôm nay luôn à?"

    hoang neutral "Ừ."

    tam neutral "Thế anh cứ về trước đi."

    tam neutral "Em mua ít đồ mang sang. Tối mình nấu ở nhà."

    hoang smile "Ý kiến hay."

    "Tâm gật."

    "Cô nhìn ra ngoài cửa kính."

    "Không hiểu vì sao, hình ảnh chiếc khăn tay trong mơ lại thoáng qua thêm một lần."

    "Đến giờ nghỉ trưa, Huyền đã biết chuyện."

    huyen surprised "Hôm nay ra mắt anh trai?"

    tam neutral "Chỉ là ăn tối thôi."

    huyen teasing "Sau khi ông ấy gọi mày là người yêu."

    huyen teasing "Rồi đưa mày về nhà gặp người thân."

    huyen neutral "Ừ. Một bữa tối hoàn toàn bình thường."

    tam irritated "Cậu nói nhỏ thôi."

    "Huyền nhấp một ngụm cà phê."

    "Mắt cô sáng lên rất thiếu kín đáo."

    huyen teasing "Không biết anh trai Hoàng thế nào nhỉ."

    tam neutral "Tớ chưa gặp."

    huyen neutral "Em trai đã thế thì ông anh chắc cũng không phải hàng thường."

    tam teasing "Đồ mê trai."

    huyen teasing "Tao đang suy luận di truyền."

    tam teasing "Mày thổi bóng vừa thôi."

    "Huyền chống cằm."

    huyen happy "Tao chỉ thấy vui cho mày."

    "Tâm nhìn cốc nước trên bàn."

    "Cô cũng vui."

    "Chỉ có một chút hồi hộp nằm ở nơi không liên quan lắm đến chuyện ra mắt."

    "Buổi chiều, mưa ngừng."

    "Tâm ghé chợ, mua đủ đồ cho bữa tối."

    "Hai túi thực phẩm nặng đến mức quai túi hằn đỏ trên ngón tay."

    "Cô định lấy xe máy."

    "Nhìn lớp mây vẫn còn thấp, cô đổi ý gọi taxi."

    "Hoàng sẽ đưa cô về."

    "Tiện hơn."

    "Chiếc taxi dừng trước cổng nhà."

    "Cánh cổng đang mở."

    "Tâm trả tiền, xách hai túi đồ xuống xe."

    "Chiếc taxi lùi sang bên kia đường."

    "Tài xế chưa rời đi ngay."

    "Tâm không để ý."

    "Cô đẩy cổng bước vào."

    $ story_flag("tam_on_way_to_meet_minh_at_hoang_house")

    return


label tam_c06_minh_returns_s01_company_rumor_begins:
    scene bg_company_open_office_day
    with fade

    "Tin đồn xuất hiện vào cuối một buổi chiều."

    "Ban đầu chỉ là một dòng tin nhắn trong nhóm nội bộ."

    "Tuần sau phía đối tác sẽ cử người sang làm việc trực tiếp."

    "Không ai biết ai gửi trước."

    "Đến lúc Tâm đọc được, câu chuyện đã có thêm ba phiên bản."

    "Một phiên bản nói dự án đang gặp vấn đề."

    "Một phiên bản nói ban lãnh đạo muốn thay toàn bộ cách vận hành."

    "Phiên bản còn lại khẳng định người sang kiểm tra khó tính đến mức từng làm một đội dự án xin chuyển bộ phận."

    "Tâm đóng khung trò chuyện."

    tam neutral "Tin đồn đi nhanh hơn tài liệu."

    "Ở bàn bên cạnh, Huyền ngẩng lên."

    huyen teasing "Nhưng tài liệu không vui bằng."

    tam confused "Cậu biết gì à?"

    huyen teasing "Biết tuần sau không nên xin nghỉ."

    tam surprised "Còn gì nữa?"

    "Huyền xoay ghế lại."

    huyen neutral "Tùy."

    tam confused "Tùy gì?"

    huyen teasing "Tùy mày muốn nghe tin thật hay tin hay."

    "Tâm nhìn cô."

    tam neutral "Tin thật."

    huyen neutral "Chán."

    "Huyền vẫn kéo ghế lại gần."

    $ _huyen_quan_mature = (
        story_state.get("huyen_quan_trust", 0) >= 55
        or story_has_direction("huyen", "huyen_quan_open")
        or story_has_direction("huyen", "huyen_quan_commit")
        or story_has_flag("huyen_quan_after_work")
    )

    $ _huyen_hoang_good = (
        (
            story_state.get("huyen_hoang_interest", 0) >= 55
            and story_state.get("hoang_huyen_interest", 0) >= 55
        )
        or story_has_direction("huyen", "huyen_hoang_commit")
        or story_has_flag("hoang_huyen_one_year_anniversary_completed")
        or story_has_flag("hoang_huyen_anniversary_clearly_confirmed")
    )

    $ _tam_other_romance_committed = (
        story_has_flag("romance_tam_quang_confirmed")
        or story_has_direction("tam", "tam_quang_commit")
        or story_has_direction("tam", "tam_minh_commit")
    )

    $ story_state["tam_c06_huyen_quan_mature"] = _huyen_quan_mature
    $ story_state["tam_c06_huyen_met_minh"] = _huyen_hoang_good
    $ story_state["tam_c06_tam_other_romance_committed"] = _tam_other_romance_committed

    "Một thông báo mới hiện trên màn hình."

    "Quân yêu cầu toàn đội rà soát tài liệu dự án trước thứ Sáu."

    "Không có tên đối tác."

    "Không có danh sách người tham dự."

    "Chỉ có một dòng cuối:"

    "Chuẩn bị cho giai đoạn phối hợp trực tiếp."

    $ story_flag("major_partner_visit_rumor_started")

    return
