# FILE: game/story/tam/tam_c04_between_work_and_hearts/s09_w02_quang_stops_asking_around.rpy
# Week 02 — Quang acts directly with Thiên An, while Tâm notices what familiarity costs.

label tam_c04_w02_s04_quang_stops_asking_around:
    scene black
    with fade

    "Tối thứ Năm, Tâm ghé qua nhà."

    "Trên bàn ăn có một hộp giữ nhiệt màu xám. Nắp hộp được đặt lệch, như thể người mở đã quá mệt để vặn lại cho đúng ren."

    thienan tired "Anh Quang mang qua."

    tam teasing "Em chưa hỏi mà."

    thienan neutral "Mặt em hỏi."

    "Thiên An đẩy hộp canh về giữa bàn rồi tiếp tục xem tài liệu."

    tam neutral "Anh ấy tự mang à?"

    thienan neutral "Ừ. Còn đứng đó đến khi chị ăn được nửa bát mới chịu về."

    tam smile "Tiến bộ rồi. Không vòng qua em nữa."

    thienan confused "Hai đứa lại bày gì đấy?"

    tam neutral "Không có gì."

    "Thiên An nhìn cô một lúc, rõ ràng không tin, nhưng điện thoại trên bàn rung trước khi cô hỏi tiếp."

    "Tâm cầm hộp giữ nhiệt lên, thử vặn lại nắp. Ren bị lệch một vòng."

    "Quang vốn hiếm khi để những thứ nhỏ như vậy sai."

    "Có lẽ anh đã vội. Hoặc người làm anh vội không phải Tâm."

    menu:
        "Nhắn Quang rằng Thiên An đã ăn":
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ story_add("tam_observation", 3)
            $ story_flag("tam_c04_w02_tam_confirms_thienan_ate")

            tam neutral "Chị An ăn rồi. Anh yên tâm đi."

            "Quang trả lời sau chưa đầy một phút."

            quang "Ừ. Cảm ơn em."

            tam teasing "Lần sau tự hỏi chị ấy."

            quang "Anh đang tập."

            "Tâm nhìn hai chữ cuối thêm một lúc rồi tắt màn hình."

        "Không làm người trung gian nữa":
            $ story_add("thienan_quang_trust", 5)
            $ story_add("quang_persistence", 5)
            $ story_add("tam_self_clarity", 5)
            $ story_flag("tam_c04_w02_tam_refuses_middle_role")

            "Tâm đặt điện thoại úp xuống bàn."

            "Nếu Quang đã mang đồ đến, nếu Thiên An đã để anh đứng lại, thì phần còn lại nên thuộc về hai người."

            "Không phải sự im lặng nào cũng là bỏ mặc. Có lúc nó chỉ là trả lại một cuộc trò chuyện cho đúng người."

        "Chụp chiếc nắp bị lệch và trêu Quang":
            $ story_add("tam_quang_interest", 5)
            $ story_add("tam_observation", 5)
            $ story_add("quang_persistence", 3)
            $ story_flag("tam_c04_w02_tam_notices_quang_was_flustered")

            "Tâm chụp chiếc nắp hộp bị lệch."

            tam teasing "Anh mà cũng đóng lệch nắp à?"

            "Tin nhắn đã xem. Không có trả lời ngay."

            "Gần ba phút sau, Quang mới nhắn lại."

            quang "Anh vội."

            tam teasing "Em biết. Em đang tò mò vì ai thôi."

            quang "Em từ nhỏ đã tò mò quá mức cần thiết."

            "Anh đánh trống lảng rất cũ. Tâm nhận ra vì cô đã nghe nó từ lâu."

    "Thiên An gấp một góc tài liệu xuống. Lần này hơi lệch."

    "Tâm không sửa giúp."

    return
