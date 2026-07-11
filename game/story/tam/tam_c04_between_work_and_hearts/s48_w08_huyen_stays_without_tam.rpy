# FILE: game/story/tam/tam_c04_between_work_and_hearts/s48_w08_huyen_stays_without_tam.rpy
# Week 08 — Huyền stays to review with Quân without using Tâm as cover.

label tam_c04_w08_s05_huyen_stays_without_tam:
    scene bg_company_open_office_day
    with dissolve

    "Thứ Sáu, sáu giờ."

    "Tâm thu laptop vào túi."

    "Huyền vẫn ngồi trước bản trình bày tháng sau."

    "Quân từ phòng họp bước ra, dừng cạnh bàn cô."

    quan neutral "Em còn ba slide chưa chốt."

    huyen neutral "Em biết. Em muốn sửa xong tối nay."

    quan neutral "Tôi xem bản cuối trước khi về."

    "Huyền nhìn Tâm."

    "Không phải cầu cứu. Chỉ là một thói quen cũ hỏi xem Tâm có ở lại không."

    menu:
        "Rời đi, để Huyền và Quân tự làm việc":
            $ story_add("career_huyen", 10)
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 5)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w08_tam_leaves_huyen_quan_alone")

            tam neutral "Tao về trước."

            huyen neutral "Ừ."

            "Cô trả lời ngay."

            "Tâm đi tới cửa. Khi quay lại, Huyền đã kéo ghế sang phía màn hình để Quân nhìn rõ hơn."

        "Ở lại nhưng làm phần việc riêng":
            $ story_add("career_tam", 5)
            $ story_add("career_huyen", 5)
            $ story_add("huyen_quan_trust", 3)
            $ story_add("tam_self_clarity", 3)
            $ story_flag("tam_c04_w08_tam_stays_without_interfering")

            tam neutral "Tao ngồi góc kia làm phần tao. Có gì tự hỏi anh Quân."

            huyen neutral "Biết rồi."

            "Tâm đeo tai nghe."

            "Qua lớp kính, cô thấy Huyền phản biện một câu rồi tự sửa một câu khác."

        "Trêu Huyền rằng cô không còn cần Tâm ngồi cạnh":
            $ story_add("huyen_quan_trust", 5)
            $ story_add("huyen_quan_interest", 5)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w08_tam_teases_huyen_no_cover")

            tam teasing "Giờ mày không cần tao ngồi làm bình phong nữa nhỉ."

            huyen irritated "Tao chưa bao giờ cần."

            tam smile "Ừ."

            "Huyền quay lại màn hình quá nhanh."

    "Cửa thang máy khép lại sau lưng Tâm."

    "Trên tầng, một chiếc ghế trống cạnh Huyền không còn khiến cô kéo thêm ghế khác vào lấp."

    return
