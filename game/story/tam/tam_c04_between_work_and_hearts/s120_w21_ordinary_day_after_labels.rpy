# FILE: game/story/tam/tam_c04_between_work_and_hearts/s120_w21_ordinary_day_after_labels.rpy

label tam_c04_w21_s02_ordinary_day_after_labels:
    scene black
    with dissolve
    if story_has_flag("tam_c04_tam_hoang_dating"):
        "Hoàng để một phần ăn trong tủ lạnh nhà mình và nhắn đúng một câu: 'Nếu em qua muộn, hâm ba phút.'"
        menu:
            "Báo Tâm sẽ qua":
                $ relationship_mark_contact("tam_hoang", "tam_c04_w21", source="story")
                $ story_add("hoang_tam_trust", 3)
                $ story_flag("tam_c04_w21_tam_goes_hoang_home")
            "Nói rõ hôm nay Tâm cần ở một mình":
                $ relationship_mark_contact("tam_hoang", "tam_c04_w21", source="story")
                $ story_add("tam_self_clarity", 5)
                $ story_flag("tam_c04_w21_tam_asks_space_cleanly")
            "Không trả lời":
                $ story_flag("tam_c04_w21_tam_ignores_hoang")
    elif story_has_flag("tam_c04_tam_quang_confirmed"):
        "Quang đặt hai chiếc cốc xuống bàn rồi khựng lại."
        quang "Anh vẫn vô thức mua ba phần."
        tam neutral "Sửa từ từ. Nhưng đừng sửa phần của em."
        $ story_add("tam_quang_interest", 5)
        $ tam_c04_add_extended_score("quang_tam_warmth", 5)
        $ story_flag("tam_c04_w21_quang_tam_new_habit")
    else:
        "Tâm nhận ra mình đã có thể tan làm sớm mà không cần tìm ai để lấp khoảng trống."
        $ story_add("career_tam", 7)
        $ story_add("tam_self_clarity", 5)
        $ story_flag("tam_c04_w21_independent_evening")
    return
