# FILE: game/story/tam/tam_c04_between_work_and_hearts/s02_new_work_rhythm.rpy
# Week 01 — Quân assigns Tâm and Huyền a more demanding work package.

label tam_c04_w01_s02_new_work_rhythm:
    scene bg_company_open_office_day
    with dissolve

    scene cg_tam_c04_team_review
    with dissolve
    "Đầu giờ sáng, Quân đặt một tập tài liệu xuống giữa bàn Tâm và Huyền."
    scene bg_meeting_room_day
    with dissolve

    quan neutral "Bản tổng hợp tiến độ tuần trước còn thiếu phần đối chiếu yêu cầu khách hàng."

    huyen confused "Thiếu ạ? Em nhớ bọn em đã đính kèm rồi."

    quan neutral "Đính kèm không có nghĩa là đối chiếu."

    "Huyền khép miệng."

    "Cô kéo tập tài liệu lại, lật qua hai trang rồi dùng đầu bút chỉ vào một bảng đã được đánh dấu."

    huyen irritated "Chỗ này bọn em ghi đúng mà."

    quan neutral "Số đúng. Cách hiểu sai."

    "Quân nhìn sang Tâm."

    quan neutral "Hai em có ba ngày. Thứ Năm tôi xem lại."

    "Anh rời đi, không nhanh cũng không chậm."

    "Huyền nhìn theo cho đến khi cánh cửa phòng họp khép lại."

    huyen frustrated "Anh ấy có thể nói một câu bình thường mà làm người khác thấy mình vừa phạm tội."

    tam smile "Ít nhất chưa có án tù."

    huyen irritated "Mày đứng về bên nào?"

    tam teasing "Bên muốn tan làm đúng giờ."

    "Tâm kéo laptop lại gần. Phần dữ liệu không sai. Vấn đề nằm ở cách hai người ghép yêu cầu của khách với kết quả thực tế."

    "Một lỗi nhỏ. Nhưng nếu không sửa, mọi con số đẹp phía sau đều trở nên vô nghĩa."

    menu:
        "Cùng Huyền chia lại toàn bộ tài liệu":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ story_add_direction("tam", "tam_support_huyen")
            $ story_flag("tam_c04_w01_tam_huyen_work_together")

            tam neutral "Chia đôi đi. Tao rà yêu cầu, mày kiểm lại dữ liệu. Xong rồi đổi cho nhau xem lần nữa."

            huyen confused "Đổi lần nữa?"

            tam smile "Để khỏi có hai người cùng hiểu sai một chỗ."

            huyen neutral "Nghe hợp lý một cách khó chịu."

            "Huyền kéo ghế sang gần hơn."

        "Dựng khung trước rồi để Huyền bổ sung dữ liệu":
            $ story_add("career_tam", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_c04_w01_tam_sets_work_structure")

            tam neutral "Để tao dựng lại khung đối chiếu trước. Mày đổ dữ liệu vào sau."

            huyen confused "Tách hẳn ra à?"

            tam neutral "Ừ. Ít nhất lúc sai sẽ biết sai từ khung hay từ số."

            huyen smile "Được. Nhưng nếu khung sai thì tao sẽ nhắc chuyện này đến cuối năm."

            tam teasing "Tao biết. Đó là lý do tao sẽ cố không sai."

        "Để Huyền phụ trách phần phải giải trình với Quân":
            $ story_add("career_huyen", 5)
            $ story_add("tam_observation", 5)
            $ story_add("huyen_quan_trust", 2)
            $ story_flag("tam_c04_w01_huyen_owns_client_mapping")

            tam neutral "Phần mapping mày nắm rõ hơn. Mày làm đầu mối đi."

            huyen shocked "Tại sao tự nhiên tao có cảm giác bị bán?"

            tam smile "Vì mày đang nhìn đúng người mua."

            huyen irritated "Tao sẽ nhớ chuyện này."

            tam teasing "Nhớ luôn yêu cầu khách hàng giúp tao."

    "Hai người bắt đầu làm."

    "Đến gần trưa, trên bàn có thêm hai cốc cà phê, ba bản in và một tờ giấy bị Huyền gạch mạnh đến rách góc."

    "Không ai nhắc đến việc đây chỉ là một tuần bình thường."

    return
