# FILE: game/story/tam/tam_c04_between_work_and_hearts/s121_w21_quan_second_trip_request.rpy

label tam_c04_w21_s03_quan_second_trip_request:
    scene bg_company_open_office_day
    with dissolve
    scene cg_tam_c04_huyen_quan_work
    with dissolve
    "Quân thông báo chuyến công tác kéo dài mười ngày."
    scene bg_company_open_office_day
    with dissolve
    quan neutral "Ánh Nhi có thể ở nhà tôi. Cô chỉ cần ghé buổi tối. Hoặc ở nhà cô cuối tuần nếu tiện."
    huyen neutral "Anh đã hỏi con bé chưa?"
    quan neutral "Nó hỏi trước tôi."
    menu:
        "Huyền nhận chăm Ánh Nhi":
            $ tam_c04_commit_huyen_quan_deep_trust()
            $ story_add("huyen_quan_trust", 7)
            $ story_add("huyen_quan_interest", 3)
            $ story_flag("tam_c04_w21_huyen_accepts_anhni_ten_days")
            huyen neutral "Gửi em thuốc, lịch học và số của giáo viên."
            quan neutral "Trong mail rồi."
        "Huyền nhận nhưng yêu cầu Quân gọi cho con mỗi tối":
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 5)
            $ story_flag("tam_c04_w21_huyen_sets_quan_call_rule")
            huyen neutral "Anh bận vẫn phải gọi. Đừng để con bé chỉ nhận ảnh sân bay."
        "Huyền từ chối phần gia đình, nhận thay việc ở công ty":
            $ story_add("career_huyen", 10)
            $ story_add("huyen_quan_trust", 3)
            $ story_flag("tam_c04_w21_huyen_professional_only")
    return
