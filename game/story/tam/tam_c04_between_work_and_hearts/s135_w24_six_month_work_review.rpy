# FILE: game/story/tam/tam_c04_between_work_and_hearts/s135_w24_six_month_work_review.rpy

label tam_c04_w24_s02_six_month_work_review:
    scene bg_meeting_room_day
    with dissolve
    scene cg_tam_c04_final_review
    with dissolve
    "Quân đặt hai bản đánh giá trước Tâm và Huyền. Góc phải đều có chữ ký của anh."
    scene bg_meeting_room_day
    with dissolve
    quan neutral "Sáu tháng không đủ để chứng minh cô sẽ đi được bao xa. Đủ để biết cô có thể tự chịu trách nhiệm tới đâu."
    menu:
        "Tâm nhận quyền dẫn một workstream":
            $ story_add("career_tam", 15)
            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_c04_w24_tam_leads_workstream")
            tam neutral "Em nhận."
        "Huyền nhận quyền dẫn phần khách hàng":
            $ story_add("career_huyen", 15)
            $ story_add("huyen_quan_trust", 5)
            $ story_flag("tam_c04_w24_huyen_leads_client_track")
            huyen neutral "Anh đừng sửa deck sau lưng em."
            quan neutral "Đừng để tôi phải sửa."
        "Tâm và Huyền chia hai workstream ngang hàng":
            $ story_add("career_tam", 12)
            $ story_add("career_huyen", 12)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 7)
            $ story_flag("tam_c04_w24_tam_huyen_parallel_leads")
    return
