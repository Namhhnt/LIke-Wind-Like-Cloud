# FILE: game/story/tam/tam_c04_between_work_and_hearts/s03_report_review.rpy
# Week 01 — First direct work collision between Huyền and Quân.

label tam_c04_w01_s03_report_review:
    scene bg_meeting_room_day
    with dissolve

    "Chiều thứ Năm, Quân xem bản báo cáo mới trong im lặng."

    "Huyền ngồi đối diện, hai tay đặt dưới bàn. Đầu ngón tay cô gõ nhẹ vào đầu gối, đều đến mức gần như có nhịp."

    "Quân dừng ở trang thứ sáu."

    quan neutral "Định nghĩa ở đây chưa thống nhất với trang hai."

    huyen irritated "Nhưng số liệu vẫn cùng một nguồn."

    quan neutral "Nguồn giống nhau không làm hai cách gọi trở thành một."

    huyen frustrated "Người đọc vẫn hiểu mà anh."

    quan neutral "Em đang dựa vào việc người đọc sẽ tự sửa phần em chưa làm rõ."

    "Căn phòng im đi."

    "Huyền ngồi thẳng hơn một chút."

    huyen irritated "Vậy anh muốn sửa theo cách nào?"

    quan neutral "Tôi muốn em giải thích cách em hiểu yêu cầu trước."

    "Câu trả lời nằm trong tài liệu. Nhưng Quân không hỏi tài liệu. Anh hỏi Huyền."

    "Tâm nhìn sang bạn mình."

    menu:
        "Cùng Huyền giải thích từng phần":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ story_add_direction("tam", "tam_support_huyen")
            $ story_flag("tam_c04_w01_tam_stays_in_quan_review")

            tam neutral "Bọn em tách yêu cầu thành hai lớp. Phần chức năng ở trang hai, phần kiểm chứng ở trang sáu."

            "Tâm kéo bản in về phía mình, đặt ngón tay vào hai dòng tương ứng."

            tam neutral "Lỗi là bọn em dùng hai tên khác nhau cho cùng một lớp dữ liệu."

            quan neutral "Vậy sửa tên hay sửa cấu trúc?"

            huyen neutral "Sửa cấu trúc. Nếu chỉ đổi tên thì lần sau vẫn có thể lệch."

            "Quân nhìn Huyền một giây rồi gật."

            quan neutral "Được. Làm lại phần đó."

        "Để Huyền tự trả lời":
            $ story_add("huyen_quan_trust", 5)
            $ story_add("career_huyen", 5)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w01_huyen_faces_quan_directly")
            $ story_flag("quan_noticed_huyen_persistence")

            "Tâm giữ tay trên mép tập tài liệu, không kéo nó về phía mình."

            "Huyền liếc sang cô. Tâm chỉ khẽ nghiêng đầu."

            huyen neutral "Em hiểu yêu cầu theo luồng người dùng, nên em gom phần kiểm chứng vào kết quả cuối."

            quan neutral "Và khách hàng đang đọc theo điều khoản nghiệm thu."

            huyen irritated "Nên họ sẽ không tự nối hai phần đó với nhau."

            quan neutral "Đúng."

            "Huyền im một nhịp."

            huyen neutral "Em sẽ tách lại theo điều khoản. Nhưng phần luồng người dùng em vẫn giữ."

            quan neutral "Nếu em chứng minh được nó cần thiết."

            huyen irritated "Em sẽ chứng minh."

            "Quân khép tập tài liệu."

            quan neutral "Tôi chờ."

        "Nhận phần sửa về mình để cuộc họp kết thúc sớm":
            $ story_add("career_tam", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_add("huyen_quan_trust", 2)
            $ story_flag("tam_c04_w01_tam_takes_report_rework")

            tam neutral "Phần cấu trúc để em sửa. Huyền kiểm lại dữ liệu sau."

            "Huyền quay sang. Cô không phản đối, nhưng bàn tay dưới bàn ngừng gõ."

            quan neutral "Được. Nhưng lần sau người phụ trách phần nào phải tự giải trình phần đó."

            tam neutral "Vâng."

    "Cuộc họp kết thúc sau đó mười phút."

    scene bg_company_lobby_afternoon
    with dissolve

    "Ra khỏi phòng, Huyền đi được vài bước rồi dừng lại cạnh máy nước."

    huyen frustrated "Tao không thích cách anh ấy nói chuyện."

    tam neutral "Ừ."

    huyen irritated "Nhưng chỗ đó... đúng là bọn mình viết chưa rõ."

    tam teasing "Mày có muốn tao giả vờ không nghe câu sau không?"

    huyen neutral "Có. Và nếu mày kể lại, tao sẽ phủ nhận."

    "Huyền bấm nút lấy nước. Chiếc cốc giấy rơi xuống hơi lệch, mắc lại ở mép máy."

    "Cô kéo nó ra, mạnh tay hơn cần thiết."

    "Tâm không nói thêm."

    return
