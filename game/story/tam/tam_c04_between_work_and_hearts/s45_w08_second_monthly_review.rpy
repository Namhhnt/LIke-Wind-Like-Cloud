# FILE: game/story/tam/tam_c04_between_work_and_hearts/s45_w08_second_monthly_review.rpy
# Week 08 — Second monthly work review.

label tam_c04_w08_s02_second_monthly_review:
    scene bg_meeting_room_day
    with dissolve

    scene cg_tam_c04_team_review
    with dissolve
    "Chiều thứ Ba, Quân đặt hai bản đánh giá xuống bàn."
    scene bg_meeting_room_day
    with dissolve

    "Lần này Huyền tự kéo bản của mình lại."

    quan neutral "Tháng trước tôi đánh giá cách hai em làm việc. Tháng này là cách hai em chịu trách nhiệm."

    "Anh nhìn Tâm trước."

    if story_has_flag("tam_c04_w06_tam_rejects_scope_change"):
        quan neutral "Em từ chối phần ngoài phạm vi đúng cách. Lập luận đủ, phương án thay thế rõ."
    elif story_has_flag("tam_c04_w06_tam_waits_for_quan_scope"):
        quan neutral "Em có kết luận nhưng chờ người khác xác nhận quá lâu. Lần tới chịu trách nhiệm cho đánh giá của mình."
    else:
        quan neutral "Em giữ được cấu trúc khi phạm vi thay đổi. Cần rõ hơn ở điểm quyết định cuối."

    "Sau đó anh chuyển sang Huyền."

    if story_has_flag("tam_c04_w07_tam_leaves_huyen_quan_agreement"):
        quan neutral "Em phản biện có căn cứ. Giữ cách đó."
    elif story_state.get("huyen_quan_trust", 0) >= 55:
        quan neutral "Em đã bớt phản ứng trước khi kiểm tra. Nhưng vẫn cần phân biệt tranh luận để làm tốt hơn và tranh luận để thắng."
    else:
        quan neutral "Em tiến bộ ở phần trình bày. Phần ổn định vẫn chưa đủ."

    menu:
        "Nhận thêm một đầu việc có quyền quyết định rõ":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_add("tam_observation", 3)
            $ story_add_direction("tam", "tam_career_focus")
            $ story_flag("tam_c04_w08_tam_accepts_decision_authority")

            tam neutral "Em muốn nhận một đầu việc có phạm vi quyết định rõ hơn."

            quan neutral "Tôi sẽ giao sau khi em hoàn tất bản hiện tại."

        "Đề nghị Tâm và Huyền review chéo theo vai trò ngang nhau":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 5)
            $ story_add("tam_self_clarity", 3)
            $ story_flag("tam_c04_w08_tam_huyen_peer_review")

            tam neutral "Bọn em có thể review chéo, nhưng không ai là người cứu phần của người kia."

            huyen neutral "Nghe hơi lạnh lùng."

            tam teasing "Nghe chuyên nghiệp."

            quan neutral "Làm thử trong tháng sau."

        "Để Huyền nhận buổi trình bày tiếp theo mà không có Tâm hỗ trợ trực tiếp":
            $ story_add("career_huyen", 10)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 3)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w08_huyen_gets_solo_presentation")

            tam neutral "Buổi tiếp theo Huyền có thể tự trình bày."

            huyen confused "Mày nói như thể tao không ngồi đây."

            tam smile "Vậy mày tự nói đi."

            huyen neutral "Em nhận."

            quan neutral "Được."

    "Quân ký vào góc dưới hai bản đánh giá."

    "Nét bút dứt khoát, không thêm lời động viên."

    "Nhưng khi đẩy giấy lại, anh đặt bản của Huyền ngay ngắn hơn lần trước."

    return
