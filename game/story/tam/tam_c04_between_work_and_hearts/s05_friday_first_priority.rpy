# FILE: game/story/tam/tam_c04_between_work_and_hearts/s05_friday_first_priority.rpy
# Week 01 — First explicit priority choice. No route is locked.

label tam_c04_w01_s05_friday_first_priority:
    scene bg_company_open_office_day
    with dissolve

    "Thứ Sáu, năm giờ bốn mươi hai phút."

    "Văn phòng đã vơi người. Ánh sáng ngoài cửa kính nhạt dần trên những mặt bàn còn mở laptop."

    "Huyền đặt một xấp giấy xuống cạnh Tâm."

    huyen tired "Tao ở lại thêm một lúc. Phần mapping vẫn còn hai chỗ nhìn không thuận mắt."

    tam neutral "Không thuận mắt mày hay không thuận mắt anh Quân?"

    huyen irritated "Hiện tại hai khái niệm đó đang đáng ghét như nhau."

    "Điện thoại Tâm rung."

    "Hoàng hỏi cuối tuần cô có bận không."

    "Ngay dưới đó là tin của Quang: anh đã gửi Thiên An phần tài liệu còn thiếu, nhưng chưa chắc cô chịu nghỉ đúng giờ."

    "Trên màn hình laptop, tab khóa học Tâm mở từ đầu tuần vẫn còn nằm ở góc phải."

    "Bốn việc. Không việc nào thật sự khẩn cấp."

    "Chỉ có điều cuối cùng cô vẫn phải đặt tay vào một việc trước."

    menu:
        "Trả lời Hoàng trước":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_sub("tam_insecurity", 5)
            $ story_add("huyen_quan_trust", 3)
            $ story_add("career_huyen", 3)
            $ story_add("thienan_quang_trust", 3)
            $ story_add("quang_persistence", 3)
            $ story_add_direction("tam", "tam_hoang_open")
            $ story_flag("tam_c04_w01_first_focus_hoang")

            "Tâm cầm điện thoại lên."

            tam smile "Cuối tuần em chưa có kế hoạch cố định. Anh định làm gì?"

            "Tin nhắn được gửi đi."

            "Ở bàn bên cạnh, Huyền đã mở lại file báo cáo. Cô kéo ghế sang đầu bàn trống, nơi Quân vừa quay lại lấy tài liệu."

            "Quang cũng không nhắn thêm. Có lẽ anh đã tự quyết định phần của mình."

            "Thế giới không đứng lại chỉ vì Tâm chọn nhìn về một phía."

        "Ở lại làm cùng Huyền":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_add("hoang_self_acceptance", 3)
            $ story_add("thienan_quang_trust", 3)
            $ story_add("quang_persistence", 3)
            $ story_add_direction("tam", "tam_support_huyen")
            $ story_flag("tam_c04_w01_first_focus_huyen")

            tam neutral "Gửi tao hai chỗ đó. Làm xong rồi về."

            huyen confused "Mày không có hẹn à?"

            tam teasing "Có một cuộc hẹn với việc không bị sửa báo cáo lần ba."

            huyen smile "Lãng mạn ghê."

            "Tâm úp điện thoại xuống bàn."

            "Hoàng không nhắn thêm ngay. Quang tự mang phần hồ sơ còn lại tới cho Thiên An."

            "Hai chiếc ghế trong văn phòng được kéo gần nhau hơn."

        "Lùi lại để Huyền tự làm việc với Quân":
            $ story_add("tam_observation", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("career_huyen", 5)
            $ story_add("hoang_self_acceptance", 3)
            $ story_add("thienan_quang_trust", 3)
            $ story_flag("tam_c04_w01_first_focus_huyen_quan")
            $ story_flag("tam_c04_w01_tam_steps_back_from_huyen_quan")

            tam neutral "Hai chỗ đó mày trao đổi trực tiếp với anh Quân đi. Mày nắm phần này rõ nhất."

            huyen shocked "Mày định bỏ tao lại thật à?"

            tam smile "Tao định để mày tự thắng. Khác nhau."

            "Huyền nhìn cô đầy nghi ngờ."

            huyen irritated "Nếu tao chết trong phòng họp thì nhớ xóa lịch sử tìm kiếm."

            tam teasing "Không. Tao sẽ dùng nó làm bằng chứng động cơ."

            "Tâm đóng laptop. Khi đi ngang phòng họp, cô thấy Huyền đang chỉ vào một dòng trong tài liệu."

            "Quân không cắt lời."

        "Nhắn Quang, bảo anh đừng vòng qua Tâm nữa":
            $ story_add("tam_observation", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ story_add("huyen_quan_trust", 3)
            $ story_add("career_huyen", 3)
            $ story_add("hoang_self_acceptance", 3)
            $ story_add_direction("tam", "tam_support_quang_thienan")
            $ story_flag("tam_c04_w01_first_focus_quang_thienan")

            "Tâm mở khung chat với Quang."

            tam neutral "Anh tự gọi chị An đi. Đừng hỏi em chị ấy có ổn không nữa."

            "Ba dấu chấm hiện lên, biến mất, rồi hiện lại."

            quang "Anh biết rồi."

            "Tin nhắn ngắn đến mức đáng ngờ."

            "Tâm đặt điện thoại xuống. Ở bên kia bàn, Huyền cầm tài liệu sang phòng Quân một mình."

            "Hoàng cũng không thúc giục câu trả lời."

        "Mang tài liệu về và tự học thêm":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_add("huyen_quan_trust", 3)
            $ story_add("career_huyen", 3)
            $ story_add("thienan_quang_trust", 3)
            $ story_add("quang_persistence", 3)
            $ story_add("hoang_self_acceptance", 3)
            $ story_add_direction("tam", "tam_career_focus")
            $ story_flag("tam_c04_w01_first_focus_career")

            "Tâm lưu file, cho tập tài liệu vào túi."

            tam neutral "Tao về trước. Tối tao xem lại phần requirement."

            huyen confused "Cuối tuần mà mày còn học à?"

            tam smile "Chưa chắc. Nhưng mang về trước thì lương tâm đỡ ồn."

            "Huyền nhăn mặt như muốn phản đối, rồi quay lại nhìn màn hình của mình."

            "Quang tự xử lý chuyện của Thiên An. Hoàng để lời mời nằm yên trong khung chat."

            "Những người khác tiếp tục phần việc của họ. Tâm cũng vậy."

    "Trước khi rời công ty, Tâm nhìn lại bàn làm việc."

    "Một chiếc cốc chưa rửa. Một góc tài liệu gấp lệch. Ba cuộc trò chuyện chưa thật sự kết thúc."

    "Cô tắt đèn bàn."

    "Cuối tuần mở ra phía trước, trống vừa đủ để người ta tự quyết định sẽ lấp nó bằng điều gì."

    return
