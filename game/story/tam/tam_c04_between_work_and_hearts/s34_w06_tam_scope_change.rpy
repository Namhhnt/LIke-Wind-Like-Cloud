# FILE: game/story/tam/tam_c04_between_work_and_hearts/s34_w06_tam_scope_change.rpy
# Week 06 — Tâm's independent brief receives an unexpected scope change.

label tam_c04_w06_s03_tam_scope_change:
    scene bg_meeting_room_day
    with dissolve

    scene cg_tam_c04_tam_work_day
    with dissolve
    "Chiều thứ Tư, khách hàng gửi một yêu cầu mới."
    scene bg_company_open_office_day
    with dissolve

    "Nếu nhận, toàn bộ cấu trúc Tâm đã dựng từ đầu tuần phải đổi."

    "Quân vẫn chưa về công ty. Tin nhắn của anh chỉ có một dòng: em đánh giá trước, chiều mai báo tôi quyết định."

    "Tâm đọc lại câu đó."

    "Không phải hỏi ý kiến. Là yêu cầu cô đưa ra ý kiến."

    menu:
        "Tự đánh giá và từ chối phần ngoài phạm vi":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_add("tam_observation", 5)
            $ story_add_direction("tam", "tam_career_focus")
            $ story_flag("tam_c04_w06_tam_rejects_scope_change")

            "Tâm viết ba lý do, đính kèm ảnh hưởng tiến độ và đề xuất một phase riêng."

            "Cô đọc lại một lần rồi gửi."

            "Không thêm câu xin lỗi ở đầu."

        "Hỏi Huyền cách cô sẽ phản hồi khách hàng":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 5)
            $ story_add("tam_self_clarity", 3)
            $ story_flag("tam_c04_w06_tam_asks_huyen_scope")

            tam neutral "Nếu là mày, mày trả lời sao?"

            huyen neutral "Tao hỏi họ muốn đổi mục tiêu hay chỉ muốn thêm việc mà không đổi tiền."

            tam smile "Câu sau bỏ đi."

            huyen teasing "Nhưng ý giữ lại."

        "Chờ Quân về rồi mới quyết định":
            $ story_add("career_tam", 3)
            $ story_add("tam_observation", 3)
            $ story_add("huyen_quan_trust", 3)
            $ story_flag("tam_c04_w06_tam_waits_for_quan_scope")

            "Tâm soạn sẵn hai phương án nhưng chưa gửi."

            "Sáng hôm sau, Quân xem chúng trong ba phút."

            quan neutral "Em đã có kết luận rồi. Lần sau gửi trước."

            "Tâm gật đầu. Câu nhận xét ngắn hơn phần cô đã chờ."

    return
