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
    if story_state.get("huyen_quan_interest", 0) < 25:
        $ tam_c04_seed_huyen_hoang_if_eligible()
        $ story_add("huyen_hoang_interest", 5)
        $ story_add("hoang_huyen_interest", 5)
        $ story_flag("tam_c04_w23_huyen_hoang_easy_friend_seed")
        huyen neutral "Anh nói được câu tử tế mà không cười à?"
        hoang neutral "Hiếm. Cô nên ghi lại."
    else:
        $ story_add("huyen_quan_interest", 3)
        $ story_flag("tam_c04_w23_huyen_keeps_quan_lane")
        huyen neutral "Có người giao chìa khóa rồi biến đi mười ngày. Không quen cũng phải quen."
    return
