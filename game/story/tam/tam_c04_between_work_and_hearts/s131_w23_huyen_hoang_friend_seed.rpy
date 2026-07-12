# FILE: game/story/tam/tam_c04_between_work_and_hearts/s131_w23_huyen_hoang_friend_seed.rpy

label tam_c04_w23_s03_huyen_hoang_friend_seed:
    if story_has_flag("tam_c04_tam_hoang_dating"):
        return

    scene black
    with dissolve

    "Sau bữa tối, Tâm đưa Ánh Nhi vào nhà vệ sinh. Huyền và Hoàng đứng lại ngoài hành lang."
    hoang neutral "Cô chăm con bé khá quen rồi."
    huyen neutral "Anh nói như tôi vừa lên chức bảo mẫu."
    hoang neutral "Tôi định nói cô hợp với việc người khác tin cô."
    "Huyền im một nhịp, rồi kéo lại quai cặp của Ánh Nhi đang cầm hộ."

    $ _hh_visible = (
        story_state.get("huyen_hoang_interest", 0) >= 15
        and story_state.get("hoang_huyen_interest", 0) >= 15
    )
    $ _hq_personal = story_state.get("huyen_quan_interest", 0) >= 25

    if _hh_visible:
        $ tam_c04_add_extended_score("huyen_hoang_interest", 5)
        $ tam_c04_add_extended_score("hoang_huyen_interest", 5)
        $ story_flag("tam_c04_w23_huyen_hoang_easy_friend_seed")
        huyen neutral "Anh nói được câu tử tế mà không cười à?"
        hoang neutral "Hiếm. Cô nên ghi lại."

        if _hq_personal:
            "Cửa phòng làm việc mở ra. Quân gọi tên Huyền để hỏi lịch sáng mai."
            "Cô quay lại đáp, nhưng vẫn giữ chiếc cặp của Ánh Nhi trong tay."
            $ story_add("huyen_quan_interest", 2)
            $ story_flag("tam_c04_w23_huyen_routes_both_visible")
    elif _hq_personal:
        $ story_add("huyen_quan_interest", 3)
        $ story_flag("tam_c04_w23_huyen_keeps_quan_lane")
        huyen neutral "Có người giao chìa khóa rồi biến đi mười ngày. Không quen cũng phải quen."
    else:
        $ tam_c04_add_extended_score("huyen_hoang_interest", 3)
        $ tam_c04_add_extended_score("hoang_huyen_interest", 3)
        $ story_flag("tam_c04_w23_huyen_hoang_interest_starts_showing")
        huyen neutral "Đừng nói kiểu đó. Nghe hơi đáng ngờ."
        hoang neutral "Tôi tưởng cô quen nghi người rồi."

    return
