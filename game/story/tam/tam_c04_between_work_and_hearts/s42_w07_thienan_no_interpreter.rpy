# FILE: game/story/tam/tam_c04_between_work_and_hearts/s42_w07_thienan_no_interpreter.rpy
# Week 07 — Tâm refuses to interpret Thiên An for Quang.

label tam_c04_w07_s05_thienan_no_interpreter:
    scene black
    with dissolve

    "Tối thứ Năm, Thiên An để lại một tập tài liệu trên bàn khách."

    "Bên trong có hai dòng ghi chú dành cho Quang."

    "Dòng đầu sửa một con số."

    "Dòng sau viết: lần tới báo em trước khi tự đổi lịch."

    "Quang đọc xong, nhìn Tâm."

    quang "Chị em giận à?"

    tam neutral "Anh hỏi chị ấy đi."

    quang "Anh đang hỏi em."

    tam neutral "Em biết."

    menu:
        "Từ chối phiên dịch và bảo Quang gọi trực tiếp":
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_add_direction("quang", "quang_thienan_open")
            $ story_flag("tam_c04_w07_tam_refuses_to_interpret_thienan")

            tam neutral "Anh muốn biết thì gọi chị ấy. Đừng dùng em làm phụ đề nữa."

            "Quang nhìn hai dòng ghi chú."

            quang "Muộn rồi."

            tam neutral "Chị ấy còn thức."

            "Anh cầm điện thoại lên."

        "Nói Thiên An chỉ muốn được báo trước":
            $ story_add("thienan_quang_trust", 3)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 3)
            $ story_add("tam_observation", 3)
            $ story_flag("tam_c04_w07_tam_gives_quang_one_hint")

            tam neutral "Chị ấy không giận việc anh giúp. Chị ấy giận việc anh quyết định thay."

            quang "Khác nhau nhiều à?"

            tam neutral "Với chị An thì có."

        "Hỏi Quang vì sao anh vẫn nhìn Tâm để tìm câu trả lời":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 3)
            $ tam_c04_add_extended_score("quang_tam_awareness", 5)
            $ story_add("tam_observation", 5)
            $ story_add_direction("quang", "quang_tam_open")
            $ story_flag("tam_c04_w07_tam_asks_why_quang_looks_to_her")

            tam neutral "Sao chuyện của chị An mà anh vẫn nhìn em?"

            quang "Vì em thường biết."

            tam neutral "Hay vì nhìn em dễ hơn?"

            "Quang không trả lời ngay."

            quang "Có thể cả hai."

    return
