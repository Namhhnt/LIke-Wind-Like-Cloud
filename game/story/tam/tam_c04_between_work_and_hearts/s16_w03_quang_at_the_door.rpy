# FILE: game/story/tam/tam_c04_between_work_and_hearts/s16_w03_quang_at_the_door.rpy
# Week 03 — Quang learns to stay near Thiên An without forcing his way in.

label tam_c04_w03_s05_quang_at_the_door:
    scene bg_tam_family_entry_evening
    with fade

    "Tối thứ Năm, Tâm về nhà muộn hơn thường lệ."

    "Quang đứng ngoài cổng, tay cầm một tập hồ sơ mỏng và chiếc ô Tâm đã để quên trên xe anh."

    tam confused "Anh chưa vào à?"

    quang "Chị An đang họp. Anh để hồ sơ rồi về."

    tam neutral "Anh đứng ngoài đây bao lâu rồi?"

    quang "Không lâu."

    "Câu trả lời cũ. Cách tránh cũ. Nhưng lần này anh không hỏi Tâm nên gọi Thiên An xuống hay không."

    "Anh chỉ đưa chiếc ô cho cô. Quai ô đã được buộc lại bằng nút cô vẫn dùng từ trước."

    menu:
        "Mở cổng, bảo Quang vào đợi trong nhà":
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_add("tam_observation", 3)
            $ story_flag("tam_c04_w03_tam_invites_quang_inside_for_thienan")

            tam neutral "Vào đi. Đứng ngoài này trông như anh tới đòi nợ."

            quang "Anh chỉ để hồ sơ thôi."

            tam teasing "Vậy để hồ sơ trong nhà. Ghế cũng ở trong nhà."

            "Quang nhìn cánh cổng đã mở rồi bước vào. Anh ngồi ở phòng khách, không gọi Thiên An, không nhắn thêm."

            "Khi cuộc họp kết thúc, Thiên An đi xuống và khựng lại rất nhẹ khi thấy anh."

        "Để Quang tự quyết định có chờ hay không":
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_c04_w03_tam_does_not_mediate_quang_waiting")
            $ story_flag("quang_thienan_stayed_by_choice")

            tam neutral "Em vào trước. Anh muốn đợi thì tự nói với chị ấy. Muốn về thì cũng tự về."

            quang "Em dứt khoát thật."

            tam neutral "Em mệt làm tổng đài rồi."

            "Tâm mở cổng, không giữ nó cho anh."

            "Vài phút sau, cô nghe tiếng bước chân Quang đi vào sân. Lần này quyết định không đi qua cô."

        "Nhận chiếc ô và hỏi vì sao Quang vẫn nhớ cách cô buộc":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 3)
            $ tam_c04_add_extended_score("quang_tam_awareness", 3)
            $ story_add("tam_observation", 5)
            $ story_add("quang_persistence", 3)
            $ story_flag("tam_c04_w03_tam_notices_quang_old_habit")
            $ story_flag("quang_tam_old_habit_noticed")

            tam neutral "Anh vẫn nhớ em buộc nút thế này à?"

            "Quang nhìn xuống quai ô."

            quang "Có gì khó nhớ đâu."

            tam teasing "Em đổi loại ô ba lần rồi."

            quang "Nhưng em vẫn buộc giống nhau."

            "Anh trả lời quá nhanh, rồi quay sang tập hồ sơ trong tay."

            quang "Anh vào đưa cái này cho chị An."

            "Tâm không chặn. Cũng không trêu thêm. Chiếc nút nhỏ nằm dưới ngón tay cô, chắc hơn mức cần thiết."

    "Cánh cửa chính không khép hẳn."

    "Ánh sáng từ phòng khách đổ ra sân một khoảng vừa đủ cho người đứng ngoài bước vào, nếu người đó tự chọn."

    return
