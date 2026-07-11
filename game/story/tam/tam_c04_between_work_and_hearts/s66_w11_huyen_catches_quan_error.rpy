label tam_c04_w11_s04_huyen_catches_quan_error:
    scene bg_company_open_office_day
    with dissolve
    "Chiều thứ Năm, Huyền phát hiện Quân ghi nhầm một con số trong bảng dự toán."
    "Cô nhìn màn hình ba giây, rồi sửa ở bản copy."
    huyen neutral "Anh Quân. Dòng mười bốn."
    "Quân kiểm tra."
    quan neutral "Ừ. Tôi ghi nhầm."
    huyen confused "Hết à?"
    quan neutral "Em muốn tôi tranh luận?"
    menu:
        "Để Huyền sửa và không trêu thêm":
            $ story_add("career_huyen", 10)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 5)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w11_huyen_quietly_fixes_quan_error")
            "Huyền lắc đầu rồi cập nhật file chung."
            "Lần đầu cô không tận dụng một lỗi của Quân để thắng một câu."
        "Nhắc Quân rằng Huyền vừa cứu một buổi review":
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 3)
            $ story_add("career_huyen", 5)
            $ story_flag("tam_c04_w11_tam_names_huyen_help")
            tam teasing "Anh nợ Huyền một lần không khoanh đỏ."
            quan neutral "Không quy đổi như vậy."
            huyen neutral "Em sẽ tự ghi sổ."
        "Cùng Huyền kiểm tra lại toàn bộ bảng":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 5)
            $ story_flag("tam_c04_w11_tam_huyen_recheck_quan_sheet")
            tam neutral "Tao kiểm tra nửa trên."
            huyen neutral "Đừng có tìm thêm lỗi để vui."
    "Quân nhận file mới mà không nói cảm ơn."
    "Mười phút sau, trên bàn Huyền có một cốc nước ấm cô không nhớ đã lấy."
    return
