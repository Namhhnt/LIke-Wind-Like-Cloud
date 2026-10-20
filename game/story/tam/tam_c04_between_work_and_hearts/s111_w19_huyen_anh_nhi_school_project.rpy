# FILE: game/story/tam/tam_c04_between_work_and_hearts/s111_w19_huyen_anh_nhi_school_project.rpy

label tam_c04_w19_s04_huyen_anh_nhi_school_project:
    scene bg_company_open_office_day
    with dissolve
    scene cg_tam_c04_school_bridge
    with dissolve
    "Ánh Nhi mang tới công ty một mô hình cầu bằng que gỗ. Một bên trụ bị lệch."
    scene bg_company_open_office_day
    with dissolve
    anhni "Bố cháu bảo để tối sửa. Nhưng tối nào bố cũng muộn."
    huyen neutral "Đưa cô xem."
    quan neutral "Cô còn việc."
    huyen neutral "Em biết. Cây cầu này cũng có deadline."
    menu:
        "Huyền sửa cùng Ánh Nhi":
            $ story_add("huyen_quan_trust", 7)
            $ story_add("huyen_quan_interest", 3)
            $ story_flag("tam_c04_w19_huyen_builds_bridge_with_anhni")
            "Quân đặt hộp keo xuống cạnh tay Huyền rồi quay lại bàn làm việc."
        "Tâm và Huyền chia nhau một người một nửa":
            $ story_add("career_tam", 3)
            $ story_add("career_huyen", 3)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 3)
            $ story_flag("tam_c04_w19_tam_huyen_help_anhni")
        "Để Quân tự về đúng giờ":
            $ story_add("huyen_quan_trust", 5)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w19_tam_pushes_quan_home")
            tam neutral "Anh về đi. File em gửi sau."
    return
