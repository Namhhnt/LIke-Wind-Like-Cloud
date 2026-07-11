# Week 09 — Tâm and Huyền work without using each other as a safety net.
label tam_c04_w09_s02_authority_without_shadow:
    scene bg_meeting_room_day
    with dissolve

    "Sáng thứ Ba, Quân đặt một bản phân công mới lên bàn."
    quan neutral "Tâm chịu trách nhiệm quyết định phạm vi. Huyền chịu trách nhiệm đầu ra đối ngoại. Hai em review chéo, không phê duyệt thay nhau."
    huyen neutral "Tức là nếu cô ấy sai, em không được cứu?"
    quan neutral "Em được chỉ ra. Người quyết định phải tự sửa."

    menu:
        "Nhận quyền quyết định và ghi rõ giới hạn của mình":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_add("tam_observation", 3)
            $ story_flag("tam_c04_w09_tam_accepts_authority_boundary")
            tam neutral "Em sẽ gửi decision log. Phần nào cần báo lên em sẽ ghi riêng."
            quan neutral "Được."

        "Đề nghị review chéo ở hai mốc cố định":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 5)
            $ story_add("tam_observation", 3)
            $ story_flag("tam_c04_w09_tam_huyen_fixed_peer_review")
            tam neutral "Bọn em review chéo giữa tuần và trước khi gửi. Ngoài hai mốc đó, ai giữ phần người đó."
            huyen neutral "Nghe như thỏa thuận không làm phiền nhau."
            tam teasing "Mày sẽ phá trước."

        "Để Huyền tự chọn cách trình bày với khách hàng":
            $ story_add("career_huyen", 10)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 2)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w09_huyen_owns_client_format")
            tam neutral "Phần trình bày để Huyền tự chọn format."
            huyen neutral "Tao đã chọn rồi."
            quan neutral "Vậy gửi trước năm giờ."

    "Quân rời phòng họp trước."
    "Huyền nhìn bản phân công một lúc rồi gấp đúng theo đường giữa."
    huyen neutral "Tự làm thật rồi đấy."
    tam neutral "Ừ."
    "Không ai nói câu đó với vẻ hoàn toàn vui."
    return
