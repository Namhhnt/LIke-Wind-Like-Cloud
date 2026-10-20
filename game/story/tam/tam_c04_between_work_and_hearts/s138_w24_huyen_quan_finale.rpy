# FILE: game/story/tam/tam_c04_between_work_and_hearts/s138_w24_huyen_quan_finale.rpy

label tam_c04_w24_s05_huyen_quan_finale:
    scene bg_c04_quan_home_night
    with dissolve
    "Quân về nhà lúc gần nửa đêm. Đèn phòng khách còn sáng. Ánh Nhi ngủ trên sofa, đầu gối lên chân Huyền."
    "Huyền vẫn cầm laptop, nhưng màn hình đã tối."
    quan neutral "Cô có thể đánh thức con bé rồi về."
    huyen tired "Anh nói nhỏ thôi."
    scene cg_tam_c04_sleeping_blanket
    with dissolve
    "Quân lấy chiếc chăn mỏng phủ lên Ánh Nhi."
    scene bg_c04_quan_home_night
    with dissolve
    if tam_c04_huyen_quan_deep_trust_ready():
        $ tam_c04_commit_huyen_quan_deep_trust()
        $ story_add("huyen_quan_trust", 7)
        $ story_add("huyen_quan_interest", 3)
        $ story_flag("tam_c04_final_huyen_quan_home_trust")
        quan neutral "Cảm ơn cô. Không chỉ vì công việc."
        huyen neutral "Em biết."
    else:
        $ story_add("career_huyen", 7)
        $ story_flag("tam_c04_final_huyen_quan_professional_trust")
        quan neutral "Bản gửi khách hàng tốt."
        huyen neutral "Em biết. Cái đó anh có thể nói ở công ty."
    return
