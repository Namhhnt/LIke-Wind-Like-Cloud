# FILE: game/story/tam/tam_c04_between_work_and_hearts/s28_w05_hoang_house_invitation.rpy
# Week 05 — Hoàng invites Tâm home without hiding the invitation inside an errand.

label tam_c04_w05_s03_hoang_house_invitation:
    $ _tam_c04_w05_hoang_active = (
        story_has_flag("tam_c04_m01_hoang_strong")
        or story_has_flag("tam_c04_m01_hoang_warm")
        or story_state.get("tam_hoang_interest", 0) >= 50
        or story_state.get("hoang_tam_trust", 0) >= 50
    )

    if not _tam_c04_w05_hoang_active:
        $ story_add("career_hoang", 5)
        $ story_add("hoang_self_acceptance", 3)
        $ story_flag("tam_c04_w05_hoang_house_invitation_skipped")
        return

    scene bg_company_lobby_afternoon
    with dissolve

    scene cg_tam_c04_hoang_lobby
    with dissolve
    "Chiều thứ Tư, Hoàng chờ Tâm ở sảnh với một chiếc chìa khóa xe trên tay."
    scene bg_company_lobby_afternoon
    with dissolve

    hoang neutral "Cuối tuần qua nhà anh ăn trưa không?"

    "Anh hỏi thẳng đến mức Tâm phải nhìn lại xem có túi đồ hay một cái cớ nào được đặt cạnh đó không."

    tam confused "Không cần em giúp mua gì à?"

    hoang smile "Không."

    tam neutral "Không có ai khác cần em tư vấn?"

    hoang teasing "Cũng không."

    "Hoàng xoay chiếc chìa khóa một vòng rồi giữ lại."

    hoang neutral "Anh chỉ muốn mời em tới."

    menu:
        "Nhận lời, nhưng hỏi Hoàng có căng thẳng không":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("hoang_tam_trust", 5)
            $ story_add("hoang_self_acceptance", 5)
            $ story_sub("tam_insecurity", 3)
            $ story_flag("tam_c04_w05_tam_accepts_hoang_house_invitation")

            tam neutral "Được. Nhưng anh đang căng thẳng đúng không?"

            hoang confused "Lộ vậy à?"

            tam teasing "Chìa khóa sắp bị anh xoay gãy rồi."

            "Hoàng nhìn xuống tay mình, rồi cất chìa khóa vào túi."

            hoang neutral "Vậy anh sẽ căng thẳng kín đáo hơn."

        "Trêu rằng lời mời này không còn đường lui":
            $ story_add("tam_hoang_interest", 5)
            $ story_add("tam_observation", 5)
            $ story_add("hoang_self_acceptance", 5)
            $ story_flag("tam_c04_w05_tam_notices_hoang_no_exit")

            tam teasing "Lần này anh không chuẩn bị câu nếu em bận thì thôi à?"

            hoang neutral "Nếu em bận, mình đổi ngày."

            tam neutral "Còn nếu em không muốn?"

            "Hoàng nhìn cô, không cười ngay."

            hoang neutral "Thì em nói không. Anh sẽ nghe."

            tam smile "Em không nói không."

        "Hẹn sau buổi review vì Tâm cần giữ nhịp công việc":
            $ story_add("hoang_tam_trust", 5)
            $ story_add("career_tam", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_c04_w05_tam_reschedules_hoang_house")

            tam neutral "Cuối tuần này em còn bản đầu. Chủ Nhật sau được không?"

            hoang neutral "Được. Anh ghi lịch."

            tam confused "Không thất vọng à?"

            hoang neutral "Có. Nhưng thất vọng không có nghĩa là phải làm em khó xử."

    "Cửa thang máy mở."

    "Hoàng không hỏi lại. Chỉ giữ cửa để Tâm bước vào trước."

    return
