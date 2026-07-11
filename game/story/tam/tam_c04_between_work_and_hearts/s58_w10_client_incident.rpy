label tam_c04_w10_s02_client_incident:
    scene bg_meeting_room_day
    with dissolve
    "Mười giờ sáng, khách hàng yêu cầu đổi phần đã chốt và vẫn giữ nguyên thời hạn."
    quan neutral "Tôi cần một quyết định trước mười một giờ. Không cần một bản giải thích dài."
    "Tâm nhìn scope. Huyền nhìn slide."
    menu:
        "Từ chối phần thay đổi và đưa phương án thay thế":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_add("tam_observation", 3)
            $ story_flag("tam_c04_w10_tam_rejects_urgent_change")
            tam neutral "Mình giữ phần đã chốt. Em đề xuất đưa yêu cầu mới sang phase tiếp theo và thêm một mock tĩnh cho buổi demo."
            quan neutral "Gửi."
        "Chia lại phạm vi để Tâm và Huyền cùng cứu deadline":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 5)
            $ story_flag("tam_c04_w10_tam_huyen_share_incident")
            tam neutral "Em giữ scope. Huyền sửa cách kể để mock không bị nhìn như phần thiếu."
            huyen neutral "Cho tao bốn mươi phút."
        "Để Huyền trực tiếp thương lượng phần trình bày":
            $ story_add("career_huyen", 10)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 2)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w10_huyen_negotiates_incident")
            tam neutral "Phần khách hàng để Huyền nói."
            huyen neutral "Em sẽ không hứa thêm deliverable. Em chỉ đổi cách trình bày phần đang có."
            quan neutral "Đúng."
    "Mười giờ năm mươi tám, mail được gửi."
    "Không ai thở phào. Họ chỉ chuyển sang việc tiếp theo."
    return
