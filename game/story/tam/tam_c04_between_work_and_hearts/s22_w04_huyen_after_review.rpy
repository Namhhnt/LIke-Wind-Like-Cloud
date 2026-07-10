# FILE: game/story/tam/tam_c04_between_work_and_hearts/s22_w04_huyen_after_review.rpy
# Week 04 — Huyền processes Quân's review through complaint, acceptance, and care.

label tam_c04_w04_s05_huyen_after_review:
    scene bg_company_open_office_day
    with dissolve

    "Sáng thứ Sáu, Huyền đặt bản đánh giá tháng dưới bàn phím."

    "Cô đã đọc nó đủ nhiều để nếp gấp giữa tờ giấy mềm hơn hai đầu."

    tam neutral "Mày định học thuộc à?"

    huyen irritated "Tao đang tìm chỗ ổng nói sai."

    tam teasing "Tìm được chưa?"

    huyen neutral "Có một chỗ dùng từ hơi quá."

    tam smile "Còn nội dung?"

    "Huyền im lặng."

    huyen frustrated "Đừng hỏi câu có đáp án khó chịu."

    "Quân đi qua, đặt một tập brief mới xuống bàn cô."

    quan neutral "Phần này em chịu chính. Thứ Hai gửi outline."

    huyen confused "Em ạ?"

    quan neutral "Có vấn đề?"

    huyen neutral "Không. Em làm được."

    "Quân gật đầu. Khi anh quay đi, Huyền lập tức mở tập brief."

    menu:
        "Ngồi xuống chia outline với Huyền":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ story_add("tam_self_clarity", 3)
            $ story_add_direction("tam", "tam_support_huyen")
            $ story_flag("tam_c04_w04_tam_helps_huyen_month_two_outline")

            tam neutral "Tao xem scope với mày. Phần quyết định cuối mày giữ."

            huyen neutral "Nói trước, tao không chia điểm ownership đâu."

            tam teasing "Mới được giao đã biết giữ quyền rồi. Tốt."

        "Để Huyền tự dựng outline":
            $ story_add("career_huyen", 5)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 1)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w04_tam_leaves_huyen_month_two_ownership")

            tam neutral "Mày tự làm đi. Lần này là phần của mày."

            huyen neutral "Tao biết."

            "Câu trả lời nhanh, nhưng không phòng thủ."

            "Huyền kéo một trang giấy trắng ra, viết tiêu đề đầu tiên trước khi mở lại tài liệu cũ."

        "Hỏi Huyền có vui vì được Quân tin không":
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 3)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w04_tam_asks_huyen_about_quan_trust")

            tam neutral "Mày vui vì được giao riêng à?"

            huyen irritated "Vui vì công việc."

            tam teasing "Tao có nói vì ai đâu."

            "Huyền nhìn cô rất lâu."

            huyen neutral "Ổng giao vì tao làm được. Thế thôi."

            tam smile "Ừ. Thế thôi."

            "Huyền cúi xuống brief. Tai cô hơi đỏ, hoặc có thể chỉ vì điều hòa sáng nay quá lạnh."

    "Đến giờ trưa, outline đã có sáu dòng."

    "Dòng thứ ba bị gạch đi rồi viết lại theo đúng cách Quân thường yêu cầu: vấn đề trước, giải pháp sau."

    "Huyền không nhận ra. Tâm không chỉ."

    return
