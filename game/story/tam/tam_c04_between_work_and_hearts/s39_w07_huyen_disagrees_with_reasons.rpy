# FILE: game/story/tam/tam_c04_between_work_and_hearts/s39_w07_huyen_disagrees_with_reasons.rpy
# Week 07 — Huyền disagrees with Quân using reasons instead of reflex.

label tam_c04_w07_s02_huyen_disagrees_with_reasons:
    scene bg_meeting_room_day
    with dissolve

    scene cg_tam_c04_huyen_presentation
    with dissolve
    "Chiều thứ Ba, Quân yêu cầu cắt phần trình bày của Huyền xuống còn một nửa."
    scene bg_meeting_room_day
    with dissolve

    huyen neutral "Em không đồng ý."

    "Căn phòng im rất ngắn."

    "Một tháng trước, câu đó sẽ đi kèm giọng cao hơn và lý do đến sau."

    "Lần này Huyền mở đúng trang dữ liệu."

    huyen neutral "Nếu cắt phần này, khách hàng sẽ thấy kết luận nhưng không thấy rủi ro. Em đề nghị giữ ba slide, bỏ phần ví dụ."

    "Quân nhìn màn hình."

    quan neutral "Ba slide vẫn dài."

    huyen neutral "Hai slide và một phụ lục."

    quan neutral "Được."

    "Huyền chớp mắt. Có lẽ cô đã chuẩn bị thêm ba câu phản biện."

    menu:
        "Không chen vào, để thỏa thuận thuộc về họ":
            $ story_add("career_huyen", 10)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 3)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w07_tam_leaves_huyen_quan_agreement")

            "Tâm giữ im lặng."

            "Huyền tự ghi lại quyết định. Quân chờ cô ghi xong mới chuyển sang mục khác."

        "Bổ sung dữ liệu để củng cố đề xuất của Huyền":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 5)
            $ story_add("huyen_quan_trust", 3)
            $ story_flag("tam_c04_w07_tam_supports_huyen_argument")

            tam neutral "Phụ lục có thể gửi trước cuộc họp. Như vậy hai slide chính đủ ngắn."

            quan neutral "Làm theo phương án đó."

            "Huyền gõ nhẹ đầu bút vào mép tài liệu, một cái cảm ơn không thành lời."

        "Sau họp hỏi Huyền có ngạc nhiên vì Quân nghe mình không":
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 5)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w07_tam_asks_huyen_quan_listened")

            tam neutral "Mày ngạc nhiên vì ổng nghe à?"

            huyen neutral "Tao ngạc nhiên vì ổng chịu thừa nhận tao có lý."

            tam teasing "Khác nhau chỗ nào?"

            huyen irritated "Rất nhiều."

    "Buổi họp kết thúc."

    "Huyền thu tài liệu. Trang cô vừa bảo vệ được đặt trên cùng."

    return
