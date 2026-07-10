# FILE: game/story/common/career/career_bonus_huyen_levels_01_04.rpy
# Huyền career decisions signed by Quân — first four levels.

label career_bonus_huyen_level_01_new_employee:
    scene bg_meeting_room_day
    with dissolve

    $ _career_bonus_title = career_bonus_current.get("title") or "Nhân viên mới"
    $ _career_bonus_salary = int(career_bonus_current.get("salary", 0) or 0)
    $ _career_bonus_salary_text = career_bonus_format_salary(_career_bonus_salary)

    "Tâm quay lại lấy điện thoại và thấy Huyền vẫn đứng trước bàn Quân."

    "Một tờ quyết định tiếp nhận nằm giữa hai người. Huyền cầm bút như đang cân nhắc ký hợp đồng đình chiến."

    quan neutral "Vị trí của em được ghi nhận là [_career_bonus_title]."

    if _career_bonus_salary > 0:
        quan neutral "Mức lương hiện tại là [_career_bonus_salary_text]."

    huyen confused "Em có được hỏi vì sao phần quy định dài hơn phần quyền lợi không ạ?"

    quan neutral "Được. Sau khi đọc hết phần quy định."

    "Huyền cúi xuống trang giấy, môi khẽ mím lại. Lần này cô đọc thật."

    huyen neutral "Em ký nhé. Nhưng nếu sau này phát hiện có chữ nhỏ quá thì em khiếu nại."

    quan neutral "Cỡ chữ mười hai."

    "Huyền ký tên. Chữ cuối hơi vọt lên, giống như vẫn muốn cãi thêm một câu."

    $ story_add("huyen_quan_trust", 1)
    $ story_flag("huyen_new_employee_decision_received_from_quan")

    return


label career_bonus_huyen_level_02_official_rank_1:
    scene bg_meeting_room_day
    with dissolve

    $ _career_bonus_title = career_bonus_current.get("title") or "Nhân viên chính thức — Rank 1"
    $ _career_bonus_salary = int(career_bonus_current.get("salary", 0) or 0)
    $ _career_bonus_salary_text = career_bonus_format_salary(_career_bonus_salary)

    "Khi Tâm bước vào, Huyền đang nhìn một tờ quyết định như thể nó vừa nói điều khó tin."

    quan neutral "Từ kỳ tới, chức danh của em là [_career_bonus_title]."

    if _career_bonus_salary > 0:
        quan neutral "Mức lương mới là [_career_bonus_salary_text]."

    huyen confused "Anh vừa nói liền hai câu tích cực đúng không ạ?"

    quan neutral "Tôi đang thông báo."

    huyen neutral "Em biết. Em chỉ xác nhận để lát nữa khỏi nghĩ mình nghe nhầm."

    "Quân đẩy cây bút về phía cô thêm một chút."

    quan neutral "Phần đối ngoại tiếp theo, em tự phụ trách. Tôi review lần cuối."

    "Huyền ký tên. Chữ cuối vẫn lệch lên trên, nhưng ít hơn lần trước."

    $ story_add("huyen_quan_trust", 2)
    $ story_flag("huyen_received_official_rank_1_from_quan")

    "Ra khỏi phòng, cô đi ngang Tâm với vẻ mặt tỉnh bơ."

    huyen neutral "Tối nay ăn gì đó đắt hơn bình thường đi."

    tam teasing "Mừng tăng lương à?"

    huyen irritated "Không. Mừng vì tao sống sót qua review."

    return


label career_bonus_huyen_level_03_official_rank_2:
    scene bg_meeting_room_day
    with dissolve

    $ _career_bonus_title = career_bonus_current.get("title") or "Nhân viên chính thức — Rank 2"
    $ _career_bonus_salary = int(career_bonus_current.get("salary", 0) or 0)
    $ _career_bonus_salary_text = career_bonus_format_salary(_career_bonus_salary)

    "Quân đặt một bản proposal cũ cạnh quyết định mới của Huyền. Những chỗ từng bị khoanh đỏ đã được sửa sạch."

    quan neutral "Em lên [_career_bonus_title]."

    if _career_bonus_salary > 0:
        quan neutral "Mức lương mới là [_career_bonus_salary_text]."

    quan neutral "Từ cấp này, em tự chốt cấu trúc trình bày và phân công phần đối ngoại."

    huyen neutral "Anh không xem outline trước à?"

    quan neutral "Em có thể gửi. Nhưng không cần chờ tôi cho phép mới làm tiếp."

    "Huyền đặt đầu bút xuống giấy rồi lại nhấc lên."

    huyen neutral "Nghe câu này từ anh hơi đáng sợ."

    quan neutral "Vì em quen bị nhắc hơn được tin."

    "Cô không đáp ngay. Nét ký đầu tiên hơi đậm hơn bình thường."

    $ story_add("huyen_quan_trust", 2)
    $ story_add("huyen_quan_interest", 1)
    $ story_flag("huyen_received_official_rank_2_from_quan")

    return


label career_bonus_huyen_level_04_official_rank_3:
    scene bg_meeting_room_day
    with dissolve

    $ _career_bonus_title = career_bonus_current.get("title") or "Nhân viên chính thức — Rank 3"
    $ _career_bonus_salary = int(career_bonus_current.get("salary", 0) or 0)
    $ _career_bonus_salary_text = career_bonus_format_salary(_career_bonus_salary)

    "Buổi họp kết thúc, nhưng Quân chưa đóng laptop. Anh lấy từ dưới tập hồ sơ một quyết định đã ký."

    quan neutral "Chức danh mới của em là [_career_bonus_title]."

    if _career_bonus_salary > 0:
        quan neutral "Mức lương mới là [_career_bonus_salary_text]."

    quan neutral "Những buổi trình bày quy mô nhỏ, em tự dẫn. Không cần tôi ngồi cạnh."

    huyen neutral "Nếu khách hàng hỏi khó thì sao?"

    quan neutral "Em trả lời. Nếu chưa biết, em nói chưa biết rồi kiểm tra lại."

    huyen teasing "Anh tin em dữ vậy?"

    "Quân nhìn cô qua mép màn hình."

    quan neutral "Quyết định có chữ ký của tôi."

    "Huyền im mất một nhịp. Câu đùa đã chuẩn bị sẵn không tìm được chỗ để đặt xuống."

    huyen neutral "Vâng. Em hiểu rồi."

    "Cô ký tên ngay phía trên chữ ký của anh. Lần này nét cuối nằm yên trên dòng."

    $ story_add("huyen_quan_trust", 3)
    $ story_add("huyen_quan_interest", 1)
    $ story_flag("huyen_received_official_rank_3_from_quan")

    return
