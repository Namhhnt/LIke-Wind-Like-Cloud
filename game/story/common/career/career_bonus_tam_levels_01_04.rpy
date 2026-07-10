# FILE: game/story/common/career/career_bonus_tam_levels_01_04.rpy
# Tâm career decisions signed by Quân — first four levels.

label career_bonus_tam_level_01_new_employee:
    scene bg_meeting_room_day
    with dissolve

    $ _career_bonus_title = career_bonus_current.get("title") or "Nhân viên mới"
    $ _career_bonus_salary = int(career_bonus_current.get("salary", 0) or 0)
    $ _career_bonus_salary_text = career_bonus_format_salary(_career_bonus_salary)

    "Sau buổi hướng dẫn cuối ngày, Quân gọi Tâm quay lại phòng họp."

    "Trên bàn là một tờ quyết định tiếp nhận. Dòng chữ ở giữa trang ngắn hơn cô tưởng."

    quan neutral "Thông tin thử việc và phạm vi công việc đã được cập nhật."
    quan neutral "Từ hôm nay, vị trí của em là [_career_bonus_title]."

    if _career_bonus_salary > 0:
        quan neutral "Mức lương hiện tại là [_career_bonus_salary_text]."

    "Quân xoay cây bút về phía cô. Phần chữ ký của anh đã nằm sẵn ở cuối trang."

    menu:
        "Đọc lại từng điều khoản trước khi ký":
            $ story_add("tam_observation", 2)
            $ story_flag("tam_read_new_employee_decision_carefully")

            tam neutral "Em xin đọc lại một lượt trước ạ."

            quan neutral "Ừ. Không cần ký nhanh để tỏ ra mình đã hiểu."

            "Tâm dừng ở mục trách nhiệm lâu hơn những mục khác. Quân không giục."

        "Ký rồi hỏi công việc đầu tiên":
            $ story_add("tam_self_clarity", 2)
            $ story_flag("tam_accepted_new_employee_role_directly")

            tam neutral "Việc đầu tiên em cần hoàn thành là gì ạ?"

            quan neutral "Đọc hết quyết định đã."

            "Tâm nhìn xuống trang giấy, khẽ kéo cây bút trở lại gần mình."

    "Cô ký tên. Nét cuối còn hơi cứng, nhưng không lệch khỏi dòng."

    return


label career_bonus_tam_level_02_official_rank_1:
    scene bg_meeting_room_day
    with dissolve

    $ _career_bonus_title = career_bonus_current.get("title") or "Nhân viên chính thức — Rank 1"
    $ _career_bonus_salary = int(career_bonus_current.get("salary", 0) or 0)
    $ _career_bonus_salary_text = career_bonus_format_salary(_career_bonus_salary)

    "Quân giữ Tâm lại sau buổi review. Chiếc ghế đối diện anh đã được kéo ra sẵn."

    "Trên bàn là quyết định xác nhận nhân viên chính thức. Góc phải có một dấu mực còn mới."

    quan neutral "Kết quả hiện tại đủ để kết thúc giai đoạn nhân viên mới."
    quan neutral "Chức danh mới là [_career_bonus_title]."

    if _career_bonus_salary > 0:
        quan neutral "Mức lương mới là [_career_bonus_salary_text], áp dụng từ kỳ kế tiếp."

    menu:
        "Nhận trách nhiệm mới":
            $ story_add("tam_self_clarity", 2)
            $ story_flag("tam_accepted_official_rank_1_responsibility")

            tam neutral "Em nhận. Phần việc mới bắt đầu từ thứ Hai đúng không ạ?"

            quan neutral "Từ thứ Hai."

            tam smile "Vậy em còn cuối tuần để lo."

            quan neutral "Lo vừa đủ thôi."

        "Hỏi rõ phạm vi trước khi nhận":
            $ story_add("tam_observation", 2)
            $ story_flag("tam_clarified_official_rank_1_scope")

            tam neutral "Em muốn xem lại phần nào em được tự quyết, phần nào vẫn cần anh duyệt."

            quan neutral "Đúng câu cần hỏi. Bản phân quyền nằm trong mail."

            tam confused "Anh gửi từ lúc nào vậy?"

            quan neutral "Sáu giờ mười hai."

    "Tâm gấp quyết định lại. Lần này mép giấy khớp đúng với đường in."

    return


label career_bonus_tam_level_03_official_rank_2:
    scene bg_meeting_room_day
    with dissolve

    $ _career_bonus_title = career_bonus_current.get("title") or "Nhân viên chính thức — Rank 2"
    $ _career_bonus_salary = int(career_bonus_current.get("salary", 0) or 0)
    $ _career_bonus_salary_text = career_bonus_format_salary(_career_bonus_salary)

    "Quân đặt trước mặt Tâm hai tập tài liệu: một bản đánh giá và một hồ sơ dự án chưa có tên người phụ trách."

    quan neutral "Quyết định này nâng em lên [_career_bonus_title]."

    if _career_bonus_salary > 0:
        quan neutral "Mức lương mới là [_career_bonus_salary_text]."

    "Anh chạm đầu ngón tay lên tập hồ sơ thứ hai."

    quan neutral "Từ cấp này, em không chỉ chịu trách nhiệm cho phần mình làm."
    quan neutral "Em sẽ review đầu ra của người khác trước khi chuyển lên tôi."

    menu:
        "Nhận dự án nhưng đề nghị một lần review chung":
            $ story_add("tam_observation", 2)
            $ story_flag("tam_requested_first_rank_2_joint_review")

            tam neutral "Dự án đầu tiên, em muốn anh review cùng em một lần. Sau đó em tự làm."

            quan neutral "Được. Một lần."

            tam neutral "Vâng. Một lần là đủ."

        "Nhận toàn bộ quyền review":
            $ story_add("tam_self_clarity", 2)
            $ story_flag("tam_accepted_rank_2_review_authority")

            tam neutral "Em hiểu. Em sẽ chịu trách nhiệm cho bản cuối trước khi gửi anh."

            quan neutral "Đừng biến chịu trách nhiệm thành tự làm hết."

            "Tâm dừng tay trên mép hồ sơ. Câu nhắc ấy đến đúng chỗ cô thường không nhận ra."

    "Quân ký thêm một nét xác nhận ở cuối quyết định rồi đẩy cả hai tập giấy sang phía cô."

    return


label career_bonus_tam_level_04_official_rank_3:
    scene bg_meeting_room_day
    with dissolve

    $ _career_bonus_title = career_bonus_current.get("title") or "Nhân viên chính thức — Rank 3"
    $ _career_bonus_salary = int(career_bonus_current.get("salary", 0) or 0)
    $ _career_bonus_salary_text = career_bonus_format_salary(_career_bonus_salary)

    "Cuộc họp đã tan gần hết. Quân vẫn để một tờ quyết định úp xuống cạnh laptop."

    "Khi Tâm ngồi lại, anh mới lật nó lên."

    quan neutral "Từ kỳ này, em lên [_career_bonus_title]."

    if _career_bonus_salary > 0:
        quan neutral "Mức lương mới là [_career_bonus_salary_text]."

    quan neutral "Các đầu việc trong nhóm nhỏ có thể dừng ở chữ ký của em trước khi tới tôi."

    tam neutral "Nếu em ký sai thì sao?"

    quan neutral "Thì em sửa. Quyền quyết định không làm người ta hết sai."

    menu:
        "Hỏi điều Quân vẫn chưa yên tâm":
            $ story_add("tam_observation", 2)
            $ story_flag("tam_asked_quan_rank_3_remaining_concern")

            tam neutral "Còn điểm nào khiến anh chưa yên tâm khi giao quyền này cho em không?"

            quan neutral "Có. Em vẫn hay giữ việc quá lâu trước khi nhờ người khác."

            tam neutral "Em biết rồi."

            quan neutral "Biết chưa đủ. Nhưng là chỗ bắt đầu được."

        "Nhận quyền ký và giới hạn của nó":
            $ story_add("tam_self_clarity", 2)
            $ story_flag("tam_accepted_rank_3_signoff_scope")

            tam neutral "Em nhận phần quyền này. Những việc vượt phạm vi, em sẽ không tự đoán."

            quan neutral "Tốt. Tự tin không có nghĩa là ký vào mọi thứ."

    "Tâm cầm quyết định lên. Chữ ký của Quân nằm dưới cùng; khoảng trống dành cho cô ở ngay phía trên."

    "Cô ký, rồi đặt bút xuống trước khi mực kịp lem."

    return
