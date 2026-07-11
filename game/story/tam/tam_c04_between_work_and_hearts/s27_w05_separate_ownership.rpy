# FILE: game/story/tam/tam_c04_between_work_and_hearts/s27_w05_separate_ownership.rpy
# Week 05 — Tâm and Huyền begin Month 02 with separate ownership.

label tam_c04_w05_s02_separate_ownership:
    scene bg_meeting_room_day
    with dissolve

    "Sáng thứ Ba, Quân đặt hai tập brief ở hai phía khác nhau của bàn."

    quan neutral "Tháng này không còn một đầu việc chung."

    "Tập bên trái mang tên Tâm. Tập bên phải mang tên Huyền."

    huyen confused "Không còn chung hẳn ạ?"

    quan neutral "Hai em vẫn cùng dự án. Nhưng mỗi phần phải có một người chịu kết quả cuối."

    "Huyền kéo tập của mình lại gần. Tâm mở trang đầu tiên."

    "Khoảng trống giữa hai tập giấy không lớn. Nhưng đủ để không ai có thể đẩy lỗi sang phía còn lại."

    menu:
        "Nhận phần độc lập và tự đặt mốc review":
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 5)
            $ story_add("tam_observation", 3)
            $ story_add_direction("tam", "tam_career_focus")
            $ story_flag("tam_c04_w05_tam_sets_independent_milestones")

            tam neutral "Em sẽ gửi cấu trúc vào thứ Tư và bản đầu vào thứ Sáu. Chỉ cần review ở hai mốc đó."

            quan neutral "Được."

            "Quân không sửa lịch. Tâm ghi tên mình ở dòng phụ trách."

        "Đề nghị hai người review chéo trước khi gửi Quân":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ tam_c04_add_extended_score("tam_huyen_work_sync", 5)
            $ story_add("tam_self_clarity", 3)
            $ story_add_direction("tam", "tam_support_huyen")
            $ story_flag("tam_c04_w05_tam_huyen_cross_review")

            tam neutral "Bọn em tách ownership, nhưng review chéo trước khi gửi anh."

            huyen neutral "Tao bắt lỗi phần mày. Mày bắt lỗi phần tao."

            quan neutral "Review chéo không có nghĩa là sửa hộ."

            tam neutral "Bọn em hiểu."

        "Để Huyền tự trình bày cách cô sẽ làm":
            $ story_add("career_huyen", 10)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 2)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w05_tam_gives_huyen_the_floor")

            tam neutral "Phần của Huyền, để Huyền nói trước đi."

            "Huyền nhìn cô một nhịp, rồi xoay brief về phía Quân."

            huyen neutral "Em chia ba mốc. Mốc đầu em tự làm, mốc hai cần dữ liệu từ Tâm, mốc cuối em chịu trình bày."

            quan neutral "Tiếp tục."

            "Huyền nói hết mà không nhìn Tâm để tìm câu tiếp theo."

    "Khi cuộc họp kết thúc, Huyền ôm tập brief vào ngực."

    huyen neutral "Tự nhiên thấy bàn làm việc rộng hơn."

    tam teasing "Mày có thể trả tao nửa chỗ để cốc."

    huyen irritated "Không liên quan."

    return
