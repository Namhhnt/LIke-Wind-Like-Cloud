# FILE: game/story/tam/tam_c04_between_work_and_hearts/s117_w20_huyen_quan_or_hoang_seed_check.rpy

label tam_c04_w20_s04_huyen_quan_or_hoang_seed_check:
    scene bg_company_open_office_day
    with dissolve

    $ _m05_hq_push = tam_c04_get_huyen_quan_push_score("m05")

    if tam_c04_huyen_quan_deep_trust_ready() and _m05_hq_push >= 2:
        scene cg_tam_c04_huyen_quan_work
        with dissolve
        "Quân đưa Huyền lịch công tác tháng sau và lịch học của Ánh Nhi trong cùng một email."
        scene bg_company_open_office_day
        with dissolve
        huyen neutral "Anh gộp hai file này làm gì?"
        quan neutral "Vì cả hai đều liên quan tới cô."
        menu:
            "Huyền nhận trách nhiệm mà không đùa":
                $ tam_c04_commit_huyen_quan_deep_trust()
                $ story_add("huyen_quan_trust", 7)
                $ story_add("huyen_quan_interest", 3)
                $ story_flag("tam_c04_w20_huyen_accepts_deep_trust")
                huyen neutral "Em sẽ sắp xếp."
            "Huyền chỉ nhận phần công việc":
                $ story_add("career_huyen", 7)
                $ story_add("huyen_quan_trust", 3)
                $ story_flag("tam_c04_w20_huyen_keeps_professional_boundary")
    elif not story_has_flag("tam_c04_tam_hoang_dating"):
        "Hoàng ghé công ty trả Quân một tập mẫu. Đến lúc anh xuống sảnh, Huyền vẫn đang đứng cạnh máy in với bản thiết kế khách hàng vừa trả lại."
        hoang neutral "Quân lại bắt cô sửa phần này à?"
        huyen neutral "Anh hỏi như thể chưa từng đứng cùng phe với anh ấy."
        hoang neutral "Tôi đứng cùng phe với bản nào đỡ phải sửa lần ba."
        scene cg_tam_c04_huyen_hoang_office
        with dissolve
        "Huyền nhìn anh, rồi đẩy một bản in sang."
        scene bg_company_open_office_day
        with dissolve
        huyen neutral "Vậy xem thử đi."
        $ tam_c04_add_extended_score("huyen_hoang_interest", 3)
        $ tam_c04_add_extended_score("hoang_huyen_interest", 3)
        $ story_flag("tam_c04_w20_huyen_hoang_friend_lane_visible")

        if story_state.get("huyen_quan_trust", 0) >= 60:
            "Mười phút sau Quân quay lại. Anh không hỏi vì sao Hoàng còn ở đó, chỉ kéo ghế ngồi xuống đầu bàn."
            "Ba người tiếp tục nói về bản thiết kế như thể cuộc tranh luận ấy đã có chỗ sẵn từ trước."
            $ story_add("huyen_quan_trust", 2)
            $ story_flag("tam_c04_w20_huyen_routes_cross_develop")
    else:
        "Quân giao Huyền phần review mới. Hoàng chỉ ghé qua chào cả hai rồi rời đi trước."
        $ story_add("huyen_quan_trust", 3)
        $ story_flag("tam_c04_w20_huyen_hoang_friendship_only")

    return
