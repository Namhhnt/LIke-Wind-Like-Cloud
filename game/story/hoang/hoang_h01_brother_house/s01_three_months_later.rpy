# FILE: game/story/hoang/hoang_h01_brother_house/s01_three_months_later.rpy
# Hoàng POV — establishes the three off-screen months and resolves
# the anniversary route from C04 commitment flags plus relationship scores.

label hoang_h01_brother_house_s01_three_months_later:
    scene black
    with fade

    $ _tam_relation = min(
        story_state.get("hoang_tam_trust", 0),
        story_state.get("tam_hoang_interest", 0)
    )

    $ _huyen_relation = min(
        story_state.get("hoang_huyen_interest", 0),
        story_state.get("huyen_hoang_interest", 0)
    )

    # Replace or supplement these names with the final exclusive flags from C04.
    $ _tam_committed = any(
        flag in story_flags
        for flag in (
            "romance_hoang_tam_confirmed",
            "direction_tam_tam_hoang_commit",
            "direction_hoang_hoang_tam_pursue",
        )
    )

    $ _huyen_committed = any(
        flag in story_flags
        for flag in (
            "romance_hoang_huyen_confirmed",
            "direction_huyen_huyen_hoang_commit",
            "direction_hoang_hoang_huyen_open",
        )
    )

    # A committed route still needs enough accumulated substance.
    # If both routes are somehow marked, the stronger route needs a clear margin.
    if _tam_committed and not _huyen_committed and _tam_relation >= 60:
        $ story_state["hoang_anniversary_route"] = "tam"

    elif _huyen_committed and not _tam_committed and _huyen_relation >= 55:
        $ story_state["hoang_anniversary_route"] = "huyen"

    elif _tam_committed and _huyen_committed:
        if _tam_relation >= 60 and _tam_relation >= _huyen_relation + 5:
            $ story_state["hoang_anniversary_route"] = "tam"
        elif _huyen_relation >= 55 and _huyen_relation >= _tam_relation + 5:
            $ story_state["hoang_anniversary_route"] = "huyen"
        else:
            $ story_state["hoang_anniversary_route"] = "friend_group"

    # Compatibility fallback for saves created before the final C04 flags.
    elif _tam_relation >= 60 and _tam_relation >= _huyen_relation + 5:
        $ story_state["hoang_anniversary_route"] = "tam"

    elif _huyen_relation >= 55 and _huyen_relation >= _tam_relation + 5:
        $ story_state["hoang_anniversary_route"] = "huyen"

    else:
        $ story_state["hoang_anniversary_route"] = "friend_group"

    "Ba tháng trôi qua mà không có sự kiện nào đủ lớn để người ta khoanh đỏ trên lịch."

    "Chỉ có những việc nhỏ tự tìm được chỗ trong ngày."

    if story_state["hoang_anniversary_route"] == "tam":
        "Tâm đã thôi hỏi trước khi lấy một chai nước trong tủ lạnh nhà Hoàng."

        "Cô vẫn đặt mọi thứ về đúng chỗ."

        "Trừ chiếc ô màu kem đang tựa bên cạnh cửa ra vào."

        "Nó ở đó từ cuối tuần trước."

        "Tâm đã nhắn hai lần rằng hôm nào tiện sẽ ghé lấy."

        "Cả hai đều biết chữ “tiện” ấy không thật sự cần thiết."

        "Điện thoại Hoàng sáng lên."

        tam "Về đến nhà chưa?"

        "Tin nhắn được gửi cách đây chưa đầy một phút."

        "Ba tháng trước, Tâm sẽ chờ thêm một lúc rồi mới hỏi."

        "Bây giờ cô hỏi ngay."

        "Hoàng cũng trả lời ngay."

        hoang "Rồi. Em ngủ đi."

        tam "Anh cũng thế."

        "Cậu đặt điện thoại xuống."

        "Mười giây sau, màn hình lại sáng."

        tam "Đừng mở máy làm việc nữa."

        "Hoàng nhìn chiếc laptop vẫn còn mở trên bàn."

        hoang smile "Biết rồi."

        $ story_flag("hoang_tam_three_months_deepened")

    elif story_state["hoang_anniversary_route"] == "huyen":
        "Danh sách phát trên xe Hoàng đã đổi tên ba lần trong tháng này."

        "Lần đầu là “Nhạc nghe được”."

        "Lần thứ hai, Huyền đổi thành “Nhạc cho người có tuổi”."

        "Hiện tại nó mang tên “Đừng tự tiện xóa”."

        "Hoàng chưa xóa."

        "Trong điện thoại còn một đoạn ghi âm dài mười bảy giây."

        huyen "Tôi nói trước nhé, quán đó dở thì ông tự ăn hết."

        "Có tiếng gió."

        "Tiếng xe chạy ngang."

        "Rồi giọng Huyền nhỏ đi một chút."

        huyen "Mà... đến nơi thì nhắn."

        "Đoạn cuối không có gì đặc biệt."

        "Hoàng đã nghe lại bốn lần."

        "Cậu không có lý do thuyết phục cho chuyện đó."

        "Có điều ba tháng qua, những hôm Huyền im hơn bình thường, cậu luôn là người nhận ra trước."

        $ story_flag("hoang_huyen_three_months_deepened")

    else:
        "Nhóm trò chuyện ba người vẫn mang cái tên Huyền đặt từ ngày đầu."

        "“Ba người trưởng thành có việc làm.”"

        "Không ai trong số họ thấy cái tên ấy còn đáng tin."

        "Tâm thường gửi ảnh đồ ăn."

        "Huyền gửi mọi thứ còn lại."

        "Hoàng chủ yếu trả lời bằng một dấu hỏi."

        "Tối nay, Huyền đào lại một tấm ảnh cũ."

        "Ba người đứng cạnh nhau ở buổi tiệc công ty."

        "Tâm nhìn nhầm hướng."

        "Huyền cười quá lớn."

        "Hoàng có vẻ như chưa biết phải đặt tay ở đâu."

        huyen "Này."

        huyen "Chủ Nhật là tròn một năm đấy."

        tam "Một năm gì?"

        huyen "Một năm hai người có vinh dự quen tôi."

        hoang "Trí nhớ của cô chỉ hoạt động khi cần tự đề cao à?"

        huyen "Thế ông có nhớ không?"

        "Hoàng nhìn ngày chụp tấm ảnh."

        "Cậu nhớ."

        "Chỉ là chưa kịp nói trước."

        $ story_flag("tam_huyen_hoang_three_months_deepened")
        $ story_flag("tam_huyen_hoang_friend_anniversary")

    "Hoàng tắt màn hình."

    "Căn phòng tối đi một chút."

    "Chủ Nhật còn bốn ngày."

    "Vừa đủ lâu để chuẩn bị một món quà."

    "Hoặc để tự làm chuyện đó khó hơn mức cần thiết."

    return
