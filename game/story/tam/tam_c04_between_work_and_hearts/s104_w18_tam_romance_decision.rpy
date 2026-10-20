# FILE: game/story/tam/tam_c04_between_work_and_hearts/s104_w18_tam_romance_decision.rpy

label tam_c04_w18_s02_tam_romance_decision:
    $ _hoang_ready = tam_c04_hoang_breakthrough_ready()
    $ _quang_ready = tam_c04_quang_tam_breakthrough_ready()
    scene bg_tam_room_morning
    with fade
    scene cg_tam_c04_decision_bed
    with dissolve
    "Tâm ngồi một mình ở mép giường. Chiếc điện thoại nằm úp bên cạnh."
    scene bg_tam_room_morning
    with dissolve
    "Không chọn cũng là một câu trả lời. Nhưng lần này cô muốn tự nói nó."
    menu:
        "Chọn Hoàng — thử bước vào một mối quan hệ nghiêm túc" if _hoang_ready:
            $ tam_c04_lock_tam_romance("hoang")
            $ story_add("tam_hoang_interest", 7)
            $ story_add("hoang_tam_trust", 7)
            $ story_sub("tam_insecurity", 5)
            $ story_flag("tam_c04_w18_tam_chooses_hoang")
        "Chọn Quang — làm rõ tình cảm giữa hai người" if _quang_ready:
            $ tam_c04_lock_tam_romance("quang")
            $ story_add("tam_quang_interest", 7)
            $ tam_c04_add_extended_score("quang_tam_awareness", 7)
            $ tam_c04_add_extended_score("quang_tam_warmth", 5)
            $ story_flag("tam_c04_w18_tam_chooses_quang")
        "Chọn độc lập — không bước vào tình cảm khi chưa thật sự muốn":
            $ tam_c04_lock_tam_romance("independent")
            $ story_add("career_tam", 10)
            $ story_add("tam_self_clarity", 10)
            $ story_flag("tam_c04_w18_tam_chooses_independent")
    return
