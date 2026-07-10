# FILE: game/story/tam/tam_c04_between_work_and_hearts/s04_quang_after_work.rpy
# Week 01 — Quang and Tâm speak with the familiarity of old family ties.

label tam_c04_w01_s04_quang_after_work:
    scene bg_company_lobby_afternoon
    with dissolve

    "Chiều hôm sau, Tâm gặp Quang ở sảnh công ty."

    "Anh đứng gần cửa kính, một tay cầm tập hồ sơ mỏng, tay kia giữ hai cốc nước."

    "Tâm nhìn hai cốc trước rồi mới nhìn anh."

    tam teasing "Anh định hối lộ ai vậy?"

    quang "Một cốc của anh. Một cốc chưa tìm được người nhận."

    tam neutral "Trà gừng, ít đường."

    quang "Ừ."

    tam teasing "Vậy là tìm được rồi còn gì."

    "Quang đưa cốc cho cô. Động tác tự nhiên như thể chuyện này đã lặp lại từ nhiều năm trước."

    quang "Dạo này chị An về nhà có muộn không?"

    tam neutral "Anh hỏi chị ấy chưa?"

    quang "Hỏi rồi."

    tam confused "Chị nói sao?"

    quang "Không sao."

    "Tâm thở ra."

    tam neutral "Vậy là có sao rồi."

    quang "Anh cũng nghĩ thế."

    "Anh đưa tập hồ sơ lên một chút."

    quang "Chị ấy để quên bản này. Anh định gửi người mang qua."

    tam teasing "Anh đứng đây mười phút chỉ để tìm người mang hộ à?"

    quang "Bảy phút."

    tam smile "Khác biệt rất lớn."

    "Quang nhìn cô, khóe miệng hơi động."

    quang "Em vẫn thích bắt bẻ người khác như trước."

    tam teasing "Em học từ người nhà."

    "Câu nói đi qua rất nhẹ. Quang không sửa chữ người nhà. Tâm cũng không."

    menu:
        "Khuyên Quang tự mang hồ sơ tới cho Thiên An":
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ tam_c04_add_extended_score("quang_thienan_resolve", 5)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w01_tam_supports_quang_thienan")
            $ story_flag("quang_thienan_direct_action")

            tam neutral "Anh tự mang qua đi."

            quang "Muộn rồi."

            tam teasing "Anh đứng đây thêm mười phút nữa thì cũng vẫn muộn."

            quang "Bảy phút."

            tam smile "Ừ. Bảy phút rất có nguyên tắc."

            "Quang nhìn tập hồ sơ, rồi cất điện thoại vào túi."

            quang "Anh đi đây."

            tam teasing "Nhớ đừng bảo em xúi."

            quang "Anh chưa bao giờ khai người nhà."

        "Nhận hồ sơ và chuyển giúp":
            $ story_add("tam_self_clarity", 5)
            $ story_add("thienan_quang_trust", 2)
            $ story_flag("tam_c04_w01_tam_carries_quang_file")

            tam neutral "Đưa em. Tối em ghé qua nhà."

            quang "Em còn việc không?"

            tam neutral "Còn. Nhưng em đi tiện hơn anh."

            "Quang không đưa ngay."

            tam teasing "Anh hỏi em giúp rồi lại không tin em à?"

            quang "Anh đang nghĩ có nên làm phiền em không."

            tam neutral "Anh nghĩ muộn rồi."

            "Lúc này anh mới đặt tập hồ sơ vào tay cô."

        "Trêu Quang vì vẫn vòng qua mình để hỏi Thiên An":
            $ story_add("tam_quang_interest", 5)
            $ tam_c04_add_extended_score("quang_tam_warmth", 3)
            $ tam_c04_add_extended_score("quang_tam_awareness", 2)
            $ story_add("tam_observation", 5)
            $ story_flag("tam_c04_w01_tam_notices_quang_familiarity")
            $ story_flag("quang_tam_familiarity_reframed")

            tam teasing "Anh lo cho chị An thì cứ nói là lo cho chị An. Sao lần nào cũng vòng qua em vậy?"

            quang "Vì em trả lời thật hơn chị ấy."

            tam neutral "Chỉ vậy thôi?"

            "Quang nhìn cô. Không né, nhưng cũng không trả lời ngay."

            quang "Với cả em dễ nói chuyện hơn."

            tam teasing "Câu này em sẽ lưu lại. Lần sau anh mà chê em phiền, em mở ra đối chứng."

            quang "Em đã phiền từ nhỏ. Hai chuyện không mâu thuẫn."

            "Tâm bật cười. Ly trà trong tay vẫn còn ấm."

    "Hai người tách nhau ở cửa thang máy."

    "Quang đi về phía bãi xe. Tâm đứng lại thêm một lúc, nhìn cốc trà đã được mua đúng vị mình vẫn uống."

    "Một việc quá quen đôi khi chỉ trở nên đáng chú ý khi người ta bỗng nhìn nó lâu hơn bình thường."

    return
